"""
Bank soal Kuesioner DISC (24 baris forced-choice, pilih 1 dari 4 kata per
baris).

Sumber: draft soal dari Stev (chip.docx, 27 Sep 2026) — SUDAH DIPERBAIKI
di 6 dari 24 baris (nomor 2, 3, 13, 14, 17, 23) karena kata yang dipakai
gak cocok sama makna kolomnya (misal "Perfeksionis" itu ciri khas
Compliance/C, bukan Dominance/D, tapi di draft asli ditaro di kolom D).
Lihat catatan "[FIX]" di tiap baris yang diubah. 18 baris lainnya sudah
benar dari draft asli, tidak diubah.

Posisi kolom SELALU tetap: A=Influence, B=Compliance, C=Steadiness,
D=Dominance (lihat DISC_KEY di bawah) — cuma ISI KATA di 6 baris itu yang
diganti biar sesuai makna kolomnya.

Tiap soal: {"id": nomor (1-24), "options": {"A": kata, "B": kata,
"C": kata, "D": kata}}.
"""

DISC_QUESTIONS = [
    {"id": 1, "options": {"A": "Bersemangat", "B": "Teliti", "C": "Sabar", "D": "Tegas"}},
    {"id": 2, "options": {"A": "Ramah", "B": "Cermat", "C": "Konsisten", "D": "Agresif"}},  # [FIX] B: Mandiri->Cermat, D: Waspada->Agresif
    {"id": 3, "options": {"A": "Menghibur", "B": "Perfeksionis", "C": "Tenang", "D": "Kompetitif"}},  # [FIX] A: Kompetitif->Menghibur, B: Suka Menolong->Perfeksionis, D: Perfeksionis->Kompetitif
    {"id": 4, "options": {"A": "Inovatif", "B": "Berhati-hati", "C": "Pendengar", "D": "Berani"}},
    {"id": 5, "options": {"A": "Humoris", "B": "Rapi", "C": "Akomodatif", "D": "Dominan"}},
    {"id": 6, "options": {"A": "Suka Bicara", "B": "Kritis", "C": "Menghindari Konflik", "D": "Ambisius"}},
    {"id": 7, "options": {"A": "Ekspresif", "B": "Sistematis", "C": "Stabil", "D": "Mandiri"}},
    {"id": 8, "options": {"A": "Visioner", "B": "Skeptis", "C": "Setia", "D": "Gigih"}},
    {"id": 9, "options": {"A": "Spontan", "B": "Terorganisir", "C": "Tenang", "D": "Percaya Diri"}},
    {"id": 10, "options": {"A": "Mudah Bergaul", "B": "Analitis", "C": "Lembut", "D": "Berorientasi Hasil"}},
    {"id": 11, "options": {"A": "Persuasif", "B": "Detail", "C": "Kooperatif", "D": "Blak-blakan"}},
    {"id": 12, "options": {"A": "Antusias", "B": "Hati-hati", "C": "Santai", "D": "Pemimpin"}},
    {"id": 13, "options": {"A": "Penuh Ide", "B": "Suka Fakta", "C": "Konsisten", "D": "Suka Tantangan"}},  # [FIX] A<->D ditukar
    {"id": 14, "options": {"A": "Penggerak", "B": "Terencana", "C": "Penyayang", "D": "Menuntut"}},  # [FIX] C: Ramah->Penyayang, D: Diplomatik->Menuntut
    {"id": 15, "options": {"A": "Energik", "B": "Waspada", "C": "Sabar", "D": "Tegas"}},
    {"id": 16, "options": {"A": "Sosial", "B": "Terstruktur", "C": "Toleran", "D": "Berkuasa"}},
    {"id": 17, "options": {"A": "Optimis", "B": "Akurat", "C": "Damai", "D": "Memerintah"}},  # [FIX] D: Kritis->Memerintah
    {"id": 18, "options": {"A": "Aktif", "B": "Formal", "C": "Tenang", "D": "Berorientasi Target"}},
    {"id": 19, "options": {"A": "Menginspirasi", "B": "Teratur", "C": "Setia Kawan", "D": "Berani Ambil Risiko"}},
    {"id": 20, "options": {"A": "Populer", "B": "Perfeksionis", "C": "Mengalah", "D": "Mandiri"}},
    {"id": 21, "options": {"A": "Spontan", "B": "Logis", "C": "Kalem", "D": "Tegas"}},
    {"id": 22, "options": {"A": "Menarik", "B": "Teliti", "C": "Tenang", "D": "Kompetitif"}},
    {"id": 23, "options": {"A": "Ramah", "B": "Rinci", "C": "Sabar", "D": "Ambisius"}},  # [FIX] B: Konsisten->Rinci
    {"id": 24, "options": {"A": "Bersemangat", "B": "Terstruktur", "C": "Harmonis", "D": "Tegas"}},
]

# Posisi kolom -> dimensi DISC yang diwakilinya (TETAP, tidak berubah).
DISC_KEY = {"A": "I", "B": "C", "C": "S", "D": "D"}
DISC_DIMENSION_NAMES = {
    "D": "Dominance",
    "I": "Influence",
    "S": "Steadiness",
    "C": "Compliance (Conscientiousness)",
}
