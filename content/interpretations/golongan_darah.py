"""
Konten Golongan Darah (4 kategori: A, B, AB, O).

Key dict ini HARUS sama persis dengan nilai yang disimpan sebagai
golongan darah user (huruf kapital: "A", "B", "AB", "O").

Struktur tiap entri sama persis dengan sistem lain (tagline, chip, title,
p1_label, p1, p2_label, p2, quote, p3_label, p3).
"""

GOLONGAN_DARAH_CONTENT = {
    "O": {
        "tagline": "🩸 Golongan Darah O",
        "chip": "GOLONGAN DARAH",
        "title": "O — Sang Pemimpin yang Percaya Diri",
        "p1_label": "Siapa Kamu",
        "p1": "Di Jepang dan sebagian Asia, golongan darah O identik dengan sosok yang tegas, optimis, "
              "dan gampang jadi pusat perhatian di kelompok manapun kamu berada. Kamu cenderung berani "
              "ambil keputusan lebih dulu ketimbang menunggu orang lain bergerak, dan biasanya orang di "
              "sekitarmu memang mengharapkan kamu untuk memimpin. Rasa percaya dirimu bukan sekadar "
              "gaya-gayaan, tapi lahir dari keyakinan bahwa masalah selalu ada jalan keluarnya asal mau "
              "dicari. Energi ini membuatmu mudah membangun jaringan pertemanan yang luas, karena orang "
              "suka berada di dekat seseorang yang terasa hidup dan penuh semangat.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kekuatan utamamu ada di keberanian ambil risiko dan kemampuan menggerakkan orang lain — "
              "kamu jarang terjebak analisis berlebihan, lebih memilih bertindak dan menyesuaikan di "
              "jalan. Sisi yang perlu dijaga: kadang keinginan untuk selalu jadi yang paling dominan "
              "bikin kamu kurang sabar dengar pendapat orang yang lebih pelan/hati-hati, dan bisa "
              "kelihatan keras kepala kalau merasa arahmu sudah benar. Belajar mendelegasikan dan sesekali "
              "diam dulu sebelum bereaksi akan bikin kepemimpinanmu makin matang.",
        "quote": "\"Pemimpin sejati bukan yang paling keras suaranya, tapi yang paling berani bertanggung jawab atas keputusannya.\"",
        "p3_label": "Panduan Praktis",
        "p3": "Karir: kamu paling berkembang di peran yang kasih ruang buat mimpin atau memulai sesuatu "
              "dari nol — wirausaha, sales, atau posisi manajerial cocok buat energimu. Asmara: kamu butuh "
              "pasangan yang bisa mengimbangi ketegasanmu, bukan yang selalu ikut — cari yang berani "
              "berpendapat balik, biar hubungannya sehat bukan cuma satu arah. Keuangan: dorongan ambil "
              "risiko bisa jadi pedang bermata dua — sisihkan dana darurat dulu sebelum coba peluang baru "
              "yang menggiurkan. Kesehatan: energimu tinggi tapi gampang capek kalau dipaksa terus tanpa "
              "jeda — jadwalkan waktu istirahat serius, bukan cuma pas sudah kelelahan.",
    },
    "A": {
        "tagline": "🩸 Golongan Darah A",
        "chip": "GOLONGAN DARAH",
        "title": "A — Sang Perfeksionis yang Bisa Diandalkan",
        "p1_label": "Siapa Kamu",
        "p1": "Golongan darah A biasa dikaitkan dengan sosok yang teliti, disiplin, dan selalu berusaha "
              "melakukan sesuatu dengan benar — bukan asal jadi. Kamu cenderung mikir dulu sebelum "
              "bertindak, dan lebih suka rencana yang matang ketimbang keputusan dadakan. Orang-orang di "
              "sekitarmu sering mengandalkanmu justru karena sifat hati-hatimu ini — kamu jarang bikin "
              "kesalahan ceroboh karena selalu double-check sebelum menyerahkan hasil kerja. Di balik sikap "
              "tenangmu, ada standar tinggi yang kamu terapkan ke diri sendiri, kadang lebih tinggi dari "
              "yang orang lain minta.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Ketelitian dan tanggung jawabmu bikin kamu jadi orang yang paling dipercaya buat pegang "
              "detail penting. Tapi sisi perfeksionis ini juga bisa jadi beban — kamu gampang terlalu keras "
              "sama diri sendiri kalau hasil belum sempurna, dan kadang susah delegasi karena takut orang "
              "lain gak sedetail kamu. Belajar menerima 'cukup baik' di hal-hal yang bukan prioritas utama "
              "akan bikin energimu lebih hemat buat yang benar-benar penting.",
        "quote": "\"Kesempurnaan itu bagus jadi arah, tapi jangan sampai jadi alasan buat gak pernah selesai.\"",
        "p3_label": "Panduan Praktis",
        "p3": "Karir: kamu cocok di peran yang butuh presisi tinggi — quality control, akuntansi, riset, "
              "atau posisi apapun yang menghargai ketelitian di atas kecepatan. Asmara: kamu menunjukkan "
              "sayang lewat tindakan kecil yang konsisten, bukan gestur besar — pastikan pasanganmu paham "
              "bahasa cintamu ini biar gak salah baca sebagai dingin. Keuangan: naluri hati-hatimu bikin "
              "kamu jarang boros, tapi jangan sampai terlalu takut ambil peluang investasi yang sebenarnya "
              "sudah kamu riset matang. Kesehatan: kecenderungan overthinking bisa memicu stres tersembunyi "
              "— sisihkan waktu buat aktivitas yang benar-benar mematikan mode 'analisis' di kepalamu.",
    },
    "B": {
        "tagline": "🩸 Golongan Darah B",
        "chip": "GOLONGAN DARAH",
        "title": "B — Sang Pembebas yang Autentik",
        "p1_label": "Siapa Kamu",
        "p1": "Golongan darah B sering digambarkan sebagai sosok yang bebas, kreatif, dan gak suka terikat "
              "aturan yang menurutmu gak masuk akal. Kamu cenderung mengikuti minat sendiri dengan penuh "
              "semangat, bahkan kalau itu berarti jalan berbeda dari kebanyakan orang. Rasa penasaranmu "
              "besar, dan begitu tertarik sama sesuatu kamu bisa total mendalaminya — tapi begitu bosan, "
              "kamu juga gak segan pindah ke hal lain. Orang di sekitarmu kadang susah menebak langkahmu "
              "berikutnya, tapi justru itu yang bikin kamu menarik dan gak membosankan.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kreativitas dan keberanianmu jadi diri sendiri adalah aset besar — kamu sering jadi sumber "
              "ide segar yang gak kepikiran orang lain. Tapi sisi spontanmu bisa bikin kamu kelihatan "
              "kurang konsisten di mata orang yang lebih suka keteraturan, dan komitmen jangka panjang "
              "kadang terasa berat kalau minatmu udah berpindah. Belajar menyelesaikan apa yang sudah "
              "dimulai, minimal sampai satu tonggak penting, akan bikin potensimu lebih kelihatan hasilnya.",
        "quote": "\"Jadi diri sendiri itu bukan pemberontakan, itu keberanian buat gak ikut arus yang gak cocok buatmu.\"",
        "p3_label": "Panduan Praktis",
        "p3": "Karir: kamu paling hidup di bidang yang kasih ruang eksplorasi — kreatif, riset, atau peran "
              "yang gak monoton dari hari ke hari. Asmara: kamu butuh pasangan yang kasih ruang gerak, "
              "bukan yang posesif — tapi juga latih diri buat kasih kepastian biar pasangan gak ngerasa "
              "digantung. Keuangan: minat yang gampang berpindah bisa bikin pengeluaran buat hobi baru "
              "menumpuk — coba tetapkan budget khusus 'eksplorasi' biar gak mengganggu pos penting lain. "
              "Kesehatan: rutinitas yang terlalu kaku bikin kamu cepat jenuh — cari bentuk olahraga/pola "
              "makan yang variatif biar konsisten dijalani, bukan yang monoton.",
    },
    "AB": {
        "tagline": "🩸 Golongan Darah AB",
        "chip": "GOLONGAN DARAH",
        "title": "AB — Sang Misterius yang Serba Bisa",
        "p1_label": "Siapa Kamu",
        "p1": "Golongan darah AB dikenal sebagai gabungan dua sisi yang kelihatannya bertentangan — bisa "
              "sangat rasional dan terstruktur di satu momen, lalu tiba-tiba jadi sangat emosional dan "
              "artistik di momen lain. Kompleksitas ini bikin kamu sering sulit ditebak, bahkan oleh orang "
              "yang sudah lama kenal kamu. Kamu punya kemampuan melihat sesuatu dari berbagai sudut "
              "pandang sekaligus, yang bikin kamu jago jadi penengah atau pemberi solusi kreatif saat "
              "orang lain cuma melihat satu sisi masalah.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Fleksibilitas berpikirmu adalah kekuatan besar — kamu bisa beradaptasi dengan situasi apapun "
              "dan menemukan pendekatan yang paling pas. Tapi dualitas ini juga bisa bikin kamu sendiri "
              "bingung menentukan mana yang benar-benar kamu mau, dan orang lain kadang kesulitan "
              "memahami maksudmu karena kamu sendiri berubah-ubah. Belajar mengenali pola kapan sisi "
              "rasional atau emosionalmu yang lebih dominan akan bikin kamu lebih mudah mengambil "
              "keputusan tanpa terombang-ambing.",
        "quote": "\"Kompleks bukan berarti bingung — itu tanda kamu punya lebih banyak cara buat memahami dunia.\"",
        "p3_label": "Panduan Praktis",
        "p3": "Karir: kamu cocok di peran yang butuh keseimbangan logika dan kreativitas — konsultan, "
              "desain strategis, atau posisi lintas-fungsi yang butuh menjembatani tim berbeda. Asmara: "
              "pasanganmu perlu paham bahwa sisi rasional dan emosionalmu sama-sama asli, bukan kamu lagi "
              "'bermuka dua' — komunikasikan ini di awal biar gak salah paham. Keuangan: sisi rasionalmu "
              "biasanya bikin kamu cukup terencana, tapi sisi impulsifmu bisa muncul tiba-tiba — pisahkan "
              "rekening 'rencana' dan 'bebas' biar dua sisi ini sama-sama terpenuhi tanpa saling ganggu. "
              "Kesehatan: pergolakan internal antara dua sisi bisa bikin capek secara mental — cari waktu "
              "sendiri secara rutin buat 'menyortir' apa yang benar-benar kamu rasakan.",
    },
}
