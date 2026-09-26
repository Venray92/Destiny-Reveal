"""
Konten Matrix Destiny — Titik Inti / Arketipe Utama (22 kategori).

Key dict ini adalah INTEGER 1-22, HARUS sama persis dengan nilai
"titik_inti" dari engine/matrix_destiny.py (hitung_matrix_destiny()).
nama_arketipe Inggris (mis. "The Partners") cocok dengan
engine.matrix_destiny.NAMA_ARKETIPE dan nama file assets/cards/matrix_destiny/.

CATATAN SCOPE (sama seperti di engine/matrix_destiny.py): ini hanya
TITIK INTI (1 dari 8 titik octagon Matrix Destiny). 7 titik lain belum
diimplementasikan.

Struktur tiap entri sama persis dengan DUMMY_RESULTS di views/revealpage.py.
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
              "adalah kesempatan baru untuk membuktikan diri.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Semangat dan keberanianmu memulai sesuatu membuat orang lain sering terinspirasi untuk "
              "berhenti menunda dan segera bertindak. Kamu juga jarang terbebani rasa takut gagal "
              "sebelum benar-benar mencoba. Namun energi awal yang begitu besar ini kadang tidak "
              "dibarengi kesabaran untuk menyelesaikan sesuatu sampai tuntas.",
        "quote": "Keberanian memulai akan terasa lebih bermakna kalau disertai niat untuk benar-"
                 "benar menyelesaikannya.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Pilih satu hal yang baru saja kamu mulai, lalu berkomitmenlah menyelesaikan tahap "
              "pertamanya secara penuh sebelum memulai hal baru yang lain minggu ini.",
    },
    2: {
        "tagline": "✧ The Listener",
        "chip": "MATRIX DESTINY",
        "title": "The Listener — Sang Pendengar yang Penuh Empati",
        "p1_label": "Siapa Kamu",
        "p1": "Susunan titik dari tanggal lahirmu membentuk arketipe The Listener, sosok yang secara "
              "alami punya kemampuan mendengarkan dengan sepenuh hati. Orang-orang merasa nyaman "
              "bercerita kepadamu, karena kamu jarang buru-buru menghakimi atau memotong pembicaraan "
              "sebelum mereka selesai bicara.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kemampuanmu mendengarkan membuat orang lain merasa benar-benar dipahami saat "
              "bersamamu. Kamu juga peka menangkap hal-hal yang tidak terucap secara langsung. Namun "
              "karena terlalu fokus mendengarkan orang lain, kamu kadang lupa menyuarakan apa yang "
              "sebenarnya kamu rasakan atau butuhkan.",
        "quote": "Mendengarkan orang lain itu berharga, tapi suaramu sendiri juga layak untuk "
                 "didengar.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Minggu ini, coba ceritakan satu hal yang sedang kamu rasakan kepada orang terdekat, "
              "alih-alih hanya menjadi pendengar seperti biasanya.",
    },
    3: {
        "tagline": "✧ The Creator",
        "chip": "MATRIX DESTINY",
        "title": "The Creator — Sang Pencipta yang Penuh Imajinasi",
        "p1_label": "Siapa Kamu",
        "p1": "Susunan titik dari tanggal lahirmu membentuk arketipe The Creator, sosok yang punya "
              "imajinasi kaya dan dorongan kuat untuk menciptakan sesuatu yang belum pernah ada "
              "sebelumnya. Kamu melihat dunia dengan cara yang berbeda, dan sering menemukan "
              "kemungkinan-kemungkinan baru dari hal-hal yang tampak biasa.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kreativitas dan orisinalitasmu membuat karya atau ide-idemu terasa segar dan berbeda "
              "dari kebanyakan orang. Kamu juga tidak takut mengambil pendekatan yang tidak biasa. "
              "Namun terlalu banyak ide yang muncul sekaligus kadang membuatmu kesulitan memilih mana "
              "yang benar-benar layak untuk diwujudkan sampai selesai.",
        "quote": "Imajinasi yang luas akan lebih bermakna kalau satu idenya benar-benar diwujudkan "
                 "sampai tuntas.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Pilih satu ide yang paling ingin kamu wujudkan minggu ini, lalu curahkan perhatianmu "
              "sepenuhnya di situ tanpa tergoda memikirkan ide lain.",
    },
    4: {
        "tagline": "✧ The Ruler",
        "chip": "MATRIX DESTINY",
        "title": "The Ruler — Sang Penguasa yang Tegas",
        "p1_label": "Siapa Kamu",
        "p1": "Susunan titik dari tanggal lahirmu membentuk arketipe The Ruler, sosok yang punya "
              "wibawa alami dan kemampuan mengambil keputusan dengan tegas. Orang-orang di sekitarmu "
              "sering melihatmu sebagai sosok yang bisa diandalkan untuk memimpin, karena kamu jarang "
              "ragu-ragu saat harus bertindak.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Ketegasan dan kemampuan memimpinmu membuat orang lain percaya pada arah yang kamu "
              "tentukan. Kamu juga bertanggung jawab penuh atas keputusan yang kamu ambil. Namun "
              "ketegasan ini kadang terlihat kaku di mata orang lain, sehingga mereka sungkan "
              "menyampaikan pendapat yang berbeda darimu.",
        "quote": "Kepemimpinan yang kuat juga membuka ruang bagi orang lain untuk berpendapat "
                 "berbeda.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Minggu ini, coba tanyakan secara terbuka pendapat orang lain sebelum mengambil "
              "keputusan, dan tunjukkan bahwa pendapat berbeda darimu tetap diterima dengan baik.",
    },
    5: {
        "tagline": "✧ The Teacher",
        "chip": "MATRIX DESTINY",
        "title": "The Teacher — Sang Guru yang Suka Berbagi Ilmu",
        "p1_label": "Siapa Kamu",
        "p1": "Susunan titik dari tanggal lahirmu membentuk arketipe The Teacher, sosok yang senang "
              "berbagi ilmu dan membantu orang lain memahami sesuatu dengan lebih baik. Kamu punya "
              "kesabaran untuk menjelaskan hal-hal yang rumit menjadi lebih sederhana, dan merasa "
              "puas ketika melihat orang lain berkembang berkat bantuanmu.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kesabaran dan kemampuanmu menjelaskan sesuatu membuat orang lain merasa terbantu dan "
              "dihargai prosesnya, bukan hanya dinilai dari hasil akhir. Kamu juga senang melihat "
              "orang lain sukses. Namun kebiasaan selalu ingin membantu ini kadang membuatmu lupa "
              "untuk terus belajar dan berkembang untuk dirimu sendiri.",
        "quote": "Mengajar orang lain akan lebih bermakna kalau kamu juga terus memberi ruang untuk "
                 "belajar bagi dirimu sendiri.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Minggu ini, luangkan waktu untuk mempelajari sesuatu yang baru untuk dirimu sendiri, "
              "bukan untuk diajarkan kepada orang lain.",
    },
    6: {
        "tagline": "✧ The Partners",
        "chip": "MATRIX DESTINY",
        "title": "The Partners — Fondasi bagi Orang-Orang di Sekitarmu",
        "p1_label": "Siapa Kamu",
        "p1": "Dalam pembacaan Matrix Destiny, susunan titik dari tanggal lahirmu membentuk arketipe "
              "The Partners, sosok yang secara alami jadi tempat bersandar bagi keluarga maupun "
              "teman dekat. Kehadiranmu memberi rasa aman, bahkan tanpa kamu perlu berkata banyak.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kesetiaanmu pada orang-orang terdekat jarang tergoyahkan, dan itu membuatmu jadi sosok "
              "yang bisa diandalkan dalam situasi sulit sekalipun. Namun karena terbiasa menjaga "
              "orang lain, kamu kadang lupa bahwa dirimu sendiri juga butuh dijaga oleh seseorang.",
        "quote": "The Partners sejati juga tahu kapan waktunya untuk diam-diam dijaga balik.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Izinkan satu orang terdekatmu untuk benar-benar membantumu minggu ini, tanpa buru-buru "
              "menolak dengan alasan bahwa kamu bisa mengurus semuanya sendiri.",
    },
    7: {
        "tagline": "✧ The Conqueror",
        "chip": "MATRIX DESTINY",
        "title": "The Conqueror — Sang Penakluk yang Pantang Menyerah",
        "p1_label": "Siapa Kamu",
        "p1": "Susunan titik dari tanggal lahirmu membentuk arketipe The Conqueror, sosok yang punya "
              "tekad kuat untuk menaklukkan tantangan apa pun yang ada di depannya. Kamu jarang "
              "berhenti hanya karena satu kegagalan, dan justru menjadikan hambatan sebagai bahan "
              "bakar untuk semakin gigih berusaha.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Ketekunan dan daya juangmu membuat orang lain kagum melihat caramu bangkit dari "
              "kegagalan. Kamu juga jarang mudah menyerah pada keadaan. Namun fokus yang terlalu "
              "besar pada 'menaklukkan' ini kadang membuatmu memandang segala sesuatu sebagai "
              "kompetisi, bahkan pada situasi yang sebenarnya tidak perlu diperlakukan seperti itu.",
        "quote": "Tidak semua hal dalam hidup perlu ditaklukkan, sebagian cukup dinikmati apa "
                 "adanya.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Minggu ini, coba nikmati satu aktivitas tanpa menjadikannya ajang untuk bersaing atau "
              "membuktikan sesuatu kepada siapa pun.",
    },
    8: {
        "tagline": "✧ The Balance",
        "chip": "MATRIX DESTINY",
        "title": "The Balance — Sang Penjaga Keseimbangan",
        "p1_label": "Siapa Kamu",
        "p1": "Susunan titik dari tanggal lahirmu membentuk arketipe The Balance, sosok yang secara "
              "alami mencari keseimbangan dalam segala aspek hidupnya. Kamu tidak suka pergi ke "
              "ekstrem yang berlebihan, dan selalu berusaha menimbang berbagai sisi sebelum mengambil "
              "keputusan.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kemampuanmu menjaga keseimbangan membuatmu jarang terjebak dalam keputusan yang "
              "gegabah. Kamu juga adil dalam memandang berbagai sudut pandang. Namun terlalu fokus "
              "menjaga keseimbangan ini kadang membuatmu ragu-ragu memilih sisi, bahkan ketika "
              "situasinya sebenarnya membutuhkan sikap yang lebih tegas.",
        "quote": "Keseimbangan yang sehat kadang juga berarti berani memilih satu sisi dengan "
                 "mantap.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Ketika dihadapkan pada satu pilihan minggu ini, coba ambil sikap yang tegas, alih-alih "
              "terus mencari jalan tengah yang menyenangkan semua pihak.",
    },
    9: {
        "tagline": "✧ The Hermit",
        "chip": "MATRIX DESTINY",
        "title": "The Hermit — Sang Perenung yang Mandiri",
        "p1_label": "Siapa Kamu",
        "p1": "Susunan titik dari tanggal lahirmu membentuk arketipe The Hermit, sosok yang menemukan "
              "kekuatan besar dalam kesendirian dan perenungan. Kamu tidak selalu butuh keramaian "
              "untuk merasa utuh, dan justru sering menemukan kejernihan pikiran ketika sedang "
              "sendirian.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kemandirian dan kedalaman berpikirmu membuatmu jarang bergantung pada validasi orang "
              "lain untuk merasa yakin. Kamu juga bisa menemukan jawaban dari dalam dirimu sendiri. "
              "Namun kecenderungan menyendiri ini kadang membuatmu menjauh dari orang lain, bahkan "
              "pada saat kamu sebenarnya butuh dukungan mereka.",
        "quote": "Kesendirian itu berharga, tapi jangan sampai membuatmu menutup pintu bagi orang "
                 "yang ingin membantumu.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Minggu ini, coba hubungi satu orang yang sudah lama tidak kamu ajak bicara, dan "
              "biarkan dirimu terbuka pada kehadiran mereka.",
    },
    10: {
        "tagline": "✧ The Wheel",
        "chip": "MATRIX DESTINY",
        "title": "The Wheel — Sang Pembawa Perubahan",
        "p1_label": "Siapa Kamu",
        "p1": "Susunan titik dari tanggal lahirmu membentuk arketipe The Wheel, sosok yang erat "
              "kaitannya dengan siklus, perubahan, dan pergerakan hidup yang terus berputar. Kamu "
              "cenderung menerima bahwa hidup punya masa naik dan masa turun, dan jarang terlalu "
              "lama terpuruk saat menghadapi masa sulit.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Penerimaanmu terhadap perubahan membuatmu lebih tangguh menghadapi naik turunnya "
              "hidup dibanding kebanyakan orang. Kamu juga cepat bangkit setelah mengalami kemunduran. "
              "Namun kebiasaan menerima perubahan secara pasif ini kadang membuatmu kurang berusaha "
              "mengendalikan arah hidupmu sendiri, dan lebih memilih pasrah pada keadaan.",
        "quote": "Menerima perubahan itu baik, tapi kamu juga punya kendali untuk mengarahkan roda "
                 "itu berputar ke arah yang kamu inginkan.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Minggu ini, coba ambil satu langkah aktif untuk mengarahkan sesuatu yang selama ini "
              "hanya kamu terima begitu saja sebagai keadaan yang tak bisa diubah.",
    },
    11: {
        "tagline": "✧ The Brave",
        "chip": "MATRIX DESTINY",
        "title": "The Brave — Sang Pemberani yang Tangguh",
        "p1_label": "Siapa Kamu",
        "p1": "Susunan titik dari tanggal lahirmu membentuk arketipe The Brave, sosok yang punya "
              "keberanian menghadapi ketakutan alih-alih menghindarinya. Kamu jarang lari dari "
              "situasi sulit, dan justru sering maju lebih dulu ketika orang lain masih ragu-ragu "
              "untuk bertindak.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Keberanianmu menghadapi hal-hal sulit membuat orang lain merasa lebih tenang berada "
              "di sekitarmu saat krisis. Kamu juga jarang membiarkan rasa takut menghalangi "
              "langkahmu. Namun keberanian yang besar ini kadang membuatmu meremehkan risiko, atau "
              "lupa meminta bantuan saat situasi sebenarnya sudah di luar kendalimu sendiri.",
        "quote": "Keberanian sejati juga tahu kapan saatnya meminta bantuan, bukan menghadapi "
                 "semuanya sendirian.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Ketika menghadapi tantangan besar minggu ini, coba minta pendapat atau bantuan dari "
              "orang lain terlebih dulu, sebelum memutuskan untuk menghadapinya sendirian.",
    },
    12: {
        "tagline": "✧ The Sacrifice",
        "chip": "MATRIX DESTINY",
        "title": "The Sacrifice — Sang Pemberi yang Rela Berkorban",
        "p1_label": "Siapa Kamu",
        "p1": "Susunan titik dari tanggal lahirmu membentuk arketipe The Sacrifice, sosok yang punya "
              "kerelaan besar untuk mengorbankan kepentingannya demi kebaikan orang lain. Kamu "
              "cenderung memikirkan dampak tindakanmu terhadap orang lain terlebih dulu, bahkan "
              "sebelum memikirkan dirimu sendiri.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kerelaan berkorbanmu membuat orang-orang terdekat merasa sangat dicintai dan "
              "diutamakan. Kamu juga jarang mengharapkan balasan atas kebaikan yang kamu berikan. "
              "Namun kebiasaan mengorbankan diri ini kadang berjalan terlalu jauh, sampai kamu "
              "kehilangan bagian dari dirimu sendiri demi kepentingan orang lain.",
        "quote": "Berkorban untuk orang lain itu mulia, tapi dirimu sendiri juga berhak diperjuangkan "
                 "dengan cara yang sama.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Minggu ini, coba tolak satu permintaan yang sebenarnya memberatkanmu, dan utamakan "
              "kebutuhanmu sendiri untuk sekali itu.",
    },
    13: {
        "tagline": "✧ The Transformation",
        "chip": "MATRIX DESTINY",
        "title": "The Transformation — Sang Pembawa Perubahan Besar",
        "p1_label": "Siapa Kamu",
        "p1": "Susunan titik dari tanggal lahirmu membentuk arketipe The Transformation, sosok yang "
              "sering mengalami perubahan besar dalam hidupnya dan keluar sebagai versi diri yang "
              "lebih kuat setiap kalinya. Kamu tidak takut meninggalkan sesuatu yang sudah tidak "
              "sesuai lagi denganmu, meski itu berarti harus memulai babak baru dari awal.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kemampuanmu bertransformasi membuatmu jarang terjebak dalam keadaan yang sudah tidak "
              "membawa kebaikan bagimu. Kamu juga tangguh menghadapi masa-masa peralihan yang berat. "
              "Namun perubahan besar yang terlalu sering ini kadang membuat orang di sekitarmu "
              "kesulitan mengikuti arah hidupmu yang terus bergeser.",
        "quote": "Bertransformasi itu kekuatan, tapi memberi waktu bagi orang lain untuk mengikutimu "
                 "juga bagian dari kebaikan.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Sebelum membuat perubahan besar minggu ini, coba ceritakan dulu rencanamu kepada orang "
              "terdekat, supaya mereka tidak merasa tertinggal begitu saja.",
    },
    14: {
        "tagline": "✧ The Alchemist",
        "chip": "MATRIX DESTINY",
        "title": "The Alchemist — Sang Peramu yang Cerdik",
        "p1_label": "Siapa Kamu",
        "p1": "Susunan titik dari tanggal lahirmu membentuk arketipe The Alchemist, sosok yang punya "
              "kemampuan meramu berbagai hal yang tampaknya tidak berhubungan menjadi sesuatu yang "
              "baru dan bernilai. Kamu pandai melihat potensi tersembunyi dalam situasi maupun "
              "sumber daya yang terbatas.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kecerdikan dan kreativitasmu dalam mengolah sesuatu membuat orang lain kagum melihat "
              "hasil yang kamu ciptakan dari keterbatasan. Kamu juga fleksibel menyesuaikan cara demi "
              "mencapai hasil terbaik. Namun kebiasaan terus-menerus bereksperimen ini kadang membuat "
              "orang lain sulit menebak arah pastimu, karena kamu jarang berpegang pada satu metode "
              "saja.",
        "quote": "Eksperimen yang cerdik akan lebih bermakna kalau sesekali kamu berpegang teguh pada "
                 "satu arah yang jelas.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Pilih satu metode atau cara kerja minggu ini, lalu jalani secara konsisten tanpa "
              "terus-menerus mengganti pendekatan di tengah jalan.",
    },
    15: {
        "tagline": "✧ The Shadow",
        "chip": "MATRIX DESTINY",
        "title": "The Shadow — Sang Penjelajah Sisi Gelap Diri",
        "p1_label": "Siapa Kamu",
        "p1": "Susunan titik dari tanggal lahirmu membentuk arketipe The Shadow, sosok yang punya "
              "keberanian untuk menghadapi sisi gelap dalam dirinya sendiri, bukan menghindarinya. "
              "Kamu cenderung lebih jujur pada diri sendiri soal ketakutan, kekecewaan, atau luka "
              "yang mungkin dihindari kebanyakan orang.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kejujuranmu menghadapi sisi gelap diri sendiri membuatmu punya pemahaman diri yang "
              "lebih dalam dibanding kebanyakan orang. Kamu juga tidak mudah terkejut oleh sisi kelam "
              "manusia, karena sudah terbiasa mengenalinya dalam diri sendiri. Namun terlalu sering "
              "berfokus pada sisi gelap ini kadang membuatmu lupa mengapresiasi sisi baik yang juga "
              "ada dalam dirimu.",
        "quote": "Mengenal sisi gelap dirimu itu penting, tapi jangan sampai kamu lupa mengenal sisi "
                 "terangmu juga.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Minggu ini, coba tuliskan satu hal baik tentang dirimu setiap hari, sebagai imbangan "
              "dari kebiasaanmu merenungkan kekuranganmu.",
    },
    16: {
        "tagline": "✧ The Collapse",
        "chip": "MATRIX DESTINY",
        "title": "The Collapse — Sang Penakluk Kehancuran",
        "p1_label": "Siapa Kamu",
        "p1": "Susunan titik dari tanggal lahirmu membentuk arketipe The Collapse, sosok yang punya "
              "kemampuan untuk bangkit setelah mengalami keruntuhan besar dalam hidupnya. Kamu "
              "cenderung mengalami masa-masa yang menghancurkan segala yang sudah kamu bangun, tapi "
              "justru dari situ kamu belajar membangun sesuatu yang jauh lebih kokoh.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Ketangguhanmu bangkit dari kehancuran membuat orang lain kagum dengan daya juangmu. "
              "Kamu juga tidak takut memulai ulang dari reruntuhan. Namun pola hidup yang berulang "
              "kali runtuh dan bangkit ini kadang membuatmu lelah, dan sesekali kamu perlu belajar "
              "mencegah keruntuhan itu terjadi lagi, bukan hanya jago bangkit darinya.",
        "quote": "Bangkit dari kehancuran itu kekuatan besar, tapi belajar mencegahnya terulang juga "
                 "bagian dari kebijaksanaan.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Minggu ini, coba kenali satu pola yang selama ini berulang kali membuatmu jatuh, dan "
              "pikirkan satu langkah kecil untuk mencegahnya terulang.",
    },
    17: {
        "tagline": "✧ The Hope",
        "chip": "MATRIX DESTINY",
        "title": "The Hope — Sang Pembawa Harapan",
        "p1_label": "Siapa Kamu",
        "p1": "Susunan titik dari tanggal lahirmu membentuk arketipe The Hope, sosok yang secara "
              "alami membawa optimisme dan keyakinan bahwa keadaan akan membaik. Kamu jarang "
              "kehilangan harapan sepenuhnya, bahkan di saat-saat yang terasa gelap bagi orang lain "
              "di sekitarmu.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Optimismemu membuat orang lain merasa lebih ringan menghadapi masalah ketika berada di "
              "dekatmu. Kamu juga jarang menyerah meski keadaan tampak sulit. Namun harapan yang "
              "terlalu besar ini kadang membuatmu mengabaikan kenyataan yang sebenarnya butuh "
              "perhatian serius, bukan sekadar dilihat dari sisi positifnya saja.",
        "quote": "Harapan yang sehat tetap perlu berpijak pada kenyataan yang ada.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Ketika menghadapi masalah minggu ini, coba akui dulu bagian yang sulit secara jujur, "
              "sebelum mencari sisi positif dari keadaan tersebut.",
    },
    18: {
        "tagline": "✧ The Mystery",
        "chip": "MATRIX DESTINY",
        "title": "The Mystery — Sang Penjaga Rahasia",
        "p1_label": "Siapa Kamu",
        "p1": "Susunan titik dari tanggal lahirmu membentuk arketipe The Mystery, sosok yang punya "
              "sisi tersembunyi dan sulit ditebak sepenuhnya oleh orang lain. Kamu cenderung menjaga "
              "banyak hal untuk dirimu sendiri, dan hanya membiarkan segelintir orang benar-benar "
              "mengenal dirimu yang sesungguhnya.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kemampuanmu menjaga privasi membuat orang lain penasaran dan tertarik untuk lebih "
              "mengenalmu. Kamu juga jarang mudah ditebak, sehingga terasa menarik bagi orang di "
              "sekitarmu. Namun kebiasaan menutup diri ini kadang membuat orang-orang terdekat "
              "merasa sulit benar-benar dekat denganmu, meski mereka sudah berusaha keras.",
        "quote": "Menjaga misteri itu menarik, tapi keintiman sejati butuh sedikit keterbukaan juga.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba bagikan satu hal pribadi yang biasanya kamu simpan sendiri kepada orang yang "
              "kamu percaya minggu ini.",
    },
    19: {
        "tagline": "✧ The Joy",
        "chip": "MATRIX DESTINY",
        "title": "The Joy — Sang Pembawa Kebahagiaan",
        "p1_label": "Siapa Kamu",
        "p1": "Susunan titik dari tanggal lahirmu membentuk arketipe The Joy, sosok yang membawa "
              "keceriaan dan energi positif ke mana pun kamu pergi. Kamu punya kemampuan menemukan "
              "hal-hal kecil yang patut disyukuri, bahkan di tengah situasi yang sebenarnya cukup "
              "berat.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Keceriaan dan energi positifmu membuat suasana di sekitarmu terasa lebih ringan dan "
              "menyenangkan. Kamu juga mudah membuat orang lain tersenyum. Namun kebiasaan selalu "
              "ingin terlihat ceria ini kadang membuatmu menyembunyikan kesedihanmu sendiri, bahkan "
              "dari orang-orang terdekat yang sebenarnya ingin membantumu.",
        "quote": "Membawa kebahagiaan bagi orang lain itu indah, tapi kesedihanmu sendiri juga "
                 "berhak diakui.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Ketika sedang tidak baik-baik saja minggu ini, coba akui itu secara terbuka kepada "
              "orang terdekat, alih-alih menutupinya dengan senyuman seperti biasa.",
    },
    20: {
        "tagline": "✧ The Awakening",
        "chip": "MATRIX DESTINY",
        "title": "The Awakening — Sang Pencari Kesadaran",
        "p1_label": "Siapa Kamu",
        "p1": "Susunan titik dari tanggal lahirmu membentuk arketipe The Awakening, sosok yang sering "
              "mengalami momen-momen penyadaran besar yang mengubah cara pandangnya terhadap hidup. "
              "Kamu terus bertumbuh melalui proses mempertanyakan dan memahami ulang keyakinan yang "
              "selama ini kamu pegang.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Keterbukaanmu untuk terus belajar dan berubah membuatmu berkembang lebih jauh "
              "dibanding banyak orang yang enggan mempertanyakan keyakinan lamanya. Kamu juga berani "
              "mengakui ketika kamu salah. Namun proses penyadaran yang terus-menerus ini kadang "
              "membuatmu belum sempat menikmati stabilitas dari satu tahap sebelum berpindah ke "
              "tahap penyadaran berikutnya.",
        "quote": "Terus berkembang itu baik, tapi sesekali berhenti sejenak untuk menikmati apa yang "
                 "sudah kamu pahami juga penting.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Minggu ini, coba berhenti sejenak dari mencari pemahaman baru, dan syukuri apa yang "
              "sudah kamu sadari sejauh ini.",
    },
    21: {
        "tagline": "✧ The Achievement",
        "chip": "MATRIX DESTINY",
        "title": "The Achievement — Sang Pencapai Tujuan",
        "p1_label": "Siapa Kamu",
        "p1": "Susunan titik dari tanggal lahirmu membentuk arketipe The Achievement, sosok yang "
              "punya dorongan kuat untuk mencapai tujuan-tujuan besar dalam hidupnya. Kamu jarang "
              "puas hanya berada di tempat yang sama, dan selalu punya target baru yang ingin kamu "
              "kejar setelah target sebelumnya tercapai.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Ambisi dan kerja kerasmu membuatmu sering mencapai hal-hal yang orang lain anggap "
              "sulit. Kamu juga disiplin dalam mengejar apa yang kamu inginkan. Namun dorongan untuk "
              "terus mencapai lebih banyak ini kadang membuatmu sulit merasa puas, sampai lupa "
              "menikmati pencapaian yang sudah ada di depan mata.",
        "quote": "Pencapaian besar akan terasa lebih bermakna kalau kamu sempat berhenti sejenak "
                 "untuk merayakannya.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Minggu ini, coba rayakan satu pencapaian yang sudah kamu raih, sekecil apa pun itu, "
              "sebelum langsung mengejar target berikutnya.",
    },
    22: {
        "tagline": "✧ The Unity",
        "chip": "MATRIX DESTINY",
        "title": "The Unity — Sang Penyatu yang Utuh",
        "p1_label": "Siapa Kamu",
        "p1": "Susunan titik dari tanggal lahirmu membentuk arketipe The Unity, arketipe terakhir "
              "dalam Matrix Destiny yang melambangkan keutuhan dan penyatuan dari segala pengalaman "
              "hidup. Kamu punya kemampuan melihat gambaran besar dan menyatukan hal-hal yang tampak "
              "terpisah menjadi satu kesatuan yang bermakna.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kemampuanmu melihat keterhubungan antar berbagai hal membuatmu bijaksana dalam "
              "memandang hidup secara utuh, tidak terpaku pada satu bagian saja. Kamu juga bisa "
              "menerima kontradiksi sebagai bagian yang wajar dari kehidupan. Namun cara pandang yang "
              "begitu luas ini kadang membuatmu kesulitan fokus pada hal-hal kecil dan spesifik yang "
              "sebenarnya juga butuh perhatianmu sekarang.",
        "quote": "Melihat gambaran besar itu bijaksana, tapi jangan sampai membuatmu melewatkan "
                 "detail kecil yang ada di depan mata.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Minggu ini, coba fokus menyelesaikan satu hal kecil dan spesifik sampai tuntas, tanpa "
              "langsung memikirkan bagaimana hal itu berhubungan dengan gambaran besar hidupmu.",
    },
}
