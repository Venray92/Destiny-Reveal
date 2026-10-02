"""
Konten Tarot (22 Arcana Mayor).

Key dict ini HARUS sama persis dengan nilai "kartu" dari engine/tarot.py
(slug lowercase: fool, magician, high_priestess, dst — sama urutan kayak
TAROT_MAJOR_ARCANA & nama file gambar 00_fool.png dst).

Catatan: Tarot itu "acak" (Kelompok F, bukan berbasis data lahir), jadi
kartu yang ditarik TIDAK merepresentasikan sifat permanen orangnya kayak
sistem lain -- lebih ke arah refleksi/perenungan sesaat. Bahasa kontennya
disesuaikan (pakai framing "kartu yang kamu tarik hari ini menunjukkan...",
bukan "kamu adalah...").
"""

TAROT_CONTENT = {
    "fool": {
        "tagline": "0 · The Fool",
        "chip": "TAROT",
        "title": "The Fool — Awal yang Berani",
        "p1_label": "Makna Kartu Ini",
        "p1": "The Fool menandai permulaan baru — sebuah lompatan ke hal yang belum pernah kamu coba "
              "sebelumnya. Kartu ini muncul saat semesta seolah mengajak kamu berhenti terlalu banyak "
              "berpikir dan mulai melangkah, meski belum semua terlihat jelas. Ada energi polos dan penuh "
              "harapan di sini, seperti pengelana yang berjalan tanpa peta tapi percaya jalannya akan "
              "terbuka sendiri.",
        "p2_label": "Pesan untuk Direnungkan",
        "p2": "Kalau belakangan ini kamu ragu memulai sesuatu — proyek baru, hubungan baru, arah karir "
              "baru — kartu ini adalah dorongan buat berani ambil langkah pertama itu. Bukan berarti "
              "tanpa perhitungan sama sekali, tapi jangan biarkan rasa takut gagal menahanmu terus-menerus "
              "di tempat yang sama.",
        "quote": "\"Setiap perjalanan besar selalu dimulai dari satu langkah yang terasa kecil dan menakutkan.\"",
        "p3_label": "Untuk Hari Ini",
        "p3": "Coba mulai satu hal kecil yang selama ini kamu tunda karena takut belum siap — kirim "
              "pesan itu, ajukan ide itu, daftar untuk hal baru itu. Energi hari ini mendukung keberanian, "
              "bukan kesempurnaan persiapan.",
    },
    "magician": {
        "tagline": "I · The Magician",
        "chip": "TAROT",
        "title": "The Magician — Kamu Punya Semua Alatnya",
        "p1_label": "Makna Kartu Ini",
        "p1": "The Magician muncul saat kamu sebenarnya sudah punya semua yang dibutuhkan untuk "
              "mewujudkan sesuatu — kemampuan, sumber daya, kesempatan — tinggal soal fokus dan kemauan "
              "buat menggerakkannya. Kartu ini melambangkan kekuatan niat: apa yang kamu pikirkan dengan "
              "sungguh-sungguh, punya peluang besar buat jadi nyata.",
        "p2_label": "Pesan untuk Direnungkan",
        "p2": "Ini bukan waktunya menunggu kondisi sempurna atau alat tambahan — apa yang kamu punya "
              "sekarang sudah cukup buat mulai. Pertanyaannya bukan 'apa aku sudah siap', tapi 'apa aku "
              "sudah pakai apa yang aku punya dengan maksimal'.",
        "quote": "\"Yang membedakan mimpi dan kenyataan sering kali cuma soal siapa yang benar-benar mulai bergerak.\"",
        "p3_label": "Untuk Hari Ini",
        "p3": "Susun satu niat konkret dan mulai kerjakan hari ini juga, sekecil apapun langkahnya — "
              "energi hari ini mendukung eksekusi, bukan perencanaan lebih lama lagi.",
    },
    "high_priestess": {
        "tagline": "II · The High Priestess",
        "chip": "TAROT",
        "title": "The High Priestess — Dengarkan Intuisimu",
        "p1_label": "Makna Kartu Ini",
        "p1": "The High Priestess mewakili pengetahuan yang gak selalu datang dari logika atau data — "
              "kadang jawaban paling tepat justru datang dari perasaan yang tenang di dalam diri. Kartu "
              "ini muncul saat ada sesuatu yang belum terlihat jelas di permukaan, tapi sebenarnya kamu "
              "sudah punya firasat soal itu.",
        "p2_label": "Pesan untuk Direnungkan",
        "p2": "Kalau ada keputusan yang belakangan bikin kamu ragu, coba diam sebentar dan dengarkan apa "
              "kata intuisimu sebelum buru-buru minta pendapat orang lain. Bukan berarti abaikan logika "
              "sepenuhnya, tapi beri ruang juga buat suara batinmu didengar.",
        "quote": "\"Tidak semua yang penting harus terlihat jelas dulu baru dipercaya.\"",
        "p3_label": "Untuk Hari Ini",
        "p3": "Luangkan waktu sendiri, sejenak tanpa gangguan, untuk benar-benar bertanya ke diri sendiri "
              "apa yang sebenarnya kamu rasakan soal satu hal yang lagi mengganjal.",
    },
    "empress": {
        "tagline": "III · The Empress",
        "chip": "TAROT",
        "title": "The Empress — Waktunya Bertumbuh",
        "p1_label": "Makna Kartu Ini",
        "p1": "The Empress melambangkan kelimpahan, kehangatan, dan pertumbuhan alami — seperti musim di "
              "mana semua yang kamu tanam sebelumnya mulai berbuah. Kartu ini sering muncul saat hidup "
              "sedang meminta kamu untuk merawat sesuatu dengan sabar, bukan buru-buru memaksakan hasil.",
        "p2_label": "Pesan untuk Direnungkan",
        "p2": "Ini waktu yang baik buat memberi perhatian ke hal-hal yang selama ini kamu abaikan karena "
              "sibuk mengejar target — relasi, kesehatan, atau proyek yang butuh dirawat pelan-pelan. "
              "Hasil besar sering datang dari perawatan konsisten, bukan dorongan sesaat.",
        "quote": "\"Yang dirawat dengan sabar biasanya tumbuh lebih kokoh dari yang dipaksa cepat besar.\"",
        "p3_label": "Untuk Hari Ini",
        "p3": "Rawat satu hal yang selama ini kamu tunda perhatiannya — hubungi orang yang kamu rindukan, "
              "atau luangkan waktu buat proyek yang selama ini cuma jalan setengah hati.",
    },
    "emperor": {
        "tagline": "IV · The Emperor",
        "chip": "TAROT",
        "title": "The Emperor — Saatnya Ambil Kendali",
        "p1_label": "Makna Kartu Ini",
        "p1": "The Emperor melambangkan struktur, disiplin, dan kepemimpinan yang tegas. Kartu ini muncul "
              "saat kamu perlu menetapkan batasan yang lebih jelas, baik ke diri sendiri maupun orang "
              "lain, supaya sesuatu yang selama ini berantakan bisa kembali teratur.",
        "p2_label": "Pesan untuk Direnungkan",
        "p2": "Kalau belakangan ini kamu merasa kewalahan karena semua terasa gak terkontrol, ini saatnya "
              "bikin sistem atau aturan main yang lebih jelas — bukan buat mengekang, tapi buat kasih "
              "pondasi yang bikin semua orang (termasuk kamu) tahu harus ngapain.",
        "quote": "\"Kebebasan yang sebenarnya sering lahir dari struktur yang jelas, bukan dari ketiadaan aturan.\"",
        "p3_label": "Untuk Hari Ini",
        "p3": "Tetapkan satu batasan yang selama ini kamu tunda — bilang tidak ke permintaan yang "
              "berlebihan, atau bikin jadwal yang lebih tegas buat dirimu sendiri.",
    },
    "hierophant": {
        "tagline": "V · The Hierophant",
        "chip": "TAROT",
        "title": "The Hierophant — Belajar dari yang Sudah Teruji",
        "p1_label": "Makna Kartu Ini",
        "p1": "The Hierophant mewakili tradisi, bimbingan, dan kebijaksanaan yang diwariskan — belajar "
              "dari orang yang lebih berpengalaman atau sistem yang sudah teruji, bukan selalu harus "
              "menemukan semuanya sendiri dari nol.",
        "p2_label": "Pesan untuk Direnungkan",
        "p2": "Kalau kamu lagi berjuang sendirian dengan sesuatu, kartu ini mengingatkan bahwa cari "
              "mentor, guru, atau komunitas yang sudah lebih dulu melewati jalan itu bukan tanda lemah — "
              "itu cara paling efisien buat belajar.",
        "quote": "\"Gak semua jalan harus ditemukan sendiri — kadang yang paling bijak adalah bertanya ke yang sudah lebih dulu lewat.\"",
        "p3_label": "Untuk Hari Ini",
        "p3": "Cari satu sumber belajar (orang, buku, komunitas) yang bisa bimbing kamu di area yang "
              "selama ini kamu coba pahami sendirian.",
    },
    "lovers": {
        "tagline": "VI · The Lovers",
        "chip": "TAROT",
        "title": "The Lovers — Pilihan dari Hati",
        "p1_label": "Makna Kartu Ini",
        "p1": "The Lovers melambangkan momen memilih — bukan cuma soal cinta romantis, tapi juga soal "
              "keselarasan antara nilai-nilai yang kamu pegang dan langkah yang kamu ambil. Kartu ini "
              "muncul saat kamu dihadapkan pada keputusan yang butuh kejujuran ke diri sendiri.",
        "p2_label": "Pesan untuk Direnungkan",
        "p2": "Kalau ada pilihan yang bikin kamu bimbang belakangan ini, coba tanya bukan 'mana yang lebih "
              "aman', tapi 'mana yang benar-benar selaras dengan siapa aku sebenarnya'.",
        "quote": "\"Keputusan yang paling melegakan biasanya yang paling jujur, bukan yang paling nyaman.\"",
        "p3_label": "Untuk Hari Ini",
        "p3": "Hadapi satu keputusan yang selama ini kamu hindari, dan coba jawab dengan jujur apa yang "
              "benar-benar kamu inginkan — bukan apa yang orang lain harapkan darimu.",
    },
    "chariot": {
        "tagline": "VII · The Chariot",
        "chip": "TAROT",
        "title": "The Chariot — Terus Maju dengan Fokus",
        "p1_label": "Makna Kartu Ini",
        "p1": "The Chariot melambangkan kemenangan lewat kemauan keras dan fokus yang gak goyah, meski "
              "ada dua arah yang menarik-narik. Kartu ini muncul saat kamu perlu menyatukan energi yang "
              "selama ini terpecah, lalu mengarahkannya ke satu tujuan yang jelas.",
        "p2_label": "Pesan untuk Direnungkan",
        "p2": "Kalau belakangan ini kamu merasa energimu kesebar ke banyak arah, saatnya pilih satu "
              "prioritas dan kejar itu dengan sungguh-sungguh, daripada setengah-setengah di banyak hal "
              "sekaligus.",
        "quote": "\"Kecepatan tanpa arah cuma bikin capek — kemenangan datang dari fokus, bukan dari sibuk ke mana-mana.\"",
        "p3_label": "Untuk Hari Ini",
        "p3": "Pilih satu tujuan yang paling penting minggu ini, dan alokasikan energi utamamu ke situ, "
              "bukan tersebar ke semua hal sekaligus.",
    },
    "strength": {
        "tagline": "VIII · Strength",
        "chip": "TAROT",
        "title": "Strength — Kekuatan yang Lembut",
        "p1_label": "Makna Kartu Ini",
        "p1": "Strength menunjukkan bahwa kekuatan sejati gak selalu soal memaksa atau melawan keras — "
              "kadang justru soal kesabaran dan ketenangan menghadapi sesuatu yang menakutkan. Kartu ini "
              "muncul saat kamu perlu menjinakkan rasa takut atau amarah dengan lembut, bukan menekannya "
              "paksa.",
        "p2_label": "Pesan untuk Direnungkan",
        "p2": "Kalau ada situasi yang bikin kamu ingin bereaksi keras, coba dekati dengan ketenangan dulu "
              "— kekuatan yang lembut biasanya lebih tahan lama dibanding ledakan emosi sesaat.",
        "quote": "\"Yang paling berani bukan yang gak pernah takut, tapi yang tetap tenang meski takut.\"",
        "p3_label": "Untuk Hari Ini",
        "p3": "Hadapi satu hal yang bikin kamu cemas dengan cara yang tenang dan sabar, bukan dengan "
              "menghindar atau meledak.",
    },
    "hermit": {
        "tagline": "IX · The Hermit",
        "chip": "TAROT",
        "title": "The Hermit — Waktunya Menyendiri Sejenak",
        "p1_label": "Makna Kartu Ini",
        "p1": "The Hermit melambangkan pentingnya waktu sendiri untuk refleksi mendalam. Kartu ini muncul "
              "saat kamu butuh menjauh sejenak dari keramaian untuk benar-benar mendengar apa yang ada di "
              "dalam dirimu, bukan suara-suara dari luar.",
        "p2_label": "Pesan untuk Direnungkan",
        "p2": "Kalau belakangan ini kamu merasa terlalu banyak dipengaruhi pendapat orang lain, ini "
              "saatnya menarik diri sejenak dan cari jawaban dari dalam diri sendiri dulu.",
        "quote": "\"Kadang jawaban paling jelas cuma bisa ditemukan dalam keheningan, bukan dalam keramaian.\"",
        "p3_label": "Untuk Hari Ini",
        "p3": "Luangkan waktu sendirian tanpa gangguan gawai, walau cuma sebentar, buat benar-benar "
              "merenungkan satu hal yang lagi kamu pikirkan.",
    },
    "wheel_of_fortune": {
        "tagline": "X · Wheel of Fortune",
        "chip": "TAROT",
        "title": "Wheel of Fortune — Siklus Sedang Berputar",
        "p1_label": "Makna Kartu Ini",
        "p1": "Wheel of Fortune melambangkan perputaran nasib — kadang di atas, kadang di bawah, dan itu "
              "bagian alami dari kehidupan. Kartu ini muncul saat ada perubahan besar di depan mata, baik "
              "yang kamu rencanakan atau yang datang tiba-tiba.",
        "p2_label": "Pesan untuk Direnungkan",
        "p2": "Kalau kamu lagi di masa sulit, kartu ini mengingatkan bahwa itu gak akan selamanya begitu "
              "— roda terus berputar. Sebaliknya, kalau lagi di masa baik, manfaatkan sebaik mungkin "
              "karena siklus akan terus bergerak.",
        "quote": "\"Yang naik pasti pernah di bawah, yang di bawah pasti akan naik lagi — itu hukum alam yang gak bisa dihindari.\"",
        "p3_label": "Untuk Hari Ini",
        "p3": "Terima perubahan yang sedang terjadi di hidupmu sebagai bagian dari siklus, bukan sesuatu "
              "yang harus dilawan mati-matian.",
    },
    "justice": {
        "tagline": "XI · Justice",
        "chip": "TAROT",
        "title": "Justice — Keseimbangan & Konsekuensi",
        "p1_label": "Makna Kartu Ini",
        "p1": "Justice melambangkan keadilan, kejujuran, dan konsekuensi dari setiap tindakan. Kartu ini "
              "muncul saat kamu perlu melihat sesuatu secara objektif, tanpa bias, dan siap menerima "
              "hasil dari keputusan yang sudah kamu ambil sebelumnya.",
        "p2_label": "Pesan untuk Direnungkan",
        "p2": "Kalau ada situasi yang terasa gak adil, coba lihat dari semua sisi dulu sebelum menyimpulkan "
              "— dan kalau ada tanggung jawab yang selama ini kamu hindari, sekaranglah saatnya "
              "menghadapinya dengan jujur.",
        "quote": "\"Keadilan dimulai dari kejujuran ke diri sendiri, sebelum menuntutnya dari orang lain.\"",
        "p3_label": "Untuk Hari Ini",
        "p3": "Selesaikan satu urusan yang butuh keputusan adil dan jujur — baik itu soal komitmen, "
              "kesepakatan, atau permintaan maaf yang tertunda.",
    },
    "hanged_man": {
        "tagline": "XII · The Hanged Man",
        "chip": "TAROT",
        "title": "The Hanged Man — Ubah Sudut Pandang",
        "p1_label": "Makna Kartu Ini",
        "p1": "The Hanged Man melambangkan jeda dan perspektif baru — kadang kamu perlu berhenti sejenak "
              "dan melihat masalah dari sudut yang berbeda sama sekali untuk menemukan jawabannya. Kartu "
              "ini muncul saat cara lama sudah gak lagi memberi hasil.",
        "p2_label": "Pesan untuk Direnungkan",
        "p2": "Kalau kamu merasa stuck dengan satu masalah, coba lepaskan dulu keinginan untuk buru-buru "
              "menyelesaikannya, dan lihat dari sudut pandang yang benar-benar baru — kadang jeda itu "
              "sendiri yang jadi kunci.",
        "quote": "\"Kadang cara paling produktif untuk maju adalah dengan berhenti sejenak dan melihat ulang arahnya.\"",
        "p3_label": "Untuk Hari Ini",
        "p3": "Coba lihat satu masalah yang bikin kamu stuck dari sudut pandang yang sama sekali berbeda "
              "— tanya pendapat orang dengan latar belakang berbeda dari biasanya.",
    },
    "death": {
        "tagline": "XIII · Death",
        "chip": "TAROT",
        "title": "Death — Transformasi, Bukan Akhir",
        "p1_label": "Makna Kartu Ini",
        "p1": "Meski namanya terdengar menakutkan, Death dalam tarot melambangkan transformasi dan "
              "penutupan satu babak untuk membuka babak baru — bukan kematian secara harfiah. Kartu ini "
              "muncul saat ada sesuatu yang perlu dilepaskan supaya ruang baru bisa tumbuh.",
        "p2_label": "Pesan untuk Direnungkan",
        "p2": "Kalau ada kebiasaan, hubungan, atau situasi yang sudah gak lagi cocok buatmu, kartu ini "
              "adalah tanda untuk mulai merelakannya — menggenggam terlalu erat cuma menahan pertumbuhan "
              "yang seharusnya sudah bisa terjadi.",
        "quote": "\"Sesuatu harus berakhir dulu supaya yang baru punya ruang untuk tumbuh.\"",
        "p3_label": "Untuk Hari Ini",
        "p3": "Identifikasi satu hal yang sebenarnya sudah gak lagi melayani dirimu, dan mulai proses "
              "melepaskannya, meski pelan-pelan.",
    },
    "temperance": {
        "tagline": "XIV · Temperance",
        "chip": "TAROT",
        "title": "Temperance — Cari Titik Seimbang",
        "p1_label": "Makna Kartu Ini",
        "p1": "Temperance melambangkan keseimbangan, kesabaran, dan perpaduan yang harmonis antara dua "
              "hal yang berbeda. Kartu ini muncul saat kamu perlu mencari jalan tengah, bukan memilih "
              "ekstrem di satu sisi saja.",
        "p2_label": "Pesan untuk Direnungkan",
        "p2": "Kalau belakangan ini hidupmu terasa timpang — terlalu banyak kerja atau terlalu santai, "
              "terlalu emosional atau terlalu menahan diri — kartu ini mengingatkan buat mencari "
              "keseimbangan pelan-pelan, bukan perubahan drastis tiba-tiba.",
        "quote": "\"Harmoni gak datang dari memilih satu sisi, tapi dari meramu keduanya dengan sabar.\"",
        "p3_label": "Untuk Hari Ini",
        "p3": "Cari satu area hidup yang lagi timpang, dan ambil langkah kecil untuk menyeimbangkannya — "
              "gak perlu langsung sempurna, cukup lebih seimbang dari kemarin.",
    },
    "devil": {
        "tagline": "XV · The Devil",
        "chip": "TAROT",
        "title": "The Devil — Kenali Belenggu yang Kamu Buat Sendiri",
        "p1_label": "Makna Kartu Ini",
        "p1": "The Devil melambangkan keterikatan yang sebenarnya bisa dilepaskan, tapi terasa sulit "
              "karena sudah jadi kebiasaan atau zona nyaman — entah itu pola pikir negatif, kebiasaan "
              "buruk, atau hubungan yang gak sehat. Kartu ini mengingatkan bahwa rantainya lebih longgar "
              "dari yang kamu kira.",
        "p2_label": "Pesan untuk Direnungkan",
        "p2": "Kalau ada sesuatu yang bikin kamu merasa terjebak belakangan ini, coba tanya jujur ke diri "
              "sendiri: apakah ini benar-benar gak bisa diubah, atau kamu cuma belum berani mengambil "
              "langkah untuk lepas darinya?",
        "quote": "\"Belenggu yang paling kuat sering kali adalah yang kita ciptakan sendiri di kepala.\"",
        "p3_label": "Untuk Hari Ini",
        "p3": "Kenali satu kebiasaan atau pola pikir yang sebenarnya menahanmu, dan ambil satu langkah "
              "kecil untuk mulai melonggarkan pegangannya.",
    },
    "tower": {
        "tagline": "XVI · The Tower",
        "chip": "TAROT",
        "title": "The Tower — Keruntuhan yang Diperlukan",
        "p1_label": "Makna Kartu Ini",
        "p1": "The Tower melambangkan perubahan mendadak yang meruntuhkan sesuatu yang selama ini "
              "kelihatan kokoh, tapi sebenarnya dibangun di atas fondasi yang rapuh. Kartu ini muncul "
              "saat sesuatu perlu runtuh dulu supaya kamu bisa membangun ulang dengan lebih kuat.",
        "p2_label": "Pesan untuk Direnungkan",
        "p2": "Kalau belakangan ini ada kejutan atau kegagalan yang bikin rencana berantakan, coba lihat "
              "itu bukan sebagai bencana total, tapi kesempatan untuk membangun ulang di atas fondasi "
              "yang lebih jujur dan kuat.",
        "quote": "\"Kadang yang runtuh memang harus runtuh, supaya yang dibangun selanjutnya lebih kokoh.\"",
        "p3_label": "Untuk Hari Ini",
        "p3": "Kalau ada rencana yang baru saja berantakan, jangan buru-buru menambal — ambil waktu dulu "
              "untuk lihat fondasi mana yang perlu benar-benar diperbaiki.",
    },
    "star": {
        "tagline": "XVII · The Star",
        "chip": "TAROT",
        "title": "The Star — Harapan Setelah Badai",
        "p1_label": "Makna Kartu Ini",
        "p1": "The Star melambangkan harapan, ketenangan, dan pemulihan setelah masa sulit. Kartu ini "
              "muncul saat kamu perlu percaya lagi bahwa hal baik masih mungkin terjadi, meski belum "
              "lama ini kamu melewati sesuatu yang berat.",
        "p2_label": "Pesan untuk Direnungkan",
        "p2": "Kalau kamu masih memulihkan diri dari sesuatu, kartu ini adalah pengingat untuk gak "
              "kehilangan harapan — proses healing itu wajar berjalan pelan, dan itu gak berarti kamu "
              "gagal.",
        "quote": "\"Setelah badai paling gelap sekalipun, selalu ada bintang yang tetap bersinar.\"",
        "p3_label": "Untuk Hari Ini",
        "p3": "Lakukan satu hal kecil yang memberimu harapan atau ketenangan — jangan buru-buru semua "
              "harus pulih sekaligus.",
    },
    "moon": {
        "tagline": "XVIII · The Moon",
        "chip": "TAROT",
        "title": "The Moon — Waspada pada Ilusi",
        "p1_label": "Makna Kartu Ini",
        "p1": "The Moon melambangkan ketidakpastian, ilusi, dan hal-hal yang belum jelas kelihatannya. "
              "Kartu ini muncul saat kamu perlu berhati-hati membedakan mana yang fakta dan mana yang "
              "cuma ketakutan atau asumsi yang belum tentu benar.",
        "p2_label": "Pesan untuk Direnungkan",
        "p2": "Kalau ada kecemasan yang bikin kamu takut tanpa alasan jelas, coba pisahkan dulu mana yang "
              "benar-benar fakta dan mana yang cuma bayangan di kepala — sering kali kenyataannya gak "
              "seburuk yang dipikirkan.",
        "quote": "\"Yang paling menakutkan sering kali bukan kenyataannya, tapi bayangan yang kita ciptakan soal itu.\"",
        "p3_label": "Untuk Hari Ini",
        "p3": "Sebelum bereaksi ke sesuatu yang bikin cemas, coba cari fakta konkretnya dulu — jangan "
              "biarkan asumsi mengambil alih keputusanmu.",
    },
    "sun": {
        "tagline": "XIX · The Sun",
        "chip": "TAROT",
        "title": "The Sun — Kebahagiaan yang Tulus",
        "p1_label": "Makna Kartu Ini",
        "p1": "The Sun adalah salah satu kartu paling positif di tarot — melambangkan kebahagiaan, "
              "vitalitas, dan kejelasan yang datang setelah melewati masa penuh keraguan. Kartu ini "
              "muncul saat kamu berhak merayakan pencapaian atau sekadar menikmati momen baik yang ada.",
        "p2_label": "Pesan untuk Direnungkan",
        "p2": "Kalau belakangan ini kamu terlalu sibuk mengejar target sampai lupa menikmati hasilnya, "
              "kartu ini mengingatkan untuk berhenti sejenak dan benar-benar merasakan kebahagiaan yang "
              "sudah kamu raih.",
        "quote": "\"Kebahagiaan yang tulus gak butuh alasan besar — kadang cukup dengan berhenti sejenak dan menyadarinya.\"",
        "p3_label": "Untuk Hari Ini",
        "p3": "Rayakan satu pencapaian kecil yang selama ini kamu anggap remeh, dan bagikan kebahagiaan "
              "itu dengan orang terdekatmu.",
    },
    "judgement": {
        "tagline": "XX · Judgement",
        "chip": "TAROT",
        "title": "Judgement — Panggilan untuk Bangkit",
        "p1_label": "Makna Kartu Ini",
        "p1": "Judgement melambangkan momen kesadaran dan kebangkitan — saat kamu melihat kembali "
              "perjalanan yang sudah dilalui dan menyadari bahwa kamu siap untuk versi diri yang lebih "
              "baik. Kartu ini muncul saat ada panggilan untuk berubah yang gak bisa lagi diabaikan.",
        "p2_label": "Pesan untuk Direnungkan",
        "p2": "Kalau ada suara kecil di dalam dirimu yang terus mengingatkan untuk berubah atau memulai "
              "sesuatu yang lebih bermakna, kartu ini adalah tanda untuk mendengarkannya sekarang, bukan "
              "menundanya lagi.",
        "quote": "\"Kebangkitan sejati dimulai saat kamu berhenti menunggu izin dari orang lain untuk berubah.\"",
        "p3_label": "Untuk Hari Ini",
        "p3": "Dengarkan panggilan yang selama ini kamu abaikan — entah itu soal karir, kebiasaan, atau "
              "cara kamu memperlakukan diri sendiri.",
    },
    "world": {
        "tagline": "XXI · The World",
        "chip": "TAROT",
        "title": "The World — Satu Babak Tuntas",
        "p1_label": "Makna Kartu Ini",
        "p1": "The World melambangkan penyelesaian penuh — satu perjalanan panjang yang akhirnya sampai "
              "di titik tuntas dan utuh. Kartu ini muncul saat kamu berhak merasa puas atas apa yang "
              "sudah dicapai, sebelum bersiap untuk babak berikutnya.",
        "p2_label": "Pesan untuk Direnungkan",
        "p2": "Kalau ada babak hidup yang terasa mulai mendekati akhir — sebuah fase, proyek, atau "
              "hubungan tertentu — kartu ini mengingatkan untuk mengakuinya sebagai pencapaian utuh, "
              "bukan sekadar lewat begitu saja tanpa disadari.",
        "quote": "\"Setiap akhir yang tuntas adalah pintu menuju awal yang baru, bukan sekadar berhenti.\"",
        "p3_label": "Untuk Hari Ini",
        "p3": "Luangkan waktu mengakui satu pencapaian besar yang sudah kamu selesaikan, sebelum "
              "melangkah ke tujuan berikutnya.",
    },
}
