"""
Konten Matrix Destiny — Titik Inti / Arketipe Utama (22 kategori).

Key dict ini adalah INTEGER 1-22, HARUS sama persis dengan nilai
"titik_inti" dari engine/matrix_destiny.py (hitung_matrix_destiny()).
nama_arketipe Inggris (mis. "The Partners") cocok dengan
engine.matrix_destiny.NAMA_ARKETIPE dan nama file assets/cards/matrix_destiny/.

CATATAN SCOPE: konten di bawah ini adalah untuk TITIK INTI (Titik Pusat /
Inti Jiwa dari octagram). Titik-titik lain di octagram (Personal Square,
Ancestral Square, Love/Money/Purpose, tabel 7 Chakra) sudah dihitung penuh
oleh engine/matrix_destiny.py dan ditampilkan sebagai diagram + tooltip di
revealpage.py, tapi belum masing-masing punya paragraf interpretasi
tersendiri seperti di bawah ini (masih pakai judul arketipe singkat dari
NAMA_ARKETIPE sebagai label tooltip).

Struktur tiap entri sama persis dengan DUMMY_RESULTS di views/revealpage.py.

REVISI (26 Sep 2026 malam): isi p1/p2/p3 diperpanjang 2-3x lipat dari versi
sebelumnya (per instruksi Stev), supaya laporannya terasa lebih bernilai
dan aplikatif, bukan cuma label singkat.
"""

