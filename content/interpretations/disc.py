"""
Konten DISC (4 dimensi: D, I, S, C).

Key dict ini HARUS sama persis dengan huruf hasil skoring DISC user
(huruf kapital tunggal: "D", "I", "S", "C").

D = Dominance, I = Influence, S = Steadiness, C = Compliance/Conscientiousness
(nama resmi ini dipakai sebagai referensi riset saja, bukan judul).

Struktur tiap entri sama persis dengan sistem lain (tagline, chip, title,
p1_label, p1, p2_label, p2, quote, p3_label, p3, domains: {karir, asmara,
keuangan, kesehatan}).
"""

DISC_CONTENT = {
    "D": {
        "tagline": "⚡ Gaya Dominan",
        "chip": "DISC",
        "title": "D — Sang Penggerak yang Tegas",
        "p1_label": "Siapa Kamu",
        "p1": "Kamu adalah tipe orang yang lebih suka bergerak dulu daripada menunggu arahan, karena "
              "bagi kamu hasil bicara lebih keras daripada rencana yang terlalu lama didiskusikan. Saat "
              "orang lain masih menimbang-nimbang, kamu biasanya sudah mengambil keputusan dan mulai "
              "jalan, karena diam di tempat terasa jauh lebih tidak nyaman ketimbang risiko salah "
              "langkah. Kamu suka tantangan besar, target yang jelas, dan lawan yang sepadan, sebab dari "
              "situ kamu merasa hidup benar-benar terpakai. Dalam kelompok, kamu sering jadi orang yang "
              "secara alami mengambil kendali, bukan karena haus kuasa, tapi karena kamu tidak tahan "
              "melihat sesuatu berjalan lambat atau tidak terarah. Kamu bicara singkat, padat, dan "
              "langsung ke inti masalah, dan berharap orang lain melakukan hal yang sama tanpa "
              "berputar-putar. Rasa percaya dirimu terlihat dari cara kamu menghadapi masalah besar "
              "seperti tantangan biasa yang tinggal dipecahkan satu per satu. Kamu tidak butuh banyak "
              "validasi dari luar untuk yakin bahwa arahmu benar, karena kamu lebih percaya pada hasil "
              "nyata daripada opini orang. Sejak kecil, mungkin kamu sudah terbiasa jadi yang paling "
              "dulu angkat tangan, paling dulu mencoba, atau paling dulu protes kalau ada yang dirasa "
              "tidak adil. Semua ini membuatmu terasa seperti mesin yang terus bergerak maju, jarang "
              "berhenti lama untuk sekadar merenung.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kekuatan terbesarmu ada di keberanian mengambil keputusan cepat dan kemampuan menembus "
              "kebuntuan yang bikin orang lain macet berlama-lama. Kamu bisa diandalkan justru di "
              "momen-momen genting, saat orang lain butuh sosok yang berani bilang \"lanjut\" atau "
              "\"stop\" tanpa ragu. Namun kecepatan dan ketegasan ini, kalau tidak dijaga, bisa terdengar "
              "seperti memaksakan kehendak, apalagi buat orang yang butuh waktu lebih lama untuk "
              "memproses sesuatu. Kamu juga cenderung fokus ke hasil akhir sampai kadang melewatkan "
              "perasaan orang-orang yang terlibat di prosesnya, padahal mereka bisa saja merasa "
              "terlindas tanpa sempat bersuara. Kesabaran adalah area yang paling perlu kamu jaga, "
              "karena dorongan untuk segera menyelesaikan sesuatu bisa membuatmu melewatkan detail "
              "penting atau masukan yang sebenarnya berharga. Belajar berhenti sejenak sebelum bereaksi "
              "akan membuat ketegasanmu terasa sebagai kekuatan, bukan tekanan.",
        "quote": "Kecepatan akan terasa jauh lebih berarti kalau disertai ruang bagi orang lain untuk mengejar.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba, di percakapan atau rapat berikutnya, tahan dulu keinginan untuk langsung menyimpulkan "
              "atau memutuskan sebelum semua orang selesai bicara. Beri jeda sekitar sepuluh detik "
              "setelah orang lain selesai berbicara sebelum kamu menanggapi, walau terasa lambat "
              "buatmu. Perhatikan apakah ada masukan yang sebenarnya berharga tapi hampir terlewat "
              "karena kamu sudah keburu bergerak ke keputusan berikutnya. Latihan kecil ini bukan buat "
              "membuatmu lebih lambat, tapi supaya ketegasanmu makin tajam karena dibangun dari "
              "informasi yang lebih lengkap.",
        "domains": {
            "karir": "Kamu bersinar di peran yang butuh keputusan cepat dan keberanian mengambil "
                     "tanggung jawab besar, seperti memimpin proyek, membuka lini bisnis baru, atau "
                     "jadi orang yang dipercaya menyelesaikan masalah mendesak. Atasan dan rekan kerja "
                     "sering mengandalkanmu justru di situasi krisis, karena kamu tidak panik dan "
                     "langsung bergerak mencari solusi. Tapi gaya komunikasimu yang to the point bisa "
                     "terdengar tajam buat rekan yang lebih sensitif, dan itu bisa membuat mereka segan "
                     "menyampaikan pendapat berbeda di depanmu. Kamu juga bisa terlihat kurang sabar "
                     "kalau harus menunggu proses birokrasi atau persetujuan berlapis yang menurutmu "
                     "membuang waktu. *PR: sebelum menyampaikan keputusan atau kritik ke rekan kerja, "
                     "coba tambahkan satu kalimat yang mengakui usaha mereka lebih dulu.*",
            "asmara": "Kamu tipe yang jujur dan langsung soal apa yang kamu mau dalam hubungan, sehingga "
                      "pasangan tidak perlu menebak-nebak posisinya di matamu. Kamu juga sosok yang "
                      "protektif dan bisa diandalkan saat pasangan menghadapi masalah, karena naluri "
                      "melindungimu cukup kuat. Namun ketegasanmu kadang membuat diskusi terasa seperti "
                      "negosiasi yang harus dimenangkan, padahal pasangan mungkin hanya ingin didengar, "
                      "bukan diberi solusi cepat. Kamu juga bisa terkesan mendominasi keputusan bersama "
                      "tanpa sadar, karena bagi kamu bergerak cepat terasa lebih efisien daripada "
                      "berdiskusi panjang. *PR: sekali dalam obrolan penting dengan pasangan, coba tanya "
                      "\"menurut kamu gimana?\" dan benar-benar tunggu jawabannya sebelum memberi pendapat.*",
            "keuangan": "Kamu berani mengambil keputusan finansial besar dan cepat melihat peluang, "
                        "misalnya berinvestasi atau memulai usaha baru, karena kamu tidak takut ambil "
                        "risiko yang diperhitungkan. Keberanian ini bisa membawa hasil besar, tapi juga "
                        "bisa membuatmu melompat ke keputusan tanpa cukup riset karena kamu tidak sabar "
                        "menunggu analisis yang lebih matang. Kamu juga cenderung ingin cepat balik "
                        "modal atau melihat hasil, sehingga bisa gelisah kalau suatu keputusan finansial "
                        "butuh waktu lama untuk berbuah. *PR: sebelum ambil keputusan finansial besar, "
                        "beri jeda minimal satu hari dan minta satu orang yang kamu percaya untuk "
                        "menantang rencanamu.*",
            "kesehatan": "Energimu besar dan kamu cenderung mendorong diri sendiri lebih keras dari "
                         "orang kebanyakan, baik dalam pekerjaan maupun olahraga, karena berhenti terasa "
                         "seperti kalah. Ini bagus untuk mencapai target, tapi juga membuatmu rawan "
                         "mengabaikan sinyal lelah dari tubuh sendiri sampai akhirnya benar-benar drop. "
                         "Kamu juga tipe yang tidak suka duduk diam terlalu lama, jadi stres yang "
                         "menumpuk sering tidak tersalurkan dengan cara yang sehat dan malah keluar "
                         "sebagai mudah tersulut emosi. *PR: jadwalkan satu hari istirahat penuh setiap "
                         "minggu di kalender, bukan cuma saat tubuh sudah memaksa berhenti.*",
        },
    },
    "I": {
        "tagline": "✨ Gaya Memengaruhi",
        "chip": "DISC",
        "title": "I — Sang Penyemangat yang Hangat",
        "p1_label": "Siapa Kamu",
        "p1": "Kamu adalah sosok yang membuat ruangan terasa lebih hidup begitu kamu masuk, karena "
              "energi dan antusiasmemu gampang menular ke orang-orang di sekitarmu. Kamu suka "
              "berinteraksi, bercerita, dan membangun koneksi baru, dan biasanya tidak butuh waktu lama "
              "untuk merasa akrab dengan orang yang baru dikenal. Optimismemu terasa tulus, bukan "
              "sekadar basa-basi, karena kamu memang melihat sisi baik dan kemungkinan positif lebih "
              "dulu sebelum memikirkan risikonya. Kamu jarang menyimpan pendapat sendirian, lebih suka "
              "membicarakannya dengan orang lain, dan dari situ ide-ide barumu sering lahir. Dalam "
              "kelompok, kamu punya kemampuan alami untuk mencairkan suasana dan membuat orang yang "
              "tadinya canggung jadi lebih nyaman berbicara. Kamu juga cenderung ekspresif, baik lewat "
              "kata-kata maupun bahasa tubuh, sehingga orang lain gampang membaca suasana hatimu. Bagi "
              "kamu, hidup terasa lebih berarti kalau dijalani bersama orang lain, bukan sendirian di "
              "balik meja. Kamu suka menjadi bagian dari sesuatu yang meriah, entah itu proyek "
              "kolaboratif, acara komunitas, atau sekadar kumpul santai dengan teman. Pujian dan "
              "pengakuan dari orang lain terasa seperti bahan bakar yang membuat semangatmu makin "
              "menyala.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kekuatan utamamu ada di kemampuan membangun hubungan dan menggerakkan semangat orang "
              "lain, sehingga kamu sering jadi perekat dalam tim atau komunitas manapun kamu berada. "
              "Kamu juga pandai mencairkan konflik lewat humor dan kehangatan, membuat suasana yang "
              "tadinya tegang jadi lebih ringan. Namun antusiasme yang besar ini kadang membuatmu "
              "kurang teliti pada detail atau lupa menepati janji kecil, karena perhatianmu gampang "
              "berpindah ke hal baru yang lebih menarik. Kamu juga bisa terlalu bergantung pada "
              "validasi dan tanggapan positif dari orang lain, sehingga kritik yang sebenarnya "
              "membangun bisa terasa jauh lebih menyakitkan dari yang seharusnya. Belajar menindaklanjuti "
              "apa yang sudah kamu mulai, bukan hanya menyalakannya, akan membuat orang-orang makin "
              "percaya pada kata-katamu.",
        "quote": "Kehangatan akan terasa jauh lebih berarti kalau diikuti dengan bukti bahwa kamu benar-benar menepati janjimu.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba pilih satu janji kecil yang pernah kamu ucapkan tapi belum sempat ditepati, lalu "
              "selesaikan itu lebih dulu sebelum membuat janji baru yang lain. Tuliskan janji-janji "
              "kecilmu di satu tempat yang selalu kamu lihat, supaya tidak hilang di tengah semua "
              "obrolan seru yang kamu jalani setiap hari. Rasakan bedanya ketika orang lain melihatmu "
              "sebagai orang yang seru sekaligus bisa dipegang kata-katanya, bukan cuma yang seru saja. "
              "Dengan begitu, energi hangatmu tetap terasa, tapi kepercayaan orang padamu juga makin "
              "kuat.",
        "domains": {
            "karir": "Kamu unggul di pekerjaan yang melibatkan banyak interaksi, seperti presentasi, "
                     "penjualan, hubungan klien, atau peran yang butuh orang membangun jaringan dengan "
                     "cepat. Rekan kerja senang berada satu tim denganmu karena kamu membawa suasana "
                     "yang menyenangkan dan bikin diskusi terasa lebih hidup. Tapi kamu bisa dianggap "
                     "kurang detail atau kurang disiplin pada tenggat waktu, terutama kalau pekerjaannya "
                     "repetitif dan minim interaksi dengan orang lain. Fokusmu juga gampang terpecah "
                     "kalau ada banyak proyek menarik yang jalan bersamaan. *PR: pakai satu checklist "
                     "sederhana untuk tugas dengan tenggat, dan cek ulang sebelum menganggap sesuatu "
                     "selesai.*",
            "asmara": "Kamu membawa kehangatan dan keceriaan ke dalam hubungan, membuat pasangan merasa "
                      "hidupnya lebih berwarna sejak ada kamu. Kamu ekspresif soal perasaan dan tidak "
                      "segan menunjukkan kasih sayang secara terbuka, yang membuat pasangan jarang "
                      "ragu soal posisinya di hatimu. Namun kamu bisa kurang sabar menghadapi momen "
                      "sepi atau konflik yang butuh percakapan serius dan mendalam, karena kamu lebih "
                      "nyaman menjaga suasana tetap ringan. Kadang kamu juga lebih fokus membuat "
                      "pasangan senang saat itu juga, sampai lupa membahas hal-hal jangka panjang yang "
                      "sebenarnya penting untuk hubungan. *PR: sisihkan waktu khusus sebulan sekali "
                      "untuk membahas hal-hal serius dengan pasangan, bukan cuma saat masalah sudah "
                      "muncul.*",
            "keuangan": "Kamu murah hati dan suka menikmati momen bersama orang lain, entah itu "
                        "traktir teman atau ikut acara seru yang mengeluarkan biaya lebih dari "
                        "rencana. Kebiasaan ini membuat pengeluaranmu gampang membengkak tanpa terasa, "
                        "karena kamu jarang mencatat detail ke mana saja uangmu pergi. Kamu juga "
                        "cenderung memutuskan pembelian berdasarkan suasana hati atau ajakan orang lain, "
                        "bukan perencanaan yang matang. *PR: coba catat semua pengeluaran selama satu "
                        "bulan penuh di satu aplikasi atau buku kecil, tanpa menghakimi diri sendiri, "
                        "cukup untuk melihat pola aslinya.*",
            "kesehatan": "Kamu paling semangat berolahraga atau menjaga pola hidup sehat kalau "
                         "dilakukan bareng teman, karena sisi sosial itu yang bikin kamu konsisten. "
                         "Sebaliknya, rutinitas sehat yang harus dijalani sendirian dan sepi biasanya "
                         "lebih cepat kamu tinggalkan di tengah jalan. Kamu juga cenderung mengabaikan "
                         "kelelahan demi tidak melewatkan acara sosial yang seru, sehingga jam istirahat "
                         "sering jadi korban. *PR: cari satu teman untuk jadi partner olahraga atau "
                         "partner cek kesehatan rutin, supaya konsistensimu terjaga lewat kebersamaan.*",
        },
    },
    "S": {
        "tagline": "🌿 Gaya Stabil",
        "chip": "DISC",
        "title": "S — Sang Penopang yang Setia",
        "p1_label": "Siapa Kamu",
        "p1": "Kamu adalah sosok yang membuat orang lain merasa aman dan tenang begitu berada di "
              "dekatmu, karena kamu jarang bereaksi berlebihan dan selalu berusaha menjaga suasana "
              "tetap kondusif. Kamu lebih suka bekerja dengan ritme yang stabil dan bisa diprediksi, "
              "dibanding perubahan mendadak yang membuat semua orang harus buru-buru menyesuaikan diri. "
              "Kesetiaanmu terhadap orang, tim, atau kebiasaan yang sudah terbukti baik membuatmu jadi "
              "sosok yang paling bisa diandalkan dalam jangka panjang, bukan cuma saat momen ramai saja. "
              "Kamu cenderung mendengarkan lebih banyak daripada bicara, dan ketika kamu akhirnya "
              "bicara, orang lain biasanya benar-benar memperhatikan karena tahu itu sudah dipikirkan "
              "matang-matang. Kamu tidak suka konflik terbuka, dan lebih memilih mencari jalan tengah "
              "yang membuat semua pihak tetap nyaman, meski itu berarti kamu harus mengalah lebih dulu. "
              "Sejak dulu, kamu mungkin dikenal sebagai teman yang paling sabar mendengarkan curhat, "
              "atau anggota tim yang paling konsisten menyelesaikan tugasnya tanpa banyak drama. Kamu "
              "juga sangat menghargai rasa aman, baik dalam hubungan maupun pekerjaan, dan butuh waktu "
              "untuk benar-benar percaya sebelum membuka diri sepenuhnya. Ketekunanmu dalam menjalani "
              "rutinitas sering diremehkan orang lain, padahal justru itu yang membuat banyak hal di "
              "sekitarmu tetap berjalan lancar tanpa gejolak.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kekuatan terbesarmu ada di konsistensi dan kesabaran, kamu bisa diandalkan untuk "
              "menyelesaikan sesuatu sampai tuntas tanpa perlu diawasi terus-menerus. Orang-orang "
              "merasa nyaman berbagi masalah denganmu karena kamu mendengarkan tanpa buru-buru "
              "menghakimi atau memotong pembicaraan. Namun sisi yang perlu dijaga adalah kecenderunganmu "
              "menahan pendapat atau ketidaknyamanan sendiri demi menjaga suasana tetap damai, sampai "
              "akhirnya perasaan itu menumpuk tanpa tersalurkan. Kamu juga bisa kesulitan beradaptasi "
              "cepat kalau ada perubahan mendadak, dan butuh waktu lebih untuk menyesuaikan diri "
              "dibanding orang lain. Kebiasaan mendahulukan kenyamanan orang lain kadang membuatmu "
              "lupa menyuarakan kebutuhanmu sendiri, sampai orang di sekitarmu tidak sadar kamu juga "
              "sedang kesulitan.",
        "quote": "Ketenangan akan terasa jauh lebih berarti kalau kamu juga memberi ruang untuk suaramu sendiri didengar.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba, di percakapan berikutnya yang membuatmu tidak nyaman, sampaikan satu kalimat "
              "jujur soal apa yang kamu rasakan, walau terasa canggung di awal. Tidak perlu langsung "
              "berkonfrontasi besar, cukup mulai dari kalimat sederhana seperti \"sebenarnya aku kurang "
              "nyaman dengan ini\". Latih dirimu untuk melihat bahwa menyuarakan pendapat bukan berarti "
              "merusak keharmonisan, justru bisa memperkuatnya kalau disampaikan dengan cara yang "
              "tenang. Semakin sering kamu latih ini di hal kecil, semakin ringan rasanya saat harus "
              "melakukannya di hal yang lebih besar.",
        "domains": {
            "karir": "Kamu jadi andalan tim di peran yang butuh konsistensi dan ketelitian jangka "
                     "panjang, seperti operasional, dukungan pelanggan, atau posisi yang menjaga "
                     "kelangsungan proses sehari-hari. Atasan mempercayakan tugas-tugas penting "
                     "kepadamu karena tahu kamu tidak akan menghilang di tengah jalan atau meninggalkan "
                     "pekerjaan setengah selesai. Namun kamu bisa kesulitan menyuarakan idemu di rapat "
                     "besar, terutama kalau suasananya ramai dan penuh orang yang lebih vokal. Kamu "
                     "juga cenderung menghindari perubahan besar dalam karir walau sebenarnya sudah "
                     "waktunya untuk naik level atau pindah peran. *PR: siapkan satu poin pendapat "
                     "sebelum rapat dimulai, dan paksa diri menyampaikannya walau hanya satu kalimat.*",
            "asmara": "Kamu adalah pasangan yang setia dan bisa diandalkan, jarang membuat drama dan "
                      "selalu berusaha hadir saat pasangan membutuhkan. Kamu memberi rasa aman lewat "
                      "konsistensi, bukan lewat kejutan besar, dan itu sangat berharga bagi pasangan "
                      "yang mencari hubungan jangka panjang. Namun kamu sering memendam kekecewaan demi "
                      "menghindari konflik, sampai akhirnya perasaan itu meledak di saat yang tidak "
                      "terduga karena sudah menumpuk terlalu lama. Kamu juga bisa terlalu lama bertahan "
                      "di hubungan yang sebenarnya sudah tidak sehat, karena tidak tega mengecewakan "
                      "pasangan dengan mengakhirinya. *PR: kalau ada sesuatu yang mengganggu perasaanmu "
                      "dalam hubungan, sampaikan dalam 48 jam, jangan ditahan sampai berminggu-minggu.*",
            "keuangan": "Kamu cenderung hati-hati dan konsisten dalam mengelola uang, lebih suka "
                        "menabung pelan-pelan daripada mengambil risiko besar yang belum jelas "
                        "hasilnya. Kebiasaan ini membuatmu jarang terjebak masalah finansial mendadak, "
                        "karena kamu memang tidak suka gegabah soal uang. Namun sisi kehati-hatian ini "
                        "kadang membuatmu melewatkan peluang investasi yang sebenarnya bagus, karena "
                        "kamu butuh waktu lama untuk merasa cukup yakin. Kamu juga bisa terlalu "
                        "mengikuti kebiasaan lama walau kondisi keuanganmu sebenarnya sudah berubah. "
                        "*PR: sisihkan sedikit dana untuk dipelajari cara investasi yang lebih rendah "
                        "risiko, sebagai langkah kecil keluar dari zona amanmu.*",
            "kesehatan": "Kamu cenderung menjaga rutinitas sehat dengan disiplin begitu kebiasaan itu "
                         "sudah terbentuk, dan jarang tergoda melompat ke tren baru yang belum "
                         "terbukti. Ini membuat pola hidupmu relatif stabil dibanding kebanyakan orang. "
                         "Namun kamu cenderung memendam stres alih-alih membicarakannya, sehingga "
                         "tekanan batin bisa muncul lewat gejala fisik seperti gampang lelah atau sakit "
                         "kepala tanpa sebab yang jelas. Kamu juga kurang suka mencoba aktivitas fisik "
                         "baru karena merasa lebih nyaman dengan rutinitas yang sudah biasa dijalani. "
                         "*PR: cari satu orang yang bisa kamu ajak cerita rutin soal apa yang sedang "
                         "kamu rasakan, bukan cuma dipendam sendiri.*",
        },
    },
    "C": {
        "tagline": "📐 Gaya Teliti",
        "chip": "DISC",
        "title": "C — Sang Perancang yang Teliti",
        "p1_label": "Siapa Kamu",
        "p1": "Kamu adalah tipe orang yang selalu ingin memahami sesuatu secara mendalam sebelum "
              "mengambil keputusan, karena bagi kamu asal-asalan sama saja dengan mempertaruhkan hasil "
              "yang seharusnya bisa dijaga kualitasnya. Kamu suka data, fakta, dan proses yang jelas, "
              "dan biasanya merasa tidak nyaman kalau harus bergerak tanpa cukup informasi. Standar yang "
              "kamu terapkan ke diri sendiri sering lebih tinggi dari yang diminta orang lain, karena "
              "kamu memang ingin hasil kerjamu benar-benar bisa dipertanggungjawabkan. Kamu jarang "
              "bicara sembarangan, lebih suka memikirkan dulu sebelum menyampaikan pendapat, sehingga "
              "kata-katamu biasanya sudah dipertimbangkan matang-matang. Dalam kelompok, kamu sering "
              "jadi orang yang menemukan detail kecil yang terlewat orang lain, dan itu yang membuat "
              "hasil akhir jadi lebih rapi dan minim kesalahan. Kamu juga cenderung menyukai struktur "
              "dan aturan yang jelas, karena itu memberi rasa aman bahwa segala sesuatu berjalan sesuai "
              "rencana. Sejak dulu, mungkin kamu dikenal sebagai orang yang paling teliti mengecek "
              "ulang sebelum menyerahkan hasil kerja, atau yang paling banyak bertanya sebelum setuju "
              "melakukan sesuatu. Kamu tidak suka dikejar-kejar tanpa alasan jelas, dan lebih memilih "
              "bekerja dengan tenang di ruang yang memberimu waktu cukup untuk berpikir.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kekuatan utamamu ada di ketelitian dan kemampuan analisis yang membuat hasil kerjamu "
              "jarang meleset dari standar tinggi yang kamu tetapkan sendiri. Orang-orang mempercayakan "
              "hal-hal penting kepadamu karena tahu kamu akan memeriksa setiap detail sebelum "
              "menyerahkannya. Namun sisi yang perlu dijaga adalah kecenderunganmu terlalu lama "
              "menganalisis sebelum bertindak, sampai kadang kehilangan momentum karena terlalu takut "
              "membuat kesalahan kecil. Kamu juga bisa terkesan menjaga jarak atau kaku bagi orang yang "
              "belum mengenalmu, padahal itu sebenarnya caramu melindungi diri dari situasi yang belum "
              "kamu pahami sepenuhnya. Standar tinggi yang kamu terapkan ke diri sendiri kadang membuat "
              "kamu terlalu kritis, baik pada hasil kerja sendiri maupun orang lain, sampai lupa "
              "mengapresiasi progres kecil yang sebenarnya sudah baik.",
        "quote": "Ketelitian akan terasa jauh lebih berarti kalau kamu juga memberi ruang bagi diri sendiri untuk belum sempurna.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba pilih satu keputusan kecil yang selama ini kamu tunda karena masih merasa belum "
              "cukup data, lalu beri diri sendiri batas waktu jelas untuk memutuskan meski informasinya "
              "belum seratus persen lengkap. Perhatikan bagaimana rasanya bergerak dengan sedikit "
              "ketidakpastian, dan catat apakah hasilnya benar-benar seburuk yang kamu bayangkan. "
              "Latihan kecil ini bukan untuk membuatmu ceroboh, tapi supaya kamu punya bukti nyata "
              "bahwa tidak semua keputusan butuh analisis sepanjang yang biasa kamu lakukan.",
        "domains": {
            "karir": "Kamu unggul di pekerjaan yang butuh presisi tinggi, seperti analisis data, "
                     "kontrol kualitas, keuangan, atau riset yang menuntut ketelitian di setiap "
                     "langkahnya. Rekan kerja mengandalkanmu justru saat sesuatu perlu dicek ulang "
                     "dengan sangat hati-hati sebelum dilepas ke publik atau klien. Namun kamu bisa "
                     "terlihat lambat mengambil keputusan di situasi yang sebenarnya butuh respons "
                     "cepat, karena kebiasaanmu selalu ingin memastikan semuanya benar dulu. Kritikmu "
                     "yang detail juga kadang terdengar terlalu tajam buat rekan kerja yang belum "
                     "terbiasa dengan gaya komunikasimu yang lugas soal kesalahan. *PR: saat memberi "
                     "masukan ke rekan kerja, mulai dengan satu hal yang sudah mereka lakukan dengan "
                     "baik sebelum masuk ke bagian yang perlu diperbaiki.*",
            "asmara": "Kamu menunjukkan kasih sayang lewat tindakan yang konsisten dan penuh "
                      "perhatian pada detail kecil, seperti mengingat hal-hal spesifik yang penting "
                      "bagi pasangan. Kamu setia dan bisa diandalkan, jarang membuat keputusan besar "
                      "dalam hubungan tanpa berpikir matang lebih dulu. Namun kamu bisa terlihat "
                      "kurang ekspresif secara emosional, sehingga pasangan kadang butuh kepastian "
                      "lebih soal perasaanmu yang sebenarnya cukup dalam. Kamu juga cenderung "
                      "menganalisis hubungan seperti masalah yang harus dipecahkan, padahal kadang "
                      "pasangan hanya butuh didengar tanpa perlu solusi. *PR: sekali seminggu, coba "
                      "ucapkan langsung apa yang kamu rasakan ke pasangan tanpa menunggu ditanya "
                      "dulu.*",
            "keuangan": "Kamu adalah pengelola uang yang rapi dan terencana, suka mencatat "
                        "pengeluaran dan membuat anggaran yang jelas sebelum mengambil keputusan "
                        "finansial apa pun. Kebiasaan ini membuatmu jarang terjebak masalah finansial "
                        "mendadak karena kamu memang menyiapkan segalanya dengan matang. Namun "
                        "kehati-hatianmu kadang membuatmu terlalu lama menimbang sebelum berinvestasi, "
                        "sampai peluang yang sebenarnya bagus keburu lewat. Kamu juga bisa terlalu "
                        "fokus pada angka sampai lupa menikmati hasil kerja keras yang sudah kamu "
                        "kumpulkan. *PR: alokasikan sebagian kecil dana khusus untuk sesuatu yang "
                        "kamu nikmati tanpa perlu dianalisis dulu untung-ruginya.*",
            "kesehatan": "Kamu cenderung disiplin soal pola makan dan rutinitas kesehatan, suka "
                         "mempelajari detail soal apa yang baik untuk tubuhmu sebelum menerapkannya. "
                         "Ketelitian ini membuat kebiasaan sehatmu biasanya cukup konsisten begitu "
                         "kamu yakin itu benar. Namun kecenderungan overthinking bisa membuat "
                         "pikiranmu tegang, dan itu sering muncul lewat ketegangan fisik seperti bahu "
                         "kaku atau susah tidur karena pikiran masih berputar. Kamu juga bisa terlalu "
                         "kritis pada tubuh sendiri kalau hasil belum sesuai standar yang kamu "
                         "tetapkan. *PR: coba satu teknik relaksasi sederhana seperti menarik napas "
                         "dalam sebelum tidur, khusus untuk menenangkan pikiran yang masih aktif "
                         "menganalisis.*",
        },
    },
}
