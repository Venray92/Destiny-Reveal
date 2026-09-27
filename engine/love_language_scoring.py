"""
Engine scoring Love Language — hitung Primary + Secondary Love Language
dari jawaban user.

Input: answers = {question_id (int): "A"/"B"} — pernyataan mana yang
dipilih user di pasangan itu. Kategori tiap pilihan diambil dari
content/questionnaires/love_language.py (field "category" per opsi,
kunci hasil rekonstruksi ulang karena kunci di draft asli rusak/gak
lengkap -- lihat catatan di file itu).
"""

from content.questionnaires.love_language_soal import (
    LOVE_LANGUAGE_NAMES,
    LOVE_LANGUAGE_QUESTIONS,
    LOVE_LANGUAGE_SLUG,
)


def score_love_language(answers: dict) -> dict:
    counts = {k: 0 for k in LOVE_LANGUAGE_NAMES}
    for q in LOVE_LANGUAGE_QUESTIONS:
        pick = answers.get(q["id"])
        if pick in ("A", "B"):
            category = q[pick]["category"]
            counts[category] += 1

    ranked = sorted(counts, key=lambda k: counts[k], reverse=True)
    primary, secondary = ranked[0], ranked[1]

    return {
        "primary": primary,
        "secondary": secondary,
        "primary_nama": LOVE_LANGUAGE_NAMES[primary],
        "secondary_nama": LOVE_LANGUAGE_NAMES[secondary],
        "primary_slug": LOVE_LANGUAGE_SLUG[primary],
        "counts": counts,
    }
