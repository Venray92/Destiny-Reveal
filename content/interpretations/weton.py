"""
Konten Weton (5 kategori, berdasarkan PASARAN).

Key dict ini HARUS sama persis dengan nilai "pasaran" dari engine/weton.py
(hitung_weton()["pasaran"]): Legi, Pahing, Pon, Wage, Kliwon.

KEPUTUSAN SCOPE (dikonfirmasi 26 Sep 2026): konten dikelompokkan
berdasarkan PASARAN, bukan neptu maupun kombinasi hari+pasaran (35
kategori). Alasannya: dalam primbon Jawa, pasaran itu yang secara
tradisional dipakai untuk membaca watak/karakter dasar seseorang, sementara
neptu (hari + pasaran) lebih dipakai untuk hitungan kecocokan/hari baik,
bukan gambaran kepribadian. Neptu tetap dihitung & ditampilkan sebagai
info pendukung di hasil, tapi bukan dasar kategori konten.

Struktur tiap entri sama persis dengan DUMMY_RESULTS di views/revealpage.py,
DITAMBAH placeholder "{hari}" dan "{neptu}" di dalam field yang relevan
(title, p1) yang perlu di-.format() saat dipakai, karena hari & neptu itu
spesifik per orang meskipun pasarannya sama.
"""

