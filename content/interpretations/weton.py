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

REVISI (26 Sep 2026 malam): isi p1/p2/p3 diperpanjang 2-3x lipat dari versi
sebelumnya (per instruksi Stev), supaya laporannya terasa lebih bernilai
dan aplikatif, bukan cuma label singkat. Placeholder {hari}/{neptu} tetap
dipertahankan persis di posisi yang sama.
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
              "memperkeruhnya. Dalam banyak kasus, kamu jadi tempat teman-teman atau keluarga singgah "
              "dulu sebelum mereka mengambil keputusan besar, karena cara bicaramu yang tenang membuat "
              "mereka merasa lebih jernih memikirkan masalahnya sendiri. Di lingkungan kerja, sifat ini "
              "membuatmu sering dipercaya memegang peran yang butuh kesabaran tinggi, seperti "
              "menengahi konflik antar rekan atau menjaga hubungan baik dengan klien yang sensitif. "
              "Di rumah pun, kamu biasanya jadi sosok yang menjaga suasana tetap adem, bahkan ketika "
              "anggota keluarga lain sedang emosi.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kepekaanmu terhadap perasaan orang lain adalah kekuatan besar yang tidak semua orang "
              "punya. Namun karena terlalu sering memikirkan perasaan orang lain, kamu kadang menunda "
              "kepentinganmu sendiri, dan itu bisa membuatmu kelelahan tanpa disadari oleh orang di "
              "sekelilingmu. Kekuatan ini juga membuatmu jadi pendengar yang baik dalam hubungan dekat, "
              "karena kamu jarang buru-buru memberi nasihat sebelum benar-benar memahami apa yang "
              "sedang dirasakan lawan bicaramu. Sayangnya, karena terbiasa jadi pihak yang mengalah "
              "demi ketenangan bersama, kamu bisa jatuh ke pola di mana orang lain terbiasa "
              "mengandalkanmu tanpa pernah balik bertanya bagaimana kabarmu. Lama-lama, beban emosional "
              "yang kamu tampung sendirian ini bisa menumpuk tanpa kamu sadari, sampai suatu saat "
              "meledak dalam bentuk kelelahan mental atau rasa kesepian, meski kamu dikelilingi banyak "
              "orang yang menyayangimu.",
        "quote": "Menjaga perasaan orang lain itu baik, asal tidak sampai melupakan perasaanmu "
                 "sendiri.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Sesekali, latih diri untuk mengatakan apa yang sebenarnya kamu butuhkan, bukan hanya "
              "apa yang membuat orang lain nyaman. Orang-orang terdekatmu justru akan lebih menghargai "
              "kejujuran itu. Cobalah mulai dari hal kecil, misalnya memberi tahu temanmu kalau kamu "
              "sedang lelah dan butuh waktu sendiri, alih-alih tetap menemani mereka sampai kamu "
              "benar-benar kehabisan energi. Kamu juga bisa membuat kebiasaan sederhana: setiap kali "
              "selesai menenangkan orang lain, tanyakan pada dirimu sendiri satu hal yang kamu "
              "butuhkan saat itu juga, lalu penuhi, sekecil apa pun itu.",
    },
    "Pahing": {
        "tagline": "☾ Pasaran Pahing",
        "chip": "WETON",
        "title": "{hari} Pahing — Neptu {neptu}, Sosok yang Bersemangat",
        "p1_label": "Siapa Kamu",
        "p1": "Menurut primbon Jawa, kamu lahir dengan pasaran Pahing, yang jatuh pada hari {hari} "
              "dengan neptu total {neptu}. Pasaran Pahing identik dengan semangat yang menyala dan "
              "keinginan kuat untuk selalu tampil terbaik. Kamu punya energi yang membuatmu tidak "
              "puas hanya berdiam di tempat, dan selalu mendorong diri sendiri untuk berkembang. "
              "Energi ini biasanya sudah terlihat sejak kamu masih muda, misalnya lewat kebiasaan "
              "ingin selalu jadi yang terdepan di sekolah, organisasi, atau lingkungan pertemanan. "
              "Dalam pekerjaan, kamu jarang betah di posisi yang terasa monoton dan datar-datar saja; "
              "kamu selalu mencari tantangan baru yang bisa membuktikan kemampuanmu. Di mata orang "
              "lain, kamu terlihat sebagai sosok yang bersemangat menular, tipe orang yang begitu "
              "masuk ruangan langsung mengubah suasana jadi lebih hidup dan penuh energi.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Semangat dan ambisimu membuat orang lain melihatmu sebagai sosok yang pantang menyerah "
              "dalam mengejar sesuatu. Kamu juga cenderung berani mengambil risiko demi hasil yang "
              "lebih besar. Namun semangat yang menggebu ini kadang membuatmu kurang sabar terhadap "
              "orang lain yang bergerak lebih lambat, atau terhadap proses yang belum menunjukkan "
              "hasil secepat yang kamu harapkan. Kekuatan ambisimu juga bisa membuatmu terlalu keras "
              "menilai dirimu sendiri ketika sesuatu tidak berjalan sesuai rencana, seolah setiap "
              "hambatan kecil adalah tanda kegagalan besar. Di lingkungan tim, semangat besarmu kadang "
              "membuat rekan kerja merasa terburu-buru atau tertekan mengikuti kecepatanmu, padahal "
              "mereka mungkin punya cara kerja yang berbeda namun sama efektifnya.",
        "quote": "Semangat besar akan lebih membawa hasil kalau disertai kesabaran menunggu waktu "
                 "yang tepat.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba beri ruang pada orang lain untuk bergerak dengan kecepatan mereka "
              "sendiri, tanpa terburu-buru mendorong mereka menyamai temponu. Ketika bekerja sama "
              "dalam tim, cobalah bertanya dulu kepada rekanmu tentang kecepatan yang nyaman buat "
              "mereka, sebelum menetapkan target yang sebenarnya cuma nyaman buatmu sendiri. Latih "
              "juga kesabaran dengan memberi jeda satu atau dua hari sebelum menilai sebuah rencana "
              "sebagai gagal, karena hasil besar kadang memang butuh waktu lebih lama dari yang kamu "
              "harapkan.",
    },
    "Pon": {
        "tagline": "☾ Pasaran Pon",
        "chip": "WETON",
        "title": "{hari} Pon — Neptu {neptu}, Penengah yang Bijaksana",
        "p1_label": "Siapa Kamu",
        "p1": "Menurut primbon Jawa, kamu lahir dengan pasaran Pon, yang jatuh pada hari {hari} "
              "dengan neptu total {neptu}. Pasaran Pon sering dikaitkan dengan sosok yang bijaksana "
              "dan pandai menjaga keseimbangan dalam hubungan dengan orang lain. Kamu cenderung "
              "berpikir matang sebelum bertindak, dan jarang membuat keputusan yang terburu-buru. "
              "Dalam pertemanan atau keluarga, kamu biasanya jadi sosok yang paling sering diminta "
              "pendapat ketika ada perselisihan, karena cara pandangmu terasa netral dan tidak "
              "memihak salah satu sisi secara membabi buta. Di tempat kerja, kemampuan ini membuatmu "
              "cocok mengisi peran yang butuh diplomasi, seperti menjembatani kepentingan antar "
              "divisi atau menjaga hubungan baik antara atasan dan bawahan. Kamu juga cenderung lebih "
              "tenang menghadapi tekanan dibanding kebanyakan orang di sekitarmu.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kebijaksanaan dan kemampuanmu menjaga keharmonisan membuat orang lain sering "
              "menjadikanmu penengah saat ada perbedaan pendapat. Kamu juga dipercaya karena "
              "pertimbanganmu yang matang. Namun kehati-hatian ini kadang membuatmu terlalu lama "
              "menimbang-nimbang, sampai kesempatan yang seharusnya bisa kamu ambil justru "
              "terlewatkan. Kebiasaan mempertimbangkan semua sisi ini juga bisa membuatmu tampak "
              "kurang tegas di mata orang lain, terutama saat situasi menuntut keputusan cepat tanpa "
              "banyak basa-basi. Ada kalanya, keinginan untuk selalu adil bagi semua pihak justru "
              "membuatmu sendiri berada di posisi yang serba salah, karena tidak ada keputusan yang "
              "bisa memuaskan semua orang sekaligus.",
        "quote": "Pertimbangan yang matang itu penting, tapi ada kalanya keberanian mengambil "
                 "keputusan lebih berarti dari kesempurnaan pertimbangan itu sendiri.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Ketika dihadapkan pada satu keputusan kecil, coba beri batas waktu untuk "
              "menimbang, lalu putuskan sebelum batas waktu itu habis, alih-alih terus menunda. "
              "Latihan ini bisa dimulai dari hal-hal sepele, seperti memilih menu makan atau tempat "
              "nongkrong, sebelum kamu terapkan pada keputusan yang lebih besar. Ingatkan juga dirimu "
              "bahwa keputusan yang \"cukup baik\" dan diambil tepat waktu, seringkali lebih "
              "berharga daripada keputusan \"sempurna\" yang datang terlambat.",
    },
    "Wage": {
        "tagline": "☾ Pasaran Wage",
        "chip": "WETON",
        "title": "{hari} Wage — Neptu {neptu}, Pribadi yang Mandiri",
        "p1_label": "Siapa Kamu",
        "p1": "Menurut primbon Jawa, kamu lahir dengan pasaran Wage, yang jatuh pada hari {hari} "
              "dengan neptu total {neptu}. Pasaran Wage sering dikaitkan dengan sosok yang mandiri dan "
              "punya pendirian kuat. Kamu tidak mudah terpengaruh pendapat orang lain, dan lebih "
              "memilih menentukan sendiri arah hidupmu berdasarkan penilaianmu sendiri. Sejak muda, "
              "kamu mungkin sudah terbiasa menyelesaikan masalahmu sendiri tanpa banyak melibatkan "
              "orang lain, bukan karena tidak peduli, tapi karena kamu memang merasa lebih nyaman "
              "mengandalkan kemampuan dan penilaianmu sendiri. Dalam lingkungan kerja, sikap ini "
              "membuatmu cocok memegang tanggung jawab yang butuh kemandirian tinggi, karena kamu "
              "jarang perlu diawasi ketat untuk tetap menyelesaikan tugas dengan baik. Orang-orang di "
              "sekitarmu menghormati keteguhan pendirianmu, meski kadang mereka juga merasa sulit "
              "benar-benar tahu apa yang sedang kamu pikirkan atau rasakan.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kemandirian dan keteguhan pendirianmu membuatmu jarang bergantung pada orang lain "
              "untuk merasa yakin. Kamu juga cenderung tenang menghadapi tekanan dari luar. Namun "
              "sikap mandiri ini kadang membuatmu enggan meminta bantuan bahkan ketika kamu benar-"
              "benar membutuhkannya, sehingga terasa lebih berat menjalani sesuatu sendirian. Sikap "
              "ini bisa membuat orang-orang terdekatmu merasa jauh darimu, bukan karena kamu tidak "
              "menyayangi mereka, tapi karena kamu terbiasa memendam kesulitan sendiri sampai "
              "benar-benar tuntas, atau sampai tidak tertahankan lagi. Ketika akhirnya kamu meminta "
              "bantuan, biasanya itu tandanya kamu memang sudah benar-benar kehabisan cara sendiri, "
              "padahal bantuan yang lebih dini bisa membuat prosesnya jauh lebih ringan.",
        "quote": "Kemandirian itu kekuatan, tapi meminta bantuan pada saat yang tepat juga bukan "
                 "tanda kelemahan.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba minta bantuan pada satu hal kecil yang sebenarnya bisa kamu tangani "
              "sendiri, dan rasakan bahwa membiarkan orang lain membantu juga bisa terasa "
              "menenangkan. Kamu bisa mulai dari hal yang risikonya rendah, misalnya meminta tolong "
              "teman mengantarkan sesuatu atau mendiskusikan rencana kecil sebelum kamu jalankan "
              "sendiri. Perhatikan juga bagaimana perasaanmu setelah menerima bantuan itu; kemungkinan "
              "besar kamu akan sadar bahwa membuka diri sedikit tidak mengurangi kemandirianmu sama "
              "sekali.",
    },
    "Kliwon": {
        "tagline": "☾ Pasaran Kliwon",
        "chip": "WETON",
        "title": "{hari} Kliwon — Neptu {neptu}, Sosok yang Penuh Kepekaan",
        "p1_label": "Siapa Kamu",
        "p1": "Menurut primbon Jawa, kamu lahir dengan pasaran Kliwon, yang jatuh pada hari {hari} "
              "dengan neptu total {neptu}. Pasaran Kliwon sering dikaitkan dengan kepekaan batin yang "
              "dalam dan kemampuan merasakan hal-hal yang tidak terucap oleh orang lain. Kamu punya "
              "intuisi yang tajam, dan sering kali firasatmu tentang sesuatu ternyata benar. Kepekaan "
              "ini membuatmu sering jadi orang pertama yang menyadari kalau ada yang tidak beres "
              "dengan seseorang, bahkan sebelum orang itu sendiri mengucapkannya. Dalam hubungan "
              "sosial, kamu punya sisi spiritual dan reflektif yang membuatmu tertarik memahami hal-hal "
              "yang lebih dalam dari sekadar permukaan, seperti makna di balik peristiwa atau pola "
              "yang berulang dalam hidup. Banyak orang merasa nyaman berbagi cerita denganmu, karena "
              "kamu punya cara memahami situasi tanpa perlu penjelasan panjang lebar.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kepekaan dan intuisimu membuatmu mudah memahami situasi maupun perasaan orang lain "
              "tanpa perlu penjelasan panjang. Kamu juga punya sisi spiritual yang membuatmu tenang "
              "menghadapi ketidakpastian. Namun kepekaan yang besar ini kadang membuatmu mudah "
              "menyerap energi negatif dari sekitarmu, sehingga suasana hatimu jadi mudah terpengaruh "
              "oleh keadaan orang lain. Kalau tidak dijaga, kepekaan ini bisa membuatmu kelelahan "
              "secara emosional tanpa penyebab yang jelas, terutama setelah berada lama di lingkungan "
              "yang penuh tekanan atau konflik. Kamu juga rentan menyerap kekhawatiran orang lain "
              "seolah itu kekhawatiranmu sendiri, sampai sulit membedakan mana perasaan yang benar-"
              "benar milikmu.",
        "quote": "Kepekaan itu anugerah, tapi kamu juga berhak menjaga jarak dari energi yang tidak "
                 "membuatmu nyaman.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Ketika merasa energimu terkuras oleh suasana atau orang lain, coba luangkan "
              "waktu sendiri sejenak untuk memulihkan diri sebelum melanjutkan aktivitas. Buat "
              "kebiasaan kecil untuk mengecek kondisi emosimu di penghujung hari, dan tanyakan pada "
              "diri sendiri mana perasaan yang benar-benar milikmu, dan mana yang mungkin kamu serap "
              "dari orang lain. Menetapkan batasan yang sehat, misalnya membatasi waktu bersama orang "
              "yang energinya terasa berat, juga akan membantu kepekaanmu tetap jadi kekuatan, bukan "
              "beban.",
    },
}
