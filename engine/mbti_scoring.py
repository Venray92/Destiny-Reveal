"""
Engine scoring MBTI — hitung 4 huruf tipe dari jawaban user.

Input: answers = {question_id (int): True/False} — True = "Setuju",
False = "Tidak Setuju". Wajib semua 32 nomor sudah terjawab sebelum
dipanggil (dijamin oleh state machine di views/loadingpage_mendalam.py).
"""

from content.questionnaires.mbti_soal import MBTI_DICHOTOMIES, MBTI_QUESTIONS


def score_mbti(answers: dict) -> dict:
    counts = {letter: 0 for pair in MBTI_DICHOTOMIES for letter in pair}
    for q in MBTI_QUESTIONS:
        if answers.get(q["id"]):
            counts[q["letter"]] += 1

    letters = []
    for a, b in MBTI_DICHOTOMIES:
        if counts[a] >= counts[b]:
            # Tie (2-2) -- dokumen asli nggak nentuin tie-break, jadi kita
            # pilih huruf PERTAMA di pasangan (E/S/T/J) secara konsisten
            # biar hasilnya selalu sama tiap kali dihitung ulang dari
            # jawaban yang sama (bukan pilihan acak).
            letters.append(a)
        else:
            letters.append(b)

    return {"tipe": "".join(letters), "counts": counts}
