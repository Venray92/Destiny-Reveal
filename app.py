"""
Destiny Reveal — entry point Streamlit app.
Homepage + preview layout form. Isi/logic ditambahin pelan-pelan dari sini.
"""

from pathlib import Path

import streamlit as st

from views.reveal_yourself import render as render_reveal_yourself
from views.loadingpage import render as render_loading
from views.loadingpage_lengkap import render as render_loading_lengkap
from views.loadingpage_mendalam import render as render_loading_mendalam
from views.revealpage import render as render_result
from views.tutorialpage import render as render_tutorial

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
    '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,wght@0,500;0,600;0,700;1,500&family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Lora:ital,wght@0,400;0,500;1,400&display=swap">',
    unsafe_allow_html=True,
)
_CSS_PATH = Path(__file__).resolve().parent / "assets" / "css" / "app.css"
st.markdown(f"<style>\n{_CSS_PATH.read_text(encoding='utf-8')}\n</style>", unsafe_allow_html=True)

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
# Bukan st.tabs — st.tabs nggak bisa dipindah programatis lewat klik tombol
# lain (misal tombol "Mulai Reveal" di hero). Jadi navigasi antar
# "halaman" (Beranda / Reveal Yourself) dipegang manual lewat
# st.session_state, dan konten dirender bergantian pakai if/else biasa.
if "dr_page" not in st.session_state:
    st.session_state.dr_page = "home"

# ── NAV BAR ──────────────────────────────────────────────────
with st.container(key="nav_row"):
    nav_l, nav_home_btn, nav_reveal_btn, nav_tutorial_btn, nav_r = st.columns(
        [2.5, 0.95, 1.35, 1.05, 1.15]
    )
    with nav_l:
        st.markdown(
            '<div style="font-family:\'Fraunces\',serif;font-size:28px;font-weight:700;'
            'color:#1c1a17;letter-spacing:-0.01em;">✨ Destiny Reveal</div>',
            unsafe_allow_html=True,
        )
    with nav_home_btn:
        if st.button(
            "Home", key="nav_btn_home", icon=":material/home:",
            type="primary" if st.session_state.dr_page == "home" else "secondary",
            use_container_width=True,
        ):
            st.session_state.dr_page = "home"
            st.rerun()
    with nav_reveal_btn:
        if st.button(
            "Reveal Yourself", key="nav_btn_reveal", icon=":material/auto_awesome:",
            type="primary" if st.session_state.dr_page == "reveal" else "secondary",
            use_container_width=True,
        ):
            st.session_state.dr_page = "reveal"
            st.rerun()
    with nav_tutorial_btn:
        if st.button(
            "Tutorial", key="nav_btn_tutorial", icon=":material/menu_book:",
            type="primary" if st.session_state.dr_page == "tutorial" else "secondary",
            use_container_width=True,
        ):
            st.session_state.dr_page = "tutorial"
            st.rerun()
    with nav_r:
        with st.container(key="lang_switch"):
            st.selectbox("Bahasa", ["🇮🇩 Indonesian", "🇬🇧 English"], label_visibility="collapsed")

