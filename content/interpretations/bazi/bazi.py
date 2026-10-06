"""
Konten BaZi (10 Day Master / Tian Gan hari lahir).

Key dict ini HARUS sama persis dengan nilai "day_master" dari
engine/bazi.py (pinyin lowercase: jia, yi, bing, ding, wu, ji, geng, xin,
ren, gui).
"""

BAZI_CONTENT = {
    "jia": {
        "tagline": "甲 · Kayu Yang",
        "chip": "BAZI",
        "title": "Jia — Sang Pohon Besar yang Kokoh",
        "p1_label": "Siapa Kamu",
        "p1": "Day Master Jia digambarkan sebagai pohon besar yang menjulang tinggi — lurus, kokoh, dan "
              "gak gampang goyah meski diterpa angin. Kamu punya prinsip yang kuat dan cenderung terus "
              "terang soal apa yang kamu yakini benar, bahkan kalau itu berarti berbeda pendapat dengan "
              "orang lain. Ada dorongan alami dalam dirimu untuk terus tumbuh dan berkembang, mirip pohon "
              "yang gak pernah berhenti mencari cahaya matahari lebih tinggi.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Integritas dan keteguhanmu bikin orang lain percaya sama kepemimpinanmu — kamu jarang "
              "plin-plan soal prinsip. Tapi kekakuan itu juga bisa jadi titik lemah: kamu kadang terlalu "
              "keras kepala buat mengalah, bahkan di hal yang sebenarnya gak terlalu penting. Belajar "
              "fleksibel di hal-hal kecil akan bikin hubunganmu dengan orang lain lebih lentur.",
        "quote": "\"Pohon yang paling tinggi tetap butuh belajar melengkung sedikit saat anginnya terlalu kencang.\"",
        "p3_label": "Panduan Praktis",
        "p3": "Karir: kamu cocok jadi pemimpin atau perintis — buka usaha sendiri atau posisi yang kasih "
              "otonomi penuh atas keputusan. Asmara: ketegasanmu perlu diimbangi kelembutan, terutama saat "
              "pasangan butuh didengar, bukan cuma diberi solusi. Keuangan: kecenderungan investasi jangka "
              "panjang (properti, bisnis sendiri) cocok buat karaktermu yang sabar menunggu hasil tumbuh. "
              "Kesehatan: jaga fleksibilitas fisik (peregangan, yoga) biar tubuh gak sekaku prinsipmu.",
    },
    "yi": {
        "tagline": "乙 · Kayu Yin",
        "chip": "BAZI",
        "title": "Yi — Sang Tanaman Merambat yang Lentur",
        "p1_label": "Siapa Kamu",
        "p1": "Day Master Yi diibaratkan seperti tanaman merambat atau rumput — lentur, adaptif, dan bisa "
              "tumbuh di celah paling sempit sekalipun. Kamu punya cara halus buat mencapai tujuan, lebih "
              "memilih membujuk dan bekerja sama ketimbang memaksa. Ketahananmu gak kelihatan jelas dari "
              "luar, tapi kamu jarang benar-benar patah meski dihadapkan tekanan berat.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kelenturan dan kemampuan diplomasimu bikin kamu mudah diterima di berbagai lingkungan. Tapi "
              "sisi ini juga bisa bikin kamu terlalu sering mengalah demi menghindari konflik, sampai "
              "kebutuhanmu sendiri kesampingkan. Belajar menyuarakan kebutuhanmu secara langsung, bukan "
              "cuma lewat cara halus, akan bikin orang lain benar-benar paham posisimu.",
        "quote": "\"Yang lentur bukan berarti lemah — akarnya sering lebih kuat dari yang terlihat di permukaan.\"",
        "p3_label": "Panduan Praktis",
        "p3": "Karir: kamu cocok di peran yang butuh diplomasi dan kerja sama — mediasi, hubungan "
              "masyarakat, atau kerja tim lintas divisi. Asmara: kamu gampang menyesuaikan diri sama "
              "pasangan, tapi pastikan itu gak bikin kamu kehilangan identitas sendiri. Keuangan: gaya "
              "bertahap dan gak buru-buru cocok buatmu — investasi kecil rutin lebih pas ketimbang "
              "taruhan besar sekaligus. Kesehatan: sisi yang menyerap tekanan orang lain bisa bikin capek "
              "batin tanpa disadari — sisihkan waktu buat 'melepas' emosi yang terserap dari sekitar.",
    },
    "bing": {
        "tagline": "丙 · Api Yang",
        "chip": "BAZI",
        "title": "Bing — Sang Matahari yang Menerangi",
        "p1_label": "Siapa Kamu",
        "p1": "Day Master Bing diibaratkan matahari — terang, hangat, dan menerangi semua yang ada di "
              "sekitarnya tanpa pandang bulu. Kamu punya energi yang gampang menular ke orang lain, dan "
              "biasanya jadi sosok yang menghidupkan suasana di manapun kamu berada. Kamu suka jadi pusat "
              "perhatian, bukan karena haus validasi, tapi karena memang begitu caramu berbagi energi.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kehangatan dan semangatmu bikin orang lain merasa didukung dan termotivasi. Tapi energi "
              "yang terlalu besar juga bisa terasa berlebihan buat orang yang lebih tenang, dan kamu perlu "
              "hati-hati supaya semangatmu gak berubah jadi impulsif atau kurang perhitungan. Belajar "
              "meredam intensitas di momen yang butuh ketenangan akan bikin pengaruhmu lebih efektif.",
        "quote": "\"Cahaya yang paling berarti bukan yang paling terang, tapi yang tahu kapan harus menghangatkan, bukan membakar.\"",
        "p3_label": "Panduan Praktis",
        "p3": "Karir: kamu bersinar di peran yang tampil di depan — presentasi, penjualan, hiburan, atau "
              "posisi yang butuh membawa energi ke tim. Asmara: pastikan sinarmu juga kasih ruang buat "
              "pasangan bersinar, bukan cuma kamu yang jadi pusat perhatian terus-menerus. Keuangan: "
              "impulsivitas bisa bikin pengeluaran meledak tiba-tiba — pakai sistem otomatis nabung "
              "sebelum sempat dorongan belanja muncul. Kesehatan: energi tinggi butuh jeda — jangan sampai "
              "'membakar diri' karena terus memberi tanpa mengisi ulang.",
    },
    "ding": {
        "tagline": "丁 · Api Yin",
        "chip": "BAZI",
        "title": "Ding — Sang Lilin yang Menghangatkan Dekat",
        "p1_label": "Siapa Kamu",
        "p1": "Day Master Ding diibaratkan seperti lilin atau cahaya bintang — gak seterang matahari, "
              "tapi hangat dan berarti untuk orang-orang di lingkaran dekatmu. Kamu punya kepekaan tinggi "
              "terhadap perasaan orang lain dan cenderung memberi pengaruh secara halus, bukan lewat "
              "gebrakan besar. Kehadiranmu terasa menenangkan, terutama buat orang yang butuh didengar.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kepekaan dan kelembutanmu bikin kamu jadi pendengar yang baik dan teman yang bisa "
              "diandalkan secara emosional. Tapi sisi ini juga bikin kamu gampang terpengaruh suasana hati "
              "orang lain, sampai kadang lupa menjaga energimu sendiri. Belajar menetapkan batas emosional "
              "yang sehat akan melindungi kehangatanmu supaya gak habis buat orang lain.",
        "quote": "\"Cahaya kecil yang konsisten sering lebih berarti dari kilatan besar yang cepat padam.\"",
        "p3_label": "Panduan Praktis",
        "p3": "Karir: kamu cocok di peran yang butuh kepekaan dan perhatian detail — konseling, seni, "
              "penulisan, atau kerja yang berdampak personal ke individu. Asmara: kehangatanmu bikin "
              "pasangan merasa aman, tapi ingatkan diri buat juga menerima perhatian, bukan cuma memberi. "
              "Keuangan: kecenderungan mengalah demi orang lain bisa bikin kamu boros buat kebutuhan orang "
              "lain — tetapkan batas jelas soal bantuan finansial. Kesehatan: kepekaan emosional tinggi "
              "bisa memicu kelelahan mental — jaga waktu 'me time' yang benar-benar gak diganggu.",
    },
    "wu": {
        "tagline": "戊 · Tanah Yang",
        "chip": "BAZI",
        "title": "Wu — Sang Gunung yang Menjulang Stabil",
        "p1_label": "Siapa Kamu",
        "p1": "Day Master Wu diibaratkan gunung besar — stabil, dapat diandalkan, dan gak mudah "
              "tergoyahkan oleh perubahan mendadak. Kamu jadi tempat orang lain bersandar saat situasi "
              "kacau, karena ketenanganmu terasa seperti pijakan yang aman. Kamu juga punya rasa tanggung "
              "jawab besar terhadap orang-orang yang kamu lindungi.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Stabilitas dan keandalanmu bikin kamu jadi sosok yang dipercaya buat memegang tanggung "
              "jawab besar. Tapi sisi ini juga bisa bikin kamu keras kepala dan lambat beradaptasi kalau "
              "situasi berubah cepat. Belajar lebih terbuka terhadap perubahan, meski itu gak nyaman di "
              "awal, akan bikin kestabilanmu lebih relevan dengan situasi yang terus bergerak.",
        "quote": "\"Gunung yang paling kokoh tetap bisa ditumbuhi hal baru di lerengnya, kalau mau memberi ruang.\"",
        "p3_label": "Panduan Praktis",
        "p3": "Karir: kamu cocok di peran yang butuh keandalan jangka panjang — manajemen operasional, "
              "properti, atau posisi yang jadi tulang punggung organisasi. Asmara: pasangan merasa aman "
              "bersamamu, tapi ingat buat sesekali keluar dari rutinitas biar hubungan tetap segar. "
              "Keuangan: naluri konservatifmu cocok buat aset stabil (properti, tabungan jangka panjang) "
              "ketimbang instrumen yang fluktuatif. Kesehatan: kecenderungan menahan beban sendirian bisa "
              "bikin stres menumpuk diam-diam — biasakan cerita ke orang terdekat sebelum beban itu "
              "menggunung.",
    },
    "ji": {
        "tagline": "己 · Tanah Yin",
        "chip": "BAZI",
        "title": "Ji — Sang Ladang Subur yang Menghidupi",
        "p1_label": "Siapa Kamu",
        "p1": "Day Master Ji diibaratkan tanah subur atau ladang — gak mencolok, tapi jadi sumber "
              "kehidupan buat semua yang tumbuh di atasnya. Kamu punya naluri merawat yang kuat, sabar, "
              "dan telaten menghadapi proses yang lama. Kamu jarang cari sorotan, lebih puas melihat orang "
              "lain berkembang berkat dukunganmu di belakang layar.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kesabaran dan sifat merawatmu bikin kamu jadi fondasi yang kuat buat tim atau keluarga. "
              "Tapi sisi ini juga bisa bikin kamu terlalu akomodatif, sampai kebutuhanmu sendiri sering "
              "nomor dua. Belajar mengakui dan menyuarakan kebutuhanmu sendiri akan bikin kamu gak "
              "'terkuras' terus-menerus buat orang lain.",
        "quote": "\"Tanah yang subur tetap butuh dirawat juga, bukan cuma terus-menerus dipakai menanam.\"",
        "p3_label": "Panduan Praktis",
        "p3": "Karir: kamu bersinar di peran pendukung yang berdampak besar — HR, pendidikan, "
              "administrasi, atau posisi yang menopang kelancaran tim. Asmara: kamu perawat yang sabar, "
              "tapi pastikan pasangan juga belajar merawat balik, bukan cuma menerima terus. Keuangan: "
              "kecenderungan menyisihkan buat orang lain perlu diimbangi dana khusus buat kebutuhanmu "
              "sendiri. Kesehatan: karena jarang mengeluh, gejala kelelahanmu sering gak disadari orang "
              "lain — rutin cek kondisi diri sendiri, jangan tunggu sampai benar-benar habis tenaga.",
    },
    "geng": {
        "tagline": "庚 · Logam Yang",
        "chip": "BAZI",
        "title": "Geng — Sang Pedang Baja yang Tegas",
        "p1_label": "Siapa Kamu",
        "p1": "Day Master Geng diibaratkan pedang atau logam mentah yang keras — tegas, berani, dan gak "
              "ragu memotong langsung ke inti masalah. Kamu punya rasa keadilan yang kuat dan gak suka "
              "basa-basi, lebih memilih bicara terus terang meski itu terdengar keras buat sebagian orang. "
              "Kamu juga jenis orang yang berani ambil keputusan sulit yang orang lain hindari.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Ketegasan dan keberanianmu bikin kamu bisa diandalkan saat situasi butuh keputusan cepat "
              "dan berani. Tapi ketajaman ini juga bisa melukai orang lain kalau disampaikan tanpa "
              "kelembutan. Belajar menyampaikan kebenaran dengan cara yang lebih halus, tanpa mengurangi "
              "ketegasannya, akan bikin pesanmu lebih mudah diterima.",
        "quote": "\"Pedang paling tajam sekalipun perlu sarung — bukan buat melemahkan, tapi buat menjaga siapa yang di sekitarnya.\"",
        "p3_label": "Panduan Praktis",
        "p3": "Karir: kamu cocok di peran yang butuh ketegasan dan keputusan cepat — hukum, audit, "
              "militer/keamanan, atau posisi eksekutif yang butuh potong kompas. Asmara: ketegasanmu perlu "
              "diimbangi kelembutan verbal, terutama saat memberi kritik ke pasangan. Keuangan: kamu tegas "
              "soal target finansial, tapi hindari keputusan besar saat sedang emosi/marah. Kesehatan: "
              "ketegangan otot & rahang sering jadi tempat 'nyimpen' emosi yang ditahan — coba teknik "
              "relaksasi fisik secara rutin.",
    },
    "xin": {
        "tagline": "辛 · Logam Yin",
        "chip": "BAZI",
        "title": "Xin — Sang Perhiasan yang Berkilau Halus",
        "p1_label": "Siapa Kamu",
        "p1": "Day Master Xin diibaratkan perhiasan atau logam mulia yang sudah diolah — halus, elegan, "
              "dan detail. Kamu punya standar estetika dan kualitas yang tinggi, baik buat diri sendiri "
              "maupun lingkungan sekitarmu. Kamu juga cukup sensitif terhadap bagaimana orang lain "
              "memandangmu, dan berusaha menjaga citra yang rapi dan terkontrol.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Ketelitian dan cita rasamu yang tinggi bikin hasil kerjamu terasa berkualitas dan "
              "terkurasi dengan baik. Tapi sensitivitas terhadap kritik bisa bikin kamu gampang terluka "
              "atau defensif kalau ada yang menyinggung hasil kerjamu. Belajar memisahkan kritik terhadap "
              "karya dari kritik terhadap diri sendiri akan bikin kamu lebih tahan banting.",
        "quote": "\"Perhiasan paling indah pun butuh proses digosok berkali-kali — kritik yang membangun adalah bagian dari proses itu.\"",
        "p3_label": "Panduan Praktis",
        "p3": "Karir: kamu cocok di bidang yang menghargai detail dan estetika — desain, perhiasan/fashion, "
              "kurasi konten, atau quality assurance. Asmara: kepekaanmu terhadap kritik perlu dikelola "
              "biar gak jadi jarak dengan pasangan saat mereka kasih masukan jujur. Keuangan: standar "
              "tinggi soal kualitas bisa bikin kamu belanja barang mahal — pastikan itu investasi, bukan "
              "cuma soal gengsi. Kesehatan: kecenderungan perfeksionis bisa memicu kecemasan soal "
              "penampilan/citra diri — latih menerima 'cukup baik' tanpa harus sempurna.",
    },
    "ren": {
        "tagline": "壬 · Air Yang",
        "chip": "BAZI",
        "title": "Ren — Sang Samudra yang Luas Tak Terbatas",
        "p1_label": "Siapa Kamu",
        "p1": "Day Master Ren diibaratkan samudra atau sungai besar — luas, dinamis, dan selalu mengalir "
              "mencari jalan baru. Kamu punya rasa ingin tahu besar dan gak suka terkurung dalam rutinitas "
              "yang itu-itu saja. Pikiranmu cepat dan terbuka terhadap ide-ide baru, dan kamu punya "
              "kemampuan menyesuaikan diri di lingkungan yang berbeda-beda.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kecerdasan dan keterbukaanmu terhadap perubahan bikin kamu jago beradaptasi di situasi apa "
              "pun. Tapi sifat yang terlalu 'mengalir bebas' ini juga bisa bikin kamu susah komit atau "
              "konsisten di satu arah dalam waktu lama. Belajar menetapkan satu wadah/tujuan yang jelas "
              "akan membantu energimu yang besar gak tercecer ke mana-mana.",
        "quote": "\"Air paling besar sekalipun butuh wadah supaya bisa dimanfaatkan, bukan cuma mengalir tanpa arah.\"",
        "p3_label": "Panduan Praktis",
        "p3": "Karir: kamu cocok di bidang yang dinamis dan penuh eksplorasi — riset, perjalanan/travel, "
              "media, atau peran yang gak monoton. Asmara: kebebasanmu perlu diimbangi komitmen yang jelas "
              "biar pasangan gak merasa digantung. Keuangan: sifat spontanmu bisa bikin rencana finansial "
              "berubah-ubah — buat 'wadah' aturan dasar (misal persentase tabungan tetap) biar tetap "
              "terarah. Kesehatan: energi yang terus bergerak butuh waktu benar-benar berhenti — jadwalkan "
              "istirahat total, bukan cuma pindah aktivitas.",
    },
    "gui": {
        "tagline": "癸 · Air Yin",
        "chip": "BAZI",
        "title": "Gui — Sang Embun yang Tenang & Dalam",
        "p1_label": "Siapa Kamu",
        "p1": "Day Master Gui diibaratkan embun, gerimis halus, atau air tenang di kedalaman — lembut di "
              "permukaan tapi menyimpan kedalaman yang gak semua orang bisa lihat. Kamu punya intuisi "
              "tajam dan kepekaan terhadap hal-hal yang gak terucap. Kamu cenderung tenang dan pendiam, "
              "tapi pikiranmu terus bekerja mengamati dan memahami sekitar.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kedalaman dan intuisimu bikin kamu bisa memahami orang lain lebih dalam dari yang mereka "
              "sadari sendiri. Tapi sifat pendiam dan misteriusmu juga bisa bikin orang lain kesulitan "
              "benar-benar dekat denganmu, karena kamu jarang membuka diri duluan. Belajar berbagi apa "
              "yang kamu rasakan/pikirkan secara lebih terbuka akan mempererat hubungan yang selama ini "
              "terasa berjarak.",
        "quote": "\"Air yang paling dalam biasanya yang paling tenang di permukaan — bukan berarti kosong, justru penuh.\"",
        "p3_label": "Panduan Praktis",
        "p3": "Karir: kamu cocok di bidang yang butuh analisa mendalam & intuisi — riset, psikologi, "
              "strategi, atau pekerjaan yang butuh bekerja tenang di balik layar. Asmara: kedalamanmu "
              "berharga, tapi pasangan butuh kamu buka suara lebih sering biar mereka gak merasa "
              "ditinggal menebak-nebak. Keuangan: kecenderungan hati-hati & penuh pertimbangan cocok buat "
              "perencanaan jangka panjang yang matang. Kesehatan: kebiasaan memendam perasaan bisa "
              "berdampak ke kesehatan mental — cari saluran ekspresi (jurnal, curhat ke orang tepercaya) "
              "secara rutin.",
    },
}
