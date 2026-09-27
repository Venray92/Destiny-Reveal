"""
Engine scoring DISC — hitung gaya dominan (D/I/S/C) dari jawaban user.

Input: answers = {question_id (int): "A"/"B"/"C"/"D"} — huruf kolom yang
dipilih user di baris itu (BUKAN langsung dimensi DISC-nya, lihat
DISC_KEY di content/questionnaires/disc.py buat pemetaan kolom->dimensi).
"""

from content.questionnaires.disc_soal import DISC_DIMENSION_NAMES, DISC_KEY, DISC_QUESTIONS


def score_disc(answers: dict) -> dict:
    counts = {"D": 0, "I": 0, "S": 0, "C": 0}
    for q in DISC_QUESTIONS:
        pick = answers.get(q["id"])
        dimensi = DISC_KEY.get(pick)
        if dimensi:
            counts[dimensi] += 1

    top_score = max(counts.values())
    tied = sorted(k for k, v in counts.items() if v == top_score)
    tipe = tied[0]

    return {
        "tipe": tipe,
        "tipe_nama": DISC_DIMENSION_NAMES[tipe],
        "tipe_tied": tied if len(tied) > 1 else None,
        "counts": counts,
    }
