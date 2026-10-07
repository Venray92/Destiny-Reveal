"""
Modal detail 15 sistem (diklik dari diagram "Satu Dirimu, 15 Cara Memandang").
Tombol "Hitung X Milikku" -> Solo Reveal untuk sistem itu.
State: dh_sysinfo = nama sistem.
"""
import streamlit as st

from components.data import CATEGORY_SYSTEMS, NODE_ORDER
from components.dialog_bus import request_open

# nama: (kutipan, deskripsi, sumber data, [3 bullet], potensi utama, titik buta)
_INFO = {
    "Zodiak": ("Peta posisi matahari saat lahir yang membentuk ego, dorongan dasar, dan esensi jiwa.",
               "Berdasarkan pergerakan matahari melintasi 12 rasi bintang ekliptika Barat. Zodiak membedah cetak biru kepribadian dasar, temperamen elemen (Api, Tanah, Udara, Air), serta bagaimana kamu merespons tantangan eksternal.",
               "Tanggal Lahir & Nama", ["Elemen Utama & Modalitas", "Dorongan Ego Dasar", "Kompatibilitas Hubungan"],
               "Mengetahui cara alami kamu mengekspresikan diri dan energi vital yang menggerakkan motivasimu.",
               "Kecenderungan terlalu mengandalkan reaksi impulsif elemen dominan saat di bawah tekanan."),
    "Shio": ("Hewan penjaga tahun lahirmu, cermin watak dan ritme keberuntunganmu.",
             "Siklus 12 hewan dalam kalender Tionghoa yang dipakai membaca watak dasar, hubungan antar-shio, dan tahun-tahun yang mendukung atau menantangmu.",
             "Tanggal Lahir (tahun lunar)", ["Watak & Gaya Hidup", "Kecocokan Antar-Shio", "Tahun Hoki & Waspada"],
             "Memahami kekuatan alami dan pasangan atau rekan yang paling selaras denganmu.",
             "Terlalu percaya stereotip hewan sampai lupa bahwa tiap orang punya konteks sendiri."),
    "Weton": ("Hitungan hari lahir Jawa yang menyatukan pasaran dan neptu jadi penanda watak.",
              "Primbon Jawa memadukan 7 hari dan 5 pasaran menjadi neptu. Dari sana dibaca karakter, rezeki, dan keselarasan hubungan menurut tradisi Nusantara.",
              "Tanggal Lahir", ["Hari, Pasaran & Neptu", "Watak Dasar Weton", "Rezeki & Hari Baik"],
              "Mengenal akar budayamu sendiri sekaligus pola watak yang diwariskan lewat hari lahir.",
              "Memakai angka neptu sebagai vonis mutlak untuk keputusan besar tanpa pertimbangan lain."),
    "Numerologi": ("Angka dari tanggal lahir dan namamu menyimpan pola hidup yang berulang.",
                   "Penafsiran angka (Life Path, Expression, Soul Urge) untuk membaca arah hidup, bakat bawaan, dan tantangan yang cenderung muncul lagi.",
                   "Tanggal Lahir & Nama Lengkap", ["Jalan Hidup Utama", "Angka Keberuntungan Pribadi", "Tantangan yang Berulang"],
                   "Melihat arah hidup dan bakat bawaan yang selama ini terasa samar.",
                   "Terpaku pada makna angka dan lupa bahwa tindakan nyata yang menentukan hasil."),
    "Matrix Destiny": ("Satu diagram dari tanggal lahir yang merangkum karakter, rezeki, dan pelajaran jiwa.",
                       "Peta numerologi 22 arkana yang diletakkan dalam diagram oktagon. Tiap titik menunjukkan energi karakter, hubungan, uang, dan karma yang dibawa sejak lahir.",
                       "Tanggal Lahir", ["Peta Kepribadian Menyeluruh", "Arah Rezeki & Keuangan", "Pelajaran Hidup Bawaan"],
                       "Gambaran besar hidupmu dalam satu peta, jadi mudah menentukan fokus.",
                       "Kewalahan oleh banyaknya titik energi dan sibuk menganalisis tanpa mulai bertindak."),
    "MBTI": ("Enam belas tipe cara berpikir dan bekerja, dari empat preferensi dasar.",
             "Model dari Myers-Briggs yang membagi preferensi energi (E/I), informasi (S/N), keputusan (T/F), dan gaya hidup (J/P) menjadi 16 tipe.",
             "Kuesioner Singkat", ["Gaya Berpikir & Memproses Info", "Cara Kerja Paling Efektif", "Kecocokan dengan Tipe Lain"],
             "Bahasa bersama untuk menjelaskan gaya kerja dan komunikasimu ke orang lain.",
             "Memakai 4 huruf sebagai kotak sempit yang membatasi diri, padahal ia cuma kecenderungan."),
    "Big Five": ("Lima dimensi karakter yang paling teruji dalam riset psikologi.",
                 "Model OCEAN: Keterbukaan, Kehati-hatian, Ekstraversi, Keramahan, dan Neurotisisme. Dinilai sebagai skor spektrum, bukan label.",
                 "Kuesioner Singkat", ["Keterbukaan pada Hal Baru", "Cara Mengelola Emosi", "Gaya Bekerja Sama"],
                 "Gambaran terukur tentang dirimu yang bisa jadi dasar pengembangan diri.",
                 "Membandingkan skor dengan orang lain dan lupa bahwa tiap dimensi punya sisi kuat masing-masing."),
    "DISC": ("Cara kamu berkomunikasi, memutuskan, dan bereaksi saat ditekan di dunia kerja.",
             "Model perilaku empat gaya: Dominance, Influence, Steadiness, Compliance. Banyak dipakai dalam rekrutmen dan pengembangan tim.",
             "Kuesioner Singkat", ["Gaya Komunikasi Kerja", "Cara Mengambil Keputusan", "Reaksi terhadap Tekanan"],
             "Tahu gaya kerjamu sendiri untuk wawancara, kolaborasi, dan memimpin tim.",
             "Kaku pada satu gaya dan sulit menyesuaikan diri dengan rekan yang berbeda."),
    "Enneagram": ("Motivasi inti dan ketakutan terdalam di balik pola perilakumu.",
                  "Sembilan tipe yang menelusuri alasan di balik tindakan, bukan sekadar tindakannya, lengkap dengan jalur tumbuh dan jalur stres.",
                  "Kuesioner Singkat", ["Motivasi Tersembunyi", "Ketakutan yang Memengaruhi Pilihan", "Arah Tumbuh Jadi Versi Terbaik"],
                  "Menyadari pemicu reaksi otomatis sehingga bisa memilih respons yang lebih sehat.",
                  "Terjebak mengidentifikasi diri pada satu tipe dan membenarkan pola lamanya."),
    "Love Language": ("Cara paling nyaman kamu memberi dan menerima kasih sayang.",
                      "Lima bahasa kasih: kata-kata afirmasi, waktu berkualitas, hadiah, pelayanan, dan sentuhan fisik. Membantu mengurangi salah paham di hubungan.",
                      "Kuesioner Singkat", ["Cara Menerima Kasih Sayang", "Cara Menyampaikan Perhatian", "Potensi Salah Paham"],
                      "Komunikasi dengan pasangan, keluarga, dan teman jadi lebih lancar dan tepat sasaran.",
                      "Berharap orang lain otomatis tahu bahasa kasihmu tanpa pernah mengatakannya."),
    "BaZi": ("Empat pilar waktu lahirmu: tahun, bulan, hari, dan jam.",
             "Astrologi Tiongkok klasik yang menghitung keseimbangan lima elemen dari empat pilar untuk membaca struktur nasib, rezeki, dan siklus hidup.",
             "Tanggal & Jam Lahir", ["Elemen Dominan Diri", "Potensi Rezeki & Karier", "Periode Hidup Penting"],
             "Memahami elemen yang perlu diperkuat dan waktu yang pas untuk melangkah.",
             "Menunda keputusan menunggu 'waktu sempurna' sampai peluang lewat."),
    "Zi Wei": ("Peta 12 istana kehidupan dari saat tepat kamu lahir.",
               "Zi Wei Dou Shu menempatkan bintang-bintang pada 12 istana (karier, harta, jodoh, dll.) berdasarkan kalender lunar dan jam lahir.",
               "Tanggal & Jam Lahir", ["Istana Karier & Harta", "Istana Jodoh & Relasi", "Bintang Utama Diri"],
               "Rincian per bidang kehidupan yang sangat spesifik untuk perencanaan jangka panjang.",
               "Terlalu fokus pada istana yang 'lemah' sehingga lupa memaksimalkan yang kuat."),
    "Human Design": ("Tipe energi bawaan dan cara alami kamu mengambil keputusan.",
                     "Perpaduan astrologi, I Ching, dan chakra yang menghasilkan bodygraph: tipe, strategi, dan otoritas pengambilan keputusan pribadi.",
                     "Tanggal, Jam & Kota Lahir", ["Tipe Energi Alami", "Cara Terbaik Memutuskan", "Peran dalam Tim"],
                     "Menemukan ritme kerja yang selaras dengan energimu, bukan meniru orang lain.",
                     "Menggunakan 'itu bukan tipeku' sebagai alasan menghindari hal yang perlu dipelajari."),
    "Golongan Darah": ("Kecenderungan sifat dasar menurut golongan darah ala Jepang dan Korea.",
                       "Pembacaan populer yang mengaitkan A, B, AB, dan O dengan gaya bersikap, bekerja, dan berelasi. Ringan dan mudah dibahas bareng teman.",
                       "Golongan Darah", ["Kecenderungan Sifat Bawaan", "Cara Menghadapi Masalah", "Kecocokan Antar-Golongan"],
                       "Pintu masuk santai untuk mulai mengenali kebiasaan dan gaya bersikapmu.",
                       "Menganggapnya fakta ilmiah padahal lebih tepat sebagai bahan refleksi."),
    "Tarot": ("Cermin simbolik untuk membaca situasi dan pilihanmu saat ini.",
              "78 kartu (Major & Minor Arcana) dengan simbol yang dibaca sebagai refleksi kondisi batin, peluang, dan nasihat untuk langkah berikutnya.",
              "Kartu yang Terbuka", ["Makna Posisi Kartu", "Nasihat Utama", "Karier, Rezeki & Asmara"],
              "Sudut pandang baru saat bingung memilih, plus pertanyaan reflektif untuk dirimu sendiri.",
              "Menyerahkan keputusan pada kartu dan lupa bahwa kamu yang menentukan arah."),
}


