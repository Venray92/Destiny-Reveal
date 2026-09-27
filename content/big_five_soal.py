"""
Bank soal Kuesioner Big Five (35 pernyataan, skala 1-5).

Sumber: draft soal dari Stev (chip.docx, 27 Sep 2026) — sudah dicek, semua
35 nomor + daftar item reverse (3,7,9,11,13,16,18,20,23,25,27,30,32,34)
KONSISTEN sama penandaan (Reverse) di tiap soalnya, TIDAK ada perubahan
isi dari draft aslinya.

Tiap soal: {"id": nomor (1-35), "trait": salah satu dari O/C/E/A/N,
"text": teks pernyataan, "reverse": True/False}.
"reverse": True artinya skor mentahnya harus dibalik dulu (skor_baru = 6 -
skor_asli) sebelum dijumlah — lihat engine/big_five.py score_big_five().
"""

BIG_FIVE_QUESTIONS = [
    # ── Openness to Experience ──
    {"id": 1, "trait": "O", "reverse": False, "text": "Saya sering merenungkan ide-ide abstrak atau filosofis yang tidak memiliki jawaban pasti."},
    {"id": 2, "trait": "O", "reverse": False, "text": "Saya sangat menikmati seni, musik, atau puisi yang menantang cara pandang saya terhadap dunia."},
    {"id": 3, "trait": "O", "reverse": True, "text": "Saya lebih menyukai rutinitas yang stabil dan dapat ditebak ketimbang mencoba hal-hal baru yang asing."},
    {"id": 4, "trait": "O", "reverse": False, "text": "Saya memiliki rasa ingin tahu yang besar terhadap cara kerja berbagai hal di alam semesta."},
    {"id": 5, "trait": "O", "reverse": False, "text": "Saya senang membayangkan skenario alternatif atau dunia fiksi yang rumit di dalam kepala saya."},
    {"id": 6, "trait": "O", "reverse": False, "text": "Saya merasa ide-ide tradisional atau konvensional seringkali membatasi potensi berpikir saya."},
    {"id": 7, "trait": "O", "reverse": True, "text": "Saya jarang tertarik pada topik ilmiah, seni rupa, atau diskusi teoretis yang mendalam."},

    # ── Conscientiousness ──
    {"id": 8, "trait": "C", "reverse": False, "text": "Saya selalu membuat daftar rencana atau jadwal terperinci sebelum memulai sebuah proyek besar."},
    {"id": 9, "trait": "C", "reverse": True, "text": "Saya sering meninggalkan barang-barang berserakan begitu saja tanpa merapikannya kembali."},
    {"id": 10, "trait": "C", "reverse": False, "text": "Saya memiliki komitmen kerja yang kuat dan jarang menunda-nunda tugas hingga batas waktu akhir."},
    {"id": 11, "trait": "C", "reverse": True, "text": "Meja kerja atau ruang pribadi saya cenderung berantakan dan sulit menemukan sesuatu dengan cepat."},
    {"id": 12, "trait": "C", "reverse": False, "text": "Saya adalah tipe orang yang sangat teliti dan memeriksa ulang pekerjaan sekecil apa pun agar bebas dari kesalahan."},
    {"id": 13, "trait": "C", "reverse": True, "text": "Saya sering bertindak secara spontan tanpa memikirkan konsekuensi jangka panjang dari tindakan saya."},
    {"id": 14, "trait": "C", "reverse": False, "text": "Saya memegang teguh janji dan tanggung jawab yang sudah saya ambil kepada orang lain."},

    # ── Extraversion ──
    {"id": 15, "trait": "E", "reverse": False, "text": "Saya merasa hidup saya lebih bersemangat ketika dikelilingi oleh banyak orang dalam suatu kegiatan sosial."},
    {"id": 16, "trait": "E", "reverse": True, "text": "Saya lebih suka menjadi pendiam dan menghindari peran sebagai pusat perhatian di dalam kelompok."},
    {"id": 17, "trait": "E", "reverse": False, "text": "Saya mudah memulai percakapan dengan orang yang baru pertama kali saya temui."},
    {"id": 18, "trait": "E", "reverse": True, "text": "Saya sering merasa cepat terkuras energinya dan lebih memilih menghabiskan akhir pekan seorang diri di rumah."},
    {"id": 19, "trait": "E", "reverse": False, "text": "Saya memancarkan energi yang ceria, antusias, dan ekspresif saat mengekspresikan emosi saya."},
    {"id": 20, "trait": "E", "reverse": True, "text": "Dalam sebuah rapat atau diskusi, saya cenderung pasif dan jarang sekali menyuarakan pendapat duluan."},
    {"id": 21, "trait": "E", "reverse": False, "text": "Saya menyukai sensasi atau petualangan yang memacu adrenalin dan keramaian yang dinamis."},

    # ── Agreeableness ──
    {"id": 22, "trait": "A", "reverse": False, "text": "Saya selalu berusaha mengutamakan kepentingan orang lain di atas kepentingan saya sendiri jika mereka membutuhkannya."},
    {"id": 23, "trait": "A", "reverse": True, "text": "Saya cenderung bersikap skeptis, curiga, dan tidak mudah percaya pada niat baik orang lain."},
    {"id": 24, "trait": "A", "reverse": False, "text": "Saya merasa tidak nyaman jika harus terlibat dalam konflik terbuka atau berdebat sengit dengan orang lain."},
    {"id": 25, "trait": "A", "reverse": True, "text": "Terkadang saya senang melontarkan kritik pedas atau menyanggah pendapat orang lain demi membuktikan poin saya."},
    {"id": 26, "trait": "A", "reverse": False, "text": "Saya memiliki rasa iba yang sangat tinggi terhadap orang yang sedang kesusahan atau menderita."},
    {"id": 27, "trait": "A", "reverse": True, "text": "Saya lebih suka bekerja secara mandiri dan kompetitif daripada harus berkompromi dalam kerja tim."},
    {"id": 28, "trait": "A", "reverse": False, "text": "Saya mudah memaafkan kesalahan orang lain dan jarang menyimpan dendam masa lalu."},

    # ── Neuroticism / Emotional Stability ──
    {"id": 29, "trait": "N", "reverse": False, "text": "Saya sering merasa cemas atau khawatir berlebihan terhadap hal-hal sepele yang belum tentu terjadi."},
    {"id": 30, "trait": "N", "reverse": True, "text": "Saya memiliki mental yang tangguh dan tidak mudah goyah ketika menghadapi tekanan hidup yang berat."},
    {"id": 31, "trait": "N", "reverse": False, "text": "Suasana hati (mood) saya bisa berubah dengan sangat drastis dan cepat dalam waktu singkat."},
    {"id": 32, "trait": "N", "reverse": True, "text": "Saya jarang merasa panik dan bisa tetap tenang di tengah situasi darurat yang kacau."},
    {"id": 33, "trait": "N", "reverse": False, "text": "Saya sering merasa kewalahan menghadapi masalah hidup dan merasa tidak sanggup lagi menanggungnya."},
    {"id": 34, "trait": "N", "reverse": True, "text": "Saya jarang merasa insecure atau meragukan kemampuan diri saya sendiri di hadapan orang lain."},
    {"id": 35, "trait": "N", "reverse": False, "text": "Kritik kecil dari orang lain bisa sangat mengganggu pikiran saya sepanjang hari."},
]

BIG_FIVE_TRAITS = ["O", "C", "E", "A", "N"]
BIG_FIVE_TRAIT_NAMES = {
    "O": "Openness",
    "C": "Conscientiousness",
    "E": "Extraversion",
    "A": "Agreeableness",
    "N": "Neuroticism",
}
# Slug dipakai buat cari gambar kartu (assets/cards/big_five/<slug>.png).
BIG_FIVE_TRAIT_SLUG = {
    "O": "openness",
    "C": "conscientiousness",
    "E": "extraversion",
    "A": "agreeableness",
    "N": "neuroticism",
}
