"""
Konten Zodiak (12 kategori).

Key dict ini HARUS sama persis dengan nilai "sign" dari engine/zodiak.py
(hitung_zodiak()["sign"]) supaya bisa langsung dipakai sebagai lookup:
Aries, Taurus, Gemini, Cancer, Leo, Virgo, Libra, Scorpio, Sagittarius,
Capricorn, Aquarius, Pisces.

Struktur tiap entri sama persis dengan DUMMY_RESULTS di views/revealpage.py
(tagline, chip, title, p1_label, p1, p2_label, p2, quote, p3_label, p3)
supaya nanti bisa langsung menggantikan DUMMY_RESULTS tanpa ubah kode
rendering.

REVISI (26 Sep 2026 malam): isi p1/p2/p3 diperpanjang 2-3x lipat dari versi
sebelumnya (per instruksi Stev), supaya laporannya terasa lebih bernilai
dan aplikatif, bukan cuma label singkat.
"""

ZODIAK_CONTENT = {
    "Aries": {
        "tagline": "☉ Matahari di Aries",
        "chip": "ZODIAK",
        "title": "Aries — Sang Pemberani yang Cepat Bergerak",
        "p1_label": "Siapa Kamu",
        "p1": "Kamu lahir saat matahari berada di rasi Aries, rasi pertama dalam siklus zodiak, dan "
              "itu tercermin dari caramu menghadapi hidup: berani mengambil langkah pertama saat orang "
              "lain masih ragu. Energi dalam dirimu terasa cepat menyala, membuatmu jarang betah "
              "berlama-lama di zona nyaman. Begitu ada tantangan baru, biasanya kamu yang paling dulu "
              "maju, bukan karena tidak takut, tapi karena kamu memilih untuk tidak membiarkan rasa "
              "takut itu menahanmu. Sifat ini sudah terlihat sejak kamu masih muda, misalnya lewat "
              "kebiasaan mengangkat tangan lebih dulu untuk mencoba sesuatu yang baru, atau memilih "
              "jalan yang belum pernah dilalui orang lain di sekitarmu. Dalam pekerjaan, energi ini "
              "membuatmu cocok mengisi peran perintis, seperti membuka proyek baru atau memimpin tim "
              "yang sedang membangun sesuatu dari nol. Dalam pertemanan, kamu sering jadi orang yang "
              "mengajak teman-temanmu keluar dari rutinitas dan mencoba pengalaman baru bersama.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Keberanian dan inisiatifmu membuat orang lain sering menjadikanmu contoh soal cara "
              "memulai sesuatu. Kamu juga jujur soal apa yang kamu rasakan, sehingga orang tahu persis "
              "di mana posisi mereka di matamu. Namun semangat yang menyala cepat itu kadang juga "
              "padam secepat itu pula, membuat beberapa rencana besar berhenti di tengah jalan sebelum "
              "sempat kamu selesaikan. Pola \"semangat di awal, hilang di tengah jalan\" ini bisa "
              "membuat orang lain ragu mempercayakan proyek jangka panjang kepadamu, meski mereka "
              "tahu betul kamu adalah orang paling tepat untuk memulai sesuatu. Kejujuranmu yang "
              "spontan juga kadang keluar tanpa penyaringan, sehingga bisa menyakiti perasaan orang "
              "lain meski itu bukan niatmu.",
        "quote": "Keberanian akan terasa jauh lebih berarti kalau disertai dengan kesabaran untuk "
                 "menyelesaikannya.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba pilih satu hal kecil yang sempat kamu tinggalkan setengah jalan, lalu "
              "selesaikan sampai tuntas sebelum memulai hal baru yang lain. Rasakan bedanya ketika kamu "
              "benar-benar menuntaskan sesuatu, bukan cuma memulainya. Kamu bisa membuat kesepakatan "
              "sederhana dengan dirimu sendiri: setiap kali ide baru muncul saat sedang mengerjakan "
              "sesuatu, tuliskan dulu ide itu di catatan terpisah, dan kembali fokus menyelesaikan "
              "yang sedang berjalan. Dengan begitu, semangat awalmu tetap tersalurkan tanpa mengorbankan "
              "penyelesaian yang sudah dimulai.",
    },
    "Taurus": {
        "tagline": "☉ Matahari di Taurus",
        "chip": "ZODIAK",
        "title": "Taurus — Sosok Tenang yang Setia",
        "p1_label": "Siapa Kamu",
        "p1": "Matahari yang berada di rasi Taurus saat kamu lahir memberimu fondasi yang tenang dan "
              "stabil. Kamu tidak mudah terpancing untuk buru-buru mengambil keputusan, dan lebih "
              "memilih memastikan segalanya benar-benar matang dulu sebelum melangkah. Kesetiaanmu "
              "pada orang, kebiasaan, dan hal-hal yang sudah terbukti baik membuatmu jadi sosok yang "
              "bisa diandalkan dalam jangka panjang. Kamu juga cenderung menikmati kenyamanan fisik, "
              "seperti makanan enak, suasana rumah yang nyaman, atau rutinitas yang sudah kamu kenal "
              "baik, karena bagimu hal-hal itu memberi rasa aman yang sulit digantikan hal lain. Dalam "
              "pekerjaan, ketekunanmu membuatmu unggul di posisi yang butuh kestabilan dan hasil yang "
              "bertahan lama, bukan sekadar tren sesaat. Orang-orang terdekatmu tahu bahwa hubungan "
              "denganmu jarang berubah drastis; begitu kamu berkomitmen, kamu benar-benar menjaganya.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Ketekunan dan kesabaranmu membuat apa pun yang kamu kerjakan cenderung bertahan lama dan "
              "kokoh, bukan sekadar tren sesaat. Orang-orang merasa nyaman berada di dekatmu karena "
              "kamu jarang berubah pikiran tiba-tiba. Sayangnya, kenyamanan pada rutinitas itu kadang "
              "membuatmu enggan mencoba hal baru, bahkan ketika perubahan itu sebenarnya bisa membawa "
              "hal yang lebih baik untukmu. Ketakutan terhadap ketidakpastian ini bisa membuatmu "
              "menolak peluang bagus hanya karena terasa asing atau belum teruji. Kamu juga bisa "
              "terlalu keras kepala mempertahankan cara lama, bahkan saat bukti di depan mata "
              "menunjukkan bahwa cara itu sudah tidak lagi relevan.",
        "quote": "Stabilitas itu berharga, tapi sesekali membiarkan diri berubah juga bagian dari "
                 "tumbuh.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba lakukan satu hal kecil yang berbeda dari kebiasaanmu, sesuatu yang "
              "sebenarnya sudah lama ingin kamu coba tapi selalu ditunda. Tidak perlu besar, cukup "
              "untuk membuktikan pada dirimu sendiri bahwa perubahan kecil itu aman. Kamu bisa mulai "
              "dari hal sepele seperti mencoba rute baru menuju tempat kerja, atau memesan menu yang "
              "belum pernah kamu coba. Perhatikan perasaanmu setelahnya, dan gunakan pengalaman itu "
              "sebagai bukti kecil bahwa keluar dari rutinitas tidak selalu berarti kehilangan rasa "
              "aman.",
    },
    "Gemini": {
        "tagline": "☉ Matahari di Gemini",
        "chip": "ZODIAK",
        "title": "Gemini — Si Lincah yang Serba Ingin Tahu",
        "p1_label": "Siapa Kamu",
        "p1": "Kamu lahir saat matahari berada di rasi Gemini, rasi yang identik dengan rasa ingin "
              "tahu yang besar dan kemampuan berkomunikasi yang luwes. Pikiranmu bergerak cepat dari "
              "satu topik ke topik lain, dan kamu jarang merasa bosan selama masih ada hal baru untuk "
              "dipelajari atau dibicarakan. Kemampuanmu menyesuaikan diri di berbagai lingkaran "
              "pertemanan membuatmu terasa mudah akrab dengan banyak orang. Kamu biasanya punya "
              "banyak minat sekaligus, dari topik ringan sampai yang cukup serius, dan senang menjadi "
              "penghubung informasi antara satu kelompok dengan kelompok lainnya. Dalam pekerjaan, "
              "kelincahan berpikirmu membuatmu cocok di peran yang butuh komunikasi lintas tim atau "
              "menangani banyak jenis tugas sekaligus. Di lingkungan sosial, kamu adalah tipe orang "
              "yang selalu punya bahan obrolan baru, membuat percakapan denganmu jarang terasa "
              "membosankan.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Keluwesanmu dalam berbicara dan beradaptasi membuat orang lain merasa nyaman bertukar "
              "cerita denganmu. Kamu juga cepat menangkap ide baru dan menghubungkannya dengan hal-hal "
              "yang sudah kamu ketahui sebelumnya. Namun rasa ingin tahu yang terlalu banyak arah "
              "kadang membuatmu kesulitan fokus menyelesaikan satu hal sampai benar-benar tuntas. "
              "Kecenderungan berpindah topik atau minat ini bisa membuat orang lain merasa kamu "
              "kurang konsisten, meski sebenarnya itu murni karena rasa ingin tahumu yang tidak "
              "pernah habis. Kamu juga bisa terjebak mengetahui banyak hal secara permukaan, tanpa "
              "benar-benar mendalami satu bidang sampai jadi ahli di dalamnya.",
        "quote": "Rasa ingin tahu akan membawamu jauh, asal kamu juga tahu kapan harus berhenti "
                 "menjelajah dan mulai mendalami.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Pilih satu proyek atau kebiasaan yang sudah lama ingin kamu kuasai, lalu fokuskan "
              "waktumu di situ secara konsisten tanpa berpindah ke hal lain. Lihat seberapa "
              "jauh kamu bisa berkembang kalau perhatianmu tidak terpecah. Kamu bisa mencoba "
              "menetapkan waktu khusus setiap minggu yang benar-benar didedikasikan untuk satu topik "
              "itu saja, dan menahan diri untuk tidak beralih ke minat baru selama waktu tersebut "
              "berlangsung.",
    },
    "Cancer": {
        "tagline": "☉ Matahari di Cancer",
        "chip": "ZODIAK",
        "title": "Cancer — Pelindung yang Penuh Perasaan",
        "p1_label": "Siapa Kamu",
        "p1": "Matahari berada di rasi Cancer saat kamu lahir, dan itu membuatmu punya kepekaan emosi "
              "yang dalam terhadap dirimu sendiri maupun orang-orang di sekitarmu. Rumah dan keluarga, "
              "baik dalam arti sebenarnya maupun orang-orang yang kamu anggap keluarga, punya tempat "
              "yang sangat penting dalam hidupmu. Kamu cenderung melindungi orang-orang terdekat "
              "dengan sepenuh hati, bahkan sebelum diminta. Kepekaanmu ini membuatmu mudah mengingat "
              "momen-momen emosional, baik yang menyenangkan maupun yang menyakitkan, dan momen-momen "
              "itu sering membentuk cara kamu memperlakukan orang lain di masa depan. Dalam "
              "hubungan, kamu adalah tipe orang yang benar-benar hadir saat orang lain sedang "
              "kesulitan, siap mendengarkan tanpa perlu diminta. Di lingkungan kerja, sisi pengasuh "
              "ini juga muncul lewat caramu memperhatikan kesejahteraan rekan-rekan setim, bukan "
              "hanya fokus pada hasil kerja semata.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Empati dan kepedulianmu membuat orang lain merasa aman menceritakan hal-hal yang berat "
              "kepadamu. Kamu juga punya ingatan emosional yang kuat, sehingga bisa mengenali perasaan "
              "seseorang bahkan dari hal-hal kecil. Sisi sensitif ini terkadang membuatmu mudah "
              "terbawa suasana hati, atau menyimpan kekecewaan lebih lama dari yang seharusnya. Kamu "
              "bisa jadi terlalu protektif terhadap orang-orang yang kamu sayangi, sampai tanpa "
              "sadar membatasi ruang gerak mereka karena rasa khawatirmu yang berlebihan. Ingatan "
              "emosionalmu yang kuat juga bisa jadi pedang bermata dua, karena kamu cenderung terus "
              "mengingat luka lama meski orang lain sudah lama melupakannya.",
        "quote": "Melindungi orang lain itu indah, tapi jangan sampai lupa melindungi perasaanmu "
                 "sendiri juga.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Ketika ada perasaan yang mengganjal, coba tuliskan atau ceritakan langsung "
              "kepada orang yang bersangkutan, alih-alih memendamnya sendirian sampai berlarut-larut. "
              "Kamu juga bisa melatih diri untuk melepaskan satu kekecewaan lama yang sebenarnya "
              "sudah tidak relevan lagi, dengan cara menuliskannya dan secara sadar memutuskan untuk "
              "tidak membawanya lagi ke hubungan yang sedang berjalan sekarang.",
    },
    "Leo": {
        "tagline": "☉ Matahari di Leo",
        "chip": "ZODIAK",
        "title": "Leo — Sang Pemimpin yang Hangat",
        "p1_label": "Siapa Kamu",
        "p1": "Kamu lahir saat matahari berada di rasi Leo, dan hal itu terlihat jelas dari cara "
              "orang-orang merespons kehadiranmu. Ada kehangatan alami dalam dirimu yang membuat "
              "orang di sekitarmu merasa lebih bersemangat begitu kamu masuk ke dalam ruangan. Kamu "
              "juga bukan tipe yang suka menunggu arahan; begitu sebuah ide muncul, kamu biasanya "
              "sudah lebih dulu bergerak. Kehadiranmu cenderung membawa energi positif ke mana pun "
              "kamu pergi, dan orang lain sering merasa lebih percaya diri hanya karena berada di "
              "dekatmu. Dalam lingkungan kerja, kamu cocok mengisi peran yang membutuhkan sosok yang "
              "bisa memotivasi tim dan mengarahkan mereka menuju tujuan bersama. Dalam pertemanan, "
              "kamu sering jadi pusat perhatian, bukan karena mencari-cari, tapi karena caramu "
              "bersikap memang menarik perhatian orang secara alami.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kepemimpinan memang terasa seperti bagian alami dari dirimu. Kamu mampu membuat orang "
              "lain percaya pada arah yang kamu tunjukkan, bahkan sebelum kamu sendiri sepenuhnya "
              "yakin. Namun semangat besar itu terkadang membuatmu lupa untuk mendengarkan lebih dulu "
              "sebelum mengambil keputusan, padahal orang-orang di sekitarmu juga ingin didengar, "
              "bukan hanya diarahkan. Kebutuhanmu untuk selalu tampil percaya diri ini kadang membuat "
              "kamu sulit mengakui kesalahan di depan orang lain, meski di dalam hati kamu sudah "
              "menyadarinya. Orang lain juga bisa merasa terbayangi olehmu, terutama saat kamu terlalu "
              "mendominasi percakapan atau pengambilan keputusan dalam kelompok.",
        "quote": "Kepemimpinan yang paling kuat adalah yang tahu kapan harus diam dan mendengarkan.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba sekali saja menahan diri untuk tidak langsung memberi solusi ketika "
              "ada teman yang bercerita tentang masalahnya. Dengarkan saja sampai selesai. Kamu "
              "mungkin akan terkejut, karena terkadang orang hanya butuh didengar, bukan diarahkan, "
              "dan hal kecil ini justru akan membuat mereka semakin percaya padamu sebagai sosok "
              "pemimpin. Latih juga dirimu untuk sesekali bertanya \"menurutmu bagaimana?\" sebelum "
              "menyampaikan pendapatmu sendiri, supaya orang lain merasa dilibatkan, bukan hanya "
              "diarahkan.",
    },
    "Virgo": {
        "tagline": "☉ Matahari di Virgo",
        "chip": "ZODIAK",
        "title": "Virgo — Perfeksionis yang Teliti",
        "p1_label": "Siapa Kamu",
        "p1": "Matahari yang berada di rasi Virgo saat kamu lahir memberimu ketelitian yang jarang "
              "dimiliki banyak orang. Kamu memperhatikan detail-detail kecil yang sering terlewat oleh "
              "orang lain, dan hal itu membuat pekerjaanmu biasanya rapi serta minim kesalahan. Kamu "
              "juga punya standar tinggi terhadap diri sendiri, dan selalu berusaha memberikan yang "
              "terbaik dalam segala hal yang kamu kerjakan. Kecenderungan untuk menganalisis ini juga "
              "muncul dalam caramu memandang berbagai situasi, kamu jarang menerima sesuatu begitu "
              "saja tanpa memikirkan bagaimana hal itu bisa diperbaiki atau disempurnakan. Dalam "
              "pekerjaan, ketelitianmu membuatmu unggul di peran yang membutuhkan akurasi tinggi, "
              "seperti mengelola data, menyusun rencana yang rinci, atau memastikan kualitas sebuah "
              "hasil kerja. Orang-orang di sekitarmu tahu bahwa kalau ada sesuatu yang kamu periksa, "
              "kemungkinan besar hasilnya akan lebih rapi dari sebelumnya.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Ketelitian dan tanggung jawabmu membuat orang lain percaya menyerahkan pekerjaan "
              "penting kepadamu, karena tahu kamu akan mengurusnya dengan serius. Kamu juga jago "
              "melihat celah perbaikan yang orang lain lewatkan. Sayangnya, standar tinggi itu kadang "
              "berbalik menjadi kritik yang terlalu keras terhadap dirimu sendiri, sampai lupa "
              "mengapresiasi hal-hal yang sudah kamu capai dengan baik. Kebiasaan ini juga bisa "
              "membuatmu terlalu fokus pada kekurangan kecil, sampai kehilangan gambaran besar tentang "
              "seberapa jauh sebenarnya kamu sudah maju. Orang lain di sekitarmu mungkin merasa "
              "sungkan menunjukkan hasil kerja mereka kepadamu, karena khawatir dinilai terlalu "
              "detail.",
        "quote": "Kesempurnaan itu indah untuk dikejar, tapi jangan sampai membuatmu lupa menghargai "
                 "kemajuan yang sudah ada.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Sebelum tidur, coba tuliskan satu hal kecil yang sudah kamu kerjakan dengan "
              "baik hari itu, tanpa langsung memikirkan apa yang masih kurang darinya. Lakukan "
              "ini secara konsisten selama beberapa minggu, dan perhatikan bagaimana kebiasaan ini "
              "perlahan membantumu melihat kemajuanmu sendiri dengan lebih adil, bukan hanya "
              "berfokus pada apa yang belum sempurna.",
    },
    "Libra": {
        "tagline": "☉ Matahari di Libra",
        "chip": "ZODIAK",
        "title": "Libra — Penjaga Keseimbangan",
        "p1_label": "Siapa Kamu",
        "p1": "Kamu lahir saat matahari berada di rasi Libra, rasi yang dilambangkan dengan timbangan, "
              "dan itu sangat terasa dari caramu memandang keadilan serta keseimbangan dalam hidup. "
              "Kamu cenderung mempertimbangkan banyak sudut pandang sebelum mengambil keputusan, dan "
              "selalu berusaha menciptakan suasana yang harmonis di sekitarmu. Estetika dan keindahan "
              "juga terasa penting bagimu, baik dalam penampilan maupun cara kamu menata hidup. Kamu "
              "biasanya jadi sosok yang dicari saat ada perselisihan, karena kemampuanmu melihat dari "
              "berbagai sisi membuat pihak-pihak yang berkonflik merasa didengarkan secara adil. Dalam "
              "lingkungan kerja, kamu cocok mengisi peran yang membutuhkan diplomasi dan kemampuan "
              "menjaga hubungan baik antar berbagai pihak. Dalam kehidupan pribadi, kamu senang "
              "menciptakan lingkungan yang indah dan nyaman, baik untuk dirimu sendiri maupun untuk "
              "orang-orang yang kamu sayangi.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kemampuanmu melihat dari berbagai sisi membuatmu jadi penengah yang baik ketika ada "
              "konflik di sekitarmu. Orang-orang senang berdiskusi denganmu karena kamu jarang "
              "memihak secara buta. Namun kebiasaan mempertimbangkan terlalu banyak hal ini kadang "
              "membuatmu sulit mengambil keputusan sendiri, sampai akhirnya keinginanmu sendiri "
              "tertunda demi menjaga keharmonisan dengan orang lain. Kecenderungan untuk selalu "
              "mencari jalan tengah ini bisa membuatmu terjebak dalam ketidakpastian yang "
              "berkepanjangan, terutama saat situasi sebenarnya membutuhkan keputusan yang tegas dan "
              "cepat. Kamu juga bisa kehilangan jati diri sendiri karena terlalu sering menyesuaikan "
              "diri dengan keinginan orang lain.",
        "quote": "Keseimbangan yang sesungguhnya juga mencakup memberi ruang bagi keinginanmu "
                 "sendiri, bukan hanya orang lain.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Ketika dihadapkan pada satu pilihan kecil, coba ambil keputusan sendiri "
              "tanpa bertanya pendapat orang lain terlebih dulu, lalu perhatikan bagaimana rasanya "
              "mempercayai penilaianmu sendiri. Kamu bisa mulai dari keputusan yang risikonya kecil, "
              "seperti memilih film yang akan ditonton atau tempat yang akan dikunjungi, sebelum "
              "melangkah ke keputusan yang lebih besar dan berdampak jangka panjang.",
    },
    "Scorpio": {
        "tagline": "☉ Matahari di Scorpio",
        "chip": "ZODIAK",
        "title": "Scorpio — Sosok Misterius yang Mendalam",
        "p1_label": "Siapa Kamu",
        "p1": "Matahari berada di rasi Scorpio saat kamu lahir, memberimu kedalaman emosi dan intuisi "
              "yang tajam. Kamu jarang puas dengan hal-hal yang terlihat di permukaan saja, dan selalu "
              "ingin memahami apa yang sebenarnya terjadi di balik sesuatu. Ketika kamu benar-benar "
              "percaya pada seseorang, kesetiaanmu terasa sangat kuat, meskipun kamu tidak mudah "
              "membiarkan orang lain masuk terlalu dalam ke dunia pribadimu. Kamu punya kemampuan "
              "membaca situasi dan orang lain jauh lebih dalam dari kebanyakan orang, sering kali "
              "menangkap hal-hal yang tersembunyi di balik kata-kata atau sikap seseorang. Dalam "
              "pekerjaan, ketajaman fokus dan daya tahanmu membuatmu unggul menyelesaikan proyek yang "
              "rumit atau membutuhkan riset mendalam. Dalam hubungan, sekali kamu memutuskan untuk "
              "percaya pada seseorang, kesetiaanmu jarang goyah, bahkan di saat-saat sulit sekalipun.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Ketajaman intuisi dan fokusmu membuatmu bisa menyelesaikan hal-hal yang orang lain "
              "anggap rumit atau menakutkan. Kamu juga setia dan penuh perhatian pada orang-orang yang "
              "sudah mendapat kepercayaanmu. Namun kecenderungan untuk menutup diri dan curiga secara "
              "berlebihan kadang membuat orang-orang di sekitarmu merasa sulit benar-benar dekat "
              "denganmu, meski niat mereka baik. Kebutuhanmu untuk selalu mengontrol informasi tentang "
              "dirimu sendiri ini bisa membuat hubungan terasa berat sebelah, karena kamu tahu banyak "
              "tentang orang lain, tapi orang lain tidak selalu tahu banyak tentangmu. Kamu juga bisa "
              "menyimpan kekecewaan atau kemarahan lebih lama dari yang seharusnya, sampai hal itu "
              "memengaruhi cara pandangmu terhadap seseorang secara keseluruhan.",
        "quote": "Kedalaman perasaanmu adalah kekuatan, tapi kepercayaan juga butuh ruang untuk "
                 "tumbuh.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba bagikan satu hal yang biasanya kamu simpan sendiri kepada orang yang kamu percaya, "
              "sekecil apa pun itu, dan lihat bagaimana keterbukaan itu bisa mempererat "
              "hubungan kalian. Latih juga dirimu untuk melepaskan satu kekecewaan lama secara sadar, "
              "dengan mengingatkan diri sendiri bahwa memegang kemarahan terlalu lama hanya akan "
              "membebani dirimu sendiri, bukan orang yang membuatmu kecewa.",
    },
    "Sagittarius": {
        "tagline": "☉ Matahari di Sagittarius",
        "chip": "ZODIAK",
        "title": "Sagittarius — Sang Penjelajah yang Bebas",
        "p1_label": "Siapa Kamu",
        "p1": "Kamu lahir saat matahari berada di rasi Sagittarius, rasi yang identik dengan semangat "
              "menjelajah dan haus akan pengalaman baru. Kamu tidak suka merasa terkurung dalam "
              "rutinitas yang itu-itu saja, dan selalu tertarik pada hal-hal yang memperluas "
              "pandanganmu tentang dunia. Kejujuranmu yang blak-blakan membuat orang lain tahu persis "
              "apa yang kamu pikirkan, tanpa harus menebak-nebak. Kamu punya rasa optimisme yang "
              "cenderung menular, membuat orang-orang di sekitarmu ikut merasa lebih ringan menghadapi "
              "masalah mereka sendiri. Dalam pekerjaan, kamu cocok mengisi peran yang memberi ruang "
              "gerak dan variasi, karena kamu cepat merasa terkekang di lingkungan yang terlalu kaku "
              "atau monoton. Dalam pertemanan, kamu adalah tipe orang yang mengajak orang lain "
              "melihat dunia dari sudut pandang yang lebih luas dan penuh kemungkinan.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Optimisme dan rasa ingin tahumu terhadap dunia membuat orang-orang di sekitarmu ikut "
              "terinspirasi untuk berani mencoba hal baru. Kamu juga jarang terjebak dalam masalah "
              "kecil karena selalu bisa melihat gambaran yang lebih besar. Sayangnya, kejujuranmu yang "
              "terlalu terus terang kadang menyakiti perasaan orang lain tanpa kamu sadari, dan "
              "keinginan bebasmu kadang membuatmu sulit berkomitmen dalam jangka panjang. Kebutuhanmu "
              "untuk selalu punya ruang bebas ini bisa membuat orang-orang terdekatmu merasa tidak "
              "yakin seberapa jauh mereka bisa mengandalkanmu, terutama dalam hubungan yang menuntut "
              "kestabilan jangka panjang.",
        "quote": "Kebebasan akan terasa lebih indah kalau kamu juga memikirkan perasaan orang yang "
                 "kamu ajak bicara.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Sebelum menyampaikan pendapat yang cukup blak-blakan, coba jeda sebentar dan "
              "pikirkan bagaimana perasaan orang yang mendengarnya, tanpa harus mengubah kejujuranmu. "
              "Kamu juga bisa melatih diri untuk menepati satu komitmen kecil secara konsisten, "
              "sebagai cara membuktikan bahwa kebebasan yang kamu junjung tinggi tetap bisa berjalan "
              "beriringan dengan tanggung jawab.",
    },
    "Capricorn": {
        "tagline": "☉ Matahari di Capricorn",
        "chip": "ZODIAK",
        "title": "Capricorn — Pekerja Keras yang Disiplin",
        "p1_label": "Siapa Kamu",
        "p1": "Matahari yang berada di rasi Capricorn saat kamu lahir memberimu ketekunan dan disiplin "
              "yang kuat dalam mengejar apa yang kamu inginkan. Kamu jarang mengharapkan hasil instan, "
              "dan lebih memilih membangun sesuatu perlahan namun kokoh dari fondasinya. Tanggung "
              "jawab terasa seperti bagian alami dari dirimu, bahkan sejak usia yang cukup muda. Kamu "
              "biasanya punya rencana jangka panjang yang jelas, dan setiap langkah yang kamu ambil "
              "cenderung terarah menuju tujuan itu, bukan sekadar bertindak spontan. Dalam pekerjaan, "
              "kedisiplinanmu membuatmu unggul di peran-peran yang membutuhkan konsistensi dan "
              "tanggung jawab besar, jenis peran yang membuat banyak orang lain kewalahan. Dalam "
              "kehidupan pribadi, kamu adalah sosok yang bisa diandalkan keluarga atau orang terdekat "
              "saat mereka membutuhkan seseorang yang tegar dan bisa diandalkan.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kedisiplinan dan keteguhanmu membuat orang lain percaya bahwa apa pun yang kamu "
              "pegang pasti akan diselesaikan dengan baik. Kamu juga tidak mudah menyerah ketika "
              "menghadapi rintangan besar. Namun fokus yang terlalu besar pada pencapaian dan "
              "tanggung jawab kadang membuatmu lupa untuk beristirahat, atau menikmati momen-momen "
              "kecil yang sebenarnya juga layak disyukuri. Kebiasaan mengukur diri sendiri lewat "
              "pencapaian ini bisa membuatmu merasa tidak pernah cukup, bahkan setelah mencapai "
              "sesuatu yang besar. Kamu juga bisa terlalu keras terhadap dirimu sendiri saat "
              "sesuatu tidak berjalan sesuai rencana yang sudah kamu susun matang-matang.",
        "quote": "Kesuksesan yang dibangun perlahan tetap butuh jeda untuk dinikmati di sepanjang "
                 "jalan.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Luangkan satu waktu khusus yang benar-benar bebas dari pekerjaan atau "
              "target, dan gunakan waktu itu untuk hal yang murni menyenangkan bagimu. Kamu juga bisa "
              "melatih diri merayakan pencapaian kecil begitu berhasil, alih-alih langsung berpindah "
              "memikirkan target berikutnya. Kebiasaan ini akan membantu perjalanan panjangmu terasa "
              "lebih ringan dan bermakna.",
    },
    "Aquarius": {
        "tagline": "☉ Matahari di Aquarius",
        "chip": "ZODIAK",
        "title": "Aquarius — Pemikir yang Out of the Box",
        "p1_label": "Siapa Kamu",
        "p1": "Kamu lahir saat matahari berada di rasi Aquarius, rasi yang identik dengan pemikiran "
              "yang unik dan cara pandang yang sering berbeda dari kebanyakan orang. Kamu tidak "
              "terlalu peduli mengikuti arus, dan lebih tertarik memikirkan bagaimana sesuatu bisa "
              "diperbaiki atau dilakukan dengan cara yang belum pernah dicoba orang lain. Kamu juga "
              "punya kepedulian besar terhadap isu-isu yang lebih luas dari dirimu sendiri. Cara "
              "berpikirmu yang unik ini sering membuatmu jadi orang yang pertama kali mengusulkan "
              "ide-ide yang di awal terdengar aneh, tapi belakangan ternyata masuk akal dan bahkan "
              "diikuti banyak orang. Dalam pekerjaan, kamu cocok mengisi peran yang membutuhkan "
              "inovasi dan pemikiran di luar kebiasaan. Dalam pergaulan, kamu punya lingkaran "
              "pertemanan yang beragam, karena kamu jarang menilai orang dari latar belakang atau "
              "kelompok sosialnya.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Orisinalitas dan idealismemu membuat orang lain terinspirasi untuk berpikir lebih "
              "terbuka. Kamu juga cenderung objektif dan tidak mudah terbawa emosi dalam menilai "
              "sesuatu. Namun kebiasaan menjaga jarak secara emosional ini kadang membuat orang-orang "
              "terdekatmu merasa sulit benar-benar memahami apa yang sedang kamu rasakan. Kecenderungan "
              "untuk lebih nyaman membicarakan ide dan konsep dibanding perasaan pribadi ini bisa "
              "membuat hubungan dekatmu terasa kurang intim, meski sebenarnya kamu peduli dengan cara "
              "yang berbeda. Kamu juga bisa terlalu terpaku pada idealisme, sampai sulit menerima "
              "bahwa dunia nyata tidak selalu bisa berjalan seideal yang kamu bayangkan.",
        "quote": "Ide-ide besar akan lebih bermakna kalau kamu juga membiarkan orang lain melihat "
                 "sisi personalmu.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba ceritakan satu perasaan pribadi, bukan hanya pendapat atau ide, kepada orang "
              "terdekatmu, dan biarkan mereka melihat sisi dirimu yang biasanya kamu jaga "
              "rapat-rapat. Latihan ini bisa dimulai dari hal kecil, seperti mengakui saat kamu "
              "merasa sedih atau khawatir, alih-alih langsung mengalihkan pembicaraan ke topik yang "
              "lebih abstrak dan aman secara emosional.",
    },
    "Pisces": {
        "tagline": "☉ Matahari di Pisces",
        "chip": "ZODIAK",
        "title": "Pisces — Jiwa yang Penuh Empati",
        "p1_label": "Siapa Kamu",
        "p1": "Matahari berada di rasi Pisces saat kamu lahir, memberimu kepekaan emosi dan imajinasi "
              "yang kaya. Kamu mudah merasakan apa yang orang lain rasakan, bahkan tanpa mereka perlu "
              "mengucapkannya. Dunia dalam kepalamu sering terasa sama nyatanya dengan dunia luar, dan "
              "hal itu membuatmu punya sisi kreatif yang jarang dimiliki orang lain. Kepekaanmu "
              "terhadap perasaan orang lain sering membuatmu jadi tempat curhat yang nyaman, karena "
              "orang merasa kamu benar-benar bisa memahami apa yang sedang mereka rasakan, bukan "
              "sekadar berpura-pura mendengarkan. Dalam bidang yang berhubungan dengan kreativitas "
              "atau seni, imajinasimu yang kaya bisa jadi sumber ide yang tidak pernah kering. Dalam "
              "hubungan, kamu cenderung memberi dengan tulus, kadang bahkan sebelum diminta, karena "
              "kamu bisa merasakan kebutuhan orang lain tanpa harus diberitahu.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Empati dan kepekaanmu membuat orang lain merasa benar-benar dipahami saat bersamamu. "
              "Kamu juga punya kemampuan membayangkan kemungkinan yang belum terpikirkan orang lain. "
              "Namun kepekaan yang besar ini kadang membuatmu terlalu mudah terbawa perasaan orang "
              "lain, sampai sulit membedakan mana emosimu sendiri dan mana yang sebenarnya bukan "
              "milikmu. Kecenderungan untuk lari ke dunia imajinasi saat kenyataan terasa berat ini "
              "juga bisa membuatmu menghindari masalah, alih-alih menghadapinya secara langsung. Kamu "
              "juga rentan dimanfaatkan oleh orang-orang yang tahu betapa mudahnya kamu berempati "
              "dan memberi.",
        "quote": "Merasakan perasaan orang lain itu indah, asal kamu tidak sampai kehilangan "
                 "perasaanmu sendiri di dalamnya.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Ketika merasa terbawa suasana hati orang lain, coba tanyakan pada diri "
              "sendiri, 'ini perasaanku atau perasaan mereka?', sebelum memutuskan apa yang perlu "
              "kamu lakukan. Kamu juga bisa melatih diri menetapkan batasan yang sehat, misalnya "
              "dengan mengenali kapan saatnya membantu orang lain, dan kapan saatnya memprioritaskan "
              "pemulihan emosimu sendiri terlebih dulu.",
    },
}
