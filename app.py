"""
Destiny Reveal — entry point Streamlit app.
Homepage + preview layout form. Isi/logic ditambahin pelan-pelan dari sini.
"""

import streamlit as st

try:
    from engine.zodiak import hitung_zodiak
    ZODIAK_ENGINE_READY = True
except ImportError:
    ZODIAK_ENGINE_READY = False

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
st.markdown(
    """
    <style>
    #MainMenu, footer, header {visibility: hidden;}

    .material-symbols-outlined {
        font-family: 'Material Symbols Outlined';
        font-weight: normal; font-style: normal; font-size: 24px; line-height: 1;
        letter-spacing: normal; text-transform: none; display: inline-block;
        white-space: nowrap; word-wrap: normal; direction: ltr;
        -webkit-font-smoothing: antialiased;
    }

    .dr-font-display { font-family: 'Fraunces', serif !important; }
    .dr-font-reading { font-family: 'Lora', serif !important; }

    /* Sembunyikan panah dropdown bawaan di tombol popover chip sistem —
       beberapa selector dipasang sekaligus karena struktur DOM-nya bisa beda
       antar versi Streamlit */
    div[data-testid="stPopover"] svg:not([data-testid="stIconMaterial"] svg) { display: none !important; }
    div[data-testid="stPopover"] button svg:last-child { display: none !important; }
    div[data-testid="stPopover"] button::after { content: none !important; }
    div[data-testid="stPopover"] button [data-testid="stIconMaterial"] { display: inline-flex !important; }

    /* Paksa panel popover selalu terang, apapun tema browser/sistemnya —
       sebelumnya panel ini ikut dark-mode sehingga teks gelap jadi tak kebaca */
    div[data-testid="stPopoverBody"],
    div[data-baseweb="popover"] div[role="tooltip"],
    div[data-baseweb="popover"] > div {
        background-color: #ffffff !important;
        color: #1c1a17 !important;
    }
    div[data-testid="stPopoverBody"] * ,
    div[data-baseweb="popover"] div[role="tooltip"] * {
        color: inherit;
    }

    /* Kolom Streamlit auto-stretch tinggi sesuai isi paling tinggi */
    [data-testid="stHorizontalBlock"] { align-items: stretch !important; }
    [data-testid="column"] { display: flex !important; flex-direction: column !important; }
    [data-testid="column"] > div { height: 100%; }

    .stApp { background-color: #ffffff; }
    .block-container { padding-top: 2rem; padding-bottom: 3rem; max-width: 1360px; }

    .stApp, .stApp p, .stApp span, .stApp div, .stApp b, .stApp li,
    .stApp label, .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5,
    .stMarkdown, .stMarkdown p {
        color: #1c1a17;
    }
    .stApp { font-family: 'Plus Jakarta Sans', -apple-system, sans-serif; }

    .dr-center { text-align: center; }

    .dr-badge {
        display: inline-flex; align-items: center; gap: 6px;
        padding: 7px 16px; border: 1px solid #ecddc9; border-radius: 100px;
        font-size: 13px; color: #8a5a2f !important; background: #fdf3e7;
        margin-bottom: 22px;
    }
    .dr-hero-title {
        font-family: 'Fraunces', serif;
        font-size: 42px; font-weight: 700; line-height: 1.25;
        margin: 0 0 22px 0; letter-spacing: -0.01em; color: #1c1a17 !important;
        text-align: left;
    }
    .dr-hero-sub {
        font-size: 18px; line-height: 1.75; color: #5c564d !important;
        max-width: 680px; margin: 0 0 30px 0; text-align: left;
    }
    .dr-hero-sub em { color: #b8562f !important; font-style: normal; font-weight: 600; }
    .dr-section-title-wrap { margin-bottom: 26px; }
    .dr-section-title {
        font-family: 'Fraunces', serif; font-size: 28px; font-weight: 700;
        color: #1c1a17 !important; margin: 0; text-align: left; display: inline-block;
        position: relative; padding-bottom: 12px;
    }
    .dr-section-title::after {
        content: ""; position: absolute; left: 0; bottom: 0;
        width: 48px; height: 3px; border-radius: 3px; background: #b8562f;
    }
    .dr-card {
        padding: 24px; border-radius: 16px; background: #ffffff;
        height: 100%; box-sizing: border-box;
        border: 2px solid #ece6dc;
    }
    .dr-card b { color: #1c1a17 !important; font-size: 15.5px; }
    .dr-card p { color: #6b6459 !important; }

    /* Stepper cara kerja */
    .dr-stepper-row { display: flex; align-items: center; margin-bottom: 18px; max-width: 640px; margin-left: auto; margin-right: auto; }
    .dr-step-circle {
        width: 46px; height: 46px; border-radius: 50%; background: #b8562f;
        color: #ffffff !important; display: flex; align-items: center; justify-content: center;
        font-weight: 800; font-size: 17px; flex-shrink: 0;
    }
    .dr-step-line { flex: 1; height: 3px; background: #ecddc9; margin: 0 10px; border-radius: 3px; }
    .dr-step-card-1, .dr-step-card-2, .dr-step-card-3 { border-color: #e4ddd0 !important; }

    /* Chip popover (sistem kecil di hero) */
    div[data-testid="stPopover"] button {
        border-radius: 100px !important; background: #f6f1e9 !important;
        border: 1px solid #ecddc9 !important; font-size: 12.5px !important; font-weight: 600 !important;
        color: #5c564d !important; padding: 5px 14px !important; min-height: 0 !important;
    }
    div[data-testid="stPopover"] button:hover {
        background: #ecddc9 !important; color: #8a5a2f !important;
    }

    /* Kartu bulk kategori */
    .dr-bulk-card {
        padding: 22px 24px; border-radius: 16px; background: #fbf8f3;
        border: 2px solid #ece6dc; height: 100%; box-sizing: border-box;
        display: flex; flex-direction: column; align-items: center; text-align: center;
    }
    .dr-bulk-icon {
        width: 44px; height: 44px; border-radius: 12px; background: #fdf3e7;
        display: flex; align-items: center; justify-content: center; margin-bottom: 12px;
        color: #b8562f !important; flex-shrink: 0;
    }
    .dr-bulk-tags-wrap { display: flex; flex-wrap: wrap; justify-content: center; gap: 6px; }
    .dr-bulk-tag {
        display: inline-block; padding: 6px 13px; border-radius: 100px;
        background: #ffffff; border: 1px solid #e4ddd0; color: #1c1a17 !important;
        font-size: 12.5px; font-weight: 600;
    }

    .dr-result-card {
        border: 2px solid #ecddc9; border-radius: 18px; overflow: hidden;
        box-shadow: 0 20px 50px -22px rgba(139,90,47,0.25);
    }
    .dr-result-header {
        padding: 18px 26px; background: linear-gradient(135deg, #d9743f, #b8562f);
        color: #ffffff !important; font-size: 14.5px; font-weight: 700;
    }
    .dr-result-header * { color: #ffffff !important; }
    .dr-mini-card {
        padding: 16px 18px; border: 1px solid #ecddc9; border-radius: 12px;
        margin-bottom: 12px; background: #fffdf9;
    }
    .dr-mini-card b { color: #1c1a17 !important; }
    .dr-mini-tag {
        display: inline-block; padding: 5px 13px; border-radius: 100px;
        background: #fdf3e7; color: #8a5a2f !important; font-size: 12.5px; font-weight: 700;
        margin-bottom: 8px;
    }
    .dr-mini-label { font-size: 12px; font-weight: 700; color: #b8562f !important; text-transform: uppercase; letter-spacing: 0.04em; margin-top: 8px; }
    .dr-mini-text { font-family: 'Lora', serif; font-size: 13.5px; color: #3a362f !important; line-height: 1.6; margin: 2px 0 0 0; }

    div.stButton > button[kind="primary"] {
        background: #b8562f; color: #ffffff !important; border: 2px solid #b8562f;
        padding: 14px 32px; border-radius: 10px; font-weight: 700; font-size: 16px;
    }
    div.stButton > button[kind="primary"]:hover { background: #a5482a; border-color: #a5482a; }
    div.stButton > button[kind="secondary"] {
        background: #ffffff; color: #1c1a17 !important; border: 2px solid #e4ddd0;
        padding: 14px 32px; border-radius: 10px; font-weight: 700; font-size: 16px;
    }
    div.stButton > button[kind="secondary"]:hover { border-color: #b8562f; color: #b8562f !important; }

    hr { border-color: #ece6dc !important; }

    .stTextInput input, .stDateInput input, .stTimeInput input,
    .stSelectbox div[data-baseweb="select"] > div {
        border-radius: 8px !important; border-color: #e4ddd0 !important;
    }

    /* Dropdown bahasa di nav: kecil & cream, bukan hitam */
    .st-key-lang_switch { max-width: 130px; margin-left: auto; }
    .st-key-lang_switch div[data-baseweb="select"] > div {
        background: #fdf3e7 !important; border: 1.5px solid #ecddc9 !important;
        border-radius: 100px !important; color: #8a5a2f !important;
        min-height: 38px !important; font-weight: 600 !important;
    }
    .st-key-lang_switch svg { fill: #8a5a2f !important; }

    /* Kontainer Contoh Laporan lebih compact */
    .dr-report-grid { display: grid; grid-template-columns: repeat(2, minmax(0,1fr)); gap: 12px; }
    .dr-report-item { padding: 4px 0; border-bottom: 1px solid #f2ecdf; }
    .dr-report-item:nth-last-child(-n+2) { border-bottom: none; }

    /* Tab (Beranda / Preview Form + Global / Mingguan) jadi pill nav modern */
    [data-testid="stTabs"] [data-baseweb="tab-list"] {
        gap: 10px !important; background: #fbf8f3; padding: 8px; border-radius: 100px;
        border: 1px solid #ece6dc; display: inline-flex !important; width: auto !important;
    }
    [data-testid="stTabs"] button[role="tab"] {
        border: 1.5px solid transparent !important;
        border-radius: 100px !important;
        padding: 10px 24px !important;
        font-size: 14.5px !important;
        font-weight: 700 !important;
        color: #6b6459 !important;
        background: transparent !important;
        transition: all 0.15s ease;
    }
    [data-testid="stTabs"] button[role="tab"] p { font-weight: 700 !important; }
    [data-testid="stTabs"] button[role="tab"]:hover {
        border-color: #ecddc9 !important; color: #b8562f !important;
    }
    [data-testid="stTabs"] button[role="tab"][aria-selected="true"] {
        border-color: #b8562f !important;
        background: #ffffff !important;
        color: #b8562f !important;
        box-shadow: 0 0 0 3px rgba(184,86,47,0.12), 0 4px 14px -4px rgba(184,86,47,0.35);
    }
    [data-testid="stTabs"] [data-baseweb="tab-highlight"] { display: none; }
    [data-testid="stTabs"] [data-baseweb="tab-border"] { display: none; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ── Data sistem lengkap (buat popover chip) — urut abjad ────
# format: (nama, icon_material, apa_ini, [topik yang bisa diketahui], aktif)
SEMUA_SISTEM = [
    ("BaZi", "account_tree",
     "Sistem astrologi Tiongkok kuno yang membaca empat pilar waktu lahir, yaitu tahun, bulan, tanggal, dan jam, untuk memetakan struktur nasib seseorang.",
     ["Elemen dominan dalam diri", "Potensi rezeki dan karier", "Periode hidup yang perlu diperhatikan"], False),
    ("Big Five", "insights",
     "Model kepribadian yang paling banyak divalidasi dalam riset psikologi modern, mengukur lima dimensi utama karakter seseorang.",
     ["Tingkat keterbukaan terhadap hal baru", "Cara mengelola emosi", "Gaya bekerja sama dengan orang lain"], False),
    ("DISC", "groups",
     "Model perilaku kerja yang memetakan bagaimana seseorang berkomunikasi, mengambil keputusan, dan merespons tekanan di lingkungan profesional.",
     ["Gaya komunikasi di tempat kerja", "Cara mengambil keputusan", "Reaksi terhadap tekanan"], False),
    ("Enneagram", "category",
     "Sistem sembilan tipe kepribadian yang menelusuri motivasi inti dan ketakutan terdalam di balik setiap perilaku.",
     ["Motivasi tersembunyi di balik tindakan", "Ketakutan yang memengaruhi pilihan", "Arah berkembang jadi versi terbaik diri"], False),
    ("Golongan Darah", "bloodtype",
     "Pembacaan sifat berdasarkan golongan darah, populer di budaya Jepang dan Korea sebagai cara memahami kecenderungan dasar seseorang.",
     ["Kecenderungan sifat bawaan", "Cara menghadapi masalah", "Kecocokan dengan golongan darah lain"], False),
    ("Human Design", "hub",
     "Sistem yang memetakan tipe energi bawaan dan cara alami seseorang dalam mengambil keputusan yang selaras dengan dirinya.",
     ["Tipe energi alami", "Cara terbaik mengambil keputusan", "Peran dalam kelompok atau tim"], False),
    ("Love Language", "favorite",
     "Konsep lima bahasa kasih yang menjelaskan cara seseorang paling nyaman menerima dan menyampaikan perhatian dalam suatu hubungan.",
     ["Cara paling nyaman menerima kasih sayang", "Cara menyampaikan perhatian ke orang lain", "Potensi kesalahpahaman dalam hubungan"], False),
    ("Matrix Destiny", "grid_view",
     "Peta numerologi menyeluruh dari tanggal lahir yang menggambarkan kepribadian, arah rezeki, hubungan, dan pelajaran hidup sekaligus.",
     ["Peta kepribadian menyeluruh", "Arah rezeki dan keuangan", "Pelajaran hidup yang dibawa sejak lahir"], False),
    ("MBTI", "psychology",
     "Salah satu tes kepribadian paling dikenal, membagi cara berpikir dan bekerja seseorang ke dalam enam belas tipe.",
     ["Gaya berpikir dan memproses informasi", "Cara bekerja yang paling efektif", "Kecocokan dengan tipe kepribadian lain"], False),
    ("Numerologi", "tag",
     "Ilmu penafsiran angka dari tanggal lahir dan nama untuk membaca arah hidup dan pola yang berulang pada diri seseorang.",
     ["Jalan hidup utama", "Angka keberuntungan pribadi", "Tantangan yang cenderung berulang"], False),
    ("Shio", "pets",
     "Astrologi Tiongkok berdasarkan siklus dua belas hewan yang menggambarkan sifat, elemen bawaan, dan peruntungan tahunan.",
     ["Sifat dan elemen bawaan lahir", "Peruntungan tahun berjalan", "Kecocokan dengan shio lain"], False),
    ("Tarot", "style",
     "Pembacaan simbolis melalui kartu yang merepresentasikan arketipe jiwa dan pelajaran hidup yang sedang dijalani seseorang.",
     ["Arketipe jiwa yang mewakili dirimu", "Pelajaran hidup yang sedang dijalani", "Energi yang sedang berlangsung"], False),
    ("Weton", "calendar_today",
     "Perhitungan tradisi Jawa yang menggabungkan hari kelahiran dan siklus pasaran untuk membaca watak bawaan dan hari baik.",
     ["Watak bawaan lahir menurut tradisi Jawa", "Hari baik untuk momen penting", "Neptu dan maknanya"], False),
    ("Zi Wei", "auto_awesome",
     "Astrologi bintang ungu dari Tiongkok yang memetakan dua belas istana kehidupan berdasarkan posisi bintang saat lahir.",
     ["Peta dua belas istana kehidupan", "Potensi karier dan jodoh", "Periode baik dalam siklus hidup"], False),
    ("Zodiak", "star",
     "Astrologi Barat yang membaca karakter dasar seseorang dari posisi matahari terhadap salah satu dari dua belas rasi bintang saat lahir.",
     ["Karakter dasar dan elemen", "Gaya emosi dan cara merespons", "Kecocokan dengan zodiak lain"], True),
]

# ── NAV ──────────────────────────────────────────────────────
nav_l, nav_r = st.columns([5, 1])
with nav_l:
    st.markdown(
        '<div style="font-family:\'Fraunces\',serif;font-size:28px;font-weight:700;'
        'color:#1c1a17;padding-top:4px;letter-spacing:-0.01em;">✨ Destiny Reveal</div>',
        unsafe_allow_html=True,
    )
with nav_r:
    with st.container(key="lang_switch"):
        st.selectbox("Bahasa", ["🇮🇩 ID", "🇬🇧 EN"], label_visibility="collapsed")

st.markdown("<hr style='margin-top:14px;'>", unsafe_allow_html=True)

tab_home, tab_form = st.tabs([":material/home: Beranda", ":material/edit_note: Preview Form Screening"])

# ══════════════════════════════════════════════════════════════
# TAB 1 — BERANDA
# ══════════════════════════════════════════════════════════════
with tab_home:

    # ── HERO ─────────────────────────────────────────────────
    st.markdown('<span class="dr-badge">✧ 15 sistem pembacaan diri, 1 laporan personal</span>', unsafe_allow_html=True)
    st.markdown('<div class="dr-hero-title">Sudah Tahu Zodiakmu?<br>Itu Baru Permukaan.</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="dr-hero-sub">'
        'Isi data sekali, 15 sistem pembacaan digabung jadi satu laporan.<br>'
        'Bukan sekadar label, tapi jawaban untuk <em>"Lalu, apa yang sebaiknya aku lakukan?"</em>'
        '</div>',
        unsafe_allow_html=True,
    )

    col_a, col_b, col_r = st.columns([1.3, 1.3, 2.4])
    with col_a:
        st.button("Mulai Eksplorasi", key="cta_hero", type="primary", icon=":material/bolt:", use_container_width=True)
    with col_b:
        st.button("Lihat Contoh Hasil", key="cta_hero_secondary", type="secondary", icon=":material/visibility:", use_container_width=True)

    st.write("")
    st.markdown('<p style="font-size:12.5px;color:#9a948a !important;margin-bottom:6px;">Klik tiap sistem untuk melihat penjelasannya:</p>', unsafe_allow_html=True)

    n_per_row = 5
    for i in range(0, len(SEMUA_SISTEM), n_per_row):
        chunk = SEMUA_SISTEM[i:i + n_per_row]
        cols = st.columns(n_per_row)
        for col, (nama, icon, apa_ini, topik_list, aktif) in zip(cols, chunk):
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

    st.write("")
    st.write("")
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
        (":material/edit_note:", "Isi Data & Pilih Fokus", "Nama, tanggal & jam lahir, lalu pilih fokus eksplorasimu.", "dr-step-card-2"),
        (":material/auto_awesome:", "Buka Hasil Lengkap", "Laporan lengkap langsung terbuka & dikirim ke email kamu.", "dr-step-card-3"),
    ]
    for col, (icon, title, desc, cls) in zip([c1, c2, c3], steps):
        with col:
            st.markdown(
                f"""<div class="dr-card {cls}">
                    <b>{title}</b>
                    <p style="font-size:13.5px;margin-top:8px;line-height:1.6;">{desc}</p>
                </div>""",
                unsafe_allow_html=True,
            )

    st.write("")
    st.write("")
    st.write("")

    # ── SATU DATA, BANYAK CARA PANDANG ────────────────────────
    st.markdown('<div class="dr-section-title-wrap"><span class="dr-section-title">Satu Data, Banyak Cara Pandang</span></div>', unsafe_allow_html=True)

    bulk_groups = [
        ("calendar_month", "Cuma dari Tanggal Lahir", ["Zodiak", "Shio", "Weton", "Numerologi", "Matrix Destiny"]),
        ("schedule", "+ Tambah Jam Lahir", ["BaZi (4 Pilar)", "Zi Wei Dou Shu", "Human Design", "Ascendant Zodiak"]),
        ("location_on", "+ Tambah Kota Lahir", ["BaZi Akurat Penuh", "Human Design Akurat Penuh"]),
        ("quiz", "Kuesioner Terpisah", ["MBTI", "Big Five", "Enneagram", "DISC", "Golongan Darah", "Love Language"]),
    ]
    bcols = st.columns(4, gap="medium")
    for col, (icon, title, items) in zip(bcols, bulk_groups):
        with col:
            tags_html = "".join(f'<span class="dr-bulk-tag">{x}</span>' for x in items)
            st.markdown(
                f"""<div class="dr-bulk-card">
                    <div class="dr-bulk-icon"><span class="material-symbols-outlined">{icon}</span></div>
                    <b style="font-size:14.5px;">{title}</b>
                    <div class="dr-bulk-tags-wrap" style="margin-top:10px;">{tags_html}</div>
                </div>""",
                unsafe_allow_html=True,
            )

    st.write("")
    st.write("")
    st.write("")

    # ── CONTOH LAPORAN — Global vs Mingguan ──────────────────
    st.markdown('<div class="dr-section-title-wrap"><span class="dr-section-title">Ini yang Kamu Dapat</span></div>', unsafe_allow_html=True)

    st.markdown('<div class="dr-result-card">', unsafe_allow_html=True)
    st.markdown('<div class="dr-result-header">✨ Contoh Laporan Personal</div>', unsafe_allow_html=True)

    with st.container():
        st.markdown('<div style="padding:22px 26px 6px 26px;">', unsafe_allow_html=True)
        tab_global, tab_mingguan = st.tabs([":material/public: Baca Global (Seumur Hidup)", ":material/calendar_month: Baca Minggu Ini"])

        with tab_global:
            hasil_global = [
                ("Zodiak: Aries",
                 "Aries dikenal sebagai zodiak dengan energi awal yang besar. Kamu cenderung bergerak cepat begitu sebuah ide muncul, dan sering merasa lebih hidup di fase memulai sesuatu yang baru dibandingkan menyelesaikannya perlahan-lahan.",
                 "Manfaatkan dorongan awal ini untuk memulai proyek atau langkah besar, tapi imbangi dengan sistem kecil yang membuatmu tetap konsisten, misalnya checklist mingguan, supaya semangat di awal tidak berhenti di tengah jalan."),
                ("Shio: Kuda",
                 "Shio Kuda punya elemen yang selaras dengan kebebasan dan pergerakan. Kamu biasanya cepat beradaptasi saat berpindah lingkungan, dan mudah merasa terkekang kalau harus terus berada dalam rutinitas yang sama setiap hari.",
                 "Cari peran kerja atau aktivitas yang memberi ruang gerak dan variasi, karena kamu justru akan lebih produktif ketika tidak dipaksa berada dalam satu pola yang kaku sepanjang waktu."),
                ("Weton: Jumat Legi",
                 "Weton Jumat Legi membawa neptu 11, kombinasi yang dalam tradisi Jawa dikaitkan dengan kepekaan sosial yang tinggi. Kamu cenderung mudah membaca suasana hati orang lain dan sering dipercaya sebagai tempat bercerita.",
                 "Manfaatkan kemampuan ini sebagai jembatan komunikasi dalam tim atau keluarga, terutama saat ada gesekan yang membutuhkan penengah yang bisa dipercaya oleh kedua belah pihak."),
                ("Life Path: 7",
                 "Angka jalan hidup 7 dalam numerologi identik dengan sisi reflektif dan pencarian makna yang lebih dalam. Kamu biasanya butuh waktu sendiri dahulu sebelum benar-benar yakin mengambil keputusan besar.",
                 "Beri diri kamu jeda, misalnya semalam, sebelum memutuskan hal penting, meskipun ada dorongan untuk langsung bertindak begitu insting muncul."),
            ]
            items_html = "".join(
                f"""<div class="dr-report-item">
                    <span class="dr-mini-tag">{tag}</span>
                    <div class="dr-mini-label">Makna</div>
                    <p class="dr-mini-text">{makna}</p>
                    <div class="dr-mini-label">Saran</div>
                    <p class="dr-mini-text">{aksi}</p>
                </div>"""
                for tag, makna, aksi in hasil_global
            )
            st.markdown(f'<div class="dr-mini-card"><div class="dr-report-grid">{items_html}</div></div>', unsafe_allow_html=True)
            st.markdown(
                '<p style="font-size:12.5px;color:#9a948a !important;">Ini contoh dummy untuk ilustrasi. Hasil ini dihitung sekali dan berlaku seumur hidup.</p>',
                unsafe_allow_html=True,
            )

        with tab_mingguan:
            st.markdown(
                """<div class="dr-mini-card">
                    <span class="dr-mini-tag">Minggu Ini</span>
                    <p class="dr-mini-text" style="margin-top:10px;">
                        Energi Aries kamu lagi kuat di sisi eksekusi minggu ini, apalagi didukung Shio Kuda yang
                        bikin kamu gampang gerak cepat begitu ada peluang. Tapi weton Jumat Legi kamu juga lagi
                        nunjukin sisi sensitif ke omongan orang sekitar, jadi jangan sampai energi cepatmu bikin ada
                        yang tersinggung karena keputusan diambil tanpa banyak ngobrol dulu.
                    </p>
                    <div class="dr-mini-label">Fokus Minggu Ini</div>
                    <p class="dr-mini-text">Eksekusi ide, tapi komunikasikan dulu ke orang terdekat sebelum jalan sendiri.</p>
                    <div class="dr-mini-label">Saran</div>
                    <p class="dr-mini-text">Luangkan 10 menit tiap pagi buat cek rencana hari itu bareng tim/partner, biar langkah cepatmu tetap selaras sama orang lain.</p>
                </div>""",
                unsafe_allow_html=True,
            )
            st.markdown(
                '<p style="font-size:12.5px;color:#9a948a !important;">Diperbarui otomatis tiap minggu, sesuai kombinasi hasil global kamu.</p>',
                unsafe_allow_html=True,
            )

        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    st.write("")
    st.write("")
    st.write("")

    # ── CTA PENUTUP ──────────────────────────────────────────
    st.markdown("<hr>", unsafe_allow_html=True)
    st.write("")
    st.markdown('<div class="dr-center"><span class="dr-section-title">Penasaran Sama Dirimu Sendiri?</span></div>', unsafe_allow_html=True)
    st.markdown(
        '<p class="dr-center" style="color:#6b6459 !important;font-size:15px;margin-bottom:22px;">Mulai sekarang, hasil pertama muncul dalam hitungan menit.</p>',
        unsafe_allow_html=True,
    )
    cta_l, cta_mid, cta_r = st.columns([1.5, 1.4, 1.5])
    with cta_mid:
        st.button("Mulai Eksplorasi Gratis", key="cta_footer", type="primary", icon=":material/arrow_forward:", use_container_width=True)

    st.write("")
    st.markdown(
        '<p style="text-align:center;color:#9a948a !important;font-size:12.5px;">© 2026 Destiny Reveal</p>',
        unsafe_allow_html=True,
    )

# ══════════════════════════════════════════════════════════════
# TAB 2 — PREVIEW FORM SCREENING (layout final, logic belum jalan)
# ══════════════════════════════════════════════════════════════
with tab_form:

    st.markdown('<p style="font-size:12.5px;font-weight:700;letter-spacing:0.06em;text-transform:uppercase;color:#b8562f !important;margin-bottom:4px;">Langkah 1 dari 3</p>', unsafe_allow_html=True)
    st.markdown('<div class="dr-section-title-wrap"><span class="dr-section-title">Verifikasi Email</span></div>', unsafe_allow_html=True)
    st.markdown('<p style="font-size:14px;color:#6b6459 !important;margin-top:-14px;">Tidak perlu membuat akun. Cukup email untuk menyimpan & membuka hasilmu nanti.</p>', unsafe_allow_html=True)

    with st.container(border=True):
        st.text_input("Alamat Email", placeholder="nama@email.com")
        vcol1, vcol2 = st.columns([1, 2])
        with vcol1:
            st.button("Kirim Kode", key="btn_send_otp", type="secondary", icon=":material/send:")
        with vcol2:
            st.text_input("Kode Verifikasi (6 digit)", placeholder="○ ○ ○ ○ ○ ○", label_visibility="collapsed")

    st.write("")
    st.write("")

    st.markdown('<p style="font-size:12.5px;font-weight:700;letter-spacing:0.06em;text-transform:uppercase;color:#b8562f !important;margin-bottom:4px;">Langkah 2 dari 3</p>', unsafe_allow_html=True)
    st.markdown('<div class="dr-section-title-wrap"><span class="dr-section-title">Isi Data Lahir</span></div>', unsafe_allow_html=True)
    st.markdown('<p style="font-size:14px;color:#6b6459 !important;margin-top:-14px;">3 kolom pertama wajib diisi. Sisanya opsional, namun membuat hasil BaZi & Human Design lebih akurat.</p>', unsafe_allow_html=True)

    with st.container(border=True):
        fcol1, fcol2 = st.columns(2)
        with fcol1:
            st.text_input("Nama Lengkap *", placeholder="Nama sesuai identitas")
            st.date_input("Tanggal Lahir *")
            st.selectbox("Jenis Kelamin (opsional)", ["— Pilih —", "Laki-laki", "Perempuan"])
        with fcol2:
            st.time_input("Jam Lahir (opsional, tapi disarankan)")
            st.text_input("Kota Lahir (opsional)", placeholder="Contoh: Jakarta")
            st.selectbox("Bahasa Laporan", ["Bahasa Indonesia", "English"])

    st.write("")
    st.write("")

    st.markdown('<p style="font-size:12.5px;font-weight:700;letter-spacing:0.06em;text-transform:uppercase;color:#b8562f !important;margin-bottom:4px;">Langkah 3 dari 3</p>', unsafe_allow_html=True)
    st.markdown('<div class="dr-section-title-wrap"><span class="dr-section-title">Pilih Fokus Eksplorasi</span></div>', unsafe_allow_html=True)
    st.markdown('<p style="font-size:14px;color:#6b6459 !important;margin-top:-14px;">Pilihan ini menentukan sistem mana yang dihitung untuk laporanmu.</p>', unsafe_allow_html=True)

    with st.container(border=True):
        st.radio(
            "Mode Eksplorasi",
            [
                "Mode Instan — Weton, Zodiak, Shio & Numerologi",
                "Mode Mendalam — MBTI, Big Five & Enneagram",
                "Mode Lengkap — Semua sistem + skor kecocokan",
            ],
            label_visibility="collapsed",
        )

    st.write("")
    st.button("Lanjut ke Ringkasan", key="btn_lanjut_form", type="primary", icon=":material/arrow_forward:")
