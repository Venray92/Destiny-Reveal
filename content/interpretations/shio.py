"""
Konten Shio (12 kategori).

Key dict ini HARUS sama persis dengan nilai "shio" dari engine/shio.py
(hitung_shio()["shio"]): Tikus, Kerbau, Macan, Kelinci, Naga, Ular, Kuda,
Kambing, Monyet, Ayam, Anjing, Babi.

Struktur tiap entri sama persis dengan DUMMY_RESULTS di views/revealpage.py.
"""

SHIO_CONTENT = {
    "Tikus": {
        "tagline": "🐭 Shio Tikus",
        "chip": "SHIO",
        "title": "Tikus — Si Cerdik yang Serba Bisa",
        "p1_label": "Siapa Kamu",
        "p1": "Dalam kepercayaan Tionghoa, shio Tikus dikenal sebagai simbol kecerdikan dan "
              "kelincahan berpikir. Kamu punya kemampuan membaca situasi dengan cepat dan menemukan "
              "jalan keluar di saat orang lain masih kebingungan. Naluri bertahan hidupmu kuat, dan "
              "kamu jarang benar-benar kehabisan akal meski berada dalam keadaan sulit.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kecerdikan dan kepekaanmu terhadap peluang membuat orang lain sering meminta "
              "pendapatmu sebelum mengambil keputusan penting. Kamu juga cepat beradaptasi dengan "
              "keadaan baru. Namun kelincahan berpikir ini terkadang membuatmu terlalu berhati-hati "
              "atau curiga berlebihan, sampai sulit benar-benar percaya penuh pada orang lain.",
        "quote": "Kecerdikan akan membawamu jauh, tapi kepercayaan yang tulus akan membawamu lebih "
                 "jauh lagi.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba beri satu orang yang selama ini kamu ragukan kesempatan untuk membuktikan "
              "dirinya minggu ini, tanpa langsung menilai dari kecurigaanmu.",
    },
    "Kerbau": {
        "tagline": "🐂 Shio Kerbau",
        "chip": "SHIO",
        "title": "Kerbau — Sosok Tekun yang Bisa Diandalkan",
        "p1_label": "Siapa Kamu",
        "p1": "Shio Kerbau melambangkan ketekunan, kejujuran, dan kerja keras yang konsisten. Kamu "
              "bukan tipe yang suka mencari jalan pintas; kamu lebih memilih menyelesaikan sesuatu "
              "langkah demi langkah sampai benar-benar tuntas. Orang-orang di sekitarmu tahu bahwa "
              "kata-katamu bisa dipegang, karena kamu jarang mengingkari janji.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Keteguhan dan kejujuranmu membuat orang lain merasa aman bekerja sama denganmu dalam "
              "jangka panjang. Kamu juga tidak mudah goyah oleh tekanan atau opini orang lain. "
              "Sayangnya, keteguhan itu kadang berubah menjadi keras kepala, membuatmu sulit menerima "
              "cara pandang baru meski cara pandang itu sebenarnya lebih baik.",
        "quote": "Keteguhan itu berharga, tapi kebesaran hati untuk berubah pikiran juga tanda "
                 "kekuatan.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Minggu ini, coba dengarkan satu pendapat yang berbeda dari caramu biasa melakukan "
              "sesuatu, dan pertimbangkan dengan pikiran terbuka sebelum menolaknya.",
    },
    "Macan": {
        "tagline": "🐯 Shio Macan",
        "chip": "SHIO",
        "title": "Macan — Pemberani yang Penuh Semangat",
        "p1_label": "Siapa Kamu",
        "p1": "Shio Macan dikenal sebagai simbol keberanian dan semangat juang yang besar. Kamu punya "
              "energi yang membuatmu tidak takut menghadapi tantangan, bahkan cenderung mencari "
              "tantangan itu sendiri. Kehadiranmu terasa penuh percaya diri, dan orang lain sering "
              "melihatmu sebagai sosok yang berani bertindak lebih dulu.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Keberanian dan semangatmu membuat orang lain terdorong untuk ikut berani mengambil "
              "risiko yang sehat. Kamu juga punya kharisma alami yang membuat orang memperhatikanmu. "
              "Namun semangat yang menggebu itu kadang membuatmu bertindak terlalu impulsif, tanpa "
              "sempat memikirkan konsekuensi jangka panjangnya.",
        "quote": "Keberanian yang matang tahu kapan harus menyerang dan kapan harus menunggu waktu "
                 "yang tepat.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Sebelum mengambil keputusan besar minggu ini, coba beri jeda satu hari untuk "
              "memikirkannya ulang, alih-alih langsung bertindak seperti biasanya.",
    },
    "Kelinci": {
        "tagline": "🐰 Shio Kelinci",
        "chip": "SHIO",
        "title": "Kelinci — Sosok Lembut yang Bijaksana",
        "p1_label": "Siapa Kamu",
        "p1": "Shio Kelinci melambangkan kelembutan, kehati-hatian, dan kebijaksanaan dalam bersikap. "
              "Kamu cenderung menghindari konflik dan lebih memilih menyelesaikan masalah dengan cara "
              "yang halus. Ketenanganmu membuat orang-orang di sekitarmu merasa nyaman, karena kamu "
              "jarang membuat suasana menjadi tegang tanpa alasan yang jelas.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kehati-hatian dan kepekaanmu membuatmu jarang terjebak dalam keputusan gegabah. Kamu "
              "juga pandai menjaga hubungan baik dengan banyak orang. Namun kebiasaan menghindari "
              "konflik ini kadang membuatmu memendam ketidaknyamanan sendiri demi menjaga suasana "
              "tetap damai, sampai akhirnya kamu sendiri yang merasa terbebani.",
        "quote": "Menjaga kedamaian itu baik, tapi bukan berarti kamu harus selalu mengalah pada "
                 "dirimu sendiri.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Ketika ada sesuatu yang mengganggumu minggu ini, coba sampaikan dengan lembut kepada "
              "orang yang bersangkutan, alih-alih memilih diam demi menghindari konflik.",
    },
    "Naga": {
        "tagline": "🐉 Shio Naga",
        "chip": "SHIO",
        "title": "Naga — Sosok yang Sulit Diabaikan",
        "p1_label": "Siapa Kamu",
        "p1": "Dalam kepercayaan Tionghoa, shio Naga dianggap sebagai simbol keberuntungan dan "
              "kekuatan. Kamu punya aura yang membuat orang lain memperhatikanmu tanpa harus berusaha "
              "keras. Rasa percaya diri itu bukan sekadar tampilan luar, tapi tumbuh dari keyakinan "
              "bahwa kamu memang mampu mencapai hal-hal besar kalau diberi kesempatan.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Ambisimu jarang setengah-setengah, dan itu yang membuat orang lain mempercayakan "
              "tanggung jawab besar padamu. Sayangnya, standar tinggi yang kamu pasang untuk diri "
              "sendiri kadang ikut dibebankan ke orang lain tanpa sadar, sehingga mereka bisa merasa "
              "tertekan berada di dekatmu kalau kamu tidak sedikit melunakkan cara menyampaikannya.",
        "quote": "Kekuatan yang sesungguhnya terlihat justru saat kamu memilih untuk lebih lembut.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba luangkan waktu untuk memuji usaha orang lain sebelum menunjukkan apa yang masih "
              "kurang. Kebiasaan kecil ini akan membuat orang-orang di sekitarmu merasa dihargai, "
              "bukan cuma dinilai dari hasil akhirnya saja.",
    },
    "Ular": {
        "tagline": "🐍 Shio Ular",
        "chip": "SHIO",
        "title": "Ular — Pemikir Tajam yang Penuh Intuisi",
        "p1_label": "Siapa Kamu",
        "p1": "Shio Ular melambangkan kebijaksanaan, ketenangan, dan intuisi yang tajam. Kamu jarang "
              "bertindak tanpa perhitungan, dan lebih suka mengamati situasi dengan saksama sebelum "
              "mengambil langkah. Ketenangan luarmu sering membuat orang salah sangka bahwa kamu tidak "
              "peduli, padahal di dalam kamu sedang memikirkan segalanya dengan sangat detail.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Ketajaman berpikir dan intuisimu membuatmu jarang terkecoh oleh hal-hal yang terlihat "
              "di permukaan. Kamu juga bisa tetap tenang dalam situasi yang membuat orang lain panik. "
              "Namun kecenderungan untuk menyimpan pemikiran sendiri ini kadang membuat orang lain "
              "kesulitan menebak apa yang sebenarnya kamu rasakan atau inginkan.",
        "quote": "Ketenangan yang bijak akan lebih bermakna kalau sesekali dibagikan, bukan hanya "
                 "disimpan sendiri.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba sampaikan satu pemikiran atau analisismu secara terbuka kepada orang terdekat "
              "minggu ini, alih-alih hanya memendamnya dalam kepala.",
    },
    "Kuda": {
        "tagline": "🐴 Shio Kuda",
        "chip": "SHIO",
        "title": "Kuda — Jiwa Bebas yang Energik",
        "p1_label": "Siapa Kamu",
        "p1": "Shio Kuda dikenal sebagai simbol kebebasan, semangat, dan energi yang tidak pernah "
              "habis. Kamu suka bergerak, mencoba hal baru, dan tidak betah terlalu lama terjebak "
              "dalam rutinitas yang membosankan. Semangatmu yang tinggi sering menular ke orang-orang "
              "di sekitarmu, membuat suasana jadi lebih hidup.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Energi dan semangat petualanganmu membuat orang lain terinspirasi untuk keluar dari "
              "rutinitas mereka juga. Kamu juga mudah bergaul dengan berbagai kalangan. Namun "
              "kebebasan yang kamu junjung tinggi ini kadang membuatmu sulit berkomitmen pada satu "
              "hal dalam jangka panjang, karena selalu ada godaan untuk mencoba yang baru.",
        "quote": "Kebebasan sejati justru terasa lebih utuh ketika kamu berani berkomitmen pada apa "
                 "yang benar-benar penting.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Pilih satu komitmen yang sudah kamu buat, lalu jaga konsistensinya selama satu minggu "
              "penuh tanpa tergoda beralih ke hal baru yang lain.",
    },
    "Kambing": {
        "tagline": "🐐 Shio Kambing",
        "chip": "SHIO",
        "title": "Kambing — Jiwa Lembut yang Penuh Empati",
        "p1_label": "Siapa Kamu",
        "p1": "Shio Kambing melambangkan kelembutan hati, kreativitas, dan kepedulian yang tulus "
              "terhadap orang lain. Kamu punya sisi artistik dan suka menciptakan suasana yang nyaman "
              "di sekitarmu. Kepekaanmu terhadap perasaan orang lain membuatmu sering jadi tempat "
              "curhat yang dipercaya banyak teman.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kepedulian dan kreativitasmu membuat orang lain merasa nyaman dan dihargai saat "
              "bersamamu. Kamu juga punya kemampuan menciptakan hal-hal indah dari sudut pandang yang "
              "berbeda. Namun kelembutan hati ini kadang membuatmu terlalu bergantung pada validasi "
              "atau persetujuan orang lain sebelum merasa yakin dengan pilihanmu sendiri.",
        "quote": "Pendapat orang lain penting, tapi keyakinanmu pada dirimu sendiri jauh lebih "
                 "penting lagi.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba ambil satu keputusan kecil minggu ini berdasarkan penilaianmu sendiri, tanpa "
              "meminta persetujuan orang lain terlebih dulu.",
    },
    "Monyet": {
        "tagline": "🐒 Shio Monyet",
        "chip": "SHIO",
        "title": "Monyet — Si Cerdas yang Penuh Ide",
        "p1_label": "Siapa Kamu",
        "p1": "Shio Monyet dikenal sebagai simbol kecerdasan, kelincahan, dan kemampuan memecahkan "
              "masalah dengan cara-cara kreatif. Kamu cepat menangkap pola dan sering menemukan solusi "
              "yang tidak terpikirkan orang lain. Rasa humor dan keluwesanmu membuat orang-orang di "
              "sekitarmu merasa senang berada di dekatmu.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kecerdasan dan kreativitasmu membuat orang lain sering meminta pendapatmu ketika "
              "menghadapi masalah yang rumit. Kamu juga pandai mencairkan suasana yang tegang. Namun "
              "kelincahan berpikir ini kadang membuatmu mudah bosan dan terlalu banyak mengambil "
              "peran sekaligus, sampai tidak ada satu pun yang benar-benar kamu dalami sepenuhnya.",
        "quote": "Kecerdasan akan lebih terasa hasilnya kalau difokuskan pada satu arah dalam satu "
                 "waktu.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Minggu ini, coba kurangi jumlah hal yang kamu kerjakan sekaligus, dan fokuskan energi "
              "pada satu atau dua hal yang paling penting bagimu.",
    },
    "Ayam": {
        "tagline": "🐓 Shio Ayam",
        "chip": "SHIO",
        "title": "Ayam — Sosok Rapi yang Percaya Diri",
        "p1_label": "Siapa Kamu",
        "p1": "Shio Ayam melambangkan ketelitian, kerapian, dan kepercayaan diri yang kuat. Kamu suka "
              "semua hal tertata dengan baik, mulai dari pekerjaan sampai penampilan sehari-hari. "
              "Kejujuranmu yang blak-blakan membuat orang lain tahu persis pendapatmu tentang sesuatu, "
              "tanpa perlu menebak-nebak lebih dulu.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Ketelitian dan kepercayaan dirimu membuat orang lain percaya pada kualitas kerjamu. "
              "Kamu juga berani bicara jujur saat orang lain memilih diam. Sayangnya, kejujuran yang "
              "terlalu terus terang ini kadang terdengar seperti kritik yang menyakitkan, meski "
              "maksudmu sebenarnya baik.",
        "quote": "Kejujuran akan lebih mudah diterima kalau disampaikan dengan sedikit lebih lembut.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Sebelum menyampaikan kritik minggu ini, coba pikirkan dulu cara penyampaian yang lebih "
              "lembut, tanpa mengubah kejujuran dari isi pesannya.",
    },
    "Anjing": {
        "tagline": "🐕 Shio Anjing",
        "chip": "SHIO",
        "title": "Anjing — Sosok Setia yang Bisa Dipercaya",
        "p1_label": "Siapa Kamu",
        "p1": "Shio Anjing dikenal sebagai simbol kesetiaan, kejujuran, dan rasa keadilan yang kuat. "
              "Kamu jarang berkhianat pada orang yang sudah kamu percaya, dan selalu berusaha "
              "melindungi orang-orang terdekatmu. Kamu juga peka terhadap ketidakadilan, dan tidak "
              "segan membela orang yang menurutmu diperlakukan tidak adil.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kesetiaan dan rasa keadilanmu membuat orang lain merasa aman menjadikanmu sahabat atau "
              "rekan kerja. Kamu juga bisa diandalkan dalam situasi sulit sekalipun. Namun sisi "
              "waspada dalam dirimu kadang membuatmu terlalu khawatir atau curiga tentang hal-hal yang "
              "belum tentu terjadi, sampai sulit benar-benar merasa tenang.",
        "quote": "Kewaspadaan itu penting, tapi jangan sampai membuatmu kehilangan ketenangan di "
                 "masa sekarang.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Ketika muncul kekhawatiran tentang sesuatu yang belum terjadi minggu ini, coba tanyakan "
              "pada diri sendiri seberapa besar kemungkinannya benar-benar terjadi, sebelum "
              "membiarkan kekhawatiran itu menguasai pikiranmu.",
    },
    "Babi": {
        "tagline": "🐷 Shio Babi",
        "chip": "SHIO",
        "title": "Babi — Sosok Tulus yang Penuh Kebaikan Hati",
        "p1_label": "Siapa Kamu",
        "p1": "Shio Babi melambangkan ketulusan, kemurahan hati, dan kejujuran yang sederhana. Kamu "
              "jarang berpikir buruk tentang orang lain, dan cenderung memberi kesempatan kedua meski "
              "sudah pernah dikecewakan. Kehadiranmu membuat orang-orang di sekitarmu merasa diterima "
              "apa adanya, tanpa banyak dihakimi.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Ketulusan dan kemurahan hatimu membuat orang lain merasa nyaman dan dihargai saat "
              "bersamamu. Kamu juga jarang menyimpan dendam terlalu lama. Namun sikap yang terlalu "
              "percaya ini kadang membuatmu mudah dimanfaatkan oleh orang-orang yang sebenarnya tidak "
              "berniat baik.",
        "quote": "Kebaikan hati akan lebih aman kalau disertai sedikit kehati-hatian dalam memilih "
                 "kepada siapa kamu memberikannya.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Minggu ini, coba perhatikan lebih saksama pola perlakuan orang-orang di sekitarmu, dan "
              "beri batasan yang wajar kepada mereka yang selama ini hanya memanfaatkan kebaikanmu.",
    },
}
