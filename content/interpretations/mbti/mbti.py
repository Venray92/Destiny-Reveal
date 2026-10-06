"""
Konten MBTI (16 tipe kepribadian).

Key dict ini HARUS sama persis dengan hasil engine/mbti_scoring.py
(score_mbti()["tipe"]) supaya bisa langsung dipakai sebagai lookup:
ISTJ, ISFJ, INFJ, INTJ, ISTP, ISFP, INFP, INTP, ESTP, ESFP, ENFP, ENTP,
ESTJ, ESFJ, ENFJ, ENTJ.

Struktur tiap entri sama persis dengan pola di content/interpretations/zodiak.py
(tagline, chip, title, p1_label, p1, p2_label, p2, quote, p3_label, p3,
domains: karir/asmara/keuangan/kesehatan) supaya bisa dipakai lewat
mekanisme lock/unlock + expander yang sama (lihat views/revealpage.py).
"""

MBTI_CONTENT = {
    "ISTJ": {
        "tagline": "🗂️ Sang Penjaga Aturan",
        "chip": "MBTI",
        "title": "ISTJ — Sang Penjaga yang Teguh Pendirian",
        "p1_label": "Siapa Kamu",
        "p1": "Kamu adalah tipe yang paling bisa diandalkan untuk memastikan sesuatu benar-benar "
              "selesai, bukan cuma dimulai dengan semangat lalu terbengkalai. Kamu percaya pada "
              "struktur, prosedur, dan bukti nyata, bukan pada kata-kata manis yang belum tentu "
              "terbukti. Sejak muda, kamu biasanya sudah jadi anak yang bisa dipegang janjinya, "
              "orang tua atau guru tahu kalau tugas diserahkan ke kamu, hasilnya pasti rapi dan "
              "tepat waktu. Kamu lebih suka belajar dari pengalaman langsung dan data yang sudah "
              "terbukti daripada teori yang masih mengambang, dan kamu jarang bertindak sebelum "
              "benar-benar yakin. Di lingkungan sosial, kamu bukan tipe yang butuh jadi pusat "
              "perhatian, kamu lebih nyaman jadi orang yang bekerja diam-diam di belakang layar "
              "tapi hasilnya paling konsisten. Kesetiaanmu pada komitmen, baik itu pekerjaan, "
              "keluarga, atau janji kecil sekalipun, jadi salah satu ciri paling kuat yang orang "
              "kenal dari dirimu. Kamu menghargai tradisi dan cara-cara yang sudah terbukti "
              "berhasil, bukan karena takut perubahan, tapi karena kamu paham betul risiko dari "
              "mengganti sesuatu yang sudah berjalan baik tanpa alasan yang jelas. Orang-orang di "
              "sekitarmu sering datang minta pendapat soal hal-hal praktis, karena mereka tahu "
              "kamu akan menjawab dengan realistis, bukan sekadar menyenangkan hati.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kedisiplinan dan tanggung jawabmu bikin orang lain merasa aman kalau ada kamu di "
              "tim, karena mereka tahu apa pun yang kamu pegang pasti dikerjakan sampai tuntas. "
              "Kamu juga jujur dan konsisten, kata-katamu bisa dipegang, dan itu jadi fondasi "
              "kepercayaan yang sulit ditandingi tipe lain. Tapi kesetiaanmu pada cara yang sudah "
              "terbukti kadang bikin kamu agak keberatan menerima ide baru yang belum ada "
              "buktinya, meski ide itu sebenarnya punya potensi bagus. Kamu juga cenderung "
              "memendam perasaan sendiri demi menjaga stabilitas, sampai akhirnya numpuk dan "
              "keluar sekaligus dalam bentuk yang tidak terduga. Standar tinggi yang kamu pegang "
              "untuk diri sendiri kadang diterapkan juga ke orang lain tanpa kamu sadari, "
              "membuat mereka merasa dinilai terus-menerus meski niatmu sebenarnya baik.",
        "quote": "Kestabilan yang kamu jaga akan terasa lebih hidup kalau sesekali kamu kasih "
                 "ruang untuk hal yang belum tentu pasti.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba sekali waktu, terima satu ide atau cara baru yang belum pernah kamu coba, "
              "meski belum ada bukti nyata bahwa itu akan berhasil. Anggap ini bukan mengganti "
              "prinsipmu, tapi menambah satu data baru ke pengalamanmu. Latih juga diri untuk "
              "mengungkapkan perasaan lebih awal, sebelum semuanya menumpuk jadi beban yang berat "
              "sendirian. Kamu bisa mulai dari hal kecil, misalnya cerita ke satu orang yang kamu "
              "percaya soal apa yang sebenarnya kamu rasakan minggu ini, bukan cuma soal apa "
              "yang harus dikerjakan.",
        "domains": {
            "karir": "Kamu paling bersinar di posisi yang butuh ketelitian, konsistensi, dan "
                     "tanggung jawab jelas, seperti keuangan, operasional, audit, atau posisi "
                     "manajerial yang menuntut sistem rapi. Atasan biasanya menaruh kepercayaan "
                     "besar padamu karena kamu jarang lalai dan selalu menyelesaikan apa yang "
                     "dijanjikan. Tapi kamu bisa kesulitan di lingkungan kerja yang serba cepat "
                     "berubah dan minim aturan jelas, karena kamu butuh struktur untuk bekerja "
                     "optimal. Kamu juga kadang ragu mengambil inisiatif di luar deskripsi "
                     "tugasmu, meski sebenarnya kamu mampu, karena terbiasa menunggu arahan yang "
                     "jelas dulu. *PR: sekali waktu, ajukan satu ide perbaikan proses tanpa "
                     "menunggu diminta, biar atasan tahu kapasitasmu lebih dari sekadar "
                     "eksekutor.*",
            "asmara": "Kamu tipe pasangan yang setia, konsisten, dan menunjukkan cinta lewat "
                      "tindakan nyata, bukan kata-kata manis, misalnya selalu ada saat "
                      "dibutuhkan atau mengingat detail kecil yang penting buat pasangan. "
                      "Namun kamu kadang kesulitan mengungkapkan perasaan secara terbuka, "
                      "sehingga pasangan bisa merasa kamu dingin padahal sebenarnya kamu peduli "
                      "sekali. Kamu juga bisa terlalu kaku soal cara berhubungan yang "
                      "\"seharusnya\", padahal setiap hubungan punya ritmenya sendiri. *PR: coba "
                      "ucapkan langsung satu hal yang kamu hargai dari pasangan, jangan cuma "
                      "ditunjukkan lewat tindakan.*",
            "keuangan": "Kamu hampir selalu punya rencana keuangan yang rapi, suka mencatat "
                        "pengeluaran, dan jarang tergoda belanja impulsif karena kamu berpikir "
                        "panjang sebelum mengeluarkan uang. Kebiasaan menabung dan menghindari "
                        "utang biasanya sudah jadi refleks alami buatmu. Tapi sisi hati-hatimu "
                        "kadang bikin kamu terlalu takut ambil risiko finansial yang sebenarnya "
                        "sudah cukup terukur, sampai melewatkan peluang yang lumayan bagus. "
                        "*PR: coba pelajari satu instrumen investasi baru yang risikonya masih "
                        "wajar, jangan cuma menyimpan semua di tempat yang paling aman.*",
            "kesehatan": "Kamu cenderung disiplin soal rutinitas, jam tidur, dan pola makan, "
                         "karena kamu memang nyaman dengan keteraturan. Tapi kebiasaan memendam "
                         "stres demi terlihat tegar bisa jadi beban tersembunyi yang baru terasa "
                         "setelah menumpuk lama, biasanya muncul sebagai ketegangan fisik atau "
                         "kelelahan yang sulit dijelaskan. Kamu juga jarang cerita kalau sedang "
                         "capek secara mental, karena merasa itu bukan hal yang perlu "
                         "dipublikasikan. *PR: sisihkan waktu rutin buat cek keadaan diri "
                         "sendiri, bukan cuma fisik, tapi juga soal apa yang kamu rasakan.*",
        },
    },
    "ISFJ": {
        "tagline": "🕊️ Sang Pelindung Sunyi",
        "chip": "MBTI",
        "title": "ISFJ — Sang Pelindung yang Setia Tanpa Banyak Bicara",
        "p1_label": "Siapa Kamu",
        "p1": "Kamu adalah tipe yang mengurus banyak hal untuk orang lain tanpa perlu diminta, "
              "dan sering kali baru disadari betapa pentingnya keberadaanmu justru saat kamu "
              "sedang tidak ada. Kamu memperhatikan detail kecil tentang orang-orang di "
              "sekitarmu, kebiasaan, preferensi, hal-hal yang mereka suka atau tidak suka, dan "
              "menyimpannya diam-diam untuk dipakai di saat yang tepat. Sejak kecil, kamu "
              "mungkin sudah jadi anak yang peka terhadap suasana hati orang di rumah, cepat "
              "menangkap kalau ada yang tidak beres meski tidak diucapkan. Kamu lebih suka "
              "bekerja di belakang layar, memastikan semuanya berjalan lancar, daripada tampil "
              "di depan dan menerima pujian. Rasa tanggung jawabmu terhadap orang-orang yang "
              "kamu sayangi sangat besar, kadang sampai kamu menomorduakan kebutuhanmu sendiri "
              "demi memastikan mereka baik-baik saja. Kamu menghargai tradisi, kenangan, dan "
              "hal-hal yang sudah terbukti membawa kehangatan, jadi kamu jarang buru-buru "
              "meninggalkan sesuatu yang sudah punya nilai emosional. Di tempat kerja atau "
              "pertemanan, kamu jadi sosok yang paling diandalkan untuk urusan praktis, orang "
              "tahu kalau minta bantuan ke kamu, pasti akan benar-benar dibantu sampai selesai. "
              "Meski terlihat pendiam, sebenarnya kamu punya perhatian yang sangat dalam "
              "terhadap dunia di sekitarmu.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kepedulian dan ketelitianmu terhadap kebutuhan orang lain bikin kamu jadi sosok "
              "yang bikin siapa pun merasa diperhatikan dan aman di dekatmu. Kamu juga pekerja "
              "keras yang jarang mengeluh, lebih memilih menyelesaikan tugas diam-diam daripada "
              "membesar-besarkannya. Tapi kebiasaan mendahulukan orang lain ini kadang membuat "
              "kebutuhanmu sendiri terabaikan sampai bertahun-tahun, dan kamu baru sadar sudah "
              "terlalu lelah setelah semuanya menumpuk. Kamu juga cenderung menghindari konflik "
              "dengan cara mengalah terus-menerus, padahal sebenarnya kamu punya pendapat yang "
              "valid untuk disuarakan. Rasa tidak enak untuk menolak permintaan orang lain "
              "kadang bikin kamu kewalahan sendiri karena terlalu banyak tanggung jawab yang "
              "kamu pikul.",
        "quote": "Merawat orang lain akan terasa lebih ringan kalau kamu juga mengizinkan "
                 "dirimu sendiri untuk dirawat.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba latih diri untuk bilang \"tidak\" pada satu permintaan yang sebenarnya "
              "memberatkanmu, meski itu terasa canggung di awal. Ingat bahwa menolak sesuatu "
              "bukan berarti kamu berhenti peduli, hanya saja kamu juga berhak menjaga "
              "batasanmu sendiri. Sisihkan waktu khusus untuk melakukan sesuatu yang murni "
              "kamu nikmati, tanpa ada unsur mengurus orang lain di dalamnya. Kalau ada "
              "perasaan tidak nyaman terhadap seseorang, coba sampaikan pelan-pelan, jangan "
              "cuma dipendam sampai kamu benar-benar lelah menahannya.",
        "domains": {
            "karir": "Kamu unggul di peran yang butuh kepedulian tinggi dan detail rapi, "
                     "seperti layanan pelanggan, kesehatan, pendidikan, HR, atau posisi "
                     "pendukung yang bikin tim lain bisa bekerja lancar. Rekan kerja sering "
                     "mengandalkanmu untuk hal-hal yang \"remeh\" tapi sebenarnya krusial, dan "
                     "kamu selalu menyelesaikannya dengan baik. Sayangnya, kamu kadang kesulitan "
                     "mempromosikan hasil kerjamu sendiri, membiarkan orang lain mengambil "
                     "kredit karena kamu tidak enak menonjolkan diri. Kamu juga bisa kewalahan "
                     "kalau terus-menerus diminta bantuan tambahan tanpa berani menetapkan "
                     "batas. *PR: sekali waktu, catat dan sampaikan sendiri kontribusimu ke "
                     "atasan, jangan tunggu orang lain yang menyebutkannya.*",
            "asmara": "Kamu pasangan yang penuh perhatian, mengingat detail kecil yang penting "
                      "buat orang yang kamu sayangi, dan selalu berusaha membuat mereka nyaman. "
                      "Kesetiaanmu dalam hubungan biasanya sangat kuat, kamu jarang "
                      "setengah-setengah kalau sudah berkomitmen. Tapi kamu sering memendam "
                      "kekecewaan demi menghindari konflik, sampai akhirnya perasaan itu "
                      "menumpuk dan meledak dalam bentuk yang tidak terduga bagi pasangan. Kamu "
                      "juga kadang terlalu banyak berkorban tanpa menyampaikan kebutuhanmu "
                      "sendiri, berharap pasangan bisa menebaknya sendiri. *PR: sampaikan satu "
                      "kebutuhanmu secara langsung ke pasangan minggu ini, jangan cuma "
                      "diharapkan mereka akan tahu sendiri.*",
            "keuangan": "Kamu cenderung hati-hati dan suka menyisihkan uang untuk kebutuhan "
                        "orang-orang terdekat, sering kali lebih mementingkan keperluan keluarga "
                        "atau pasangan daripada keinginan pribadi. Kebiasaan menabung untuk "
                        "kebutuhan jangka panjang biasanya sudah tertanam kuat dalam dirimu. "
                        "Namun kamu bisa terlalu murah hati sampai lupa menyisihkan untuk "
                        "dirimu sendiri, atau merasa bersalah kalau membeli sesuatu untuk "
                        "kesenanganmu sendiri. *PR: alokasikan satu pos kecil khusus untuk "
                        "kebutuhanmu sendiri tiap bulan, dan pakai tanpa rasa bersalah.*",
            "kesehatan": "Kamu rentan menyerap beban emosional orang-orang di sekitarmu sampai "
                         "lupa mengurus kondisimu sendiri, dan sering menunda istirahat karena "
                         "merasa masih ada yang perlu dibantu. Tubuhmu biasanya jadi tempat "
                         "pertama yang memberi sinyal kalau kamu sudah kelelahan, lewat sakit "
                         "kepala, gangguan pencernaan, atau kelelahan yang sulit hilang meski "
                         "sudah tidur cukup. Kamu juga cenderung menahan diri untuk periksa ke "
                         "dokter kalau merasa keluhannya \"belum seberapa\". *PR: jadwalkan satu "
                         "waktu istirahat mingguan yang benar-benar untuk dirimu sendiri, tanpa "
                         "diganggu urusan orang lain.*",
        },
    },
    "INFJ": {
        "tagline": "🔮 Sang Penglihat yang Jarang Ditemukan",
        "chip": "MBTI",
        "title": "INFJ — Sang Idealis yang Melihat Lebih Dalam",
        "p1_label": "Siapa Kamu",
        "p1": "Kamu adalah tipe yang jarang ditemukan, dan orang yang mengenalmu dengan baik "
              "biasanya merasakan ada kedalaman tersendiri dalam cara kamu memandang dunia. "
              "Kamu punya kemampuan menangkap makna di balik hal-hal yang tidak terucap, sering "
              "kali kamu tahu ada yang salah pada seseorang jauh sebelum mereka sendiri sadar "
              "atau mau mengakuinya. Sejak muda, kamu mungkin sering merasa berbeda dari "
              "teman-teman sebaya, lebih suka merenung sendirian atau bicara panjang tentang "
              "makna hidup daripada obrolan ringan sehari-hari. Kamu punya visi yang kuat "
              "tentang bagaimana dunia seharusnya berjalan, dan visi itu sering jadi pendorong "
              "di balik pilihan-pilihan besar dalam hidupmu. Kamu memilih pertemanan yang "
              "sedikit tapi dalam, daripada banyak kenalan yang hanya di permukaan, karena kamu "
              "butuh koneksi yang benar-benar bermakna untuk merasa terhubung. Dalam bekerja "
              "atau berkarya, kamu ingin apa yang kamu lakukan punya tujuan yang lebih besar "
              "dari sekadar mencari nafkah, kamu ingin merasa apa yang kamu kerjakan benar-benar "
              "berarti. Orang-orang sering datang padamu untuk curhat, karena kamu punya cara "
              "mendengarkan yang membuat mereka merasa benar-benar dipahami. Di balik "
              "ketenangan yang kamu tunjukkan ke luar, sebenarnya ada dunia batin yang sangat "
              "ramai dengan pemikiran dan perasaan.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kepekaan dan wawasanmu terhadap orang lain membuatmu jadi sosok yang bisa "
              "memberi nasihat mendalam, bukan sekadar basa-basi menenangkan. Idealismemu juga "
              "jadi bahan bakar yang kuat untuk memperjuangkan hal-hal yang kamu yakini benar. "
              "Tapi standar tinggi yang kamu pasang, baik untuk dirimu sendiri maupun dunia di "
              "sekitarmu, kadang bikin kamu gampang kecewa saat kenyataan tidak sesuai harapan. "
              "Kamu juga rentan kelelahan secara emosional karena terlalu banyak menyerap "
              "perasaan orang lain, sampai lupa mengurus dirimu sendiri. Kecenderungan untuk "
              "memendam pemikiran dan perasaan sendiri, alih-alih membaginya, kadang bikin kamu "
              "merasa kesepian meski dikelilingi banyak orang.",
        "quote": "Visi besar yang kamu bawa akan lebih ringan dijalani kalau kamu izinkan "
                 "dirimu istirahat dari menyelamatkan semua orang.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba bagikan satu pemikiran atau perasaan yang selama ini cuma kamu simpan "
              "sendiri, ke satu orang yang benar-benar kamu percaya. Kamu tidak harus selalu "
              "jadi pihak yang mendengarkan, sesekali biarkan dirimu jadi yang didengarkan "
              "juga. Latih diri untuk menerima bahwa tidak semua hal bisa sesuai idealmu, dan "
              "itu bukan berarti usahamu sia-sia. Beri jeda waktu sendirian yang cukup setiap "
              "hari untuk mengisi ulang energimu, sebelum kembali memberi perhatian ke orang "
              "lain.",
        "domains": {
            "karir": "Kamu berkembang di bidang yang punya makna dan dampak jelas, seperti "
                     "konseling, penulisan, psikologi, pekerjaan sosial, atau peran strategis "
                     "yang butuh visi jangka panjang. Kamu paling produktif kalau merasa apa "
                     "yang dikerjakan benar-benar berarti, bukan sekadar mengejar target angka. "
                     "Tapi kamu bisa cepat jenuh di pekerjaan yang terasa hampa atau penuh "
                     "birokrasi tanpa tujuan jelas, dan kesulitan menyembunyikan kekecewaan itu. "
                     "Kamu juga cenderung memendam ketidakpuasan di tempat kerja sampai "
                     "akhirnya memilih pergi tanpa banyak drama. *PR: sampaikan langsung ke "
                     "atasan kalau ada bagian pekerjaan yang terasa tidak sejalan dengan "
                     "nilaimu, jangan cuma dipendam sampai capek sendiri.*",
            "asmara": "Kamu mencari hubungan yang dalam dan bermakna, bukan sekadar status, "
                      "dan kamu bisa sangat setia serta suportif pada pasangan yang benar-benar "
                      "kamu percaya. Kamu punya kepekaan tinggi terhadap kebutuhan emosional "
                      "pasangan, kadang bahkan sebelum mereka mengungkapkannya sendiri. Namun "
                      "kamu juga bisa memasang standar hubungan yang sangat ideal, sehingga "
                      "kecewa saat kenyataan tidak seindah bayanganmu. Kamu cenderung menahan "
                      "diri untuk mengungkapkan ketidakpuasan, sampai akhirnya merasa jauh "
                      "tanpa pasangan tahu penyebabnya. *PR: ungkapkan satu kekhawatiran kecil "
                      "dalam hubungan sekarang juga, jangan tunggu sampai jadi jarak yang besar.*",
            "keuangan": "Kamu biasanya tidak terlalu tertarik pada uang untuk gengsi, tapi "
                        "lebih pada apa yang bisa dilakukan uang itu untuk mendukung nilai atau "
                        "tujuan hidupmu. Kamu cenderung cukup hati-hati dalam mengelola "
                        "keuangan, meski kadang kurang memberi perhatian detail karena "
                        "pikiranmu sibuk dengan hal-hal yang lebih besar. Kamu juga rentan "
                        "mengorbankan kebutuhan finansial sendiri demi membantu orang lain "
                        "atau tujuan yang kamu yakini penting. *PR: buat rencana keuangan "
                        "sederhana yang tetap kasih ruang untuk membantu orang lain, tapi tidak "
                        "mengorbankan kebutuhan dasarmu sendiri.*",
            "kesehatan": "Kamu rentan kelelahan mental karena terlalu banyak berpikir dan "
                         "menyerap emosi dari sekitarmu, sampai sulit mematikan pikiran saat "
                         "waktunya istirahat. Kamu juga cenderung menyimpan stres sendirian, "
                         "jarang mencari bantuan meski sebenarnya sudah kewalahan. Pola tidur "
                         "yang terganggu karena pikiran yang terus berputar jadi salah satu "
                         "keluhan yang sering muncul pada tipe ini. *PR: coba praktikkan rutinitas "
                         "sederhana sebelum tidur untuk \"mematikan\" pikiran, misalnya menulis "
                         "jurnal singkat sebelum berbaring.*",
        },
    },
    "INTJ": {
        "tagline": "♟️ Sang Perencana Jangka Panjang",
        "chip": "MBTI",
        "title": "INTJ — Sang Perencana yang Selalu Berpikir Jauh ke Depan",
        "p1_label": "Siapa Kamu",
        "p1": "Kamu adalah tipe yang selalu punya rencana, dan bukan sekadar rencana biasa, "
              "tapi peta besar yang sudah dipikirkan sampai beberapa langkah ke depan. Kamu "
              "tidak suka bertindak asal-asalan, setiap keputusan besar biasanya sudah melalui "
              "analisis panjang di kepalamu sebelum kamu ambil. Sejak kecil, kamu mungkin sudah "
              "terbiasa berpikir mandiri, tidak terlalu bergantung pada pendapat orang lain "
              "untuk menentukan apa yang kamu yakini benar. Kamu punya standar intelektual yang "
              "tinggi, baik untuk dirimu sendiri maupun orang-orang yang kamu ajak berdiskusi, "
              "dan kamu jarang puas dengan jawaban yang terasa dangkal. Dalam pergaulan, kamu "
              "lebih memilih sedikit orang yang benar-benar bisa diajak diskusi bermakna "
              "daripada lingkaran pertemanan yang luas tapi dangkal. Kamu punya visi jangka "
              "panjang yang kuat tentang mau jadi apa dan mau ke mana hidupmu, dan kamu bekerja "
              "sistematis untuk mencapainya, bukan cuma berangan-angan. Orang-orang sering "
              "melihatmu sebagai sosok yang tenang dan penuh perhitungan, jarang panik meski "
              "situasinya rumit, karena kamu sudah terbiasa memikirkan kemungkinan terburuk "
              "sebelum itu terjadi. Kamu juga tidak takut mempertanyakan cara-cara lama kalau "
              "menurutmu ada cara yang lebih efisien untuk mencapai hasil yang sama.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kemampuanmu melihat gambaran besar dan menyusun strategi jangka panjang bikin "
              "kamu jadi sosok yang diandalkan untuk merancang solusi rumit yang orang lain "
              "belum kepikiran. Kepercayaan dirimu pada penilaian sendiri juga bikin kamu jarang "
              "goyah oleh tekanan sosial. Tapi keyakinan kuat pada logikamu sendiri kadang "
              "bikin kamu kurang sabar pada orang yang berpikir lebih lambat atau butuh "
              "penjelasan berulang, meski itu bukan berarti mereka kurang mampu. Kamu juga bisa "
              "terlihat dingin atau jauh di mata orang lain, padahal sebenarnya kamu peduli, "
              "hanya saja caramu menunjukkannya tidak selalu lewat kata-kata hangat. "
              "Kecenderungan untuk terlalu percaya pada rencana sendiri kadang bikin kamu agak "
              "keberatan menerima masukan dari orang lain, meski masukan itu sebenarnya valid.",
        "quote": "Rencana paling matang sekalipun akan lebih kuat kalau kamu beri ruang untuk "
                 "masukan dari orang yang melihat sudut pandang berbeda.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba minta pendapat dari satu orang yang punya cara berpikir berbeda darimu "
              "soal rencana yang sedang kamu susun, lalu dengarkan tanpa langsung membantah. "
              "Latih diri untuk mengungkapkan apresiasi secara verbal ke orang-orang di "
              "sekitarmu, jangan hanya lewat tindakan atau hasil kerja. Sesekali, biarkan "
              "dirimu melakukan sesuatu yang tidak ada dalam rencana besar, sekadar untuk "
              "bersenang-senang tanpa tujuan produktif. Ingat bahwa tidak semua orang berpikir "
              "secepat dirimu, dan itu bukan kekurangan mereka.",
        "domains": {
            "karir": "Kamu unggul di posisi strategis yang butuh analisis mendalam dan "
                     "perencanaan jangka panjang, seperti manajemen, riset, teknologi, atau "
                     "posisi kepemimpinan yang merancang arah besar organisasi. Kamu paling "
                     "puas kalau diberi otonomi untuk menentukan cara kerja sendiri, bukan "
                     "diawasi ketat langkah demi langkah. Tapi kamu bisa terlihat sulit "
                     "didekati oleh rekan kerja yang tidak terbiasa dengan gaya komunikasimu "
                     "yang langsung dan efisien, sehingga kadang disalahartikan sebagai sombong. "
                     "Kamu juga kurang sabar pada rapat yang bertele-tele tanpa hasil konkret. "
                     "*PR: luangkan waktu untuk basa-basi singkat dengan rekan kerja sebelum "
                     "masuk ke inti pembicaraan, biar hubungan kerja terasa lebih hangat.*",
            "asmara": "Kamu pasangan yang setia dan serius kalau sudah berkomitmen, jarang "
                      "main-main soal perasaan, dan selalu memikirkan masa depan hubungan "
                      "secara matang. Kamu juga menghargai pasangan yang bisa diajak diskusi "
                      "mendalam, bukan cuma obrolan ringan. Tapi kamu kadang kesulitan "
                      "mengekspresikan kasih sayang secara terbuka, sehingga pasangan bisa "
                      "merasa kamu jauh padahal sebenarnya kamu sangat peduli. Kamu juga "
                      "cenderung menganalisis hubungan terlalu rasional, sampai lupa momen "
                      "kecil yang sederhana juga penting. *PR: sesekali lakukan hal romantis "
                      "spontan tanpa perlu dipikirkan dulu untung-ruginya.*",
            "keuangan": "Kamu punya perencanaan keuangan yang matang dan biasanya sudah "
                        "memikirkan strategi jangka panjang seperti investasi atau dana pensiun "
                        "jauh sebelum orang lain memikirkannya. Kamu jarang tergoda belanja "
                        "impulsif karena selalu berpikir dulu sebelum mengeluarkan uang. Tapi "
                        "kamu bisa terlalu fokus pada efisiensi sampai lupa menikmati hasil "
                        "kerja kerasmu sendiri sesekali. *PR: alokasikan satu pos kecil khusus "
                        "untuk kesenangan tanpa perlu dianalisis untung-ruginya dulu.*",
            "kesehatan": "Kamu cenderung mengabaikan kebutuhan fisik saat sedang fokus "
                         "mengejar target atau menyelesaikan proyek besar, sampai lupa makan "
                         "atau tidur cukup. Pikiranmu yang terus aktif juga bikin kamu susah "
                         "benar-benar rileks, bahkan saat sedang \"istirahat\" pikiranmu masih "
                         "bekerja memikirkan hal lain. Kamu juga jarang terbuka soal beban "
                         "mental yang kamu rasakan karena merasa itu harus bisa diatasi "
                         "sendiri. *PR: jadwalkan waktu istirahat sebagai agenda yang sama "
                         "pentingnya dengan pekerjaan, bukan sekadar sisa waktu kalau sempat.*",
        },
    },
    "ISTP": {
        "tagline": "🔧 Sang Pengrajin Diam-diam",
        "chip": "MBTI",
        "title": "ISTP — Sang Pengrajin yang Tenang tapi Piawai",
        "p1_label": "Siapa Kamu",
        "p1": "Kamu adalah tipe yang paling nyaman belajar lewat praktik langsung, bukan lewat "
              "teori yang panjang lebar. Kamu suka mengutak-atik sesuatu sampai paham cara "
              "kerjanya, entah itu alat, sistem, atau masalah yang butuh solusi praktis. Sejak "
              "kecil, kamu mungkin sudah jadi anak yang senang membongkar mainan atau alat "
              "elektronik sekadar untuk tahu isinya, bukan untuk merusak. Kamu tenang di "
              "tengah situasi yang membuat orang lain panik, karena kepalamu otomatis mencari "
              "solusi praktis alih-alih ikut larut dalam kepanikan. Kamu juga tidak suka "
              "terikat aturan yang terasa tidak masuk akal, kamu lebih percaya pada logika dan "
              "hasil nyata daripada sekadar mengikuti tradisi. Dalam pergaulan, kamu tidak "
              "banyak bicara, tapi kalau sudah bicara biasanya to the point dan jujur apa "
              "adanya. Kamu menghargai kebebasan bergerak dan tidak suka diatur terlalu ketat, "
              "kamu bekerja paling baik kalau diberi ruang untuk menemukan cara sendiri. "
              "Orang-orang di sekitarmu sering kagum dengan caramu tetap kalem menghadapi "
              "masalah teknis atau darurat yang bikin panik orang lain.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Ketenanganmu di tengah tekanan dan kemampuan praktismu menyelesaikan masalah "
              "bikin kamu jadi sosok yang dicari saat situasi darurat atau teknis muncul. Kamu "
              "juga jujur dan tidak suka drama, orang tahu persis di mana posisinya kalau "
              "berurusan denganmu. Tapi kecenderunganmu untuk menghindari komitmen jangka "
              "panjang kadang bikin orang lain merasa sulit memprediksi kehadiranmu. Kamu juga "
              "kurang suka membahas perasaan secara mendalam, sehingga orang terdekatmu kadang "
              "merasa tidak tahu apa yang sebenarnya kamu rasakan. Sikap cuek terhadap aturan "
              "sosial yang menurutmu tidak logis kadang membuat orang lain menganggapmu acuh, "
              "padahal kamu sebenarnya cuma memilih fokus pada hal yang menurutmu penting.",
        "quote": "Kebebasan yang kamu jaga akan terasa lebih bermakna kalau sesekali kamu bagi "
                 "sedikit ruang itu untuk orang-orang yang peduli padamu.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba ceritakan satu hal yang sedang kamu pikirkan atau rasakan ke orang yang "
              "kamu percaya, meski terasa canggung di awal. Kamu tidak perlu langsung fasih "
              "membahas perasaan, cukup mulai dari satu kalimat sederhana. Latih diri untuk "
              "tetap hadir di satu komitmen sampai selesai, meski rasa bosan mulai muncul di "
              "tengah jalan. Sesekali, tanyakan kabar orang terdekatmu bukan karena ada masalah "
              "teknis yang perlu dipecahkan, tapi sekadar untuk menunjukkan kamu peduli.",
        "domains": {
            "karir": "Kamu bersinar di bidang teknis dan praktis yang butuh keterampilan "
                     "tangan atau pemecahan masalah langsung, seperti teknik, IT, mekanik, "
                     "desain produk, atau pekerjaan lapangan yang dinamis. Kamu paling produktif "
                     "kalau diberi kebebasan menentukan cara kerja sendiri, bukan diikat "
                     "prosedur kaku. Tapi kamu bisa cepat bosan dengan pekerjaan rutin yang "
                     "terlalu administratif atau penuh rapat panjang tanpa hasil nyata. Kamu "
                     "juga kurang suka mempromosikan diri, sehingga kontribusimu kadang kurang "
                     "terlihat dibanding rekan yang lebih vokal. *PR: sesekali, ceritakan hasil "
                     "kerjamu secara terbuka ke tim, jangan cuma diam-diam menyelesaikannya.*",
            "asmara": "Kamu pasangan yang tenang dan tidak banyak menuntut drama, lebih suka "
                      "menunjukkan sayang lewat tindakan nyata seperti membantu menyelesaikan "
                      "masalah praktis pasangan. Kamu juga menghargai ruang pribadi dan "
                      "berharap pasangan memahami kebutuhanmu untuk waktu sendiri. Namun kamu "
                      "kadang terlalu menahan diri untuk membahas perasaan secara terbuka, "
                      "membuat pasangan merasa sulit membaca apa yang sebenarnya kamu rasakan. "
                      "*PR: coba ungkapkan satu perasaanmu secara langsung ke pasangan, jangan "
                      "cuma ditunjukkan lewat tindakan.*",
            "keuangan": "Kamu cenderung praktis soal uang, lebih suka membeli barang yang "
                        "fungsional dan tahan lama daripada sekadar ikut tren. Kamu juga tidak "
                        "terlalu suka repot dengan perencanaan keuangan yang rumit, lebih "
                        "nyaman dengan sistem sederhana yang bisa langsung kamu pahami. Tapi "
                        "kadang kamu kurang memikirkan rencana jangka panjang karena fokus pada "
                        "kebutuhan saat ini saja. *PR: sisihkan sedikit waktu untuk membuat "
                        "rencana keuangan jangka panjang sederhana, meski terasa membosankan.*",
            "kesehatan": "Kamu cenderung aktif secara fisik dan senang aktivitas yang "
                         "menantang, tapi kadang kurang memperhatikan sinyal tubuh yang minta "
                         "istirahat karena terlalu asyik dengan apa yang sedang dikerjakan. "
                         "Kamu juga jarang membicarakan beban emosional, lebih memilih "
                         "menyimpannya sendiri sampai kadang muncul sebagai ketegangan fisik. "
                         "*PR: kalau merasa lelah secara fisik atau emosional, coba istirahat "
                         "dulu sebelum melanjutkan, jangan tunggu sampai benar-benar habis "
                         "tenaga.*",
        },
    },
    "ISFP": {
        "tagline": "🎨 Sang Seniman yang Hidup dengan Rasa",
        "chip": "MBTI",
        "title": "ISFP — Sang Seniman yang Hidup dengan Rasa",
        "p1_label": "Siapa Kamu",
        "p1": "Kamu adalah tipe yang menjalani hidup lewat rasa, bukan lewat aturan atau logika "
              "kaku semata. Kamu peka terhadap keindahan di sekitarmu, entah itu warna, musik, "
              "suasana, atau momen kecil yang orang lain sering lewatkan begitu saja. Sejak "
              "muda, kamu mungkin sudah terbiasa mengekspresikan diri lewat cara-cara kreatif, "
              "entah lewat gambar, tulisan, musik, atau sekadar cara berpakaian yang mencolok "
              "khas dirimu sendiri. Kamu memegang nilai-nilai pribadi dengan sangat kuat, "
              "meski tidak selalu diucapkan keras-keras, dan kamu tidak suka dipaksa hidup "
              "sesuai standar orang lain. Kamu cenderung menghindari konflik terbuka, lebih "
              "suka menjaga harmoni dan membiarkan tindakanmu berbicara dibanding berdebat "
              "panjang. Dalam pergaulan, kamu hangat dan baik hati, tapi butuh waktu untuk "
              "benar-benar membuka diri pada orang baru. Kamu hidup di momen sekarang, lebih "
              "suka menikmati apa yang ada di depan mata daripada terlalu sibuk merencanakan "
              "jauh ke depan. Orang-orang di sekitarmu sering merasa nyaman berada di dekatmu "
              "karena kamu jarang menghakimi dan selalu memberi ruang bagi mereka untuk jadi "
              "diri sendiri.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kepekaan estetikamu dan kemampuan menghargai keindahan bikin kamu jadi sosok "
              "yang bisa melihat sisi indah dari hal-hal yang orang lain anggap biasa saja. "
              "Kebaikan hati dan sikapmu yang tidak suka menghakimi juga bikin orang merasa "
              "aman jadi diri sendiri di dekatmu. Tapi kecenderunganmu menghindari konflik "
              "kadang bikin kamu memendam ketidakpuasan sampai lama, alih-alih menyelesaikannya "
              "lebih awal. Kamu juga bisa terlalu fokus pada momen sekarang sampai kurang "
              "memikirkan konsekuensi jangka panjang dari keputusan yang kamu ambil. Sikapmu "
              "yang lembut kadang membuat orang lain memanfaatkan kebaikanmu, karena kamu "
              "kesulitan menegaskan batasan secara tegas.",
        "quote": "Rasa yang kamu jaga dalam diri akan lebih kuat kalau kamu berani "
                 "menyuarakannya, bukan hanya merasakannya sendirian.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba sampaikan satu ketidaksetujuan kecil secara langsung ke orang yang "
              "bersangkutan, alih-alih memendamnya sampai terasa berat. Latih diri untuk "
              "memikirkan konsekuensi jangka panjang sebelum mengambil keputusan besar, tanpa "
              "harus kehilangan spontanitasmu yang khas. Beri dirimu waktu untuk mengevaluasi "
              "hubungan atau situasi yang sudah lama tidak membuatmu nyaman, jangan cuma "
              "bertahan karena tidak enak berubah. Sesekali, tegaskan batasan pada orang yang "
              "terus-menerus memanfaatkan kebaikanmu.",
        "domains": {
            "karir": "Kamu bersinar di bidang kreatif seperti seni, desain, fotografi, "
                     "musik, atau pekerjaan yang memberi ruang untuk ekspresi personal. Kamu "
                     "paling produktif di lingkungan yang fleksibel dan tidak terlalu terikat "
                     "aturan kaku. Tapi kamu bisa kesulitan di lingkungan kerja yang penuh "
                     "kompetisi terbuka atau konflik, karena kamu cenderung menghindarinya "
                     "daripada menghadapinya langsung. Kamu juga kadang kurang percaya diri "
                     "mempromosikan karya atau kemampuanmu sendiri. *PR: tunjukkan satu hasil "
                     "karyamu ke orang lain minggu ini, meski terasa tidak nyaman "
                     "dipamerkan.*",
            "asmara": "Kamu pasangan yang lembut, penuh perhatian, dan pandai menciptakan "
                      "momen hangat yang berkesan bagi orang yang kamu sayangi. Kamu juga "
                      "sangat menghargai kebebasan personal dalam hubungan, tidak suka "
                      "mengekang atau dikekang. Tapi kamu cenderung menghindari membahas "
                      "masalah dalam hubungan secara langsung, memilih diam sampai akhirnya "
                      "jarak itu terasa oleh pasangan. *PR: kalau ada yang mengganjal dalam "
                      "hubungan, bicarakan dalam 24 jam, jangan tunggu sampai terlupakan atau "
                      "menumpuk.*",
            "keuangan": "Kamu cenderung mengikuti kata hati soal belanja, sering membeli "
                        "sesuatu karena terasa indah atau bermakna secara personal, bukan "
                        "karena benar-benar dibutuhkan. Kamu juga kurang suka repot dengan "
                        "perencanaan keuangan detail, lebih nyaman menjalani apa adanya. "
                        "*PR: catat pengeluaran selama satu bulan penuh, supaya kamu punya "
                        "gambaran nyata tanpa perlu mengubah gaya hidup drastis dulu.*",
            "kesehatan": "Kamu peka terhadap suasana hati dan mudah terpengaruh energi "
                         "emosional di sekitarmu, sehingga rentan merasa lelah tanpa sebab "
                         "yang jelas kalau lingkunganmu sedang tegang. Kamu juga cenderung "
                         "memendam perasaan sendiri dan mengekspresikannya lewat kegiatan "
                         "kreatif, yang bagus, tapi kadang tidak cukup kalau bebannya sudah "
                         "terlalu besar. *PR: cari satu teman yang bisa diajak bicara terbuka "
                         "soal perasaan, jangan cuma disalurkan lewat karya sendirian.*",
        },
    },
    "INFP": {
        "tagline": "🌙 Sang Pemimpi yang Setia pada Hati",
        "chip": "MBTI",
        "title": "INFP — Sang Pemimpi yang Setia pada Nilai Sendiri",
        "p1_label": "Siapa Kamu",
        "p1": "Kamu adalah tipe yang hidup dengan dunia batin yang sangat kaya, penuh dengan "
              "nilai, cita-cita, dan imajinasi yang tidak selalu kamu tunjukkan ke luar. Kamu "
              "punya kompas moral yang kuat tentang apa yang benar dan salah menurutmu sendiri, "
              "dan kamu jarang mau berkompromi soal nilai-nilai inti yang kamu pegang. Sejak "
              "kecil, kamu mungkin sudah jadi anak yang suka menulis, membaca, atau membayangkan "
              "dunia lain yang lebih ideal daripada kenyataan di sekitarmu. Kamu peka terhadap "
              "perasaan orang lain, tapi lebih memilih memproses perasaanmu sendiri secara "
              "personal daripada langsung membaginya ke semua orang. Kamu punya keinginan kuat "
              "untuk hidup autentik, jadi diri sendiri tanpa perlu berpura-pura demi diterima "
              "lingkungan. Dalam pertemanan, kamu memilih kualitas dibanding kuantitas, beberapa "
              "orang yang benar-benar memahamimu jauh lebih berarti daripada banyak kenalan "
              "yang dangkal. Kamu sering jadi pendengar yang baik karena kamu tulus ingin "
              "memahami orang lain, bukan sekadar menunggu giliran bicara. Meski terlihat "
              "tenang di luar, sebenarnya ada dunia imajinasi dan idealisme yang sangat hidup "
              "di dalam dirimu.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kedalaman emosional dan idealismemu bikin kamu jadi sosok yang penuh empati dan "
              "kreatif, sering menghasilkan ide atau karya yang menyentuh karena datang dari "
              "tempat yang tulus. Kesetiaanmu pada nilai pribadi juga bikin kamu sulit "
              "dipengaruhi tekanan sosial untuk jadi sesuatu yang bukan dirimu. Tapi "
              "sensitivitasmu yang tinggi kadang bikin kritik kecil terasa sangat berat, dan "
              "kamu butuh waktu lama untuk pulih dari kekecewaan. Kamu juga cenderung terlalu "
              "banyak berangan-angan tentang bagaimana sesuatu seharusnya, sampai kesulitan "
              "bergerak ke langkah nyata untuk mewujudkannya. Kecenderungan untuk menghindari "
              "konflik demi menjaga kedamaian batin kadang bikin masalah yang sebenarnya "
              "penting jadi tidak terselesaikan.",
        "quote": "Dunia batin yang kaya akan lebih bermakna kalau sesekali kamu beranikan diri "
                 "membawanya keluar, bukan hanya disimpan sendiri.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba ambil satu langkah kecil dan konkret untuk mewujudkan satu ide atau "
              "cita-cita yang selama ini cuma ada di kepalamu, sekecil apa pun itu. Latih diri "
              "untuk menerima kritik sebagai masukan, bukan serangan pribadi, meski itu butuh "
              "waktu dan latihan. Beranikan diri menyampaikan ketidaksetujuan secara langsung "
              "saat sesuatu benar-benar mengganggu nilaimu, jangan cuma dipendam demi menjaga "
              "kedamaian sesaat. Beri dirimu batas waktu untuk berangan-angan, lalu paksa diri "
              "beralih ke tindakan nyata.",
        "domains": {
            "karir": "Kamu berkembang di bidang yang memberi ruang untuk kreativitas dan "
                     "makna personal, seperti penulisan, seni, konseling, atau pekerjaan sosial "
                     "yang sejalan dengan nilai-nilaimu. Kamu paling termotivasi kalau merasa "
                     "pekerjaanmu berkontribusi pada sesuatu yang lebih besar. Tapi kamu bisa "
                     "kesulitan di lingkungan kerja yang sangat kompetitif, penuh kritik keras, "
                     "atau terlalu birokratis tanpa ruang kreatif. Kamu juga cenderung menunda "
                     "pekerjaan yang terasa hampa secara personal, meski sebenarnya penting. "
                     "*PR: pecah satu proyek besar jadi langkah-langkah kecil yang lebih terasa "
                     "bisa dikerjakan, biar tidak terhenti karena kewalahan.*",
            "asmara": "Kamu pasangan yang tulus, penuh perhatian, dan mencari koneksi yang "
                      "benar-benar mendalam, bukan sekadar hubungan di permukaan. Kamu sangat "
                      "setia pada orang yang kamu percaya dan berusaha memahami mereka secara "
                      "utuh. Tapi kamu bisa terlalu mengidealkan hubungan, sehingga kecewa saat "
                      "kenyataan tidak seromantis bayanganmu. Kamu juga cenderung menghindari "
                      "konflik, memilih diam saat sebenarnya ada yang mengganjal. *PR: sampaikan "
                      "kekecewaan kecil ke pasangan segera setelah muncul, jangan biarkan "
                      "menumpuk jadi jarak emosional.*",
            "keuangan": "Kamu cenderung kurang tertarik memikirkan uang secara detail, lebih "
                        "fokus pada hal-hal yang terasa bermakna daripada angka-angka di "
                        "rekening. Kamu juga bisa impulsif membeli sesuatu yang terasa selaras "
                        "dengan nilai atau minatmu, meski belum tentu dalam anggaran yang "
                        "realistis. *PR: buat anggaran sederhana yang tetap kasih ruang untuk "
                        "hal-hal yang bermakna buatmu, biar keuanganmu tetap sehat tanpa "
                        "mengorbankan apa yang kamu suka.*",
            "kesehatan": "Kamu rentan larut dalam perasaan sendiri sampai lupa mengurus "
                         "kebutuhan fisik, seperti makan teratur atau tidur cukup, terutama "
                         "saat sedang banyak pikiran. Kamu juga cenderung menyimpan emosi berat "
                         "sendirian, jarang mencari bantuan meski sebenarnya butuh. *PR: cari "
                         "satu cara ekspresi yang bisa dilakukan rutin, seperti menulis jurnal "
                         "atau bicara ke teman dekat, supaya emosi tidak menumpuk terlalu "
                         "lama.*",
        },
    },
    "INTP": {
        "tagline": "🧩 Sang Penjelajah Ide",
        "chip": "MBTI",
        "title": "INTP — Sang Penjelajah Ide yang Rasa Ingin Tahunya Tak Pernah Padam",
        "p1_label": "Siapa Kamu",
        "p1": "Kamu adalah tipe yang hidup untuk memahami cara kerja sesuatu, entah itu sistem, "
              "ide, atau teori yang rumit sekalipun. Rasa ingin tahumu tidak pernah benar-benar "
              "berhenti, kamu bisa menghabiskan waktu berjam-jam mendalami satu topik yang "
              "menarik perhatianmu, sekadar untuk memuaskan rasa penasaran, bukan karena ada "
              "yang menyuruh. Sejak kecil, kamu mungkin sudah dikenal sebagai anak yang banyak "
              "bertanya \"kenapa\", sering membuat orang dewasa di sekitarmu kewalahan menjawab. "
              "Kamu lebih tertarik pada ide dan konsep dibanding urusan sosial yang terasa "
              "basa-basi, dan kamu jarang mengikuti sesuatu hanya karena itu sedang populer. "
              "Kamu berpikir mandiri dan skeptis terhadap klaim yang belum terbukti logikanya, "
              "kamu ingin memahami sendiri sebelum menerima begitu saja. Dalam pergaulan, kamu "
              "cenderung pendiam sampai topik yang kamu sukai muncul, lalu tiba-tiba kamu bisa "
              "bicara panjang lebar dengan antusias. Kamu menghargai kebebasan berpikir dan "
              "tidak suka dipaksa mengikuti aturan yang menurutmu tidak masuk akal. Orang-orang "
              "sering datang padamu untuk memecahkan masalah rumit, karena kamu punya cara "
              "berpikir yang tidak biasa dan bisa melihat sudut pandang yang orang lain lewatkan.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kemampuan analisismu yang tajam dan rasa ingin tahu yang besar bikin kamu jadi "
              "sosok yang bisa memecahkan masalah rumit dengan cara yang orisinal. Kamu juga "
              "objektif dan jarang terbawa emosi saat menilai sesuatu, sehingga pendapatmu "
              "sering dipercaya karena dianggap netral. Tapi kecenderunganmu terlalu asyik "
              "mendalami ide sampai lupa menyelesaikan hal-hal praktis sehari-hari kadang bikin "
              "banyak urusan tertunda. Kamu juga bisa terlihat cuek atau jauh secara emosional, "
              "padahal kamu sebenarnya peduli, hanya saja kamu lebih nyaman mengekspresikannya "
              "lewat diskusi ide daripada kata-kata hangat. Kebiasaan mengkritisi segala sesuatu "
              "secara logis kadang bikin orang lain merasa idenya terus-menerus dibantah, meski "
              "niatmu sebenarnya cuma ingin memahami lebih dalam.",
        "quote": "Ide-ide besar akan lebih berarti kalau sesekali kamu izinkan dirinya keluar "
                 "dari kepala dan benar-benar diwujudkan.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba pilih satu ide yang sudah lama kamu pikirkan, lalu ambil satu langkah kecil "
              "nyata untuk mewujudkannya, meski belum sempurna. Latih diri untuk menyelesaikan "
              "urusan praktis yang membosankan sebelum berpindah ke topik baru yang lebih "
              "menarik. Sesekali, tunjukkan apresiasi secara verbal ke orang-orang di "
              "sekitarmu, jangan cuma disimpan dalam pikiran. Ingat bahwa tidak semua diskusi "
              "perlu berakhir dengan siapa yang benar, kadang cukup untuk saling memahami sudut "
              "pandang.",
        "domains": {
            "karir": "Kamu bersinar di bidang yang butuh analisis mendalam dan pemecahan "
                     "masalah kompleks, seperti riset, teknologi, sains, atau bidang akademik "
                     "yang memberi ruang eksplorasi ide bebas. Kamu paling produktif kalau "
                     "diberi otonomi untuk bekerja dengan caramu sendiri tanpa terlalu banyak "
                     "diawasi. Tapi kamu bisa kesulitan dengan pekerjaan yang penuh rutinitas "
                     "administratif atau tenggat ketat yang menuntut keputusan cepat tanpa "
                     "cukup waktu berpikir. Kamu juga kadang menunda pekerjaan yang terasa "
                     "membosankan sampai mepet deadline. *PR: pecah tugas administratif jadi "
                     "target kecil harian, biar tidak menumpuk sampai mendekati tenggat.*",
            "asmara": "Kamu pasangan yang setia dan menghargai kedalaman intelektual dalam "
                      "hubungan, senang berdiskusi panjang tentang topik yang menarik minat "
                      "kalian berdua. Kamu juga cenderung menghargai ruang pribadi pasangan "
                      "sebanyak kamu menghargai ruangmu sendiri. Tapi kamu kadang kesulitan "
                      "mengekspresikan kasih sayang secara emosional, lebih nyaman menunjukkan "
                      "perhatian lewat diskusi atau bantuan praktis. *PR: sesekali ungkapkan "
                      "perasaanmu secara langsung dan sederhana, tanpa perlu dianalisis "
                      "dulu.*",
            "keuangan": "Kamu cenderung rasional soal uang, jarang tergoda tren atau tekanan "
                        "sosial untuk membeli sesuatu, tapi kadang kurang tertarik memikirkan "
                        "perencanaan keuangan detail karena terasa membosankan dibanding topik "
                        "lain yang lebih menarik minatmu. *PR: sisihkan waktu khusus tiap bulan "
                        "untuk cek kondisi keuangan, anggap ini sebagai \"riset\" kecil yang "
                        "perlu dilakukan rutin.*",
            "kesehatan": "Kamu rentan lupa mengurus kebutuhan fisik dasar, seperti makan atau "
                         "tidur teratur, saat sedang asyik mendalami sesuatu yang menarik "
                         "perhatianmu. Kamu juga cenderung memendam beban emosional, lebih "
                         "memilih menganalisisnya sendiri daripada membicarakannya dengan orang "
                         "lain. *PR: pasang pengingat sederhana untuk jeda makan dan istirahat "
                         "saat sedang fokus dalam sesuatu, biar tidak terlewat begitu saja.*",
        },
    },
    "ESTP": {
        "tagline": "⚡ Sang Petualang Siap Aksi",
        "chip": "MBTI",
        "title": "ESTP — Sang Petualang yang Selalu Siap Bergerak",
        "p1_label": "Siapa Kamu",
        "p1": "Kamu adalah tipe yang hidup di momen sekarang, penuh energi, dan selalu siap "
              "mengambil tindakan tanpa banyak berpikir panjang. Kamu belajar paling baik lewat "
              "pengalaman langsung, bukan lewat teori yang panjang lebar, dan kamu jarang takut "
              "mencoba hal baru meski risikonya belum sepenuhnya jelas. Sejak kecil, kamu "
              "mungkin sudah jadi anak yang aktif secara fisik, suka tantangan, dan cepat bosan "
              "kalau harus duduk diam terlalu lama. Kamu punya kemampuan membaca situasi dengan "
              "cepat dan bertindak sesuai kebutuhan saat itu juga, membuat kamu jadi sosok yang "
              "tenang saat orang lain panik menghadapi keadaan darurat. Dalam pergaulan, kamu "
              "mudah akrab dengan orang baru, punya energi sosial yang tinggi, dan sering jadi "
              "pusat perhatian di kerumunan karena caramu yang ceria dan spontan. Kamu tidak "
              "terlalu suka aturan kaku yang membatasi gerakmu, kamu lebih percaya pada "
              "insting dan kemampuan beradaptasi langsung di lapangan. Orang-orang di "
              "sekitarmu sering terinspirasi oleh keberanianmu untuk mencoba hal-hal yang "
              "mereka sendiri masih ragu melakukannya.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Keberanian dan kesigapanmu bertindak bikin kamu jadi sosok yang bisa diandalkan "
              "saat situasi butuh keputusan cepat. Kamu juga punya energi sosial yang bikin "
              "suasana jadi lebih hidup ke mana pun kamu pergi. Tapi kecenderunganmu bertindak "
              "dulu baru berpikir belakangan kadang bikin kamu mengambil risiko yang sebenarnya "
              "bisa dihindari kalau dipertimbangkan lebih dulu. Kamu juga bisa cepat bosan "
              "dengan komitmen jangka panjang yang terasa monoton, membuat orang lain ragu "
              "mengandalkanmu untuk hal-hal yang butuh konsistensi lama. Sikap spontanmu kadang "
              "dianggap kurang peka terhadap perasaan orang lain, padahal kamu sebenarnya "
              "cuma fokus pada momen yang sedang berlangsung.",
        "quote": "Keberanian mengambil tindakan akan jauh lebih kuat kalau diimbangi dengan "
                 "sedikit jeda untuk memikirkan dampaknya.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba beri jeda sejenak sebelum mengambil keputusan besar, sekadar untuk "
              "memikirkan kemungkinan konsekuensinya. Latih diri untuk menyelesaikan satu "
              "komitmen sampai tuntas meski sudah tidak seseru di awal, sebagai latihan "
              "konsistensi. Perhatikan reaksi orang di sekitarmu setelah kamu bertindak "
              "spontan, dan tanyakan langsung kalau ada yang merasa terdampak. Sesekali, coba "
              "aktivitas yang butuh kesabaran dan perencanaan panjang, meski itu terasa "
              "membosankan di awal.",
        "domains": {
            "karir": "Kamu bersinar di pekerjaan yang dinamis dan penuh aksi, seperti sales, "
                     "olahraga, event, penanganan darurat, atau bidang yang butuh keputusan "
                     "cepat di lapangan. Kamu paling produktif kalau diberi kebebasan bergerak, "
                     "bukan terikat meja dan rutinitas kaku. Tapi kamu bisa kesulitan dengan "
                     "pekerjaan yang butuh perencanaan detail jangka panjang atau administrasi "
                     "berulang. Kamu juga kadang terburu-buru mengambil keputusan tanpa cukup "
                     "data. *PR: sebelum ambil keputusan besar di kerjaan, coba cek dulu dengan "
                     "satu rekan yang lebih teliti soal detail.*",
            "asmara": "Kamu pasangan yang seru dan penuh energi, pandai membawa kesenangan dan "
                      "petualangan baru ke dalam hubungan. Kamu juga jujur dan langsung soal "
                      "perasaan, tidak suka main tebak-tebakan. Tapi kamu bisa kesulitan "
                      "berkomitmen jangka panjang kalau hubungan mulai terasa monoton, dan "
                      "kadang kurang peka terhadap kebutuhan emosional pasangan yang lebih "
                      "suka ketenangan. *PR: sesekali ajak pasangan bicara pelan tentang "
                      "perasaan, bukan cuma lewat aktivitas seru bareng.*",
            "keuangan": "Kamu cenderung impulsif soal uang, suka membeli sesuatu di saat "
                        "itu juga tanpa banyak pertimbangan, terutama untuk pengalaman seru "
                        "seperti liburan atau hobi baru. Kebiasaan menabung untuk jangka "
                        "panjang sering terasa kurang menarik dibanding menikmati momen "
                        "sekarang. *PR: sisihkan otomatis sebagian penghasilan ke tabungan "
                        "sebelum sempat dibelanjakan, biar tidak habis duluan.*",
            "kesehatan": "Kamu aktif secara fisik dan biasanya menyukai olahraga atau "
                         "aktivitas yang menantang adrenalin, tapi kadang kurang hati-hati "
                         "soal keselamatan karena terlalu percaya diri. Kamu juga jarang "
                         "memperhatikan tanda kelelahan karena terus mengejar aktivitas baru. "
                         "*PR: pakai pengaman standar (helm, pemanasan, dll) setiap kali "
                         "olahraga ekstrem, sekecil apa pun rasanya berlebihan.*",
        },
    },
    "ESFP": {
        "tagline": "🎉 Sang Penghibur yang Menghidupkan Suasana",
        "chip": "MBTI",
        "title": "ESFP — Sang Penghibur yang Menghidupkan Suasana",
        "p1_label": "Siapa Kamu",
        "p1": "Kamu adalah tipe yang bikin ruangan terasa lebih hidup begitu kamu masuk. Energi "
              "dan kehangatanmu menular ke orang-orang di sekitar, dan kamu punya bakat alami "
              "untuk membuat suasana yang tadinya kaku jadi cair dan menyenangkan. Sejak kecil, "
              "kamu mungkin sudah jadi anak yang suka tampil, entah menyanyi, menari, atau "
              "sekadar bercerita dengan ekspresif di depan keluarga. Kamu hidup di momen "
              "sekarang, lebih suka menikmati apa yang ada di depan mata daripada terlalu "
              "khawatir soal masa depan yang belum tentu terjadi. Kamu peka terhadap perasaan "
              "orang di sekitarmu, cepat menangkap kalau ada yang sedang sedih dan biasanya "
              "jadi orang pertama yang berusaha menghiburnya. Dalam pergaulan, kamu mudah akrab "
              "dengan siapa saja, tidak pilih-pilih teman, dan senang jadi bagian dari "
              "kebersamaan. Kamu menghargai kebebasan berekspresi dan tidak suka terlalu "
              "banyak diatur, kamu lebih nyaman menjalani hidup secara spontan dan fleksibel. "
              "Orang-orang di sekitarmu sering merasa lebih bahagia setelah menghabiskan waktu "
              "bersamamu, karena kehadiranmu terasa ringan dan menyenangkan.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kehangatan dan energi positifmu bikin kamu jadi sosok yang dicari orang saat "
              "butuh dihibur atau sekadar butuh suasana yang lebih ringan. Kepekaanmu terhadap "
              "perasaan orang lain juga bikin kamu jadi teman yang suportif dan penuh empati. "
              "Tapi kecenderunganmu untuk fokus pada kesenangan saat ini kadang bikin kamu "
              "kurang memikirkan konsekuensi jangka panjang dari keputusan yang kamu ambil. "
              "Kamu juga bisa terlalu menghindari konflik demi menjaga suasana tetap "
              "menyenangkan, sehingga masalah yang sebenarnya penting jadi tertunda "
              "penyelesaiannya. Sensitivitasmu terhadap kritik kadang bikin kamu terlalu "
              "terpukul saat menerima masukan, meski itu disampaikan dengan niat baik.",
        "quote": "Keceriaan yang kamu bawa akan makin berarti kalau sesekali kamu izinkan "
                 "dirimu memikirkan langkah selanjutnya, bukan cuma momen sekarang.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba luangkan waktu sejenak setiap minggu untuk memikirkan rencana jangka "
              "menengah, sekecil apa pun itu, supaya keputusan spontanmu tetap punya arah. "
              "Latih diri untuk menghadapi konflik kecil secara langsung, alih-alih "
              "menghindarinya demi menjaga suasana tetap nyaman. Terima kritik sebagai bahan "
              "untuk berkembang, bukan sebagai penilaian terhadap dirimu secara keseluruhan. "
              "Sesekali, beri dirimu waktu sendiri untuk merenung, bukan selalu dikelilingi "
              "keramaian.",
        "domains": {
            "karir": "Kamu bersinar di bidang yang butuh interaksi langsung dan energi "
                     "positif, seperti entertainment, event, penjualan, hospitality, atau "
                     "pekerjaan kreatif yang melibatkan banyak orang. Kamu paling termotivasi "
                     "kalau pekerjaanmu memberi ruang untuk tampil dan berinteraksi. Tapi kamu "
                     "bisa kesulitan dengan pekerjaan yang sangat administratif dan repetitif "
                     "tanpa interaksi sosial. Kamu juga kadang menunda tugas yang terasa "
                     "membosankan demi mengejar hal yang lebih menyenangkan. *PR: selesaikan "
                     "satu tugas membosankan di awal hari, biar sisa harimu bisa dinikmati "
                     "tanpa beban.*",
            "asmara": "Kamu pasangan yang hangat, ekspresif, dan pandai menciptakan momen "
                      "menyenangkan bersama orang yang kamu sayangi. Kamu juga jujur soal "
                      "perasaan dan tidak suka menyimpan sesuatu terlalu lama. Tapi kamu bisa "
                      "menghindari pembicaraan serius soal masa depan hubungan karena terasa "
                      "kurang menyenangkan dibanding menikmati momen sekarang. *PR: sesekali, "
                      "ajak pasangan bicara serius soal rencana ke depan, meski terasa kurang "
                      "seru dibanding kencan biasa.*",
            "keuangan": "Kamu cenderung suka membelanjakan uang untuk pengalaman dan "
                        "kesenangan bersama orang lain, seperti nongkrong, liburan, atau "
                        "hadiah, dan kurang suka repot dengan perencanaan keuangan detail. "
                        "*PR: tetapkan batas bulanan untuk pengeluaran sosial, supaya tetap "
                        "bisa menikmati momen tanpa mengorbankan tabungan.*",
            "kesehatan": "Kamu cenderung mengabaikan tanda kelelahan fisik maupun emosional "
                         "karena terus mengejar kesenangan dan interaksi sosial, sampai "
                         "akhirnya kelelahan menumpuk tanpa disadari. Kamu juga rentan "
                         "menyerap suasana hati orang di sekitarmu. *PR: jadwalkan satu hari "
                         "penuh tanpa agenda sosial tiap minggu, khusus untuk memulihkan "
                         "energi.*",
        },
    },
    "ENFP": {
        "tagline": "✨ Sang Juru Kampanye yang Penuh Semangat",
        "chip": "MBTI",
        "title": "ENFP — Sang Juru Kampanye yang Penuh Semangat",
        "p1_label": "Siapa Kamu",
        "p1": "Kamu adalah tipe yang penuh semangat dan selalu punya ide baru yang membuat "
              "orang di sekitarmu ikut tertular antusiasmenya. Kamu melihat kemungkinan di "
              "mana-mana, sering menghubungkan hal-hal yang orang lain anggap tidak berkaitan "
              "jadi satu ide segar yang menarik. Sejak kecil, kamu mungkin sudah dikenal "
              "sebagai anak yang penuh rasa ingin tahu, senang mencoba banyak hal baru, dan "
              "sulit diam kalau ada ide menarik yang muncul di kepala. Kamu punya kepekaan "
              "tinggi terhadap perasaan orang lain, sering jadi orang yang paling dulu "
              "menyadari kalau ada yang sedang sedih meski mereka belum bicara. Dalam "
              "pergaulan, kamu hangat dan mudah akrab, energi sosialmu terasa menular ke "
              "siapa pun yang berada di dekatmu. Kamu menghargai kebebasan untuk mengejar "
              "banyak minat sekaligus, tidak suka dikotakkan hanya jadi satu hal saja. "
              "Orang-orang di sekitarmu sering datang padamu untuk mencari semangat baru saat "
              "mereka sedang jenuh, karena kamu punya cara melihat sisi menarik dari hampir "
              "semua hal. Kamu juga punya idealisme yang kuat tentang dunia yang lebih baik, "
              "dan kamu ingin jadi bagian dari perubahan itu.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Antusiasme dan kreativitasmu bikin kamu jadi sosok yang bisa menginspirasi orang "
              "lain untuk berani mencoba hal baru. Empati dan kehangatanmu juga bikin orang "
              "merasa benar-benar didengar saat bicara denganmu. Tapi banyaknya ide dan minat "
              "yang kamu kejar sekaligus kadang bikin kamu kesulitan menyelesaikan satu hal "
              "sampai tuntas sebelum pindah ke ide berikutnya yang lebih menarik. Kamu juga "
              "rentan kelelahan emosional karena terlalu banyak menyerap perasaan orang-orang "
              "di sekitarmu. Kecenderungan untuk menghindari rutinitas dan detail teknis "
              "kadang bikin proyek besar yang sebenarnya punya potensi jadi terbengkalai di "
              "tengah jalan.",
        "quote": "Semangat yang kamu bawa akan jauh lebih berdampak kalau kamu setia "
                 "menuntaskannya sampai akhir.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba pilih satu ide yang paling kamu yakini punya potensi, lalu fokus "
              "menyelesaikannya sampai tuntas sebelum mengejar ide baru yang muncul di tengah "
              "jalan. Tuliskan ide-ide lain yang muncul di catatan terpisah supaya tidak "
              "hilang, tapi tidak mengganggu fokusmu saat ini. Beri dirimu waktu istirahat "
              "yang cukup untuk memulihkan energi emosional, terutama setelah banyak "
              "berinteraksi dengan orang lain. Latih diri untuk menikmati proses yang repetitif "
              "sesekali, bukan cuma bagian yang seru di awal.",
        "domains": {
            "karir": "Kamu bersinar di pekerjaan kreatif yang butuh ide segar dan interaksi "
                     "dengan banyak orang, seperti marketing, konten kreatif, konsultasi, atau "
                     "kewirausahaan. Kamu paling produktif di fase awal proyek yang penuh "
                     "eksplorasi ide. Tapi kamu bisa kehilangan minat begitu proyek masuk fase "
                     "rutin dan detail, membuat rekan kerja was-was menyerahkan tugas jangka "
                     "panjang padamu. *PR: cari partner kerja yang kuat di eksekusi detail, "
                     "biar ide-idemu bisa benar-benar terwujud sampai selesai.*",
            "asmara": "Kamu pasangan yang hangat, ekspresif, dan pandai membawa kegembiraan "
                      "dalam hubungan, selalu punya ide baru untuk dilakukan bersama. Kamu "
                      "juga tulus dan penuh empati terhadap perasaan pasangan. Tapi kamu bisa "
                      "gelisah kalau hubungan terasa monoton dan butuh variasi terus-menerus "
                      "supaya tetap merasa hidup. *PR: sebelum menyimpulkan hubungan "
                      "membosankan, coba dulu ajak pasangan menciptakan hal baru bareng.*",
            "keuangan": "Kamu cenderung impulsif dan kurang suka terikat perencanaan "
                        "keuangan detail, sering tergoda membeli sesuatu karena terasa menarik "
                        "saat itu juga. Semangatmu mencoba banyak hal baru juga bisa bikin "
                        "pengeluaran untuk hobi menumpuk tanpa disadari. *PR: pakai sistem "
                        "tabungan otomatis yang jalan tanpa perlu kamu pikirkan tiap bulan, "
                        "biar tetap konsisten meski fokusmu berpindah-pindah.*",
            "kesehatan": "Kamu rentan kelelahan karena energi sosial dan emosionalmu terkuras "
                         "menyerap perasaan orang lain, apalagi kalau kamu juga sedang "
                         "mengejar banyak proyek sekaligus. Pola tidur dan makan juga bisa "
                         "berantakan saat kamu sedang bersemangat dengan sesuatu. *PR: "
                         "jadwalkan waktu \"me time\" rutin tiap minggu untuk mengisi ulang "
                         "energi, bukan cuma saat sudah benar-benar kelelahan.*",
        },
    },
    "ENTP": {
        "tagline": "💡 Sang Pendebat Pengulik Kemungkinan",
        "chip": "MBTI",
        "title": "ENTP — Sang Pendebat yang Suka Mengulik Kemungkinan",
        "p1_label": "Siapa Kamu",
        "p1": "Kamu adalah tipe yang hidup untuk mengulik ide, mempertanyakan asumsi, dan "
              "melihat kemungkinan yang orang lain belum kepikiran. Kamu senang berdebat, bukan "
              "untuk mencari musuh, tapi karena buatmu diskusi yang tajam adalah cara paling "
              "seru untuk menguji ide sampai benar-benar kuat. Sejak kecil, kamu mungkin sudah "
              "jadi anak yang suka bertanya \"tapi kenapa harus begitu?\" dan tidak puas dengan "
              "jawaban yang terasa asal. Kamu punya energi mental yang cepat, bisa "
              "menghubungkan ide dari berbagai bidang berbeda dan menemukan pola yang orang "
              "lain lewatkan. Dalam pergaulan, kamu cerdas dan menghibur, sering jadi orang "
              "yang bikin obrolan biasa jadi diskusi yang jauh lebih menarik dari perkiraan "
              "semua orang. Kamu tidak suka rutinitas yang monoton, kamu lebih hidup saat "
              "menghadapi tantangan intelektual baru yang belum pernah kamu coba pecahkan. "
              "Kamu juga cenderung skeptis terhadap aturan yang dianggap \"sudah begitu dari "
              "dulu\" tanpa alasan jelas, dan tidak segan mempertanyakannya secara terbuka. "
              "Orang-orang di sekitarmu sering merasa terpicu berpikir lebih dalam setelah "
              "ngobrol denganmu, meski kadang mereka juga butuh napas sejenak dari intensitas "
              "diskusimu.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kecerdasan dan kelincahan berpikirmu bikin kamu jadi sosok yang bisa melihat "
              "peluang dan solusi kreatif yang orang lain lewatkan. Rasa percaya dirimu untuk "
              "mempertanyakan status quo juga jadi kekuatan besar saat sistem lama memang perlu "
              "diperbarui. Tapi kesenanganmu berdebat kadang bikin orang lain merasa "
              "diserang, padahal niatmu sebenarnya cuma ingin menguji ide, bukan menjatuhkan "
              "orangnya. Kamu juga cenderung kehilangan minat begitu ide sudah cukup "
              "dieksplorasi secara konsep, tapi belum sampai ke eksekusi nyata. Kebiasaan "
              "melompat dari satu ide ke ide lain yang lebih menarik kadang bikin proyek "
              "sebelumnya terbengkalai sebelum benar-benar selesai.",
        "quote": "Ide-ide brilian akan jauh lebih bernilai kalau kamu juga setia mengawalnya "
                 "sampai benar-benar terwujud.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba pilih satu ide yang paling menjanjikan, lalu paksa dirimu untuk "
              "mengeksekusinya sampai selesai sebelum pindah ke ide baru yang lebih menggoda. "
              "Sebelum berdebat, ingatkan diri untuk mengecek dulu apakah lawan bicaramu "
              "nyaman dengan gaya diskusi yang intens, atau butuh pendekatan yang lebih "
              "lembut. Latih diri untuk menerima bahwa tidak semua aturan perlu "
              "dipertanyakan saat itu juga, kadang cukup dicatat dulu untuk didiskusikan di "
              "waktu yang lebih tepat. Beri ruang untuk mendengarkan tanpa langsung mencari "
              "celah untuk dibantah.",
        "domains": {
            "karir": "Kamu bersinar di bidang yang butuh inovasi dan pemecahan masalah "
                     "kreatif, seperti kewirausahaan, konsultasi, teknologi, atau riset yang "
                     "penuh tantangan intelektual. Kamu paling termotivasi di fase awal proyek "
                     "yang penuh brainstorming. Tapi kamu bisa cepat bosan begitu proyek masuk "
                     "fase eksekusi detail dan repetitif, membuat rekan kerja kewalahan "
                     "menyelesaikan apa yang kamu mulai. *PR: cari partner kerja yang kuat di "
                     "eksekusi, biar ide briliianmu benar-benar terwujud jadi hasil nyata.*",
            "asmara": "Kamu pasangan yang menyenangkan dan penuh stimulasi intelektual, "
                      "senang berdiskusi dan bercanda dengan orang yang kamu sayangi. Kamu "
                      "juga jujur dan langsung soal perasaan, tidak suka berbasa-basi. Tapi "
                      "kamu bisa kesulitan menghadapi konflik emosional yang butuh kelembutan, "
                      "karena kamu cenderung mendekatinya secara logis padahal pasangan butuh "
                      "empati. *PR: saat pasangan sedang emosional, tahan dulu keinginan "
                      "berdebat, cukup dengarkan dulu sampai mereka merasa dipahami.*",
            "keuangan": "Kamu cenderung suka mengeksplorasi peluang finansial baru dan "
                        "berani ambil risiko yang menurutmu masuk akal, tapi kadang kurang "
                        "sabar mengikuti rencana keuangan jangka panjang yang terasa "
                        "membosankan. *PR: sisihkan sebagian dana di instrumen yang stabil "
                        "sebelum mengejar peluang baru yang lebih berisiko, biar tetap ada "
                        "jaring pengaman.*",
            "kesehatan": "Kamu cenderung terlalu asyik dengan aktivitas mental sampai lupa "
                         "istirahat fisik, dan pikiranmu yang terus aktif kadang bikin susah "
                         "benar-benar rileks bahkan saat sedang santai. *PR: coba jadwalkan "
                         "waktu tanpa gadget dan diskusi, khusus untuk benar-benar "
                         "mengistirahatkan pikiran.*",
        },
    },
    "ESTJ": {
        "tagline": "📋 Sang Pengatur yang Tegas",
        "chip": "MBTI",
        "title": "ESTJ — Sang Pengatur yang Tegas dan Terstruktur",
        "p1_label": "Siapa Kamu",
        "p1": "Kamu adalah tipe yang punya kemampuan alami untuk mengorganisasi sesuatu jadi "
              "rapi dan berjalan efisien. Kamu percaya pada aturan, struktur, dan tanggung "
              "jawab yang jelas, karena buatmu itu adalah cara paling masuk akal supaya "
              "sesuatu bisa berhasil. Sejak kecil, kamu mungkin sudah jadi anak yang suka "
              "memimpin permainan atau kegiatan kelompok, secara natural mengambil peran "
              "mengatur tanpa perlu diminta. Kamu tegas dalam menyampaikan pendapat, orang "
              "tahu persis apa yang kamu pikirkan karena kamu jarang berbasa-basi soal hal "
              "yang penting. Kamu menghargai kerja keras dan hasil nyata, dan kamu tidak "
              "terlalu sabar dengan orang yang banyak bicara tapi minim tindakan. Dalam "
              "kelompok, kamu sering jadi orang yang secara otomatis dipercaya memegang "
              "tanggung jawab besar, karena orang tahu kalau kamu yang pegang, semuanya akan "
              "berjalan sesuai rencana. Kamu setia pada tradisi dan sistem yang sudah terbukti "
              "berhasil, dan kamu punya standar tinggi baik untuk diri sendiri maupun "
              "orang-orang di sekitarmu. Kepemimpinanmu terasa alami, bukan dipaksakan, karena "
              "orang lain secara natural merasa lebih tenang kalau kamu yang mengambil "
              "kendali.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Ketegasan dan kemampuan organisasimu bikin kamu jadi sosok yang bisa diandalkan "
              "untuk memimpin proyek besar sampai selesai sesuai rencana. Kejujuranmu yang "
              "langsung juga bikin orang tahu persis di mana posisinya kalau berurusan "
              "denganmu. Tapi standar tinggi yang kamu pegang kadang diterapkan terlalu ketat "
              "ke orang lain, membuat mereka merasa tertekan meski niatmu sebenarnya baik. "
              "Kamu juga bisa kurang sabar dengan cara berpikir yang berbeda dari caramu "
              "sendiri, sehingga kesulitan menerima pendekatan alternatif yang sebenarnya "
              "sama validnya. Kecenderungan untuk fokus pada hasil kadang bikin kamu kurang "
              "memperhatikan perasaan orang-orang yang terlibat dalam proses mencapainya.",
        "quote": "Struktur yang kamu bangun akan terasa lebih kuat kalau ada ruang untuk "
                 "fleksibilitas dan pendapat yang berbeda dari caramu sendiri.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba dengarkan satu pendapat yang berbeda dari caramu bekerja tanpa langsung "
              "mengoreksinya, biarkan dulu selesai sebelum kamu menanggapi. Latih diri untuk "
              "menanyakan perasaan orang-orang di timmu, bukan cuma progres pekerjaan mereka. "
              "Sesekali, izinkan rencana berjalan sedikit berbeda dari yang kamu susun, dan "
              "lihat apakah hasilnya tetap baik meski caranya berbeda. Sampaikan apresiasi "
              "secara terbuka saat orang lain melakukan sesuatu dengan baik, jangan cuma "
              "diam saja.",
        "domains": {
            "karir": "Kamu unggul di posisi kepemimpinan dan manajemen yang butuh struktur "
                     "jelas, seperti operasional, manajemen proyek, atau posisi eksekutif yang "
                     "menuntut ketegasan dalam pengambilan keputusan. Atasan dan bawahan sama-"
                     "sama tahu kalau kamu yang pegang kendali, semuanya berjalan terorganisir. "
                     "Tapi kamu bisa terlihat terlalu kaku di lingkungan yang butuh fleksibilitas "
                     "tinggi atau kreativitas bebas. Kamu juga kadang kurang sabar dengan "
                     "proses yang belum menunjukkan hasil cepat. *PR: beri ruang bagi tim untuk "
                     "mencoba cara mereka sendiri dulu, sebelum kamu turun tangan "
                     "mengoreksi.*",
            "asmara": "Kamu pasangan yang bertanggung jawab dan bisa diandalkan, serius soal "
                      "komitmen dan selalu berusaha memastikan hubungan berjalan stabil. Kamu "
                      "juga jujur dan langsung soal apa yang kamu inginkan dari hubungan. Tapi "
                      "kamu bisa terlalu fokus pada aspek praktis hubungan sampai kurang "
                      "memberi ruang untuk momen emosional yang lebih lembut. *PR: sesekali, "
                      "tanyakan perasaan pasangan tanpa langsung menawarkan solusi, cukup "
                      "dengarkan dulu.*",
            "keuangan": "Kamu punya perencanaan keuangan yang rapi dan disiplin, jarang "
                        "tergoda belanja impulsif karena kamu selalu berpikir soal manfaat "
                        "jangka panjang. Tapi kamu bisa terlalu kaku soal anggaran sampai lupa "
                        "menikmati hasil kerja kerasmu sesekali. *PR: alokasikan satu pos kecil "
                        "khusus untuk kesenangan tanpa merasa bersalah menggunakannya.*",
            "kesehatan": "Kamu cenderung mendorong diri terus bekerja meski tubuh sudah "
                         "memberi sinyal lelah, karena tidak suka merasa tertinggal dari target "
                         "yang kamu tetapkan sendiri. Kamu juga jarang mengakui kalau sedang "
                         "stres, lebih memilih tetap tampil tegar di depan orang lain. *PR: "
                         "jadwalkan waktu istirahat sebagai bagian dari rencana kerjamu, bukan "
                         "sekadar kalau ada waktu sisa.*",
        },
    },
    "ESFJ": {
        "tagline": "🤝 Sang Penghubung yang Peduli",
        "chip": "MBTI",
        "title": "ESFJ — Sang Penghubung yang Peduli Sekitarnya",
        "p1_label": "Siapa Kamu",
        "p1": "Kamu adalah tipe yang selalu memperhatikan kebutuhan orang-orang di sekitarmu, "
              "sering jadi orang yang memastikan semua orang dalam kelompok merasa nyaman dan "
              "diperhatikan. Kamu punya kepekaan sosial yang tinggi, cepat menangkap perubahan "
              "suasana hati orang lain dan berusaha memperbaikinya kalau terasa kurang "
              "nyaman. Sejak kecil, kamu mungkin sudah jadi anak yang senang mengorganisir "
              "acara keluarga atau memastikan semua teman merasa dilibatkan dalam kegiatan "
              "bersama. Kamu menghargai tradisi, hubungan yang harmonis, dan struktur sosial "
              "yang jelas, karena itu bikin kamu merasa semua orang tahu perannya "
              "masing-masing. Dalam pertemanan, kamu jadi sosok yang selalu diandalkan untuk "
              "urusan praktis, mengatur acara, mengingatkan hal penting, atau sekadar "
              "memastikan semua orang baik-baik saja. Kamu bekerja keras untuk menjaga "
              "hubungan tetap harmonis, kadang sampai mengorbankan kebutuhanmu sendiri demi "
              "menghindari konflik. Orang-orang di sekitarmu merasa dihargai dan diperhatikan "
              "kalau berada di dekatmu, karena kamu tulus peduli pada kesejahteraan mereka. "
              "Kamu juga sangat setia pada komunitas atau kelompok yang sudah kamu anggap "
              "sebagai keluarga.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kepedulian dan kehangatanmu bikin kamu jadi sosok yang bisa menyatukan orang-"
              "orang dari latar belakang berbeda jadi satu kelompok yang harmonis. Kamu juga "
              "sangat bisa diandalkan untuk urusan praktis yang bikin acara atau kegiatan "
              "kelompok berjalan lancar. Tapi kebutuhanmu akan persetujuan sosial kadang bikin "
              "kamu kesulitan menghadapi konflik langsung, memilih mengalah meski sebenarnya "
              "punya pendapat berbeda. Kamu juga rentan terlalu memikirkan pendapat orang lain "
              "tentang dirimu, sampai kesulitan membuat keputusan yang murni untuk dirimu "
              "sendiri. Kecenderungan untuk terlalu banyak mengurus orang lain kadang bikin "
              "kamu kelelahan tanpa disadari karena lupa mengurus kebutuhanmu sendiri.",
        "quote": "Kehangatan yang kamu bagi ke orang lain akan lebih tahan lama kalau kamu "
                 "juga mengizinkan dirimu menerima kehangatan itu balik.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba sampaikan satu pendapat berbeda secara langsung saat kamu tidak setuju "
              "dengan sesuatu, meski itu terasa canggung di awal. Latih diri untuk membuat satu "
              "keputusan kecil murni berdasarkan apa yang kamu mau, bukan berdasarkan apa yang "
              "menurutmu akan disetujui orang lain. Beri dirimu izin untuk beristirahat tanpa "
              "merasa bersalah karena tidak sedang mengurus siapa-siapa. Perhatikan kalau kamu "
              "mulai kelelahan karena terlalu banyak memikirkan kebutuhan orang lain, dan ambil "
              "jeda sebelum benar-benar habis tenaga.",
        "domains": {
            "karir": "Kamu unggul di peran yang butuh koordinasi dan hubungan interpersonal "
                     "kuat, seperti HR, event, pendidikan, layanan pelanggan, atau posisi yang "
                     "menjaga hubungan tim tetap solid. Rekan kerja merasa nyaman "
                     "berkoordinasi denganmu karena kamu selalu memastikan semua orang "
                     "terlibat dan dihargai. Tapi kamu bisa kesulitan memberi kritik langsung "
                     "yang tegas, karena tidak enak membuat orang lain kecewa. Kamu juga "
                     "cenderung terlalu memikirkan pendapat atasan tentang dirimu sampai "
                     "kurang berani mengambil sikap sendiri. *PR: latih diri menyampaikan satu "
                     "kritik konstruktif secara langsung ke rekan kerja, bukan lewat orang "
                     "lain.*",
            "asmara": "Kamu pasangan yang penuh perhatian dan selalu berusaha membuat orang "
                      "yang kamu sayangi merasa dicintai lewat tindakan nyata sehari-hari. Kamu "
                      "juga setia dan menghargai stabilitas dalam hubungan. Tapi kamu bisa "
                      "terlalu mengalah demi menghindari konflik, sampai kebutuhanmu sendiri "
                      "sering terabaikan. *PR: sampaikan satu kebutuhanmu secara jelas ke "
                      "pasangan, jangan berharap mereka menebaknya sendiri.*",
            "keuangan": "Kamu cenderung murah hati dan senang membelanjakan uang untuk "
                        "keluarga atau orang-orang terdekat, kadang sampai lupa menyisihkan "
                        "untuk kebutuhanmu sendiri. Kamu juga suka membeli sesuatu untuk "
                        "menyenangkan orang lain meski anggaran sebenarnya terbatas. *PR: "
                        "tetapkan batas jelas untuk pengeluaran demi orang lain, supaya "
                        "kebutuhanmu sendiri tetap terjaga.*",
            "kesehatan": "Kamu rentan kelelahan karena terus-menerus memikirkan kebutuhan "
                         "orang lain sampai lupa mengurus dirimu sendiri, dan kamu cenderung "
                         "menahan diri untuk mengeluh meski sebenarnya sudah capek. *PR: "
                         "sisihkan waktu rutin tiap minggu khusus untuk dirimu sendiri, tanpa "
                         "diganggu urusan orang lain.*",
        },
    },
    "ENFJ": {
        "tagline": "🌟 Sang Penggerak yang Menginspirasi",
        "chip": "MBTI",
        "title": "ENFJ — Sang Penggerak yang Menginspirasi Orang Lain",
        "p1_label": "Siapa Kamu",
        "p1": "Kamu adalah tipe yang punya kemampuan alami untuk melihat potensi terbaik dalam "
              "diri orang lain, sering kali bahkan sebelum mereka sendiri menyadarinya. Kamu "
              "punya karisma yang membuat orang mau mengikuti visimu, bukan karena dipaksa, "
              "tapi karena mereka benar-benar percaya pada apa yang kamu perjuangkan. Sejak "
              "kecil, kamu mungkin sudah jadi anak yang secara natural jadi pemimpin kelompok, "
              "dipercaya teman-teman untuk menyatukan mereka dalam satu tujuan bersama. Kamu "
              "sangat peka terhadap emosi orang lain dan punya kemampuan komunikasi yang kuat "
              "untuk menyampaikan gagasan dengan cara yang menyentuh hati. Dalam pergaulan, "
              "kamu hangat dan penuh perhatian, orang merasa benar-benar didengar dan dihargai "
              "saat bicara denganmu. Kamu punya idealisme yang kuat tentang bagaimana dunia "
              "seharusnya berjalan, dan kamu bekerja aktif untuk mewujudkannya lewat "
              "pengaruhmu pada orang-orang di sekitar. Kamu sering jadi sosok yang dicari saat "
              "kelompok butuh arahan atau semangat baru, karena kamu punya kemampuan menyatukan "
              "orang-orang yang berbeda pendapat jadi satu tujuan yang sama. Kepedulianmu "
              "terhadap pertumbuhan orang lain kadang lebih besar daripada perhatianmu pada "
              "dirimu sendiri.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kemampuanmu menginspirasi dan menyatukan orang lain bikin kamu jadi sosok yang "
              "dicari saat kelompok butuh pemimpin yang bisa membawa perubahan nyata. Empati "
              "dan komunikasimu yang kuat juga bikin orang merasa dipahami secara mendalam. "
              "Tapi kecenderunganmu untuk selalu memprioritaskan kebutuhan orang lain kadang "
              "bikin kamu mengabaikan kebutuhanmu sendiri sampai kelelahan tanpa disadari. Kamu "
              "juga bisa terlalu berharap semua orang di sekitarmu berkembang sesuai visimu, "
              "padahal tidak semua orang siap atau mau berubah secepat yang kamu harapkan. "
              "Kepekaanmu terhadap penolakan atau kritik kadang membuatmu terlalu terpukul, "
              "meski di luar kamu tetap terlihat tenang.",
        "quote": "Cahaya yang kamu bagikan untuk menerangi orang lain akan lebih tahan lama "
                 "kalau kamu juga menyalakannya untuk dirimu sendiri.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba luangkan waktu untuk memikirkan kebutuhanmu sendiri, bukan cuma kebutuhan "
              "orang-orang yang kamu bantu. Latih diri untuk menerima bahwa tidak semua orang "
              "bisa atau mau berubah sesuai harapanmu, dan itu bukan berarti usahamu sia-sia. "
              "Sesekali, izinkan dirimu menerima bantuan dari orang lain, alih-alih selalu jadi "
              "pihak yang membantu. Ungkapkan kalau kamu sedang lelah secara jujur, jangan "
              "cuma tetap tampil kuat demi orang lain.",
        "domains": {
            "karir": "Kamu bersinar di posisi kepemimpinan yang melibatkan pengembangan "
                     "orang lain, seperti pendidikan, HR, konsultasi, atau kepemimpinan "
                     "organisasi yang butuh visi kuat dan kemampuan menggerakkan tim. Kamu "
                     "paling puas kalau merasa pekerjaanmu membantu orang lain bertumbuh. Tapi "
                     "kamu bisa kelelahan kalau terus-menerus mengurus kebutuhan tim tanpa "
                     "menjaga batasan yang jelas. Kamu juga kadang terlalu berharap tim "
                     "mengikuti visimu secepat yang kamu mau. *PR: tetapkan satu batas jelas "
                     "soal jam kerja atau tanggung jawab yang bukan bagianmu, dan pegang "
                     "batas itu.*",
            "asmara": "Kamu pasangan yang suportif dan penuh perhatian, selalu berusaha "
                      "membantu pasangan berkembang jadi versi terbaik dari diri mereka. Kamu "
                      "juga komunikatif dan tulus soal perasaan. Tapi kamu bisa terlalu "
                      "berharap pasangan berubah sesuai visimu tentang hubungan ideal, "
                      "sehingga kecewa kalau kenyataannya berbeda. *PR: terima pasangan apa "
                      "adanya di satu hal yang selama ini ingin kamu ubah, dan lihat "
                      "bagaimana rasanya.*",
            "keuangan": "Kamu cenderung murah hati dan sering membantu orang lain secara "
                        "finansial, kadang sampai mengorbankan kebutuhanmu sendiri demi "
                        "mendukung orang-orang yang kamu pedulikan. *PR: buat batas jelas "
                        "untuk bantuan finansial ke orang lain, supaya kebutuhanmu sendiri "
                        "tetap terjaga.*",
            "kesehatan": "Kamu rentan kelelahan emosional karena terus-menerus memberi "
                         "perhatian ke orang lain sampai lupa mengisi ulang energimu sendiri, "
                         "dan kamu cenderung menyembunyikan kelelahan itu demi tetap terlihat "
                         "kuat. *PR: jadwalkan waktu istirahat rutin yang benar-benar untuk "
                         "dirimu sendiri, dan anggap itu sama pentingnya dengan membantu orang "
                         "lain.*",
        },
    },
    "ENTJ": {
        "tagline": "👑 Sang Komandan Berorientasi Hasil",
        "chip": "MBTI",
        "title": "ENTJ — Sang Komandan yang Berorientasi pada Hasil",
        "p1_label": "Siapa Kamu",
        "p1": "Kamu adalah tipe yang secara alami mengambil kendali saat situasi butuh arahan "
              "jelas, dan kamu tidak takut mengambil keputusan besar meski risikonya tinggi. "
              "Kamu punya visi jangka panjang yang kuat dan kemampuan menyusun strategi untuk "
              "mencapainya secara sistematis. Sejak kecil, kamu mungkin sudah jadi anak yang "
              "memimpin kelompok bermain, punya cara pandang yang lebih terstruktur "
              "dibanding teman-teman sebaya. Kamu percaya diri dalam menyampaikan pendapat "
              "dan tidak takut mempertanyakan cara-cara lama kalau menurutmu ada pendekatan "
              "yang lebih efisien. Dalam pergaulan, kamu tegas dan langsung, orang tahu "
              "persis apa yang kamu pikirkan karena kamu jarang berbasa-basi soal hal yang "
              "penting. Kamu menghargai kompetensi dan hasil nyata di atas segalanya, dan "
              "kamu punya standar tinggi baik untuk dirimu sendiri maupun orang-orang yang "
              "bekerja denganmu. Orang-orang di sekitarmu sering merasa termotivasi untuk "
              "bekerja lebih baik saat berada di bawah kepemimpinanmu, karena kamu punya "
              "cara membuat target besar terasa bisa dicapai. Kamu tidak suka membuang waktu "
              "untuk hal-hal yang tidak produktif, kamu lebih suka langsung bergerak menuju "
              "hasil.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kemampuan kepemimpinan dan visimu yang kuat bikin kamu jadi sosok yang bisa "
              "membawa tim mencapai target besar yang orang lain anggap mustahil. Ketegasanmu "
              "dalam mengambil keputusan juga bikin orang merasa aman berada di bawah "
              "arahanmu saat situasi tidak menentu. Tapi keinginanmu untuk selalu mencapai "
              "hasil terbaik kadang bikin kamu kurang sabar dengan proses yang lambat atau "
              "orang yang belum secepat dirimu. Kamu juga bisa terlihat terlalu dominan dalam "
              "diskusi, sehingga orang lain merasa sungkan menyampaikan pendapat berbeda. "
              "Kecenderungan untuk fokus pada efisiensi dan hasil kadang bikin kamu kurang "
              "memperhatikan sisi emosional dari orang-orang yang bekerja bersamamu.",
        "quote": "Ambisi besar akan jauh lebih kuat kalau dibawa bersama orang-orang yang "
                 "merasa didengar, bukan cuma diarahkan.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba beri jeda dalam diskusi untuk mendengarkan pendapat orang lain sampai "
              "selesai, sebelum kamu menyampaikan penilaianmu sendiri. Latih diri untuk "
              "menanyakan perasaan tim, bukan cuma progres kerja mereka. Sesekali, izinkan "
              "proses berjalan dengan kecepatan yang berbeda dari yang kamu inginkan, dan "
              "lihat apakah hasilnya tetap baik. Sampaikan apresiasi secara terbuka saat "
              "orang lain berhasil melakukan sesuatu dengan baik, jangan cuma dianggap "
              "sebagai standar yang memang seharusnya begitu.",
        "domains": {
            "karir": "Kamu unggul di posisi kepemimpinan strategis yang butuh visi besar dan "
                     "kemampuan eksekusi, seperti manajemen puncak, kewirausahaan, atau "
                     "konsultasi bisnis. Kamu paling puas kalau diberi tanggung jawab besar "
                     "dan otonomi untuk mengambil keputusan. Tapi kamu bisa terlihat "
                     "mengintimidasi bagi rekan kerja yang tidak terbiasa dengan gaya "
                     "komunikasimu yang langsung dan penuh tekanan. Kamu juga kadang kurang "
                     "sabar dengan anggota tim yang butuh waktu lebih lama untuk memahami "
                     "sesuatu. *PR: luangkan waktu menjelaskan alasan di balik keputusanmu ke "
                     "tim, bukan cuma memberi instruksi.*",
            "asmara": "Kamu pasangan yang setia dan serius soal komitmen, selalu memikirkan "
                      "masa depan hubungan secara matang dan strategis. Kamu juga menghargai "
                      "pasangan yang punya ambisi dan bisa diajak diskusi setara. Tapi kamu "
                      "bisa terlalu fokus pada pencapaian bersama sampai lupa momen emosional "
                      "sederhana yang juga penting dalam hubungan. *PR: sesekali, luangkan "
                      "waktu berkualitas bersama pasangan tanpa agenda atau target apa pun.*",
            "keuangan": "Kamu punya perencanaan keuangan yang ambisius dan terstruktur, "
                        "sering memikirkan investasi dan pertumbuhan kekayaan jangka panjang "
                        "secara serius. Tapi kamu bisa terlalu fokus mengejar target finansial "
                        "sampai lupa menikmati hasil kerja kerasmu sesekali. *PR: alokasikan "
                        "satu pos khusus untuk kesenangan, terlepas dari seberapa besar target "
                        "finansialmu belum tercapai.*",
            "kesehatan": "Kamu cenderung mendorong diri bekerja keras tanpa henti, sering "
                         "mengabaikan sinyal kelelahan karena merasa masih ada target yang "
                         "belum tercapai. Kamu juga jarang mengakui kalau sedang stres, lebih "
                         "memilih tetap terlihat kuat di depan tim. *PR: jadwalkan waktu "
                         "istirahat sebagai bagian dari target kerjamu, bukan sekadar kalau "
                         "ada waktu sisa.*",
        },
    },
}
