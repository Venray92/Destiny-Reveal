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
              "takut itu menahanmu.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Keberanian dan inisiatifmu membuat orang lain sering menjadikanmu contoh soal cara "
              "memulai sesuatu. Kamu juga jujur soal apa yang kamu rasakan, sehingga orang tahu persis "
              "di mana posisi mereka di matamu. Namun semangat yang menyala cepat itu kadang juga "
              "padam secepat itu pula, membuat beberapa rencana besar berhenti di tengah jalan sebelum "
              "sempat kamu selesaikan.",
        "quote": "Keberanian akan terasa jauh lebih berarti kalau disertai dengan kesabaran untuk "
                 "menyelesaikannya.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba pilih satu hal kecil yang sempat kamu tinggalkan setengah jalan, lalu "
              "selesaikan sampai tuntas sebelum memulai hal baru yang lain. Rasakan bedanya ketika kamu "
              "benar-benar menuntaskan sesuatu, bukan cuma memulainya.",
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
              "bisa diandalkan dalam jangka panjang.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Ketekunan dan kesabaranmu membuat apa pun yang kamu kerjakan cenderung bertahan lama dan "
              "kokoh, bukan sekadar tren sesaat. Orang-orang merasa nyaman berada di dekatmu karena "
              "kamu jarang berubah pikiran tiba-tiba. Sayangnya, kenyamanan pada rutinitas itu kadang "
              "membuatmu enggan mencoba hal baru, bahkan ketika perubahan itu sebenarnya bisa membawa "
              "hal yang lebih baik untukmu.",
        "quote": "Stabilitas itu berharga, tapi sesekali membiarkan diri berubah juga bagian dari "
                 "tumbuh.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba lakukan satu hal kecil yang berbeda dari kebiasaanmu, sesuatu yang "
              "sebenarnya sudah lama ingin kamu coba tapi selalu ditunda. Tidak perlu besar, cukup "
              "untuk membuktikan pada dirimu sendiri bahwa perubahan kecil itu aman.",
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
              "pertemanan membuatmu terasa mudah akrab dengan banyak orang.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Keluwesanmu dalam berbicara dan beradaptasi membuat orang lain merasa nyaman bertukar "
              "cerita denganmu. Kamu juga cepat menangkap ide baru dan menghubungkannya dengan hal-hal "
              "yang sudah kamu ketahui sebelumnya. Namun rasa ingin tahu yang terlalu banyak arah "
              "kadang membuatmu kesulitan fokus menyelesaikan satu hal sampai benar-benar tuntas.",
        "quote": "Rasa ingin tahu akan membawamu jauh, asal kamu juga tahu kapan harus berhenti "
                 "menjelajah dan mulai mendalami.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Pilih satu proyek atau kebiasaan yang sudah lama ingin kamu kuasai, lalu fokuskan "
              "waktumu di situ secara konsisten tanpa berpindah ke hal lain. Lihat seberapa "
              "jauh kamu bisa berkembang kalau perhatianmu tidak terpecah.",
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
              "dengan sepenuh hati, bahkan sebelum diminta.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Empati dan kepedulianmu membuat orang lain merasa aman menceritakan hal-hal yang berat "
              "kepadamu. Kamu juga punya ingatan emosional yang kuat, sehingga bisa mengenali perasaan "
              "seseorang bahkan dari hal-hal kecil. Sisi sensitif ini terkadang membuatmu mudah "
              "terbawa suasana hati, atau menyimpan kekecewaan lebih lama dari yang seharusnya.",
        "quote": "Melindungi orang lain itu indah, tapi jangan sampai lupa melindungi perasaanmu "
                 "sendiri juga.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Ketika ada perasaan yang mengganjal, coba tuliskan atau ceritakan langsung "
              "kepada orang yang bersangkutan, alih-alih memendamnya sendirian sampai berlarut-larut.",
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
              "sudah lebih dulu bergerak.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kepemimpinan memang terasa seperti bagian alami dari dirimu. Kamu mampu membuat orang "
              "lain percaya pada arah yang kamu tunjukkan, bahkan sebelum kamu sendiri sepenuhnya "
              "yakin. Namun semangat besar itu terkadang membuatmu lupa untuk mendengarkan lebih dulu "
              "sebelum mengambil keputusan, padahal orang-orang di sekitarmu juga ingin didengar, "
              "bukan hanya diarahkan.",
        "quote": "Kepemimpinan yang paling kuat adalah yang tahu kapan harus diam dan mendengarkan.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba sekali saja menahan diri untuk tidak langsung memberi solusi ketika "
              "ada teman yang bercerita tentang masalahnya. Dengarkan saja sampai selesai. Kamu "
              "mungkin akan terkejut, karena terkadang orang hanya butuh didengar, bukan diarahkan, "
              "dan hal kecil ini justru akan membuat mereka semakin percaya padamu sebagai sosok "
              "pemimpin.",
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
              "terbaik dalam segala hal yang kamu kerjakan.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Ketelitian dan tanggung jawabmu membuat orang lain percaya menyerahkan pekerjaan "
              "penting kepadamu, karena tahu kamu akan mengurusnya dengan serius. Kamu juga jago "
              "melihat celah perbaikan yang orang lain lewatkan. Sayangnya, standar tinggi itu kadang "
              "berbalik menjadi kritik yang terlalu keras terhadap dirimu sendiri, sampai lupa "
              "mengapresiasi hal-hal yang sudah kamu capai dengan baik.",
        "quote": "Kesempurnaan itu indah untuk dikejar, tapi jangan sampai membuatmu lupa menghargai "
                 "kemajuan yang sudah ada.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Sebelum tidur, coba tuliskan satu hal kecil yang sudah kamu kerjakan dengan "
              "baik hari itu, tanpa langsung memikirkan apa yang masih kurang darinya.",
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
              "juga terasa penting bagimu, baik dalam penampilan maupun cara kamu menata hidup.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kemampuanmu melihat dari berbagai sisi membuatmu jadi penengah yang baik ketika ada "
              "konflik di sekitarmu. Orang-orang senang berdiskusi denganmu karena kamu jarang "
              "memihak secara buta. Namun kebiasaan mempertimbangkan terlalu banyak hal ini kadang "
              "membuatmu sulit mengambil keputusan sendiri, sampai akhirnya keinginanmu sendiri "
              "tertunda demi menjaga keharmonisan dengan orang lain.",
        "quote": "Keseimbangan yang sesungguhnya juga mencakup memberi ruang bagi keinginanmu "
                 "sendiri, bukan hanya orang lain.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Ketika dihadapkan pada satu pilihan kecil, coba ambil keputusan sendiri "
              "tanpa bertanya pendapat orang lain terlebih dulu, lalu perhatikan bagaimana rasanya "
              "mempercayai penilaianmu sendiri.",
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
              "membiarkan orang lain masuk terlalu dalam ke dunia pribadimu.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Ketajaman intuisi dan fokusmu membuatmu bisa menyelesaikan hal-hal yang orang lain "
              "anggap rumit atau menakutkan. Kamu juga setia dan penuh perhatian pada orang-orang yang "
              "sudah mendapat kepercayaanmu. Namun kecenderungan untuk menutup diri dan curiga secara "
              "berlebihan kadang membuat orang-orang di sekitarmu merasa sulit benar-benar dekat "
              "denganmu, meski niat mereka baik.",
        "quote": "Kedalaman perasaanmu adalah kekuatan, tapi kepercayaan juga butuh ruang untuk "
                 "tumbuh.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba bagikan satu hal yang biasanya kamu simpan sendiri kepada orang yang kamu percaya, "
              "sekecil apa pun itu, dan lihat bagaimana keterbukaan itu bisa mempererat "
              "hubungan kalian.",
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
              "apa yang kamu pikirkan, tanpa harus menebak-nebak.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Optimisme dan rasa ingin tahumu terhadap dunia membuat orang-orang di sekitarmu ikut "
              "terinspirasi untuk berani mencoba hal baru. Kamu juga jarang terjebak dalam masalah "
              "kecil karena selalu bisa melihat gambaran yang lebih besar. Sayangnya, kejujuranmu yang "
              "terlalu terus terang kadang menyakiti perasaan orang lain tanpa kamu sadari, dan "
              "keinginan bebasmu kadang membuatmu sulit berkomitmen dalam jangka panjang.",
        "quote": "Kebebasan akan terasa lebih indah kalau kamu juga memikirkan perasaan orang yang "
                 "kamu ajak bicara.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Sebelum menyampaikan pendapat yang cukup blak-blakan, coba jeda sebentar dan "
              "pikirkan bagaimana perasaan orang yang mendengarnya, tanpa harus mengubah kejujuranmu.",
    },
    "Capricorn": {
        "tagline": "☉ Matahari di Capricorn",
        "chip": "ZODIAK",
        "title": "Capricorn — Pekerja Keras yang Disiplin",
        "p1_label": "Siapa Kamu",
        "p1": "Matahari yang berada di rasi Capricorn saat kamu lahir memberimu ketekunan dan disiplin "
              "yang kuat dalam mengejar apa yang kamu inginkan. Kamu jarang mengharapkan hasil instan, "
              "dan lebih memilih membangun sesuatu perlahan namun kokoh dari fondasinya. Tanggung "
              "jawab terasa seperti bagian alami dari dirimu, bahkan sejak usia yang cukup muda.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kedisiplinan dan keteguhanmu membuat orang lain percaya bahwa apa pun yang kamu "
              "pegang pasti akan diselesaikan dengan baik. Kamu juga tidak mudah menyerah ketika "
              "menghadapi rintangan besar. Namun fokus yang terlalu besar pada pencapaian dan "
              "tanggung jawab kadang membuatmu lupa untuk beristirahat, atau menikmati momen-momen "
              "kecil yang sebenarnya juga layak disyukuri.",
        "quote": "Kesuksesan yang dibangun perlahan tetap butuh jeda untuk dinikmati di sepanjang "
                 "jalan.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Luangkan satu waktu khusus yang benar-benar bebas dari pekerjaan atau "
              "target, dan gunakan waktu itu untuk hal yang murni menyenangkan bagimu.",
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
              "punya kepedulian besar terhadap isu-isu yang lebih luas dari dirimu sendiri.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Orisinalitas dan idealismemu membuat orang lain terinspirasi untuk berpikir lebih "
              "terbuka. Kamu juga cenderung objektif dan tidak mudah terbawa emosi dalam menilai "
              "sesuatu. Namun kebiasaan menjaga jarak secara emosional ini kadang membuat orang-orang "
              "terdekatmu merasa sulit benar-benar memahami apa yang sedang kamu rasakan.",
        "quote": "Ide-ide besar akan lebih bermakna kalau kamu juga membiarkan orang lain melihat "
                 "sisi personalmu.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba ceritakan satu perasaan pribadi, bukan hanya pendapat atau ide, kepada orang "
              "terdekatmu, dan biarkan mereka melihat sisi dirimu yang biasanya kamu jaga "
              "rapat-rapat.",
    },
    "Pisces": {
        "tagline": "☉ Matahari di Pisces",
        "chip": "ZODIAK",
        "title": "Pisces — Jiwa yang Penuh Empati",
        "p1_label": "Siapa Kamu",
        "p1": "Matahari berada di rasi Pisces saat kamu lahir, memberimu kepekaan emosi dan imajinasi "
              "yang kaya. Kamu mudah merasakan apa yang orang lain rasakan, bahkan tanpa mereka perlu "
              "mengucapkannya. Dunia dalam kepalamu sering terasa sama nyatanya dengan dunia luar, dan "
              "hal itu membuatmu punya sisi kreatif yang jarang dimiliki orang lain.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Empati dan kepekaanmu membuat orang lain merasa benar-benar dipahami saat bersamamu. "
              "Kamu juga punya kemampuan membayangkan kemungkinan yang belum terpikirkan orang lain. "
              "Namun kepekaan yang besar ini kadang membuatmu terlalu mudah terbawa perasaan orang "
              "lain, sampai sulit membedakan mana emosimu sendiri dan mana yang sebenarnya bukan "
              "milikmu.",
        "quote": "Merasakan perasaan orang lain itu indah, asal kamu tidak sampai kehilangan "
                 "perasaanmu sendiri di dalamnya.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Ketika merasa terbawa suasana hati orang lain, coba tanyakan pada diri "
              "sendiri, 'ini perasaanku atau perasaan mereka?', sebelum memutuskan apa yang perlu "
              "kamu lakukan.",
    },
}
