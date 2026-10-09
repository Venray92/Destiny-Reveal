"""
Kalender Energi bulanan: menandai tanggal penting dari 4 sistem (Daily Free, tanda gratis; detail berbayar).

Tiga jenis tanda (aturan, tabel skor ada di content/daily_energy.py):
- Bisnis  : pejabat hari (12 Day Officers / Jian Chu) Kai, Cheng, Ding = baik (Tong Shu); Po, Wei = dihindari.
            "Prima" bila disertai personal day 1 atau 8 (Numerologi: inisiatif / hasil). "Baik" bila
            pejabat baik + Bulan di rumah 2/6/10/11 (uang, kerja, karier, jaringan).
- Konflik : cabang bumi hari Chong (bentrok) atau Hai (rugi) dengan shio user. "Tinggi" bila Bulan di
            rumah 6/8/12 atau pejabat hari Po/Wei; selain itu "Waspada".
- Romansa : cabang hari Liu He / San He dengan shio user. "Puncak" bila Bulan di rumah 5/7 DAN personal day 2/6;
            "Baik" bila salah satunya.
Pejabat hari = (cabang hari - cabang bulan Tionghoa) mod 12 -> Jian, Chu, Man, Ping, Ding, Zhi, Po, Wei, Cheng, Shou, Kai, Bi.
"""

import calendar
import datetime as _dt
from datetime import datetime, time

from content import daily_energy as DE
from content import periodic
from engine.astro_lite import rumah, tanda_bulan
from engine.kalender_cina import cabang_bulan, pilar_hari
from engine.weton import hitung_weton
from engine.zodiak import hitung_zodiak

OFFICERS = [
    ("Jian", "Mendirikan", "Baik untuk memulai hal baru dan menetapkan arah."),
    ("Chu", "Membersihkan", "Baik untuk bersih-bersih, melepas yang lama, dan pemulihan."),
    ("Man", "Penuh", "Baik untuk perayaan dan kumpul, kurang cocok untuk kontrak besar."),
    ("Ping", "Seimbang", "Hari biasa: cocok untuk perbaikan dan urusan rutin."),
    ("Ding", "Menetapkan", "Baik untuk tanda tangan, kesepakatan, dan keputusan."),
    ("Zhi", "Memegang", "Baik untuk mengikat janji dan merapikan; hindari terburu-buru."),
    ("Po", "Menghancurkan", "Hindari memulai hal penting, kontrak, atau hajatan."),
    ("Wei", "Bahaya", "Hati-hati dan hindari risiko tinggi; pilih jalur aman."),
    ("Cheng", "Menyelesaikan", "Sangat baik untuk kontrak, peluncuran, dan menuntaskan target."),
    ("Shou", "Menuai", "Baik untuk menagih, menerima hasil, dan menutup transaksi."),
    ("Kai", "Membuka", "Baik untuk membuka usaha, memulai proyek, dan menjalin relasi."),
    ("Bi", "Menutup", "Baik untuk menutup urusan dan menyimpan; hindari memulai hal besar."),
]
GOOD, AVOID = {"Kai", "Cheng", "Ding"}, {"Po", "Wei"}
RELASI_LABEL = {"liu_he": "Liu He", "san_he": "San He", "chong": "Chong", "hai": "Hai", "sama": "Fu Yin", "netral": "netral"}


def pejabat(d):
    i = (pilar_hari(d)[1] - cabang_bulan(d)) % 12
    return i, OFFICERS[i]


def _hari(tgl_lahir, d, shio_idx, sign):
    oi, (on, oid, odesc) = pejabat(d)
    house = rumah(sign, tanda_bulan(d))
    rel = DE._relasi(pilar_hari(d)[1], shio_idx)
    pm = periodic.personal_month(tgl_lahir, d.year, d.month)
    pd = periodic._reduksi(pm + d.day)
    marks = []
    if on in GOOD:
        if pd in (1, 8):
            marks.append(("bisnis", "prima", f"Hari {on} ({oid}) + personal day {pd}: kombinasi terbaik untuk bisnis dan keputusan."))
        elif house in (2, 6, 10, 11):
            marks.append(("bisnis", "baik", f"Hari {on} ({oid}) + Bulan di rumah {house}: mendukung uang, kerja, dan jaringan."))
    if rel in ("chong", "hai"):
        keras = house in (6, 8, 12) or on in AVOID
        why = f"Hari {RELASI_LABEL[rel]} dengan shiomu"
        if keras:
            why += f" + {'Bulan di rumah ' + str(house) if house in (6, 8, 12) else 'pejabat hari ' + on}: rawan gesekan, tunda keputusan emosional."
        else:
            why += ": waspada salah paham, cek ulang ucapan dan janji."
        marks.append(("konflik", "tinggi" if keras else "waspada", why))
    if rel in ("liu_he", "san_he"):
        a, b = house in (5, 7), pd in (2, 6)
        if a or b:
            why = f"Hari {RELASI_LABEL[rel]} dengan shiomu"
            why += (f" + Bulan di rumah {house} dan personal day {pd}: peluang romansa dan kedekatan paling kuat." if a and b
                    else (f" + Bulan di rumah {house}: suasana hati condong ke relasi." if a
                          else f" + personal day {pd}: hangat untuk hubungan dekat."))
            marks.append(("romansa", "puncak" if a and b else "baik", why))
    return {"d": d, "off": {"id": on, "nama": oid, "desc": odesc, "baik": on in GOOD, "hindari": on in AVOID},
            "pd": pd, "house": house, "rel": RELASI_LABEL[rel], "marks": marks}


def bulan(tgl_lahir, tahun, bln):
    """List hari satu bulan (dict per hari) + skor energi harian."""
    sign = hitung_zodiak(tgl_lahir)["sign"]
    si = DE.shio_user_idx(tgl_lahir)
    out = []
    for n in range(1, calendar.monthrange(tahun, bln)[1] + 1):
        d = _dt.date(tahun, bln, n)
        r = _hari(tgl_lahir, d, si, sign)
        e = DE.skor_energi(tgl_lahir, d)
        r["skor"], r["tier"] = e["skor"], e["tier"]
        out.append(r)
    return out


def ringkas(hari):
    c = {"bisnis": 0, "konflik": 0, "romansa": 0}
    for h in hari:
        for t, _lv, _w in h["marks"]:
            c[t] += 1
    return c


# ─────────────── detail berbayar (dari JSON harian 4 sistem) ───────────────
def detail_hari(tgl_lahir, d):
    """{sistem: {pesan, aksi, hindari, jam_baik, angka, warna}} untuk tanggal d, dari content/interpretations/*/daily.json."""
    now = datetime.combine(d, time(12))
    wt = hitung_weton(tgl_lahir)
    kunci = {"Zodiak": hitung_zodiak(tgl_lahir)["sign"], "Shio": DE.SHIO_URUT[DE.shio_user_idx(tgl_lahir)],
             "Weton": f"{wt['hari']} {wt['pasaran']}", "Numerologi": None}
    out = {}
    for s, k in kunci.items():
        e = periodic.get_daily(s, k, now=now, tgl_lahir=tgl_lahir)
        if e and e.get("pesan"):
            out[s] = {"pesan": e["pesan"], "aksi": e.get("aksi") or [], "hindari": e.get("hindari") or [],
                      "jam_baik": e.get("jam_baik") or "", "angka": e.get("angka_hoki") or "", "warna": e.get("warna_hoki") or ""}
    return out
