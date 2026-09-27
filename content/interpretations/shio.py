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
    },
}