MATRIX_DESTINY_CONTENT = {
    1: {
        "tagline": "✧ The Beginner",
        "chip": "MATRIX DESTINY",
        "title": "The Beginner — Sang Pemula yang Berani Memulai",
        "p1_label": "Siapa Kamu",
        "p1": "Dalam pembacaan Matrix Destiny, susunan titik dari tanggal lahirmu membentuk arketipe "
              "The Beginner, sosok yang membawa energi awal mula dan keberanian untuk memulai sesuatu "
              "dari nol. Kamu jarang takut dengan lembaran kosong, karena bagimu setiap permulaan "
              "adalah kesempatan baru untuk membuktikan diri. Energi ini biasanya sudah terlihat sejak "
              "kamu masih muda, lewat kebiasaan mengangkat tangan lebih dulu untuk mencoba sesuatu yang "
              "belum pernah kamu lakukan. Dalam pekerjaan, kamu cocok mengisi peran perintis, seperti "
              "membuka cabang baru, merancang produk pertama, atau memimpin tim yang baru dibentuk. "
              "Dalam kehidupan sosial, kamu sering jadi orang yang mengajak teman-temanmu keluar dari "
              "rutinitas dan mencoba hal baru bersama, karena bagimu ketidakpastian di awal justru "
              "terasa menyenangkan, bukan menakutkan.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Semangat dan keberanianmu memulai sesuatu membuat orang lain sering terinspirasi untuk "
              "berhenti menunda dan segera bertindak. Kamu juga jarang terbebani rasa takut gagal "
              "sebelum benar-benar mencoba. Namun energi awal yang begitu besar ini kadang tidak "
              "dibarengi kesabaran untuk menyelesaikan sesuatu sampai tuntas. Kamu bisa punya banyak "
              "proyek yang dimulai dengan penuh semangat, tapi berhenti di tengah jalan begitu "
              "tantangan sebenarnya baru dimulai. Orang-orang di sekitarmu mungkin melihatmu sebagai "
              "sosok yang penuh ide, tapi juga sedikit ragu mempercayakan proyek jangka panjang "
              "kepadamu, karena tahu semangat awalmu bisa memudar.",
        "quote": "Keberanian memulai akan terasa lebih bermakna kalau disertai niat untuk benar-"
                 "benar menyelesaikannya.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Pilih satu hal yang baru saja kamu mulai, lalu berkomitmenlah menyelesaikan tahap "
              "pertamanya secara penuh sebelum memulai hal baru yang lain. Buat kesepakatan sederhana "
              "dengan dirimu sendiri: setiap kali ide baru muncul di tengah proses, catat dulu di "
              "tempat terpisah, dan kembali fokus pada yang sedang berjalan. Cara ini membantu energi "
              "awalmu tersalurkan tanpa mengorbankan penyelesaian yang sudah dimulai.",
    },
    2: {
        "tagline": "✧ The Listener",
        "chip": "MATRIX DESTINY",
        "title": "The Listener — Sang Pendengar yang Penuh Empati",
        "p1_label": "Siapa Kamu",
        "p1": "Susunan titik dari tanggal lahirmu membentuk arketipe The Listener, sosok yang secara "
              "alami punya kemampuan mendengarkan dengan sepenuh hati. Orang-orang merasa nyaman "
              "bercerita kepadamu, karena kamu jarang buru-buru menghakimi atau memotong pembicaraan "
              "sebelum mereka selesai bicara. Kemampuan ini membuatmu sering jadi tempat curhat "
              "pertama yang dituju banyak orang, entah itu keluarga, teman, atau bahkan rekan kerja "
              "yang belum terlalu dekat sekalipun. Dalam lingkungan kerja, sisi ini membuatmu cocok "
              "mengisi peran yang membutuhkan kemampuan memahami kebutuhan orang lain secara mendalam, "
              "seperti layanan pelanggan, konseling, atau posisi yang menjembatani komunikasi antar "
              "pihak. Kamu juga cenderung sabar menunggu orang lain selesai bicara sebelum "
              "menanggapi, sesuatu yang jarang dimiliki banyak orang di tengah percakapan yang serba "
              "cepat.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kemampuanmu mendengarkan membuat orang lain merasa benar-benar dipahami saat "
              "bersamamu. Kamu juga peka menangkap hal-hal yang tidak terucap secara langsung. Namun "
              "karena terlalu fokus mendengarkan orang lain, kamu kadang lupa menyuarakan apa yang "
              "sebenarnya kamu rasakan atau butuhkan. Kebiasaan ini bisa membuat orang-orang di "
              "sekitarmu terbiasa selalu bercerita kepadamu, tanpa pernah balik bertanya bagaimana "
              "kabarmu sendiri. Lama-lama, kamu bisa merasa seperti wadah bagi cerita semua orang, "
              "tapi tidak punya tempat sendiri untuk menuangkan isi hatimu.",
        "quote": "Mendengarkan orang lain itu berharga, tapi suaramu sendiri juga layak untuk "
                 "didengar.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba ceritakan satu hal yang sedang kamu rasakan kepada orang terdekat, "
              "alih-alih hanya menjadi pendengar seperti biasanya. Mulai dari hal kecil, seperti "
              "mengakui saat kamu sedang lelah atau butuh dukungan, alih-alih terus menahannya sendiri "
              "sambil tetap mendengarkan cerita orang lain. Orang-orang yang benar-benar peduli "
              "padamu akan senang mendapat kesempatan untuk balas mendengarkanmu.",
    },
    3: {
        "tagline": "✧ The Creator",
        "chip": "MATRIX DESTINY",
        "title": "The Creator — Sang Pencipta yang Penuh Imajinasi",
        "p1_label": "Siapa Kamu",
        "p1": "Susunan titik dari tanggal lahirmu membentuk arketipe The Creator, sosok yang punya "
              "imajinasi kaya dan dorongan kuat untuk menciptakan sesuatu yang belum pernah ada "
              "sebelumnya. Kamu melihat dunia dengan cara yang berbeda, dan sering menemukan "
              "kemungkinan-kemungkinan baru dari hal-hal yang tampak biasa. Rasa ingin taumu terhadap "
              "kemungkinan-kemungkinan baru ini membuatmu jarang puas hanya mengikuti cara yang sudah "
              "ada; kamu selalu bertanya \"bagaimana kalau dibuat dengan cara lain?\". Dalam "
              "pekerjaan, dorongan menciptakan ini membuatmu unggul di bidang yang membutuhkan "
              "inovasi, entah itu produk baru, konten kreatif, atau solusi atas masalah yang belum "
              "terpecahkan. Dalam kehidupan pribadi, orang-orang sering datang kepadamu untuk mencari "
              "ide segar, karena mereka tahu kamu jarang kehabisan gagasan baru.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kreativitas dan orisinalitasmu membuat karya atau ide-idemu terasa segar dan berbeda "
              "dari kebanyakan orang. Kamu juga tidak takut mengambil pendekatan yang tidak biasa. "
              "Namun terlalu banyak ide yang muncul sekaligus kadang membuatmu kesulitan memilih mana "
              "yang benar-benar layak untuk diwujudkan sampai selesai. Kamu bisa terjebak dalam "
              "siklus terus-menerus memikirkan ide baru, sampai tidak ada satu pun yang benar-benar "
              "kamu kerjakan sampai matang. Orang lain mungkin melihatmu sebagai sosok yang penuh "
              "gagasan brilian, tapi juga sedikit kesulitan mengikuti eksekusi konkret dari semua ide "
              "itu.",
        "quote": "Imajinasi yang luas akan lebih bermakna kalau satu idenya benar-benar diwujudkan "
                 "sampai tuntas.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Pilih satu ide yang paling ingin kamu wujudkan, lalu curahkan perhatianmu "
              "sepenuhnya di situ tanpa tergoda memikirkan ide lain. Buat target kecil setiap minggu "
              "untuk ide yang kamu pilih itu, dan tahan godaan untuk memulai ide baru sebelum target "
              "itu tercapai. Kamu akan terkejut melihat betapa jauh satu ide bisa berkembang kalau "
              "diberi fokus penuh.",
    },
    4: {
        "tagline": "✧ The Ruler",
        "chip": "MATRIX DESTINY",
        "title": "The Ruler — Sang Penguasa yang Tegas",
        "p1_label": "Siapa Kamu",
        "p1": "Susunan titik dari tanggal lahirmu membentuk arketipe The Ruler, sosok yang punya "
              "wibawa alami dan kemampuan mengambil keputusan dengan tegas. Orang-orang di sekitarmu "
              "sering melihatmu sebagai sosok yang bisa diandalkan untuk memimpin, karena kamu jarang "
              "ragu-ragu saat harus bertindak. Wibawa ini bukan sesuatu yang kamu buat-buat; itu "
              "muncul dari cara bicaramu yang penuh keyakinan dan sikap yang konsisten dalam berbagai "
              "situasi. Dalam pekerjaan, kamu cocok memegang posisi yang membutuhkan pengambilan "
              "keputusan cepat dan tegas, terutama di saat-saat krisis ketika orang lain masih "
              "bingung menentukan arah. Dalam keluarga atau kelompok pertemanan, kamu sering jadi "
              "sosok yang dituju saat semua orang butuh seseorang untuk menentukan langkah "
              "selanjutnya.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Ketegasan dan kemampuan memimpinmu membuat orang lain percaya pada arah yang kamu "
              "tentukan. Kamu juga bertanggung jawab penuh atas keputusan yang kamu ambil. Namun "
              "ketegasan ini kadang terlihat kaku di mata orang lain, sehingga mereka sungkan "
              "menyampaikan pendapat yang berbeda darimu. Kebiasaan cepat memutuskan ini bisa membuat "
              "orang-orang di sekitarmu merasa kurang dilibatkan, bahkan dalam hal-hal yang sebenarnya "
              "berdampak langsung pada mereka. Kamu juga bisa dianggap terlalu dominan dalam "
              "diskusi, sampai membuat suara-suara yang lebih pelan menjadi tidak terdengar.",
        "quote": "Kepemimpinan yang kuat juga membuka ruang bagi orang lain untuk berpendapat "
                 "berbeda.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba tanyakan secara terbuka pendapat orang lain sebelum mengambil "
              "keputusan, dan tunjukkan bahwa pendapat berbeda darimu tetap diterima dengan baik. "
              "Latih dirimu untuk diam sejenak setelah bertanya, memberi ruang bagi orang lain untuk "
              "benar-benar menyampaikan pandangannya, alih-alih langsung menyela dengan "
              "keputusanmu sendiri.",
    },
    5: {
        "tagline": "✧ The Teacher",
        "chip": "MATRIX DESTINY",
        "title": "The Teacher — Sang Guru yang Suka Berbagi Ilmu",
        "p1_label": "Siapa Kamu",
        "p1": "Susunan titik dari tanggal lahirmu membentuk arketipe The Teacher, sosok yang senang "
              "berbagi ilmu dan membantu orang lain memahami sesuatu dengan lebih baik. Kamu punya "
              "kesabaran untuk menjelaskan hal-hal yang rumit menjadi lebih sederhana, dan merasa "
              "puas ketika melihat orang lain berkembang berkat bantuanmu. Kamu biasanya punya cara "
              "menjelaskan yang mudah dipahami, karena kamu selalu berusaha melihat sesuatu dari sudut "
              "pandang orang yang belum mengerti, bukan hanya dari sudut pandangmu sendiri yang sudah "
              "paham. Dalam pekerjaan, kemampuan ini membuatmu cocok mengisi peran yang berhubungan "
              "dengan pengajaran, pelatihan, atau membimbing rekan kerja yang lebih junior. Orang-"
              "orang di sekitarmu sering datang bertanya kepadamu, bukan hanya karena kamu tahu "
              "jawabannya, tapi karena kamu bisa menjelaskannya dengan cara yang membuat mereka "
              "benar-benar mengerti.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kesabaran dan kemampuanmu menjelaskan sesuatu membuat orang lain merasa terbantu dan "
              "dihargai prosesnya, bukan hanya dinilai dari hasil akhir. Kamu juga senang melihat "
              "orang lain sukses. Namun kebiasaan selalu ingin membantu ini kadang membuatmu lupa "
              "untuk terus belajar dan berkembang untuk dirimu sendiri. Kamu bisa terlalu sibuk "
              "mengurus perkembangan orang lain, sampai perkembanganmu sendiri jadi terhenti atau "
              "tertunda. Kadang kamu juga merasa berat melihat orang yang kamu bimbing melampaui "
              "dirimu, meski di lain sisi kamu bangga karena itu berkat bantuanmu.",
        "quote": "Mengajar orang lain akan lebih bermakna kalau kamu juga terus memberi ruang untuk "
                 "belajar bagi dirimu sendiri.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Luangkan waktu untuk mempelajari sesuatu yang baru untuk dirimu sendiri, "
              "bukan untuk diajarkan kepada orang lain. Pilih satu topik yang murni menarik minatmu "
              "sendiri, tanpa memikirkan apakah nantinya kamu akan mengajarkan hal itu kepada siapa "
              "pun. Nikmati proses belajar itu sebagai hadiah untuk dirimu sendiri.",
    },
    6: {
        "tagline": "✧ The Partners",
        "chip": "MATRIX DESTINY",
        "title": "The Partners — Fondasi bagi Orang-Orang di Sekitarmu",
        "p1_label": "Siapa Kamu",
        "p1": "Dalam pembacaan Matrix Destiny, susunan titik dari tanggal lahirmu membentuk arketipe "
              "The Partners, sosok yang secara alami jadi tempat bersandar bagi keluarga maupun "
              "teman dekat. Kehadiranmu memberi rasa aman, bahkan tanpa kamu perlu berkata banyak. "
              "Orang-orang di sekitarmu sering merasa lebih tenang ketika kamu ada di dekat mereka, "
              "karena kamu memancarkan rasa stabil yang sulit dijelaskan tapi mudah dirasakan. Dalam "
              "hubungan personal, kamu cenderung jadi fondasi yang menjaga semuanya tetap berjalan, "
              "baik dalam keluarga, pertemanan, maupun hubungan kerja sama. Kamu juga jarang "
              "menuntut perhatian besar untuk dirimu sendiri, dan lebih fokus memastikan orang-orang "
              "yang kamu sayangi merasa didukung.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kesetiaanmu pada orang-orang terdekat jarang tergoyahkan, dan itu membuatmu jadi sosok "
              "yang bisa diandalkan dalam situasi sulit sekalipun. Namun karena terbiasa menjaga "
              "orang lain, kamu kadang lupa bahwa dirimu sendiri juga butuh dijaga oleh seseorang. "
              "Kebiasaan selalu jadi pihak yang kuat dan stabil ini bisa membuat orang lain lupa "
              "bertanya bagaimana kabarmu, karena mereka terbiasa melihatmu sebagai sosok yang selalu "
              "baik-baik saja. Kamu sendiri juga sering enggan menunjukkan kerentanan, karena merasa "
              "harus terus jadi fondasi yang kuat untuk orang lain.",
        "quote": "The Partners sejati juga tahu kapan waktunya untuk diam-diam dijaga balik.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Izinkan satu orang terdekatmu untuk benar-benar membantumu, tanpa buru-buru "
              "menolak dengan alasan bahwa kamu bisa mengurus semuanya sendiri. Mulai dengan berbagi "
              "satu kekhawatiran kecil kepada orang yang kamu percaya, dan biarkan mereka menjadi "
              "fondasi bagimu, sebagaimana kamu selama ini menjadi fondasi bagi mereka.",
    },
    7: {
        "tagline": "✧ The Conqueror",
        "chip": "MATRIX DESTINY",
        "title": "The Conqueror — Sang Penakluk yang Pantang Menyerah",
        "p1_label": "Siapa Kamu",
        "p1": "Susunan titik dari tanggal lahirmu membentuk arketipe The Conqueror, sosok yang punya "
              "tekad kuat untuk menaklukkan tantangan apa pun yang ada di depannya. Kamu jarang "
              "berhenti hanya karena satu kegagalan, dan justru menjadikan hambatan sebagai bahan "
              "bakar untuk semakin gigih berusaha. Dorongan ini membuatmu terlihat berbeda dari orang "
              "kebanyakan saat menghadapi kesulitan; ketika orang lain mundur, kamu justru semakin "
              "termotivasi untuk membuktikan bahwa kamu bisa melewatinya. Dalam pekerjaan, semangat "
              "juang ini membuatmu unggul di lingkungan yang penuh tantangan dan persaingan, jenis "
              "lingkungan yang membuat banyak orang lain menyerah lebih dulu. Dalam hidup sehari-"
              "hari, kamu sering jadi contoh bagi orang-orang di sekitarmu tentang bagaimana caranya "
              "bangkit setelah jatuh.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Ketekunan dan daya juangmu membuat orang lain kagum melihat caramu bangkit dari "
              "kegagalan. Kamu juga jarang mudah menyerah pada keadaan. Namun fokus yang terlalu "
              "besar pada 'menaklukkan' ini kadang membuatmu memandang segala sesuatu sebagai "
              "kompetisi, bahkan pada situasi yang sebenarnya tidak perlu diperlakukan seperti itu. "
              "Kebiasaan ini bisa membuatmu sulit rileks, karena selalu ada 'medan pertempuran' baru "
              "yang perlu kamu taklukkan. Orang-orang di sekitarmu juga bisa merasa lelah kalau harus "
              "selalu bersaing denganmu, bahkan dalam momen-momen santai yang sebenarnya tidak "
              "membutuhkan persaingan.",
        "quote": "Tidak semua hal dalam hidup perlu ditaklukkan, sebagian cukup dinikmati apa "
                 "adanya.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba nikmati satu aktivitas tanpa menjadikannya ajang untuk bersaing atau "
              "membuktikan sesuatu kepada siapa pun. Pilih sesuatu yang murni untuk kesenangan, "
              "seperti hobi santai atau waktu bersama keluarga, dan sadari setiap kali dorongan untuk "
              "'menang' muncul, lalu dengan sengaja lepaskan dorongan itu untuk sesaat.",
    },
    8: {
        "tagline": "✧ The Balance",
        "chip": "MATRIX DESTINY",
        "title": "The Balance — Sang Penjaga Keseimbangan",
        "p1_label": "Siapa Kamu",
        "p1": "Susunan titik dari tanggal lahirmu membentuk arketipe The Balance, sosok yang secara "
              "alami mencari keseimbangan dalam segala aspek hidupnya. Kamu tidak suka pergi ke "
              "ekstrem yang berlebihan, dan selalu berusaha menimbang berbagai sisi sebelum mengambil "
              "keputusan. Kamu cenderung nyaman berada di tengah, bukan karena takut memilih, tapi "
              "karena kamu memang percaya bahwa kebenaran sering berada di titik temu berbagai sudut "
              "pandang. Dalam pekerjaan, kamu cocok mengisi peran yang membutuhkan pertimbangan dari "
              "berbagai kepentingan, seperti manajemen konflik atau perencanaan yang melibatkan "
              "banyak pihak. Dalam hubungan personal, kamu sering jadi sosok penengah yang dipercaya "
              "kedua belah pihak, karena kamu jarang memihak secara membabi buta.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kemampuanmu menjaga keseimbangan membuatmu jarang terjebak dalam keputusan yang "
              "gegabah. Kamu juga adil dalam memandang berbagai sudut pandang. Namun terlalu fokus "
              "menjaga keseimbangan ini kadang membuatmu ragu-ragu memilih sisi, bahkan ketika "
              "situasinya sebenarnya membutuhkan sikap yang lebih tegas. Kebiasaan selalu mencari "
              "jalan tengah ini bisa membuatmu terlihat tidak punya pendirian yang kuat, meski "
              "sebenarnya kamu hanya sedang berusaha bersikap adil. Kamu juga bisa kehilangan momen "
              "penting karena terlalu lama menimbang, sementara keputusan sebenarnya butuh diambil "
              "segera.",
        "quote": "Keseimbangan yang sehat kadang juga berarti berani memilih satu sisi dengan "
                 "mantap.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Ketika dihadapkan pada satu pilihan, coba ambil sikap yang tegas, alih-alih "
              "terus mencari jalan tengah yang menyenangkan semua pihak. Latih diri dengan memberi "
              "batas waktu untuk menimbang, misalnya satu hari, lalu putuskan sebelum waktu itu habis, "
              "meski keputusan itu berarti tidak semua pihak akan merasa puas sepenuhnya.",
    },
    9: {
        "tagline": "✧ The Hermit",
        "chip": "MATRIX DESTINY",
        "title": "The Hermit — Sang Perenung yang Mandiri",
        "p1_label": "Siapa Kamu",
        "p1": "Susunan titik dari tanggal lahirmu membentuk arketipe The Hermit, sosok yang menemukan "
              "kekuatan besar dalam kesendirian dan perenungan. Kamu tidak selalu butuh keramaian "
              "untuk merasa utuh, dan justru sering menemukan kejernihan pikiran ketika sedang "
              "sendirian. Waktu sendirimu bukan pelarian dari orang lain, tapi ruang yang benar-benar "
              "kamu butuhkan untuk mengisi ulang energi dan memikirkan sesuatu secara mendalam. Dalam "
              "pekerjaan, kemandirian ini membuatmu cocok di peran yang membutuhkan konsentrasi tinggi "
              "dan pemikiran mendalam tanpa banyak gangguan, seperti riset atau perencanaan strategis. "
              "Orang-orang di sekitarmu tahu bahwa kadang kamu perlu waktu sendiri, dan mereka belajar "
              "menghargai kebutuhan itu tanpa menganggapnya sebagai penolakan terhadap mereka.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kemandirian dan kedalaman berpikirmu membuatmu jarang bergantung pada validasi orang "
              "lain untuk merasa yakin. Kamu juga bisa menemukan jawaban dari dalam dirimu sendiri. "
              "Namun kecenderungan menyendiri ini kadang membuatmu menjauh dari orang lain, bahkan "
              "pada saat kamu sebenarnya butuh dukungan mereka. Kebiasaan memproses segalanya sendiri "
              "ini bisa membuat orang-orang terdekatmu merasa jauh darimu, atau bahkan tidak "
              "menyadari saat kamu sedang kesulitan, karena kamu jarang menunjukkannya secara "
              "terbuka.",
        "quote": "Kesendirian itu berharga, tapi jangan sampai membuatmu menutup pintu bagi orang "
                 "yang ingin membantumu.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba hubungi satu orang yang sudah lama tidak kamu ajak bicara, dan "
              "biarkan dirimu terbuka pada kehadiran mereka. Latih juga dirimu untuk sesekali "
              "membagikan apa yang sedang kamu renungkan kepada orang lain, alih-alih menyimpannya "
              "sepenuhnya untuk dirimu sendiri.",
    },
    10: {
        "tagline": "✧ The Wheel",
        "chip": "MATRIX DESTINY",
        "title": "The Wheel — Sang Pembawa Perubahan",
        "p1_label": "Siapa Kamu",
        "p1": "Susunan titik dari tanggal lahirmu membentuk arketipe The Wheel, sosok yang erat "
              "kaitannya dengan siklus, perubahan, dan pergerakan hidup yang terus berputar. Kamu "
              "cenderung menerima bahwa hidup punya masa naik dan masa turun, dan jarang terlalu "
              "lama terpuruk saat menghadapi masa sulit. Penerimaan ini membuatmu lebih mudah "
              "bergerak maju dibanding orang yang terlalu lama terpaku pada satu kegagalan atau satu "
              "masa keemasan yang sudah lewat. Dalam pekerjaan, sikap ini membuatmu cukup tangguh "
              "menghadapi perubahan mendadak, seperti restrukturisasi, pergantian arah bisnis, atau "
              "situasi yang tidak terduga. Dalam kehidupan pribadi, kamu cenderung tidak terlalu "
              "terguncang menghadapi perubahan besar, karena bagimu itu memang bagian alami dari "
              "roda kehidupan yang terus berputar.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Penerimaanmu terhadap perubahan membuatmu lebih tangguh menghadapi naik turunnya "
              "hidup dibanding kebanyakan orang. Kamu juga cepat bangkit setelah mengalami kemunduran. "
              "Namun kebiasaan menerima perubahan secara pasif ini kadang membuatmu kurang berusaha "
              "mengendalikan arah hidupmu sendiri, dan lebih memilih pasrah pada keadaan. Sikap ini "
              "bisa membuatmu kehilangan kesempatan untuk benar-benar mengarahkan hidup ke arah yang "
              "kamu inginkan, karena kamu terlalu cepat menerima sesuatu sebagai \"memang sudah "
              "takdirnya begitu\", padahal ada ruang untuk kamu ubah kalau kamu berusaha lebih "
              "aktif.",
        "quote": "Menerima perubahan itu baik, tapi kamu juga punya kendali untuk mengarahkan roda "
                 "itu berputar ke arah yang kamu inginkan.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba ambil satu langkah aktif untuk mengarahkan sesuatu yang selama ini "
              "hanya kamu terima begitu saja sebagai keadaan yang tak bisa diubah. Pilih satu area "
              "dalam hidupmu yang selama ini kamu anggap sudah \"pasti begitu\", dan cari tahu "
              "apakah sebenarnya ada langkah kecil yang bisa kamu ambil untuk mengubah arahnya.",
    },
    11: {
        "tagline": "✧ The Brave",
        "chip": "MATRIX DESTINY",
        "title": "The Brave — Sang Pemberani yang Tangguh",
        "p1_label": "Siapa Kamu",
        "p1": "Susunan titik dari tanggal lahirmu membentuk arketipe The Brave, sosok yang punya "
              "keberanian menghadapi ketakutan alih-alih menghindarinya. Kamu jarang lari dari "
              "situasi sulit, dan justru sering maju lebih dulu ketika orang lain masih ragu-ragu "
              "untuk bertindak. Keberanian ini bukan berarti kamu tidak pernah takut, tapi kamu "
              "memilih untuk tetap melangkah meski rasa takut itu ada. Dalam pekerjaan, sifat ini "
              "membuatmu cocok mengisi peran yang membutuhkan keberanian mengambil keputusan sulit "
              "atau menghadapi situasi krisis. Dalam kehidupan sosial, orang-orang sering merasa "
              "lebih tenang berada di dekatmu saat menghadapi masalah besar, karena mereka tahu kamu "
              "tidak akan panik dan tetap bisa berpikir jernih.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Keberanianmu menghadapi hal-hal sulit membuat orang lain merasa lebih tenang berada "
              "di sekitarmu saat krisis. Kamu juga jarang membiarkan rasa takut menghalangi "
              "langkahmu. Namun keberanian yang besar ini kadang membuatmu meremehkan risiko, atau "
              "lupa meminta bantuan saat situasi sebenarnya sudah di luar kendalimu sendiri. "
              "Kebiasaan menghadapi semuanya sendirian ini bisa membuatmu menanggung beban yang "
              "sebenarnya bisa lebih ringan kalau kamu berbagi dengan orang lain lebih awal.",
        "quote": "Keberanian sejati juga tahu kapan saatnya meminta bantuan, bukan menghadapi "
                 "semuanya sendirian.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Ketika menghadapi tantangan besar, coba minta pendapat atau bantuan dari "
              "orang lain terlebih dulu, sebelum memutuskan untuk menghadapinya sendirian. Latih "
              "dirimu untuk mengenali tanda-tanda saat sebuah situasi sudah terlalu besar untuk "
              "dihadapi sendiri, dan jangan ragu melibatkan orang lain sebelum keadaan menjadi lebih "
              "sulit dari yang seharusnya.",
    },
    12: {
        "tagline": "✧ The Sacrifice",
        "chip": "MATRIX DESTINY",
        "title": "The Sacrifice — Sang Pemberi yang Rela Berkorban",
        "p1_label": "Siapa Kamu",
        "p1": "Susunan titik dari tanggal lahirmu membentuk arketipe The Sacrifice, sosok yang punya "
              "kerelaan besar untuk mengorbankan kepentingannya demi kebaikan orang lain. Kamu "
              "cenderung memikirkan dampak tindakanmu terhadap orang lain terlebih dulu, bahkan "
              "sebelum memikirkan dirimu sendiri. Kerelaan ini biasanya sudah terlihat sejak dulu, "
              "misalnya lewat kebiasaan mendahulukan kebutuhan keluarga atau teman dekat, bahkan saat "
              "itu berarti kamu harus menunda keinginanmu sendiri. Dalam pekerjaan, sisi ini membuatmu "
              "cocok di peran yang membutuhkan pengabdian tinggi, seperti pelayanan sosial atau posisi "
              "yang berdampak langsung pada kesejahteraan orang lain. Orang-orang di sekitarmu merasa "
              "sangat dicintai dan diutamakan olehmu, karena kamu memang tulus dalam memberi.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kerelaan berkorbanmu membuat orang-orang terdekat merasa sangat dicintai dan "
              "diutamakan. Kamu juga jarang mengharapkan balasan atas kebaikan yang kamu berikan. "
              "Namun kebiasaan mengorbankan diri ini kadang berjalan terlalu jauh, sampai kamu "
              "kehilangan bagian dari dirimu sendiri demi kepentingan orang lain. Pola ini bisa "
              "membuatmu merasa kosong atau lelah tanpa alasan yang jelas, karena kamu terus memberi "
              "tanpa pernah benar-benar mengisi ulang dirimu sendiri. Kamu juga bisa dimanfaatkan "
              "orang-orang yang tahu betapa mudahnya kamu mengalah demi mereka.",
        "quote": "Berkorban untuk orang lain itu mulia, tapi dirimu sendiri juga berhak diperjuangkan "
                 "dengan cara yang sama.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba tolak satu permintaan yang sebenarnya memberatkanmu, dan utamakan "
              "kebutuhanmu sendiri untuk sekali itu. Latih diri untuk mengenali batas kemampuanmu, "
              "dan ingat bahwa berkata \"tidak\" pada satu permintaan tidak mengurangi ketulusanmu "
              "dalam membantu orang lain di lain waktu.",
    },
    13: {
        "tagline": "✧ The Transformation",
        "chip": "MATRIX DESTINY",
        "title": "The Transformation — Sang Pembawa Perubahan Besar",
        "p1_label": "Siapa Kamu",
        "p1": "Susunan titik dari tanggal lahirmu membentuk arketipe The Transformation, sosok yang "
              "sering mengalami perubahan besar dalam hidupnya dan keluar sebagai versi diri yang "
              "lebih kuat setiap kalinya. Kamu tidak takut meninggalkan sesuatu yang sudah tidak "
              "sesuai lagi denganmu, meski itu berarti harus memulai babak baru dari awal. Kamu "
              "biasanya sudah beberapa kali mengalami titik balik besar dalam hidup, entah itu "
              "perubahan karier, hubungan, atau cara pandang terhadap diri sendiri, dan setiap "
              "kalinya kamu keluar sebagai versi yang lebih matang. Dalam pekerjaan, kemampuan "
              "beradaptasi dengan perubahan besar ini membuatmu cukup tangguh menghadapi masa "
              "transisi yang membuat banyak orang lain kewalahan. Orang-orang di sekitarmu kadang "
              "kagum, kadang juga sedikit khawatir, melihat betapa beraninya kamu melepaskan sesuatu "
              "yang sudah mapan demi memulai sesuatu yang baru.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kemampuanmu bertransformasi membuatmu jarang terjebak dalam keadaan yang sudah tidak "
              "membawa kebaikan bagimu. Kamu juga tangguh menghadapi masa-masa peralihan yang berat. "
              "Namun perubahan besar yang terlalu sering ini kadang membuat orang di sekitarmu "
              "kesulitan mengikuti arah hidupmu yang terus bergeser. Orang-orang terdekatmu mungkin "
              "merasa perlu menyesuaikan diri berkali-kali dengan versi dirimu yang baru, dan itu bisa "
              "terasa melelahkan bagi mereka, meski kamu sendiri merasa perubahan itu perlu dan "
              "sehat.",
        "quote": "Bertransformasi itu kekuatan, tapi memberi waktu bagi orang lain untuk mengikutimu "
                 "juga bagian dari kebaikan.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Sebelum membuat perubahan besar, coba ceritakan dulu rencanamu kepada orang "
              "terdekat, supaya mereka tidak merasa tertinggal begitu saja. Beri mereka waktu untuk "
              "bertanya dan memahami alasan di balik perubahan yang kamu rencanakan, supaya "
              "transformasimu terasa seperti perjalanan bersama, bukan kejutan yang tiba-tiba.",
    },
    14: {
        "tagline": "✧ The Alchemist",
        "chip": "MATRIX DESTINY",
        "title": "The Alchemist — Sang Peramu yang Cerdik",
        "p1_label": "Siapa Kamu",
        "p1": "Susunan titik dari tanggal lahirmu membentuk arketipe The Alchemist, sosok yang punya "
              "kemampuan meramu berbagai hal yang tampaknya tidak berhubungan menjadi sesuatu yang "
              "baru dan bernilai. Kamu pandai melihat potensi tersembunyi dalam situasi maupun "
              "sumber daya yang terbatas. Kemampuan ini membuatmu bisa menciptakan solusi kreatif "
              "dari keterbatasan, sesuatu yang sering membuat orang lain terkejut karena mereka "
              "sendiri tidak melihat kemungkinan itu sebelumnya. Dalam pekerjaan, kecerdikanmu "
              "membuatmu cocok mengisi peran yang membutuhkan improvisasi dan pemecahan masalah "
              "dengan sumber daya seadanya, seperti mengelola proyek dengan anggaran terbatas atau "
              "mencari solusi cepat di tengah kondisi yang tidak ideal. Orang-orang di sekitarmu "
              "sering kagum melihat bagaimana kamu bisa menghasilkan sesuatu yang berharga dari "
              "bahan-bahan yang tampaknya biasa saja.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kecerdikan dan kreativitasmu dalam mengolah sesuatu membuat orang lain kagum melihat "
              "hasil yang kamu ciptakan dari keterbatasan. Kamu juga fleksibel menyesuaikan cara demi "
              "mencapai hasil terbaik. Namun kebiasaan terus-menerus bereksperimen ini kadang membuat "
              "orang lain sulit menebak arah pastimu, karena kamu jarang berpegang pada satu metode "
              "saja. Kamu bisa terlalu sering mengganti pendekatan di tengah proses, sampai orang "
              "lain kesulitan mengikuti alur kerja yang kamu jalankan, atau merasa tidak yakin metode "
              "mana yang benar-benar akan kamu pakai sampai akhir.",
        "quote": "Eksperimen yang cerdik akan lebih bermakna kalau sesekali kamu berpegang teguh pada "
                 "satu arah yang jelas.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Pilih satu metode atau cara kerja, lalu jalani secara konsisten tanpa "
              "terus-menerus mengganti pendekatan di tengah jalan. Beri dirimu batas waktu tertentu "
              "untuk bertahan pada satu metode sebelum menilai apakah metode itu perlu diganti, "
              "supaya kecerdikanmu bereksperimen tetap terarah menuju hasil yang jelas.",
    },
    15: {
        "tagline": "✧ The Shadow",
        "chip": "MATRIX DESTINY",
        "title": "The Shadow — Sang Penjelajah Sisi Gelap Diri",
        "p1_label": "Siapa Kamu",
        "p1": "Susunan titik dari tanggal lahirmu membentuk arketipe The Shadow, sosok yang punya "
              "keberanian untuk menghadapi sisi gelap dalam dirinya sendiri, bukan menghindarinya. "
              "Kamu cenderung lebih jujur pada diri sendiri soal ketakutan, kekecewaan, atau luka "
              "yang mungkin dihindari kebanyakan orang. Kejujuran ini membuatmu punya pemahaman diri "
              "yang jauh lebih dalam, karena kamu tidak lari dari bagian-bagian dirimu yang terasa "
              "sulit diterima. Dalam hubungan dengan orang lain, kemampuan ini membuatmu bisa "
              "berempati secara mendalam terhadap orang yang sedang berjuang dengan sisi gelap "
              "mereka sendiri, karena kamu sudah lebih dulu mengenal perjuangan serupa dalam dirimu. "
              "Kamu juga cenderung tidak mudah terkejut dengan sisi kelam manusia, karena sudah "
              "terbiasa mengenalinya lewat proses refleksi dirimu sendiri.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kejujuranmu menghadapi sisi gelap diri sendiri membuatmu punya pemahaman diri yang "
              "lebih dalam dibanding kebanyakan orang. Kamu juga tidak mudah terkejut oleh sisi kelam "
              "manusia, karena sudah terbiasa mengenalinya dalam diri sendiri. Namun terlalu sering "
              "berfokus pada sisi gelap ini kadang membuatmu lupa mengapresiasi sisi baik yang juga "
              "ada dalam dirimu. Kebiasaan ini bisa membuatmu terjebak dalam pandangan yang terlalu "
              "keras terhadap diri sendiri, seolah kesalahan atau kekuranganmu lebih layak diperhatikan "
              "dibanding pencapaian dan kebaikan yang sudah kamu lakukan.",
        "quote": "Mengenal sisi gelap dirimu itu penting, tapi jangan sampai kamu lupa mengenal sisi "
                 "terangmu juga.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba tuliskan satu hal baik tentang dirimu setiap hari, sebagai imbangan "
              "dari kebiasaanmu merenungkan kekuranganmu. Latih diri untuk memberi perhatian yang "
              "sama besarnya pada sisi terangmu, seperti perhatian yang selama ini kamu berikan pada "
              "sisi gelapmu, supaya pemahaman dirimu terasa lebih utuh dan seimbang.",
    },
    16: {
        "tagline": "✧ The Collapse",
        "chip": "MATRIX DESTINY",
        "title": "The Collapse — Sang Penakluk Kehancuran",
        "p1_label": "Siapa Kamu",
        "p1": "Susunan titik dari tanggal lahirmu membentuk arketipe The Collapse, sosok yang punya "
              "kemampuan untuk bangkit setelah mengalami keruntuhan besar dalam hidupnya. Kamu "
              "cenderung mengalami masa-masa yang menghancurkan segala yang sudah kamu bangun, tapi "
              "justru dari situ kamu belajar membangun sesuatu yang jauh lebih kokoh. Pola hidup "
              "seperti ini sering membuatmu punya kedalaman dan kebijaksanaan yang tidak dimiliki "
              "orang yang belum pernah mengalami kehancuran serupa. Dalam pekerjaan atau kehidupan "
              "pribadi, ketangguhanmu bangkit dari titik nol membuat orang lain melihatmu sebagai "
              "sosok yang inspiratif, terutama bagi mereka yang sedang menghadapi masa-masa sulit "
              "serupa. Kamu juga cenderung tidak takut memulai ulang, karena kamu sudah membuktikan "
              "pada dirimu sendiri berkali-kali bahwa kamu bisa bangkit dari reruntuhan.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Ketangguhanmu bangkit dari kehancuran membuat orang lain kagum dengan daya juangmu. "
              "Kamu juga tidak takut memulai ulang dari reruntuhan. Namun pola hidup yang berulang "
              "kali runtuh dan bangkit ini kadang membuatmu lelah, dan sesekali kamu perlu belajar "
              "mencegah keruntuhan itu terjadi lagi, bukan hanya jago bangkit darinya. Kamu bisa "
              "terjebak dalam siklus yang sama berulang kali, tanpa benar-benar berhenti sejenak "
              "untuk mengevaluasi pola apa yang selalu membawamu ke titik kehancuran itu.",
        "quote": "Bangkit dari kehancuran itu kekuatan besar, tapi belajar mencegahnya terulang juga "
                 "bagian dari kebijaksanaan.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba kenali satu pola yang selama ini berulang kali membuatmu jatuh, dan "
              "pikirkan satu langkah kecil untuk mencegahnya terulang. Tuliskan pola itu secara "
              "jujur, dan diskusikan dengan orang yang kamu percaya untuk mendapat perspektif baru "
              "tentang bagaimana cara mencegahnya, bukan sekadar cara bangkit setelahnya.",
    },
    17: {
        "tagline": "✧ The Hope",
        "chip": "MATRIX DESTINY",
        "title": "The Hope — Sang Pembawa Harapan",
        "p1_label": "Siapa Kamu",
        "p1": "Susunan titik dari tanggal lahirmu membentuk arketipe The Hope, sosok yang secara "
              "alami membawa optimisme dan keyakinan bahwa keadaan akan membaik. Kamu jarang "
              "kehilangan harapan sepenuhnya, bahkan di saat-saat yang terasa gelap bagi orang lain "
              "di sekitarmu. Sifat ini membuatmu sering jadi sumber semangat bagi orang-orang yang "
              "sedang berjuang, karena mereka bisa merasakan keyakinanmu bahwa segala sesuatu akan "
              "membaik, meski situasinya belum menunjukkan tanda-tanda itu. Dalam pekerjaan, "
              "optimismemu membuatmu cocok mengisi peran yang membutuhkan semangat memotivasi tim, "
              "terutama di masa-masa sulit ketika moral orang lain sedang turun. Dalam kehidupan "
              "pribadi, kamu adalah sosok yang orang cari saat mereka butuh diyakinkan bahwa masih "
              "ada jalan keluar dari masalah yang sedang mereka hadapi.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Optimismemu membuat orang lain merasa lebih ringan menghadapi masalah ketika berada di "
              "dekatmu. Kamu juga jarang menyerah meski keadaan tampak sulit. Namun harapan yang "
              "terlalu besar ini kadang membuatmu mengabaikan kenyataan yang sebenarnya butuh "
              "perhatian serius, bukan sekadar dilihat dari sisi positifnya saja. Kamu bisa terlalu "
              "cepat melompat ke \"pasti akan baik-baik saja\" tanpa benar-benar mengakui betapa "
              "beratnya sebuah masalah, sehingga orang lain merasa perasaan sulit mereka tidak "
              "sepenuhnya divalidasi.",
        "quote": "Harapan yang sehat tetap perlu berpijak pada kenyataan yang ada.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Ketika menghadapi masalah, coba akui dulu bagian yang sulit secara jujur, "
              "sebelum mencari sisi positif dari keadaan tersebut. Latih diri untuk mengatakan "
              "\"ini memang berat\" terlebih dulu sebelum menawarkan harapan, supaya orang lain "
              "merasa perasaannya benar-benar didengar, bukan langsung dialihkan ke sisi positif.",
    },
    18: {
        "tagline": "✧ The Mystery",
        "chip": "MATRIX DESTINY",
        "title": "The Mystery — Sang Penjaga Rahasia",
        "p1_label": "Siapa Kamu",
        "p1": "Susunan titik dari tanggal lahirmu membentuk arketipe The Mystery, sosok yang punya "
              "sisi tersembunyi dan sulit ditebak sepenuhnya oleh orang lain. Kamu cenderung menjaga "
              "banyak hal untuk dirimu sendiri, dan hanya membiarkan segelintir orang benar-benar "
              "mengenal dirimu yang sesungguhnya. Sikap ini bukan karena kamu tidak percaya pada "
              "orang lain, tapi karena kamu memang lebih nyaman membagikan dirimu secara bertahap, "
              "bukan sekaligus. Dalam pergaulan, aura misterius ini membuat orang lain penasaran dan "
              "tertarik untuk lebih mengenalmu, karena kamu terasa berbeda dari orang-orang yang "
              "terlalu terbuka sejak awal. Dalam pekerjaan, kemampuan menjaga privasi ini membuatmu "
              "cocok di peran yang membutuhkan kerahasiaan atau kehati-hatian dalam menyampaikan "
              "informasi.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kemampuanmu menjaga privasi membuat orang lain penasaran dan tertarik untuk lebih "
              "mengenalmu. Kamu juga jarang mudah ditebak, sehingga terasa menarik bagi orang di "
              "sekitarmu. Namun kebiasaan menutup diri ini kadang membuat orang-orang terdekat "
              "merasa sulit benar-benar dekat denganmu, meski mereka sudah berusaha keras. Sikap "
              "ini bisa membuat hubungan yang seharusnya bisa lebih dalam justru berhenti di "
              "permukaan, karena orang lain tidak pernah benar-benar tahu apa yang sedang terjadi "
              "dalam pikiran atau hatimu.",
        "quote": "Menjaga misteri itu menarik, tapi keintiman sejati butuh sedikit keterbukaan juga.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba bagikan satu hal pribadi yang biasanya kamu simpan sendiri kepada orang yang "
              "kamu percaya. Mulailah dari hal yang terasa aman untuk dibagikan, dan perhatikan "
              "bagaimana keterbukaan kecil itu justru bisa mempererat hubungan, bukan membuatmu "
              "kehilangan kendali atas privasimu.",
    },
    19: {
        "tagline": "✧ The Joy",
        "chip": "MATRIX DESTINY",
        "title": "The Joy — Sang Pembawa Kebahagiaan",
        "p1_label": "Siapa Kamu",
        "p1": "Susunan titik dari tanggal lahirmu membentuk arketipe The Joy, sosok yang membawa "
              "keceriaan dan energi positif ke mana pun kamu pergi. Kamu punya kemampuan menemukan "
              "hal-hal kecil yang patut disyukuri, bahkan di tengah situasi yang sebenarnya cukup "
              "berat. Kemampuan ini membuatmu jadi sosok yang dicari orang lain saat mereka butuh "
              "suasana yang lebih ringan, karena kehadiranmu punya cara membuat beban terasa tidak "
              "seberat sebelumnya. Dalam pekerjaan, energi positifmu bisa mencairkan suasana yang "
              "tegang dan membuat tim tetap bersemangat meski sedang menghadapi tekanan. Dalam "
              "pertemanan, kamu sering jadi sosok yang paling diingat karena berhasil membuat momen "
              "yang biasa saja terasa lebih menyenangkan.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Keceriaan dan energi positifmu membuat suasana di sekitarmu terasa lebih ringan dan "
              "menyenangkan. Kamu juga mudah membuat orang lain tersenyum. Namun kebiasaan selalu "
              "ingin terlihat ceria ini kadang membuatmu menyembunyikan kesedihanmu sendiri, bahkan "
              "dari orang-orang terdekat yang sebenarnya ingin membantumu. Kamu bisa terjebak dalam "
              "peran sebagai \"yang selalu bahagia\", sampai orang lain lupa bertanya bagaimana "
              "perasaanmu yang sesungguhnya, dan kamu sendiri jadi enggan menunjukkan sisi rapuhmu.",
        "quote": "Membawa kebahagiaan bagi orang lain itu indah, tapi kesedihanmu sendiri juga "
                 "berhak diakui.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Ketika sedang tidak baik-baik saja, coba akui itu secara terbuka kepada "
              "orang terdekat, alih-alih menutupinya dengan senyuman seperti biasa. Latih diri "
              "untuk membiarkan orang lain melihat sisi rapuhmu sesekali, karena itu justru akan "
              "membuat kebahagiaan yang kamu bagikan terasa lebih tulus dan manusiawi.",
    },
    20: {
        "tagline": "✧ The Awakening",
        "chip": "MATRIX DESTINY",
        "title": "The Awakening — Sang Pencari Kesadaran",
        "p1_label": "Siapa Kamu",
        "p1": "Susunan titik dari tanggal lahirmu membentuk arketipe The Awakening, sosok yang sering "
              "mengalami momen-momen penyadaran besar yang mengubah cara pandangnya terhadap hidup. "
              "Kamu terus bertumbuh melalui proses mempertanyakan dan memahami ulang keyakinan yang "
              "selama ini kamu pegang. Kamu jarang merasa puas hanya berhenti pada satu pemahaman, "
              "dan selalu terbuka pada kemungkinan bahwa cara pandangmu bisa berkembang lebih jauh "
              "lagi. Dalam kehidupan pribadi, sifat ini membuatmu terus mengalami perubahan cara "
              "pandang seiring bertambahnya pengalaman, dan kamu tidak takut mengakui ketika "
              "keyakinan lamamu ternyata perlu diperbarui. Orang-orang di sekitarmu sering melihatmu "
              "sebagai sosok yang terus berkembang, jarang stagnan pada satu pola pikir dalam waktu "
              "yang terlalu lama.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Keterbukaanmu untuk terus belajar dan berubah membuatmu berkembang lebih jauh "
              "dibanding banyak orang yang enggan mempertanyakan keyakinan lamanya. Kamu juga berani "
              "mengakui ketika kamu salah. Namun proses penyadaran yang terus-menerus ini kadang "
              "membuatmu belum sempat menikmati stabilitas dari satu tahap sebelum berpindah ke "
              "tahap penyadaran berikutnya. Kamu bisa terus merasa \"belum sampai\" pada pemahaman "
              "yang benar-benar final, sampai lupa menghargai seberapa jauh perjalanan yang sudah "
              "kamu tempuh.",
        "quote": "Terus berkembang itu baik, tapi sesekali berhenti sejenak untuk menikmati apa yang "
                 "sudah kamu pahami juga penting.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba berhenti sejenak dari mencari pemahaman baru, dan syukuri apa yang "
              "sudah kamu sadari sejauh ini. Tuliskan tiga hal penting yang sudah kamu pelajari "
              "tentang dirimu sendiri selama setahun terakhir, dan luangkan waktu untuk benar-benar "
              "menghargai perjalanan itu sebelum melangkah mencari pemahaman berikutnya.",
    },
    21: {
        "tagline": "✧ The Achievement",
        "chip": "MATRIX DESTINY",
        "title": "The Achievement — Sang Pencapai Tujuan",
        "p1_label": "Siapa Kamu",
        "p1": "Susunan titik dari tanggal lahirmu membentuk arketipe The Achievement, sosok yang "
              "punya dorongan kuat untuk mencapai tujuan-tujuan besar dalam hidupnya. Kamu jarang "
              "puas hanya berada di tempat yang sama, dan selalu punya target baru yang ingin kamu "
              "kejar setelah target sebelumnya tercapai. Dorongan ini membuatmu terus bergerak maju, "
              "bahkan ketika orang lain merasa sudah cukup dengan pencapaian yang ada. Dalam "
              "pekerjaan, ambisi ini membuatmu unggul di lingkungan yang kompetitif dan penuh "
              "tantangan, karena kamu selalu terdorong untuk melampaui standar yang sudah ada. Orang-"
              "orang di sekitarmu sering kagum melihat betapa banyak yang sudah kamu capai, meski "
              "kamu sendiri kadang merasa itu belum cukup.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Ambisi dan kerja kerasmu membuatmu sering mencapai hal-hal yang orang lain anggap "
              "sulit. Kamu juga disiplin dalam mengejar apa yang kamu inginkan. Namun dorongan untuk "
              "terus mencapai lebih banyak ini kadang membuatmu sulit merasa puas, sampai lupa "
              "menikmati pencapaian yang sudah ada di depan mata. Kebiasaan ini bisa membuatmu "
              "merasa selalu kurang, meski dari luar kamu terlihat sangat sukses. Kamu juga bisa "
              "mengorbankan waktu istirahat dan hubungan personal demi terus mengejar target "
              "berikutnya.",
        "quote": "Pencapaian besar akan terasa lebih bermakna kalau kamu sempat berhenti sejenak "
                 "untuk merayakannya.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba rayakan satu pencapaian yang sudah kamu raih, sekecil apa pun itu, "
              "sebelum langsung mengejar target berikutnya. Luangkan waktu khusus untuk benar-benar "
              "menikmati hasil kerja kerasmu, entah dengan merayakannya bersama orang terdekat atau "
              "sekadar memberi dirimu jeda sebelum kembali mengejar target baru.",
    },
    22: {
        "tagline": "✧ The Unity",
        "chip": "MATRIX DESTINY",
        "title": "The Unity — Sang Penyatu yang Utuh",
        "p1_label": "Siapa Kamu",
        "p1": "Susunan titik dari tanggal lahirmu membentuk arketipe The Unity, arketipe terakhir "
              "dalam Matrix Destiny yang melambangkan keutuhan dan penyatuan dari segala pengalaman "
              "hidup. Kamu punya kemampuan melihat gambaran besar dan menyatukan hal-hal yang tampak "
              "terpisah menjadi satu kesatuan yang bermakna. Kemampuan ini membuatmu bisa melihat "
              "keterhubungan antara pengalaman-pengalaman yang berbeda dalam hidupmu, dan memahami "
              "bagaimana semuanya membentuk siapa dirimu sekarang. Dalam pekerjaan, kamu cocok "
              "mengisi peran yang membutuhkan pemikiran strategis jangka panjang, karena kamu bisa "
              "melihat bagaimana berbagai bagian kecil saling berhubungan menuju tujuan yang lebih "
              "besar. Dalam kehidupan pribadi, kamu cenderung bijaksana dalam menyikapi kontradiksi, "
              "karena kamu memahami bahwa hidup jarang hitam putih.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kemampuanmu melihat keterhubungan antar berbagai hal membuatmu bijaksana dalam "
              "memandang hidup secara utuh, tidak terpaku pada satu bagian saja. Kamu juga bisa "
              "menerima kontradiksi sebagai bagian yang wajar dari kehidupan. Namun cara pandang yang "
              "begitu luas ini kadang membuatmu kesulitan fokus pada hal-hal kecil dan spesifik yang "
              "sebenarnya juga butuh perhatianmu sekarang. Kamu bisa terlalu sibuk memikirkan gambaran "
              "besar, sampai detail-detail penting di depan mata jadi terabaikan begitu saja.",
        "quote": "Melihat gambaran besar itu bijaksana, tapi jangan sampai membuatmu melewatkan "
                 "detail kecil yang ada di depan mata.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba fokus menyelesaikan satu hal kecil dan spesifik sampai tuntas, tanpa "
              "langsung memikirkan bagaimana hal itu berhubungan dengan gambaran besar hidupmu. "
              "Latih diri untuk memberi perhatian penuh pada tugas kecil yang ada di depanmu saat "
              "ini juga, sebagai imbangan dari kebiasaanmu selalu berpikir jangka panjang dan luas.",
    },
}
