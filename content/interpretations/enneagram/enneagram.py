"""Konten interpretasi Enneagram (9 tipe kepribadian) untuk Destiny Reveal.

Key top-level adalah integer 1-9, sesuai 9 tipe klasik Enneagram:
1=The Reformer, 2=The Helper, 3=The Achiever, 4=The Individualist,
5=The Investigator, 6=The Loyalist, 7=The Enthusiast, 8=The Challenger,
9=The Peacemaker.
"""

ENNEAGRAM_CONTENT = {
    1: {
        "tagline": "Satu titik yang selalu mencari garis paling lurus.",
        "chip": "ENNEAGRAM",
        "title": "Tipe 1 — Sang Penjaga Standar yang Berintegritas",
        "p1_label": "Siapa Kamu",
        "p1": "Di dalam dirimu ada suara yang terus menilai, membandingkan apa yang ada dengan "
              "apa yang seharusnya ada, dan suara itu jarang benar-benar diam. Kamu tumbuh dengan "
              "kepekaan tinggi terhadap benar dan salah, rapi dan berantakan, pantas dan tidak "
              "pantas, sehingga kamu sering jadi orang yang paling dulu sadar kalau ada sesuatu "
              "yang kurang pas, entah itu kalimat yang typo, rencana yang bolong, atau sikap yang "
              "kurang etis. Dorongan untuk melakukan sesuatu dengan benar bukan sekadar kebiasaan, "
              "tapi jadi semacam kompas yang menuntun hampir semua keputusanmu. Di balik semua itu, "
              "ada kekhawatiran yang jarang kamu ucapkan keras-keras, yaitu takut dianggap salah, "
              "cacat, atau tidak cukup baik, dan itu yang membuatmu bekerja keras untuk selalu "
              "berada di sisi yang benar. Kamu punya rasa tanggung jawab yang besar terhadap "
              "dirimu sendiri maupun orang di sekitarmu, dan sering merasa harus jadi contoh yang "
              "baik meski tidak ada yang memintanya. Orang-orang di sekitarmu biasanya tahu bahwa "
              "kalau ada yang perlu dikerjakan dengan teliti dan bertanggung jawab, kamu adalah "
              "orang yang bisa diandalkan untuk itu. Kamu juga punya prinsip yang kuat tentang apa "
              "yang kamu anggap adil, dan cukup sulit untuk berkompromi kalau itu menyangkut nilai "
              "yang kamu pegang. Semua ini membuatmu jadi sosok yang konsisten, bisa dipercaya, "
              "dan punya standar yang jelas, meski kadang standar itu terasa berat bahkan untuk "
              "kamu sendiri jalani.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Integritas dan ketelitianmu adalah aset besar, kamu bisa diandalkan untuk "
              "menyelesaikan sesuatu dengan benar, bukan cuma cepat selesai. Kamu juga punya "
              "kepekaan moral yang membuatmu berani menyuarakan sesuatu yang kamu anggap tidak "
              "adil, bahkan ketika orang lain memilih diam. Namun suara pengoreksi di kepalamu itu "
              "kadang bekerja lembur, membuatmu terlalu keras menilai diri sendiri atas kesalahan "
              "kecil yang sebenarnya wajar terjadi. Kekerasan terhadap diri sendiri ini juga bisa "
              "keluar ke arah orang lain, lewat kritik yang terasa menusuk meski niatmu sebenarnya "
              "membantu. Kamu bisa jadi terlalu fokus pada apa yang belum sempurna, sampai lupa "
              "mengapresiasi apa yang sudah baik. Rasa kesal yang terpendam karena merasa jadi "
              "satu-satunya yang peduli standar juga sering muncul diam-diam, dan kalau tidak "
              "disalurkan dengan sehat, bisa berubah jadi kaku atau gampang tersinggung.",
        "quote": "Nggak ada yang sempurna, tapi hal yang sudah dikerjakan dengan tulus tetap "
                 "layak dihargai apa adanya.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba latih dirimu untuk mengucapkan satu kalimat apresiasi ke diri sendiri setiap "
              "kali menyelesaikan sesuatu, sebelum otakmu buru-buru mencari apa yang masih kurang. "
              "Kamu bisa mulai dari hal kecil, misalnya setelah menyelesaikan tugas, tarik napas "
              "sebentar dan akui bahwa kamu sudah berusaha sebaik mungkin, terlepas dari hasil "
              "akhirnya. Latihan ini bukan untuk membuatmu berhenti punya standar, tapi supaya "
              "standar itu tidak selalu terasa seperti beban yang harus kamu pikul sendirian. "
              "Semakin sering kamu melakukannya, semakin ringan rasanya menjalani hari tanpa "
              "harus menunggu semuanya sempurna dulu baru boleh merasa lega.",
        "domains": {
            "karir": "Kamu jadi andalan di pekerjaan yang butuh ketelitian, kepatuhan pada "
                     "prosedur, dan standar kualitas tinggi, seperti audit, quality control, "
                     "penyuntingan, atau peran apa pun yang hasil akhirnya harus benar-benar rapi. "
                     "Atasan biasanya percaya penuh kalau tugas diserahkan ke kamu karena tahu "
                     "kamu tidak akan asal selesai. Tapi kecenderungan untuk terus merevisi demi "
                     "kesempurnaan bisa bikin pekerjaan molor dari deadline, dan kamu bisa "
                     "kelelahan sendiri karena menuntut diri terlalu tinggi di setiap detail. Kamu "
                     "juga bisa jadi frustrasi kalau rekan kerja terlihat kurang peduli soal "
                     "kualitas seperti kamu. *PR: tentukan dulu standar “cukup baik” sebelum "
                     "mulai kerja, dan hentikan revisi begitu standar itu tercapai, bukan menunggu "
                     "sampai terasa sempurna.*",
            "asmara": "Kamu pasangan yang setia dan bertanggung jawab, memegang komitmen dengan "
                      "serius dan berusaha jadi versi terbaik untuk orang yang kamu sayangi. Tapi "
                      "standar tinggi yang biasa kamu terapkan ke diri sendiri kadang ikut "
                      "terbawa ke pasangan, membuatmu tanpa sadar mengkritik hal-hal kecil yang "
                      "sebenarnya tidak perlu dipermasalahkan. Kamu juga bisa kesulitan "
                      "mengungkapkan sisi lepas dan santai dari dirimu karena terlalu sibuk "
                      "menjaga segalanya tetap “benar”. Pasangan mungkin merasa harus selalu "
                      "hati-hati supaya tidak dinilai kurang sempurna di matamu. *PR: sebelum "
                      "menyampaikan kritik ke pasangan, tanya dulu ke diri sendiri apakah ini "
                      "benar-benar penting, atau cuma soal caramu yang berbeda dari caranya.*",
            "keuangan": "Kamu cenderung disiplin dan hati-hati soal uang, jarang belanja "
                        "sembarangan karena kamu punya prinsip jelas soal mana pengeluaran yang "
                        "pantas dan mana yang berlebihan. Kebiasaan mencatat dan merencanakan ini "
                        "membuatmu jarang kaget soal kondisi finansial sendiri. Namun sisi "
                        "perfeksionismu bisa bikin kamu terlalu keras menghukum diri sendiri kalau "
                        "sekali saja belanja di luar rencana, padahal itu wajar terjadi sesekali. "
                        "Kamu juga bisa menunda menikmati hasil kerja kerasmu karena merasa belum "
                        "“pantas” untuk itu. *PR: sisihkan anggaran kecil khusus untuk hal yang "
                        "murni menyenangkan, tanpa merasa bersalah setelah memakainya.*",
            "kesehatan": "Kedisiplinanmu biasanya juga terlihat dari rutinitas hidup sehat yang "
                         "kamu jaga, dari pola makan sampai jadwal tidur. Tapi ketegangan yang "
                         "terus-menerus karena tuntutan tinggi terhadap diri sendiri bisa "
                         "menumpuk jadi stres fisik, seperti rahang yang mengencang atau bahu "
                         "yang kaku tanpa kamu sadari. Kamu juga tipe yang sulit benar-benar "
                         "rileks karena pikiranmu terus mengevaluasi apa yang masih perlu "
                         "diperbaiki, bahkan saat sedang istirahat. *PR: coba luangkan 10 menit "
                         "sehari untuk aktivitas yang benar-benar tanpa tujuan atau target, "
                         "sekadar untuk melatih dirimu berhenti mengevaluasi.*",
        },
    },
    2: {
        "tagline": "Hati yang selalu punya ruang lebih untuk orang lain.",
        "chip": "ENNEAGRAM",
        "title": "Tipe 2 — Sang Pemberi yang Tulus",
        "p1_label": "Siapa Kamu",
        "p1": "Kamu punya kepekaan alami untuk membaca apa yang dibutuhkan orang lain, bahkan "
              "sebelum mereka mengucapkannya, dan itu membuatmu jadi sosok yang hangat serta "
              "mudah didekati. Memberi perhatian, bantuan, atau sekadar telinga untuk mendengarkan "
              "terasa begitu alami buatmu, sampai kadang kamu lupa menanyakan hal yang sama untuk "
              "dirimu sendiri. Di balik kehangatan itu, ada kebutuhan yang cukup dalam untuk "
              "merasa dicintai dan dibutuhkan, dan tanpa sadar kamu sering mengukur nilai dirimu "
              "dari seberapa banyak kamu bisa membantu orang lain. Ketakutan yang jarang kamu "
              "sadari secara terbuka adalah takut tidak dicintai kalau kamu berhenti memberi, "
              "sehingga memberi jadi caramu mendapatkan tempat di hati orang. Kamu juga sangat "
              "peka terhadap suasana hati orang di sekitarmu, dan sering menyesuaikan diri supaya "
              "hubungan tetap harmonis. Orang-orang biasanya merasa nyaman curhat ke kamu karena "
              "kamu benar-benar hadir dan peduli, bukan sekadar basa-basi. Kamu bisa jadi sosok "
              "yang diandalkan dalam keluarga atau lingkaran pertemanan sebagai orang yang selalu "
              "ada saat dibutuhkan. Namun di balik semua kehangatan itu, ada bagian dirimu yang "
              "diam-diam berharap orang lain juga peka dan memberi perhatian yang sama tanpa harus "
              "kamu minta.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kemampuanmu membaca kebutuhan orang lain dan memberi dukungan tulus adalah hal "
              "yang bikin banyak orang merasa disayangi saat berada di dekatmu. Kamu juga fleksibel "
              "dan gampang menyesuaikan diri, sehingga banyak orang dari berbagai latar belakang "
              "merasa nyaman berteman denganmu. Tapi kebiasaan mendahulukan orang lain bisa "
              "membuatmu kehabisan energi tanpa disadari, karena kamu jarang mengisi ulang untuk "
              "dirimu sendiri. Ketika kebutuhanmu tidak terpenuhi, kamu bisa diam-diam merasa "
              "kecewa atau bahkan sedikit dendam, meski jarang mengungkapkannya secara langsung. "
              "Kamu juga rentan kesulitan menolak permintaan orang lain, karena takut dianggap "
              "tidak peduli atau kurang baik. Kalau dibiarkan terus, pola ini bisa membuatmu "
              "merasa lelah secara emosional tanpa tahu persis kenapa.",
        "quote": "Merawat orang lain akan terasa lebih ringan kalau kamu juga mengizinkan dirimu "
                 "sendiri untuk dirawat.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba latih dirimu untuk menyebutkan satu kebutuhanmu sendiri secara langsung, tanpa "
              "menunggu orang lain menyadarinya lebih dulu. Ini bisa dimulai dari hal sederhana, "
              "seperti bilang kamu lelah dan butuh istirahat, alih-alih tetap memaksakan diri "
              "membantu. Latihan ini bukan tentang berhenti peduli pada orang lain, tapi supaya "
              "kepedulian itu juga mengalir balik ke dirimu sendiri. Semakin sering kamu "
              "mengungkapkan kebutuhanmu, semakin orang di sekitarmu belajar bahwa hubungan yang "
              "sehat memang dua arah, bukan cuma kamu yang terus memberi.",
        "domains": {
            "karir": "Kamu unggul di pekerjaan yang melibatkan orang lain secara langsung, seperti "
                     "layanan pelanggan, HR, pengajaran, atau peran pendukung tim yang butuh "
                     "empati tinggi. Rekan kerja sering merasa nyaman datang ke kamu untuk minta "
                     "bantuan karena tahu kamu akan selalu berusaha membantu. Tapi kecenderungan "
                     "sulit menolak permintaan bisa membuatmu kebanjiran tugas orang lain sampai "
                     "pekerjaanmu sendiri terbengkalai. Kamu juga bisa merasa kurang dihargai "
                     "kalau kontribusimu dianggap biasa saja, padahal kamu sudah mengerahkan "
                     "banyak energi untuk itu. *PR: sebelum menyanggupi bantuan tambahan, cek dulu "
                     "kapasitasmu sendiri, dan berani bilang “aku bantu setelah tugasku selesai” "
                     "kalau memang perlu.*",
            "asmara": "Kamu pasangan yang penuh perhatian, selalu berusaha membuat orang yang kamu "
                      "sayangi merasa diperhatikan dan dicintai. Namun kamu bisa terlalu banyak "
                      "memberi sampai lupa menyampaikan apa yang kamu sendiri butuhkan dari "
                      "hubungan itu, lalu diam-diam berharap pasangan membalasnya tanpa diminta. "
                      "Ketika harapan itu tidak terpenuhi, kamu bisa merasa kecewa tapi memilih "
                      "memendamnya demi menjaga suasana tetap baik-baik saja. Pasangan mungkin "
                      "tidak sepenuhnya sadar seberapa besar pengorbanan yang sudah kamu lakukan "
                      "karena kamu jarang mengungkapkannya secara terbuka. *PR: latih diri untuk "
                      "mengucapkan langsung apa yang kamu butuhkan dari pasangan, alih-alih "
                      "berharap dia menebaknya sendiri.*",
            "keuangan": "Kamu cenderung murah hati soal uang, tidak segan membantu orang lain "
                        "secara finansial atau mentraktir tanpa banyak pikir panjang. Kebiasaan "
                        "ini menunjukkan kehangatanmu, tapi juga bisa membuatmu kesulitan menabung "
                        "untuk dirimu sendiri karena selalu mendahulukan kebutuhan orang lain. "
                        "Kamu juga kadang memberi lebih dari kemampuanmu demi menghindari perasaan "
                        "tidak enak menolak. *PR: tetapkan batas jumlah bantuan finansial bulanan "
                        "untuk orang lain, supaya kebutuhanmu sendiri tetap terjaga.*",
            "kesehatan": "Karena energimu banyak tersita untuk mengurus orang lain, kamu sering "
                         "lupa memperhatikan sinyal lelah dari tubuhmu sendiri sampai benar-benar "
                         "kecapean. Kamu juga cenderung menahan emosi negatif demi menjaga suasana "
                         "tetap nyaman untuk orang di sekitar, yang lama-lama bisa menumpuk jadi "
                         "beban pikiran. Pola mendahulukan orang lain ini bisa membuatmu telat "
                         "menyadari kapan sebenarnya kamu butuh istirahat. *PR: jadwalkan waktu "
                         "istirahat khusus untuk dirimu sendiri di kalender, dan perlakukan jadwal "
                         "itu sepenting janji dengan orang lain.*",
        },
    },
    3: {
        "tagline": "Selalu bergerak menuju versi diri yang lebih bersinar.",
        "chip": "ENNEAGRAM",
        "title": "Tipe 3 — Sang Pengejar Prestasi yang Gigih",
        "p1_label": "Siapa Kamu",
        "p1": "Kamu tumbuh dengan dorongan kuat untuk membuktikan kemampuanmu lewat pencapaian "
              "nyata, dan sejak kecil mungkin sudah terbiasa mendapat pujian karena berhasil "
              "melakukan sesuatu dengan baik. Energi dan fokusmu terasa besar ketika ada target "
              "yang jelas di depan mata, dan kamu tahu persis bagaimana caranya menyesuaikan diri "
              "supaya terlihat kompeten di berbagai situasi. Di balik semangat mengejar hasil itu, "
              "ada kekhawatiran yang cukup dalam, yaitu takut dianggap tidak berharga kalau tidak "
              "punya pencapaian untuk ditunjukkan. Kamu jago membaca apa yang dianggap sukses oleh "
              "lingkunganmu, lalu menyesuaikan citra diri supaya sesuai dengan gambaran itu, "
              "kadang sampai kamu sendiri lupa membedakan mana yang benar-benar kamu inginkan dan "
              "mana yang cuma supaya terlihat baik di mata orang lain. Kamu juga punya kemampuan "
              "alami untuk memotivasi diri sendiri dan orang lain, karena kamu percaya bahwa kerja "
              "keras memang membuahkan hasil. Orang-orang di sekitarmu biasanya melihatmu sebagai "
              "sosok yang produktif, percaya diri, dan tahu cara mencapai tujuan. Namun jauh di "
              "dalam, kamu kadang merasa lelah harus terus tampil sempurna, dan bertanya-tanya "
              "seperti apa dirimu kalau tidak sedang mengejar sesuatu.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kegigihan dan efisiensimu membuatmu jadi orang yang bisa diandalkan untuk "
              "menyelesaikan sesuatu tepat waktu dan dengan hasil yang meyakinkan. Kamu juga "
              "pandai memotivasi tim dan menciptakan momentum, membuat orang lain ikut terpacu "
              "bekerja lebih baik. Namun fokus berlebihan pada citra dan hasil bisa membuatmu "
              "mengabaikan perasaanmu sendiri, sampai kamu jarang benar-benar berhenti untuk "
              "merasakan apa yang sedang terjadi di dalam dirimu. Kamu juga rentan menyamakan "
              "harga dirimu dengan pencapaian, sehingga kegagalan kecil bisa terasa seperti "
              "ancaman besar terhadap siapa dirimu sebenarnya. Kecenderungan untuk terus tampil "
              "meyakinkan di depan orang lain kadang membuatmu sulit jujur soal kelelahan atau "
              "keraguan yang sebenarnya kamu rasakan.",
        "quote": "Kamu tetap berharga bukan karena apa yang berhasil kamu capai, tapi karena siapa "
                 "kamu apa adanya.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba luangkan waktu setiap minggu untuk melakukan sesuatu yang tidak berhubungan "
              "sama sekali dengan pencapaian atau produktivitas, murni untuk kesenangan. Rasakan "
              "bagaimana rasanya melakukan sesuatu tanpa tujuan membuktikan apa pun ke siapa pun. "
              "Kamu juga bisa mulai bertanya ke diri sendiri, seandainya tidak ada yang menilai "
              "hasilnya, apakah kamu tetap mau melakukan hal itu. Latihan kecil ini membantumu "
              "perlahan mengenali dirimu di luar daftar pencapaian, dan menyadari bahwa kamu tetap "
              "layak dihargai bahkan saat sedang tidak produktif.",
        "domains": {
            "karir": "Kamu jadi bintang di lingkungan kerja yang kompetitif dan berorientasi "
                     "target, mampu naik jenjang karier dengan cepat karena hasil kerjamu yang "
                     "konsisten dan meyakinkan. Kamu juga pandai membangun personal branding yang "
                     "membuat orang lain percaya pada kemampuanmu. Tapi kecenderungan untuk terus "
                     "mengejar pencapaian berikutnya bisa membuatmu sulit berhenti sejenak untuk "
                     "menikmati keberhasilan yang sudah diraih. Kamu juga rawan burnout karena "
                     "merasa harus selalu tampil sempurna di depan atasan dan rekan kerja. *PR: "
                     "sebelum langsung lanjut ke target berikutnya, luangkan waktu untuk benar-"
                     "benar mengakui dan merayakan pencapaian yang baru saja kamu selesaikan.*",
            "asmara": "Kamu pasangan yang penuh semangat dan bisa membawa energi positif ke "
                      "hubungan, sering mengajak pasangan mencapai hal-hal baru bersama. Tapi "
                      "kesibukanmu mengejar berbagai target bisa membuat waktu berkualitas dengan "
                      "pasangan jadi terpinggirkan, dan kamu kadang lebih nyaman membahas rencana "
                      "atau pencapaian daripada perasaan yang lebih dalam. Pasangan mungkin merasa "
                      "sulit benar-benar mengenal sisi rapuhmu karena kamu terbiasa menjaga citra "
                      "tetap kuat di depannya. *PR: coba ceritakan satu kekhawatiran atau "
                      "kegagalanmu ke pasangan tanpa langsung menutupnya dengan solusi atau "
                      "rencana perbaikan.*",
            "keuangan": "Kamu cenderung ambisius soal keuangan, sering menargetkan penghasilan "
                        "atau aset tertentu sebagai bukti kesuksesanmu. Kamu juga cukup disiplin "
                        "berinvestasi kalau itu sejalan dengan citra sukses yang kamu bangun. "
                        "Namun kamu bisa tergoda membeli barang-barang bermerek atau gaya hidup "
                        "tertentu demi terlihat sukses di mata orang lain, meski itu sebenarnya "
                        "di luar kebutuhanmu. *PR: sebelum membeli sesuatu yang mahal, tanya ke "
                        "diri sendiri apakah kamu benar-benar menginginkannya atau sekadar ingin "
                        "terlihat sukses.*",
            "kesehatan": "Kamu punya stamina tinggi dan disiplin menjaga penampilan serta "
                         "produktivitas fisik, sering menjadikan olahraga sebagai bagian dari "
                         "rutinitas pencapaian. Tapi kamu rawan mengabaikan sinyal kelelahan "
                         "karena terlalu fokus terus bergerak dan menghasilkan sesuatu. Stres yang "
                         "tidak disadari juga bisa tersimpan di tubuh karena kamu jarang benar-"
                         "benar berhenti dan merasakan apa yang terjadi secara emosional. *PR: "
                         "coba satu hari dalam seminggu di mana kamu sengaja tidak mengejar target "
                         "apa pun, termasuk target olahraga, dan biarkan tubuhmu benar-benar "
                         "beristirahat.*",
        },
    },
    4: {
        "tagline": "Selalu mencari warna paling asli dari dirinya sendiri.",
        "chip": "ENNEAGRAM",
        "title": "Tipe 4 — Sang Pencari Makna yang Mendalam",
        "p1_label": "Siapa Kamu",
        "p1": "Kamu merasakan hidup dengan intensitas yang berbeda dari kebanyakan orang, seolah "
              "setiap emosi punya warna dan lapisan yang ingin benar-benar kamu pahami sebelum "
              "melepaskannya. Sejak muda, kamu mungkin sering merasa sedikit berbeda dari orang "
              "sekitar, dan alih-alih menganggap itu masalah, kamu perlahan belajar menjadikan "
              "keunikan itu sebagai bagian dari identitasmu. Di balik kedalaman perasaan itu, ada "
              "kekhawatiran yang jarang kamu ucapkan, yaitu takut tidak punya identitas yang "
              "cukup jelas atau berarti, sehingga kamu terus mencari sesuatu yang benar-benar "
              "terasa “kamu banget”. Kamu punya kepekaan estetika dan emosional yang tinggi, "
              "membuatmu bisa menangkap keindahan atau kesedihan dalam hal-hal yang mungkin "
              "terlewat oleh orang lain. Kamu juga cenderung membandingkan dirimu dengan orang "
              "lain, kadang merasa ada sesuatu yang orang lain punya tapi kamu tidak, meski secara "
              "logika kamu tahu itu belum tentu benar. Ekspresi diri terasa penting buatmu, entah "
              "lewat cara berpakaian, tulisan, seni, atau caramu bicara tentang perasaan secara "
              "terbuka. Orang-orang di sekitarmu biasanya melihatmu sebagai sosok yang autentik "
              "dan punya kedalaman, seseorang yang tidak takut menunjukkan sisi rapuh dari "
              "dirinya.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kepekaan emosional dan kreativitasmu membuatmu bisa memahami dan mengungkapkan "
              "perasaan dengan cara yang jarang dimiliki orang lain, dan itu sering jadi sumber "
              "koneksi yang dalam dengan orang-orang di sekitarmu. Kamu juga berani menjadi diri "
              "sendiri meski itu berarti tidak selalu mengikuti arus. Namun kecenderungan untuk "
              "terus membandingkan diri dengan orang lain bisa membuatmu merasa kurang, padahal "
              "kamu punya banyak hal berharga yang sering luput kamu sadari sendiri. Emosi yang "
              "intens juga kadang membuatmu terlarut cukup lama dalam perasaan sedih atau "
              "melankolis, sampai sulit kembali ke aktivitas sehari-hari. Kamu bisa terjebak "
              "menunggu momen atau perasaan yang “sempurna” sebelum bertindak, padahal langkah "
              "kecil yang biasa saja sebenarnya sudah cukup untuk memulai.",
        "quote": "Kamu tidak perlu jadi berbeda untuk berarti, karena dirimu yang biasa saja pun "
                 "sudah cukup berharga.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba pilih satu hal kecil yang ingin kamu lakukan, lalu kerjakan tanpa menunggu "
              "mood atau perasaan yang pas dulu. Latih dirimu untuk mulai bergerak meski suasana "
              "hati belum sepenuhnya mendukung, karena tindakan kecil kadang justru yang membantu "
              "memperbaiki suasana hati, bukan sebaliknya. Kamu juga bisa mencoba menuliskan satu "
              "hal biasa yang tetap berarti dalam harimu, tanpa harus terasa istimewa atau "
              "dramatis. Latihan ini membantumu menyadari bahwa makna tidak selalu datang dari "
              "momen besar, tapi juga dari hal-hal sederhana yang konsisten kamu jalani.",
        "domains": {
            "karir": "Kamu bersinar di pekerjaan yang memberi ruang ekspresi diri, seperti bidang "
                     "kreatif, seni, menulis, desain, atau apa pun yang memungkinkanmu menuangkan "
                     "perasaan jadi sesuatu yang nyata. Kamu punya perspektif unik yang sering "
                     "membuat hasil kerjamu terasa berbeda dari orang lain. Tapi kamu bisa "
                     "kehilangan motivasi di pekerjaan yang terasa monoton atau tidak punya ruang "
                     "untuk keaslianmu, dan gampang merasa pekerjaan itu tidak “cocok” meski "
                     "sebenarnya baru butuh penyesuaian kecil. Kamu juga rawan menunda pekerjaan "
                     "sambil menunggu inspirasi datang. *PR: tetapkan waktu kerja rutin meski "
                     "sedang tidak merasa terinspirasi, dan biarkan hasilnya biasa saja dulu, "
                     "bukan harus langsung istimewa.*",
            "asmara": "Kamu pasangan yang penuh kedalaman, mampu membangun koneksi emosional yang "
                      "kuat dan membuat orang yang kamu cintai merasa benar-benar dipahami. Tapi "
                      "kamu juga bisa terlalu fokus pada apa yang “kurang” dalam hubungan, "
                      "membandingkannya dengan bayangan hubungan ideal yang sebenarnya tidak "
                      "sepenuhnya realistis. Ketika hubungan terasa terlalu stabil atau biasa "
                      "saja, kamu bisa diam-diam merindukan drama atau intensitas yang lebih "
                      "besar. Pasangan mungkin merasa perlu berhati-hati karena suasana hatimu "
                      "bisa berubah cukup cepat. *PR: sebelum menyimpulkan hubunganmu kurang "
                      "berarti, coba tuliskan tiga hal biasa yang sebenarnya sudah baik dari "
                      "hubungan itu.*",
            "keuangan": "Kamu cenderung mengaitkan pengeluaran dengan ekspresi diri, seperti "
                        "membeli barang yang terasa “mewakili” siapa kamu, entah itu buku, karya "
                        "seni, atau barang dengan nilai estetika tinggi. Kebiasaan ini bisa "
                        "membuatmu kesulitan membedakan mana kebutuhan dan mana keinginan yang "
                        "didorong emosi sesaat. Suasana hati yang naik turun juga kadang "
                        "memengaruhi pola belanjamu, di mana kamu belanja lebih banyak saat "
                        "sedang sedih untuk menghibur diri. *PR: sebelum belanja karena sedang "
                        "merasa emosional, coba tunda dulu dan tuliskan dulu perasaanmu di jurnal "
                        "sebagai gantinya.*",
            "kesehatan": "Kepekaanmu terhadap emosi bisa jadi berkah sekaligus tantangan, karena "
                         "kamu cenderung merasakan naik turun suasana hati lebih dalam dibanding "
                         "orang lain. Kalau tidak disalurkan dengan sehat, perasaan yang terpendam "
                         "bisa memengaruhi energi fisikmu, membuatmu gampang lelah tanpa sebab "
                         "yang jelas. Kamu juga rawan mengisolasi diri saat sedang merasa sedih, "
                         "padahal dukungan dari orang lain sebenarnya bisa membantu. *PR: cari "
                         "satu cara menyalurkan emosi secara rutin, seperti menulis jurnal atau "
                         "membuat sesuatu, alih-alih hanya memendamnya sendirian.*",
        },
    },
    5: {
        "tagline": "Pikiran yang senang menyelam sebelum bicara.",
        "chip": "ENNEAGRAM",
        "title": "Tipe 5 — Sang Pengamat yang Mendalam",
        "p1_label": "Siapa Kamu",
        "p1": "Kamu punya cara memahami dunia lewat pengamatan dan pemikiran mendalam, lebih "
              "dulu menyerap informasi diam-diam sebelum memutuskan mau terlibat sejauh mana. Sejak "
              "kecil, kamu mungkin sudah terbiasa menikmati waktu sendirian untuk membaca, "
              "meneliti, atau sekadar merenung, karena di situlah kamu merasa paling nyaman dan "
              "punya kendali penuh atas ruang pribadimu. Di balik ketenanganmu, ada kekhawatiran "
              "yang cukup mendasar, yaitu takut kehabisan energi atau merasa kewalahan kalau "
              "terlalu banyak dituntut secara emosional maupun sosial, sehingga kamu belajar "
              "menjaga jarak sebagai cara melindungi diri. Kamu sangat menghargai kompetensi dan "
              "pengetahuan, dan sering merasa lebih percaya diri ketika sudah benar-benar "
              "memahami sesuatu secara mendalam sebelum berbicara atau bertindak. Privasi terasa "
              "penting buatmu, dan kamu cenderung membagi hidupmu jadi kotak-kotak yang terpisah, "
              "supaya energimu tidak terkuras oleh terlalu banyak tuntutan sekaligus. Orang-orang "
              "di sekitarmu biasanya menghormati wawasanmu yang luas dan caramu berpikir yang "
              "tajam, meski kadang mereka merasa kamu agak sulit dijangkau secara emosional. "
              "Ketika kamu sudah merasa aman dengan seseorang, kamu sebenarnya bisa sangat setia "
              "dan hangat, hanya saja butuh waktu untuk sampai ke titik itu.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kemampuan analisismu yang tajam dan rasa ingin tahu yang besar membuatmu bisa "
              "memahami hal-hal kompleks dengan cara yang jernih dan objektif. Kamu juga mandiri "
              "dan tidak mudah terbawa opini orang lain, karena kamu lebih percaya pada apa yang "
              "sudah kamu pelajari dan pahami sendiri. Namun kebiasaan menjaga jarak emosional "
              "bisa membuat orang lain merasa kamu dingin atau sulit didekati, padahal sebenarnya "
              "kamu hanya butuh waktu lebih untuk merasa nyaman. Kamu juga rawan menarik diri "
              "sepenuhnya saat merasa terlalu banyak tuntutan, sampai orang di sekitarmu merasa "
              "diabaikan. Kecenderungan untuk terus mengumpulkan informasi sebelum bertindak "
              "kadang membuatmu terlalu lama di fase “belajar” dan terlambat mempraktikkan apa "
              "yang sudah kamu ketahui.",
        "quote": "Pengetahuan akan terasa lebih hidup ketika kamu berani mempraktikkannya, bukan "
                 "hanya menyimpannya di kepala.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba pilih satu topik yang sudah lama kamu pelajari, lalu bagikan pemahamanmu ke "
              "satu orang secara langsung, meski terasa sedikit tidak nyaman untuk keluar dari "
              "zona amanmu. Latih dirimu untuk terlibat lebih dulu sebelum merasa benar-benar "
              "siap seratus persen, karena kesiapan penuh itu kadang tidak pernah benar-benar "
              "datang. Kamu juga bisa mencoba menghabiskan waktu bersama orang lain tanpa agenda "
              "belajar apa pun, sekadar untuk hadir dan terhubung. Latihan kecil ini membantumu "
              "perlahan menyeimbangkan waktu sendirian yang kamu butuhkan dengan koneksi yang "
              "juga penting untuk dijaga.",
        "domains": {
            "karir": "Kamu unggul di pekerjaan yang membutuhkan riset mendalam, analisis, atau "
                     "keahlian teknis, seperti bidang penelitian, teknologi, atau peran yang "
                     "memberimu ruang kerja mandiri. Kamu dikenal sebagai orang yang benar-benar "
                     "menguasai bidangnya, bukan sekadar tahu permukaan. Tapi kamu bisa kesulitan "
                     "di lingkungan kerja yang menuntut banyak interaksi sosial atau rapat "
                     "mendadak, karena itu terasa menguras energimu lebih cepat dari yang orang "
                     "lain sadari. Kamu juga rawan menunda presentasi ide karena merasa belum "
                     "cukup riset, padahal timing kadang lebih penting dari kesempurnaan data. "
                     "*PR: tetapkan batas waktu riset sebelum menyampaikan ide, supaya kamu tidak "
                     "terjebak terlalu lama di fase persiapan.*",
            "asmara": "Kamu pasangan yang setia dan penuh pertimbangan begitu sudah merasa nyaman "
                      "dan percaya, dan mampu memberi perhatian yang dalam meski caranya tidak "
                      "selalu ekspresif. Tapi kebutuhanmu akan waktu dan ruang sendiri kadang "
                      "disalahartikan pasangan sebagai kurang peduli, padahal itu caramu "
                      "mengisi ulang energi. Kamu juga cenderung menyimpan perasaan sendiri "
                      "sampai benar-benar yakin sebelum membagikannya, yang bisa membuat pasangan "
                      "merasa sulit benar-benar memahami isi kepalamu. *PR: coba beri tahu "
                      "pasangan lebih awal kapan kamu butuh waktu sendiri, supaya itu tidak "
                      "terasa seperti penolakan buatnya.*",
            "keuangan": "Kamu cenderung hemat dan berhati-hati soal uang, sering melakukan riset "
                        "mendalam sebelum membeli sesuatu yang nilainya besar. Kebiasaan ini "
                        "membuatmu jarang menyesal soal keputusan finansial karena semuanya sudah "
                        "dipikirkan matang-matang. Namun kamu bisa terlalu pelit terhadap diri "
                        "sendiri, menunda kenyamanan yang sebenarnya sudah mampu kamu penuhi "
                        "karena masih merasa perlu riset lebih jauh lagi. *PR: tetapkan satu "
                        "kategori pengeluaran yang boleh kamu putuskan tanpa riset panjang, "
                        "sekadar untuk melatih fleksibilitas.*",
            "kesehatan": "Kamu cenderung nyaman dengan rutinitas yang tenang dan waktu sendirian "
                         "untuk mengisi ulang energi, dan itu penting buat kesehatan mentalmu. "
                         "Tapi kamu rawan mengabaikan kebutuhan fisik seperti makan teratur atau "
                         "bergerak aktif karena terlalu asyik tenggelam dalam pikiran atau "
                         "pekerjaan. Kamu juga cenderung menahan diri dari mencari bantuan saat "
                         "sedang kesulitan, karena lebih memilih mencari jawabannya sendiri "
                         "terlebih dulu. *PR: pasang pengingat sederhana untuk jeda makan atau "
                         "bergerak setiap beberapa jam, supaya kebutuhan fisikmu tidak terlewat "
                         "begitu saja.*",
        },
    },
    6: {
        "tagline": "Selalu menyiapkan payung sebelum langit benar-benar mendung.",
        "chip": "ENNEAGRAM",
        "title": "Tipe 6 — Sang Penjaga Kesetiaan yang Waspada",
        "p1_label": "Siapa Kamu",
        "p1": "Kamu punya kepekaan tajam untuk membaca potensi risiko dan bahaya yang mungkin "
              "belum disadari orang lain, dan pikiranmu sering bekerja beberapa langkah lebih maju "
              "untuk mempersiapkan berbagai kemungkinan. Kesetiaanmu pada orang-orang dan "
              "kelompok yang kamu percaya sangat kuat, dan kamu termasuk orang yang akan berdiri "
              "di samping mereka saat keadaan sulit. Di balik kewaspadaan itu, ada kebutuhan "
              "mendasar akan rasa aman dan dukungan, dan kekhawatiran yang sering muncul adalah "
              "takut berada sendirian tanpa arahan atau dukungan yang bisa diandalkan saat "
              "keadaan sulit. Kamu cenderung mempertanyakan banyak hal sebelum benar-benar "
              "percaya, baik itu pada orang, rencana, maupun keputusan besar, karena kamu ingin "
              "memastikan semuanya sudah dipikirkan matang dari berbagai sisi. Pikiranmu bisa "
              "sangat aktif membayangkan skenario terburuk, bukan karena kamu pesimis, tapi "
              "karena itu caramu merasa lebih siap menghadapi apa pun yang mungkin terjadi. Kamu "
              "juga punya rasa solidaritas yang kuat terhadap kelompok atau komunitas yang kamu "
              "anggap sebagai rumah, dan biasanya jadi orang yang paling bisa diandalkan saat "
              "situasi mulai tidak menentu. Orang-orang di sekitarmu tahu bahwa kamu adalah "
              "sosok yang jujur, teliti, dan bisa dipercaya untuk memikirkan hal-hal yang mungkin "
              "terlewat oleh yang lain.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kewaspadaan dan kemampuan antisipasimu membuatmu jadi orang yang bisa diandalkan "
              "saat tim atau keluarga butuh perencanaan matang menghadapi ketidakpastian. "
              "Kesetiaanmu juga membuat orang-orang di sekitarmu merasa punya sekutu yang benar-"
              "benar bisa dipercaya. Namun kekhawatiran yang terus berputar di kepala bisa membuat "
              "kamu sulit benar-benar rileks, bahkan saat situasi sebenarnya baik-baik saja. "
              "Keraguan yang berlebihan juga kadang membuatmu sulit mengambil keputusan cepat, "
              "karena kamu terus mempertimbangkan berbagai kemungkinan sebelum yakin sepenuhnya. "
              "Kamu bisa jadi terlalu curiga terhadap niat orang lain, terutama saat merasa "
              "kurang punya kendali atas situasi, dan itu kadang menciptakan jarak yang sebenarnya "
              "tidak perlu ada.",
        "quote": "Rasa aman yang paling kuat bukan datang dari memastikan semua kemungkinan "
                 "buruk, tapi dari percaya kamu bisa menghadapi apa pun yang datang.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba latih dirimu mengambil satu keputusan kecil tanpa memikirkan semua skenario "
              "terburuknya dulu, dan lihat bagaimana rasanya bertindak dengan cukup informasi "
              "saja, bukan informasi yang sempurna. Kamu bisa mulai dari hal sederhana, seperti "
              "memilih tempat makan tanpa riset panjang, sekadar untuk melatih rasa percaya pada "
              "penilaianmu sendiri. Setiap kali pikiran mulai membayangkan hal buruk yang belum "
              "tentu terjadi, coba tuliskan juga satu kemungkinan baik yang sama-sama masuk "
              "akal. Latihan ini membantumu perlahan membangun rasa aman dari dalam diri sendiri, "
              "bukan hanya dari kepastian eksternal.",
        "domains": {
            "karir": "Kamu unggul di pekerjaan yang butuh perencanaan matang dan manajemen risiko, "
                     "seperti compliance, keamanan, manajemen proyek, atau peran apa pun yang "
                     "menghargai ketelitian dan kesetiaan pada tim. Rekan kerja mempercayaimu "
                     "sebagai orang yang akan mengingatkan potensi masalah sebelum jadi krisis "
                     "besar. Tapi kecenderungan untuk terus mempertanyakan keputusan bisa membuat "
                     "prosesnya terasa lambat, dan kamu bisa cemas berlebihan soal hal-hal yang "
                     "sebenarnya masih di luar kendalimu. Kamu juga rawan meragukan keputusan yang "
                     "sudah diambil, bahkan setelah semuanya berjalan lancar. *PR: tetapkan batas "
                     "waktu untuk berpikir sebelum mengambil keputusan, lalu percayakan sisanya "
                     "pada kemampuanmu beradaptasi.*",
            "asmara": "Kamu pasangan yang setia dan berkomitmen penuh begitu sudah merasa aman "
                      "dan percaya pada hubungan itu. Tapi rasa waspadamu kadang membuatmu "
                      "mencari-cari tanda bahaya dalam hubungan yang sebenarnya baik-baik saja, "
                      "seperti terlalu menganalisis pesan singkat pasangan atau perubahan kecil "
                      "dalam nada bicaranya. Kekhawatiran ini, kalau dibiarkan, bisa menciptakan "
                      "ketegangan yang sebenarnya tidak perlu ada dalam hubungan. Pasangan mungkin "
                      "perlu memberi kepastian ekstra supaya kamu merasa lebih tenang. *PR: "
                      "sebelum menyimpulkan sesuatu yang buruk dari sikap pasangan, coba tanyakan "
                      "langsung apa maksudnya daripada menebak-nebak sendiri.*",
            "keuangan": "Kamu cenderung berhati-hati dan suka menyiapkan dana darurat sebagai "
                        "bentuk rasa aman, dan itu kebiasaan finansial yang sehat. Tapi "
                        "kekhawatiran berlebihan soal masa depan bisa membuatmu terlalu menahan "
                        "diri, sampai sulit menikmati hasil kerja kerasmu sendiri karena selalu "
                        "membayangkan skenario darurat yang mungkin belum tentu terjadi. Kamu "
                        "juga bisa ragu-ragu terlalu lama sebelum mengambil keputusan investasi, "
                        "sampai kehilangan momen yang sebenarnya baik. *PR: tetapkan target dana "
                        "darurat yang jelas, dan izinkan dirimu menikmati sisanya begitu target "
                        "itu tercapai.*",
            "kesehatan": "Kecemasan yang terus berputar di kepala bisa jadi sumber ketegangan "
                         "fisik yang sebenarnya bisa dihindari, seperti sulit tidur nyenyak "
                         "karena pikiran terus aktif memikirkan berbagai kemungkinan. Kamu juga "
                         "rawan merasa gelisah tanpa sebab jelas, terutama saat situasi di "
                         "sekitarmu terasa tidak menentu. Kebiasaan mengantisipasi hal buruk ini "
                         "kalau tidak dikelola bisa berubah jadi kecemasan yang menetap. *PR: "
                         "coba latihan pernapasan sederhana sebelum tidur untuk membantu "
                         "menenangkan pikiran yang masih aktif berputar.*",
        },
    },
    7: {
        "tagline": "Selalu ada satu pintu baru yang menarik untuk dibuka.",
        "chip": "ENNEAGRAM",
        "title": "Tipe 7 — Sang Penjelajah yang Penuh Semangat",
        "p1_label": "Siapa Kamu",
        "p1": "Kamu punya energi yang terasa selalu siap menyambut hal baru, dan pikiranmu senang "
              "melompat dari satu ide menarik ke ide lainnya sebelum satu hal selesai sepenuhnya "
              "dijelajahi. Kamu jago melihat sisi positif dan kemungkinan seru dari hampir semua "
              "situasi, bahkan yang awalnya terlihat sulit sekalipun, dan itu membuatmu jadi sosok "
              "yang menyenangkan diajak berbicara maupun berencana. Di balik semangat itu, ada "
              "kecenderungan menghindari rasa sakit atau kekosongan, sehingga kamu selalu mencari "
              "kegiatan, rencana, atau opsi baru sebagai cara menjaga diri tetap bergerak dan "
              "tidak terjebak dalam perasaan berat. Kamu juga punya rasa ingin tahu yang besar "
              "terhadap banyak hal sekaligus, membuatmu punya berbagai minat yang kadang terasa "
              "tidak berhubungan satu sama lain, tapi semuanya sama-sama menarik buatmu. "
              "Fleksibilitasmu tinggi, kamu cepat beradaptasi dengan perubahan rencana dan jarang "
              "merasa terjebak dalam satu jalur saja. Orang-orang di sekitarmu biasanya merasa "
              "lebih hidup dan optimis saat berada di dekatmu, karena energimu menular dan "
              "membuat suasana terasa lebih ringan. Namun di balik semua semangat itu, ada "
              "momen-momen ketika kamu sebenarnya butuh berhenti sejenak, hanya saja kamu sering "
              "memilih untuk terus bergerak daripada berhadapan dengan perasaan yang lebih berat.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Optimisme dan energi positifmu membuatmu jadi sumber semangat bagi orang di "
              "sekitarmu, dan kemampuanmu melihat berbagai kemungkinan membuat banyak ide segar "
              "muncul dari kepalamu. Kamu juga cepat beradaptasi dan jarang terjebak lama dalam "
              "kesedihan, sehingga bisa bangkit lebih cepat dari kebanyakan orang. Namun "
              "kecenderungan untuk terus mencari hal baru bisa membuatmu kesulitan menyelesaikan "
              "sesuatu sampai tuntas, karena godaan untuk pindah ke hal yang lebih menarik selalu "
              "ada. Kamu juga rentan menghindari perasaan yang tidak nyaman dengan langsung "
              "mengalihkan perhatian ke kesibukan lain, padahal perasaan itu kadang perlu "
              "benar-benar dihadapi dulu. Kebiasaan menghindari komitmen jangka panjang, entah "
              "dalam pekerjaan atau hubungan, bisa membuat orang lain merasa sulit benar-benar "
              "mengandalkanmu untuk hal yang butuh konsistensi.",
        "quote": "Kebahagiaan yang paling dalam justru sering ditemukan setelah kamu berani "
                 "berhenti sejenak dan merasakan, bukan terus berlari menghindar.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba pilih satu hal yang sudah kamu mulai tapi belum selesai, lalu fokuskan "
              "energimu untuk menyelesaikannya sebelum memulai hal baru yang lain. Latih dirimu "
              "untuk duduk sebentar dengan perasaan yang tidak nyaman, tanpa buru-buru "
              "mengalihkannya dengan aktivitas atau rencana baru. Kamu bisa mulai dari lima menit "
              "saja, sekadar merasakan apa yang sebenarnya sedang kamu rasakan tanpa menghakimi "
              "atau langsung mencari solusi. Latihan kecil ini membantumu membangun ketahanan "
              "terhadap ketidaknyamanan, sehingga kamu tidak selalu harus lari untuk merasa baik.",
        "domains": {
            "karir": "Kamu bersinar di pekerjaan yang dinamis dan penuh variasi, seperti bidang "
                     "kreatif, pengembangan bisnis, atau peran yang memungkinkanmu terus belajar "
                     "hal baru. Kamu jago melempar ide segar dan membawa energi positif ke dalam "
                     "tim. Tapi kamu bisa kesulitan di pekerjaan yang repetitif atau butuh fokus "
                     "jangka panjang pada satu proyek, karena rasa bosan datang lebih cepat "
                     "dibanding orang lain. Kamu juga rawan memulai banyak proyek sekaligus tanpa "
                     "sempat menyelesaikannya satu per satu. *PR: batasi dirimu hanya mengerjakan "
                     "maksimal dua proyek besar dalam satu waktu, dan tolak dulu ide baru sampai "
                     "salah satunya selesai.*",
            "asmara": "Kamu pasangan yang menyenangkan dan membawa banyak kegembiraan ke dalam "
                      "hubungan, selalu punya ide seru untuk dilakukan bersama. Tapi kamu bisa "
                      "menghindari percakapan berat atau konflik dengan mengalihkan suasana "
                      "menjadi lebih ringan, padahal beberapa hal justru perlu benar-benar "
                      "dibicarakan sampai selesai. Kamu juga rawan merasa gelisah kalau hubungan "
                      "terasa terlalu rutin, dan diam-diam mulai membayangkan opsi lain yang "
                      "lebih menarik. Pasangan mungkin merasa perlu kejelasan lebih soal "
                      "komitmenmu. *PR: saat konflik muncul, coba bertahan dalam percakapan itu "
                      "sampai selesai, alih-alih mengalihkannya dengan bercanda atau ganti "
                      "topik.*",
            "keuangan": "Kamu cenderung impulsif soal uang, terutama untuk hal-hal yang "
                        "berhubungan dengan pengalaman baru, seperti jalan-jalan, hobi baru, atau "
                        "barang yang sedang menarik perhatianmu saat itu. Kebiasaan ini membuat "
                        "hidupmu terasa penuh warna, tapi juga bisa bikin kondisi keuanganmu "
                        "kurang stabil kalau tidak diimbangi perencanaan. Kamu juga cenderung "
                        "menghindari memikirkan hal-hal serius seperti tabungan jangka panjang "
                        "karena terasa kurang seru. *PR: alokasikan sebagian penghasilan otomatis "
                        "ke tabungan sebelum uang itu sempat kamu pakai untuk hal-hal spontan.*",
            "kesehatan": "Energimu yang tinggi butuh disalurkan lewat aktivitas yang bervariasi, "
                         "dan kamu cenderung cepat bosan dengan rutinitas olahraga yang itu-itu "
                         "saja. Tapi kebiasaan menghindari rasa tidak nyaman bisa membuatmu "
                         "kurang peka terhadap sinyal tubuh yang sebenarnya butuh istirahat, "
                         "karena kamu lebih memilih terus bergerak dan sibuk. Kamu juga rawan "
                         "mengabaikan kebutuhan tidur yang cukup demi mengejar aktivitas lain "
                         "yang terasa lebih menarik. *PR: coba tetapkan jam tidur tetap, dan "
                         "perlakukan itu sebagai komitmen sepenting janji dengan orang lain.*",
        },
    },
    8: {
        "tagline": "Berdiri kokoh, siap melindungi apa yang penting.",
        "chip": "ENNEAGRAM",
        "title": "Tipe 8 — Sang Pelindung yang Tegas",
        "p1_label": "Siapa Kamu",
        "p1": "Kamu punya kekuatan alami untuk mengambil kendali dalam situasi yang tidak "
              "menentu, dan orang-orang di sekitarmu sering secara alami melihat ke arahmu saat "
              "keadaan mulai kacau. Sejak dulu, kamu mungkin belajar bahwa dunia bisa jadi tempat "
              "yang keras, sehingga kamu memilih untuk jadi kuat dan tegas daripada terlihat "
              "rentan. Di balik ketegasan itu, ada kekhawatiran yang cukup mendasar, yaitu takut "
              "dikendalikan atau dimanfaatkan oleh orang lain, sehingga kamu berusaha selalu "
              "punya kendali penuh atas hidup dan keputusanmu sendiri. Kamu bicara apa adanya dan "
              "tidak suka berbasa-basi, karena kamu menghargai kejujuran langsung dibanding "
              "kesopanan yang terasa palsu. Kamu juga punya insting kuat untuk melindungi orang-"
              "orang yang kamu sayangi, dan akan maju paling depan kalau ada yang mengancam mereka. "
              "Rasa keadilan dalam dirimu cukup kuat, kamu tidak suka melihat orang lemah "
              "diperlakukan semena-mena, dan sering jadi orang yang berani bersuara saat yang "
              "lain memilih diam. Orang-orang di sekitarmu biasanya merasa aman berada dekat "
              "denganmu, karena mereka tahu kamu akan berdiri di depan untuk melindungi mereka "
              "kalau dibutuhkan.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Ketegasan dan keberanianmu membuatmu jadi sosok pelindung yang bisa diandalkan "
              "saat situasi sulit, dan orang lain merasa lebih tenang tahu kamu ada di pihak "
              "mereka. Kamu juga jujur dan berani menyuarakan kebenaran meski itu tidak populer. "
              "Namun intensitasmu yang besar kadang membuat orang lain merasa gentar atau "
              "terintimidasi, meski itu bukan niatmu. Kamu juga bisa kesulitan menunjukkan sisi "
              "rentan atau mengakui butuh bantuan, karena itu terasa seperti kelemahan di "
              "matamu sendiri. Kecenderungan untuk selalu ingin memegang kendali kadang membuatmu "
              "sulit mempercayakan sesuatu ke orang lain, bahkan saat mereka sebenarnya mampu "
              "menanganinya.",
        "quote": "Kekuatan yang sesungguhnya juga termasuk keberanian untuk menunjukkan sisi "
                 "lembut, bukan hanya sisi tegasmu saja.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba latih dirimu untuk mengakui satu perasaan rentan ke orang yang kamu percaya, "
              "tanpa buru-buru menutupinya dengan ketegasan. Kamu bisa mulai dari hal kecil, "
              "seperti mengakui kamu sedang lelah atau butuh bantuan, alih-alih terus tampil "
              "kuat sendirian. Latihan ini bukan untuk membuatmu kehilangan kekuatanmu, tapi "
              "supaya orang di sekitarmu juga punya kesempatan menunjukkan dukungan mereka "
              "balik ke kamu. Semakin sering kamu melakukannya, semakin kamu sadar bahwa "
              "menunjukkan sisi rentan tidak membuatmu kehilangan kendali, justru memperkuat "
              "hubungan yang kamu miliki.",
        "domains": {
            "karir": "Kamu unggul di posisi kepemimpinan yang butuh keputusan cepat dan tegas, "
                     "seperti manajemen krisis, kewirausahaan, atau peran apa pun yang butuh "
                     "orang berani mengambil risiko dan bertanggung jawab penuh. Tim biasanya "
                     "merasa lebih terarah saat kamu yang memimpin. Tapi gaya komunikasimu yang "
                     "blak-blakan bisa terasa terlalu keras untuk sebagian orang, dan kamu bisa "
                     "kesulitan mendelegasikan tugas karena merasa harus mengendalikan semuanya "
                     "sendiri. Kamu juga rawan berbenturan dengan atasan yang punya gaya "
                     "kepemimpinan berbeda dari caramu. *PR: sebelum menyampaikan kritik ke tim, "
                     "coba lunakkan dulu cara penyampaiannya tanpa mengurangi ketegasan isi "
                     "pesannya.*",
            "asmara": "Kamu pasangan yang protektif dan setia, siap membela orang yang kamu "
                      "cintai tanpa ragu. Tapi kamu bisa kesulitan menunjukkan sisi lembut atau "
                      "mengakui kebutuhan emosionalmu sendiri, karena terbiasa jadi yang kuat "
                      "dalam hubungan. Kecenderungan untuk selalu memegang kendali juga bisa "
                      "membuat pasangan merasa kurang punya ruang untuk mengambil keputusan "
                      "bersama. Pasangan mungkin butuh waktu lebih untuk benar-benar melihat sisi "
                      "rapuhmu di balik ketegasan yang biasa kamu tunjukkan. *PR: coba biarkan "
                      "pasangan mengambil keputusan kecil dalam hubungan tanpa kamu ikut campur "
                      "atau mengoreksi.*",
            "keuangan": "Kamu cenderung berani mengambil keputusan finansial besar, termasuk "
                        "risiko dalam bisnis atau investasi, karena kamu percaya diri dengan "
                        "penilaianmu sendiri. Keberanian ini bisa membuahkan hasil besar, tapi "
                        "juga bisa berujung kerugian kalau kamu terlalu yakin tanpa "
                        "mempertimbangkan masukan orang lain. Kamu juga cenderung menggunakan "
                        "uang sebagai simbol kendali dan kemandirian, sehingga sulit menerima "
                        "bantuan finansial meski sebenarnya dibutuhkan. *PR: sebelum mengambil "
                        "keputusan finansial besar, coba minta pendapat satu orang yang kamu "
                        "percaya sebelum memutuskan sendiri.*",
            "kesehatan": "Energimu yang besar dan intens butuh penyaluran fisik yang setara, dan "
                         "kamu biasanya menikmati aktivitas yang menantang secara fisik. Tapi "
                         "kamu rawan mengabaikan sinyal tubuh yang butuh istirahat karena tidak "
                         "suka merasa lemah atau kalah oleh keterbatasan fisik sendiri. Kamu juga "
                         "cenderung memendam stres emosional daripada mengungkapkannya, yang "
                         "lama-lama bisa berubah jadi ketegangan fisik. *PR: kalau tubuh sudah "
                         "memberi sinyal lelah, coba benar-benar berhenti sejenak, alih-alih "
                         "memaksakan diri terus bergerak.*",
        },
    },
    9: {
        "tagline": "Air tenang yang tetap punya arus di dalamnya.",
        "chip": "ENNEAGRAM",
        "title": "Tipe 9 — Sang Penjaga Kedamaian yang Lembut",
        "p1_label": "Siapa Kamu",
        "p1": "Kamu punya kemampuan alami untuk membuat orang lain merasa nyaman dan diterima "
              "apa adanya, karena kamu jarang menghakimi dan lebih senang mencari titik temu "
              "daripada memperbesar perbedaan. Sejak dulu, kamu mungkin belajar bahwa menjaga "
              "suasana tetap tenang lebih mudah dilakukan daripada menyuarakan pendapat yang "
              "bisa memicu konflik, sehingga kamu terbiasa mengalah demi keharmonisan bersama. Di "
              "balik sikap tenangmu, ada kekhawatiran yang cukup dalam, yaitu takut kehilangan "
              "koneksi atau menyebabkan perpecahan, sehingga kamu sering meredam pendapat atau "
              "keinginanmu sendiri demi menjaga hubungan tetap baik-baik saja. Kamu punya "
              "kemampuan melihat sudut pandang banyak pihak sekaligus, membuatmu jadi penengah "
              "yang baik saat orang lain sedang berselisih. Kamu juga cenderung menghindari "
              "keputusan besar atau perubahan mendadak, karena itu terasa mengganggu rasa nyaman "
              "yang sudah kamu bangun. Orang-orang di sekitarmu biasanya merasa tenang dan aman "
              "berada di dekatmu, karena kamu jarang membuat suasana jadi tegang atau penuh "
              "drama. Namun di balik ketenangan itu, ada bagian dirimu yang sebenarnya punya "
              "banyak pendapat dan keinginan, hanya saja kamu sering memilih untuk tidak "
              "mengungkapkannya secara terbuka.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kemampuanmu menciptakan suasana damai dan menerima orang lain apa adanya membuat "
              "banyak orang merasa nyaman berada di dekatmu tanpa merasa dihakimi. Kamu juga "
              "pendengar yang baik dan bisa melihat berbagai sudut pandang sekaligus, membuatmu "
              "jadi sosok yang bijaksana dalam menengahi konflik. Namun kebiasaan menghindari "
              "konflik bisa membuatmu menumpuk kekesalan yang tidak pernah benar-benar "
              "tersampaikan, sampai suatu saat meledak tanpa disangka-sangka. Kamu juga rawan "
              "menunda keputusan penting karena berharap masalah akan selesai dengan sendirinya "
              "seiring waktu. Kecenderungan untuk mengikuti kemauan orang lain demi menjaga "
              "kedamaian kadang membuatmu kehilangan arah tentang apa yang sebenarnya kamu "
              "inginkan untuk dirimu sendiri.",
        "quote": "Kedamaian yang sesungguhnya bukan berarti tanpa suara, tapi berani "
                 "menyuarakan diri dengan tetap tenang.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba latih dirimu untuk menyampaikan satu pendapat kecil yang berbeda dari orang "
              "lain, meski itu berarti risiko sedikit ketegangan. Mulai dari hal sederhana, "
              "seperti memilih tempat makan sesuai keinginanmu sendiri, alih-alih selalu "
              "mengikuti pilihan orang lain. Perhatikan bahwa menyuarakan pendapat tidak selalu "
              "berujung konflik besar seperti yang mungkin kamu bayangkan. Latihan kecil ini "
              "membantumu perlahan percaya bahwa suaramu juga penting, dan hubungan yang sehat "
              "justru bisa bertahan meski ada perbedaan pendapat di dalamnya.",
        "domains": {
            "karir": "Kamu jadi perekat yang baik dalam tim, membantu menjaga suasana kerja tetap "
                     "harmonis dan menjadi penengah yang adil saat ada perselisihan antar rekan "
                     "kerja. Kamu juga bekerja dengan tenang dan konsisten tanpa banyak drama. "
                     "Tapi kamu bisa kesulitan menyuarakan pendapat sendiri dalam rapat, dan "
                     "sering setuju dengan ide orang lain meski sebenarnya punya pandangan "
                     "berbeda. Kamu juga rawan menunda pekerjaan yang terasa membosankan atau "
                     "kurang jelas prioritasnya. *PR: sebelum rapat, tuliskan dulu satu pendapatmu "
                     "sendiri di kertas, supaya kamu punya sesuatu yang siap disampaikan alih-alih "
                     "hanya mengikuti arus diskusi.*",
            "asmara": "Kamu pasangan yang sabar dan menerima, jarang membuat drama dan selalu "
                      "berusaha menjaga hubungan tetap tenang. Tapi kebiasaan mengalah demi "
                      "menghindari konflik bisa membuat kebutuhan dan keinginanmu sendiri jadi "
                      "terpinggirkan, sampai kamu sendiri lupa apa yang sebenarnya kamu mau dari "
                      "hubungan itu. Kamu juga cenderung menunda membicarakan masalah, berharap "
                      "semuanya membaik dengan sendirinya. Pasangan mungkin tidak sepenuhnya sadar "
                      "ada kekesalan yang sudah lama kamu pendam. *PR: pilih satu hal yang selama "
                      "ini mengganggumu dalam hubungan, lalu sampaikan langsung ke pasangan "
                      "dengan nada tenang, bukan dipendam lagi.*",
            "keuangan": "Kamu cenderung santai soal uang, jarang terlalu ambisius mengejar "
                        "kekayaan dan lebih memilih hidup yang stabil dan tidak banyak drama "
                        "finansial. Tapi sikap menghindari konflik ini juga bisa membuatmu malas "
                        "mengurus hal-hal penting seperti negosiasi gaji atau menagih uang yang "
                        "dipinjam orang lain. Kamu juga rawan menunda keputusan finansial besar "
                        "karena merasa terlalu ribet memikirkannya. *PR: tetapkan tanggal khusus "
                        "setiap bulan untuk mengecek dan mengurus urusan finansial, supaya tidak "
                        "terus ditunda tanpa batas.*",
            "kesehatan": "Ketenanganmu biasanya jadi kekuatan besar untuk kesehatan mental, kamu "
                         "jarang mudah panik atau stres berlebihan. Tapi kebiasaan memendam emosi "
                         "demi menghindari konflik bisa berubah jadi kelelahan yang tidak "
                         "kelihatan, dan kamu bisa jadi kurang peka terhadap kebutuhan fisikmu "
                         "sendiri karena terlalu fokus menjaga kenyamanan orang lain. Kamu juga "
                         "rawan jadi kurang aktif bergerak karena lebih nyaman berdiam di zona "
                         "yang sudah familiar. *PR: cari satu aktivitas fisik ringan yang bisa "
                         "kamu lakukan rutin, sekadar untuk menjaga tubuh tetap bergerak setiap "
                         "hari.*",
        },
    },
}
