"""
Decision Reveal (Batch 5): 7 kartu, Pilihan A vs B.
Polarity + intensitas per kartu: content/interpretations/tarot/decision_meta.json (dibuat Claude, tradisional upright).
Teks per kartu: .../tarot/decision.json (dari Gemini). Kalau file/kunci belum ada -> teks sementara (flag "placeholder").
"""

import json
from functools import lru_cache
from pathlib import Path

_BASE = Path(__file__).resolve().parent / "interpretations" / "tarot"

# (judul, field teks, penjelasan posisi)
POSITIONS = [
    ("Inti Situasi", "sebagai_opsi", "Energi dasar dari keputusan yang sedang kamu hadapi."),
    ("Pilihan A: Energi", "sebagai_opsi", "Apa yang ditawarkan Pilihan A kepadamu."),
    ("Pilihan A: Risiko", "sebagai_risiko", "Apa yang perlu diwaspadai kalau kamu memilih A."),
    ("Pilihan B: Energi", "sebagai_opsi", "Apa yang ditawarkan Pilihan B kepadamu."),
    ("Pilihan B: Risiko", "sebagai_risiko", "Apa yang perlu diwaspadai kalau kamu memilih B."),
    ("Faktor Tersembunyi", "faktor_tersembunyi", "Hal yang mungkin belum kamu sadari."),
    ("Arah Saran", "arah_saran", "Langkah yang paling selaras untuk 7 hari ke depan."),
]
_SIGN = {"dukung": 1, "netral": 0, "waspada": -1}
_POL_LABEL = {"dukung": "Mendukung", "netral": "Tergantung sikapmu", "waspada": "Perlu waspada"}
_FALLBACK = {
    "sebagai_opsi": {"dukung": "Kartu ini memberi energi yang mendukung langkah ini, selama kamu menjalaninya dengan sadar.",
                     "netral": "Kartu ini tidak condong ke satu sisi; hasilnya sangat bergantung pada cara kamu menyikapinya.",
                     "waspada": "Kartu ini menunjukkan energi yang berat di sisi ini, jadi butuh persiapan ekstra sebelum melangkah."},
    "sebagai_risiko": {"dukung": "Risikonya relatif ringan, tapi tetap cek hal-hal kecil agar tidak terlena.",
                       "netral": "Risikonya bergantung pada keputusan lanjutan yang kamu ambil setelah ini.",
                       "waspada": "Risikonya nyata dan perlu rencana cadangan sebelum kamu memutuskan."},
    "faktor_tersembunyi": {"dukung": "Ada dukungan yang belum kamu sadari; cek siapa atau apa yang bisa membantumu.",
                           "netral": "Ada hal yang belum jelas; tanyakan dulu sebelum memutuskan.",
                           "waspada": "Ada kekhawatiran tersembunyi yang perlu kamu akui lebih dulu."},
    "arah_saran": {"dukung": "Ambil satu langkah kecil minggu ini yang menguji pilihan yang paling kamu condongi.",
                   "netral": "Kumpulkan satu informasi tambahan dalam 7 hari sebelum memutuskan.",
                   "waspada": "Tunda keputusan besar beberapa hari dan selesaikan dulu hal yang paling mengganjal."},
}


def key(slug):
    """slug kartu engine ('fool', 'cups_03') -> kunci data ('major_00', 'cups_03')."""
    from engine.tarot import TAROT_MAJOR_ARCANA
    return f"major_{TAROT_MAJOR_ARCANA.index(slug):02d}" if slug in TAROT_MAJOR_ARCANA else slug


@lru_cache(maxsize=1)
def _meta():
    return json.loads((_BASE / "decision_meta.json").read_text(encoding="utf-8"))


@lru_cache(maxsize=1)
def _texts():
    try:
        d = json.loads((_BASE / "decision.json").read_text(encoding="utf-8"))
        return d if isinstance(d, dict) else {}
    except (OSError, ValueError):
        return {}


def polarity(slug):
    m = _meta()[key(slug)]
    return m["polarity"], m["intensitas"]


def skor_kartu(slug):
    p, i = polarity(slug)
    return _SIGN[p] * i


def teks(slug, field):
    """(teks, placeholder?)"""
    t = (_texts().get(key(slug)) or {}).get(field)
    if isinstance(t, str) and t.strip():
        return t.strip(), False
    return _FALLBACK[field][polarity(slug)[0]], True


def kata_kunci(slug):
    k = (_texts().get(key(slug)) or {}).get("kata_kunci")
    return [x for x in k if isinstance(x, str)][:3] if isinstance(k, list) else []


def baca(cards):
    """cards = 7 slug. Return dict hasil lengkap."""
    if len(cards) != 7:
        raise ValueError("Decision Reveal butuh 7 kartu")
    pos, ph = [], False
    for i, slug in enumerate(cards):
        judul, field, mean = POSITIONS[i]
        t, p = teks(slug, field)
        ph = ph or p
        pol, it = polarity(slug)
        pos.append({"i": i, "slug": slug, "judul": judul, "makna": mean, "teks": t, "polarity": pol,
                    "label": _POL_LABEL[pol], "intensitas": it, "kunci": kata_kunci(slug)})
    a, b = skor_kartu(cards[1]) + skor_kartu(cards[2]), skor_kartu(cards[3]) + skor_kartu(cards[4])
    selisih = a - b
    unggul = "A" if selisih >= 2 else "B" if selisih <= -2 else None
    jelas = "cukup jelas" if abs(selisih) >= 4 else "tipis"
    if unggul:
        v = (f"Tebaran condong ke Pilihan {unggul} ({jelas}). Energinya lebih mendukung dan risikonya lebih terkelola "
             f"dibanding pilihan lain. Ini kecenderungan, bukan kepastian.")
    elif a >= 3 and b >= 3:
        v = "Kedua pilihan sama-sama didukung. Pilih berdasarkan nilai dan prioritas hidupmu, bukan karena takut salah."
    elif a <= -3 and b <= -3:
        v = "Kedua pilihan terasa berat. Pertimbangkan menunda, mencari opsi ketiga, atau memperkecil risiko dulu."
    else:
        v = "Kedua pilihan seimbang. Faktor tersembunyi dan arah saran di bawah bisa jadi pembeda."
    return {"cards": list(cards), "pos": pos, "skor": {"A": a, "B": b}, "unggul": unggul, "selisih": selisih,
            "jelas": jelas, "verdict": v, "placeholder": ph, "inti": polarity(cards[0])[0]}
