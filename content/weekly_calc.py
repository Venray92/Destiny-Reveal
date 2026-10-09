"""
Weekly & Monthly Report: susun laporan dari data yang SUDAH ada (library periodik + engine), tanpa konten baru.
Energi harian = biorhythm (siklus 23/28/33 hari dari tanggal lahir) + bonus kalau harinya cocok dengan
`hari_terbaik` di library / pasaran weton yang sama. Semua deterministik (input sama -> output sama).
"""

import datetime as _dt
import math
import re

from content import periodic
from engine.rotation import BULAN, HARI, format_periode_minggu, today_wib, week_start

FOCUS = {
    "harmoni": ("Harmoni Terpadu", "☀️", "Rekomendasi presisi buat minggu ini"),
    "karier": ("Fokus Karier & Keuangan", "💼", "Timing & peluang karier"),
    "asmara": ("Fokus Asmara & Relasi", "💗", "Panduan hubungan"),
}
# sistem yang dipakai tiap fokus (weekly / monthly)
SYSTEMS = {
    "weekly": {"harmoni": ["Zodiak", "Weton"], "karier": ["Zodiak", "Weton", "Shio"], "asmara": ["Zodiak", "Weton", "Tarot"]},
    "monthly": {"harmoni": ["Zodiak", "Shio", "Numerologi", "BaZi", "Zi Wei"],
                "karier": ["Zodiak", "Shio", "BaZi", "Numerologi"],
                "asmara": ["Zodiak", "Shio", "Zi Wei", "Tarot"]},
}

_TEMA_HARI = {
    "Senin": "Hari Bulan: perasaan dan intuisi lebih peka, mulai pekan dengan niat yang jelas.",
    "Selasa": "Hari Mars: dorongan aksi kuat, cocok untuk eksekusi dan negosiasi.",
    "Rabu": "Hari Merkurius: komunikasi, dokumen, dan koordinasi cenderung lancar.",
    "Kamis": "Hari Jupiter: peluang dan relasi lebih mudah bertumbuh.",
    "Jumat": "Hari Venus: harmoni, relasi, dan hal-hal yang menyenangkan hati.",
    "Sabtu": "Hari Saturnus: waktu untuk disiplin, evaluasi, dan merapikan struktur.",
    "Minggu": "Hari Matahari: vitalitas dan arah hidup lebih terasa jelas.",
}
_TIER_TEKS = {
    "puncak": "Puncak energi, manfaatkan untuk keputusan atau aksi terbesarmu.",
    "baik": "Energi mendukung, jalankan rencana utama dengan percaya diri.",
    "netral": "Energi stabil, cocok untuk pekerjaan rutin dan merapikan detail.",
    "hindari": "Energi menurun, hindari keputusan besar dan jaga waktu istirahat.",
}
_TIER_LABEL = {"puncak": "PUNCAK", "baik": "Baik", "netral": "Netral", "hindari": "Hindari"}
_ELEMEN_WARNA = {"Api": "Terracotta", "Tanah": "Emas Mustard", "Udara": "Biru Langit", "Air": "Biru Laut"}
_ELEMEN_ARAH = {"Api": "Selatan", "Tanah": "Barat Daya", "Udara": "Barat", "Air": "Utara"}
_QUOTE = {
    "tinggi": ["Keberanian bukan tanpa ragu, melainkan tetap melangkah.", "Saat angin searah, layarkan rencanamu sepenuhnya.",
               "Momentum adalah hadiah bagi yang sudah bersiap."],
    "sedang": ["Langkah kecil yang konsisten mengalahkan lompatan yang tidak terarah.",
               "Ritme yang stabil lebih berharga daripada semangat yang meledak sesaat.",
               "Rapikan hari ini, dan hari esok akan terasa lebih ringan."],
    "rendah": ["Berhenti sejenak bukan mundur, itu cara mengisi tenaga untuk melangkah jauh.",
               "Tidak semua minggu untuk berlari; sebagian untuk memulihkan diri.",
               "Tenang adalah strategi, bukan kelemahan."],
}