st.markdown("<hr style='margin-top:14px;'>", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# HALAMAN — BERANDA
# ══════════════════════════════════════════════════════════════
if st.session_state.dr_page == "home":

    # ── HERO ─────────────────────────────────────────────────
    st.markdown('<div class="dr-hero-title">Ada Banyak Versi Dirimu yang Belum Kamu Kenal.</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="dr-hero-sub">'
        'Masa lalu sudah menjadi pelajaran, saatnya kenali dirimu sepenuhnya sebelum melangkah ke depan.<br>'
        '<em>Satu pembacaan lengkap</em> dari 15 sistem ini akan menunjukkan potensi, kelebihan, kelemahan, '
        'dan langkah yang sebaiknya kamu ambil.'
        '</div>',
        unsafe_allow_html=True,
    )

    col_a, col_b, col_r = st.columns([1.3, 1.3, 2.4])
    with col_a:
        if st.button("Mulai Reveal", key="cta_hero", type="primary", icon=":material/bolt:", use_container_width=True):
            st.session_state.dr_page = "reveal"
            st.rerun()

    st.write("")
    st.markdown('<p style="font-size:12.5px;color:#9a948a !important;margin-bottom:6px;">Klik tiap sistem untuk melihat penjelasannya:</p>', unsafe_allow_html=True)

    n_per_row = 5
    for i in range(0, len(SEMUA_SISTEM), n_per_row):
        chunk = SEMUA_SISTEM[i:i + n_per_row]
        cols = st.columns(n_per_row)
        for col, (nama, icon, apa_ini, topik_list, ajakan, aktif) in zip(cols, chunk):
            with col:
                with st.popover(nama, use_container_width=True, icon=f":material/{icon}:"):
                    status_badge = "Sudah aktif" if aktif else "Segera hadir"
                    status_color = "#8a5a2f" if aktif else "#9a948a"
                    st.markdown(
                        f'<p style="font-size:11px;font-weight:700;letter-spacing:0.06em;'
                        f'text-transform:uppercase;color:{status_color} !important;margin-bottom:6px;">{status_badge}</p>',
                        unsafe_allow_html=True,
                    )
                    st.markdown(f"**{nama}**")
                    st.write(apa_ini)
                    st.markdown(
                        '<p style="font-size:12.5px;font-weight:700;color:#3a362f !important;margin:14px 0 4px 0;">Bisa bantu kamu tahu:</p>',
                        unsafe_allow_html=True,
                    )
                    for topik in topik_list:
                        st.markdown(
                            f'<p style="font-size:13px;color:#3a362f !important;margin:2px 0;">'
                            f'<span style="color:#b8562f !important;">•</span> {topik}</p>',
                            unsafe_allow_html=True,
                        )
                    st.markdown(
                        f'<p style="font-size:12.5px;color:#8a5a2f !important;font-style:italic;'
                        f'margin:14px 0 0 0;padding-top:10px;border-top:1px solid #ecddc9;">{ajakan}</p>',
                        unsafe_allow_html=True,
                    )

    st.write("")

    # ── CARA KERJA ───────────────────────────────────────────
    st.markdown('<div class="dr-section-title-wrap"><span class="dr-section-title">Tiga Langkah, Tanpa Ribet</span></div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="dr-stepper-row">
            <div class="dr-step-circle">1</div>
            <div class="dr-step-line"></div>
            <div class="dr-step-circle">2</div>
            <div class="dr-step-line"></div>
            <div class="dr-step-circle">3</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns(3, gap="medium")
    steps = [
        (":material/mail:", "Verifikasi Email", "Masukkan email, dapat kode verifikasi. Tanpa akun atau password.", "dr-step-card-1"),
        (":material/auto_awesome:", "Pilih Mode & Diproses", "Pilih fokus eksplorasimu, data lain ditanya pelan-pelan sambil diproses.", "dr-step-card-2"),
        (":material/visibility:", "Buka Hasil Lengkap", "Laporan lengkap langsung terbuka & dikirim ke email kamu.", "dr-step-card-3"),
    ]
    for idx, (col, (icon, title, desc, cls)) in enumerate(zip([c1, c2, c3], steps)):
        with col:
            with st.container(key=f"drfillheight_step{idx}"):
                st.markdown(
                    f"""<div class="dr-card {cls}">
                        <b>{title}</b>
                        <p style="font-size:13.5px;margin-top:8px;line-height:1.6;">{desc}</p>
                    </div>""",
                    unsafe_allow_html=True,
                )

    st.write("")

    # ── SATU DATA, BANYAK CARA PANDANG ────────────────────────
    st.markdown('<div class="dr-section-title-wrap"><span class="dr-section-title">Satu Data, Banyak Cara Pandang</span></div>', unsafe_allow_html=True)

    # SENGAJA disamain persis (isi + urutan) sama RY_MODES di
    # views/reveal_yourself.py (mode Lengkap) — lihat docs/changelog.md.
    bulk_groups = [
        ("calendar_month", "Tanggal Lahir & Nama Lengkap", ["Zodiak", "Shio", "Weton", "Numerologi", "Matrix Destiny"], None),
        ("schedule", "+ Tambah Jam Lahir", ["BaZi", "Zi Wei Dou Shu", "Human Design"], "BaZi & Human Design makin akurat kalau ditambah kota lahir."),
        ("quiz", "Kuesioner", ["MBTI", "Big Five", "Enneagram", "DISC", "Love Language"], None),
        ("water_drop", "Input Langsung", ["Golongan Darah"], None),
        ("casino", "Acak", ["Tarot"], None),
    ]
    bcols = st.columns(5, gap="medium")
    for idx, (col, (icon, title, items, note)) in enumerate(zip(bcols, bulk_groups)):
        with col:
            with st.container(key=f"drfillheight_bulk{idx}"):
                tags_html = "".join(f'<span class="dr-bulk-tag">{x}</span>' for x in items)
                note_html = (
                    f'<div class="dr-bulk-note">{note}</div>' if note else ""
                )
                # Digabung lewat concatenation (BUKAN f-string multi-baris
                # kayak sebelumnya) — kalau note_html kosong ("") dan
                # ditaruh di baris sendiri di f-string, baris itu jadi
                # cuma whitespace doang, ke-anggap "baris kosong" sama
                # parser markdown Streamlit, jadi HTML block-nya keputus
                # duluan SEBELUM closing </div> — akibatnya </div> penutup
                # kartu kebaca sebagai teks literal (bukan tag beneran).
                # Concatenation biasa nggak punya masalah ini karena semua
                # nyambung jadi SATU baris string, gak ada baris kosong
                # sama sekali di HTML akhirnya.
                st.markdown(
                    '<div class="dr-bulk-card">'
                    f'<div class="dr-bulk-icon"><span class="material-symbols-outlined">{icon}</span></div>'
                    f'<b style="font-size:14.5px;">{title}</b>'
                    f'<div class="dr-bulk-tags-wrap" style="margin-top:10px;">{tags_html}</div>'
                    f'{note_html}'
                    '</div>',
                    unsafe_allow_html=True,
                )

    st.write("")

    # ── CTA PENUTUP ──────────────────────────────────────────
    # Sengaja tanpa st.write("") kosong di sini — tiap st.write("") nambah
    # elemen container-nya sendiri, dan gap antar stVerticalBlock (1rem) ikut
    # kekali tiap ada elemen kosong tambahan, jadi jaraknya membengkak jauh
    # lebih besar dari yang kelihatan di kode. Jarak sekarang cuma diatur
    # lewat margin di <hr>-nya sendiri.
    st.markdown("<hr style='margin-top:4px;margin-bottom:20px;'>", unsafe_allow_html=True)
    st.markdown('<div class="dr-center"><span class="dr-section-title">Penasaran Sama Dirimu Sendiri?</span></div>', unsafe_allow_html=True)
    st.markdown(
        '<p class="dr-center" style="color:#6b6459 !important;font-size:15px;margin-bottom:22px;">Mulai sekarang, hasil pertama muncul dalam hitungan menit.</p>',
        unsafe_allow_html=True,
    )
    cta_l, cta_mid, cta_r = st.columns([1.5, 1.4, 1.5])
    with cta_mid:
        if st.button("Mulai Reveal Gratis", key="cta_footer", type="primary", icon=":material/arrow_forward:", use_container_width=True):
            st.session_state.dr_page = "reveal"
            st.rerun()

    st.write("")
    st.markdown(
        '<p class="dr-footer-copyright">© 2026 Destiny Reveal '
        '<span class="dr-footer-byline">· By Zio</span></p>',
        unsafe_allow_html=True,
    )

# ══════════════════════════════════════════════════════════════
# HALAMAN — REVEAL YOURSELF (Verifikasi Email + Pilih Mode)
# ══════════════════════════════════════════════════════════════
elif st.session_state.dr_page == "reveal":
    render_reveal_yourself()

# ══════════════════════════════════════════════════════════════
# HALAMAN — TUTORIAL (penjelasan semua sistem/chip)
# ══════════════════════════════════════════════════════════════
elif st.session_state.dr_page == "tutorial":
    render_tutorial(SEMUA_SISTEM)

# ══════════════════════════════════════════════════════════════
# HALAMAN — LOADING (proses per-titik, floating window minta data)
# ══════════════════════════════════════════════════════════════
elif st.session_state.dr_page == "loading":
    render_loading()

# ══════════════════════════════════════════════════════════════
# HALAMAN — LOADING PAGE 2 (Mode Mendalam: kuesioner MBTI/Big Five/
# Enneagram/DISC/Love Language, 1 soal per layar)
# ══════════════════════════════════════════════════════════════
elif st.session_state.dr_page == "loading_mendalam":
    render_loading_mendalam()

# ══════════════════════════════════════════════════════════════
# HALAMAN — LOADING PAGE 3 (Mode Lengkap: semua 15 sistem, form
# intake sekaligus di awal + animasi 10 titik data, lalu lepas ke
# Loading Page 2 buat 5 sistem kuesioner)
# ══════════════════════════════════════════════════════════════
elif st.session_state.dr_page == "loading_lengkap":
    render_loading_lengkap()

# ══════════════════════════════════════════════════════════════
# HALAMAN — HASIL AKHIR (stub, belum dibuat penuh)
# ══════════════════════════════════════════════════════════════
else:
    render_result()
