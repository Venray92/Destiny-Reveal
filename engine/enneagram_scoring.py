"""
Engine scoring Enneagram — hitung tipe inti (1-9) dari jawaban user.

Input: answers = {question_id (int): True/False} — True = "Setuju".
"""

from content.questionnaires.enneagram_soal import ENNEAGRAM_QUESTIONS, ENNEAGRAM_TYPE_NAMES


def score_enneagram(answers: dict) -> dict:
    counts = {t: 0 for t in range(1, 10)}
    for q in ENNEAGRAM_QUESTIONS:
        if answers.get(q["id"]):
            counts[q["type"]] += 1

    top_score = max(counts.values())
    tied = sorted(t for t, c in counts.items() if c == top_score)
    # Kalau ada lebih dari 1 tipe seri (skor sama persis) -- dokumen asli
    # bilang "baca deskripsi mendalam buat lihat mana yang paling
    # merepresentasikan" (butuh manusia mutusin). Buat kebutuhan engine
    # otomatis, kita ambil nomor tipe terkecil secara konsisten, tapi
    # tetap simpan daftar lengkap yang seri di "tipe_tied" biar UI bisa
    # kasih tau user kalau hasilnya sebenarnya seri, bukan tunggal.
    tipe = tied[0]

    return {
        "tipe": tipe,
        "tipe_nama": ENNEAGRAM_TYPE_NAMES[tipe],
        "tipe_tied": tied if len(tied) > 1 else None,
        "counts": counts,
    }