# ─────────────── util kecil ───────────────
def _kalimat(text, n=1, maks=210):
    """n kalimat pertama, dipotong rapi kalau kepanjangan."""
    parts = re.split(r"(?<=[.!?])\s+", (text or "").strip())
    out = " ".join(parts[:n]).strip()
    if len(out) > maks:
        out = out[:maks].rsplit(" ", 1)[0].rstrip(",;:") + "…"
    return out


def _rata(vals):
    return round(sum(vals) / len(vals)) if vals else 0


def _bio(tgl_lahir, d):
    t = (d - tgl_lahir).days
    x = sum(math.sin(2 * math.pi * t / p) for p in (23, 28, 33)) / 3
    return 62 + 38 * x


def _energi(tgl_lahir, d, bonus_hari, pasaran_user):
    from engine.weton import hitung_weton
    e = _bio(tgl_lahir, d)
    if HARI[d.weekday()] in bonus_hari:
        e += 8
    try:
        if hitung_weton(d)["pasaran"] == pasaran_user:
            e += 4
    except Exception:
        pass
    return max(15, min(100, int(round(e / 5.0)) * 5))


def _tier(e, puncak):
    if puncak:
        return "puncak"
    return "baik" if e >= 75 else "netral" if e >= 55 else "hindari"


def _label_harmoni(idx):
    return ("Sangat Kondusif" if idx >= 80 else "Kondusif" if idx >= 65
            else "Cukup Stabil" if idx >= 50 else "Perlu Kehati-hatian")


def _tarot(kind):
    try:
        from content.result_builder import build_display_data
        from engine.tarot import kartu_periodik
        return build_display_data("Tarot", {"kartu": kartu_periodik(kind)}) or {}
    except Exception:
        return {}


def _rekam(kind, sistem, prof, now):
    """Record library (dict) untuk satu sistem, atau None kalau tidak tersedia."""
    from engine.weton import hitung_weton
    from engine.zodiak import hitung_zodiak
    tgl = prof["tgl"]
    get = periodic.get_weekly if kind == "weekly" else periodic.get_monthly
    try:
        if sistem == "Zodiak":
            return get("Zodiak", hitung_zodiak(tgl)["sign"], now=now)
        if sistem == "Shio":
            from engine.shio import hitung_shio
            return get("Shio", hitung_shio(tgl)["shio"], now=now)
        if sistem == "Weton":
            w = hitung_weton(tgl)
            return get("Weton", f"{w['hari']} {w['pasaran']}", now=now)
        if sistem == "Numerologi":
            return get("Numerologi", "", now=now, tgl_lahir=tgl)
        if sistem == "BaZi":
            from engine.bazi import hitung_bazi
            return get("BaZi", hitung_bazi(tgl)["day_master"], now=now)
        if sistem == "Zi Wei":
            jam = prof.get("jam")
            if jam is None:
                return None
            from engine.ziwei import hitung_ziwei
            zw = hitung_ziwei(tgl, jam.hour if hasattr(jam, "hour") else int(jam))
            slug = {"ziwei": "zi_wei", "tianji": "tian_ji", "taiyang": "tai_yang", "wuqu": "wu_qu", "tiantong": "tian_tong",
                    "lianzhen": "lian_zhen", "tianfu": "tian_fu", "taiyin": "tai_yin", "tanlang": "tan_lang",
                    "jumen": "ju_men", "tianxiang": "tian_xiang", "tianliang": "tian_liang", "qisha": "qi_sha",
                    "pojun": "po_jun"}[zw["bintang"]]
            return get("Zi Wei", f"{slug}|{zw['ming_gong']}", now=now)
    except Exception:
        return None
    return None


def profil_terdeteksi(tgl):
    from engine.weton import hitung_weton
    from engine.zodiak import hitung_zodiak
    w = hitung_weton(tgl)
    return {"zodiak": hitung_zodiak(tgl), "weton": w}


