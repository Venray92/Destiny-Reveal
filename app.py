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
    '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />',
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

    .stApp { background-color: #ffffff; }
    .block-container { padding-top: 2rem; padding-bottom: 3rem; max-width: 1360px; }

    .stApp, .stApp p, .stApp span, .stApp div, .stApp b, .stApp li,
    .stApp label, .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5,
    .stMarkdown, .stMarkdown p {
        color: #1c1a17;
    }
    .stApp { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }

    .dr-center { text-align: center; }

    .dr-badge {
        display: inline-flex; align-items: center; gap: 6px;
        padding: 7px 16px; border: 1px solid #ecddc9; border-radius: 100px;
        font-size: 13px; color: #8a5a2f !important; background: #fdf3e7;
        margin-bottom: 22px;
    }
    .dr-hero-title {
        font-size: 58px; font-weight: 800; line-height: 1.12;
        margin: 0 0 20px 0; letter-spacing: -0.02em; color: #1c1a17 !important;
        text-align: left;
    }
    .dr-hero-sub {
        font-size: 18px; line-height: 1.75; color: #5c564d !important;
        max-width: 680px; margin: 0 0 30px 0; text-align: left;
    }
    .dr-hero-sub em { color: #b8562f !important; font-style: normal; font-weight: 600; }
    .dr-section-label {
        font-size: 13px; font-weight: 700; letter-spacing: 0.08em;
        text-transform: uppercase; color: #b8562f !important; margin-bottom: 8px;
        text-align: center;
    }
    .dr-section-title {
        font-size: 30px; font-weight: 800; color: #1c1a17 !important;
        margin: 0 0 10px 0; text-align: center;
    }
    .dr-section-sub {
        font-size: 15px; color: #6b6459 !important; margin: 0 auto 30px auto;
        text-align: center; max-width: 560px;
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
    .dr-step-card-1 { border-color: #ecddc9 !important; }
    .dr-step-card-2 { border-color: #d98a5e !important; }
    .dr-step-card-3 { border-color: #b8562f !important; }

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
        border: 2px solid #ece6dc; height: 220px; box-sizing: border-box;
        display: flex; flex-direction: column; align-items: center; text-align: center;
    }
    .dr-bulk-icon {
        width: 44px; height: 44px; border-radius: 12px; background: #fdf3e7;
        display: flex; align-items: center; justify-content: center; margin-bottom: 12px;
        color: #b8562f !important; flex-shrink: 0;
    }
    .dr-bulk-tags-wrap { display: flex; flex-wrap: wrap; justify-content: center; gap: 6px; overflow-y: auto; }
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
        padding: 18px 26px; background: linear-gradient(135deg, #8a5a2f, #6b4226);
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
    .dr-mini-text { font-size: 13.5px; color: #3a362f !important; line-height: 1.6; margin: 2px 0 0 0; }

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
# format: (nama, arti_singkat, icon_material, aktif)
SEMUA_SISTEM = [
    ("BaZi", "Untuk mengetahui struktur nasib & elemen dominan dari 4 pilar waktu lahir.", "account_tree", False),
    ("Big Five", "Untuk mengetahui 5 trait kepribadian yang tervalidasi riset psikologi.", "insights", False),
    ("DISC", "Untuk mengetahui gaya perilaku kerja & komunikasimu.", "groups", False),
    ("Enneagram", "Untuk mengetahui motivasi inti di balik perilakumu, dari 9 tipe dasar.", "category", False),
    ("Golongan Darah", "Untuk mengetahui kecenderungan sifat dari golongan darah, populer di budaya Jepang & Korea.", "bloodtype", False),
    ("Human Design", "Untuk mengetahui tipe energi & cara alami kamu mengambil keputusan.", "hub", False),
    ("Love Language", "Untuk mengetahui cara kamu paling nyaman menerima & menyampaikan kasih sayang.", "favorite", False),
    ("Matrix Destiny", "Untuk mengetahui peta menyeluruh: kepribadian, rezeki, cinta & karma.", "grid_view", False),
    ("MBTI", "Untuk mengetahui gaya berpikir & bekerja lewat 16 tipe kepribadian.", "psychology", False),
    ("Numerologi", "Untuk mengetahui jalan hidup utama dari angka lahir & nama.", "tag", False),
    ("Shio", "Untuk mengetahui sifat & elemen bawaan dari siklus 12 hewan Tiongkok.", "pets", False),
    ("Tarot", "Untuk mengetahui arketipe jiwa & pelajaran hidup dari sudut pandang tarot.", "style", False),
    ("Weton", "Untuk mengetahui watak bawaan lahir & hari baik menurut tradisi Jawa.", "calendar_today", False),
    ("Zi Wei", "Untuk mengetahui peta 12 istana kehidupan dari astrologi bintang ungu.", "auto_awesome", False),
    ("Zodiak", "Untuk mengetahui karakter dasar dari posisi matahari saat kamu lahir.", "star", True),
]

# ── NAV ──────────────────────────────────────────────────────
nav_l, nav_r = st.columns([5, 1])
with nav_l:
    st.markdown(
        '<div style="font-size:22px;font-weight:800;color:#1c1a17;padding-top:6px;">✨ Destiny Reveal</div>',
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
    st.markdown('<div class="dr-hero-title">Sudah Tahu Zodiakmu?<br>Tapi Sudah Tahu Weton, Shio,<br>sampai Matrix Destiny-mu?</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="dr-hero-sub">'
        'Cukup isi data sekali saja.<br>'
        '15 sistem pembacaan kepribadian akan digabungkan menjadi satu laporan.<br>'
        'Bukan sekadar label, tetapi jawaban atas pertanyaan yang paling sering muncul:<br>'
        '<em>"Lalu, apa yang sebaiknya aku lakukan?"</em>'
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
        for col, (nama, arti, icon, aktif) in zip(cols, chunk):
            with col:
                with st.popover(nama, use_container_width=True, icon=f":material/{icon}:"):
                    if aktif and nama == "Zodiak":
                        st.markdown("**✨ Zodiak (Aktif)**")
                        st.write(
                            "Zodiak membaca karakter dasar seseorang dari posisi matahari "
                            "terhadap salah satu dari 12 rasi bintang saat ia lahir. Setiap "
                            "rasi punya elemen (Api, Tanah, Udara, atau Air) yang menggambarkan "
                            "kecenderungan dasar cara seseorang bereaksi dan mengambil keputusan."
                        )
                        st.markdown("**Yang bisa diketahui:** kecenderungan sifat dasar, gaya emosi, dan cara merespons situasi baru.")
                        st.markdown("---")
                        st.markdown("**Coba sekarang:**")
                        tgl_coba = st.date_input("Tanggal lahir", key="zodiak_demo_date", label_visibility="collapsed")
                        if ZODIAK_ENGINE_READY:
                            hasil = hitung_zodiak(tgl_coba)
                            st.success(f"Zodiakmu: **{hasil['sign']}** (elemen {hasil['element']})")
                        else:
                            st.info("Engine belum ter-upload ke repo. Tambahkan engine/zodiak.py dulu.")
                    else:
                        st.markdown(f"**{nama}**")
                        st.write(arti)
                        st.caption("Belum aktif — masih dalam pengembangan.")

    st.write("")
    st.write("")
    st.write("")

    # ── CARA KERJA ───────────────────────────────────────────
    st.markdown('<div class="dr-section-label">Cara Kerja</div>', unsafe_allow_html=True)
    st.markdown('<div class="dr-section-title">Tiga Langkah, Tanpa Ribet</div>', unsafe_allow_html=True)
    st.write("")

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
    st.markdown('<div class="dr-section-label">Yang Digabungkan</div>', unsafe_allow_html=True)
    st.markdown('<div class="dr-section-title">Satu Data, Banyak Cara Pandang</div>', unsafe_allow_html=True)
    st.markdown('<div class="dr-section-sub">Makin lengkap data yang kamu isi, makin banyak & makin akurat hasil yang kamu dapat.</div>', unsafe_allow_html=True)

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
    st.markdown('<div class="dr-section-label">Contoh Laporan</div>', unsafe_allow_html=True)
    st.markdown('<div class="dr-section-title">Ini yang Kamu Dapat</div>', unsafe_allow_html=True)
    st.markdown('<div class="dr-section-sub">Preview singkat terbuka gratis. Laporan penuh & action plan terbuka setelah pembayaran.</div>', unsafe_allow_html=True)

    st.markdown('<div class="dr-result-card">', unsafe_allow_html=True)
    st.markdown('<div class="dr-result-header">✨ Contoh Laporan Personal</div>', unsafe_allow_html=True)

    with st.container():
        st.markdown('<div style="padding:22px 26px 6px 26px;">', unsafe_allow_html=True)
        tab_global, tab_mingguan = st.tabs([":material/public: Baca Global (Seumur Hidup)", ":material/calendar_month: Baca Minggu Ini"])

        with tab_global:
            hasil_global = [
                ("Zodiak: Aries", "Cepat bergerak, nggak suka nunggu buat eksekusi ide.",
                 "Manfaatkan energi awal yang kuat buat mulai proyek baru, tapi siapin sistem biar konsisten sampai selesai."),
                ("Shio: Kuda", "Suka kebebasan, mudah beradaptasi di lingkungan baru.",
                 "Cari peran kerja yang fleksibel, bukan yang terlalu terkekang rutinitas kaku."),
                ("Weton: Jumat Legi", "Neptu 11, kepekaan sosial tinggi & mudah dipercaya orang.",
                 "Cocok jadi jembatan komunikasi dalam tim, manfaatkan buat negosiasi atau membangun relasi kerja."),
                ("Life Path: 7", "Reflektif, butuh waktu sendiri sebelum ambil keputusan besar.",
                 "Kasih jeda 1 hari sebelum memutuskan hal penting, meski insting pengen langsung gas."),
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
    st.markdown('<div class="dr-section-title">Penasaran Sama Dirimu Sendiri?</div>', unsafe_allow_html=True)
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

    st.markdown('<div class="dr-section-label">Langkah 1 dari 3</div>', unsafe_allow_html=True)
    st.markdown('<div class="dr-section-title">Verifikasi Email</div>', unsafe_allow_html=True)
    st.markdown('<div class="dr-section-sub">Nggak perlu bikin akun. Cukup email buat simpan & buka hasilmu nanti.</div>', unsafe_allow_html=True)

    with st.container(border=True):
        st.text_input("Alamat Email", placeholder="nama@email.com")
        vcol1, vcol2 = st.columns([1, 2])
        with vcol1:
            st.button("Kirim Kode", key="btn_send_otp", type="secondary", icon=":material/send:")
        with vcol2:
            st.text_input("Kode Verifikasi (6 digit)", placeholder="○ ○ ○ ○ ○ ○", label_visibility="collapsed")

    st.write("")
    st.write("")

    st.markdown('<div class="dr-section-label">Langkah 2 dari 3</div>', unsafe_allow_html=True)
    st.markdown('<div class="dr-section-title">Isi Data Lahir</div>', unsafe_allow_html=True)
    st.markdown('<div class="dr-section-sub">3 field pertama wajib. Sisanya opsional, tapi bikin hasil BaZi & Human Design lebih akurat.</div>', unsafe_allow_html=True)

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

    st.markdown('<div class="dr-section-label">Langkah 3 dari 3</div>', unsafe_allow_html=True)
    st.markdown('<div class="dr-section-title">Pilih Fokus Eksplorasi</div>', unsafe_allow_html=True)
    st.markdown('<div class="dr-section-sub">Ini menentukan sistem mana yang dihitung buat laporanmu.</div>', unsafe_allow_html=True)

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
