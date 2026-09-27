"""
Konten Numerologi — Angka Hidup / Life Path (12 kategori).

Key dict ini adalah INTEGER, HARUS sama persis dengan nilai balikan
engine/numerologi.py (hitung_life_path()): 1, 2, 3, 4, 5, 6, 7, 8, 9,
11, 22, 33 (angka 11/22/33 adalah Master Number, tidak direduksi lagi).

Struktur tiap entri sama persis dengan DUMMY_RESULTS di views/revealpage.py.

REVISI (26 Sep 2026 malam): isi p1/p2/p3 diperpanjang 2-3x lipat dari versi
sebelumnya (per instruksi Stev), supaya laporannya terasa lebih bernilai
dan aplikatif, bukan cuma label singkat.
"""

NUMEROLOGI_CONTENT = {
    1: {
        "tagline": "✦ Angka Hidup 1",
        "chip": "NUMEROLOGI",
        "title": "Angka Hidup 1 — Sang Pemula yang Mandiri",
        "p1_label": "Siapa Kamu",
        "p1": "Angka hidup 1 dihitung dari penjumlahan digit tanggal lahirmu, dan dalam numerologi "
              "angka ini melambangkan jiwa kepemimpinan serta kemandirian yang kuat. Kamu cenderung "
              "suka memulai sesuatu dari nol dan tidak terlalu nyaman hanya mengikuti arahan orang "
              "lain. Ada dorongan alami dalam dirimu untuk menjadi yang terdepan. Dorongan ini biasanya "
              "sudah terlihat sejak kecil, misalnya lewat kebiasaan ingin menyelesaikan sesuatu dengan "
              "caramu sendiri, bukan cara yang diajarkan orang lain begitu saja. Dalam pekerjaan, kamu "
              "cocok mengisi peran yang membutuhkan inisiatif tinggi, seperti merintis proyek baru atau "
              "memimpin tim yang sedang membangun sesuatu dari awal. Kamu jarang puas hanya jadi bagian "
              "kecil dari sistem yang sudah ada; kamu ingin punya andil nyata dalam menentukan arah "
              "sesuatu berjalan.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Inisiatif dan kepercayaan dirimu membuat orang lain sering melihatmu sebagai penggerak "
              "utama dalam sebuah kelompok. Kamu juga berani mengambil keputusan tanpa harus menunggu "
              "persetujuan banyak pihak. Namun dorongan untuk selalu memimpin ini kadang membuatmu "
              "kurang sabar bekerja sama, atau sulit menerima ide dari orang lain. Kebutuhan untuk "
              "selalu berada di posisi terdepan ini bisa membuat rekan kerja atau anggota timmu merasa "
              "kurang dilibatkan dalam pengambilan keputusan, meski niatmu sebenarnya baik. Kamu juga "
              "bisa terlalu cepat mengambil alih sebuah proses, tanpa memberi kesempatan orang lain "
              "untuk berkembang dan belajar dari kesalahan mereka sendiri.",
        "quote": "Menjadi pemimpin yang baik juga berarti tahu kapan harus mengikuti arahan orang "
                 "lain.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba biarkan satu keputusan kecil diambil oleh orang lain di sekitarmu, "
              "dan lihat bagaimana rasanya melepaskan kendali sejenak. Latih juga dirimu untuk "
              "bertanya pendapat rekan kerja atau teman sebelum langsung menetapkan arah, meski kamu "
              "sudah punya gambaran jelas di kepala. Kebiasaan kecil ini akan membuat orang lain "
              "merasa lebih dihargai dan dilibatkan dalam proses yang kamu pimpin.",
    },
    2: {
        "tagline": "✦ Angka Hidup 2",
        "chip": "NUMEROLOGI",
        "title": "Angka Hidup 2 — Sosok Harmonis yang Peka",
        "p1_label": "Siapa Kamu",
        "p1": "Angka hidup 2 melambangkan kepekaan, kerja sama, dan kemampuan menjaga keharmonisan "
              "dalam hubungan dengan orang lain. Kamu cenderung memperhatikan perasaan orang di "
              "sekitarmu, dan lebih nyaman bekerja dalam tim dibanding sendirian. Kedamaian terasa "
              "penting bagimu, dan kamu berusaha menghindari konflik sebisa mungkin. Kepekaan ini "
              "membuatmu jadi sosok yang sering diminta bantuannya untuk menjembatani perbedaan "
              "pendapat, karena kamu tahu cara menyampaikan sesuatu tanpa membuat pihak lain merasa "
              "diserang. Dalam lingkungan kerja, kamu unggul di peran yang membutuhkan kerja sama tim "
              "yang solid, karena kamu selalu memikirkan bagaimana keputusan yang diambil akan "
              "memengaruhi orang lain, bukan hanya dirimu sendiri. Dalam hubungan personal, kamu "
              "adalah pasangan atau teman yang penuh perhatian, selalu berusaha memahami apa yang "
              "sedang dirasakan orang terdekatmu.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kepekaan dan kemampuanmu bekerja sama membuat orang lain merasa nyaman berada satu tim "
              "denganmu. Kamu juga jago menjembatani perbedaan pendapat. Namun kebiasaan mengutamakan "
              "keharmonisan ini kadang membuatmu terlalu sering mengalah, sampai kebutuhanmu sendiri "
              "jadi terabaikan. Pola mengalah demi menjaga kedamaian ini, kalau dibiarkan terus-"
              "menerus, bisa membuat orang lain terbiasa mengesampingkan pendapatmu karena tahu kamu "
              "jarang bersikeras. Kamu juga bisa kesulitan menyampaikan kekecewaan secara langsung, "
              "sehingga perasaan tidak nyaman itu justru menumpuk diam-diam sampai akhirnya meledak "
              "dalam bentuk yang tidak terduga.",
        "quote": "Kerja sama yang sehat juga memberi ruang bagi kebutuhanmu sendiri untuk didengar.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba sampaikan satu pendapat yang berbeda dari mayoritas, meski itu berarti "
              "sedikit mengganggu keharmonisan yang biasa kamu jaga. Latih diri dengan cara "
              "menyampaikan kebutuhanmu secara jelas namun tetap lembut, misalnya dengan kalimat "
              "\"aku sebenarnya lebih nyaman kalau...\", supaya kebutuhanmu tersampaikan tanpa harus "
              "memaksakan atau mengorbankan gaya komunikasimu yang halus.",
    },
    3: {
        "tagline": "✦ Angka Hidup 3",
        "chip": "NUMEROLOGI",
        "title": "Angka Hidup 3 — Jiwa Kreatif yang Ekspresif",
        "p1_label": "Siapa Kamu",
        "p1": "Angka hidup 3 melambangkan kreativitas, komunikasi, dan semangat untuk mengekspresikan "
              "diri. Kamu punya cara pandang yang unik terhadap dunia, dan senang membagikannya lewat "
              "kata-kata, karya, atau sekadar obrolan yang hidup. Kehadiranmu sering membawa warna "
              "baru di tengah suasana yang biasa-biasa saja. Bakat komunikasi ini membuatmu mudah "
              "menyampaikan ide-ide rumit dengan cara yang ringan dan menarik, sehingga orang lain "
              "senang mendengarkanmu berbicara, entah dalam presentasi formal maupun obrolan santai. "
              "Dalam pekerjaan, kreativitasmu membuatmu cocok di bidang yang membutuhkan ide segar dan "
              "cara penyampaian yang menarik, seperti konten, desain, atau bidang lain yang "
              "menghargai orisinalitas. Dalam pertemanan, kamu sering jadi sosok yang menghidupkan "
              "suasana, membuat kumpul-kumpul yang tadinya biasa saja terasa jauh lebih seru.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kreativitas dan kemampuan komunikasimu membuat orang lain senang menghabiskan waktu "
              "denganmu. Kamu juga pandai mencairkan suasana yang kaku. Namun energi ekspresif ini "
              "kadang membuatmu kesulitan fokus menyelesaikan satu hal, karena terlalu banyak ide baru "
              "yang ingin kamu coba sekaligus. Kebiasaan melompat dari satu ide ke ide lain ini bisa "
              "membuat karya atau proyekmu terasa banyak tapi tidak ada yang benar-benar matang. Kamu "
              "juga bisa terlalu bergantung pada validasi dari orang lain terhadap ekspresi dirimu, "
              "sampai merasa kurang percaya diri saat karyamu tidak mendapat respons yang kamu "
              "harapkan.",
        "quote": "Kreativitas akan lebih berbuah kalau kamu memberi satu ide waktu yang cukup untuk "
                 "benar-benar tumbuh.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Pilih satu ide kreatif yang sudah lama kamu simpan, lalu wujudkan sampai selesai "
              "sebelum berpindah memikirkan ide yang lain. Kamu bisa membuat target sederhana, "
              "misalnya menyelesaikan satu bagian kecil dari ide itu setiap minggu, supaya "
              "prosesnya terasa ringan tapi tetap membawamu maju menuju penyelesaian yang utuh.",
    },
    4: {
        "tagline": "✦ Angka Hidup 4",
        "chip": "NUMEROLOGI",
        "title": "Angka Hidup 4 — Sosok Teratur yang Bisa Diandalkan",
        "p1_label": "Siapa Kamu",
        "p1": "Angka hidup 4 melambangkan ketertiban, kedisiplinan, dan fondasi yang kuat dalam segala "
              "hal yang kamu bangun. Kamu suka bekerja dengan sistem yang jelas, dan lebih percaya "
              "pada proses yang teruji dibanding jalan pintas. Orang-orang di sekitarmu tahu bahwa "
              "kamu adalah sosok yang bisa diandalkan untuk urusan yang butuh ketelitian. Kamu "
              "biasanya lebih nyaman ketika semuanya sudah direncanakan dengan matang, dan merasa "
              "sedikit tidak nyaman ketika harus bergerak tanpa arah yang jelas. Dalam pekerjaan, "
              "kedisiplinanmu membuatmu unggul di peran yang membutuhkan struktur dan konsistensi "
              "tinggi, jenis pekerjaan yang butuh ketekunan bertahun-tahun untuk membuahkan hasil. "
              "Orang-orang terdekatmu tahu bahwa kalau kamu sudah menjanjikan sesuatu, kamu akan "
              "bekerja keras untuk memenuhinya, apa pun rintangannya.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kedisiplinan dan ketekunanmu membuat apa pun yang kamu bangun cenderung kokoh dan "
              "bertahan lama. Kamu juga jarang mengecewakan orang lain karena selalu berusaha "
              "memenuhi tanggung jawabmu. Sayangnya, kecintaan pada keteraturan ini kadang membuatmu "
              "sulit fleksibel ketika keadaan menuntut perubahan mendadak. Kebutuhanmu akan struktur "
              "yang jelas ini bisa membuatmu merasa cemas atau bahkan kaku saat menghadapi situasi "
              "yang di luar rencana. Kamu juga bisa terlalu fokus pada proses yang \"benar\" sampai "
              "lupa bahwa terkadang cara yang lebih fleksibel justru bisa membawa hasil yang sama "
              "baiknya, atau bahkan lebih baik.",
        "quote": "Fondasi yang kuat tetap butuh sedikit ruang untuk menyesuaikan diri dengan "
                 "perubahan.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Ketika rencana berubah mendadak, coba hadapi dengan tenang dan cari cara "
              "baru menyesuaikan diri, alih-alih merasa terganggu karena keluar dari jadwal. Latih "
              "juga dirimu untuk sesekali membiarkan sesuatu berjalan tanpa rencana detail terlebih "
              "dulu, sebagai cara membuktikan pada dirimu sendiri bahwa fleksibilitas juga bisa "
              "membawa hasil yang baik.",
    },
    5: {
        "tagline": "✦ Angka Hidup 5",
        "chip": "NUMEROLOGI",
        "title": "Angka Hidup 5 — Petualang yang Haus Kebebasan",
        "p1_label": "Siapa Kamu",
        "p1": "Angka hidup 5 melambangkan kebebasan, perubahan, dan rasa ingin tahu yang besar "
              "terhadap pengalaman baru. Kamu tidak suka terjebak dalam rutinitas yang monoton, dan "
              "selalu tertarik mencoba hal-hal yang belum pernah kamu lakukan sebelumnya. Hidup "
              "terasa lebih bermakna bagimu ketika penuh variasi. Kamu biasanya punya keingintahuan "
              "yang tinggi terhadap banyak hal, mulai dari tempat-tempat baru, budaya yang berbeda, "
              "sampai ide-ide yang menantang cara pandang lamamu. Dalam pekerjaan, kamu cocok di "
              "lingkungan yang dinamis dan memberi ruang untuk mencoba pendekatan baru, karena kamu "
              "cepat merasa jenuh dengan rutinitas yang itu-itu saja. Dalam pergaulan, kamu adalah "
              "sosok yang selalu punya cerita menarik untuk dibagikan, karena kamu jarang menolak "
              "kesempatan untuk mencoba sesuatu yang baru.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Keluwesan dan keberanianmu mencoba hal baru membuat hidupmu jarang terasa membosankan. "
              "Kamu juga mudah beradaptasi dengan lingkungan yang berbeda-beda. Namun kecintaan pada "
              "kebebasan ini kadang membuatmu kesulitan berkomitmen pada satu hal dalam jangka "
              "panjang, karena selalu ada godaan untuk berpindah ke hal yang baru. Pola ini bisa "
              "membuat orang-orang terdekatmu merasa tidak yakin seberapa lama kamu akan bertahan "
              "pada satu keputusan, entah itu pekerjaan, hubungan, maupun rencana jangka panjang. Kamu "
              "juga bisa terjebak dalam siklus mencari kebahagiaan lewat pengalaman baru, tanpa pernah "
              "benar-benar mendalami satu hal sampai merasakan kepuasan yang lebih utuh.",
        "quote": "Kebebasan akan terasa lebih bermakna kalau sesekali kamu memberi ruang bagi "
                 "komitmen untuk tumbuh.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Pilih satu komitmen yang sudah kamu buat, lalu pertahankan konsistensinya "
              "tanpa tergoda mencari variasi baru. Kamu bisa membuat kesepakatan dengan dirimu sendiri "
              "untuk bertahan pada satu hal selama jangka waktu tertentu, misalnya tiga bulan, sebelum "
              "menilai apakah kamu benar-benar ingin berpindah atau ternyata konsistensi itu membawa "
              "hasil yang lebih memuaskan dari yang kamu kira.",
    },
    6: {
        "tagline": "✦ Angka Hidup 6",
        "chip": "NUMEROLOGI",
        "title": "Angka Hidup 6 — Pengasuh yang Penuh Tanggung Jawab",
        "p1_label": "Siapa Kamu",
        "p1": "Angka hidup 6 melambangkan kepedulian, tanggung jawab, dan cinta terhadap keluarga "
              "maupun orang-orang terdekat. Kamu cenderung merasa bertanggung jawab menjaga "
              "kesejahteraan orang di sekitarmu, bahkan kadang lebih dari kesejahteraanmu sendiri. "
              "Kehadiranmu membuat orang lain merasa diperhatikan dan diurus dengan baik. Sejak muda, "
              "kamu mungkin sudah terbiasa mengambil peran mengurus orang lain, entah itu adik, "
              "teman, atau anggota keluarga yang membutuhkan bantuan. Dalam pekerjaan, sisi "
              "pengasuhmu membuatmu cocok di peran yang berhubungan langsung dengan kesejahteraan "
              "orang lain, seperti mengelola tim, pendidikan, atau bidang layanan yang membutuhkan "
              "empati tinggi. Dalam keluarga, kamu sering jadi sosok yang menjaga semuanya tetap "
              "berjalan baik, bahkan ketika tidak ada yang secara eksplisit memintamu melakukannya.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kepedulian dan tanggung jawabmu membuat orang-orang terdekat merasa aman dan "
              "diperhatikan. Kamu juga rela berkorban demi kebahagiaan orang yang kamu sayangi. Namun "
              "kebiasaan mengutamakan orang lain ini kadang membuatmu lupa mengurus kebutuhanmu "
              "sendiri, sampai akhirnya kamu yang kelelahan tanpa disadari orang di sekitarmu. Pola "
              "mengurus orang lain tanpa henti ini, kalau dibiarkan terus, bisa membuatmu merasa "
              "hampa atau lelah secara emosional, terutama saat kebaikanmu tidak dihargai atau "
              "bahkan dianggap wajar oleh orang-orang yang terbiasa menerima perhatianmu.",
        "quote": "Merawat orang lain akan lebih berkelanjutan kalau kamu juga merawat dirimu "
                 "sendiri.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Luangkan satu waktu khusus yang benar-benar untuk mengurus kebutuhanmu "
              "sendiri, tanpa merasa bersalah karena tidak sedang mengurus orang lain. Kamu bisa "
              "membuat jadwal sederhana untuk waktu pribadi ini, dan perlakukan itu sepenting janji "
              "dengan orang lain, supaya kamu tidak mudah membatalkannya demi mengurus kebutuhan "
              "orang lain lebih dulu.",
    },
    7: {
        "tagline": "✦ Angka Hidup 7",
        "chip": "NUMEROLOGI",
        "title": "Angka Hidup 7 — Pemikir Mendalam yang Penuh Perenungan",
        "p1_label": "Siapa Kamu",
        "p1": "Angka hidup 7 melambangkan kedalaman berpikir, rasa ingin tahu terhadap makna di balik "
              "sesuatu, dan kecenderungan untuk merenung. Kamu jarang puas dengan jawaban yang "
              "sederhana, dan selalu ingin memahami sesuatu sampai ke akarnya. Waktu sendiri terasa "
              "penting bagimu untuk mengolah pikiran dan menemukan kejernihan. Kamu biasanya lebih "
              "tertarik pada percakapan yang mendalam dibanding basa-basi ringan, dan senang "
              "mengeksplorasi topik-topik yang jarang dibahas orang kebanyakan. Dalam pekerjaan, "
              "kedalaman analisismu membuatmu unggul di bidang yang membutuhkan riset, pemikiran "
              "kritis, atau pemahaman mendalam terhadap suatu masalah. Kamu juga cenderung "
              "membutuhkan waktu sendirian secara teratur untuk mengisi ulang energi, karena terlalu "
              "banyak interaksi sosial bisa membuatmu merasa lelah secara mental.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kedalaman berpikirmu membuatmu bisa melihat sesuatu dari sudut pandang yang jarang "
              "terpikirkan orang lain. Kamu juga punya kemampuan analisis yang tajam. Namun "
              "kecenderungan untuk banyak merenung sendirian ini kadang membuatmu menjauh dari orang "
              "lain, sampai mereka merasa sulit benar-benar dekat denganmu. Kebiasaan memproses "
              "segalanya sendirian ini bisa membuat orang-orang terdekatmu merasa tidak diberi "
              "kesempatan untuk memahami apa yang sedang kamu pikirkan atau rasakan. Kamu juga bisa "
              "terjebak dalam analisis yang berlebihan, sampai sulit mengambil tindakan karena terus "
              "mencari pemahaman yang lebih sempurna.",
        "quote": "Perenungan yang dalam akan lebih bermakna kalau sesekali kamu bagikan hasilnya "
                 "kepada orang lain.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba ajak satu orang terdekatmu berdiskusi tentang sesuatu yang sedang kamu pikirkan, "
              "alih-alih memprosesnya sendirian seperti biasa. Kamu juga bisa melatih diri menetapkan "
              "batas waktu untuk merenungkan sesuatu, misalnya satu atau dua hari, sebelum akhirnya "
              "memutuskan untuk bertindak, supaya perenungan tidak berubah menjadi penundaan yang "
              "berlarut-larut.",
    },
    8: {
        "tagline": "✦ Angka Hidup 8",
        "chip": "NUMEROLOGI",
        "title": "Angka Hidup 8 — Pengelola yang Rapi",
        "p1_label": "Siapa Kamu",
        "p1": "Angka hidup 8 dihitung dari penjumlahan digit tanggal lahirmu, dan dalam numerologi "
              "angka ini identik dengan kemampuan mengelola sesuatu secara terstruktur, baik itu "
              "waktu, uang, maupun rencana jangka panjang. Kamu cenderung berpikir realistis dan "
              "senang melihat hasil yang bisa diukur. Kamu biasanya punya naluri bisnis atau "
              "manajerial yang kuat, dan cepat melihat bagaimana sebuah sumber daya, baik itu waktu, "
              "uang, atau tenaga, bisa dikelola dengan lebih efisien. Dalam pekerjaan, kemampuan ini "
              "membuatmu cocok mengisi peran yang berhubungan dengan pengelolaan, perencanaan "
              "keuangan, atau kepemimpinan yang berorientasi hasil. Kamu juga cenderung punya standar "
              "yang jelas tentang apa yang dianggap sukses, dan bekerja keras secara konsisten untuk "
              "mencapainya.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Disiplin dan tanggung jawabmu membuat orang lain merasa aman menitipkan urusan penting "
              "kepadamu. Meski begitu, fokus yang terlalu besar pada hasil kadang membuatmu lupa "
              "menikmati proses, sehingga pencapaian yang seharusnya membanggakan malah terasa "
              "biasa saja. Kebiasaan mengukur segalanya lewat hasil yang terlihat ini bisa membuatmu "
              "kurang menghargai usaha-usaha kecil yang sebenarnya juga penting dalam perjalananmu. "
              "Kamu juga bisa terlalu fokus pada pencapaian materi atau status, sampai mengabaikan "
              "hubungan personal yang sebenarnya juga membutuhkan perhatianmu.",
        "quote": "Pencapaian akan terasa lebih berarti kalau kamu sempat menikmati perjalanannya.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba beri dirimu waktu untuk merayakan pencapaian kecil sebelum langsung berpindah ke "
              "target berikutnya. Kebiasaan ini akan membuat perjalananmu terasa lebih ringan. Kamu "
              "juga bisa menyisihkan waktu khusus setiap minggu untuk terhubung dengan orang-orang "
              "terdekat, tanpa membahas pekerjaan atau target apa pun, sebagai cara menjaga "
              "keseimbangan antara pencapaian dan hubungan personal.",
    },
    9: {
        "tagline": "✦ Angka Hidup 9",
        "chip": "NUMEROLOGI",
        "title": "Angka Hidup 9 — Jiwa Dermawan yang Berpandangan Luas",
        "p1_label": "Siapa Kamu",
        "p1": "Angka hidup 9 melambangkan kepedulian terhadap sesama, jiwa yang dermawan, dan cara "
              "pandang yang luas melampaui kepentingan diri sendiri. Kamu cenderung memikirkan "
              "dampak dari tindakanmu terhadap orang lain atau dunia secara umum, dan sering merasa "
              "terpanggil untuk membantu ketika melihat ketidakadilan. Kamu biasanya punya empati "
              "yang meluas, tidak hanya kepada orang-orang terdekat, tapi juga kepada mereka yang "
              "bahkan tidak kamu kenal secara personal. Dalam pekerjaan, kepedulian ini membuatmu "
              "cocok di bidang yang berhubungan dengan pelayanan sosial, pendidikan, atau apa pun yang "
              "punya dampak positif bagi banyak orang. Dalam hubungan personal, kamu adalah sosok "
              "yang mudah memaafkan, dan jarang membiarkan konflik kecil merusak hubungan yang sudah "
              "terjalin lama.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kepedulian dan kebesaran hatimu membuat orang lain merasa terinspirasi untuk juga "
              "peduli pada sesama. Kamu juga mudah memaafkan dan jarang menyimpan dendam. Namun sisi "
              "idealis ini kadang membuatmu kecewa berat ketika kenyataan tidak sesuai harapanmu "
              "tentang kebaikan orang lain. Idealisme yang tinggi ini bisa membuatmu merasa kecil "
              "hati saat melihat betapa lambatnya perubahan besar terjadi di dunia, meski kamu sudah "
              "berusaha sebaik mungkin. Kamu juga bisa terlalu banyak memberi tanpa memperhatikan "
              "batas kemampuanmu sendiri, sampai akhirnya kehabisan energi untuk menjaga dirimu "
              "sendiri.",
        "quote": "Kepedulian besar tetap perlu disertai penerimaan bahwa tidak semua orang akan "
                 "sebaik yang kamu harapkan.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Ketika kecewa terhadap sikap seseorang, coba terima bahwa itu bukan "
              "cerminan dari kebaikanmu sendiri, dan lanjutkan tanpa membawa kekecewaan itu terlalu "
              "lama. Kamu juga bisa melatih diri menetapkan batas yang wajar dalam memberi, supaya "
              "kepedulian besarmu tetap berkelanjutan tanpa membuatmu kehabisan energi untuk dirimu "
              "sendiri.",
    },
    11: {
        "tagline": "✦ Angka Hidup 11 (Master Number)",
        "chip": "NUMEROLOGI",
        "title": "Angka Hidup 11 — Intuisi yang Menyala Terang",
        "p1_label": "Siapa Kamu",
        "p1": "Angka hidup 11 adalah salah satu Master Number dalam numerologi, angka yang sengaja "
              "tidak direduksi lebih jauh karena dianggap membawa getaran yang lebih kuat. Kamu "
              "punya intuisi yang sangat tajam, dan sering merasakan atau memahami sesuatu jauh "
              "sebelum orang lain menyadarinya. Ada semacam kepekaan batin yang membuatmu peka "
              "terhadap suasana maupun perasaan di sekitarmu. Kepekaan ini sering membuatmu merasa "
              "\"berbeda\" dari orang-orang di sekitarmu, karena kamu menangkap hal-hal yang orang "
              "lain lewatkan begitu saja. Dalam kehidupan sehari-hari, kamu mungkin sering "
              "mengalami firasat yang ternyata benar, atau merasakan suasana sebuah ruangan bahkan "
              "sebelum kamu benar-benar memahami situasinya secara rasional. Kamu juga cenderung "
              "punya visi yang kuat tentang bagaimana dunia seharusnya berjalan, dan itu membuatmu "
              "sering jadi sumber inspirasi bagi orang lain.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Intuisi dan kepekaanmu yang tajam membuatmu bisa menjadi sumber inspirasi bagi orang "
              "lain, karena kamu sering melihat kemungkinan yang belum terpikirkan. Kamu juga punya "
              "idealisme yang kuat tentang bagaimana seharusnya sesuatu berjalan. Namun kepekaan "
              "yang besar ini kadang membuatmu mudah kewalahan oleh emosi, baik emosimu sendiri "
              "maupun emosi orang di sekitarmu. Kepekaan yang tidak dijaga ini bisa membuatmu "
              "kelelahan secara mental, terutama saat berada di lingkungan yang penuh tekanan atau "
              "emosi negatif. Kamu juga bisa merasa terlalu tertekan oleh idealisme dan ekspektasi "
              "tinggi yang kamu tetapkan untuk dirimu sendiri, sampai lupa bahwa kamu juga manusia "
              "biasa yang berhak melakukan kesalahan.",
        "quote": "Intuisi yang tajam akan lebih membawa kebaikan kalau kamu juga menjaga "
                 "ketenanganmu sendiri.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Ketika merasa kewalahan oleh perasaan, coba luangkan waktu sendirian "
              "sejenak untuk menenangkan pikiran, sebelum memutuskan langkah selanjutnya. Kamu juga "
              "bisa melatih diri dengan kebiasaan sederhana seperti menulis jurnal atau meditasi "
              "singkat setiap hari, supaya kepekaan yang besar dalam dirimu tetap jadi kekuatan, "
              "bukan beban yang menguras energimu.",
    },
    22: {
        "tagline": "✦ Angka Hidup 22 (Master Number)",
        "chip": "NUMEROLOGI",
        "title": "Angka Hidup 22 — Sang Pembangun Besar",
        "p1_label": "Siapa Kamu",
        "p1": "Angka hidup 22 adalah Master Number yang dikenal sebagai 'Sang Pembangun Besar' dalam "
              "numerologi, karena menggabungkan visi besar dengan kemampuan mewujudkannya secara "
              "nyata. Kamu tidak hanya bermimpi besar, tapi juga punya ketekunan untuk benar-benar "
              "mewujudkan mimpi itu langkah demi langkah. Kamu sering memikirkan dampak jangka "
              "panjang dari apa yang kamu bangun. Kombinasi visi dan ketekunan ini jarang dimiliki "
              "banyak orang sekaligus, karena biasanya orang punya salah satu saja: bisa bermimpi "
              "besar tapi kurang tekun, atau tekun tapi tidak berani bermimpi besar. Dalam pekerjaan, "
              "kamu cocok memegang proyek-proyek besar yang butuh perencanaan matang sekaligus "
              "eksekusi jangka panjang, seperti membangun institusi, sistem, atau warisan yang bisa "
              "dinikmati banyak orang. Orang-orang di sekitarmu sering merasa yakin bahwa rencana "
              "besarmu bukan sekadar angan-angan, karena kamu selalu punya langkah konkret untuk "
              "mewujudkannya.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Perpaduan visi besar dan ketekunanmu membuat orang lain percaya bahwa apa yang kamu "
              "rencanakan benar-benar bisa terwujud, bukan sekadar angan-angan. Kamu juga sanggup "
              "bekerja dalam jangka panjang demi hasil yang besar. Namun standar yang begitu tinggi "
              "ini kadang membuatmu merasa tertekan oleh beban ekspektasi yang kamu tetapkan sendiri. "
              "Beban ini bisa membuatmu jarang merasa puas, karena selalu ada visi yang lebih besar "
              "lagi untuk dikejar. Kamu juga bisa terlalu banyak menanggung tanggung jawab sendirian, "
              "karena merasa hanya kamu yang benar-benar memahami gambaran besar dari apa yang sedang "
              "dibangun.",
        "quote": "Membangun sesuatu yang besar tetap butuh jeda, supaya kamu tidak habis sebelum "
                 "mimpimu benar-benar selesai.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Pecah satu tujuan besarmu menjadi langkah-langkah kecil, dan izinkan "
              "dirimu merasa cukup setelah menyelesaikan satu langkah kecil itu. Kamu juga bisa "
              "melatih diri mendelegasikan sebagian tanggung jawab kepada orang lain yang kamu "
              "percaya, supaya beban besar yang kamu pikul tidak sepenuhnya bertumpu di pundakmu "
              "sendiri.",
    },
    33: {
        "tagline": "✦ Angka Hidup 33 (Master Number)",
        "chip": "NUMEROLOGI",
        "title": "Angka Hidup 33 — Pembimbing yang Penuh Kasih",
        "p1_label": "Siapa Kamu",
        "p1": "Angka hidup 33 adalah Master Number paling jarang muncul dalam numerologi, dikenal "
              "sebagai 'Sang Pembimbing' karena melambangkan kasih sayang tanpa syarat dan keinginan "
              "besar untuk membantu pertumbuhan orang lain. Kamu punya kemampuan alami untuk membuat "
              "orang lain merasa didukung dan dipahami, seringkali tanpa kamu sadari sendiri "
              "seberapa besar pengaruhmu terhadap mereka. Kamu biasanya jadi tempat orang lain "
              "kembali saat mereka butuh bimbingan atau sekadar didengar, karena caramu memberi "
              "dukungan terasa tulus dan tanpa banyak menghakimi. Dalam pekerjaan, kemampuan ini "
              "membuatmu cocok di bidang yang berhubungan dengan pengajaran, konseling, atau peran "
              "kepemimpinan yang berfokus pada pengembangan orang lain. Dalam hubungan personal, kamu "
              "sering jadi sosok yang paling dipercaya untuk mendengarkan masalah orang-orang "
              "terdekatmu, karena mereka tahu kamu akan mendukung tanpa menghakimi.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kasih sayang dan kepedulianmu terhadap perkembangan orang lain membuatmu jadi sosok "
              "yang dicari saat orang butuh bimbingan atau dukungan emosional. Kamu juga sabar "
              "menemani proses orang lain tanpa terburu-buru. Namun kecenderungan untuk selalu "
              "memberi ini kadang membuatmu lupa bahwa kamu sendiri juga berhak menerima dukungan "
              "yang sama besarnya. Kebiasaan selalu jadi pihak yang memberi ini bisa membuatmu "
              "kehabisan energi emosional tanpa disadari, terutama karena kamu jarang secara "
              "terbuka mengakui saat kamu sendiri sedang membutuhkan bantuan. Orang lain juga bisa "
              "terbiasa menganggapmu selalu kuat, sampai lupa bertanya bagaimana kabarmu sendiri.",
        "quote": "Membimbing orang lain akan lebih berkelanjutan kalau kamu juga mengizinkan dirimu "
                 "dibimbing dan didukung.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba terima bantuan atau dukungan dari orang lain tanpa langsung "
              "menolaknya dengan alasan bisa mengurus semuanya sendiri. Kamu juga bisa melatih diri "
              "untuk secara terbuka bercerita saat kamu sendiri sedang menghadapi kesulitan, supaya "
              "orang-orang yang kamu bimbing selama ini juga punya kesempatan membalas kebaikan yang "
              "sudah kamu berikan.",
    },
}
