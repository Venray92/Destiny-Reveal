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

REVISI (27 Sep 2026): tiap entri ditambahin key "domains" (karir, asmara,
keuangan, kesehatan) — Fase A dari fitur tiering Versi Pendek/Panjang, lihat
views/revealpage.py (_domain_unlocked_for, DOMAIN_ORDER dkk) dan
views/loadingpage.py (_final_dialog). SENGAJA baru Zodiak yang diisi dulu
sebagai bukti alur (mekanisme lock/unlock + expander), 4 sistem lain
(Shio/Weton/Numerologi/Matrix Destiny) belum punya "domains" sama sekali
-- ini Fase B yang masih pending, BUKAN bug/kelupaan.
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
        "domains": {
            "karir": "Kamu bersinar di proyek rintisan atau posisi yang butuh orang berani ambil "
                     "langkah pertama, misalnya buka lini bisnis baru, jadi orang pertama yang "
                     "menawarkan ide di rapat, atau memimpin tim yang baru dibentuk dari nol. Tapi "
                     "begitu proyeknya masuk fase rutin dan repetitif, semangatmu gampang kendur, dan "
                     "kamu bisa kehilangan minat tepat di fase yang justru paling menentukan hasil "
                     "akhirnya. Rekan kerja kadang was-was menyerahkan tugas jangka panjang kepadamu "
                     "karena sudah melihat pola ini berulang kali, meski mereka tahu betul kamu adalah "
                     "orang paling tepat untuk memulai sesuatu dari nol. *PR: minta satu rekan pegang "
                     "bagian follow-up/detail administratif dari proyekmu, biar energimu tetap "
                     "tersalur ke bagian yang benar-benar kamu kuasai.*",
            "asmara": "Kamu jujur dan langsung soal perasaan, bikin pasangan tahu persis posisinya "
                      "tanpa perlu menebak-nebak, dan itu jadi kekuatan besar buat hubungan yang jujur. "
                      "Tapi kesabaranmu diuji kalau hubungan terasa monoton, kamu butuh hal baru "
                      "supaya percikan itu tetap ada, dan kalau tidak ada, kamu bisa jadi gelisah atau "
                      "mulai mencari-cari kesalahan kecil dalam hubungan yang sebenarnya baik-baik "
                      "saja. Pasanganmu mungkin merasa harus terus menciptakan kejutan supaya kamu "
                      "tetap tertarik, padahal hubungan yang matang juga butuh momen-momen tenang. "
                      "*PR: sebelum menganggap hubungan membosankan, coba dulu ajak pasangan bikin "
                      "\"hal baru\" bareng, bukan langsung mundur atau mencari yang lain.*",
            "keuangan": "Kamu gampang tergoda beli sesuatu yang baru dan menarik perhatian saat itu "
                        "juga, tanpa banyak mikir jangka panjang, karena dorongan untuk segera "
                        "memiliki sesuatu yang kamu inginkan terasa begitu kuat. Ini bikin belanja "
                        "impulsif jadi kebiasaan yang sering bikin kaget pas cek saldo di akhir bulan, "
                        "apalagi kalau kamu sedang dalam mood yang sedang tinggi dan merasa layak "
                        "\"reward diri sendiri\". Kamu juga cenderung tidak sabar menunggu diskon "
                        "atau promo, lebih memilih beli sekarang meski harganya belum tentu paling "
                        "murah. *PR: kasih jeda 24 jam sebelum beli barang di atas nominal tertentu, "
                        "supaya dorongan awal itu sempat mereda dulu.*",
            "kesehatan": "Energimu besar dan butuh disalurkan lewat gerak fisik yang intens, kalau "
                         "nggak malah jadi gelisah, susah diam, atau gampang emosi tanpa sebab yang "
                         "jelas. Risikonya, kamu sering terburu-buru tanpa pemanasan cukup saat "
                         "olahraga atau aktivitas fisik lainnya, jadi rawan cedera otot atau sendi, "
                         "terutama di bagian kepala dan wajah yang jadi titik lemah khas Aries. Kamu "
                         "juga tipe yang memaksakan diri tetap aktif meski tubuh sudah memberi sinyal "
                         "lelah, karena tidak suka merasa \"kalah\" oleh keterbatasan fisik sendiri. "
                         "*PR: biasakan pemanasan 5 menit sebelum olahraga, sekecil apa pun rasanya "
                         "buang-buang waktu.*",
        },
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
        "domains": {
            "karir": "Kamu unggul di posisi yang butuh konsistensi dan hasil tahan lama, bukan proyek "
                     "yang berubah arah tiap minggu, dan atasan biasanya menaruh kepercayaan besar "
                     "padamu untuk hal-hal yang butuh ketekunan bertahun-tahun. Sisi kerasnya, kamu "
                     "bisa lambat beradaptasi kalau perusahaan tiba-tiba ganti sistem kerja atau arah "
                     "bisnis, dan perubahan mendadak itu bisa terasa seperti ancaman, bukan sekadar "
                     "penyesuaian biasa. Kamu juga cenderung menunda mengajukan diri untuk peran baru "
                     "yang sebenarnya kamu sanggup, karena lebih nyaman di posisi yang sudah kamu "
                     "kuasai. *PR: coba anggap perubahan sebagai versi baru dari stabilitas, bukan "
                     "ancaman terhadapnya.*",
            "asmara": "Kesetiaanmu jarang goyah begitu berkomitmen, dan pasanganmu merasa aman "
                      "karenanya, karena kamu bukan tipe yang gampang tergoda pindah hati begitu "
                      "keadaan sedikit sulit. Tapi kamu bisa terlalu lama bertahan di hubungan yang "
                      "sebenarnya sudah tidak sehat, cuma karena benci perubahan dan merasa lebih "
                      "aman dengan yang sudah dikenal, meski itu berarti mengorbankan kebahagiaanmu "
                      "sendiri. Kamu juga bisa keras kepala soal cara menunjukkan cinta, padahal "
                      "pasangan mungkin butuh bentuk perhatian yang sedikit berbeda dari biasanya. "
                      "*PR: sesekali tanya diri sendiri, ini bertahan karena cinta atau karena takut "
                      "berubah?*",
            "keuangan": "Kamu cukup baik menabung, tapi juga suka memanjakan diri dengan hal-hal yang "
                        "terasa nyaman, makanan enak, barang berkualitas, pengalaman menyenangkan, "
                        "karena bagimu kenyamanan fisik adalah investasi yang sama pentingnya dengan "
                        "uang di rekening. Kalau tidak dijaga, pengeluaran \"kenyamanan\" ini bisa "
                        "menggerus tabungan pelan-pelan tanpa kamu sadari, karena masing-masing "
                        "pembelian terasa kecil dan wajar. Kamu juga cenderung enggan menjual atau "
                        "melepas aset lama meski sudah tidak terlalu berguna, karena merasa sayang "
                        "atau terikat secara emosional. *PR: catat khusus pos \"kenyamanan diri\" tiap "
                        "bulan biar kelihatan totalnya.*",
            "kesehatan": "Kamu suka menikmati makanan enak dan gaya hidup santai, yang enak tapi bisa "
                         "berujung kurang gerak kalau dibiarkan terus, apalagi kalau rutinitas "
                         "harianmu memang tidak banyak menuntut aktivitas fisik. Area leher dan "
                         "tenggorokan cenderung jadi titik lemahmu, dan kamu mungkin baru sadar ada "
                         "yang salah setelah masalahnya cukup mengganggu, karena kamu jarang proaktif "
                         "memeriksakan diri selagi masih merasa baik-baik saja. *PR: pasang jadwal "
                         "jalan kaki/olahraga ringan rutin, bukan cuma pas mood.*",
        },
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
        "domains": {
            "karir": "Kamu jago di peran yang butuh komunikasi lintas tim atau menangani banyak hal "
                     "sekaligus, dan atasan biasanya senang punya kamu di tim karena selalu bisa "
                     "diandalkan menjembatani informasi antar divisi. Tapi bisa keteteran "
                     "menyelesaikan satu proyek besar sampai tuntas karena gampang tergoda tugas baru "
                     "yang lebih menarik, dan kamu bisa punya banyak pekerjaan setengah jalan di saat "
                     "yang sama. Rekan kerja mungkin melihatmu sebagai sosok multitasking, tapi juga "
                     "sedikit ragu soal seberapa dalam kamu benar-benar menguasai satu bidang tertentu. "
                     "*PR: sebelum terima tanggung jawab baru, selesaikan dulu satu yang sedang jalan "
                     "sampai kelar.*",
            "asmara": "Kamu butuh obrolan yang hidup dan bervariasi supaya hubungan terasa segar, dan "
                      "gampang bosan kalau komunikasi jadi datar atau itu-itu saja setiap harinya. "
                      "Risikonya, kamu bisa terlihat kurang serius di mata pasangan yang butuh "
                      "kepastian, karena kamu sering mengalihkan topik berat dengan candaan atau "
                      "obrolan ringan. Pasangan mungkin merasa sulit benar-benar tahu isi hatimu, "
                      "karena kamu lebih nyaman berbicara tentang ide dibanding perasaan yang lebih "
                      "dalam. *PR: sesekali dengarkan cerita pasangan sampai habis tanpa buru-buru "
                      "ganti topik.*",
            "keuangan": "Kamu suka coba banyak hal baru, hobi, gadget, langganan aplikasi, yang kalau "
                        "dikumpulkan ternyata menggerus budget cukup banyak, apalagi kalau separuhnya "
                        "cuma dipakai sebentar lalu ditinggal begitu minatmu beralih ke hal lain. Kamu "
                        "juga jarang benar-benar mengecek total pengeluaran kecil-kecil ini secara "
                        "keseluruhan, karena masing-masing terasa remeh saat dibeli satu per satu. "
                        "*PR: review langganan/hobi yang jarang dipakai tiap 3 bulan, hentikan yang "
                        "sudah tidak relevan.*",
            "kesehatan": "Pikiranmu jarang berhenti bergerak dari satu topik ke topik lain, yang bagus "
                         "buat kreativitas tapi melelahkan buat sistem sarafmu kalau terus-menerus "
                         "tanpa jeda. Kamu juga cenderung susah tidur nyenyak karena kepala masih "
                         "sibuk memikirkan banyak hal saat seharusnya sudah waktunya istirahat. *PR: "
                         "sisihkan 10 menit tiap malam buat journaling atau duduk diam tanpa gadget, "
                         "biar pikiran benar-benar istirahat.*",
        },
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
        "domains": {
            "karir": "Kamu unggul di peran yang butuh empati, memperhatikan kesejahteraan tim, "
                     "menjaga suasana kerja tetap hangat, dan rekan-rekan biasanya merasa nyaman "
                     "bercerita masalah pribadi maupun pekerjaan denganmu. Risikonya, kritik terhadap "
                     "pekerjaanmu bisa terasa seperti serangan pribadi, dan kamu bisa terbawa perasaan "
                     "berhari-hari hanya karena satu masukan kecil dari atasan. Kamu juga cenderung "
                     "menyimpan kekecewaan soal keputusan kerja yang menurutmu tidak adil, meski tidak "
                     "selalu menunjukkannya secara terbuka. *PR: latih diri memisahkan \"kerjaanku "
                     "dikritik\" dari \"aku sebagai orang dikritik\".*",
            "asmara": "Kamu pasangan yang penuh perhatian dan protektif, selalu memastikan orang yang "
                      "kamu sayangi merasa aman dan diperhatikan dalam segala hal. Tapi kadang sikap "
                      "protektifmu berubah jadi posesif tanpa disadari, atau kamu diam-diam ngambek "
                      "tanpa bilang apa masalahnya, berharap pasangan bisa menebak sendiri apa yang "
                      "salah. Pola ini bisa membuat pasangan merasa bingung dan sering salah "
                      "menafsirkan suasana hatimu yang naik turun. *PR: kalau ada yang mengganjal, "
                      "bilang langsung, jangan biarkan pasangan menebak-nebak lewat sikap dingin.*",
            "keuangan": "Kamu rajin menabung untuk keluarga atau rumah, dan biasanya punya rencana "
                        "yang cukup matang soal masa depan finansial orang-orang yang kamu sayangi. "
                        "Tapi gampang belanja impulsif saat mood sedang turun sebagai bentuk menghibur "
                        "diri sendiri, entah lewat makanan, barang kesukaan, atau hal-hal kecil yang "
                        "memberi rasa nyaman sesaat. Kebiasaan ini kalau tidak disadari bisa "
                        "menumpuk jadi pengeluaran yang cukup besar dalam sebulan. *PR: kalau lagi "
                        "sedih dan pengen belanja, tunda dulu satu hari, cek lagi apa benar butuh.*",
            "kesehatan": "Perasaanmu yang naik-turun sering berdampak ke perutmu, gampang mual atau "
                         "perih pas lagi stres atau cemas, karena secara fisik kamu memang cukup "
                         "sensitif terhadap tekanan emosional. Kamu juga cenderung memendam kekhawatiran "
                         "sampai berdampak ke pola tidur, sering terbangun malam hari karena pikiran "
                         "yang terus berputar soal orang-orang yang kamu khawatirkan. *PR: jaga jam "
                         "makan tetap teratur meski lagi banyak pikiran, jangan sampai telat atau lupa "
                         "makan sama sekali.*",
        },
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
        "domains": {
            "karir": "Panggung adalah tempatmu bersinar, presentasi di depan klien, memimpin proyek, "
                     "atau posisi yang hasil kerjanya langsung terlihat dan diakui banyak orang. Namun "
                     "kesabaranmu diuji saat harus menjalani proses yang lambat atau kerja di balik "
                     "layar tanpa apresiasi langsung, dan kamu bisa kehilangan motivasi kalau merasa "
                     "usahamu tidak diperhatikan. Kamu juga cenderung ingin selalu jadi yang paling "
                     "menonjol dalam tim, sampai kadang lupa memberi ruang bagi rekan lain untuk "
                     "bersinar juga. *PR: sekali sebulan, ambil satu tugas yang hasilnya baru "
                     "kelihatan lama, latih kesabaran menjalani prosesnya.*",
            "asmara": "Kamu mencintai dengan totalitas dan setia, tidak setengah-setengah kalau sudah "
                      "berkomitmen, dan pasanganmu tahu betul kamu akan memperjuangkan hubungan "
                      "dengan sepenuh hati. Tapi kamu juga butuh diakui secara terbuka, dan kalau "
                      "merasa itu tidak datang, kamu bisa jadi posesif atau menuntut lebih dari "
                      "kapasitas pasangan untuk terus-menerus memujimu. Kebutuhan akan pengakuan ini "
                      "bisa membuat hubungan terasa berat sebelah, seolah semuanya harus berpusat "
                      "padamu. *PR: sebelum menuntut perhatian, tanya dulu apa yang sedang dia butuhkan "
                      "saat itu.*",
            "keuangan": "Kamu cenderung royal, terutama untuk hal yang menunjang citra diri, "
                        "penampilan, pengalaman, hadiah untuk orang tersayang, karena bagimu tampil "
                        "maksimal itu penting. Bisa jadi jebakan kalau tidak diimbangi kebiasaan "
                        "menabung, terutama kalau kamu sering membeli sesuatu demi menjaga gengsi di "
                        "depan orang lain, bukan karena benar-benar butuh. *PR: sisihkan minimal 10% "
                        "penghasilan otomatis sebelum uang itu sempat kamu pegang.*",
            "kesehatan": "Energimu besar tapi gampang habis kalau terus dipaksa tanpa jeda, kamu tipe "
                         "yang baru berhenti setelah benar-benar kehabisan tenaga, karena tidak suka "
                         "merasa \"kalah\" oleh rasa lelah. Bagian jantung dan punggung cenderung jadi "
                         "titik lemahmu kalau kamu terus memaksakan diri tampil prima tanpa istirahat "
                         "yang cukup. *PR: jadwalkan satu hari penuh tanpa agenda setiap minggu, dan "
                         "benar-benar patuhi jadwal itu.*",
        },
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
        "domains": {
            "karir": "Ketelitianmu jadi aset besar di pekerjaan yang butuh akurasi tinggi, QA, "
                     "analisis data, penyusunan rencana rinci, dan atasan biasanya menaruh "
                     "kepercayaan besar padamu untuk hal-hal yang tidak boleh salah sedikit pun. Tapi "
                     "standar tinggi ke diri sendiri bisa berujung burnout kalau tidak direm, karena "
                     "kamu jarang merasa hasil kerjamu sudah cukup baik meski orang lain sudah "
                     "memujinya. Kamu juga bisa terlalu lama memeriksa ulang sesuatu yang sebenarnya "
                     "sudah selesai, sampai kehilangan waktu untuk mengerjakan hal lain yang sama "
                     "pentingnya. *PR: tetapkan batas \"cukup baik\" untuk tugas kecil, simpan energi "
                     "maksimal buat yang benar-benar penting.*",
            "asmara": "Kamu menunjukkan cinta lewat tindakan praktis, bantuin beresin masalah, "
                      "memperhatikan detail kebutuhan pasangan yang bahkan mereka sendiri belum "
                      "sadari. Sayangnya ini kadang ditangkap sebagai \"banyak protes\" atau terlalu "
                      "mengoreksi, karena caramu peduli sering dibungkus dalam bentuk kritik atau "
                      "saran perbaikan. Pasangan mungkin merasa tidak pernah cukup baik di matamu, "
                      "padahal maksudmu sebenarnya ingin membantu supaya semuanya berjalan lebih baik. "
                      "*PR: sesekali puji dulu sebelum kasih masukan perbaikan.*",
            "keuangan": "Kamu rapi mencatat pengeluaran dan cenderung hemat, tahu persis ke mana "
                        "uangmu pergi setiap bulan, dan jarang terkejut dengan tagihan yang tidak "
                        "terduga. Tapi bisa terlalu pelit ke diri sendiri sampai jarang menikmati "
                        "hasil kerja keras, merasa bersalah setiap kali mengeluarkan uang untuk "
                        "sesuatu yang sifatnya murni kesenangan. *PR: alokasikan budget kecil khusus "
                        "\"untuk senang-senang\" tiap bulan, tanpa rasa bersalah.*",
            "kesehatan": "Kecenderungan overthinking dan mengkritik diri sendiri sering muncul sebagai "
                         "gejala fisik, sakit kepala, perut tegang, susah rileks, karena pikiranmu "
                         "jarang benar-benar berhenti mengevaluasi. Sistem pencernaanmu cenderung jadi "
                         "titik lemah kalau kamu terus-menerus menyimpan kecemasan soal kesempurnaan. "
                         "*PR: latih self-compassion sederhana, bicara ke diri sendiri seperti kamu "
                         "bicara ke sahabat yang sedang berjuang.*",
        },
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
        "domains": {
            "karir": "Kamu unggul di peran diplomasi dan menjaga hubungan antar pihak, negosiasi, "
                     "kerja sama lintas tim, klien, karena kamu jago melihat kepentingan semua sisi "
                     "sekaligus. Tapi kamu bisa lambat ambil keputusan sendiri, sering menunggu "
                     "persetujuan orang lain dulu sebelum benar-benar yakin melangkah, sampai "
                     "kesempatan yang seharusnya bisa kamu ambil justru diambil orang lain lebih dulu. "
                     "*PR: sekali dalam seminggu, ambil satu keputusan kerja sendiri tanpa polling "
                     "pendapat tim dulu.*",
            "asmara": "Kamu romantis dan mencari hubungan yang seimbang, selalu berusaha memastikan "
                      "kedua belah pihak merasa adil diperlakukan. Tapi takut konflik bikin kamu "
                      "menunda ngomongin masalah yang sebenarnya sudah lama mengganjal, sampai "
                      "akhirnya menumpuk jadi kekecewaan yang lebih besar dari yang seharusnya. "
                      "Pasangan mungkin tidak pernah tahu ada yang salah sampai kamu benar-benar "
                      "meledak. *PR: coba sampaikan satu ketidaknyamanan kecil langsung saat itu "
                      "terjadi, jangan ditimbun.*",
            "keuangan": "Kamu suka barang dan pengalaman yang estetik, yang kalau tidak dikontrol bisa "
                        "menggerus budget demi tampilan atau suasana yang indah, karena bagimu "
                        "keindahan visual punya nilai tersendiri yang sulit diabaikan. *PR: sebelum "
                        "beli barang dekoratif, tanya apakah ini kebutuhan atau cuma pengen terlihat "
                        "bagus.*",
            "kesehatan": "Kebiasaan menimbang-nimbang terlalu lama dan memendam konflik bisa memicu "
                         "stres kronis tanpa kamu sadari sumbernya, karena kamu terus memikirkan "
                         "berbagai kemungkinan tanpa pernah benar-benar melepaskannya. Area ginjal "
                         "dan punggung bawah cenderung jadi titik lemah kalau ketegangan ini "
                         "dibiarkan menumpuk lama. *PR: coba olahraga yang menstabilkan seperti yoga "
                         "atau jalan santai rutin, bukan cuma pas capek pikiran.*",
        },
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
        "domains": {
            "karir": "Fokus dan daya tahanmu bikin kamu unggul di proyek rumit yang butuh riset "
                     "mendalam atau kerja krisis, jenis pekerjaan yang membuat banyak orang lain "
                     "menyerah sebelum benar-benar memahami masalahnya. Tapi kamu susah delegasi atau "
                     "percaya rekan kerja pegang bagian penting, karena merasa hanya kamu yang benar-"
                     "benar bisa mengerjakannya dengan standar yang kamu inginkan. Ini bisa membuatmu "
                     "kelebihan beban kerja tanpa disadari orang lain di sekitarmu. *PR: coba "
                     "delegasikan satu tugas kecil ke rekan kerja, biar terbiasa melepas kontrol "
                     "sedikit demi sedikit.*",
            "asmara": "Kesetiaanmu kuat begitu percaya pada seseorang, dan kamu akan memperjuangkan "
                      "hubungan itu dengan intensitas yang jarang dimiliki orang lain. Tapi kecemburuan "
                      "dan kebutuhan mengontrol informasi soal dirimu bisa bikin pasangan merasa "
                      "hubungan berat sebelah, karena kamu tahu banyak tentang mereka tapi jarang "
                      "membuka diri secara setara. *PR: coba ceritakan satu hal personal yang biasa "
                      "kamu tutup rapat, ke pasangan yang sudah lama kamu percaya.*",
            "keuangan": "Kamu diam-diam sangat perhitungan dan strategis soal uang, punya rencana "
                        "jangka panjang yang jarang kamu bagikan ke orang lain. Tapi juga bisa ambil "
                        "risiko besar seperti investasi agresif tanpa cerita ke orang terdekat, "
                        "karena kamu lebih nyaman mengambil keputusan besar sendirian daripada "
                        "mendengar pendapat yang berbeda. *PR: sebelum ambil keputusan finansial "
                        "besar sendirian, diskusikan dulu dengan satu orang yang kamu percaya.*",
            "kesehatan": "Kamu cenderung memendam stres secara internal, yang lama-lama bisa "
                         "termanifestasi jadi ketegangan fisik atau gangguan tidur, karena kamu jarang "
                         "menunjukkan tanda-tanda sedang kewalahan ke orang lain. Area reproduksi dan "
                         "sistem eliminasi cenderung jadi titik lemah kalau emosi yang terpendam "
                         "dibiarkan menumpuk terlalu lama. *PR: cari satu outlet rutin buat melepas "
                         "emosi, olahraga intens, journaling, atau curhat ke orang terpercaya.*",
        },
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
        "domains": {
            "karir": "Kamu cocok kerja yang variatif atau melibatkan eksplorasi dan perjalanan, dan "
                     "cepat gerah di lingkungan kantor yang kaku dan monoton, merasa terkurung kalau "
                     "harus duduk di meja yang sama setiap hari mengerjakan hal yang itu-itu saja. "
                     "*PR: kalau terjebak rutinitas kaku, cari cara kecil menambah variasi ke tugas "
                     "sehari-hari, alih-alih langsung resign.*",
            "asmara": "Kamu butuh ruang bebas dalam hubungan dan takut merasa dikekang, yang kadang "
                      "bikin pasangan ragu seberapa jauh mereka bisa mengandalkanmu untuk komitmen "
                      "jangka panjang. Kejujuranmu yang blak-blakan soal kebutuhan ini sebenarnya "
                      "bagus, tapi kalau tidak diimbangi kepastian, pasangan bisa merasa hubungan "
                      "kalian tidak punya arah yang jelas. *PR: coba komit ke satu hal kecil dan "
                      "tepati konsisten, buktikan kebebasan tetap bisa jalan bareng tanggung jawab.*",
            "keuangan": "Kamu royal untuk pengalaman, traveling, hobi baru, hal-hal yang memperluas "
                        "pandangan, dibanding barang, karena bagimu pengalaman jauh lebih berharga "
                        "dari kepemilikan. Tapi kurang planning jangka panjang seperti dana darurat, "
                        "karena kamu lebih fokus pada kesempatan yang ada sekarang daripada "
                        "kemungkinan yang belum terjadi. *PR: sisihkan satu pos khusus dana darurat "
                        "sebelum uangnya \"terpakai\" buat pengalaman baru.*",
            "kesehatan": "Kamu aktif dan suka olahraga luar ruang, tubuhmu terasa paling hidup saat "
                         "sedang bergerak dan menjelajah. Tapi rasa percaya diri berlebih bisa bikin "
                         "kamu kurang hati-hati dan rawan cedera, atau malas checkup rutin karena "
                         "merasa selalu fit dan tidak butuh diperiksa. Area pinggul dan paha "
                         "cenderung jadi titik lemah kalau kamu terlalu memaksakan aktivitas fisik. "
                         "*PR: jadwalkan medical checkup rutin walau merasa baik-baik saja.*",
        },
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
        "domains": {
            "karir": "Kedisiplinanmu bikin kamu unggul di posisi kepemimpinan jangka panjang, dan "
                     "atasan mempercayaimu memegang tanggung jawab besar karena tahu kamu tidak akan "
                     "lari dari komitmen. Tapi kamu rawan burnout karena terus-menerus mengejar target "
                     "berikutnya tanpa jeda, merasa belum pantas istirahat sebelum semua target "
                     "tercapai. *PR: tetapkan satu hari kerja per minggu yang benar-benar batasi jam "
                     "lembur.*",
            "asmara": "Kamu serius dan bertanggung jawab dalam hubungan, jarang main-main soal "
                      "komitmen dan selalu memikirkan masa depan jangka panjang bersama pasangan. Tapi "
                      "fokus berlebih ke karir bisa bikin quality time sama pasangan jadi korban "
                      "pertama yang dikorbankan, sampai pasangan merasa selalu berada di urutan kedua "
                      "setelah pekerjaanmu. *PR: kunci satu jadwal tetap tiap minggu khusus buat "
                      "pasangan, jangan sampai digeser demi kerjaan.*",
            "keuangan": "Kamu disiplin menabung dan merencanakan jangka panjang, punya visi yang jelas "
                        "soal ke mana arah finansialmu dalam sepuluh atau dua puluh tahun ke depan. "
                        "Tapi kadang terlalu pelit menikmati hasil kerja kerasmu sendiri, terus "
                        "menunda kesenangan demi target yang lebih besar lagi. *PR: alokasikan dana "
                        "kecil khusus buat menikmati pencapaian begitu satu target besar tercapai.*",
            "kesehatan": "Tekanan yang terus-menerus kamu pikul rawan bermuara ke stres kronis atau "
                         "ketegangan di tulang dan sendi, terutama area lutut dan tulang yang jadi "
                         "titik lemah khas Capricorn kalau beban dipikul terlalu lama tanpa jeda. *PR: "
                         "jadikan istirahat sebagai jadwal wajib di kalender, bukan hal opsional yang "
                         "gampang dibatalkan.*",
        },
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
        "domains": {
            "karir": "Kamu unggul di pekerjaan yang butuh inovasi dan cara pandang baru, sering jadi "
                     "orang yang mengusulkan pendekatan berbeda saat orang lain masih terpaku pada "
                     "cara lama. Tapi kurang cocok di lingkungan yang sangat kaku aturan dan "
                     "hierarkis, karena kamu merasa terkekang harus mengikuti prosedur yang menurutmu "
                     "sudah tidak relevan lagi. *PR: kalau terjebak sistem kaku, cari satu celah kecil "
                     "buat menyalurkan ide inovatifmu tanpa melanggar aturan besar.*",
            "asmara": "Kamu butuh pasangan yang menghargai kebebasan berpikirmu dan tidak menuntutmu "
                      "jadi orang yang konvensional. Tapi kamu sendiri susah menunjukkan sisi "
                      "emosional atau vulnerable, bikin hubungan terasa kurang intim, karena kamu "
                      "lebih nyaman membicarakan ide dan konsep dibanding perasaan yang lebih dalam. "
                      "*PR: coba ungkapkan satu perasaan, bukan ide atau pendapat, ke pasangan secara "
                      "langsung.*",
            "keuangan": "Kamu cenderung belanja untuk gadget, hal-hal unik, atau donasi ke isu sosial "
                        "yang kamu pedulikan, karena bagimu mendukung sesuatu yang bermakna lebih "
                        "penting dari sekadar menabung. Tapi kurang perhatian ke tabungan konvensional, "
                        "sampai kondisi finansial jangka panjangmu jadi kurang terencana. *PR: buat 1 "
                        "rekening terpisah khusus tabungan yang tidak kamu sentuh sama sekali.*",
            "kesehatan": "Pikiranmu sering terlalu aktif menjelang tidur, banyak ide berputar yang "
                         "bikin susah benar-benar rileks, karena otakmu terus memproses konsep dan "
                         "kemungkinan baru bahkan saat tubuh sudah lelah. Sistem sirkulasi dan "
                         "pergelangan kaki cenderung jadi titik lemah kalau ketegangan mental ini "
                         "dibiarkan menumpuk. *PR: jadwalkan digital detox rutin sebelum tidur, "
                         "minimal 30 menit tanpa layar.*",
        },
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
        "domains": {
            "karir": "Kamu unggul di bidang kreatif atau pekerjaan yang butuh empati, konseling, seni, "
                     "layanan, karena kamu bisa memahami kebutuhan orang lain lebih dalam dari "
                     "sekadar apa yang mereka ucapkan. Tapi kurang cocok di lingkungan yang sangat "
                     "kompetitif dan keras, karena suasana yang penuh persaingan bisa membuatmu "
                     "kehilangan semangat atau merasa tidak nyaman berkepanjangan. *PR: kalau "
                     "lingkungan kerja terasa terlalu keras, cari komunitas kecil di dalamnya yang "
                     "suportif buat jadi tempat berlindung.*",
            "asmara": "Kamu pasangan yang romantis dan memberi tanpa pamrih, selalu berusaha "
                      "memenuhi kebutuhan pasangan bahkan sebelum diminta. Tapi ini juga bikin kamu "
                      "rawan dimanfaatkan karena susah bilang tidak, apalagi kalau pasangan tahu "
                      "betapa mudahnya kamu berkorban demi orang yang kamu sayangi. *PR: latih satu "
                      "kalimat penolakan sederhana yang bisa kamu pakai kapan saja tanpa rasa "
                      "bersalah berlebihan.*",
            "keuangan": "Kamu gampang lupa budget karena mengikuti suasana hati, dan rawan dipinjami "
                        "atau dimanfaatkan orang lain secara finansial karena susah menolak permintaan "
                        "tolong, bahkan dari orang yang sebenarnya kurang tulus. *PR: tetapkan batas "
                        "jelas berapa yang boleh dipinjamkan tanpa mengganggu kebutuhanmu sendiri.*",
            "kesehatan": "Kamu gampang menyerap energi atau emosi orang di sekitarmu sampai kelelahan "
                         "tanpa sadar sumbernya, dan cenderung lari ke dunia hiburan, tidur, nonton, "
                         "scroll medsos, buat kabur dari masalah yang terasa terlalu berat untuk "
                         "dihadapi langsung. Area kaki dan sistem imun cenderung jadi titik lemah "
                         "kalau kelelahan emosional ini dibiarkan menumpuk. *PR: sisihkan waktu "
                         "sendirian rutin buat \"recharge\", dan kenali kapan istirahat berubah jadi "
                         "menghindar.*",
        },
    },
}
