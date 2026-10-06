"""
Data periodik (harian / mingguan / bulanan) dari JSON baru. Menggantikan content/dynamic_loader.py.

File: content/interpretations/<sistem>/{daily,weekly,monthly}.json  (list of record, 1 record per kombinasi kunci)
Tiap record dipilih lewat kunci yang DIHITUNG dari kalender (bukan acak, bukan hash):

  sistem      periode   kunci record
  Zodiak      harian    tanda user + rumah transit Bulan (1-12)
  Zodiak      mingguan  tanda user + fase Bulan pada Senin minggu itu
  Zodiak      bulanan   tanda user + rumah transit Matahari pada tgl 15
  Shio        harian    shio user + elemen hari (batang langit pilar hari)
  Shio        bulanan   shio user + shio bulan Tionghoa pada tgl 15
  Weton       harian    weton user + pasaran hari ini
  Weton       mingguan  weton user + fase Bulan pada Senin minggu itu
  Shio        mingguan  shio user + fase Bulan pada Senin minggu itu
  Numerologi  harian    personal month + personal day (butuh tanggal lahir)
  Numerologi  mingguan  personal month (bulan Senin itu) + fase Bulan pada Senin
  Numerologi  bulanan   personal year + personal month (butuh tanggal lahir)
  BaZi        bulanan   day master (unsur_pinyin) + bulan Tionghoa tgl 15 (<shio>_<elemen cabang>)
  Zi Wei      bulanan   bintang utama + istana transit = (cabang bulan Tionghoa - cabang Ming Gong) mod 12 + 1
                        (key fungsi: "<slug bintang>|<cabang Ming Gong>", mis. "qi_sha|Zi"; versi penyederhanaan kita)

Semua tanggal acuan = WIB. Record yang belum ada di JSON -> fungsi return None (UI sembunyikan kartu).
Sampel tgl 15 dipakai buat bulanan karena Matahari / bulan Tionghoa ganti sekitar tgl 4-8 dan 20-23.
"""

import datetime as _dt
from functools import lru_cache
from pathlib import Path

from content import safe_json
from engine.astro_lite import fase_bulan, rumah, tanda_bulan, tanda_matahari, TANDA
from engine.kalender_cina import cabang_bulan, elemen_hari, shio_bulan
from engine.rotation import BULAN, format_periode_minggu, format_tanggal, today_wib, week_start
from engine.weton import hitung_weton

_BASE = Path(__file__).resolve().parent / "interpretations"

# (sistem, periode) -> (file, field kunci record)
_SPEC = {
    ("Zodiak", "daily"): ("zodiak/daily.json", ("sign_user", "house")),
    ("Zodiak", "weekly"): ("zodiak/weekly.json", ("sign_user", "fase_bulan")),
    ("Zodiak", "monthly"): ("zodiak/monthly.json", ("sign_user", "sun_house")),
    ("Shio", "daily"): ("shio/daily.json", ("shio_user", "elemen_hari_ini")),
    ("Shio", "monthly"): ("shio/monthly.json", ("shio_user", "shio_bulan_ini")),
    ("Weton", "daily"): ("weton/daily.json", ("weton_user", "pasaran_hari_ini")),
    ("Weton", "weekly"): ("weton/weekly.json", ("weton_user", "fase_bulan")),
    ("Numerologi", "monthly"): ("numerologi/monthly.json", ("personal_year", "personal_month")),
    ("Shio", "weekly"): ("shio/weekly.json", ("shio_user", "fase_bulan")),
    ("Numerologi", "daily"): ("numerologi/daily.json", ("personal_month", "personal_day")),
    ("Numerologi", "weekly"): ("numerologi/weekly.json", ("personal_month", "fase_bulan")),
    ("BaZi", "monthly"): ("bazi/monthly.json", ("day_master", "elemen_bulan")),
    ("Zi Wei", "monthly"): ("ziwei/monthly.json", ("bintang_utama", "istana_transit")),
}

# Elemen cabang bumi (dipakai kunci bulanan BaZi: <shio bulan>_<elemen cabang>)
_ELEMEN_CABANG = {"tikus": "air", "kerbau": "tanah", "macan": "kayu", "kelinci": "kayu", "naga": "tanah", "ular": "api",
                  "kuda": "api", "kambing": "tanah", "monyet": "logam", "ayam": "logam", "anjing": "tanah", "babi": "air"}
_CABANG_ZIWEI = ["Zi", "Chou", "Yin", "Mao", "Chen", "Si", "Wu", "Wei", "Shen", "You", "Xu", "Hai"]


