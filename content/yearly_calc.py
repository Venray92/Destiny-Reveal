"""
Yearly Forecast (Batch 6): Shio kamu x Shio tahun (relasi cabang bumi) + Personal Year Numerologi + kurva 12 bulan.
Dihitung di kode (deterministik): relasi, Personal Year, skor tiap bulan, bulan terbaik/terjaga.
Teks per kombinasi dari Gemini: interpretations/shio/yearly.json (kunci "tikus__kerbau") dan
interpretations/numerologi/yearly_personal.json (kunci "1".."9"). File belum ada -> teks sementara (flag "placeholder").
"""

import json
from datetime import date
from functools import lru_cache
from pathlib import Path

from content import daily_energy as DE
from content import periodic
from engine.kalender_cina import SHIO_URUT, cabang_bulan

_BASE = Path(__file__).resolve().parent / "interpretations"
BULAN = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November",
         "Desember"]
TEMA_PY = {1: "Inisiasi & Awal Baru", 2: "Kemitraan & Kesabaran", 3: "Ekspresi & Kreativitas", 4: "Fondasi & Disiplin",
           5: "Perubahan & Kebebasan", 6: "Tanggung Jawab & Keluarga", 7: "Refleksi & Pendalaman Batin",
           8: "Panen, Otoritas & Keuangan", 9: "Penyelesaian & Pelepasan"}
REL_LABEL = {"sama": "Ben Ming Nian (shio sama)", "liu_he": "Liu He (harmoni)", "san_he": "San He (selaras)",
             "chong": "Chong (bentrok)", "hai": "Hai (saling merugikan)", "netral": "Netral"}
REL_INFO = {
    "sama": "Shio tahun sama dengan shiomu: tahun ulang tahun shio, penuh perubahan dan ujian diri.",
    "liu_he": "Shio tahun berpasangan dengan shiomu: dukungan dan pintu terbuka lebih mudah datang.",
    "san_he": "Shio tahun satu segitiga harmoni dengan shiomu: langkah terasa selaras dan saling menguatkan.",
    "chong": "Shio tahun berhadapan dengan shiomu: ada gesekan dan perubahan mendadak, butuh fleksibilitas.",
    "hai": "Shio tahun saling merugikan dengan shiomu: jaga komunikasi dan jangan biarkan energi bocor.",
    "netral": "Tidak ada hubungan khusus: tahun ini ditentukan oleh usaha dan pilihanmu sendiri.",
}
SECTIONS = [("karier", "💼 Karier"), ("keuangan", "💰 Keuangan"), ("asmara", "💗 Asmara"), ("kesehatan", "🌿 Kesehatan & Energi")]
_FALL = {
    "karier": "Fokus pada satu target karier utama dan ukur kemajuannya tiap bulan.",
    "keuangan": "Susun anggaran tahunan sederhana dan sisihkan dana cadangan sebelum mengambil keputusan besar.",
    "asmara": "Luangkan waktu berkualitas untuk orang terdekat dan sampaikan harapanmu dengan jelas.",
    "kesehatan": "Jaga ritme tidur, olahraga ringan, dan jeda dari layar agar stamina stabil sepanjang tahun.",
    "ringkasan": "Gambaran tahunmu ditentukan oleh hubungan shiomu dengan shio tahun serta siklus Personal Year-mu.",
    "tips": ["Tetapkan satu tujuan besar tahun ini", "Evaluasi progres tiap akhir bulan", "Pilih satu kebiasaan sehat dan jaga konsisten"],
}


@lru_cache(maxsize=2)
def _load(rel):
    try:
        d = json.loads((_BASE / rel).read_text(encoding="utf-8"))
        return d if isinstance(d, dict) else {}
    except (OSError, ValueError):
        return {}


def shio_tahun(year):
    return (year - 4) % 12  # 0 = Tikus; berlaku sejak Imlek (Jan-Feb), bukan 1 Januari


def _score(mean):
    return int(round(max(5, min(98, 58 + (mean - 66) * 1.5))))


def kurva(tgl, year):
    """12 skor bulanan 0-100: hubungan cabang bulan x shio kamu (40%), personal month (35%), relasi tahun (25%)."""
    u, rt = DE.shio_user_idx(tgl), DE._relasi(shio_tahun(year), DE.shio_user_idx(tgl))
    out = []
    for m in range(1, 13):
        rel = DE._relasi(cabang_bulan(date(year, m, 15)), u)
        pm = periodic.personal_month(tgl, year, m)
        mean = 0.4 * DE.RELASI_SKOR[rel] + 0.35 * DE.NUM_SKOR[pm] + 0.25 * DE.RELASI_SKOR[rt]
        out.append({"bulan": BULAN[m - 1], "m": m, "skor": _score(mean), "rel": rel, "pm": pm})
    return out


def tier(skor):
    return DE.tier(skor)[0]


def baca(tgl, year):
    u = DE.shio_user_idx(tgl)
    t = shio_tahun(year)
    rel = DE._relasi(t, u)
    py = periodic.personal_year(tgl, year)
    kv = kurva(tgl, year)
    skor = int(round(sum(x["skor"] for x in kv) / 12))
    rank = sorted(kv, key=lambda x: (-x["skor"], x["m"]))
    key = f"{SHIO_URUT[u]}__{SHIO_URUT[t]}"
    rec = _load("shio/yearly.json").get(key) or {}
    prec = _load("numerologi/yearly_personal.json").get(str(py)) or {}
    ph = False

    def pick(name):
        nonlocal ph
        v = rec.get(name)
        if isinstance(v, str) and v.strip():
            return v.strip()
        ph = True
        return _FALL[name]
    tips = rec.get("tips")
    if not (isinstance(tips, list) and tips):
        tips, ph = _FALL["tips"], True
    pyr = {k: prec.get(k) for k in ("judul", "tema", "ringkasan")}
    py_ph = not pyr.get("ringkasan")
    if py_ph:
        pyr = {"judul": TEMA_PY[py], "tema": TEMA_PY[py],
               "ringkasan": f"Tahun ini kamu berada di siklus {py}: {TEMA_PY[py].lower()}."}
    return {"year": year, "shio_kamu": SHIO_URUT[u].capitalize(), "shio_tahun": SHIO_URUT[t].capitalize(), "rel": rel,
            "rel_label": REL_LABEL[rel], "rel_info": REL_INFO[rel], "py": py, "py_data": pyr, "skor": skor,
            "tier": tier(skor), "kurva": kv, "terbaik": sorted(rank[:2], key=lambda x: x["m"]),
            "terjaga": sorted(rank[-2:], key=lambda x: x["m"]),
            "judul": rec.get("judul") if isinstance(rec.get("judul"), str) and rec.get("judul") else f"Tahun {SHIO_URUT[t].capitalize()} untuk {SHIO_URUT[u].capitalize()}",
            "ringkasan": pick("ringkasan"), "sections": [(lb, pick(k)) for k, lb in SECTIONS], "tips": [str(x) for x in tips][:3],
            "paruh": prec.get("paruh_tahun") if isinstance(prec.get("paruh_tahun"), str) else "",
            "placeholder": ph or py_ph}
