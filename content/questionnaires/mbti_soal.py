"""
Bank soal Kuesioner MBTI (32 pernyataan, format Setuju/Tidak Setuju).

Sumber: draft soal dari Stev (chip.docx, 27 Sep 2026), sudah dicek — semua
32 nomor dan pengelompokan 8-soal-per-dikotomi sudah benar, TIDAK ada
perubahan isi dari draft aslinya.

Tiap soal: {"id": nomor (1-32), "letter": salah satu dari E/I/S/N/T/F/J/P,
"text": teks pernyataan}. "letter" menandakan poin ini nambah skor ke huruf
apa kalau user jawab "Setuju" — dipakai oleh engine/mbti.py buat scoring
(lihat score_mbti()).
"""

MBTI_QUESTIONS = [
    # ── Bagian 1: Energi (Extraversion / Introversion) ──
    {"id": 1, "letter": "E", "text": "Saya merasa energi saya langsung terisi penuh kembali setelah menghabiskan waktu di tengah keramaian atau pesta yang meriah."},
    {"id": 2, "letter": "I", "text": "Setelah seharian beraktivitas sosial, hal yang paling saya butuhkan adalah duduk sendirian di kamar dalam keheningan total."},
    {"id": 3, "letter": "E", "text": "Saya lebih suka mendiskusikan ide baru secara langsung dengan orang lain sambil berbicara, ketimbang merenungkannya sendirian terlebih dahulu."},
    {"id": 4, "letter": "I", "text": "Saya sering merasa lelah secara mental bukan karena pekerjaannya, tetapi karena terlalu banyak basa-basi dengan orang lain."},
    {"id": 5, "letter": "E", "text": "Ketika dihadapkan pada masalah pelik, reaksi pertama saya adalah menelepon seseorang untuk meminta pendapat atau sekadar curhat."},
    {"id": 6, "letter": "I", "text": "Saya lebih memilih menulis email panjang yang detail ketimbang harus melakukan panggilan telepon atau video call spontan."},
    {"id": 7, "letter": "E", "text": "Saya merasa tidak masalah jika harus berkenalan dan mengobrol dengan orang asing yang duduk sebelah saya di transportasi umum."},
    {"id": 8, "letter": "I", "text": "Saya sering menunda membalas pesan teks atau chat bukan karena malas, tapi karena butuh waktu lama untuk merangkai respons yang tepat."},

    # ── Bagian 2: Informasi (Sensing / Intuition) ──
    {"id": 9, "letter": "S", "text": "Saya lebih mempercayai bukti nyata, data statistik, dan pengalaman masa lalu daripada firasat atau teori abstrak."},
    {"id": 10, "letter": "N", "text": "Saya lebih suka memikirkan \"kemungkinan-kemungkinan besar di masa depan\" ketimbang meributkan detail teknis di masa kini."},
    {"id": 11, "letter": "S", "text": "Saat membaca sebuah cerita atau instruksi, saya cenderung fokus pada urutan kejadian nyata yang tertulis secara literal."},
    {"id": 12, "letter": "N", "text": "Saya sering melihat makna tersembunyi, simbol, atau pola di balik kejadian sehari-hari yang sering dilewatkan orang lain."},
    {"id": 13, "letter": "S", "text": "Saya lebih menyukai hobi atau pekerjaan yang menghasilkan sesuatu yang konkret, praktis, dan bisa langsung dilihat hasilnya."},
    {"id": 14, "letter": "N", "text": "Saya mudah merasa bosan dengan rutinitas yang monoton dan berulang karena otak saya selalu mencari inovasi atau cara baru."},
    {"id": 15, "letter": "S", "text": "Bagi saya, ungkapan \"burung di tangan lebih baik daripada seribu di dahan\" adalah prinsip hidup yang masuk akal."},
    {"id": 16, "letter": "N", "text": "Saya sering melamun memikirkan skenario-skenario hipotetis (misalnya: \"bagaimana kalau hukum fisika diubah?\") yang tidak ada hubungannya dengan kenyataan."},

    # ── Bagian 3: Keputusan (Thinking / Feeling) ──
    {"id": 17, "letter": "T", "text": "Dalam sebuah argumen, kebenaran dan logika objektif jauh lebih penting daripada menjaga perasaan orang agar tidak tersinggung."},
    {"id": 18, "letter": "F", "text": "Keputusan terbaik adalah keputusan yang tidak melukai perasaan siapa pun, bahkan jika itu berarti mengorbankan sedikit efisiensi."},
    {"id": 19, "letter": "T", "text": "Saya sering dianggap terlalu blak-blakan atau dingin karena saya lebih suka berbicara apa adanya tanpa membungkusnya dengan basa-basi emosional."},
    {"id": 20, "letter": "F", "text": "Saya bisa dengan mudah merasakan beban emosional atau kesedihan orang lain di ruangan yang sama, seolah-olah itu milik saya sendiri."},
    {"id": 21, "letter": "T", "text": "Saat seseorang menceritakan masalahnya, refleks pertama saya adalah langsung memberikan solusi logis dan langkah praktis untuk memperbaikinya."},
    {"id": 22, "letter": "F", "text": "Ketika seseorang bercerita, hal utama yang mereka butuhkan bukanlah solusi, melainkan empati dan validasi bahwa perasaan mereka sah."},
    {"id": 23, "letter": "T", "text": "Saya menilai aturan dibuat untuk ditegakkan secara adil dan merata, tanpa memandang kedekatan emosional saya dengan pelanggarnya."},
    {"id": 24, "letter": "F", "text": "Saya sulit mengatakan \"tidak\" kepada orang lain karena saya selalu membayangkan betapa kecewanya mereka jika saya menolak."},

    # ── Bagian 4: Gaya Hidup (Judging / Perceiving) ──
    {"id": 25, "letter": "J", "text": "Saya merasa cemas dan tidak tenang jika liburan atau agenda harian saya tidak direncanakan dengan rinci sejak awal."},
    {"id": 26, "letter": "P", "text": "Saya lebih menikmati hidup mengalir secara spontan dan membenci jadwal yang terlalu ketat atau mengikat."},
    {"id": 27, "letter": "J", "text": "Saya selalu menyelesaikan tugas atau pekerjaan jauh hari sebelum tenggat waktu (deadline) berakhir agar bisa tidur dengan tenang."},
    {"id": 28, "letter": "P", "text": "Saya bekerja paling produktif dan kreatif justru saat berada di bawah tekanan mendesak mendekati deadline (sistem kebut semalam)."},
    {"id": 29, "letter": "J", "text": "Meja kerja atau kamar saya harus selalu tertata rapi agar pikiran saya juga bisa fokus dan teratur."},
    {"id": 30, "letter": "P", "text": "Bagi saya, kekacauan (messiness) di sekitar saya bukanlah masalah besar selama saya tahu di mana letak barang-barang saya."},
    {"id": 31, "letter": "J", "text": "Saya merasa sangat terganggu jika rencana yang sudah disusun tiba-tiba berubah di detik-detik terakhir."},
    {"id": 32, "letter": "P", "text": "Saya lebih suka membiarkan pintu tetap terbuka untuk peluang lain, sehingga saya jarang berkomitmen pada satu rencana secara kaku."},
]

# Pasangan kutub yang dibandingkan buat nentuin 4 huruf hasil akhir.
MBTI_DICHOTOMIES = [("E", "I"), ("S", "N"), ("T", "F"), ("J", "P")]
