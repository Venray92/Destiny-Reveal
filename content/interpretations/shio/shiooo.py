"""
Konten Shio (12 kategori).

Key dict ini HARUS sama persis dengan nilai "shio" dari engine/shio.py
(hitung_shio()["shio"]): Tikus, Kerbau, Macan, Kelinci, Naga, Ular, Kuda,
Kambing, Monyet, Ayam, Anjing, Babi.

Struktur tiap entri sama persis dengan DUMMY_RESULTS di views/revealpage.py.

REVISI (26 Sep 2026 malam): isi p1/p2/p3 diperpanjang 2-3x lipat dari versi
sebelumnya (per instruksi Stev), supaya laporannya terasa lebih bernilai
dan aplikatif, bukan cuma label singkat.
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
              "kamu jarang benar-benar kehabisan akal meski berada dalam keadaan sulit. Kecerdikan ini "
              "biasanya sudah kelihatan sejak kamu masih kecil, misalnya lewat kebiasaan mencari cara "
              "paling efisien untuk menyelesaikan tugas, bukan sekadar cara yang paling umum dilakukan "
              "orang lain. Di lingkungan kerja, kamu sering jadi orang yang dicari saat tim menghadapi "
              "masalah mendadak, karena kamu bisa berpikir cepat sambil tetap tenang. Dalam pergaulan, "
              "kelincahan berpikirmu membuatmu mudah menyesuaikan diri di berbagai kelompok, dari "
              "obrolan santai sampai diskusi yang serius sekalipun.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kecerdikan dan kepekaanmu terhadap peluang membuat orang lain sering meminta "
              "pendapatmu sebelum mengambil keputusan penting. Kamu juga cepat beradaptasi dengan "
              "keadaan baru. Namun kelincahan berpikir ini terkadang membuatmu terlalu berhati-hati "
              "atau curiga berlebihan, sampai sulit benar-benar percaya penuh pada orang lain. "
              "Kewaspadaan yang berlebihan ini bisa membuatmu menganalisis motif orang lain secara "
              "berlebihan, bahkan pada niat baik yang sebenarnya tulus, sehingga hubungan yang "
              "seharusnya bisa lebih dekat justru berhenti di permukaan saja. Kamu juga bisa terlalu "
              "sibuk memikirkan rencana cadangan, sampai lupa menikmati momen yang sedang berjalan.",
        "quote": "Kecerdikan akan membawamu jauh, tapi kepercayaan yang tulus akan membawamu lebih "
                 "jauh lagi.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba beri satu orang yang selama ini kamu ragukan kesempatan untuk membuktikan "
              "dirinya, tanpa langsung menilai dari kecurigaanmu. Mulailah dengan langkah kecil, "
              "misalnya mempercayakan satu tugas sederhana kepada orang tersebut dan melihat "
              "bagaimana hasilnya, sebelum menyimpulkan apa pun tentang niatnya. Latihan kecil ini "
              "akan membantumu membedakan mana kewaspadaan yang benar-benar dibutuhkan, dan mana yang "
              "sebenarnya hanya kebiasaan lama yang sudah tidak relevan lagi.",
        "domains": {
            "karir": "Di dunia kerja, kecerdikanmu adalah aset yang jarang dimiliki orang lain secara "
                     "alami. Kamu bisa melihat celah atau peluang di tempat yang orang lain anggap "
                     "jalan buntu, dan itu membuatmu cocok di peran yang menuntut solusi cepat atau "
                     "negosiasi yang lihai, seperti business development, marketing, atau posisi yang "
                     "butuh membaca situasi pasar dengan gesit. Atasan biasanya menghargaimu karena "
                     "kamu jarang kehabisan ide saat menghadapi masalah mendadak. Tantangannya, "
                     "kewaspadaan berlebihmu bisa membuatmu ragu mendelegasikan tugas, karena merasa "
                     "orang lain tidak akan mengerjakannya seteliti dirimu, dan ini bisa membuatmu "
                     "kelebihan beban kerja tanpa disadari. Kamu juga perlu hati-hati agar kecerdikan "
                     "tidak berubah jadi terlalu banyak jalan pintas yang mengorbankan kualitas jangka "
                     "panjang demi hasil instan. *PR: Latih delegasi satu tugas kecil ke rekan kerja "
                     "minggu ini, dan biarkan dia menyelesaikannya dengan caranya sendiri.*",
            "asmara": "Dalam hubungan asmara, kamu cenderung mengamati dulu sebelum benar-benar "
                      "membuka hati, karena naluri waspadamu juga bekerja di ranah perasaan. Kamu "
                      "ingin memastikan pasanganmu benar-benar tulus sebelum kamu berinvestasi penuh "
                      "secara emosional, dan proses ini kadang membuat pasangan merasa harus "
                      "membuktikan diri berulang-ulang. Kecerdikanmu juga bisa membuatmu pandai "
                      "membaca sinyal dari pasangan, seperti tahu kapan dia sedang tidak baik-baik "
                      "saja meski dia tidak bilang apa-apa. Namun kalau kewaspadaan ini kebablasan, "
                      "kamu bisa terus mencurigai motif pasangan bahkan saat tidak ada tanda-tanda "
                      "yang mencurigakan, dan itu bisa melelahkan hubungan dalam jangka panjang. "
                      "Kepercayaan yang kamu bangun pelan-pelan justru akan jauh lebih kuat kalau "
                      "kamu berani memberi ruang tanpa terus menguji. *PR: Sekali ini, coba percaya "
                      "penuh pada kata-kata pasanganmu tanpa mencari bukti tambahan.*",
            "keuangan": "Soal keuangan, kecerdikanmu membuatmu jago melihat peluang yang orang lain "
                        "lewatkan, entah itu diskon tersembunyi, cara menghemat, atau peluang usaha "
                        "sampingan yang belum banyak dilirik orang. Kamu juga cenderung punya rencana "
                        "cadangan untuk keuanganmu, tidak suka mengandalkan satu sumber penghasilan "
                        "saja. Sisi ini membuatmu relatif aman secara finansial dibanding kebanyakan "
                        "orang. Tapi kewaspadaan berlebih bisa membuatmu terlalu banyak menimbun uang "
                        "untuk skenario terburuk yang belum tentu terjadi, sampai jarang menikmati "
                        "hasil kerja kerasmu sendiri. Kamu juga perlu waspada terhadap kebiasaan "
                        "menghitung untung-rugi secara berlebihan dalam hal-hal kecil, yang justru "
                        "menghabiskan energi mental lebih banyak dari nilai uang yang dihemat. "
                        "*PR: Alokasikan satu pos kecil bulan ini khusus untuk menikmati sesuatu tanpa "
                        "rasa bersalah.*",
            "kesehatan": "Otakmu yang selalu aktif berpikir dan menganalisis bisa jadi pedang bermata "
                         "dua untuk kesehatanmu. Di satu sisi, kewaspadaanmu membuatmu cepat sadar "
                         "kalau ada yang tidak beres dengan tubuhmu dan segera mencari solusi. Di sisi "
                         "lain, pikiran yang terus bekerja bahkan saat seharusnya istirahat bisa "
                         "membuatmu susah tidur nyenyak atau gampang merasa cemas tanpa sebab yang "
                         "jelas. Kamu tipe yang sering memikirkan banyak kemungkinan sekaligus, "
                         "termasuk soal kesehatan, sehingga gejala kecil bisa terasa lebih menakutkan "
                         "di kepalamu daripada kenyataannya. Penting untukmu punya rutinitas yang benar-"
                         "benar mematikan mode 'berpikir' itu, entah lewat olahraga ringan, journaling, "
                         "atau sekadar diam tanpa gadget beberapa menit sehari. *PR: Coba teknik napas "
                         "dalam 5 menit sebelum tidur, tanpa memikirkan rencana besok.*",
        },
    },
    "Kerbau": {
        "tagline": "🐂 Shio Kerbau",
        "chip": "SHIO",
        "title": "Kerbau — Sosok Tekun yang Bisa Diandalkan",
        "p1_label": "Siapa Kamu",
        "p1": "Shio Kerbau melambangkan ketekunan, kejujuran, dan kerja keras yang konsisten. Kamu "
              "bukan tipe yang suka mencari jalan pintas; kamu lebih memilih menyelesaikan sesuatu "
              "langkah demi langkah sampai benar-benar tuntas. Orang-orang di sekitarmu tahu bahwa "
              "kata-katamu bisa dipegang, karena kamu jarang mengingkari janji. Dalam pekerjaan, "
              "ketekunanmu membuatmu unggul di tugas-tugas yang butuh waktu lama dan konsistensi "
              "tinggi, jenis pekerjaan yang membuat banyak orang lain menyerah di tengah jalan. Kamu "
              "juga jarang tergoda mengambil jalan pintas meski itu bisa mempercepat hasil, karena "
              "bagimu proses yang benar sama pentingnya dengan hasil akhirnya. Di lingkungan keluarga "
              "atau pertemanan, kamu adalah sosok yang selalu ada, sosok yang orang tahu pasti bisa "
              "diandalkan meski situasinya sedang sulit.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Keteguhan dan kejujuranmu membuat orang lain merasa aman bekerja sama denganmu dalam "
              "jangka panjang. Kamu juga tidak mudah goyah oleh tekanan atau opini orang lain. "
              "Sayangnya, keteguhan itu kadang berubah menjadi keras kepala, membuatmu sulit menerima "
              "cara pandang baru meski cara pandang itu sebenarnya lebih baik. Kekukuhan ini juga bisa "
              "membuatmu terjebak dalam cara lama yang sebenarnya sudah tidak lagi efektif, hanya "
              "karena itu cara yang sudah kamu kenal dan kuasai. Orang di sekitarmu mungkin merasa "
              "sungkan menyampaikan kritik atau masukan, karena tahu betapa sulitnya membuatmu berubah "
              "pikiran begitu keputusan sudah diambil.",
        "quote": "Keteguhan itu berharga, tapi kebesaran hati untuk berubah pikiran juga tanda "
                 "kekuatan.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba dengarkan satu pendapat yang berbeda dari caramu biasa melakukan "
              "sesuatu, dan pertimbangkan dengan pikiran terbuka sebelum menolaknya. Alih-alih "
              "langsung mempertahankan cara lamamu, coba tanyakan dulu alasan di balik pendapat "
              "berbeda itu, dan bandingkan hasilnya secara objektif. Kamu juga bisa mencoba satu kali "
              "melakukan sesuatu dengan cara baru dalam skala kecil, sebagai eksperimen, sebelum "
              "menilai apakah cara itu lebih baik atau tidak dari kebiasaanmu.",
        "domains": {
            "karir": "Dalam pekerjaan, kamu adalah tipe yang akan tetap ada mengerjakan sesuatu sampai "
                     "benar-benar tuntas, bahkan saat rekan-rekan lain sudah mulai kehilangan semangat "
                     "di tengah proyek panjang. Ini membuatmu jadi andalan untuk peran yang butuh "
                     "konsistensi dan ketahanan, seperti operasional, quality control, atau posisi "
                     "yang menuntut disiplin tinggi dalam jangka waktu lama. Atasan biasanya "
                     "mempercayaimu memegang tanggung jawab besar karena tahu kamu tidak akan lari "
                     "dari masalah. Tantangannya, kamu bisa terlalu lama bertahan di pekerjaan atau "
                     "cara kerja yang sebenarnya sudah tidak sehat untukmu, hanya karena merasa harus "
                     "loyal atau karena belum terbiasa dengan perubahan. Kamu juga perlu belajar bahwa "
                     "meminta kenaikan posisi atau gaji bukan berarti tidak tahu diri, tapi bagian wajar "
                     "dari mengakui kerja kerasmu sendiri. *PR: Coba ajukan satu hal yang selama ini "
                     "kamu pendam soal pekerjaanmu ke atasan minggu ini.*",
            "asmara": "Dalam hubungan, kesetiaanmu terasa jelas dan pasangan biasanya merasa aman "
                      "bersamamu karena kamu bukan tipe yang mudah tergoda berpindah hati. Kamu juga "
                      "menunjukkan cinta lewat tindakan nyata dan konsisten, bukan lewat kata-kata "
                      "manis yang berlebihan, dan itu justru jadi bentuk kepercayaan yang paling kuat "
                      "bagi orang yang benar-benar mengenalmu. Namun keteguhanmu bisa berubah jadi "
                      "kekakuan kalau pasangan butuh kamu beradaptasi dengan caranya, misalnya soal "
                      "cara berkomunikasi atau menyelesaikan konflik. Kamu cenderung merasa caramu "
                      "sendiri sudah benar, sehingga kompromi terasa seperti kekalahan, padahal "
                      "hubungan yang sehat butuh dua orang yang mau sama-sama menyesuaikan diri. "
                      "*PR: Tanyakan ke pasanganmu satu hal yang menurutnya bisa kamu perbaiki, dan "
                      "dengarkan tanpa langsung membela diri.*",
            "keuangan": "Soal uang, kamu adalah tipe yang paling bisa diandalkan untuk menabung secara "
                        "konsisten dan tidak mudah tergoda pengeluaran impulsif. Kamu percaya bahwa "
                        "kekayaan dibangun pelan-pelan lewat kerja keras dan kedisiplinan, bukan lewat "
                        "jalan pintas yang berisiko. Prinsip ini membuat kondisi finansialmu cenderung "
                        "stabil dalam jangka panjang dibanding kebanyakan orang. Namun kehati-hatianmu "
                        "yang berlebihan bisa membuatmu melewatkan peluang investasi yang sebenarnya "
                        "masuk akal, hanya karena terasa asing atau belum pernah kamu coba sebelumnya. "
                        "Kamu juga cenderung menunda menikmati hasil kerja kerasmu sendiri, terus "
                        "menabung untuk masa depan sampai lupa bahwa masa sekarang juga layak "
                        "dirayakan sesekali. *PR: Riset satu instrumen investasi baru minggu ini, "
                        "meski hanya sekadar untuk memahami cara kerjanya.*",
            "kesehatan": "Ketahanan fisik dan mentalmu biasanya cukup kuat, dan kamu jarang mengeluh "
                         "soal capek meski beban kerjamu berat. Sayangnya, kebiasaan ini bisa membuatmu "
                         "mengabaikan sinyal-sinyal awal kelelahan atau stres, karena kamu terbiasa "
                         "'tahan banting' dan menganggap istirahat sebagai sesuatu yang bisa ditunda "
                         "terus. Pola makan dan tidurmu juga bisa jadi kaku, kamu nyaman dengan "
                         "rutinitas yang sama setiap hari, yang bagus untuk konsistensi tapi kadang "
                         "membuatmu kurang fleksibel menyesuaikan pola hidup saat tubuh sebenarnya "
                         "butuh sesuatu yang berbeda. Penting untukmu belajar bahwa istirahat bukan "
                         "tanda kelemahan, tapi bagian dari menjaga daya tahan jangka panjang yang "
                         "selama ini jadi kekuatanmu. *PR: Jadwalkan satu hari penuh minggu ini khusus "
                         "untuk benar-benar istirahat tanpa merasa bersalah.*",
        },
    },
    "Macan": {
        "tagline": "🐯 Shio Macan",
        "chip": "SHIO",
        "title": "Macan — Pemberani yang Penuh Semangat",
        "p1_label": "Siapa Kamu",
        "p1": "Shio Macan dikenal sebagai simbol keberanian dan semangat juang yang besar. Kamu punya "
              "energi yang membuatmu tidak takut menghadapi tantangan, bahkan cenderung mencari "
              "tantangan itu sendiri. Kehadiranmu terasa penuh percaya diri, dan orang lain sering "
              "melihatmu sebagai sosok yang berani bertindak lebih dulu. Sejak muda, kamu mungkin "
              "sudah terbiasa mengambil risiko yang bagi orang lain terasa menakutkan, entah itu "
              "mencoba hal baru, membela pendapatmu di depan umum, atau memulai sesuatu tanpa jaminan "
              "keberhasilan. Di lingkungan kerja, energi ini membuatmu cocok mengisi peran yang butuh "
              "keputusan cepat dan keberanian mengambil tindakan, terutama saat orang lain masih ragu "
              "atau menunggu arahan. Karisma alami yang kamu miliki juga membuat orang lain "
              "cenderung mengikuti arahmu, bahkan tanpa kamu perlu memaksa.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Keberanian dan semangatmu membuat orang lain terdorong untuk ikut berani mengambil "
              "risiko yang sehat. Kamu juga punya kharisma alami yang membuat orang memperhatikanmu. "
              "Namun semangat yang menggebu itu kadang membuatmu bertindak terlalu impulsif, tanpa "
              "sempat memikirkan konsekuensi jangka panjangnya. Dorongan untuk selalu bertindak cepat "
              "ini bisa membuatmu melewatkan detail penting yang sebenarnya krusial, atau membuat "
              "keputusan besar hanya berdasarkan semangat sesaat. Di hubungan dengan orang lain, "
              "keberanianmu yang terlalu dominan kadang membuat orang di sekitarmu merasa tertinggal "
              "atau kesulitan mengimbangi langkahmu yang cepat.",
        "quote": "Keberanian yang matang tahu kapan harus menyerang dan kapan harus menunggu waktu "
                 "yang tepat.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Sebelum mengambil keputusan besar, coba beri jeda satu hari untuk "
              "memikirkannya ulang, alih-alih langsung bertindak seperti biasanya. Gunakan jeda itu "
              "untuk menuliskan kemungkinan terbaik dan terburuk dari keputusan itu, supaya kamu "
              "punya gambaran lebih lengkap sebelum melangkah. Kamu juga bisa melatih diri bertanya "
              "kepada satu orang yang kamu percaya sebelum mengambil keputusan besar, bukan untuk "
              "meminta izin, tapi untuk mendengar sudut pandang yang mungkin belum kamu "
              "pertimbangkan.",
        "domains": {
            "karir": "Di lingkungan kerja, keberanianmu membuatmu cocok mengambil peran yang butuh "
                     "inisiatif dan keputusan cepat, seperti memimpin proyek baru, membuka lini bisnis "
                     "yang belum pernah dicoba, atau tampil di depan saat situasi genting. Kamu tidak "
                     "takut mengambil tanggung jawab besar, dan energi ini sering menular ke tim, "
                     "membuat mereka ikut berani mengambil langkah yang tadinya terasa menakutkan. "
                     "Namun sisi impulsifmu bisa membuatmu mengambil keputusan besar tanpa "
                     "mempertimbangkan data atau masukan tim secara utuh, yang berisiko menimbulkan "
                     "masalah di kemudian hari. Kamu juga cenderung ingin semua berjalan sesuai "
                     "kecepatanmu, sampai lupa bahwa tidak semua orang punya ritme kerja yang sama, "
                     "dan itu bisa membuat rekan kerja merasa tertekan atau tertinggal. *PR: Sebelum "
                     "mengambil keputusan besar minggu ini, minta pendapat dua rekan kerja dulu.*",
            "asmara": "Dalam asmara, semangat dan kepercayaan dirimu membuatmu jadi sosok yang menarik "
                      "perhatian, kamu tidak ragu mengejar apa yang kamu mau, termasuk soal perasaan. "
                      "Pasanganmu biasanya merasa hidup jadi lebih penuh warna dan petualangan "
                      "bersamamu, karena kamu jarang membiarkan hubungan terasa monoton. Tapi "
                      "dominasimu dalam mengambil keputusan bisa membuat pasangan merasa pendapatnya "
                      "kurang didengar, terutama saat kamu sudah yakin dengan satu arah dan langsung "
                      "bergerak tanpa banyak diskusi. Kamu juga perlu waspada terhadap kecenderungan "
                      "bosan kalau hubungan terasa terlalu stabil dan tanpa tantangan, padahal "
                      "hubungan yang matang justru dibangun dari momen-momen tenang, bukan cuma dari "
                      "gairah yang menggebu. *PR: Tanyakan pendapat pasanganmu dulu sebelum mengambil "
                      "keputusan penting berikutnya dalam hubungan kalian.*",
            "keuangan": "Soal keuangan, keberanianmu membuatmu tidak takut mengambil risiko yang "
                        "sebenarnya bisa mendatangkan hasil besar, entah lewat usaha sendiri, investasi "
                        "yang agresif, atau peluang yang orang lain anggap terlalu berisiko. Kamu juga "
                        "punya keyakinan diri yang membuatmu percaya usahamu akan membuahkan hasil. "
                        "Namun dorongan untuk bertindak cepat tanpa perhitungan matang bisa membuatmu "
                        "mengambil keputusan finansial besar hanya berdasarkan semangat sesaat, tanpa "
                        "riset yang cukup. Kamu perlu belajar menahan diri sejenak sebelum "
                        "menandatangani sesuatu yang besar, karena keputusan finansial yang diambil "
                        "dalam kondisi terlalu bersemangat sering kali menyesatkan di kemudian hari. "
                        "*PR: Tunda satu keputusan finansial besar selama tiga hari sebelum benar-benar "
                        "memutuskannya.*",
            "kesehatan": "Energimu yang besar biasanya membuatmu jarang sakit dan cepat pulih kalau "
                         "sedang tidak fit, karena tubuhmu memang terbiasa aktif bergerak. Kamu juga "
                         "cenderung menikmati olahraga yang menantang adrenalin, bukan sekadar rutinitas "
                         "yang datar. Tapi semangatmu yang menggebu bisa membuatmu memaksakan diri "
                         "terlalu keras, entah dalam olahraga, pekerjaan, atau aktivitas lain, sampai "
                         "tubuh sebenarnya butuh jeda tapi kamu abaikan sinyalnya. Kamu juga tipe yang "
                         "kurang sabar menunggu proses penyembuhan kalau sedang cedera atau sakit, "
                         "ingin cepat kembali beraktivitas seperti biasa padahal tubuh belum sepenuhnya "
                         "siap. *PR: Kalau tubuhmu memberi sinyal lelah minggu ini, coba benar-benar "
                         "berhenti sejenak, bukan memaksakan diri lanjut.*",
        },
    },
    "Kelinci": {
        "tagline": "🐰 Shio Kelinci",
        "chip": "SHIO",
        "title": "Kelinci — Sosok Lembut yang Bijaksana",
        "p1_label": "Siapa Kamu",
        "p1": "Shio Kelinci melambangkan kelembutan, kehati-hatian, dan kebijaksanaan dalam bersikap. "
              "Kamu cenderung menghindari konflik dan lebih memilih menyelesaikan masalah dengan cara "
              "yang halus. Ketenanganmu membuat orang-orang di sekitarmu merasa nyaman, karena kamu "
              "jarang membuat suasana menjadi tegang tanpa alasan yang jelas. Dalam pergaulan, kamu "
              "biasanya jadi sosok yang menenangkan ketika suasana sedang panas, karena caramu bicara "
              "yang lembut jarang memancing amarah orang lain. Di tempat kerja, kehati-hatianmu "
              "membuatmu jarang membuat kesalahan yang tergesa-gesa, karena kamu selalu memastikan "
              "situasinya aman sebelum melangkah. Kamu juga cenderung punya selera yang halus dan "
              "menghargai keindahan, baik dalam cara berpakaian, menata ruang, maupun caramu memilih "
              "kata-kata saat berbicara dengan orang lain.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kehati-hatian dan kepekaanmu membuatmu jarang terjebak dalam keputusan gegabah. Kamu "
              "juga pandai menjaga hubungan baik dengan banyak orang. Namun kebiasaan menghindari "
              "konflik ini kadang membuatmu memendam ketidaknyamanan sendiri demi menjaga suasana "
              "tetap damai, sampai akhirnya kamu sendiri yang merasa terbebani. Kecenderungan untuk "
              "selalu mengalah demi kedamaian ini bisa membuat orang lain, tanpa mereka sadari, "
              "terbiasa mengambil keuntungan dari sikap lembutmu. Kamu juga bisa kehilangan kesempatan "
              "penting karena terlalu takut sikapmu akan dianggap terlalu memaksa atau mengganggu "
              "kenyamanan orang lain.",
        "quote": "Menjaga kedamaian itu baik, tapi bukan berarti kamu harus selalu mengalah pada "
                 "dirimu sendiri.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Ketika ada sesuatu yang mengganggumu, coba sampaikan dengan lembut kepada "
              "orang yang bersangkutan, alih-alih memilih diam demi menghindari konflik. Kamu bisa "
              "mulai dengan kalimat sederhana seperti \"aku sebenarnya kurang nyaman kalau...\", "
              "yang tetap terdengar lembut tapi jujur. Latih juga dirimu mengenali perbedaan antara "
              "konflik yang sehat, yang membantu hubungan jadi lebih jelas, dengan konflik yang "
              "benar-benar merusak, supaya kamu tidak menghindari semua bentuk ketidaksepakatan "
              "secara membabi buta.",
        "domains": {
            "karir": "Di tempat kerja, kehati-hatian dan seleramu yang halus membuatmu cocok di peran "
                     "yang butuh diplomasi dan estetika, seperti mediasi antar tim, desain, atau "
                     "posisi yang berhubungan langsung dengan klien yang sensitif. Kamu jarang membuat "
                     "suasana kerja jadi tegang, dan itu membuat rekan-rekan merasa nyaman berdiskusi "
                     "denganmu. Namun kecenderungan menghindari konflik ini bisa membuatmu enggan "
                     "menyampaikan ketidaksetujuan secara langsung ke atasan atau rekan kerja, sehingga "
                     "idemu yang sebenarnya bagus jadi tidak tersampaikan dengan maksimal. Kamu juga "
                     "berisiko dilewati untuk promosi karena dianggap terlalu 'aman' dan kurang "
                     "menonjolkan diri, padahal kemampuanmu sebenarnya setara atau lebih baik dari "
                     "rekan lain yang lebih vokal. *PR: Sampaikan satu ide atau pendapatmu secara "
                     "langsung dalam rapat berikutnya, tanpa menunggu ditanya dulu.*",
            "asmara": "Dalam hubungan, kelembutanmu membuat pasangan merasa sangat nyaman dan jarang "
                      "merasa terancam olehmu. Kamu juga pandai menciptakan suasana romantis yang "
                      "tenang, bukan yang dramatis, dan itu jadi kekuatan tersendiri buat pasangan yang "
                      "mencari ketenangan. Tapi kebiasaan menghindari konflik bisa membuatmu memendam "
                      "kekecewaan terhadap pasangan sampai menumpuk, dan ketika akhirnya meledak, "
                      "pasangan justru bingung karena selama ini kamu terlihat baik-baik saja. Kamu "
                      "juga perlu waspada terhadap kecenderungan mengalah terus-menerus demi menghindari "
                      "pertengkaran, sampai kebutuhanmu sendiri jarang benar-benar terpenuhi dalam "
                      "hubungan itu. *PR: Sampaikan satu hal yang selama ini mengganjal di hati ke "
                      "pasanganmu minggu ini, dengan cara yang lembut tapi jujur.*",
            "keuangan": "Soal keuangan, kehati-hatianmu membuatmu jarang terjebak pengeluaran impulsif "
                        "atau investasi berisiko tinggi yang tidak kamu pahami. Kamu juga punya selera "
                        "yang baik dalam memilih barang berkualitas yang tahan lama, dibanding membeli "
                        "banyak barang murah yang cepat rusak. Namun kecenderungan menghindari "
                        "ketidaknyamanan bisa membuatmu enggan bernegosiasi soal harga atau gaji, "
                        "karena merasa canggung atau takut dianggap terlalu menuntut. Ini bisa membuat "
                        "nilai finansialmu sebenarnya lebih rendah dari yang seharusnya kamu dapatkan. "
                        "Kamu juga cenderung menghindari topik keuangan yang sensitif dengan pasangan "
                        "atau keluarga, padahal keterbukaan soal ini justru penting untuk perencanaan "
                        "jangka panjang. *PR: Coba negosiasikan satu hal soal harga atau kompensasi "
                        "yang selama ini kamu hindari.*",
            "kesehatan": "Ketenanganmu secara alami membuat sistem tubuhmu relatif tidak mudah stres "
                         "berlebihan, dan kamu cenderung punya kebiasaan menjaga diri dengan cara yang "
                         "halus, seperti tidur cukup dan menjaga penampilan. Namun kebiasaan memendam "
                         "perasaan dan menghindari konflik bisa berdampak pada kesehatan secara diam-"
                         "diam, tekanan emosional yang tidak tersalurkan sering muncul sebagai keluhan "
                         "fisik seperti sakit kepala, gangguan pencernaan, atau kelelahan yang tidak "
                         "jelas sebabnya. Kamu perlu punya saluran yang sehat untuk melepaskan emosi "
                         "yang selama ini kamu simpan sendiri, entah lewat jurnal, olahraga, atau "
                         "bicara dengan orang yang benar-benar kamu percaya. *PR: Coba tuliskan satu "
                         "hal yang selama ini kamu pendam, tanpa perlu menunjukkannya ke siapa pun.*",
        },
    },
    "Naga": {
        "tagline": "🐉 Shio Naga",
        "chip": "SHIO",
        "title": "Naga — Sosok yang Sulit Diabaikan",
        "p1_label": "Siapa Kamu",
        "p1": "Dalam kepercayaan Tionghoa, shio Naga dianggap sebagai simbol keberuntungan dan "
              "kekuatan. Kamu punya aura yang membuat orang lain memperhatikanmu tanpa harus berusaha "
              "keras. Rasa percaya diri itu bukan sekadar tampilan luar, tapi tumbuh dari keyakinan "
              "bahwa kamu memang mampu mencapai hal-hal besar kalau diberi kesempatan. Sejak kecil, "
              "kamu mungkin sudah terbiasa jadi pusat perhatian, entah karena prestasi, cara "
              "bicaramu yang penuh keyakinan, atau sekadar kehadiranmu yang terasa berbeda dari orang "
              "kebanyakan. Dalam karier, energi ini membuatmu cocok mengisi peran-peran yang "
              "membutuhkan sosok yang bisa dipercaya untuk memimpin atau mewakili sebuah kelompok. "
              "Orang-orang cenderung mengingat pertemuan pertama denganmu, karena kesan yang kamu "
              "berikan biasanya cukup kuat dan sulit dilupakan begitu saja.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Ambisimu jarang setengah-setengah, dan itu yang membuat orang lain mempercayakan "
              "tanggung jawab besar padamu. Sayangnya, standar tinggi yang kamu pasang untuk diri "
              "sendiri kadang ikut dibebankan ke orang lain tanpa sadar, sehingga mereka bisa merasa "
              "tertekan berada di dekatmu kalau kamu tidak sedikit melunakkan cara menyampaikannya. "
              "Rasa percaya diri yang besar ini, kalau tidak diimbangi kerendahan hati, bisa membuat "
              "orang lain merasa tidak dihargai pendapatnya, karena merasa kamu selalu yakin bahwa "
              "caramu adalah yang paling benar. Kamu juga bisa kesulitan menerima kritik, karena "
              "terbiasa menjadi sosok yang dikagumi, bukan yang dikoreksi.",
        "quote": "Kekuatan yang sesungguhnya terlihat justru saat kamu memilih untuk lebih lembut.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba luangkan waktu untuk memuji usaha orang lain sebelum menunjukkan apa yang masih "
              "kurang. Kebiasaan kecil ini akan membuat orang-orang di sekitarmu merasa dihargai, "
              "bukan cuma dinilai dari hasil akhirnya saja. Latih juga dirimu menerima satu kritik "
              "kecil tanpa langsung membela diri, dengan cara mendengarkan sampai selesai dan "
              "bertanya \"apa maksudnya lebih lanjut?\" sebelum menanggapi. Kebiasaan ini akan "
              "membuat orang lain lebih berani jujur denganmu di masa depan.",
        "domains": {
            "karir": "Ambisi dan auramu yang kuat membuatmu cocok mengisi posisi kepemimpinan atau "
                     "peran yang membutuhkan sosok yang bisa dipercaya untuk mewakili sebuah tim. Kamu "
                     "punya visi besar dan berani mengejarnya tanpa setengah-setengah, dan itu sering "
                     "membuat orang lain terinspirasi ikut bekerja lebih keras di dekatmu. Namun standar "
                     "tinggi yang kamu pasang untuk dirimu sendiri bisa membuatmu tidak sabar dengan "
                     "rekan kerja yang lebih lambat atau punya cara kerja berbeda, sehingga kamu "
                     "berisiko dianggap terlalu dominan atau sulit diajak kompromi. Kamu juga perlu "
                     "waspada terhadap kebiasaan sulit menerima kritik dari atasan atau rekan kerja, "
                     "karena terbiasa jadi sosok yang dikagumi, bukan yang dikoreksi. *PR: Minta satu "
                     "masukan jujur dari rekan kerja soal caramu memimpin, lalu dengarkan sampai "
                     "selesai tanpa membela diri.*",
            "asmara": "Dalam asmara, karismamu membuatmu jarang kesulitan menarik perhatian, dan "
                      "pasanganmu biasanya bangga berada di sisimu karena kehadiranmu yang penuh "
                      "percaya diri. Kamu juga tipe yang berani berkomitmen kalau sudah yakin, tidak "
                      "setengah-setengah dalam mencintai. Tapi standar tinggi yang kamu terapkan ke "
                      "diri sendiri bisa ikut kamu bebankan ke pasangan tanpa sadar, membuatnya merasa "
                      "harus terus membuktikan diri layak bersamamu. Kamu juga bisa kesulitan meminta "
                      "maaf lebih dulu saat berselisih, karena merasa mengalah sama dengan kalah, "
                      "padahal dalam hubungan yang sehat, siapa yang meminta maaf lebih dulu bukan soal "
                      "menang atau kalah. *PR: Coba jadi yang pertama meminta maaf di perselisihan "
                      "kecil berikutnya, meski menurutmu kamu tidak sepenuhnya salah.*",
            "keuangan": "Soal keuangan, ambisimu membuatmu berani menargetkan hasil besar dan biasanya "
                        "kamu punya rencana jangka panjang yang jelas untuk mencapainya, entah lewat "
                        "karier, bisnis, atau investasi. Kamu tidak puas dengan hasil yang biasa-biasa "
                        "saja, dan dorongan ini sering membuahkan hasil finansial yang lebih baik "
                        "dibanding kebanyakan orang. Namun ambisi yang terlalu besar bisa membuatmu "
                        "mengambil risiko finansial yang sebenarnya di luar kemampuanmu, hanya demi "
                        "gengsi atau ingin terlihat sukses di mata orang lain. Kamu juga perlu waspada "
                        "terhadap gaya hidup yang mengikuti citra diri yang ingin kamu tunjukkan, "
                        "sampai pengeluaran untuk penampilan melebihi kebutuhan yang sebenarnya. "
                        "*PR: Evaluasi satu pengeluaran besar bulan ini, apakah itu benar-benar "
                        "kebutuhan atau sekadar menjaga gengsi.*",
            "kesehatan": "Energi dan rasa percaya dirimu biasanya membuatmu tampak selalu bugar dan "
                         "penuh semangat di mata orang lain. Kamu jarang mau terlihat lemah, dan ini "
                         "bisa membuatmu memaksakan diri tetap tampil prima meski sebenarnya tubuhmu "
                         "sedang butuh istirahat. Kebiasaan menahan diri untuk tidak terlihat rapuh ini "
                         "berisiko membuatmu menunda pergi ke dokter atau mengakui saat sesuatu terasa "
                         "tidak beres, sampai masalahnya jadi lebih besar dari seharusnya. Kamu juga "
                         "perlu belajar bahwa mengakui butuh bantuan atau istirahat bukan tanda "
                         "kelemahan, justru bagian dari menjaga kekuatan yang selama ini jadi identitas "
                         "dirimu. *PR: Kalau ada keluhan fisik yang kamu abaikan minggu-minggu ini, "
                         "coba periksakan diri sekarang, jangan ditunda lagi.*",
        },
    },
    "Ular": {
        "tagline": "🐍 Shio Ular",
        "chip": "SHIO",
        "title": "Ular — Pemikir Tajam yang Penuh Intuisi",
        "p1_label": "Siapa Kamu",
        "p1": "Shio Ular melambangkan kebijaksanaan, ketenangan, dan intuisi yang tajam. Kamu jarang "
              "bertindak tanpa perhitungan, dan lebih suka mengamati situasi dengan saksama sebelum "
              "mengambil langkah. Ketenangan luarmu sering membuat orang salah sangka bahwa kamu tidak "
              "peduli, padahal di dalam kamu sedang memikirkan segalanya dengan sangat detail. Kamu "
              "punya kebiasaan mengamati orang lain sebelum benar-benar terbuka, dan biasanya butuh "
              "waktu cukup lama sebelum kamu benar-benar mempercayai seseorang sepenuhnya. Dalam "
              "pekerjaan, ketajaman analisismu membuatmu unggul dalam melihat pola atau risiko yang "
              "belum disadari orang lain, sehingga kamu sering jadi orang yang diandalkan untuk "
              "memikirkan strategi jangka panjang. Kamu juga cenderung nyaman menghabiskan waktu "
              "sendiri untuk merenung, dan tidak selalu butuh keramaian untuk merasa baik-baik saja.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Ketajaman berpikir dan intuisimu membuatmu jarang terkecoh oleh hal-hal yang terlihat "
              "di permukaan. Kamu juga bisa tetap tenang dalam situasi yang membuat orang lain panik. "
              "Namun kecenderungan untuk menyimpan pemikiran sendiri ini kadang membuat orang lain "
              "kesulitan menebak apa yang sebenarnya kamu rasakan atau inginkan. Kebiasaan menjaga "
              "jarak emosional ini bisa membuat hubungan dekatmu terasa dingin di mata orang lain, "
              "meski sebenarnya kamu peduli. Orang-orang di sekitarmu mungkin sering merasa tidak "
              "yakin apakah mereka benar-benar dekat denganmu, karena kamu jarang membagikan apa yang "
              "sebenarnya ada di pikiranmu.",
        "quote": "Ketenangan yang bijak akan lebih bermakna kalau sesekali dibagikan, bukan hanya "
                 "disimpan sendiri.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba sampaikan satu pemikiran atau analisismu secara terbuka kepada orang terdekat, "
              "alih-alih hanya memendamnya dalam kepala. Mulailah dari topik yang terasa aman, "
              "misalnya pendapatmu tentang sesuatu yang sedang terjadi, sebelum melangkah ke "
              "perasaan yang lebih personal. Ingat bahwa keterbukaan sedikit demi sedikit tidak akan "
              "mengurangi ketenanganmu, justru bisa membuat orang lain merasa lebih dekat dan "
              "dipercaya olehmu.",
        "domains": {
            "karir": "Ketajaman analisismu adalah senjata utama di dunia kerja, kamu bisa melihat "
                     "risiko atau pola yang belum disadari orang lain jauh sebelum masalah itu benar-"
                     "benar muncul. Ini membuatmu cocok di peran strategi, riset, atau posisi yang "
                     "butuh pemikiran jangka panjang dan ketenangan dalam mengambil keputusan. Rekan "
                     "kerja mungkin sulit menebak isi kepalamu, tapi mereka tahu keputusanmu biasanya "
                     "sudah dipikirkan matang-matang. Tantangannya, kebiasaan menyimpan pemikiran "
                     "sendiri bisa membuat tim kesulitan memahami arah pikiranmu, sehingga kolaborasi "
                     "terasa kurang lancar meski idemu sebenarnya bagus. Kamu juga cenderung kurang "
                     "vokal mempromosikan pencapaianmu sendiri, sampai kontribusimu kurang terlihat "
                     "dibanding rekan yang lebih terbuka. *PR: Bagikan satu insight atau analisismu "
                     "secara terbuka di rapat tim minggu ini, bukan hanya menyimpannya sendiri.*",
            "asmara": "Dalam asmara, intuisimu yang tajam membuatmu jarang salah menilai karakter "
                      "pasangan, kamu bisa merasakan ketulusan atau kepura-puraan seseorang jauh "
                      "sebelum orang lain menyadarinya. Kamu juga tipe yang setia sekali sudah "
                      "berkomitmen, meski butuh waktu lama untuk sampai ke titik itu. Namun kebiasaan "
                      "menjaga jarak emosional bisa membuat pasangan merasa tidak pernah benar-benar "
                      "mengenalmu sepenuhnya, meski sudah lama bersama. Ketenangan luarmu yang jarang "
                      "menunjukkan emosi juga bisa disalahartikan sebagai ketidakpedulian, padahal "
                      "kamu sebenarnya sangat memperhatikan dari dalam. Pasangan butuh sesekali melihat "
                      "sisi rentanmu untuk merasa benar-benar dekat. *PR: Ceritakan satu perasaan yang "
                      "biasanya kamu simpan sendiri kepada pasanganmu minggu ini.*",
            "keuangan": "Soal keuangan, ketajaman analisismu membuatmu jago membaca peluang dan risiko "
                        "sebelum mengambil keputusan finansial, kamu jarang tergoda investasi yang "
                        "terlihat menggiurkan di permukaan tapi sebenarnya berisiko tinggi. Kamu lebih "
                        "suka riset mendalam dulu sebelum benar-benar menaruh uang di sesuatu. Namun "
                        "kehati-hatian ini kadang berubah jadi terlalu banyak analisis sampai "
                        "kehilangan momentum, peluang bagus yang sebenarnya sudah cukup jelas bisa "
                        "terlewat karena kamu masih terus mempertimbangkan. Kamu juga cenderung tidak "
                        "membicarakan rencana keuangan dengan orang terdekat, padahal masukan dari "
                        "sudut pandang lain kadang membantu melengkapi analisismu sendiri. *PR: "
                        "Diskusikan satu rencana finansialmu dengan orang yang kamu percaya minggu "
                        "ini.*",
            "kesehatan": "Ketenanganmu secara alami adalah modal besar untuk kesehatan mental, kamu "
                         "jarang panik berlebihan menghadapi tekanan. Namun kebiasaan memendam segala "
                         "sesuatu di dalam kepala tanpa membaginya bisa jadi beban tersembunyi yang "
                         "lama-lama menumpuk jadi stres kronis, meski dari luar kamu terlihat baik-baik "
                         "saja. Kamu juga cenderung lebih nyaman menyendiri untuk memulihkan energi, "
                         "yang sebenarnya sehat, tapi perlu diimbangi dengan interaksi sosial yang "
                         "cukup supaya tidak terlalu terisolasi. Sesekali pikiranmu yang terus bekerja "
                         "menganalisis segala hal juga bisa membuatmu susah benar-benar rileks, bahkan "
                         "saat sedang beristirahat. *PR: Coba lakukan satu aktivitas fisik yang membuat "
                         "pikiranmu benar-benar berhenti menganalisis, seperti jalan kaki tanpa "
                         "tujuan.*",
        },
    },
    "Kuda": {
        "tagline": "🐴 Shio Kuda",
        "chip": "SHIO",
        "title": "Kuda — Jiwa Bebas yang Energik",
        "p1_label": "Siapa Kamu",
        "p1": "Shio Kuda dikenal sebagai simbol kebebasan, semangat, dan energi yang tidak pernah "
              "habis. Kamu suka bergerak, mencoba hal baru, dan tidak betah terlalu lama terjebak "
              "dalam rutinitas yang membosankan. Semangatmu yang tinggi sering menular ke orang-orang "
              "di sekitarmu, membuat suasana jadi lebih hidup. Kamu biasanya tidak nyaman kalau harus "
              "duduk diam terlalu lama tanpa aktivitas, dan selalu mencari cara untuk membuat harimu "
              "terasa lebih dinamis, entah lewat pekerjaan, hobi, atau sekadar jalan-jalan tanpa "
              "rencana pasti. Dalam pergaulan, energimu yang positif membuat orang lain senang "
              "diajak berkegiatan bersamamu, karena kamu jarang membuat suasana terasa berat atau "
              "membosankan. Di tempat kerja, kamu cenderung lebih bersemangat mengerjakan proyek yang "
              "bervariasi dibanding tugas yang berulang dan monoton.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Energi dan semangat petualanganmu membuat orang lain terinspirasi untuk keluar dari "
              "rutinitas mereka juga. Kamu juga mudah bergaul dengan berbagai kalangan. Namun "
              "kebebasan yang kamu junjung tinggi ini kadang membuatmu sulit berkomitmen pada satu "
              "hal dalam jangka panjang, karena selalu ada godaan untuk mencoba yang baru. "
              "Kecenderungan berpindah dari satu hal ke hal lain ini bisa membuat beberapa "
              "rencana besarmu tidak pernah benar-benar selesai, karena perhatianmu sudah teralihkan "
              "ke sesuatu yang lebih menarik. Dalam hubungan, sikap ini juga bisa membuat pasangan "
              "atau sahabat merasa tidak yakin seberapa jauh mereka bisa mengandalkan komitmenmu.",
        "quote": "Kebebasan sejati justru terasa lebih utuh ketika kamu berani berkomitmen pada apa "
                 "yang benar-benar penting.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Pilih satu komitmen yang sudah kamu buat, lalu jaga konsistensinya "
              "tanpa tergoda beralih ke hal baru yang lain. Untuk membantu, coba tuliskan alasan awal "
              "kenapa kamu memilih komitmen itu, dan baca ulang setiap kali godaan untuk berpindah "
              "muncul. Kamu juga bisa memberi dirimu penghargaan kecil setiap kali berhasil bertahan "
              "satu tahap penuh, supaya konsistensi terasa menyenangkan, bukan sekadar kewajiban.",
        "domains": {
            "karir": "Semangat dan fleksibilitasmu membuatmu cocok di pekerjaan yang penuh variasi dan "
                     "dinamika, seperti event organizer, sales lapangan, atau peran yang mengharuskanmu "
                     "berpindah tempat dan bertemu banyak orang baru. Kamu cepat beradaptasi dengan "
                     "lingkungan baru dan jarang merasa canggung di situasi yang asing. Namun "
                     "kecenderunganmu mudah bosan bisa membuatmu berpindah pekerjaan atau proyek "
                     "terlalu sering sebelum benar-benar menuai hasil dari yang sedang kamu kerjakan. "
                     "Rekam jejak yang terlihat 'loncat-loncat' ini bisa membuat orang lain ragu "
                     "mempercayakan tanggung jawab jangka panjang padamu, meski sebenarnya kamu punya "
                     "kemampuan yang cukup untuk itu. *PR: Pilih satu proyek yang sedang berjalan, dan "
                     "komit menyelesaikannya sampai tuntas sebelum memulai yang baru.*",
            "asmara": "Dalam asmara, energi positifmu membuat hubungan terasa seru dan penuh "
                      "kejutan, pasanganmu jarang merasa bosan karena kamu selalu punya ide aktivitas "
                      "baru. Kamu juga tipe yang terbuka dan jujur soal apa yang kamu rasakan, tidak "
                      "suka menyimpan drama berkepanjangan. Namun rasa takut terjebak dalam rutinitas "
                      "bisa membuatmu ragu berkomitmen serius, karena merasa komitmen sama dengan "
                      "kehilangan kebebasan. Pasangan mungkin merasa tidak yakin seberapa jauh mereka "
                      "bisa mengandalkanmu untuk jangka panjang, terutama kalau kamu sering "
                      "menghindari pembicaraan soal masa depan hubungan. *PR: Ajak pasanganmu bicara "
                      "terbuka soal satu rencana jangka panjang, tanpa menghindar seperti biasanya.*",
            "keuangan": "Soal uang, sifat spontanmu membuatmu tidak ragu mengeluarkan uang untuk "
                        "pengalaman baru, entah itu jalan-jalan, hobi, atau mencoba sesuatu yang belum "
                        "pernah kamu lakukan. Kamu percaya hidup harus dinikmati, bukan cuma ditabung "
                        "untuk masa depan yang belum pasti. Namun kebiasaan ini bisa membuat "
                        "tabunganmu jarang benar-benar bertambah, karena begitu ada uang lebih, "
                        "dorongan untuk segera menggunakannya untuk hal baru selalu muncul. Kamu perlu "
                        "sistem yang membuat menabung terasa otomatis, karena kalau mengandalkan niat "
                        "semata, godaan untuk membelanjakannya biasanya menang. *PR: Buat rekening "
                        "tabungan terpisah yang auto-debet setiap gajian, supaya kamu tidak sempat "
                        "tergoda memakainya.*",
            "kesehatan": "Energimu yang tinggi membuatmu jarang diam, dan itu bagus untuk kebugaran "
                         "fisik karena tubuhmu terbiasa aktif bergerak. Kamu juga cenderung cepat "
                         "bosan dengan rutinitas olahraga yang monoton, jadi olahraga yang bervariasi "
                         "atau berkelompok biasanya lebih cocok buatmu dibanding rutin sendirian. "
                         "Namun gaya hidupmu yang serba cepat dan berpindah-pindah bisa membuat pola "
                         "makan dan tidurmu jadi tidak teratur, kamu mungkin sering melewatkan waktu "
                         "makan atau begadang karena terlalu asyik dengan aktivitas baru. Ketidaktetapan "
                         "jadwal ini, kalau dibiarkan terus, bisa berdampak ke stamina jangka "
                         "panjangmu. *PR: Coba tetapkan satu jam tidur yang konsisten selama seminggu "
                         "ke depan, meski hari-harimu terasa berbeda-beda.*",
        },
    },
    "Kambing": {
        "tagline": "🐐 Shio Kambing",
        "chip": "SHIO",
        "title": "Kambing — Jiwa Lembut yang Penuh Empati",
        "p1_label": "Siapa Kamu",
        "p1": "Shio Kambing melambangkan kelembutan hati, kreativitas, dan kepedulian yang tulus "
              "terhadap orang lain. Kamu punya sisi artistik dan suka menciptakan suasana yang nyaman "
              "di sekitarmu. Kepekaanmu terhadap perasaan orang lain membuatmu sering jadi tempat "
              "curhat yang dipercaya banyak teman. Kamu biasanya punya cara pandang yang lembut "
              "terhadap dunia, dan lebih tertarik menciptakan sesuatu yang indah atau menenangkan "
              "dibanding bersaing secara langsung dengan orang lain. Dalam lingkungan sosial, kamu "
              "sering jadi sosok yang membuat orang lain merasa diterima apa adanya, tanpa banyak "
              "dihakimi. Sisi kreatifmu juga sering muncul dalam hal-hal sehari-hari, seperti caramu "
              "menata ruangan, memilih pakaian, atau menciptakan suasana hangat dalam sebuah "
              "pertemuan.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kepedulian dan kreativitasmu membuat orang lain merasa nyaman dan dihargai saat "
              "bersamamu. Kamu juga punya kemampuan menciptakan hal-hal indah dari sudut pandang yang "
              "berbeda. Namun kelembutan hati ini kadang membuatmu terlalu bergantung pada validasi "
              "atau persetujuan orang lain sebelum merasa yakin dengan pilihanmu sendiri. Kebutuhan "
              "akan persetujuan ini bisa membuatmu ragu mengambil keputusan penting tanpa mendengar "
              "banyak pendapat orang lain terlebih dulu, bahkan untuk hal-hal yang sebenarnya kamu "
              "sendiri sudah tahu jawabannya. Kamu juga bisa jadi terlalu sensitif terhadap kritik, "
              "sampai kritik kecil terasa seperti penolakan besar terhadap dirimu secara keseluruhan.",
        "quote": "Pendapat orang lain penting, tapi keyakinanmu pada dirimu sendiri jauh lebih "
                 "penting lagi.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba ambil satu keputusan kecil berdasarkan penilaianmu sendiri, tanpa "
              "meminta persetujuan orang lain terlebih dulu. Latih kepercayaan ini dengan cara "
              "bertahap, mulai dari keputusan yang risikonya kecil seperti memilih tempat makan, "
              "sampai akhirnya kamu terbiasa mempercayai penilaianmu sendiri untuk hal-hal yang lebih "
              "besar. Ingatkan juga dirimu bahwa kritik terhadap satu keputusan bukan berarti "
              "penolakan terhadap dirimu secara keseluruhan.",
        "domains": {
            "karir": "Sisi kreatif dan empatimu membuatmu cocok di pekerjaan yang melibatkan seni, "
                     "desain, konten, atau bidang apa pun yang butuh sentuhan personal dan kepekaan "
                     "rasa. Kamu juga jago menciptakan suasana kerja yang nyaman, dan rekan-rekan "
                     "senang berkolaborasi denganmu karena kamu jarang membuat suasana jadi kaku atau "
                     "kompetitif secara berlebihan. Namun kebutuhan akan validasi bisa membuatmu ragu "
                     "mengajukan ide sendiri sebelum yakin orang lain akan menyukainya, sehingga "
                     "kontribusimu yang sebenarnya berharga jadi tertahan. Kamu juga cenderung sulit "
                     "bersaing secara terang-terangan untuk promosi atau pengakuan, karena merasa "
                     "canggung menonjolkan diri sendiri. *PR: Ajukan satu ide kreatifmu di tempat kerja "
                     "tanpa menunggu validasi orang lain lebih dulu.*",
            "asmara": "Dalam hubungan, kelembutan dan empatimu membuat pasangan merasa benar-benar "
                      "dipahami, kamu peka terhadap perasaan mereka bahkan sebelum mereka "
                      "mengungkapkannya. Kamu juga suka menciptakan momen-momen romantis yang penuh "
                      "perhatian pada detail kecil. Namun kebutuhan akan persetujuan bisa membuatmu "
                      "terlalu sering mengesampingkan keinginanmu sendiri demi menyenangkan pasangan, "
                      "sampai kebutuhanmu sendiri jarang benar-benar tersampaikan. Kamu juga bisa "
                      "sangat terpukul oleh kritik kecil dari pasangan, menganggapnya sebagai tanda "
                      "hubungan sedang bermasalah, padahal belum tentu demikian. *PR: Sampaikan satu "
                      "keinginanmu sendiri ke pasangan minggu ini, tanpa dibungkus permintaan maaf "
                      "berlebihan.*",
            "keuangan": "Soal keuangan, seleramu yang halus membuatmu cenderung tertarik membelanjakan "
                        "uang untuk hal-hal yang indah atau berkualitas, entah itu barang seni, "
                        "dekorasi, atau pengalaman yang estetis. Kamu menghargai keindahan lebih dari "
                        "sekadar fungsi semata. Namun kebutuhan validasi sosial bisa membuatmu "
                        "membelanjakan uang untuk mengikuti standar orang lain, entah demi terlihat "
                        "mapan atau supaya diterima di lingkungan tertentu, meski itu sebenarnya di "
                        "luar kemampuanmu. Kamu juga cenderung ragu menegosiasikan harga atau meminta "
                        "kompensasi yang layak, karena tidak nyaman terlihat terlalu menuntut. *PR: "
                        "Buat anggaran khusus untuk hal-hal estetis yang kamu suka, supaya "
                        "pengeluaranmu lebih terkontrol tanpa harus merasa bersalah.*",
            "kesehatan": "Kepekaanmu terhadap suasana membuatmu mudah terpengaruh energi di sekitarmu, "
                         "kalau lingkunganmu penuh tekanan atau konflik, kamu bisa ikut merasa lelah "
                         "secara emosional meski masalahnya bukan langsung soal dirimu. Kamu butuh "
                         "ruang yang tenang dan indah untuk memulihkan energi, dan ini bukan sesuatu "
                         "yang boleh kamu anggap remeh. Kebiasaan terlalu memikirkan pendapat orang "
                         "lain juga bisa memicu kecemasan berlebihan, terutama saat merasa dinilai "
                         "atau dikritik. Penting untukmu punya ruang atau aktivitas kreatif sebagai "
                         "pelarian yang sehat dari tekanan sosial yang kamu rasakan. *PR: Sisihkan "
                         "waktu untuk satu aktivitas kreatif minggu ini, khusus untuk dirimu sendiri, "
                         "tanpa tujuan menyenangkan orang lain.*",
        },
    },
    "Monyet": {
        "tagline": "🐒 Shio Monyet",
        "chip": "SHIO",
        "title": "Monyet — Si Cerdas yang Penuh Ide",
        "p1_label": "Siapa Kamu",
        "p1": "Shio Monyet dikenal sebagai simbol kecerdasan, kelincahan, dan kemampuan memecahkan "
              "masalah dengan cara-cara kreatif. Kamu cepat menangkap pola dan sering menemukan solusi "
              "yang tidak terpikirkan orang lain. Rasa humor dan keluwesanmu membuat orang-orang di "
              "sekitarmu merasa senang berada di dekatmu. Kamu biasanya punya banyak ide sekaligus, "
              "dan senang menghubungkan hal-hal yang sekilas tidak berkaitan menjadi solusi yang unik. "
              "Di lingkungan kerja, kemampuan ini membuatmu cocok mengisi peran yang butuh "
              "fleksibilitas dan pemikiran cepat, terutama saat menghadapi masalah yang belum pernah "
              "ditemui sebelumnya. Dalam pergaulan, kamu adalah tipe orang yang bisa mencairkan "
              "suasana kaku hanya dengan satu candaan yang tepat waktu, membuat orang lain merasa "
              "lebih rileks berada di sekitarmu.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kecerdasan dan kreativitasmu membuat orang lain sering meminta pendapatmu ketika "
              "menghadapi masalah yang rumit. Kamu juga pandai mencairkan suasana yang tegang. Namun "
              "kelincahan berpikir ini kadang membuatmu mudah bosan dan terlalu banyak mengambil "
              "peran sekaligus, sampai tidak ada satu pun yang benar-benar kamu dalami sepenuhnya. "
              "Kecenderungan untuk selalu mencari hal baru yang menantang otakmu ini bisa membuatmu "
              "kehilangan minat di tengah jalan, tepat ketika sebuah proyek sebenarnya butuh "
              "ketekunan untuk benar-benar selesai. Orang lain mungkin melihatmu sebagai sosok yang "
              "penuh ide tapi kurang tuntas dalam eksekusi.",
        "quote": "Kecerdasan akan lebih terasa hasilnya kalau difokuskan pada satu arah dalam satu "
                 "waktu.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba kurangi jumlah hal yang kamu kerjakan sekaligus, dan fokuskan energi "
              "pada satu atau dua hal yang paling penting bagimu. Buat daftar prioritas sederhana "
              "di awal minggu, dan latih dirimu menahan godaan untuk memulai ide baru sebelum salah "
              "satu dari prioritas itu benar-benar selesai. Rasakan bagaimana hasil kerjamu terasa "
              "lebih dalam dan memuaskan ketika kamu benar-benar fokus, dibanding saat energimu "
              "terbagi ke banyak arah sekaligus.",
        "domains": {
            "karir": "Kreativitas dan kelincahan berpikirmu membuatmu cocok di pekerjaan yang dinamis "
                     "dan penuh tantangan baru, seperti inovasi produk, konsultasi, atau peran yang "
                     "butuh solusi kreatif untuk masalah yang belum pernah ditemui sebelumnya. Kamu "
                     "cepat belajar hal baru dan jarang kehabisan ide segar untuk ditawarkan ke tim. "
                     "Namun kecenderungan mudah bosan bisa membuatmu mengambil terlalu banyak proyek "
                     "sekaligus, sehingga kualitas eksekusi jadi korban karena perhatianmu terpecah. "
                     "Rekan kerja mungkin melihatmu sebagai sosok penuh ide tapi kurang bisa "
                     "diandalkan untuk menyelesaikan sesuatu sampai tuntas, dan ini bisa merugikan "
                     "reputasimu dalam jangka panjang. *PR: Selesaikan satu proyek yang sudah lama "
                     "tertunda sebelum menerima tanggung jawab baru apa pun.*",
            "asmara": "Dalam asmara, humor dan keluwesanmu membuat hubungan terasa menyenangkan dan "
                      "jarang membosankan, pasanganmu pasti sering tertawa karena caramu melihat "
                      "sesuatu dari sudut pandang yang unik. Kamu juga fleksibel dan mudah menyesuaikan "
                      "diri dengan kebiasaan pasangan. Namun kelincahan pikiranmu bisa membuatmu sulit "
                      "benar-benar hadir secara emosional dalam momen serius, kamu cenderung mengalihkan "
                      "pembicaraan berat dengan candaan, yang kadang membuat pasangan merasa "
                      "perasaannya tidak ditanggapi secara serius. Kamu juga perlu waspada terhadap "
                      "godaan untuk selalu mencari yang 'lebih menarik', bahkan saat hubunganmu "
                      "sekarang sebenarnya sudah baik. *PR: Saat pasanganmu membicarakan sesuatu yang "
                      "serius minggu ini, dengarkan tanpa membelokkannya jadi candaan.*",
            "keuangan": "Soal keuangan, kecerdikanmu membuatmu pandai melihat berbagai peluang "
                        "penghasilan sekaligus, entah lewat pekerjaan utama, proyek sampingan, atau "
                        "ide bisnis kreatif yang belum banyak dipikirkan orang lain. Namun kebiasaan "
                        "mencoba banyak hal sekaligus bisa membuat sumber dayamu, baik waktu maupun "
                        "uang, terlalu terbagi ke banyak arah tanpa ada yang benar-benar dikembangkan "
                        "maksimal. Kamu juga cenderung mudah tergoda peluang baru yang terlihat "
                        "menjanjikan, sampai lupa menuntaskan komitmen finansial yang sudah kamu mulai "
                        "sebelumnya. *PR: Pilih satu sumber penghasilan tambahan untuk benar-benar "
                        "difokuskan bulan ini, dan tunda ide-ide lain dulu.*",
            "kesehatan": "Pikiranmu yang selalu aktif dan penuh ide membuatmu jarang merasa bosan, "
                         "tapi juga bisa membuat kepalamu sulit benar-benar istirahat, bahkan saat "
                         "tubuhmu sedang tidak melakukan apa-apa, otakmu tetap sibuk memikirkan ide "
                         "baru. Ini bisa berdampak pada kualitas tidur dan membuatmu gampang merasa "
                         "gelisah tanpa sebab yang jelas. Kamu juga cenderung melompat dari satu "
                         "rutinitas kesehatan ke rutinitas lain, mencoba diet atau olahraga baru "
                         "sebelum benar-benar melihat hasil dari yang sebelumnya. Konsistensi kecil "
                         "justru akan memberi hasil yang lebih nyata dibanding terus berganti metode. "
                         "*PR: Pilih satu rutinitas kesehatan sederhana dan jalani konsisten selama "
                         "dua minggu penuh tanpa berganti.*",
        },
    },
    "Ayam": {
        "tagline": "🐓 Shio Ayam",
        "chip": "SHIO",
        "title": "Ayam — Sosok Rapi yang Percaya Diri",
        "p1_label": "Siapa Kamu",
        "p1": "Shio Ayam melambangkan ketelitian, kerapian, dan kepercayaan diri yang kuat. Kamu suka "
              "semua hal tertata dengan baik, mulai dari pekerjaan sampai penampilan sehari-hari. "
              "Kejujuranmu yang blak-blakan membuat orang lain tahu persis pendapatmu tentang sesuatu, "
              "tanpa perlu menebak-nebak lebih dulu. Kebiasaan menjaga segala sesuatu tetap rapi ini "
              "biasanya terlihat jelas di ruang kerjamu, jadwal harianmu, sampai cara kamu menyusun "
              "rencana untuk masa depan. Di lingkungan kerja, ketelitianmu membuatmu bisa diandalkan "
              "untuk pekerjaan yang butuh presisi tinggi, di mana kesalahan kecil sekalipun bisa "
              "berdampak besar. Rasa percaya diri yang kamu tunjukkan juga membuat orang lain "
              "cenderung mempercayai penilaianmu, terutama soal detail-detail yang mereka sendiri "
              "mungkin lewatkan.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Ketelitian dan kepercayaan dirimu membuat orang lain percaya pada kualitas kerjamu. "
              "Kamu juga berani bicara jujur saat orang lain memilih diam. Sayangnya, kejujuran yang "
              "terlalu terus terang ini kadang terdengar seperti kritik yang menyakitkan, meski "
              "maksudmu sebenarnya baik. Standar tinggi yang kamu pegang untuk dirimu sendiri juga "
              "sering kamu terapkan ke orang lain tanpa sadar, sehingga mereka bisa merasa dinilai "
              "terlalu keras hanya karena tidak serapi atau seteliti dirimu. Hal ini bisa membuat "
              "sebagian orang merasa sungkan atau bahkan enggan bekerja sama denganmu, meski "
              "sebenarnya mereka menghargai standar tinggimu.",
        "quote": "Kejujuran akan lebih mudah diterima kalau disampaikan dengan sedikit lebih lembut.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Sebelum menyampaikan kritik, coba pikirkan dulu cara penyampaian yang lebih "
              "lembut, tanpa mengubah kejujuran dari isi pesannya. Cobalah teknik sederhana: sebutkan "
              "dulu satu hal yang sudah dilakukan dengan baik, sebelum menyampaikan bagian yang masih "
              "perlu diperbaiki. Latihan ini akan membuat orang lain lebih terbuka menerima "
              "masukanmu, tanpa mengurangi ketelitian dan kejujuran yang selama ini jadi ciri khasmu.",
        "domains": {
            "karir": "Ketelitianmu adalah aset besar di dunia kerja, kamu cocok di peran yang butuh "
                     "presisi tinggi seperti quality assurance, audit, finance, atau posisi apa pun "
                     "yang tidak memberi ruang untuk kesalahan kecil. Atasan mempercayaimu untuk hal-"
                     "hal detail yang orang lain sering lewatkan. Namun kejujuranmu yang terus terang "
                     "bisa terdengar seperti kritik pedas di telinga rekan kerja yang lebih sensitif, "
                     "meski niatmu sebenarnya membantu. Standar tinggi yang kamu pegang untuk diri "
                     "sendiri juga sering kamu terapkan ke tim tanpa sadar, sehingga sebagian orang "
                     "merasa sungkan atau tertekan bekerja sama denganmu. *PR: Sebelum memberi masukan "
                     "ke rekan kerja minggu ini, mulai dengan menyebut satu hal yang sudah dia lakukan "
                     "dengan baik.*",
            "asmara": "Dalam hubungan, kejujuranmu membuat pasangan tahu persis di mana posisinya, "
                      "tidak ada permainan tebak-tebakan denganmu. Kamu juga suka menjaga hubungan "
                      "tetap rapi dan terencana, dari komunikasi sampai rencana masa depan. Namun "
                      "standar tinggi yang kamu miliki bisa membuat pasangan merasa terus dinilai, "
                      "terutama soal hal-hal kecil seperti kerapian atau cara melakukan sesuatu. "
                      "Kejujuranmu yang blak-blakan, kalau tidak dibungkus dengan cukup lembut, bisa "
                      "terasa menyakitkan bagi pasangan yang lebih sensitif, meski maksudmu sebenarnya "
                      "baik dan ingin hubungan jadi lebih baik. *PR: Sampaikan satu kritik ke "
                      "pasanganmu minggu ini dengan cara yang lebih lembut dari biasanya.*",
            "keuangan": "Soal keuangan, ketelitianmu membuatmu jago mengatur anggaran secara detail, "
                        "kamu tahu persis ke mana uangmu pergi dan jarang terkejut dengan pengeluaran "
                        "yang tidak terduga. Kerapian ini membuat kondisi finansialmu cenderung "
                        "terkontrol dengan baik dibanding kebanyakan orang. Namun standar tinggi yang "
                        "kamu pegang bisa membuatmu terlalu keras pada diri sendiri soal pengeluaran "
                        "kecil, sampai merasa bersalah untuk hal-hal yang sebenarnya wajar dinikmati. "
                        "Kamu juga cenderung terlalu vokal soal kebiasaan finansial orang lain di "
                        "sekitarmu, yang kadang membuat mereka merasa dihakimi. *PR: Izinkan dirimu "
                        "satu pengeluaran kecil minggu ini yang sifatnya murni untuk kesenangan, tanpa "
                        "menghitung ulang berkali-kali.*",
            "kesehatan": "Kerapian dan ketelitianmu biasanya membuatmu disiplin soal pola hidup sehat, "
                         "dari jadwal makan sampai rutinitas olahraga yang terstruktur dengan baik. "
                         "Kamu juga cenderung cepat sadar kalau ada yang tidak beres dengan tubuhmu "
                         "karena kamu memperhatikan detail dengan saksama. Namun standar tinggi yang "
                         "kamu terapkan bisa membuatmu terlalu keras pada diri sendiri soal kesempurnaan "
                         "fisik atau pola hidup, sampai sedikit penyimpangan dari rencana terasa seperti "
                         "kegagalan besar. Perfeksionisme ini, kalau dibiarkan, bisa memicu stres yang "
                         "sebenarnya tidak perlu. *PR: Kalau kamu melewatkan satu hari rutinitas sehatmu "
                         "minggu ini, coba lanjutkan lagi besok tanpa menyalahkan diri sendiri.*",
        },
    },
    "Anjing": {
        "tagline": "🐕 Shio Anjing",
        "chip": "SHIO",
        "title": "Anjing — Sosok Setia yang Bisa Dipercaya",
        "p1_label": "Siapa Kamu",
        "p1": "Shio Anjing dikenal sebagai simbol kesetiaan, kejujuran, dan rasa keadilan yang kuat. "
              "Kamu jarang berkhianat pada orang yang sudah kamu percaya, dan selalu berusaha "
              "melindungi orang-orang terdekatmu. Kamu juga peka terhadap ketidakadilan, dan tidak "
              "segan membela orang yang menurutmu diperlakukan tidak adil. Kesetiaanmu biasanya "
              "teruji justru di masa-masa sulit, saat orang lain mulai menjauh, kamu justru cenderung "
              "tetap berada di sisi orang yang kamu sayangi. Dalam lingkungan kerja, rasa "
              "tanggung jawab dan keadilanmu membuatmu dipercaya memegang peran yang butuh integritas "
              "tinggi. Orang-orang di sekitarmu tahu bahwa kalau kamu sudah berjanji, kamu akan "
              "berusaha keras menepatinya, apa pun yang terjadi.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kesetiaan dan rasa keadilanmu membuat orang lain merasa aman menjadikanmu sahabat atau "
              "rekan kerja. Kamu juga bisa diandalkan dalam situasi sulit sekalipun. Namun sisi "
              "waspada dalam dirimu kadang membuatmu terlalu khawatir atau curiga tentang hal-hal yang "
              "belum tentu terjadi, sampai sulit benar-benar merasa tenang. Kecenderungan untuk "
              "selalu memikirkan skenario terburuk ini bisa membuatmu kelelahan secara mental, "
              "bahkan ketika kenyataannya semuanya baik-baik saja. Kamu juga bisa terlalu keras "
              "menilai orang lain yang menurutmu bersikap tidak adil, tanpa memberi mereka "
              "kesempatan untuk menjelaskan sudut pandangnya.",
        "quote": "Kewaspadaan itu penting, tapi jangan sampai membuatmu kehilangan ketenangan di "
                 "masa sekarang.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Ketika muncul kekhawatiran tentang sesuatu yang belum terjadi, coba tanyakan "
              "pada diri sendiri seberapa besar kemungkinannya benar-benar terjadi, sebelum "
              "membiarkan kekhawatiran itu menguasai pikiranmu. Kamu bisa membuat catatan sederhana "
              "berisi kekhawatiran yang pernah muncul, lalu tinjau ulang setelah beberapa waktu untuk "
              "melihat berapa banyak yang benar-benar terjadi. Latihan ini bisa membantumu melihat "
              "dengan lebih jernih bahwa sebagian besar kekhawatiranmu sebenarnya tidak pernah "
              "terwujud.",
        "domains": {
            "karir": "Rasa tanggung jawab dan integritasmu membuatmu jadi sosok yang dipercaya "
                     "memegang posisi penting, terutama yang berhubungan dengan kepercayaan atau "
                     "keadilan, seperti HR, legal, atau peran yang mengharuskan kamu membela "
                     "kepentingan orang lain. Rekan kerja tahu kamu tidak akan mengkhianati kepercayaan "
                     "yang diberikan. Namun kecenderunganmu terlalu banyak memikirkan skenario "
                     "terburuk bisa membuatmu ragu mengambil keputusan yang sebenarnya sudah cukup "
                     "jelas, karena terus mencari kemungkinan yang bisa salah. Kamu juga bisa terlalu "
                     "keras menilai rekan kerja yang menurutmu bersikap tidak adil, tanpa memberi "
                     "mereka kesempatan menjelaskan konteksnya. *PR: Ambil satu keputusan kerja yang "
                     "selama ini kamu tunda karena terlalu banyak mempertimbangkan kemungkinan buruk.*",
            "asmara": "Dalam hubungan, kesetiaanmu tidak diragukan, kamu adalah tipe yang akan tetap "
                      "ada bahkan di masa-masa sulit, dan pasanganmu tahu betul itu. Kamu juga peka "
                      "terhadap ketidakadilan dalam hubungan dan tidak akan diam kalau merasa "
                      "diperlakukan tidak baik. Namun kecenderungan waspada dan curiga bisa membuatmu "
                      "terlalu sering menganalisis kata-kata atau sikap pasangan, mencari tanda-tanda "
                      "masalah yang sebenarnya tidak ada. Kekhawatiran berlebihan ini bisa melelahkan "
                      "hubungan, membuat pasangan merasa terus-menerus dicurigai padahal dia tidak "
                      "melakukan kesalahan apa pun. *PR: Sekali ini, coba nikmati momen tenang bersama "
                      "pasangan tanpa mencari-cari hal yang perlu dikhawatirkan.*",
            "keuangan": "Soal keuangan, sifat waspadamu membuatmu cenderung menyiapkan dana darurat "
                        "yang cukup dan jarang mengambil risiko finansial yang gegabah. Kamu juga jujur "
                        "dan adil dalam urusan uang dengan orang lain, tidak suka mengambil keuntungan "
                        "yang bukan hakmu. Namun kekhawatiran berlebihan soal masa depan bisa membuatmu "
                        "terlalu konservatif, sampai melewatkan peluang yang sebenarnya cukup aman "
                        "untuk diambil. Kamu juga bisa menghabiskan energi mental yang besar untuk "
                        "terus mengkhawatirkan skenario finansial terburuk yang kemungkinannya kecil "
                        "terjadi. *PR: Tuliskan rencana dana daruratmu di atas kertas, lalu izinkan "
                        "dirimu berhenti mengkhawatirkannya setelah itu.*",
            "kesehatan": "Kesetiaanmu pada rutinitas biasanya membuatmu disiplin menjaga kesehatan, "
                         "kamu jarang melewatkan hal-hal yang sudah jadi kebiasaan baik. Namun sifat "
                         "waspada yang berlebihan bisa membuat pikiranmu terus bekerja memikirkan "
                         "kemungkinan buruk, termasuk soal kesehatanmu sendiri, yang berujung pada "
                         "kecemasan yang menguras energi mental. Ketegangan ini kalau dibiarkan terus "
                         "bisa berdampak fisik, seperti sulit tidur nyenyak atau tubuh yang selalu "
                         "terasa tegang meski tidak sedang melakukan aktivitas berat. Kamu butuh cara "
                         "untuk benar-benar melepaskan kewaspadaan itu sesekali. *PR: Coba satu "
                         "aktivitas relaksasi sederhana setiap malam minggu ini, seperti peregangan "
                         "ringan sebelum tidur.*",
        },
    },
    "Babi": {
        "tagline": "🐷 Shio Babi",
        "chip": "SHIO",
        "title": "Babi — Sosok Tulus yang Penuh Kebaikan Hati",
        "p1_label": "Siapa Kamu",
        "p1": "Shio Babi melambangkan ketulusan, kemurahan hati, dan kejujuran yang sederhana. Kamu "
              "jarang berpikir buruk tentang orang lain, dan cenderung memberi kesempatan kedua meski "
              "sudah pernah dikecewakan. Kehadiranmu membuat orang-orang di sekitarmu merasa diterima "
              "apa adanya, tanpa banyak dihakimi. Kamu biasanya melihat sisi baik dari setiap orang "
              "terlebih dulu, sebelum menilai kesalahan atau kekurangan mereka. Dalam pertemanan, "
              "kamu adalah sosok yang murah hati, baik dalam berbagi waktu, tenaga, maupun materi, "
              "tanpa terlalu banyak menghitung untung rugi. Di lingkungan kerja, ketulusanmu membuat "
              "rekan-rekan merasa nyaman bekerja sama denganmu, karena mereka tahu kamu jarang punya "
              "agenda tersembunyi di balik setiap tindakanmu.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Ketulusan dan kemurahan hatimu membuat orang lain merasa nyaman dan dihargai saat "
              "bersamamu. Kamu juga jarang menyimpan dendam terlalu lama. Namun sikap yang terlalu "
              "percaya ini kadang membuatmu mudah dimanfaatkan oleh orang-orang yang sebenarnya tidak "
              "berniat baik. Kebaikan hatimu yang tanpa syarat ini bisa membuat sebagian orang "
              "sengaja mengambil keuntungan dari kesediaanmu untuk selalu membantu, sementara kamu "
              "sendiri jarang meminta imbalan apa pun. Kalau tidak diimbangi kehati-hatian, pola ini "
              "bisa berulang terus-menerus tanpa kamu sadari.",
        "quote": "Kebaikan hati akan lebih aman kalau disertai sedikit kehati-hatian dalam memilih "
                 "kepada siapa kamu memberikannya.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba perhatikan lebih saksama pola perlakuan orang-orang di sekitarmu, dan "
              "beri batasan yang wajar kepada mereka yang selama ini hanya memanfaatkan kebaikanmu. "
              "Latih dirimu untuk sesekali berkata \"tidak\" pada permintaan yang terasa tidak adil, "
              "tanpa harus merasa bersalah karenanya. Ingat, kebaikan hati yang sehat tetap bisa "
              "berjalan bersama batasan yang jelas, dan itu justru membuat kebaikanmu lebih "
              "berkelanjutan.",
        "domains": {
            "karir": "Ketulusan dan kemurahan hatimu membuat rekan kerja senang berkolaborasi "
                     "denganmu, kamu jarang punya agenda tersembunyi dan itu membuatmu dipercaya di "
                     "lingkungan kerja mana pun. Kamu cocok di peran yang melibatkan kerja sama tim "
                     "atau pelayanan kepada orang lain, karena kamu tulus ingin membantu tanpa banyak "
                     "menghitung untung-rugi. Namun ketulusan ini bisa dimanfaatkan rekan kerja yang "
                     "kurang bertanggung jawab, mereka bisa membebankan tugasnya padamu karena tahu "
                     "kamu jarang menolak permintaan tolong. Kamu juga cenderung kurang vokal "
                     "memperjuangkan haknya sendiri, seperti kenaikan gaji atau pengakuan atas "
                     "kerja kerasmu. *PR: Sekali ini, tolak satu permintaan tolong yang sebenarnya di "
                     "luar tanggung jawabmu di kantor.*",
            "asmara": "Dalam hubungan, ketulusanmu membuat pasangan merasa benar-benar diterima apa "
                      "adanya, kamu jarang menghakimi kekurangan pasangan dan selalu memberi "
                      "kesempatan kedua. Kamu juga murah hati dalam mencintai, tidak pelit memberi "
                      "waktu dan perhatian. Namun sikap yang terlalu percaya ini bisa membuatmu "
                      "gampang dimanfaatkan oleh pasangan yang kurang bertanggung jawab, kamu terus "
                      "memaafkan meski pola kesalahan yang sama berulang. Kamu perlu belajar bahwa "
                      "memberi kesempatan kedua itu baik, tapi ada batas wajar sebelum itu berubah "
                      "jadi membiarkan diri terus dirugikan. *PR: Perhatikan satu pola dalam "
                      "hubunganmu yang selama ini terus berulang, dan bicarakan dengan pasangan tanpa "
                      "langsung memaafkan begitu saja.*",
            "keuangan": "Soal keuangan, kemurahan hatimu membuatmu senang berbagi dengan orang "
                        "terdekat, entah lewat traktiran, bantuan, atau hadiah tanpa alasan khusus. "
                        "Kamu percaya rezeki akan berputar kalau kamu murah hati pada orang lain. "
                        "Namun sikap yang terlalu percaya dan murah hati ini bisa membuatmu rentan "
                        "dimanfaatkan orang yang sengaja mendekat karena tahu kamu mudah membantu "
                        "secara finansial. Kamu juga jarang mencatat atau menagih kembali uang yang "
                        "kamu pinjamkan, sampai tanpa sadar kondisi keuanganmu sendiri jadi terganggu "
                        "karena terlalu banyak membantu orang lain. *PR: Buat batasan jelas soal "
                        "berapa banyak yang bisa kamu bantu bulan ini, dan patuhi batasan itu.*",
            "kesehatan": "Sifatmu yang santai dan jarang menyimpan dendam membuat bebanmu secara "
                         "mental cenderung lebih ringan dibanding orang lain, kamu tidak mudah stres "
                         "memikirkan hal-hal yang sudah lewat. Namun sikap terlalu percaya dan mudah "
                         "memaafkan bisa membuatmu menahan kekecewaan yang seharusnya diproses, "
                         "bukan sekadar dilupakan begitu saja, dan itu bisa menumpuk jadi beban "
                         "emosional yang tidak terlihat. Kamu juga cenderung kurang tegas menjaga "
                         "waktu istirahatmu sendiri karena selalu memprioritaskan membantu orang lain "
                         "lebih dulu. *PR: Jadwalkan satu waktu khusus minggu ini yang benar-benar "
                         "untuk dirimu sendiri, tanpa bisa diganggu urusan membantu orang lain.*",
        },
    },
}