WETON_CONTENT = {
    "Legi": {
        "tagline": "☾ Pasaran Legi",
        "chip": "WETON",
        "title": "{hari} Legi — Neptu {neptu}, Pembawa Ketenangan",
        "p1_label": "Siapa Kamu",
        "p1": "Menurut primbon Jawa, kamu lahir dengan pasaran Legi, yang jatuh pada hari {hari} "
              "dengan neptu total {neptu}. Pasaran Legi sering dikaitkan dengan sosok yang membawa "
              "ketenangan bagi lingkungan sekitarnya, tempat orang lain merasa nyaman bercerita dan "
              "meminta pendapat. Kehadiranmu cenderung meredakan suasana yang tegang, bukan "
              "memperkeruhnya.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kepekaanmu terhadap perasaan orang lain adalah kekuatan besar yang tidak semua orang "
              "punya. Namun karena terlalu sering memikirkan perasaan orang lain, kamu kadang menunda "
              "kepentinganmu sendiri, dan itu bisa membuatmu kelelahan tanpa disadari oleh orang di "
              "sekelilingmu.",
        "quote": "Menjaga perasaan orang lain itu baik, asal tidak sampai melupakan perasaanmu "
                 "sendiri.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Sesekali, latih diri untuk mengatakan apa yang sebenarnya kamu butuhkan, bukan hanya "
              "apa yang membuat orang lain nyaman. Orang-orang terdekatmu justru akan lebih menghargai "
              "kejujuran itu.",
    },
    "Pahing": {
        "tagline": "☾ Pasaran Pahing",
        "chip": "WETON",
        "title": "{hari} Pahing — Neptu {neptu}, Sosok yang Bersemangat",
        "p1_label": "Siapa Kamu",
        "p1": "Menurut primbon Jawa, kamu lahir dengan pasaran Pahing, yang jatuh pada hari {hari} "
              "dengan neptu total {neptu}. Pasaran Pahing identik dengan semangat yang menyala dan "
              "keinginan kuat untuk selalu tampil terbaik. Kamu punya energi yang membuatmu tidak "
              "puas hanya berdiam di tempat, dan selalu mendorong diri sendiri untuk berkembang.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Semangat dan ambisimu membuat orang lain melihatmu sebagai sosok yang pantang menyerah "
              "dalam mengejar sesuatu. Kamu juga cenderung berani mengambil risiko demi hasil yang "
              "lebih besar. Namun semangat yang menggebu ini kadang membuatmu kurang sabar terhadap "
              "orang lain yang bergerak lebih lambat, atau terhadap proses yang belum menunjukkan "
              "hasil secepat yang kamu harapkan.",
        "quote": "Semangat besar akan lebih membawa hasil kalau disertai kesabaran menunggu waktu "
                 "yang tepat.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Minggu ini, coba beri ruang pada orang lain untuk bergerak dengan kecepatan mereka "
              "sendiri, tanpa terburu-buru mendorong mereka menyamai temponu.",
    },
    "Pon": {
        "tagline": "☾ Pasaran Pon",
        "chip": "WETON",
        "title": "{hari} Pon — Neptu {neptu}, Penengah yang Bijaksana",
        "p1_label": "Siapa Kamu",
        "p1": "Menurut primbon Jawa, kamu lahir dengan pasaran Pon, yang jatuh pada hari {hari} "
              "dengan neptu total {neptu}. Pasaran Pon sering dikaitkan dengan sosok yang bijaksana "
              "dan pandai menjaga keseimbangan dalam hubungan dengan orang lain. Kamu cenderung "
              "berpikir matang sebelum bertindak, dan jarang membuat keputusan yang terburu-buru.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kebijaksanaan dan kemampuanmu menjaga keharmonisan membuat orang lain sering "
              "menjadikanmu penengah saat ada perbedaan pendapat. Kamu juga dipercaya karena "
              "pertimbanganmu yang matang. Namun kehati-hatian ini kadang membuatmu terlalu lama "
              "menimbang-nimbang, sampai kesempatan yang seharusnya bisa kamu ambil justru "
              "terlewatkan.",
        "quote": "Pertimbangan yang matang itu penting, tapi ada kalanya keberanian mengambil "
                 "keputusan lebih berarti dari kesempurnaan pertimbangan itu sendiri.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Ketika dihadapkan pada satu keputusan kecil minggu ini, coba beri batas waktu untuk "
              "menimbang, lalu putuskan sebelum batas waktu itu habis, alih-alih terus menunda.",
    },
    "Wage": {
        "tagline": "☾ Pasaran Wage",
        "chip": "WETON",
        "title": "{hari} Wage — Neptu {neptu}, Pribadi yang Mandiri",
        "p1_label": "Siapa Kamu",
        "p1": "Menurut primbon Jawa, kamu lahir dengan pasaran Wage, yang jatuh pada hari {hari} "
              "dengan neptu total {neptu}. Pasaran Wage sering dikaitkan dengan sosok yang mandiri dan "
              "punya pendirian kuat. Kamu tidak mudah terpengaruh pendapat orang lain, dan lebih "
              "memilih menentukan sendiri arah hidupmu berdasarkan penilaianmu sendiri.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kemandirian dan keteguhan pendirianmu membuatmu jarang bergantung pada orang lain "
              "untuk merasa yakin. Kamu juga cenderung tenang menghadapi tekanan dari luar. Namun "
              "sikap mandiri ini kadang membuatmu enggan meminta bantuan bahkan ketika kamu benar-"
              "benar membutuhkannya, sehingga terasa lebih berat menjalani sesuatu sendirian.",
        "quote": "Kemandirian itu kekuatan, tapi meminta bantuan pada saat yang tepat juga bukan "
                 "tanda kelemahan.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Minggu ini, coba minta bantuan pada satu hal kecil yang sebenarnya bisa kamu tangani "
              "sendiri, dan rasakan bahwa membiarkan orang lain membantu juga bisa terasa "
              "menenangkan.",
    },
    "Kliwon": {
        "tagline": "☾ Pasaran Kliwon",
        "chip": "WETON",
        "title": "{hari} Kliwon — Neptu {neptu}, Sosok yang Penuh Kepekaan",
        "p1_label": "Siapa Kamu",
        "p1": "Menurut primbon Jawa, kamu lahir dengan pasaran Kliwon, yang jatuh pada hari {hari} "
              "dengan neptu total {neptu}. Pasaran Kliwon sering dikaitkan dengan kepekaan batin yang "
              "dalam dan kemampuan merasakan hal-hal yang tidak terucap oleh orang lain. Kamu punya "
              "intuisi yang tajam, dan sering kali firasatmu tentang sesuatu ternyata benar.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kepekaan dan intuisimu membuatmu mudah memahami situasi maupun perasaan orang lain "
              "tanpa perlu penjelasan panjang. Kamu juga punya sisi spiritual yang membuatmu tenang "
              "menghadapi ketidakpastian. Namun kepekaan yang besar ini kadang membuatmu mudah "
              "menyerap energi negatif dari sekitarmu, sehingga suasana hatimu jadi mudah terpengaruh "
              "oleh keadaan orang lain.",
        "quote": "Kepekaan itu anugerah, tapi kamu juga berhak menjaga jarak dari energi yang tidak "
                 "membuatmu nyaman.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Ketika merasa energimu terkuras oleh suasana atau orang lain minggu ini, coba luangkan "
              "waktu sendiri sejenak untuk memulihkan diri sebelum melanjutkan aktivitas.",
    },
}
