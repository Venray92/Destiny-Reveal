"""
Konten Numerologi — Angka Hidup / Life Path (12 kategori).

Key dict ini adalah INTEGER, HARUS sama persis dengan nilai balikan
engine/numerologi.py (hitung_life_path()): 1, 2, 3, 4, 5, 6, 7, 8, 9,
11, 22, 33 (angka 11/22/33 adalah Master Number, tidak direduksi lagi).

Struktur tiap entri sama persis dengan DUMMY_RESULTS di views/revealpage.py.
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
              "lain. Ada dorongan alami dalam dirimu untuk menjadi yang terdepan.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Inisiatif dan kepercayaan dirimu membuat orang lain sering melihatmu sebagai penggerak "
              "utama dalam sebuah kelompok. Kamu juga berani mengambil keputusan tanpa harus menunggu "
              "persetujuan banyak pihak. Namun dorongan untuk selalu memimpin ini kadang membuatmu "
              "kurang sabar bekerja sama, atau sulit menerima ide dari orang lain.",
        "quote": "Menjadi pemimpin yang baik juga berarti tahu kapan harus mengikuti arahan orang "
                 "lain.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba biarkan satu keputusan kecil diambil oleh orang lain di sekitarmu, "
              "dan lihat bagaimana rasanya melepaskan kendali sejenak.",
    },
    2: {
        "tagline": "✦ Angka Hidup 2",
        "chip": "NUMEROLOGI",
        "title": "Angka Hidup 2 — Sosok Harmonis yang Peka",
        "p1_label": "Siapa Kamu",
        "p1": "Angka hidup 2 melambangkan kepekaan, kerja sama, dan kemampuan menjaga keharmonisan "
              "dalam hubungan dengan orang lain. Kamu cenderung memperhatikan perasaan orang di "
              "sekitarmu, dan lebih nyaman bekerja dalam tim dibanding sendirian. Kedamaian terasa "
              "penting bagimu, dan kamu berusaha menghindari konflik sebisa mungkin.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kepekaan dan kemampuanmu bekerja sama membuat orang lain merasa nyaman berada satu tim "
              "denganmu. Kamu juga jago menjembatani perbedaan pendapat. Namun kebiasaan mengutamakan "
              "keharmonisan ini kadang membuatmu terlalu sering mengalah, sampai kebutuhanmu sendiri "
              "jadi terabaikan.",
        "quote": "Kerja sama yang sehat juga memberi ruang bagi kebutuhanmu sendiri untuk didengar.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba sampaikan satu pendapat yang berbeda dari mayoritas, meski itu berarti "
              "sedikit mengganggu keharmonisan yang biasa kamu jaga.",
    },
    3: {
        "tagline": "✦ Angka Hidup 3",
        "chip": "NUMEROLOGI",
        "title": "Angka Hidup 3 — Jiwa Kreatif yang Ekspresif",
        "p1_label": "Siapa Kamu",
        "p1": "Angka hidup 3 melambangkan kreativitas, komunikasi, dan semangat untuk mengekspresikan "
              "diri. Kamu punya cara pandang yang unik terhadap dunia, dan senang membagikannya lewat "
              "kata-kata, karya, atau sekadar obrolan yang hidup. Kehadiranmu sering membawa warna "
              "baru di tengah suasana yang biasa-biasa saja.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kreativitas dan kemampuan komunikasimu membuat orang lain senang menghabiskan waktu "
              "denganmu. Kamu juga pandai mencairkan suasana yang kaku. Namun energi ekspresif ini "
              "kadang membuatmu kesulitan fokus menyelesaikan satu hal, karena terlalu banyak ide baru "
              "yang ingin kamu coba sekaligus.",
        "quote": "Kreativitas akan lebih berbuah kalau kamu memberi satu ide waktu yang cukup untuk "
                 "benar-benar tumbuh.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Pilih satu ide kreatif yang sudah lama kamu simpan, lalu wujudkan sampai selesai "
              "sebelum berpindah memikirkan ide yang lain.",
    },
    4: {
        "tagline": "✦ Angka Hidup 4",
        "chip": "NUMEROLOGI",
        "title": "Angka Hidup 4 — Sosok Teratur yang Bisa Diandalkan",
        "p1_label": "Siapa Kamu",
        "p1": "Angka hidup 4 melambangkan ketertiban, kedisiplinan, dan fondasi yang kuat dalam segala "
              "hal yang kamu bangun. Kamu suka bekerja dengan sistem yang jelas, dan lebih percaya "
              "pada proses yang teruji dibanding jalan pintas. Orang-orang di sekitarmu tahu bahwa "
              "kamu adalah sosok yang bisa diandalkan untuk urusan yang butuh ketelitian.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kedisiplinan dan ketekunanmu membuat apa pun yang kamu bangun cenderung kokoh dan "
              "bertahan lama. Kamu juga jarang mengecewakan orang lain karena selalu berusaha "
              "memenuhi tanggung jawabmu. Sayangnya, kecintaan pada keteraturan ini kadang membuatmu "
              "sulit fleksibel ketika keadaan menuntut perubahan mendadak.",
        "quote": "Fondasi yang kuat tetap butuh sedikit ruang untuk menyesuaikan diri dengan "
                 "perubahan.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Ketika rencana berubah mendadak, coba hadapi dengan tenang dan cari cara "
              "baru menyesuaikan diri, alih-alih merasa terganggu karena keluar dari jadwal.",
    },
    5: {
        "tagline": "✦ Angka Hidup 5",
        "chip": "NUMEROLOGI",
        "title": "Angka Hidup 5 — Petualang yang Haus Kebebasan",
        "p1_label": "Siapa Kamu",
        "p1": "Angka hidup 5 melambangkan kebebasan, perubahan, dan rasa ingin tahu yang besar "
              "terhadap pengalaman baru. Kamu tidak suka terjebak dalam rutinitas yang monoton, dan "
              "selalu tertarik mencoba hal-hal yang belum pernah kamu lakukan sebelumnya. Hidup "
              "terasa lebih bermakna bagimu ketika penuh variasi.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Keluwesan dan keberanianmu mencoba hal baru membuat hidupmu jarang terasa membosankan. "
              "Kamu juga mudah beradaptasi dengan lingkungan yang berbeda-beda. Namun kecintaan pada "
              "kebebasan ini kadang membuatmu kesulitan berkomitmen pada satu hal dalam jangka "
              "panjang, karena selalu ada godaan untuk berpindah ke hal yang baru.",
        "quote": "Kebebasan akan terasa lebih bermakna kalau sesekali kamu memberi ruang bagi "
                 "komitmen untuk tumbuh.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Pilih satu komitmen yang sudah kamu buat, lalu pertahankan konsistensinya "
              "tanpa tergoda mencari variasi baru.",
    },
    6: {
        "tagline": "✦ Angka Hidup 6",
        "chip": "NUMEROLOGI",
        "title": "Angka Hidup 6 — Pengasuh yang Penuh Tanggung Jawab",
        "p1_label": "Siapa Kamu",
        "p1": "Angka hidup 6 melambangkan kepedulian, tanggung jawab, dan cinta terhadap keluarga "
              "maupun orang-orang terdekat. Kamu cenderung merasa bertanggung jawab menjaga "
              "kesejahteraan orang di sekitarmu, bahkan kadang lebih dari kesejahteraanmu sendiri. "
              "Kehadiranmu membuat orang lain merasa diperhatikan dan diurus dengan baik.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kepedulian dan tanggung jawabmu membuat orang-orang terdekat merasa aman dan "
              "diperhatikan. Kamu juga rela berkorban demi kebahagiaan orang yang kamu sayangi. Namun "
              "kebiasaan mengutamakan orang lain ini kadang membuatmu lupa mengurus kebutuhanmu "
              "sendiri, sampai akhirnya kamu yang kelelahan tanpa disadari orang di sekitarmu.",
        "quote": "Merawat orang lain akan lebih berkelanjutan kalau kamu juga merawat dirimu "
                 "sendiri.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Luangkan satu waktu khusus yang benar-benar untuk mengurus kebutuhanmu "
              "sendiri, tanpa merasa bersalah karena tidak sedang mengurus orang lain.",
    },
    7: {
        "tagline": "✦ Angka Hidup 7",
        "chip": "NUMEROLOGI",
        "title": "Angka Hidup 7 — Pemikir Mendalam yang Penuh Perenungan",
        "p1_label": "Siapa Kamu",
        "p1": "Angka hidup 7 melambangkan kedalaman berpikir, rasa ingin tahu terhadap makna di balik "
              "sesuatu, dan kecenderungan untuk merenung. Kamu jarang puas dengan jawaban yang "
              "sederhana, dan selalu ingin memahami sesuatu sampai ke akarnya. Waktu sendiri terasa "
              "penting bagimu untuk mengolah pikiran dan menemukan kejernihan.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kedalaman berpikirmu membuatmu bisa melihat sesuatu dari sudut pandang yang jarang "
              "terpikirkan orang lain. Kamu juga punya kemampuan analisis yang tajam. Namun "
              "kecenderungan untuk banyak merenung sendirian ini kadang membuatmu menjauh dari orang "
              "lain, sampai mereka merasa sulit benar-benar dekat denganmu.",
        "quote": "Perenungan yang dalam akan lebih bermakna kalau sesekali kamu bagikan hasilnya "
                 "kepada orang lain.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba ajak satu orang terdekatmu berdiskusi tentang sesuatu yang sedang kamu pikirkan, "
              "alih-alih memprosesnya sendirian seperti biasa.",
    },
    8: {
        "tagline": "✦ Angka Hidup 8",
        "chip": "NUMEROLOGI",
        "title": "Angka Hidup 8 — Pengelola yang Rapi",
        "p1_label": "Siapa Kamu",
        "p1": "Angka hidup 8 dihitung dari penjumlahan digit tanggal lahirmu, dan dalam numerologi "
              "angka ini identik dengan kemampuan mengelola sesuatu secara terstruktur, baik itu "
              "waktu, uang, maupun rencana jangka panjang. Kamu cenderung berpikir realistis dan "
              "senang melihat hasil yang bisa diukur.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Disiplin dan tanggung jawabmu membuat orang lain merasa aman menitipkan urusan penting "
              "kepadamu. Meski begitu, fokus yang terlalu besar pada hasil kadang membuatmu lupa "
              "menikmati proses, sehingga pencapaian yang seharusnya membanggakan malah terasa "
              "biasa saja.",
        "quote": "Pencapaian akan terasa lebih berarti kalau kamu sempat menikmati perjalanannya.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba beri dirimu waktu untuk merayakan pencapaian kecil sebelum langsung berpindah ke "
              "target berikutnya. Kebiasaan ini akan membuat perjalananmu terasa lebih ringan.",
    },
    9: {
        "tagline": "✦ Angka Hidup 9",
        "chip": "NUMEROLOGI",
        "title": "Angka Hidup 9 — Jiwa Dermawan yang Berpandangan Luas",
        "p1_label": "Siapa Kamu",
        "p1": "Angka hidup 9 melambangkan kepedulian terhadap sesama, jiwa yang dermawan, dan cara "
              "pandang yang luas melampaui kepentingan diri sendiri. Kamu cenderung memikirkan "
              "dampak dari tindakanmu terhadap orang lain atau dunia secara umum, dan sering merasa "
              "terpanggil untuk membantu ketika melihat ketidakadilan.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kepedulian dan kebesaran hatimu membuat orang lain merasa terinspirasi untuk juga "
              "peduli pada sesama. Kamu juga mudah memaafkan dan jarang menyimpan dendam. Namun sisi "
              "idealis ini kadang membuatmu kecewa berat ketika kenyataan tidak sesuai harapanmu "
              "tentang kebaikan orang lain.",
        "quote": "Kepedulian besar tetap perlu disertai penerimaan bahwa tidak semua orang akan "
                 "sebaik yang kamu harapkan.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Ketika kecewa terhadap sikap seseorang, coba terima bahwa itu bukan "
              "cerminan dari kebaikanmu sendiri, dan lanjutkan tanpa membawa kekecewaan itu terlalu "
              "lama.",
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
              "terhadap suasana maupun perasaan di sekitarmu.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Intuisi dan kepekaanmu yang tajam membuatmu bisa menjadi sumber inspirasi bagi orang "
              "lain, karena kamu sering melihat kemungkinan yang belum terpikirkan. Kamu juga punya "
              "idealisme yang kuat tentang bagaimana seharusnya sesuatu berjalan. Namun kepekaan "
              "yang besar ini kadang membuatmu mudah kewalahan oleh emosi, baik emosimu sendiri "
              "maupun emosi orang di sekitarmu.",
        "quote": "Intuisi yang tajam akan lebih membawa kebaikan kalau kamu juga menjaga "
                 "ketenanganmu sendiri.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Ketika merasa kewalahan oleh perasaan, coba luangkan waktu sendirian "
              "sejenak untuk menenangkan pikiran, sebelum memutuskan langkah selanjutnya.",
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
              "panjang dari apa yang kamu bangun.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Perpaduan visi besar dan ketekunanmu membuat orang lain percaya bahwa apa yang kamu "
              "rencanakan benar-benar bisa terwujud, bukan sekadar angan-angan. Kamu juga sanggup "
              "bekerja dalam jangka panjang demi hasil yang besar. Namun standar yang begitu tinggi "
              "ini kadang membuatmu merasa tertekan oleh beban ekspektasi yang kamu tetapkan sendiri.",
        "quote": "Membangun sesuatu yang besar tetap butuh jeda, supaya kamu tidak habis sebelum "
                 "mimpimu benar-benar selesai.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Pecah satu tujuan besarmu menjadi langkah-langkah kecil, dan izinkan "
              "dirimu merasa cukup setelah menyelesaikan satu langkah kecil itu.",
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
              "seberapa besar pengaruhmu terhadap mereka.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kasih sayang dan kepedulianmu terhadap perkembangan orang lain membuatmu jadi sosok "
              "yang dicari saat orang butuh bimbingan atau dukungan emosional. Kamu juga sabar "
              "menemani proses orang lain tanpa terburu-buru. Namun kecenderungan untuk selalu "
              "memberi ini kadang membuatmu lupa bahwa kamu sendiri juga berhak menerima dukungan "
              "yang sama besarnya.",
        "quote": "Membimbing orang lain akan lebih berkelanjutan kalau kamu juga mengizinkan dirimu "
                 "dibimbing dan didukung.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba terima bantuan atau dukungan dari orang lain tanpa langsung "
              "menolaknya dengan alasan bisa mengurus semuanya sendiri.",
    },
}
