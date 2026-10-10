"""
Destiny Reveal — entry point Streamlit app.
Homepage + preview layout form. Isi/logic ditambahin pelan-pelan dari sini.
"""

from pathlib import Path

import streamlit as st

from views import home_v2

st.set_page_config(
    page_title="Destiny Reveal",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Custom CSS ──────────────────────────────────────────────
st.markdown(
    '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />'
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,wght@0,500;0,600;0,700;1,500&family=Plus+Jakarta+Sans:ital,wght@0,300..800;1,300..800&family=Lora:ital,wght@0,400..700;1,400..700&family=Playfair+Display:ital,wght@0,400..900;1,400..900&display=swap">',
    unsafe_allow_html=True,
)
_CSS_PATH = Path(__file__).resolve().parent / "assets" / "css" / "app.css"
_CSS_PARTS_DIR = Path(__file__).resolve().parent / "assets" / "css" / "parts"  # urut nama file (01_, 02_, ...)
_CSS_HOME_V2 = "".join(f.read_text(encoding="utf-8") for f in sorted(_CSS_PARTS_DIR.glob("*.css")))
st.markdown(
    f"<style>\n{_CSS_PATH.read_text(encoding='utf-8')}\n"
    f"{_CSS_HOME_V2}\n</style>",
    unsafe_allow_html=True,
)

# ── Data sistem lengkap (buat popover chip) — urut abjad ────
# format: (nama, icon_material, apa_ini, [topik yang bisa diketahui], kalimat_ajakan, aktif)
SEMUA_SISTEM = [
    ("BaZi", "account_tree",
     "Sistem astrologi Tiongkok kuno yang membaca empat pilar waktu lahir, yaitu tahun, bulan, tanggal, dan jam, untuk memetakan struktur nasib seseorang secara mendalam.",
     ["Elemen dominan dalam diri", "Potensi rezeki dan karier", "Periode hidup yang perlu diperhatikan"],
     "Banyak yang baru sadar polanya justru dari sisi yang paling sering diabaikan, yaitu jam lahir.", False),
    ("Big Five", "insights",
     "Model kepribadian yang paling banyak divalidasi dalam riset psikologi modern, mengukur lima dimensi utama karakter seseorang secara terukur.",
     ["Tingkat keterbukaan terhadap hal baru", "Cara mengelola emosi", "Gaya bekerja sama dengan orang lain"],
     "Cocok buat kamu yang ingin memahami diri lewat data, bukan sekadar label kepribadian.", False),
    ("DISC", "groups",
     "Model perilaku kerja yang memetakan bagaimana seseorang berkomunikasi, mengambil keputusan, dan merespons tekanan di lingkungan profesional.",
     ["Gaya komunikasi di tempat kerja", "Cara mengambil keputusan", "Reaksi terhadap tekanan"],
     "Sering dipakai perusahaan untuk proses rekrutmen, sekarang kamu bisa coba versi personalnya sendiri.", False),
    ("Enneagram", "category",
     "Sistem sembilan tipe kepribadian yang menelusuri motivasi inti dan ketakutan terdalam di balik setiap perilaku seseorang.",
     ["Motivasi tersembunyi di balik tindakan", "Ketakutan yang memengaruhi pilihan", "Arah berkembang jadi versi terbaik diri"],
     "Kalau kamu sering bertanya kenapa selalu bereaksi dengan cara yang sama, jawabannya mungkin ada di sini.", False),
    ("Golongan Darah", "bloodtype",
     "Pembacaan sifat berdasarkan golongan darah, populer di budaya Jepang dan Korea sebagai cara memahami kecenderungan dasar seseorang.",
     ["Kecenderungan sifat bawaan", "Cara menghadapi masalah", "Kecocokan dengan golongan darah lain"],
     "Terdengar sederhana, tapi banyak orang justru merasa gambarannya paling mengena.", False),
    ("Human Design", "hub",
     "Sistem yang memetakan tipe energi bawaan dan cara alami seseorang dalam mengambil keputusan yang selaras dengan dirinya.",
     ["Tipe energi alami", "Cara terbaik mengambil keputusan", "Peran dalam kelompok atau tim"],
     "Cocok buat kamu yang lelah memaksakan cara kerja orang lain ke dalam ritme hidupmu sendiri.", False),
    ("Love Language", "favorite",
     "Konsep lima bahasa kasih yang menjelaskan cara seseorang paling nyaman menerima dan menyampaikan perhatian dalam suatu hubungan.",
     ["Cara paling nyaman menerima kasih sayang", "Cara menyampaikan perhatian ke orang lain", "Potensi kesalahpahaman dalam hubungan"],
     "Pahami ini, dan komunikasi dengan orang terdekatmu bisa terasa jauh lebih lancar.", False),
    ("Matrix Destiny", "grid_view",
     "Peta numerologi menyeluruh dari tanggal lahir yang menggambarkan kepribadian, arah rezeki, hubungan, dan pelajaran hidup sekaligus dalam satu diagram.",
     ["Peta kepribadian menyeluruh", "Arah rezeki dan keuangan", "Pelajaran hidup yang dibawa sejak lahir"],
     "Satu peta yang merangkum hampir semua sisi hidupmu hanya dari satu tanggal lahir.", False),
    ("MBTI", "psychology",
     "Salah satu tes kepribadian paling dikenal secara global, membagi cara berpikir dan bekerja seseorang ke dalam enam belas tipe.",
     ["Gaya berpikir dan memproses informasi", "Cara bekerja yang paling efektif", "Kecocokan dengan tipe kepribadian lain"],
     "Tes yang paling sering jadi bahan obrolan, sekarang saatnya lihat versi yang lebih lengkap.", False),
    ("Numerologi", "tag",
     "Ilmu penafsiran angka dari tanggal lahir dan nama untuk membaca arah hidup dan pola yang berulang pada diri seseorang.",
     ["Jalan hidup utama", "Angka keberuntungan pribadi", "Tantangan yang cenderung berulang"],
     "Angka lahir dan namamu ternyata menyimpan pola yang jarang disadari sebelumnya.", False),
    ("Shio", "pets",
     "Astrologi Tiongkok berdasarkan siklus dua belas hewan yang menggambarkan sifat, elemen bawaan, dan peruntungan tahunan seseorang.",
     ["Sifat dan elemen bawaan lahir", "Peruntungan tahun berjalan", "Kecocokan dengan shio lain"],
     "Dipercaya turun-temurun, tapi jarang dibaca sampai ke elemen dan peruntungan tahunannya.", False),
    ("Tarot", "style",
     "Pembacaan simbolis melalui kartu yang merepresentasikan arketipe jiwa dan pelajaran hidup yang sedang dijalani seseorang saat ini.",
     ["Arketipe jiwa yang mewakili dirimu", "Pelajaran hidup yang sedang dijalani", "Energi yang sedang berlangsung"],
     "Bukan soal menebak masa depan, tapi mengenali energi yang sedang kamu jalani sekarang.", False),
    ("Weton", "calendar_today",
     "Perhitungan tradisi Jawa yang menggabungkan hari kelahiran dan siklus pasaran untuk membaca watak bawaan dan hari baik.",
     ["Watak bawaan lahir menurut tradisi Jawa", "Hari baik untuk momen penting", "Neptu dan maknanya"],
     "Sistem asli Indonesia yang masih dipakai untuk menentukan hari baik sampai sekarang.", False),
    ("Zi Wei", "auto_awesome",
     "Astrologi bintang ungu dari Tiongkok yang memetakan dua belas istana kehidupan berdasarkan posisi bintang saat lahir.",
     ["Peta dua belas istana kehidupan", "Potensi karier dan jodoh", "Periode baik dalam siklus hidup"],
     "Lebih detail dibanding astrologi Barat, karena memetakan dua belas sisi kehidupan sekaligus.", False),
    ("Zodiak", "star",
     "Astrologi Barat yang membaca karakter dasar seseorang dari posisi matahari terhadap salah satu dari dua belas rasi bintang saat lahir.",
     ["Karakter dasar dan elemen", "Gaya emosi dan cara merespons", "Kecocokan dengan zodiak lain"],
     "Sistem yang paling familiar, tapi baru terasa lengkap kalau digabung dengan sistem lain.", True),
]

# ── NAVIGASI HALAMAN ────────────────────────────────────────
# Cuma ada satu halaman (Home). Alur Reveal berjalan di modal "Reveal Dirimu".
if "dr_page" not in st.session_state:
    st.session_state.dr_page = "home"

# ── NAV BAR (v2, lihat views/home_v2.py — dipakai semua halaman) ──
# Navbar-nya position:fixed (biar freeze pas discroll), jadi butuh spacer
# di bawahnya biar konten halaman ga ketutupan.
home_v2.render_navbar(st.session_state.dr_page)
st.markdown('<div style="height:88px;"></div>', unsafe_allow_html=True)

if st.session_state.get("dh_toast"):
    st.toast(st.session_state.pop("dh_toast"), icon="✨")

# Halaman lain (reveal, tutorial, loading, hasil) sudah diganti modal "Reveal Dirimu" di Home.
# Nilai dr_page apa pun yang tidak dikenal jatuh ke Home.
home_v2.render(SEMUA_SISTEM)