def _cat(nama):
    for cat, lit in CATEGORY_SYSTEMS.items():
        if lit and nama in lit:
            return cat.upper()
    return "SISTEM"


def _go_solo(nama):
    from components.solo_reveal import ACTIVE
    from components.mini_modals import request_solo
    if nama in ACTIVE:
        request_solo(nama)
    else:
        request_open("solo", dh_solo_step="dev", dh_solo_sys=nama, dh_solo_err=None)


def open_from_node(nama):
    """on_click node diagram: simpan sistem lalu minta dialog dibuka di run berikutnya."""
    st.session_state.dh_sysinfo = nama
    st.session_state.dh_open_dialog = "sysinfo"


@st.dialog("Detail Sistem", width="large")
def sysinfo_dialog():
    nama = st.session_state.get("dh_sysinfo")
    if nama not in _INFO:
        st.rerun()
        return
    quote, desc, src, bullets, potensi, buta = _INFO[nama]
    no = [n for n, _ in NODE_ORDER].index(nama) + 1
    bl = "".join(f"<li>{b}</li>" for b in bullets)
    st.markdown(
        f'<div class="dh-step dh-step-mini dh-step-sysinfo"></div>'
        f'<div class="dh-si-eyebrow">SISTEM #{no} · {_cat(nama)}</div>'
        f'<div class="dh-si-title">{nama}</div>'
        f'<div class="dh-si-quote">&ldquo;{quote}&rdquo;</div>'
        f'<div class="dh-si-desc">{desc}</div>'
        f'<div class="dh-si-lbl">SUMBER DATA MASUKAN</div><div class="dh-si-src">{src}</div>'
        f'<div class="dh-si-lbl">APA YANG DIPETAKAN</div><ul class="dh-si-list">{bl}</ul>'
        f'<div class="dh-si-cards"><div class="dh-si-card dh-si-good"><b>POTENSI UTAMA</b><p>{potensi}</p></div>'
        f'<div class="dh-si-card dh-si-shadow"><b>TITIK BUTA (SHADOW)</b><p>{buta}</p></div></div>',
        unsafe_allow_html=True)
    c1, c2 = st.columns([1, 2], gap="small")
    with c1:
        if st.button("Tutup", key="dhsi_close", use_container_width=True):
            st.session_state.pop("dh_sysinfo", None)
            st.rerun()
    with c2:
        if st.button(f"Hitung {nama} Milikku →", key="dhsi_go", type="primary", use_container_width=True):
            _go_solo(nama)


DIALOGS = {"sysinfo": sysinfo_dialog}