# ─────────────── laporan ───────────────
def build_report(kind, prof, focus="harmoni", now=None):
    """kind: weekly|monthly. prof: {nama,tgl,jam?,...}. Return dict siap render (lihat components/weekly_report.py)."""
    d0 = today_wib(now)
    tgl = prof["tgl"]
    from engine.shio import hitung_shio
    from engine.weton import hitung_weton
    from engine.zodiak import hitung_zodiak
    zod, wet, sh = hitung_zodiak(tgl), hitung_weton(tgl), hitung_shio(tgl)
    systems = SYSTEMS[kind][focus]
    recs = {s: _rekam(kind, s, prof, now) for s in systems if s != "Tarot"}
    recs = {s: r for s, r in recs.items() if r}
    tarot = _tarot(kind)  # dipakai juga buat kartu aspek (karier/asmara/finansial) di semua fokus

    # hari "terbaik" dari library (nama hari)
    bonus_hari = set()
    for r in recs.values():
        hb = (r.get("hari_terbaik") or "").split(" ")[0]
        if hb in HARI:
            bonus_hari.add(hb)

    if kind == "weekly":
        start = week_start(d0)
        tanggal = [start + _dt.timedelta(i) for i in range(7)]
    else:
        first = _dt.date(d0.year, d0.month, 1)
        nxt = _dt.date(d0.year + (d0.month == 12), d0.month % 12 + 1, 1)
        tanggal = [first + _dt.timedelta(i) for i in range((nxt - first).days)]
    en = {d: _energi(tgl, d, bonus_hari, wet["pasaran"]) for d in tanggal}
    idx = _rata(list(en.values()))

    # ── bar energi + kartu navigasi ──
    if kind == "weekly":
        urut = sorted(tanggal, key=lambda d: (-en[d], d))
        puncak = [d for d in urut[:2] if en[d] >= (70 if d is not urut[0] else 0)]
        rendah = urut[-1] if en[urut[-1]] < 60 else None
        bars, hari_cards = [], []
        for d in tanggal:
            t = _tier(en[d], d in puncak)
            if d is rendah and t != "puncak":
                t = "hindari"
            nama = HARI[d.weekday()]
            bars.append({"label": nama, "pct": en[d], "tier": t, "tag": _TIER_LABEL[t]})
            hari_cards.append({"label": f"{nama}, {d.day}", "tier": t,
                               "text": f"{_TEMA_HARI[nama]} {_TIER_TEKS[t]}"})
        best_txt = " & ".join(f"{HARI[d.weekday()]} ({d.day})" for d in sorted(puncak))
        best_nama = " & ".join(HARI[d.weekday()] for d in sorted(puncak))
        best_dates = sorted(puncak)
        low_date = rendah
        periode = format_periode_minggu(d0)
        judul = "WEEKLY COSMIC REPORT"
        nav_judul = "NAVIGASI 7 HARI (HARI DEMI HARI)"
        best_head = "HARI TERBAIK MINGGU INI:"
        unit = "pekan"
    else:
        # 4-5 blok minggu dalam bulan (1-7, 8-14, 15-21, 22-28, 29-akhir)
        blok = [tanggal[i:i + 7] for i in range(0, len(tanggal), 7)]
        kunci = set()
        for r in recs.values():
            kunci |= {int(x) for x in re.findall(r"ke-(\d)", r.get("fase_kunci") or "")}
        bars, hari_cards = [], []
        rata_blok = [_rata([en[d] for d in b]) for b in blok]
        mx = max(rata_blok)
        for i, (b, e) in enumerate(zip(blok, rata_blok), 1):
            t = _tier(e, e == mx and e >= 70)
            if e == min(rata_blok) and e < 60:
                t = "hindari"
            bars.append({"label": f"Minggu {i}", "pct": e, "tier": t, "tag": _TIER_LABEL[t]})
            best_d = max(b, key=lambda d: (en[d], -d.toordinal()))
            kt = " Fase kunci bulan ini." if i in kunci else ""
            hari_cards.append({"label": f"Minggu {i} ({b[0].day}-{b[-1].day} {BULAN[b[0].month - 1][:3]})", "tier": t,
                               "text": f"Rata-rata energi {e}%. Hari terkuat: {HARI[best_d.weekday()]}, {best_d.day}. "
                                       f"{_TIER_TEKS[t]}{kt}", "kunci": i in kunci})
        kand = [d for d in tanggal if d >= d0]
        if len(kand) < 3:
            kand = tanggal  # akhir bulan: pakai seluruh bulan
        best_dates = sorted(sorted(kand, key=lambda d: (-en[d], d))[:3])
        puncak = best_dates
        low_date = sorted(kand, key=lambda d: (en[d], d))[0]
        best_txt = ", ".join(f"{d.day}" for d in best_dates) + f" {BULAN[d0.month - 1]}"
        best_nama = best_txt
        periode = f"{BULAN[d0.month - 1]} {d0.year}"
        judul = "MONTHLY COSMIC REPORT"
        nav_judul = "NAVIGASI 4 MINGGU (FASE BULAN INI)"
        best_head = "GOLDEN DAYS BULAN INI:"
        unit = "bulan"

    # ── top 3 prioritas ──
    def fokus(s):
        r = recs.get(s) or {}
        return r.get("fokus_mingguan") or r.get("fokus_bulan_ini")

    p_dates = (list(best_dates) + list(best_dates))[:2] if best_dates else [tanggal[0], tanggal[0]]
    if len(best_dates) > 1:
        p_dates = best_dates[:2]
    cand = []
    if fokus("Zodiak"):
        cand.append(fokus("Zodiak"))
    for s in ("Shio", "Numerologi", "BaZi", "Zi Wei"):
        if fokus(s) and s in systems and len(cand) < 2:
            cand.append(fokus(s))
    if focus == "asmara" and tarot.get("title") and len(cand) < 2:
        cand.append(f"Tema kartu: {tarot['title']}")
    if len(cand) < 2:
        hb = (recs.get("Weton") or {}).get("hari_terbaik")
        cand.append(f"Selaraskan ritme di hari {hb}" if hb else "Selaraskan ritme harianmu")
    prio = []
    for i, (judul_p, dt) in enumerate(zip(cand[:2], p_dates)):
        e = en[dt]
        lv = "High" if e >= 80 else "Medium" if e >= 60 else "Low"
        prio.append({"title": judul_p, "best": f"{HARI[dt.weekday()]}, {dt.day}", "pct": e, "level": lv,
                     "cls": "hi" if lv == "High" else "md"})
    ld = low_date or sorted(tanggal, key=lambda d: (en[d], d))[0]
    prio.append({"title": "Istirahat total & pemulihan energi", "best": f"{HARI[ld.weekday()]}, {ld.day}",
                 "pct": en[ld], "level": "Low / Rest", "cls": "lo"})

    # ── elemen dominan ──
    elemen = f"{zod['element']} & {sh['elemen']}".upper()

    # ── tema & arus energi ──
    tema = []
    z = recs.get("Zodiak") or {}
    w = recs.get("Weton") or {}
    if z.get("timing"):
        tema.append(_kalimat(z["timing"], 2, 330) + " " + _kalimat(z.get("prediksi"), 2, 330))
    if kind == "weekly" and w.get("timing"):
        tema.append(_kalimat(w["timing"], 1, 220) + " " + _kalimat(w.get("prediksi"), 2, 330))
    for s in systems:
        if s in ("Zodiak", "Weton", "Tarot"):
            continue
        r = recs.get(s)
        if r and r.get("timing") and len(tema) < 3:
            tema.append(f"{s}: " + _kalimat(r["timing"], 1, 220) + " " + _kalimat(r.get("prediksi"), 1, 220))
    if tarot.get("p1") and len(tema) < 3:
        tema.append(f"Kartu {tarot.get('title', '')}: " + _kalimat(tarot["p1"], 2, 300))
    # ── insight ──
    saran_z = _kalimat((z or w).get("saran"), 1, 150).rstrip(".")
    insight = (f"Energi terbaik berada di {'hari ' if kind == 'weekly' else 'tanggal '}{best_nama}. "
               f"Gunakan momen emas ini untuk {saran_z[:1].lower() + saran_z[1:] if saran_z else 'mengambil langkah terpenting'}.")

    # ── aspek ──
    def pick(*pairs):
        for s, f in pairs:
            r = recs.get(s) or {}
            if r.get(f):
                return _kalimat(r[f], 2, 230)
        return ""

    # Library periodik tidak dipisah per aspek; kartu Tarot punya uraian khusus karier/asmara/keuangan -> dipakai di semua fokus
    dom = tarot.get("domains") or {}
    fb = ("saran",) if kind == "weekly" else ("peluang",)
    karier = _kalimat(dom.get("karir"), 1, 270) or pick(("Zodiak", fb[0]), ("Weton", "saran"))
    asmara = _kalimat(dom.get("asmara"), 1, 270) or pick(("Weton", "prediksi"), ("Zodiak", "prediksi"))
    fin = _kalimat(dom.get("keuangan"), 1, 270) or pick(("Weton", "saran"), ("Numerologi", "peluang"), ("Zodiak", fb[0]))
    arah_w = (w.get("arah_rezeki") or "")
    if arah_w and kind == "weekly" and focus != "asmara":
        fin = (fin + f" Arah rezeki: {arah_w}.").strip()
    aspek = [("💼", "Karier & Bisnis", karier), ("💗", "Asmara & Hubungan", asmara), ("💰", "Arus Kas & Finansial", fin)]

    # ── hoki ──
    from engine.numerologi import hitung_life_path
    lp = hitung_life_path(tgl)
    angka = []
    for n in (lp, (wet["neptu"] - 1) % 9 + 1, best_dates[0].day if best_dates else d0.day):
        if n not in angka:
            angka.append(n)
    for n in (r.get("angka_pendukung") for r in recs.values() if r.get("angka_pendukung")):
        for x in n:
            if x not in angka and len(angka) < 3:
                angka.append(x)
    arah = (w.get("arah_rezeki") or "").strip() or _ELEMEN_ARAH.get(zod["element"], "Timur")
    hoki = {"angka": ", ".join(str(a) for a in angka[:3]), "warna": _ELEMEN_WARNA.get(zod["element"], "Terracotta"), "arah": arah}

    # ── quote, do's & don'ts ──
    grup = "tinggi" if idx >= 70 else "sedang" if idx >= 55 else "rendah"
    qs = _QUOTE[grup]
    quote = qs[(d0.isocalendar()[1] if kind == "weekly" else d0.month) % len(qs)]
    dos, donts = [], []
    f_do = "saran"
    f_dont = "hindari" if kind == "weekly" else "hindari_risiko"
    for s in systems:
        r = recs.get(s)
        if r:
            if r.get(f_do) and len(dos) < 3:
                dos.append(_kalimat(r[f_do], 1, 170))
            if r.get(f_dont) and len(donts) < 3:
                donts.append(_kalimat(r[f_dont], 1, 170))
    # lengkapi sampai 3 poin dari hitungan energi (bukan teks acak)
    ld2 = low_date or tanggal[0]
    if len(dos) < 3:
        dos.append(f"Eksekusi hal terpenting di {'hari' if kind == 'weekly' else 'tanggal'} terbaik: {best_txt}.")
    if len(dos) < 3:
        dos.append(f"Jadwalkan waktu istirahat dan pemulihan di {HARI[ld2.weekday()]}, {ld2.day}.")
    if len(donts) < 3:
        donts.append(f"Tunda keputusan besar di {HARI[ld2.weekday()]}, {ld2.day}: energimu di titik terendah ({en[ld2]}%).")
    while len(donts) < 3:
        donts.append("Memaksakan diri di luar ritme energimu hanya karena merasa harus selalu produktif.")
    sub = "Kombinasi " + " & ".join(
        {"Zodiak": f"Zodiak {zod['sign']} ({zod['element']})", "Weton": f"Weton {wet['hari']} {wet['pasaran']} (Neptu {wet['neptu']})",
         "Shio": f"Shio {sh['shio']}", "Numerologi": f"Numerologi (Life Path {lp})", "BaZi": "BaZi", "Zi Wei": "Zi Wei",
         "Tarot": "Tarot"}[s] for s in systems if s == "Tarot" or s in recs)
    return {
        "kind": kind, "judul": judul, "periode": periode, "nama": prof.get("nama") or "Kamu", "sub": sub,
        "harmoni": {"idx": idx, "label": _label_harmoni(idx)}, "elemen": elemen,
        "prio": prio, "bars": bars, "bars_judul": "ENERGY BAR 7 HARI" if kind == "weekly" else "ENERGY BAR 4 MINGGU",
        "insight": insight, "tema": tema, "nav_judul": nav_judul, "best_head": best_head, "best_txt": best_txt,
        "cards": hari_cards, "aspek": aspek, "tarot_judul": tarot.get("title", ""), "hoki": hoki, "quote": quote, "dos": dos, "donts": donts, "unit": unit,
        "sistem": [s for s in systems if s == "Tarot" or s in recs],
    }
