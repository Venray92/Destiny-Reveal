"""
Konten interpretasi Love Language / Bahasa Cinta (5 kategori).

Berdasar teori 5 Love Languages Gary Chapman: Words of Affirmation (WA),
Quality Time (QT), Receiving Gifts (RG), Acts of Service (AS), Physical
Touch (PT). Konten merepresentasikan bahasa cinta UTAMA hasil kuesioner.
"""

LOVE_LANGUAGE_CONTENT = {
    "WA": {
        "tagline": "Kata yang diucapkan, tersimpan selamanya",
        "chip": "LOVE LANGUAGE",
        "title": "Kata-kata Afirmasi — Kamu Hidup dari Kalimat yang Tulus",
        "p1_label": "Siapa Kamu",
        "p1": "Buat kamu, kata-kata bukan sekadar bunyi yang lewat begitu saja, tapi sesuatu yang "
              "benar-benar menempel dan diputar ulang di kepala lama setelah diucapkan. Kamu merasa "
              "paling dicintai ketika seseorang secara spesifik bilang apa yang mereka hargai "
              "darimu, bukan cuma basa-basi umum yang bisa ditujukan ke siapa saja. Pujian yang "
              "detail, ucapan terima kasih yang disampaikan langsung, atau kalimat dukungan di "
              "saat kamu ragu, semua itu terasa seperti bahan bakar yang mengisi ulang energimu. "
              "Sebaliknya, diam yang berkepanjangan atau komentar yang terasa tajam bisa membekas "
              "jauh lebih dalam buatmu dibanding orang lain, walau niatnya cuma bercanda. Kamu "
              "sendiri juga cenderung ekspresif lewat kata, entah lewat pesan panjang yang jujur, "
              "catatan kecil, atau sekadar bilang langsung ke orang yang kamu sayangi kenapa "
              "mereka berarti. Kamu suka menyusun kalimat dengan hati-hati saat ingin menunjukkan "
              "perhatian, karena kamu tahu persis betapa berartinya rangkaian kata yang pas. Orang "
              "di sekitarmu biasanya bisa merasakan ketulusanmu lewat cara kamu memilih kata, "
              "bukan cuma dari apa yang kamu lakukan. Buatmu, mendengar \"aku bangga sama kamu\" "
              "atau \"terima kasih udah jadi diri kamu\" punya bobot yang jauh lebih besar "
              "daripada yang orang lain sering sadari.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kepekaanmu terhadap kata membuatmu jago membaca nada dan maksud di balik kalimat "
              "orang lain, dan kamu juga pandai memberi dukungan verbal yang bikin orang di "
              "sekitarmu merasa dilihat. Kamu tahu kapan seseorang butuh didengar lewat kata-kata, "
              "dan itu bikin banyak orang nyaman curhat atau berbagi cerita denganmu. Tapi "
              "sensitivitas ini juga berarti kamu bisa terlalu menganalisis satu kalimat yang "
              "sebenarnya diucapkan tanpa maksud apa-apa, lalu memikirkannya berulang kali sampai "
              "muncul kekhawatiran yang tidak perlu. Kesalahpahaman paling umum muncul saat "
              "pasangan atau teman yang bahasa cintanya berbeda menunjukkan sayang lewat tindakan, "
              "bukan kata, sehingga kamu merasa kurang diyakinkan padahal mereka sebenarnya peduli "
              "dengan caranya sendiri. Kamu juga bisa terlalu berharap orang lain otomatis tahu "
              "ucapan seperti apa yang kamu butuhkan, padahal setiap orang punya cara berbeda "
              "dalam mengekspresikan perhatian.",
        "quote": "Kata yang tulus tidak butuh diulang berkali-kali untuk terasa nyata, ia cukup "
                 "diucapkan sekali dengan benar.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba mulai bilang secara spesifik apa yang kamu butuhkan dari orang terdekatmu, "
              "misalnya \"aku bakal senang banget kalau kamu bilang kamu bangga sama aku\", "
              "daripada menunggu mereka menebak sendiri. Latih juga dirimu untuk tidak langsung "
              "menyimpulkan hal buruk dari kalimat yang terdengar datar atau singkat, karena tidak "
              "semua orang terbiasa merangkai kata sepertimu. Sesekali perhatikan juga cara orang "
              "lain menunjukkan sayang lewat hal-hal di luar kata-kata, karena bisa jadi itu adalah "
              "bentuk perhatian yang sama tulusnya, hanya dibungkus dengan cara berbeda. Selain "
              "bahasa cinta utamamu ini, biasanya setiap orang juga punya bahasa cinta kedua yang "
              "cukup kuat, dan ada baiknya kamu mulai mengenali itu juga supaya kamu makin paham "
              "ragam cara kamu bisa merasa dicintai.",
        "domains": {
            "karir": "Kamu berkembang di lingkungan kerja yang terbuka memberi apresiasi verbal, "
                     "misalnya atasan yang menyebut kontribusimu di depan tim atau rekan kerja yang "
                     "menyampaikan terima kasih secara langsung. Tanpa itu, kamu bisa merasa "
                     "kerjamu tidak terlihat walau sebenarnya dihargai, karena kamu terbiasa "
                     "mengukur pengakuan lewat apa yang diucapkan orang, bukan cuma dari hasil "
                     "kerja itu sendiri. Kamu juga cenderung jadi rekan kerja yang rajin memberi "
                     "masukan dan pujian yang membangun ke orang lain, sesuatu yang bikin suasana "
                     "tim jadi lebih hangat. Namun, kalau lingkungan kerjamu memang jarang memberi "
                     "umpan balik verbal, kamu perlu belajar mencari tanda penghargaan dari sumber "
                     "lain, seperti kepercayaan yang diberikan lewat tanggung jawab baru. *PR: "
                     "minta umpan balik langsung ke atasan atau rekan kerja soal kontribusimu, "
                     "daripada menunggu pujian datang dengan sendirinya.*",
            "asmara": "Dalam hubungan romantis, kamu paling merasa dicintai lewat ucapan sayang, "
                      "pujian yang tulus, dan kalimat penenang saat kamu sedang cemas. Kamu juga "
                      "rajin mengungkapkan perasaanmu lewat kata, entah lewat pesan panjang atau "
                      "obrolan mendalam, dan berharap pasangan melakukan hal serupa. Kalau "
                      "pasanganmu tipe yang lebih pendiam atau menunjukkan sayang lewat tindakan, "
                      "kamu bisa merasa ada jarak emosional meski sebenarnya perhatian itu ada, "
                      "hanya disampaikan dengan cara yang berbeda. Penting buatmu untuk sadar "
                      "bahwa minimnya kata-kata bukan berarti minimnya cinta, tapi bisa jadi cara "
                      "ekspresi yang memang tidak sama dengan caramu. *PR: ajak pasangan bicara "
                      "soal cara masing-masing biasa menunjukkan sayang, supaya kalian sama-sama "
                      "paham tanpa harus menebak.*",
            "keuangan": "Kamu cenderung lebih menghargai pengalaman atau barang yang datang dengan "
                        "ucapan tulus dibanding nilai nominalnya, dan kadang rela mengeluarkan "
                        "uang untuk hal-hal yang berhubungan dengan komunikasi, seperti kartu "
                        "ucapan, kelas menulis, atau hadiah yang disertai pesan personal. Kamu juga "
                        "cukup terbuka membicarakan keuangan secara verbal dengan pasangan atau "
                        "keluarga, karena bagimu ngobrol jujur soal uang adalah bentuk kepercayaan. "
                        "Risikonya, kamu bisa kurang teliti pada detail angka karena lebih fokus "
                        "pada kesepakatan lisan dibanding pencatatan tertulis. *PR: mulai catat "
                        "kesepakatan keuangan penting secara tertulis, bukan cuma mengandalkan "
                        "obrolan lisan yang gampang lupa detailnya.*",
            "kesehatan": "Secara emosional, kamu butuh ruang untuk didengar dan divalidasi lewat "
                         "kata supaya merasa aman, dan kalau perasaanmu terus dipendam tanpa "
                         "disampaikan, itu bisa menumpuk jadi beban yang cukup berat. Kamu juga "
                         "rentan terpengaruh kuat oleh kalimat kritik yang tajam, bahkan yang "
                         "sebenarnya tidak dimaksudkan untuk menyakiti, sehingga penting buatmu "
                         "punya ruang aman untuk bicara jujur soal perasaan. Kebiasaan menulis "
                         "jurnal atau bercerita ke orang yang bisa dipercaya biasanya sangat "
                         "membantu buatmu untuk melepaskan apa yang dipikirkan. *PR: sediakan waktu "
                         "rutin untuk cerita perasaanmu ke orang yang kamu percaya, daripada "
                         "menyimpannya sendirian.*",
        },
    },
    "QT": {
        "tagline": "Kehadiran yang penuh, bukan sekadar berada di ruang yang sama",
        "chip": "LOVE LANGUAGE",
        "title": "Waktu Berkualitas — Kehadiran adalah Cinta Bagimu",
        "p1_label": "Siapa Kamu",
        "p1": "Buat kamu, cinta terasa paling nyata saat ada seseorang yang benar-benar hadir "
              "bersamamu, tanpa gangguan, tanpa setengah hati. Bukan soal berapa lama waktu yang "
              "dihabiskan, tapi seberapa penuh perhatian orang itu saat sedang bersamamu, entah "
              "lagi ngobrol santai atau melakukan aktivitas bareng. Kamu paling merasa disayang "
              "ketika seseorang menyisihkan waktu khusus untukmu, meletakkan ponselnya, dan benar-"
              "benar mendengarkan tanpa terburu-buru pindah topik atau kegiatan lain. Momen sekecil "
              "apa pun jadi berarti kalau dilakukan dengan fokus penuh, seperti masak bareng, jalan "
              "kaki tanpa tujuan tertentu, atau sekadar duduk berdua tanpa banyak bicara. Kamu juga "
              "cenderung mengingat detail dari momen-momen kebersamaan itu, karena bagimu momen "
              "seperti itu adalah bukti nyata bahwa seseorang memilih untuk ada di situ bersamamu. "
              "Sebaliknya, kalau seseorang terus-terusan terganggu oleh hal lain saat sedang "
              "bersamamu, kamu bisa merasa diabaikan meski mereka secara fisik ada di dekatmu. Kamu "
              "juga cenderung berusaha menciptakan waktu berkualitas untuk orang-orang yang kamu "
              "sayangi, entah dengan mengajak ngobrol serius atau merancang kegiatan bersama. Bagi "
              "orang lain, kehadiranmu yang fokus dan penuh perhatian sering terasa menenangkan.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kemampuanmu untuk hadir penuh membuat orang di sekitarmu merasa benar-benar "
              "didengar dan diprioritaskan, sesuatu yang tidak semua orang bisa berikan. Kamu juga "
              "jago menciptakan momen kebersamaan yang berkesan, bahkan dari aktivitas sederhana "
              "sekalipun. Namun, kebutuhanmu akan waktu bersama yang fokus kadang berbenturan "
              "dengan kesibukan orang lain, dan kamu bisa merasa dinomorduakan kalau seseorang "
              "sering membatalkan rencana atau terus sibuk dengan hal lain saat sedang bersamamu. "
              "Kesalahpahaman yang sering muncul, orang yang sayang padamu tapi sibuk bisa terasa "
              "seperti tidak peduli di matamu, padahal mereka sebenarnya hanya kewalahan dengan "
              "banyak hal, bukan karena tidak menghargaimu. Kamu juga perlu hati-hati supaya "
              "kebutuhan akan waktu bersama tidak berubah jadi tuntutan yang membuat orang lain "
              "merasa tertekan.",
        "quote": "Waktu yang diberikan dengan penuh perhatian selalu terasa lebih besar dari "
                 "jumlah jam yang tertulis di jam tangan.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba sampaikan secara terbuka ke orang terdekatmu kalau kamu butuh waktu khusus "
              "bersama, tanpa distraksi, daripada memendam kekecewaan kalau itu tidak terjadi "
              "dengan sendirinya. Latih juga dirimu untuk memahami bahwa kesibukan orang lain "
              "bukan selalu tanda mereka tidak peduli, melainkan sering kali soal manajemen waktu "
              "yang memang sedang padat. Buat kesepakatan kecil, misalnya waktu tanpa gawai selama "
              "beberapa saat, supaya kebutuhanmu akan kehadiran penuh tetap terpenuhi tanpa harus "
              "menuntut waktu yang terlalu banyak. Selain bahasa cinta utamamu ini, biasanya setiap "
              "orang juga punya bahasa cinta kedua yang cukup kuat, dan ada baiknya kamu mulai "
              "mengenali itu juga supaya kamu makin paham ragam cara kamu bisa merasa dicintai.",
        "domains": {
            "karir": "Kamu bekerja paling baik dalam kolaborasi yang melibatkan diskusi langsung "
                     "dan fokus penuh, seperti rapat empat mata atau sesi brainstorming yang benar-"
                     "benar interaktif, dibanding komunikasi yang serba singkat lewat pesan teks. "
                     "Kamu juga menghargai atasan atau rekan kerja yang menyediakan waktu untuk "
                     "benar-benar mendengarkan idemu, bukan sekadar menjawab cepat sambil "
                     "melakukan hal lain. Risikonya, kamu bisa merasa kurang terhubung dengan tim "
                     "yang lebih banyak berkomunikasi lewat pesan singkat atau rapat yang terburu-"
                     "buru. Kamu cenderung membangun hubungan kerja yang lebih dalam dengan orang "
                     "yang mau menyisihkan waktu untuk ngobrol di luar urusan pekerjaan. *PR: "
                     "jadwalkan sesi ngobrol empat mata dengan rekan atau atasan secara rutin, "
                     "supaya kebutuhan koneksimu tetap terpenuhi di tengah kesibukan kerja.*",
            "asmara": "Dalam hubungan romantis, kamu paling bahagia saat pasangan menyisihkan "
                      "waktu khusus untuk berdua, tanpa gangguan gawai atau pikiran yang melayang "
                      "ke hal lain. Kamu cenderung mengingat detail momen kebersamaan kalian, dan "
                      "itu jadi salah satu cara utamamu mengukur kedekatan hubungan. Tapi kalau "
                      "pasanganmu sedang sibuk dengan pekerjaan atau urusan lain, kamu bisa cepat "
                      "merasa terabaikan, padahal itu belum tentu berarti mereka kurang sayang. "
                      "Penting buatmu untuk membedakan antara kesibukan sementara dan kurangnya "
                      "perhatian yang sebenarnya, supaya tidak salah menilai situasi. *PR: sepakati "
                      "waktu rutin berdua dengan pasangan, sekecil apa pun, sebagai ruang khusus "
                      "yang bebas dari gangguan.*",
            "keuangan": "Kamu cenderung lebih memilih menghabiskan uang untuk pengalaman bersama "
                        "dibanding barang, seperti liburan singkat, makan berdua, atau kegiatan "
                        "yang bisa dinikmati sama-sama, karena bagimu momen itu punya nilai lebih "
                        "dari sekadar barang fisik. Kamu juga cukup rela menyisihkan anggaran "
                        "khusus untuk aktivitas bersama orang terdekat, meski itu berarti "
                        "mengurangi pengeluaran untuk hal lain. Sisi yang perlu diperhatikan, kamu "
                        "bisa kurang memikirkan tabungan jangka panjang karena terlalu fokus pada "
                        "pengalaman yang terasa berharga saat ini. *PR: sisihkan sebagian dana "
                        "khusus untuk pengalaman bersama, tapi tetap alokasikan porsi tabungan "
                        "supaya kebutuhan jangka panjang tidak terlewat.*",
            "kesehatan": "Secara emosional, kamu butuh waktu yang tidak terburu-buru untuk merasa "
                         "tenang dan terhubung, dan jadwal yang terlalu padat tanpa jeda kebersamaan "
                         "bisa bikin kamu merasa hampa meski secara fisik baik-baik saja. Kesepian "
                         "juga terasa lebih berat buatmu dibanding orang lain, karena kamu mengukur "
                         "kedekatan lewat waktu yang dihabiskan bersama. Kamu perlu menjaga "
                         "keseimbangan supaya kebutuhan akan kebersamaan tidak membuatmu mengabaikan "
                         "waktu sendiri yang juga penting untuk memulihkan energi. *PR: jadwalkan "
                         "waktu berkualitas bersama orang terdekat secara rutin, sekaligus sisakan "
                         "waktu sendiri untuk menjaga keseimbangan emosimu.*",
        },
    },
    "RG": {
        "tagline": "Sesuatu yang bisa digenggam, mengingatkan bahwa kamu dipikirkan",
        "chip": "LOVE LANGUAGE",
        "title": "Menerima Hadiah — Simbol Kecil yang Berarti Besar",
        "p1_label": "Siapa Kamu",
        "p1": "Buat kamu, sebuah hadiah bukan soal harganya, tapi soal usaha dan perhatian yang "
              "tersimpan di baliknya. Kamu merasa paling disayang ketika seseorang memikirkan "
              "sesuatu khusus untukmu, entah itu barang kecil yang mengingatkan mereka padamu, "
              "sesuatu yang kamu sebut sekilas dan ternyata diingat, atau benda buatan tangan yang "
              "dibuat dengan usaha. Bagimu, hadiah adalah simbol yang bisa dipegang dari perhatian "
              "yang sebenarnya sulit diungkapkan dengan cara lain. Kamu juga cenderung menyimpan "
              "barang-barang pemberian orang terdekat dengan hati-hati, karena benda itu punya "
              "cerita dan makna yang jauh lebih besar dari sekadar fungsinya. Saat kamu ingin "
              "menunjukkan sayang, kamu sering memikirkan hadiah yang pas untuk orang tersebut, "
              "bahkan kalau itu cuma benda kecil yang murah, karena buatmu ketepatan pilihan jauh "
              "lebih penting dari nilai uangnya. Momen tidak diberi apa-apa saat momen penting bisa "
              "terasa menyakitkan buatmu, bukan karena kamu materialistis, tapi karena kamu "
              "mengasosiasikan hadiah dengan bukti bahwa seseorang memikirkanmu. Kamu juga peka "
              "membaca kapan waktu yang tepat untuk memberi kejutan kecil ke orang-orang yang kamu "
              "sayangi.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kepekaanmu terhadap detail membuatmu jago memilih hadiah yang benar-benar cocok "
              "untuk orang lain, sesuatu yang sering bikin penerimanya merasa benar-benar "
              "dimengerti. Kamu juga rajin mengingat momen-momen penting orang terdekat, dan itu "
              "membuatmu jadi sosok yang diandalkan saat ada perayaan atau momen spesial. Namun, "
              "kebutuhanmu akan simbol fisik ini kadang disalahpahami sebagai sifat materialistis, "
              "padahal buatmu ini murni soal makna di balik pemberian, bukan soal nilai uangnya. "
              "Orang yang bahasa cintanya berbeda kadang lupa memberi hadiah bukan karena tidak "
              "sayang, tapi karena mereka menunjukkan perhatian lewat cara lain, dan ini bisa bikin "
              "kamu merasa kurang diperhatikan padahal sebenarnya tidak begitu. Kamu juga perlu "
              "berhati-hati supaya harapan akan hadiah tidak berubah jadi kekecewaan berlebihan "
              "saat momen tertentu terlewat tanpa pemberian apa pun.",
        "quote": "Hadiah yang paling berkesan bukan yang paling mahal, tapi yang menunjukkan "
                 "seseorang benar-benar memperhatikanmu.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba sampaikan ke orang terdekatmu bahwa kamu menghargai simbol fisik, sekecil "
              "apa pun bentuknya, supaya mereka paham cara sederhana untuk membuatmu merasa "
              "disayang. Latih juga dirimu untuk melihat bentuk perhatian lain sebagai hal yang "
              "sama berartinya, bahkan kalau itu tidak datang dalam bentuk benda yang bisa "
              "dipegang. Kalau kamu merasa kecewa karena tidak menerima hadiah di momen tertentu, "
              "coba tanya dulu ke diri sendiri apakah orang itu memang menunjukkan sayang lewat "
              "cara lain yang mungkin luput kamu sadari. Selain bahasa cinta utamamu ini, biasanya "
              "setiap orang juga punya bahasa cinta kedua yang cukup kuat, dan ada baiknya kamu "
              "mulai mengenali itu juga supaya kamu makin paham ragam cara kamu bisa merasa "
              "dicintai.",
        "domains": {
            "karir": "Kamu menghargai pengakuan yang berbentuk konkret di tempat kerja, seperti "
                     "sertifikat, bonus kecil, atau suvenir dari perusahaan, karena benda-benda itu "
                     "terasa seperti bukti nyata dari kerja kerasmu yang diakui. Kamu juga sering "
                     "jadi orang yang mengingat momen penting rekan kerja, seperti ulang tahun atau "
                     "pencapaian tertentu, dan menunjukkan perhatian lewat pemberian kecil. Risiko "
                     "yang perlu diperhatikan, kamu bisa merasa kurang dihargai kalau kontribusimu "
                     "hanya diakui secara lisan tanpa bentuk konkret apa pun, padahal sebenarnya "
                     "penghargaan itu tetap ada. Kamu perlu belajar melihat kepercayaan yang "
                     "diberikan lewat tanggung jawab baru sebagai bentuk pengakuan yang sama "
                     "berartinya. *PR: kalau memungkinkan, usulkan sistem penghargaan kecil yang "
                     "konkret di timmu, sekaligus latih diri menerima pengakuan verbal dengan sama "
                     "senangnya.*",
            "asmara": "Dalam hubungan romantis, kamu merasa paling dicintai saat pasangan "
                      "memberikan sesuatu yang menunjukkan mereka benar-benar mendengarkan apa yang "
                      "kamu suka, bukan sekadar hadiah asal-asalan di momen tertentu. Kamu juga "
                      "cenderung menyimpan barang-barang pemberian pasangan sebagai pengingat "
                      "momen-momen berharga dalam hubungan kalian. Tapi kalau pasanganmu bukan tipe "
                      "yang terbiasa memberi hadiah, kamu bisa salah menyimpulkan bahwa mereka "
                      "kurang perhatian, padahal mereka mungkin menunjukkan sayang lewat kata-kata "
                      "atau tindakan yang sama tulusnya. Penting buatmu untuk membuka obrolan jujur "
                      "soal ini, supaya tidak ada kesalahpahaman yang berlarut-larut. *PR: beri tahu "
                      "pasangan secara langsung kalau hadiah kecil, sekecil apa pun, sangat berarti "
                      "buatmu, daripada berharap mereka menebaknya sendiri.*",
            "keuangan": "Kamu senang membelikan hadiah untuk orang lain dan cukup royal soal "
                        "ini, kadang mengeluarkan lebih dari yang direncanakan demi memberi sesuatu "
                        "yang pas untuk orang tersayang. Kamu juga menghargai barang-barang yang "
                        "punya makna personal, sehingga kadang lebih memilih membeli sesuatu yang "
                        "unik dibanding yang murni fungsional. Ini bisa jadi tantangan kalau tidak "
                        "diimbangi dengan perencanaan, karena pengeluaran untuk hadiah bisa "
                        "menumpuk tanpa disadari, apalagi kalau banyak momen penting terjadi "
                        "berdekatan. *PR: buat pos anggaran khusus untuk hadiah setiap ada rencana "
                        "pengeluaran, supaya kebiasaan memberi tetap terjaga tanpa mengganggu "
                        "keuangan lain.*",
            "kesehatan": "Secara emosional, kamu butuh bukti nyata bahwa dirimu diperhatikan supaya "
                         "merasa aman dalam hubungan, dan kalau bukti itu tidak pernah muncul dalam "
                         "bentuk apa pun, kamu bisa mulai meragukan seberapa besar kamu dianggap "
                         "penting. Kamu juga cenderung menyimpan kenangan lewat benda-benda "
                         "fisik, dan itu bisa jadi sumber ketenangan tersendiri saat kamu merasa "
                         "sendirian atau butuh pengingat bahwa ada orang yang peduli. Penting untuk "
                         "diingat, ketenangan emosionalmu tidak seharusnya bergantung sepenuhnya "
                         "pada benda, karena rasa aman yang sehat juga perlu datang dari dalam "
                         "dirimu sendiri. *PR: sesekali coba beri hadiah kecil untuk dirimu sendiri "
                         "sebagai bentuk penghargaan, tanpa menunggu orang lain memberikannya.*",
        },
    },
    "AS": {
        "tagline": "Tindakan nyata berbicara lebih keras dari sekadar kata",
        "chip": "LOVE LANGUAGE",
        "title": "Tindakan Pelayanan — Kamu Percaya pada Cinta yang Dikerjakan",
        "p1_label": "Siapa Kamu",
        "p1": "Buat kamu, cinta paling terasa nyata lewat hal-hal yang dikerjakan, bukan sekadar "
              "diucapkan. Kamu merasa paling disayang ketika seseorang meringankan bebanmu lewat "
              "tindakan konkret, entah itu membantu menyelesaikan tugas, menyiapkan sesuatu tanpa "
              "diminta, atau sekadar mengerjakan hal kecil yang kamu sebenarnya bisa lakukan "
              "sendiri tapi terasa lebih berarti kalau dibantu. Bagimu, ada perbedaan besar antara "
              "orang yang bilang mau membantu dan orang yang benar-benar melakukannya, dan kamu "
              "lebih percaya pada yang kedua. Kamu sendiri juga cenderung menunjukkan sayang lewat "
              "tindakan, seperti menyiapkan sesuatu untuk orang terdekat, membantu menyelesaikan "
              "pekerjaan mereka, atau mengambil alih tugas yang terasa berat buat mereka. Kamu "
              "jarang banyak bicara soal perasaanmu, tapi orang yang mengenalmu dengan baik tahu "
              "bahwa kesibukanmu membantu adalah caramu menunjukkan perhatian. Melihat hasil kerja "
              "nyata yang membantu orang lain memberimu kepuasan tersendiri, karena bagimu itu "
              "adalah bukti paling jujur dari niat baik seseorang. Kamu juga cenderung memperhatikan "
              "hal-hal kecil yang bisa dibantu tanpa perlu diminta, karena kamu terbiasa membaca "
              "kebutuhan orang lain lewat pengamatan, bukan lewat obrolan panjang.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Keandalanmu dalam membantu membuat orang di sekitarmu merasa bisa benar-benar "
              "mengandalkanmu di saat sulit, dan itu membangun rasa percaya yang kuat dalam "
              "hubungan apa pun. Kamu juga jago melihat kebutuhan praktis orang lain sebelum "
              "mereka sempat meminta, sesuatu yang bikin bantuanmu terasa tulus dan tidak dipaksakan. "
              "Namun, kecenderunganmu untuk terus membantu bisa membuatmu kelelahan kalau tidak "
              "dijaga batasnya, apalagi kalau bantuan itu tidak pernah dibalas dengan cara yang "
              "sama. Kesalahpahaman yang sering muncul, orang yang bahasa cintanya berbeda bisa "
              "terlihat kurang peduli di matamu kalau mereka lebih banyak mengungkapkan sayang "
              "lewat kata dibanding tindakan, padahal perhatian mereka sama tulusnya. Kamu juga "
              "perlu hati-hati karena kadang menunjukkan sayang lewat bantuan tanpa diminta bisa "
              "disalahartikan sebagai ikut campur, padahal niatmu murni untuk meringankan beban "
              "orang lain.",
        "quote": "Tindakan kecil yang dikerjakan dengan tulus sering berbicara lebih jujur "
                 "daripada janji yang panjang.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba sampaikan secara langsung ke orang terdekatmu bahwa bantuan konkret adalah "
              "cara utama kamu merasa disayang, supaya mereka tahu bentuk perhatian seperti apa "
              "yang paling berarti buatmu. Latih juga dirimu untuk sesekali meminta bantuan, bukan "
              "cuma memberi, karena membiarkan orang lain membantumu juga bentuk kepercayaan yang "
              "penting dalam hubungan. Perhatikan batasanmu sendiri supaya kebiasaan membantu tidak "
              "membuatmu kelelahan atau merasa dimanfaatkan, terutama kalau bantuan itu jarang "
              "dibalas. Selain bahasa cinta utamamu ini, biasanya setiap orang juga punya bahasa "
              "cinta kedua yang cukup kuat, dan ada baiknya kamu mulai mengenali itu juga supaya "
              "kamu makin paham ragam cara kamu bisa merasa dicintai.",
        "domains": {
            "karir": "Kamu adalah rekan kerja yang diandalkan karena selalu siap membantu "
                     "menyelesaikan tugas tim tanpa banyak drama, dan kamu lebih percaya pada hasil "
                     "kerja nyata dibanding janji atau presentasi yang berlebihan. Kamu juga cepat "
                     "menawarkan bantuan saat melihat rekan kerja kewalahan, bahkan sebelum mereka "
                     "sempat meminta. Risikonya, kamu bisa kelebihan beban karena terlalu sering "
                     "mengambil alih pekerjaan orang lain, dan itu bisa membuatmu lelah tanpa "
                     "disadari tim. Kamu juga cenderung menilai kontribusi orang lain lebih dari "
                     "apa yang mereka kerjakan dibanding apa yang mereka katakan di rapat. *PR: "
                     "belajar bilang tidak pada permintaan bantuan yang di luar kapasitasmu, "
                     "supaya kualitas kerjamu sendiri tetap terjaga.*",
            "asmara": "Dalam hubungan romantis, kamu menunjukkan sayang lewat tindakan nyata, "
                      "seperti menyiapkan sesuatu untuk pasangan atau membantu menyelesaikan hal "
                      "yang berat buat mereka, dan kamu merasa paling dicintai kalau diperlakukan "
                      "dengan cara yang sama. Kamu cenderung tidak terlalu banyak mengungkapkan "
                      "perasaan lewat kata, sehingga pasangan perlu memperhatikan tindakanmu untuk "
                      "benar-benar memahami seberapa besar kamu peduli. Kalau pasanganmu lebih "
                      "ekspresif lewat kata-kata dibanding tindakan, kamu bisa merasa kurang "
                      "yakin akan perhatian mereka, padahal itu cuma perbedaan cara mengekspresikan "
                      "sayang. *PR: sesekali ucapkan juga perasaanmu lewat kata-kata ke pasangan, "
                      "supaya mereka tidak hanya bergantung menebak dari tindakanmu.*",
            "keuangan": "Kamu cenderung menghabiskan uang atau waktu untuk hal-hal yang membantu "
                        "meringankan beban orang lain, seperti membayar lebih dulu untuk urusan "
                        "bersama atau membeli alat yang memudahkan pekerjaan orang terdekat. Kamu "
                        "juga lebih suka berinvestasi pada layanan yang menghemat waktu dan tenaga "
                        "dibanding barang yang sekadar terlihat bagus. Sisi yang perlu diperhatikan, "
                        "kamu kadang lupa mencatat berapa banyak yang sudah kamu keluarkan untuk "
                        "membantu orang lain, sehingga bisa mengganggu perencanaan keuanganmu "
                        "sendiri. *PR: catat pengeluaran yang kamu keluarkan untuk membantu orang "
                        "lain, supaya kebiasaan baik ini tidak mengorbankan kestabilan keuanganmu "
                        "sendiri.*",
            "kesehatan": "Secara emosional, kamu butuh merasa berguna dan produktif supaya merasa "
                         "baik-baik saja, dan kalau kamu tidak bisa membantu siapa pun dalam waktu "
                         "lama, itu bisa membuatmu merasa gelisah atau kurang berarti. Kamu juga "
                         "rentan mengabaikan kebutuhan istirahatmu sendiri karena terlalu fokus "
                         "memenuhi kebutuhan orang lain terlebih dulu. Penting buatmu untuk sadar "
                         "bahwa merawat diri sendiri juga bentuk tindakan pelayanan yang sama "
                         "pentingnya, hanya saja ditujukan untuk dirimu sendiri. *PR: jadwalkan "
                         "waktu khusus untuk merawat dirimu sendiri, dan perlakukan itu sepenting "
                         "kamu memperlakukan kebutuhan orang lain.*",
        },
    },
    "PT": {
        "tagline": "Sentuhan yang tenang, mengatakan apa yang kata tak sanggup ucapkan",
        "chip": "LOVE LANGUAGE",
        "title": "Sentuhan Fisik — Kedekatan yang Kamu Rasakan lewat Raga",
        "p1_label": "Siapa Kamu",
        "p1": "Buat kamu, kedekatan fisik adalah cara paling langsung untuk merasakan bahwa "
              "seseorang benar-benar hadir dan peduli. Kamu merasa paling dicintai lewat hal-hal "
              "sederhana seperti pelukan, rangkulan, genggaman tangan, atau sekadar duduk "
              "berdekatan dengan orang yang kamu sayangi. Sentuhan yang tulus terasa lebih "
              "meyakinkan buatmu dibanding kata-kata panjang, karena ada sesuatu yang langsung "
              "tersampaikan lewat kontak fisik yang sulit dijelaskan dengan kalimat. Kamu juga "
              "cenderung nyaman berada dekat secara fisik dengan orang-orang terdekatmu, entah itu "
              "lewat pelukan singkat saat bertemu atau sekadar duduk bersebelahan tanpa jarak yang "
              "canggung. Saat kamu sedang cemas atau sedih, dipeluk atau ditemani secara fisik "
              "terasa jauh lebih menenangkan buatmu dibanding dinasihati panjang lebar. Kamu juga "
              "mengekspresikan sayang lewat sentuhan yang wajar, seperti menepuk pundak, "
              "merangkul, atau memegang tangan orang yang kamu percaya. Ketiadaan sentuhan dalam "
              "waktu lama bisa bikin kamu merasa ada jarak, meski secara emosional hubungan itu "
              "sebenarnya baik-baik saja. Buatmu, kedekatan fisik yang wajar dan nyaman adalah "
              "bahasa yang paling jujur untuk menyampaikan bahwa seseorang ada di sisimu.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kepekaanmu terhadap sentuhan membuatmu jago menenangkan orang lain lewat kehadiran "
              "fisik yang wajar, seperti merangkul teman yang sedang sedih atau memegang tangan "
              "seseorang yang sedang cemas. Kamu juga cenderung membangun kedekatan yang terasa "
              "hangat dan personal dengan orang-orang terdekatmu. Namun, kebutuhanmu akan sentuhan "
              "perlu selalu disesuaikan dengan kenyamanan orang lain, karena tidak semua orang "
              "merasa nyaman dengan kontak fisik yang sama denganmu, terutama di tahap awal "
              "hubungan atau pertemanan. Kesalahpahaman yang sering muncul, orang yang bahasa "
              "cintanya berbeda bisa terasa jauh atau dingin di matamu kalau mereka jarang "
              "melakukan kontak fisik, padahal mereka menunjukkan sayang lewat cara lain yang sama "
              "tulusnya. Penting buatmu untuk selalu menghormati batas kenyamanan orang lain, "
              "supaya kebutuhan akan sentuhan tidak membuat orang lain merasa tidak nyaman.",
        "quote": "Kadang pelukan yang tulus bisa mengatakan apa yang tidak sanggup diucapkan "
                 "oleh kata-kata sekalipun.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba sampaikan ke orang terdekatmu bahwa kontak fisik yang wajar, seperti pelukan "
              "atau genggaman tangan, adalah cara yang sangat berarti buatmu untuk merasa dekat, "
              "supaya mereka paham tanpa harus menebak. Latih juga dirimu untuk selalu bertanya "
              "atau memperhatikan kenyamanan orang lain sebelum melakukan kontak fisik, terutama "
              "pada orang yang belum terlalu dekat denganmu. Kalau orang terdekatmu tidak terlalu "
              "nyaman dengan sentuhan, coba cari bentuk kedekatan lain yang tetap terasa hangat "
              "buatmu, seperti duduk berdekatan atau kontak mata yang tulus. Selain bahasa cinta "
              "utamamu ini, biasanya setiap orang juga punya bahasa cinta kedua yang cukup kuat, "
              "dan ada baiknya kamu mulai mengenali itu juga supaya kamu makin paham ragam cara "
              "kamu bisa merasa dicintai.",
        "domains": {
            "karir": "Di lingkungan kerja, kebutuhanmu akan kedekatan fisik biasanya muncul lewat "
                     "hal-hal kecil dan profesional, seperti tos setelah pencapaian tim atau "
                     "tepukan pundak sebagai bentuk dukungan, yang bikin suasana kerja terasa lebih "
                     "hangat buatmu. Kamu juga cenderung lebih nyaman bekerja langsung berdampingan "
                     "dengan rekan tim dibanding komunikasi jarak jauh yang serba lewat layar. "
                     "Penting untuk selalu menjaga batas profesional dalam konteks kerja, karena "
                     "kenyamanan terhadap kontak fisik bisa sangat berbeda antar orang di lingkungan "
                     "profesional. Kamu bisa tetap membangun kedekatan tim lewat cara lain yang "
                     "tetap terasa personal tanpa harus mengandalkan sentuhan. *PR: cari cara lain "
                     "untuk membangun kedekatan tim di kantor, seperti obrolan santai atau kegiatan "
                     "bersama, supaya kebutuhanmu akan kedekatan tetap terpenuhi secara wajar.*",
            "asmara": "Dalam hubungan romantis, kamu merasa paling dekat dan aman lewat kontak "
                      "fisik yang wajar dan konsisten, seperti pelukan, genggaman tangan, atau "
                      "sekadar duduk berdekatan dengan pasangan. Kedekatan fisik ini terasa seperti "
                      "penegasan nyata bahwa hubungan kalian baik-baik saja, bahkan lebih dari kata-"
                      "kata sekalipun. Kalau pasanganmu tidak terlalu terbiasa dengan kontak fisik, "
                      "kamu bisa salah menyimpulkan bahwa hubungan sedang renggang, padahal itu "
                      "cuma perbedaan cara mengekspresikan kedekatan. Penting untuk selalu "
                      "memastikan bahwa kebutuhanmu ini disampaikan dan diterima dengan nyaman oleh "
                      "pasangan, bukan dipaksakan. *PR: obrolkan dengan pasangan soal jenis "
                      "sentuhan yang membuat kalian berdua sama-sama nyaman, supaya kedekatan fisik "
                      "terasa alami untuk kalian berdua.*",
            "keuangan": "Kamu cenderung menghargai pengalaman yang melibatkan kebersamaan fisik, "
                        "seperti liburan bersama, pijat, atau aktivitas yang membuat kamu dan orang "
                        "terdekat bisa berada dekat satu sama lain, dan kamu rela mengeluarkan "
                        "biaya untuk pengalaman semacam itu. Kamu juga cukup memperhatikan "
                        "kenyamanan fisik dalam pengeluaranmu sehari-hari, seperti memilih tempat "
                        "yang nyaman untuk ditinggali atau dikunjungi bersama. Sisi yang perlu "
                        "dijaga, kamu bisa kurang mempertimbangkan efisiensi biaya karena lebih "
                        "fokus pada kenyamanan dan kedekatan yang dirasakan. *PR: bandingkan dulu "
                        "beberapa pilihan sebelum memutuskan pengeluaran untuk kenyamanan, supaya "
                        "tetap sesuai dengan anggaran yang kamu punya.*",
            "kesehatan": "Secara emosional, kamu butuh kontak fisik yang wajar untuk merasa "
                         "tenang dan terhubung, dan ketiadaan sentuhan dalam waktu lama bisa "
                         "membuatmu merasa sepi meski secara emosional kamu baik-baik saja. Kamu "
                         "juga cenderung lebih cepat pulih dari stres lewat aktivitas yang "
                         "melibatkan gerak fisik atau kedekatan dengan orang lain, seperti olahraga "
                         "bersama atau sekadar dipeluk saat sedang lelah. Penting untuk tetap "
                         "menjaga sumber ketenangan lain di luar sentuhan, supaya kestabilan "
                         "emosimu tidak sepenuhnya bergantung pada kehadiran orang lain secara "
                         "fisik. *PR: cari juga cara menenangkan diri sendiri tanpa sentuhan orang "
                         "lain, seperti olahraga ringan atau teknik pernapasan, untuk saat kamu "
                         "sedang sendirian.*",
        },
    },
}
