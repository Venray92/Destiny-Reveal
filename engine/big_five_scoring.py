"""
Engine scoring Big Five — hitung skor + level (Rendah/Sedang/Tinggi) per
5 trait dari jawaban user.

Input: answers = {question_id (int): skor 1-5}. Item reverse dibalik
otomatis (6 - skor_asli) berdasarkan flag "reverse" di
content/questionnaires/big_five.py — sama persis rumus & daftar nomor
reverse dari draft asli Stev (sudah dicek konsisten).
"""

from content.questionnaires.big_five_soal import (
    BIG_FIVE_QUESTIONS,
    BIG_FIVE_TRAIT_SLUG,
    BIG_FIVE_TRAITS,
)


def _level(score: int) -> str:
    if score <= 17:
        return "Rendah"
    if score <= 24:
        return "Sedang"
    return "Tinggi"


def score_big_five(answers: dict) -> dict:
    scores = {t: 0 for t in BIG_FIVE_TRAITS}
    for q in BIG_FIVE_QUESTIONS:
        raw = answers.get(q["id"], 3)  # fallback netral kalau entah kenapa kosong
        val = 6 - raw if q["reverse"] else raw
        scores[q["trait"]] += val

    levels = {t: _level(s) for t, s in scores.items()}
    # Trait dengan skor tertinggi dipakai buat pilih gambar kartu teaser
    # (bukan "tipe" absolut — Big Five memang bukan sistem bertipe, tapi
    # butuh SATU gambar representatif buat kartu di loading page).
    dominant_trait = max(scores, key=scores.get)

    return {
        "scores": scores,
        "levels": levels,
        "dominant_trait": dominant_trait,
        "dominant_slug": BIG_FIVE_TRAIT_SLUG[dominant_trait],
    }