def tersedia(system, kind):
    """Apakah kombinasi sistem + periode ini punya data periodik."""
    return (system, kind) in _SPEC


def _records(system, kind):
    """List record mentah (dipisah supaya gampang di-monkeypatch di tes)."""
    f = _SPEC.get((system, kind))
    d = safe_json.load(_BASE / f[0]) if f else None
    return d if isinstance(d, list) else []


@lru_cache(maxsize=None)
def _index(system, kind):
    fields = _SPEC[(system, kind)][1]
    idx = {}
    for r in _records(system, kind):
        if isinstance(r, dict):
            idx[tuple(str(r.get(f, "")).strip().lower() for f in fields)] = r
    return idx


def _norm(x):
    return str(x).strip().lower().replace(" ", "_")


def personal_year(tgl_lahir, tahun):
    return _reduksi(_reduksi(tgl_lahir.day) + _reduksi(tgl_lahir.month) + _reduksi(tahun))


def personal_month(tgl_lahir, tahun, bulan):
    return _reduksi(personal_year(tgl_lahir, tahun) + bulan)


def _reduksi(n):
    """Reduksi ke 1-9 (master number ikut direduksi: data periodik hanya punya 1-9)."""
    while n > 9:
        n = sum(int(c) for c in str(n))
    return n


def kunci(system, kind, key, now=None, tgl_lahir=None):
    """Tuple kunci record untuk (sistem, periode, key user, waktu). None kalau tidak bisa dihitung."""
    d = today_wib(now)
    try:
        if system == "Zodiak":
            tanda = str(key).strip().title()
            if tanda not in TANDA:
                return None
            if kind == "daily":
                return (tanda.lower(), str(rumah(tanda, tanda_bulan(d))))
            if kind == "weekly":
                return (tanda.lower(), fase_bulan(week_start(d)))
            if kind == "monthly":
                return (tanda.lower(), str(rumah(tanda, tanda_matahari(_dt.date(d.year, d.month, 15)))))
        elif system == "Shio":
            if kind == "daily":
                return (_norm(key), elemen_hari(d))
            if kind == "weekly":
                return (_norm(key), fase_bulan(week_start(d)))
            if kind == "monthly":
                return (_norm(key), shio_bulan(_dt.date(d.year, d.month, 15)))
        elif system == "Weton":
            if kind == "daily":
                return (_norm(key), hitung_weton(d)["pasaran"].lower())
            if kind == "weekly":
                return (_norm(key), fase_bulan(week_start(d)))
        elif system == "Numerologi" and tgl_lahir:
            if kind == "monthly":
                return (str(personal_year(tgl_lahir, d.year)), str(personal_month(tgl_lahir, d.year, d.month)))
            if kind == "daily":
                pm = personal_month(tgl_lahir, d.year, d.month)
                return (str(pm), str(_reduksi(pm + d.day)))
            if kind == "weekly":
                senin = week_start(d)
                return (str(personal_month(tgl_lahir, senin.year, senin.month)), fase_bulan(senin))
        elif system == "BaZi" and kind == "monthly":
            from engine.bazi import TIANGAN
            tg = next((t for t in TIANGAN if t["pinyin"] == _norm(key)), None)
            sb = shio_bulan(_dt.date(d.year, d.month, 15))
            return (f"{tg['elemen'].lower()}_{tg['pinyin']}", f"{sb}_{_ELEMEN_CABANG[sb]}") if tg else None
        elif system == "Zi Wei" and kind == "monthly":
            slug, _, mg = str(key).partition("|")  # key = "<slug bintang>|<cabang Ming Gong>"
            if mg not in _CABANG_ZIWEI:
                return None
            cb = cabang_bulan(_dt.date(d.year, d.month, 15))
            return (slug, str((cb - _CABANG_ZIWEI.index(mg)) % 12 + 1))
    except (KeyError, ValueError, AttributeError):
        return None
    return None


def _ambil(system, kind, key, now, tgl_lahir):
    if not tersedia(system, kind):
        return None, None
    k = kunci(system, kind, key, now, tgl_lahir)
    rec = _index(system, kind).get(k) if k else None
    return (rec, k) if rec else (None, k)


def get_daily(system, key, now=None, tgl_lahir=None):
    """Harian. Return {periode, key, dasar, pesan, aksi, hindari, jam_baik, angka_hoki, warna_hoki} atau None."""
    rec, k = _ambil(system, "daily", key, now, tgl_lahir)
    if not rec:
        return None
    d = today_wib(now)
    return {"periode": format_tanggal(d), "key": d.isoformat(), "dasar": k,
            **{f: rec.get(f) for f in ("pesan", "aksi", "hindari", "jam_baik", "angka_hoki", "warna_hoki")}}


