"""
Bank soal Kuesioner Enneagram (36 pernyataan, 4 soal per tipe, format
Setuju/Tidak Setuju).

Sumber: draft soal dari Stev (chip.docx, 27 Sep 2026) — sudah dicek, semua
36 nomor dan pengelompokan 4-soal-per-tipe sudah benar, TIDAK ada
perubahan isi dari draft aslinya.

Tiap soal: {"id": nomor (1-36), "type": nomor tipe (1-9), "text": teks
pernyataan}.
"""

ENNEAGRAM_QUESTIONS = [
    # ── Tipe 1: The Reformer ──
    {"id": 1, "type": 1, "text": "Saya memiliki standar batin yang sangat tinggi dan merasa terganggu jika melihat sesuatu dikerjakan secara asal-asalan."},
    {"id": 2, "type": 1, "text": "Saya sering menjadi pengkritik paling keras bagi diri saya sendiri ketika melakukan kesalahan kecil."},
    {"id": 3, "type": 1, "text": "Bagi saya, selalu ada batasan yang jelas antara apa yang mutlak benar dan apa yang mutlak salah."},
    {"id": 4, "type": 1, "text": "Saya merasa bertanggung jawab untuk memperbaiki sistem atau situasi yang rusak di sekitar saya agar menjadi ideal."},

    # ── Tipe 2: The Helper ──
    {"id": 5, "type": 2, "text": "Saya sering kali lebih mendahulukan kebutuhan orang lain ketimbang mengurus diri saya sendiri."},
    {"id": 6, "type": 2, "text": "Saya merasa sangat dibutuhkan dan berharga ketika ada orang yang datang meminta bantuan kepada saya."},
    {"id": 7, "type": 2, "text": "Terkadang saya merasa sakit hati atau kecewa jika kebaikan yang saya beri tidak dibalas dengan perhatian serupa."},
    {"id": 8, "type": 2, "text": "Saya sangat peka terhadap perubahan suasana hati atau perasaan orang-orang yang ada di dekat saya."},

    # ── Tipe 3: The Achiever ──
    {"id": 9, "type": 3, "text": "Saya mengukur nilai diri saya sebagian besar dari seberapa banyak pencapaian dan kesuksesan yang telah saya raih."},
    {"id": 10, "type": 3, "text": "Saya sangat menjaga citra diri dan ingin selalu terlihat kompeten serta sukses di mata orang lain."},
    {"id": 11, "type": 3, "text": "Saya adalah tipe orang yang sangat fokus pada target, efisiensi waktu, dan hasil akhir yang nyata."},
    {"id": 12, "type": 3, "text": "Saya merasa tidak nyaman atau gelisah jika harus menghabiskan waktu seharian tanpa menghasilkan apa pun yang produktif."},

    # ── Tipe 4: The Individualist ──
    {"id": 13, "type": 4, "text": "Saya sering merasa berbeda dari orang kebanyakan dan merasa tidak ada yang benar-benar memahami diri saya."},
    {"id": 14, "type": 4, "text": "Saya mengekspresikan kedalaman emosi dan pengalaman batin saya melalui seni, tulisan, atau gaya hidup yang khas."},
    {"id": 15, "type": 4, "text": "Saya cenderung merindukan hal-hal yang tidak ada atau merasa ada sesuatu yang fundamental hilang dalam hidup saya."},
    {"id": 16, "type": 4, "text": "Saya sangat menghindari menjadi orang yang \"biasa-biasa saja\" atau sama persis dengan orang lain di keramaian."},

    # ── Tipe 5: The Investigator ──
    {"id": 17, "type": 5, "text": "Saya lebih suka mengamati situasi dari luar secara objektif daripada langsung terjun terlibat di dalamnya."},
    {"id": 18, "type": 5, "text": "Saya sangat menghargai privasi dan membutuhkan banyak waktu menyendiri untuk mengisi ulang energi mental saya."},
    {"id": 19, "type": 5, "text": "Saya senang mendalami suatu topik atau bidang ilmu secara ekstrem sampai saya benar-benar menguasainya."},
    {"id": 20, "type": 5, "text": "Saya sering merasa dunia luar menuntut terlalu banyak energi, sehingga saya suka membatasi keterlibatan sosial."},

    # ── Tipe 6: The Loyalist ──
    {"id": 21, "type": 6, "text": "Saya memiliki kewaspadaan tinggi dan selalu memikirkan skenario terburuk sebelum mengambil sebuah keputusan."},
    {"id": 22, "type": 6, "text": "Kesetiaan dalam persahabatan atau tim adalah hal yang paling mutlak dan tidak bisa ditawar bagi saya."},
    {"id": 23, "type": 6, "text": "Saya cenderung skeptis dan tidak langsung percaya pada figur otoritas atau aturan baru sebelum terbukti aman."},
    {"id": 24, "type": 6, "text": "Saya sering merasa cemas mengenai masa depan dan mencari kepastian agar merasa aman dari bahaya."},

    # ── Tipe 7: The Enthusiast ──
    {"id": 25, "type": 7, "text": "Saya sangat menyukai variasi, pengalaman baru, dan mudah merasa bosan jika terjebak dalam rutinitas monoton."},
    {"id": 26, "type": 7, "text": "Saya selalu berusaha melihat sisi positif dari segala hal dan menghindari pembicaraan yang terlalu suram atau sedih."},
    {"id": 27, "type": 7, "text": "Pikiran saya sering melompat-lompat dengan banyak ide proyek menarik yang ingin saya coba sekaligus."},
    {"id": 28, "type": 7, "text": "Saya takut merasa terkekang, terbatas, atau tertinggal dari berbagai keseruan yang sedang terjadi di luar sana."},

    # ── Tipe 8: The Challenger ──
    {"id": 29, "type": 8, "text": "Saya tidak ragu untuk menghadapi konflik secara langsung demi membela keadilan atau melindungi orang yang lemah."},
    {"id": 30, "type": 8, "text": "Saya lebih suka memegang kendali penuh atas situasi dan nasib saya sendiri daripada diatur oleh orang lain."},
    {"id": 31, "type": 8, "text": "Orang-orang sering menganggap saya terlalu blak-blakan, dominan, atau intimidatif saat berbicara."},
    {"id": 32, "type": 8, "text": "Menunjukkan kelemahan atau kerentanan di hadapan orang lain adalah hal yang sangat sulit bagi saya."},

    # ── Tipe 9: The Peacemaker ──
    {"id": 33, "type": 9, "text": "Saya sangat menghindari konflik terbuka dan sering menjadi penengah atau pengalah agar suasana tetap tenang."},
    {"id": 34, "type": 9, "text": "Saya terkadang kesulitan mengenali keinginan diri sendiri karena terlalu sering mengikuti arus atau keinginan orang lain."},
    {"id": 35, "type": 9, "text": "Saya memiliki pembawaan yang santai, sabar, dan tidak mudah merasa stres oleh masalah eksternal."},
    {"id": 36, "type": 9, "text": "Saya cenderung menunda-nunda pekerjaan berat atau mengalihkan perhatian pada hal yang nyaman demi menghindari ketegangan."},
]

ENNEAGRAM_TYPE_NAMES = {
    1: "The Reformer",
    2: "The Helper",
    3: "The Achiever",
    4: "The Individualist",
    5: "The Investigator",
    6: "The Loyalist",
    7: "The Enthusiast",
    8: "The Challenger",
    9: "The Peacemaker",
}
