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
        "domains": {
            "karir": "Ketenanganmu adalah aset berharga di dunia kerja, kamu cocok di peran yang butuh "
                     "kesabaran ekstra, seperti customer service, mediasi, HR, atau posisi apa pun yang "
                     "mengharuskan menjaga hubungan baik dengan banyak pihak sekaligus. Rekan kerja "
                     "merasa aman berdiskusi denganmu karena kamu jarang bereaksi berlebihan meski "
                     "situasinya sedang tegang. Namun kebiasaan mendahulukan ketenangan tim di atas "
                     "kepentinganmu sendiri bisa membuatmu jadi tempat sampah keluhan tanpa "
                     "penghargaan yang seimbang, dan kamu jarang mengajukan diri untuk hal-hal yang "
                     "sebenarnya jadi hakmu, seperti promosi atau pengakuan atas jasamu meredam "
                     "banyak konflik di belakang layar. *PR: Sampaikan satu pencapaianmu yang selama "
                     "ini kamu diamkan ke atasan minggu ini.*",
            "asmara": "Dalam hubungan, ketenanganmu membuat pasangan merasa punya tempat berlabuh yang "
                      "aman, kamu jarang membuat drama dan selalu berusaha memahami sudut pandangnya "
                      "lebih dulu sebelum bereaksi. Ini membuat hubunganmu terasa stabil dan nyaman "
                      "dalam jangka panjang. Namun kebiasaan mengalah demi menjaga kedamaian bisa "
                      "membuat kebutuhan emosionalmu sendiri jarang tersampaikan, sampai pasangan tidak "
                      "benar-benar tahu apa yang membuatmu bahagia atau kecewa. Lama-lama, ini bisa "
                      "membuatmu merasa sendirian meski berada dalam hubungan, karena kamu selalu jadi "
                      "yang memberi ruang, jarang menerima. *PR: Ceritakan satu hal yang kamu butuhkan "
                      "dari pasanganmu minggu ini, tanpa dibungkus permintaan maaf.*",
            "keuangan": "Soal keuangan, sifat tenangmu membuatmu jarang mengambil keputusan finansial "
                        "yang gegabah, kamu lebih suka mempertimbangkan matang-matang sebelum "
                        "mengeluarkan uang untuk sesuatu yang besar. Kamu juga cenderung dermawan pada "
                        "keluarga atau teman yang sedang kesulitan. Namun kebiasaan mendahulukan "
                        "kebutuhan orang lain bisa membuat rencana keuanganmu sendiri sering "
                        "tertunda, kamu lebih siap membantu orang lain daripada menabung untuk "
                        "tujuanmu sendiri. Penting untukmu belajar bahwa menjaga kondisi finansialmu "
                        "sendiri tetap sehat bukan berarti kamu pelit atau tidak peduli pada orang "
                        "lain. *PR: Sisihkan dana untuk tujuan finansialmu sendiri sebelum membantu "
                        "orang lain bulan ini, bukan sesudahnya.*",
            "kesehatan": "Karena kamu terbiasa jadi tempat orang lain berkeluh kesah, tanpa sadar kamu "
                         "menyerap banyak beban emosional yang sebenarnya bukan milikmu. Ini bisa "
                         "menumpuk jadi kelelahan mental yang tidak terlihat dari luar, karena kamu "
                         "tetap tampak tenang meski di dalam sedang penuh. Kamu perlu punya ruang "
                         "khusus untuk melepaskan beban itu, bukan sekadar menampungnya terus-menerus. "
                         "Kesehatan fisikmu juga bisa terdampak kalau kelelahan emosional ini "
                         "dibiarkan, misalnya lewat gangguan tidur atau energi yang cepat habis "
                         "meski aktivitas fisikmu tidak berat. *PR: Cari satu orang atau cara untuk "
                         "'curhat balik' minggu ini, bukan hanya jadi pendengar seperti biasanya.*",
        },
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
        "domains": {
            "karir": "Ambisimu yang besar membuatmu cocok mengejar posisi kepemimpinan atau peran yang "
                     "menuntut hasil nyata dan terukur, seperti target sales, manajemen proyek, atau "
                     "wirausaha. Kamu tidak takut kerja keras demi mencapai apa yang kamu inginkan, "
                     "dan semangat ini sering membuatmu naik jabatan lebih cepat dari rekan seangkatan. "
                     "Namun ketidaksabaranmu bisa membuatmu terburu-buru mengambil keputusan penting "
                     "sebelum semua data terkumpul, dan kekecewaan terhadap hasil yang belum "
                     "maksimal bisa membuatmu terlalu keras menilai kinerja diri sendiri maupun tim. "
                     "*PR: Beri tim atau proyekmu jeda satu minggu tambahan sebelum menilai hasilnya "
                     "sebagai kurang memuaskan.*",
            "asmara": "Dalam hubungan, energimu yang menggebu membuat hubungan terasa hidup dan penuh "
                      "semangat, kamu tidak suka hubungan yang terasa datar dan selalu ingin "
                      "mengajak pasangan berkembang bersama. Namun ketidaksabaranmu bisa membuatmu "
                      "cepat kecewa kalau pasangan tidak bergerak secepat yang kamu harapkan, entah "
                      "dalam mengambil keputusan bersama atau menyelesaikan masalah. Kamu perlu belajar "
                      "bahwa ritme setiap orang berbeda, dan memaksakan kecepatanmu justru bisa membuat "
                      "pasangan merasa tertekan dan kurang dihargai prosesnya sendiri. *PR: Tanyakan "
                      "ke pasanganmu ritme yang nyaman buatnya dalam mengambil keputusan bersama, dan "
                      "hormati itu minggu ini.*",
            "keuangan": "Soal keuangan, semangat dan ambisimu membuatmu berani mengejar penghasilan "
                        "lebih besar, entah lewat kerja keras ekstra, usaha sampingan, atau investasi "
                        "yang agresif. Kamu jarang puas dengan hasil yang biasa-biasa saja. Namun "
                        "ketidaksabaran untuk cepat melihat hasil bisa membuatmu tergoda mengambil "
                        "keputusan finansial berisiko tinggi tanpa riset yang cukup, hanya karena "
                        "ingin cepat kaya atau cepat melihat pertumbuhan. Kesabaran dalam membangun "
                        "kekayaan justru sering jadi kunci yang lebih penting dari kecepatan semata. "
                        "*PR: Sebelum mengambil peluang investasi baru, riset dulu selama satu minggu "
                        "penuh tanpa terburu-buru memutuskan.*",
            "kesehatan": "Energimu yang tinggi membuatmu jarang lelah secara fisik, tapi ambisi yang "
                         "terus mendorongmu bergerak bisa membuatmu lupa memberi tubuh waktu istirahat "
                         "yang cukup. Kamu tipe yang sulit berhenti sebelum target tercapai, bahkan "
                         "kalau itu berarti mengorbankan jam tidur atau pola makan yang teratur. "
                         "Tekanan yang kamu ciptakan sendiri demi mengejar hasil terbaik juga bisa "
                         "memicu stres yang berdampak ke kesehatan jangka panjang kalau tidak "
                         "diimbangi jeda yang cukup. *PR: Tetapkan satu waktu istirahat wajib setiap "
                         "hari minggu ini, yang tidak bisa digeser apa pun alasannya.*",
        },
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
        "domains": {
            "karir": "Kebijaksanaanmu membuatmu cocok di peran yang butuh diplomasi dan pandangan "
                     "netral, seperti manajemen tim lintas divisi, konsultasi, atau posisi yang "
                     "menuntut kamu menjembatani kepentingan berbagai pihak. Rekan kerja "
                     "mempercayaimu untuk mengambil keputusan yang adil bagi semua orang. Namun "
                     "kebiasaan menimbang semua sisi terlalu lama bisa membuatmu terlihat lambat "
                     "mengambil keputusan di mata atasan, terutama di situasi yang butuh respons "
                     "cepat. Kamu juga cenderung menghindari posisi yang memaksamu memihak salah satu "
                     "sisi secara tegas, meski kadang situasi memang menuntut ketegasan seperti itu. "
                     "*PR: Ambil satu keputusan kerja minggu ini dalam waktu maksimal satu hari, tanpa "
                     "menimbang berlarut-larut.*",
            "asmara": "Dalam hubungan, kebijaksanaanmu membuat pasangan merasa didengar dan dipahami "
                      "dari berbagai sudut pandang, kamu jarang menghakimi buru-buru dan selalu "
                      "berusaha adil dalam menilai situasi. Namun kehati-hatian ini bisa membuatmu "
                      "sulit mengambil sikap tegas soal apa yang benar-benar kamu inginkan dari "
                      "hubungan, kamu lebih sering menyesuaikan diri demi keharmonisan daripada "
                      "menyuarakan kebutuhanmu sendiri. Pasangan mungkin merasa kesulitan menebak "
                      "keinginanmu yang sesungguhnya, karena kamu terlalu sering mempertimbangkan "
                      "perasaannya di atas perasaanmu sendiri. *PR: Sampaikan satu keinginanmu secara "
                      "tegas ke pasangan minggu ini, tanpa embel-embel 'terserah kamu aja'.*",
            "keuangan": "Soal keuangan, sikap hati-hatimu membuatmu jarang terjebak keputusan "
                        "finansial impulsif, kamu selalu mempertimbangkan berbagai opsi sebelum "
                        "benar-benar memutuskan. Kestabilan ini membuat kondisi finansialmu cenderung "
                        "aman dalam jangka panjang. Namun kebiasaan menimbang terlalu lama bisa "
                        "membuatmu melewatkan peluang investasi yang sebenarnya sudah cukup jelas "
                        "menguntungkan, karena kamu masih terus mempertimbangkan kemungkinan lain "
                        "yang belum tentu lebih baik. *PR: Tetapkan tenggat waktu maksimal satu minggu "
                        "untuk memutuskan satu peluang finansial yang sedang kamu pertimbangkan.*",
            "kesehatan": "Ketenangan dan sikap tidak terburu-buru membuatmu relatif jarang stres "
                         "berlebihan menghadapi tekanan sehari-hari. Namun kebiasaan terus menimbang "
                         "berbagai kemungkinan bisa membuat pikiranmu sulit benar-benar beristirahat, "
                         "kamu terus memikirkan berbagai skenario bahkan untuk hal-hal yang sebenarnya "
                         "sudah selesai atau tidak lagi relevan. Kamu perlu belajar melepaskan proses "
                         "berpikir itu di waktu-waktu tertentu, supaya pikiranmu benar-benar dapat "
                         "jeda. *PR: Coba tetapkan satu jam setiap malam khusus untuk berhenti "
                         "memikirkan keputusan apa pun, dan benar-benar rileks.*",
        },
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
        "domains": {
            "karir": "Kemandirianmu adalah aset besar di dunia kerja, kamu bisa dipercaya memegang "
                     "tanggung jawab tanpa perlu diawasi ketat, dan ini membuatmu cocok di peran "
                     "individual contributor tingkat tinggi, freelance, atau posisi yang butuh "
                     "inisiatif tanpa arahan detail. Atasan tahu kalau tugas diserahkan padamu, "
                     "hasilnya akan tetap baik meski tanpa pengawasan ketat. Namun keengananmu meminta "
                     "bantuan bisa membuatmu kesulitan sendiri saat beban kerja sebenarnya sudah "
                     "berlebihan, dan kamu jarang mendelegasikan meski itu akan membuat pekerjaan lebih "
                     "efisien. *PR: Delegasikan satu tugas ke rekan kerja minggu ini, meski kamu yakin "
                     "bisa mengerjakannya sendiri lebih cepat.*",
            "asmara": "Dalam hubungan, kemandirianmu membuat pasangan merasa tidak perlu terus-"
                      "menerus mengkhawatirkanmu, kamu bisa berdiri di atas kaki sendiri secara "
                      "emosional maupun praktis. Namun kebiasaan memendam kesulitan sendiri bisa "
                      "membuat pasangan merasa jauh darimu, mereka ingin dilibatkan dalam masalahmu "
                      "tapi kamu jarang membuka pintu itu sampai benar-benar terpaksa. Keintiman yang "
                      "sehat justru butuh keterbukaan yang lebih sering, bukan hanya saat keadaan "
                      "sudah darurat. *PR: Ceritakan satu kesulitan kecil yang sedang kamu hadapi ke "
                      "pasanganmu minggu ini, sebelum itu jadi terlalu berat untuk ditanggung "
                      "sendiri.*",
            "keuangan": "Soal keuangan, kemandirianmu membuatmu terbiasa mengatur uangmu sendiri "
                        "tanpa banyak bergantung pada bantuan orang lain, dan kamu cenderung punya "
                        "rencana yang jelas untuk mencapai tujuan finansialmu sendiri. Namun sikap "
                        "ini bisa membuatmu enggan mencari nasihat finansial dari orang lain, meski "
                        "masukan dari sudut pandang berbeda kadang bisa membuka peluang yang belum "
                        "kamu pertimbangkan. Kamu juga cenderung menanggung semua beban finansial "
                        "keluarga sendirian tanpa membagi tanggung jawab, meski itu sebenarnya di luar "
                        "kapasitasmu. *PR: Diskusikan satu rencana finansial dengan orang yang kamu "
                        "percaya minggu ini, bukan cuma memutuskan sendirian.*",
            "kesehatan": "Kebiasaan menyelesaikan masalah sendirian membuatmu jarang meminta bantuan "
                         "profesional, termasuk soal kesehatan, sampai kondisinya benar-benar tidak "
                         "tertahankan. Kamu tipe yang akan terus mencoba mengatasi sendiri sebelum "
                         "akhirnya menyerah dan mencari bantuan, padahal deteksi dan penanganan dini "
                         "biasanya jauh lebih ringan. Beban yang kamu pendam sendirian, baik fisik "
                         "maupun mental, juga bisa menumpuk tanpa disadari sampai berdampak pada "
                         "energi dan staminamu sehari-hari. *PR: Kalau ada keluhan kesehatan yang "
                         "sudah kamu tunda beberapa waktu, periksakan diri minggu ini, jangan ditangani "
                         "sendiri lagi.*",
        },
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
        "domains": {
            "karir": "Intuisimu yang tajam membuatmu unggul di pekerjaan yang butuh kepekaan membaca "
                     "situasi atau orang, seperti konseling, HR, riset pasar, atau peran apa pun yang "
                     "mengharuskan kamu memahami kebutuhan orang lain lebih dari yang mereka ucapkan. "
                     "Rekan kerja sering merasa kamu 'mengerti' masalah mereka lebih cepat dari yang "
                     "mereka jelaskan sendiri. Namun kepekaan ini bisa membuatmu mudah menyerap "
                     "tekanan dari lingkungan kerja yang penuh konflik atau kompetisi, dan itu bisa "
                     "menguras energimu lebih cepat dibanding rekan lain yang tidak sesensitif dirimu. "
                     "*PR: Setelah rapat atau interaksi kerja yang berat minggu ini, beri diri lima "
                     "menit untuk 'melepaskan' energi itu sebelum lanjut ke tugas berikutnya.*",
            "asmara": "Dalam hubungan, kepekaanmu membuatmu bisa merasakan perubahan suasana hati "
                      "pasangan bahkan sebelum diucapkan, dan ini membuat pasangan merasa benar-benar "
                      "dipahami. Kamu juga punya kedalaman emosional yang membuat hubunganmu terasa "
                      "bermakna, bukan sekadar permukaan. Namun kepekaan yang besar ini bisa membuatmu "
                      "terlalu mudah menyerap kecemasan atau masalah pasangan sebagai bebanmu sendiri, "
                      "sampai sulit membedakan mana emosimu dan mana emosinya. Kamu perlu menjaga "
                      "batasan emosional yang sehat supaya empati tidak berubah jadi kelelahan. "
                      "*PR: Ketika pasanganmu sedang emosi minggu ini, coba dampingi tanpa "
                      "sepenuhnya ikut larut dalam perasaan itu.*",
            "keuangan": "Soal keuangan, intuisimu kadang membantumu merasakan peluang atau risiko "
                        "yang belum tentu terlihat jelas secara data, semacam firasat yang sering "
                        "terbukti benar. Namun kepekaan emosionalmu bisa membuat keputusan "
                        "finansialmu mudah terpengaruh suasana hati, kamu bisa berbelanja lebih "
                        "banyak saat sedang sedih untuk menghibur diri, atau menahan diri berlebihan "
                        "saat sedang cemas tanpa alasan finansial yang jelas. Penting untukmu punya "
                        "sistem yang tidak bergantung pada mood harian dalam mengatur uang. *PR: Buat "
                        "anggaran tetap bulanan yang tidak berubah mengikuti suasana hatimu, dan "
                        "patuhi itu minggu ini.*",
            "kesehatan": "Kepekaanmu terhadap energi sekitar membuatmu rentan menyerap stres orang "
                         "lain sebagai stresmu sendiri, ini bisa berdampak nyata ke kesehatan fisik "
                         "seperti gangguan tidur, sakit kepala, atau kelelahan yang datang tanpa "
                         "sebab jelas. Kamu butuh ritual pemulihan yang konsisten untuk 'membersihkan' "
                         "energi yang kamu serap sepanjang hari, entah lewat meditasi, journaling, "
                         "atau sekadar waktu sendiri dalam diam. Mengabaikan kebutuhan ini dalam "
                         "jangka panjang bisa membuat kepekaanmu yang sebenarnya adalah kekuatan justru "
                         "jadi sumber kelelahan kronis. *PR: Lakukan satu ritual 'membersihkan energi' "
                         "sederhana setiap malam minggu ini, meski hanya lima menit.*",
        },
    },
}