def get_weekly(system, key, now=None, tgl_lahir=None):
    """Mingguan. Return {periode, key, dasar, ...field record} atau None."""
    rec, k = _ambil(system, "weekly", key, now, tgl_lahir)
    if not rec:
        return None
    d = today_wib(now)
    skip = set(_SPEC[(system, "weekly")][1])
    return {"periode": format_periode_minggu(d), "key": week_start(d).isoformat(), "dasar": k,
            **{f: v for f, v in rec.items() if f not in skip}}


def get_monthly(system, key, now=None, tgl_lahir=None):
    """Bulanan. Numerologi butuh `tgl_lahir` (date). Return {periode, key, dasar, ...field record} atau None."""
    rec, k = _ambil(system, "monthly", key, now, tgl_lahir)
    if not rec:
        return None
    d = today_wib(now)
    skip = set(_SPEC[(system, "monthly")][1])
    return {"periode": f"{BULAN[d.month - 1]} {d.year}", "key": f"{d.year}-{d.month:02d}", "dasar": k,
            **{f: v for f, v in rec.items() if f not in skip}}


def _kombinasi_harapan(system, kind):
    """Semua kombinasi kunci yang HARUS ada (untuk audit kelengkapan)."""
    from engine.kalender_cina import ELEMEN_BATANG, SHIO_URUT
    hari = ["senin", "selasa", "rabu", "kamis", "jumat", "sabtu", "minggu"]
    pas = ["legi", "pahing", "pon", "wage", "kliwon"]
    fase = ("new_moon", "first_quarter", "full_moon", "third_quarter")
    tanda = [t.lower() for t in TANDA]
    weton = [f"{h}_{p}" for h in hari for p in pas]
    unsur = list(dict.fromkeys(ELEMEN_BATANG))
    if system == "Zodiak":
        return {"daily": [(t, str(h)) for t in tanda for h in range(1, 13)],
                "weekly": [(t, f) for t in tanda for f in fase],
                "monthly": [(t, str(h)) for t in tanda for h in range(1, 13)]}[kind]
    if system == "Shio":
        return {"daily": [(s, e) for s in SHIO_URUT for e in unsur],
                "weekly": [(s, f) for s in SHIO_URUT for f in fase],
                "monthly": [(s, b) for s in SHIO_URUT for b in SHIO_URUT]}[kind]
    if system == "Weton":
        return {"daily": [(w, p) for w in weton for p in pas], "weekly": [(w, f) for w in weton for f in fase]}[kind]
    if system == "BaZi":
        dm = ["kayu_jia", "kayu_yi", "api_bing", "api_ding", "tanah_wu", "tanah_ji", "logam_geng", "logam_xin", "air_ren", "air_gui"]
        return [(d, f"{sb}_{_ELEMEN_CABANG[sb]}") for d in dm for sb in SHIO_URUT]
    if system == "Zi Wei":
        bt = ["zi_wei", "tian_ji", "tai_yang", "wu_qu", "tian_tong", "lian_zhen", "tian_fu", "tai_yin", "tan_lang",
              "ju_men", "tian_xiang", "tian_liang", "qi_sha", "po_jun"]
        return [(b, str(h)) for b in bt for h in range(1, 13)]
    # Numerologi
    if kind == "daily":
        return [(str(m), str(d)) for m in range(1, 10) for d in range(1, 10)]
    if kind == "weekly":
        return [(str(m), f) for m in range(1, 10) for f in fase]
    return [(str(y), str(m)) for y in range(1, 10) for m in range(1, 10)]


def audit(system, kind):
    """Cek kelengkapan: return {"hilang": [...], "duplikat_beda_isi": [...], "duplikat_sama": n, "total": n}."""
    recs = _records(system, kind)
    fields = _SPEC[(system, kind)][1]
    seen, beda, sama = {}, [], 0
    for r in recs:
        k = tuple(str(r.get(f, "")).strip().lower() for f in fields)
        if k in seen:
            if seen[k] == r:
                sama += 1
            else:
                beda.append(k)
        seen[k] = r
    hilang = [k for k in _kombinasi_harapan(system, kind) if k not in seen]
    return {"total": len(recs), "hilang": hilang, "duplikat_beda_isi": beda, "duplikat_sama": sama}
