"""
Destiny Reveal — entry point Streamlit app.
Homepage + preview layout form. Isi/logic ditambahin pelan-pelan dari sini.
"""

import streamlit as st

st.set_page_config(
    page_title="Destiny Reveal",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Custom CSS ──────────────────────────────────────────────
st.markdown(
    """
    <style>
    #MainMenu, footer, header {visibility: hidden;}

    .stApp { background-color: #ffffff; }
    .block-container { padding-top: 2rem; padding-bottom: 3rem; max-width: 1360px; }

    /* Paksa semua teks jadi gelap — biar nggak ketelen tema gelap browser */
    .stApp, .stApp p, .stApp span, .stApp div, .stApp b, .stApp li,
    .stApp label, .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5,
    .stMarkdown, .stMarkdown p {
        color: #1c1a17;
    }
    .stApp { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }

    .dr-badge {
        display: inline-flex; align-items: center; gap: 6px;
        padding: 7px 16px; border: 1px solid #ecddc9; border-radius: 100px;
        font-size: 13px; color: #8a5a2f !important; background: #fdf3e7;
        margin-bottom: 22px;
    }
    .dr-hero-title {
        font-size: 46px; font-weight: 800; line-height: 1.15;
        margin: 0 0 18px 0; letter-spacing: -0.01em; color: #1c1a17 !important;
    }
    .dr-hero-sub {
        font-size: 17.5px; line-height: 1.65; color: #5c564d !important;
        max-width: 620px; margin: 0 0 26px 0;
    }
    .dr-chip {
        display: inline-block; padding: 7px 16px; border-radius: 100px;
        background: #f6f1e9; font-size: 13px; color: #5c564d !important;
        font-weight: 600; margin: 4px 6px 0 0;
    }
    .dr-section-label {
        font-size: 13px; font-weight: 700; letter-spacing: 0.08em;
        text-transform: uppercase; color: #b8562f !important; margin-bottom: 8px;
    }
    .dr-section-title {
        font-size: 30px; font-weight: 800; color: #1c1a17 !important;
        margin: 0 0 10px 0;
    }
    .dr-section-sub {
        font-size: 15px; color: #6b6459 !important; margin: 0 0 28px 0;
    }
    .dr-card {
        padding: 24px; border: 1px solid #ece6dc; border-radius: 16px;
        background: #ffffff; height: 100%;
    }
    .dr-card b { color: #1c1a17 !important; font-size: 15.5px; }
    .dr-card p { color: #6b6459 !important; }
    .dr-step-num {
        width: 36px; height: 36px; border-radius: 10px; background: #fdf3e7;
        display: flex; align-items: center; justify-content: center;
        font-weight: 800; color: #b8562f !important; margin-bottom: 12px; font-size: 15px;
    }
    .dr-result-card {
        border: 1px solid #ece6dc; border-radius: 18px; overflow: hidden;
        box-shadow: 0 20px 50px -22px rgba(28,26,23,0.18);
    }
    .dr-result-header {
        padding: 20px 26px; background: #1c1a17; color: #ffffff !important;
        font-size: 14.5px; font-weight: 700;
    }
    .dr-result-header * { color: #ffffff !important; }
    .dr-result-tag {
        display: inline-block; padding: 7px 15px; border-radius: 100px;
        background: #fdf3e7; color: #8a5a2f !important; font-size: 13px; font-weight: 700;
        margin: 4px 8px 4px 0;
    }
    .dr-result-body p { color: #3a362f !important; }

    div[data-testid="stVerticalBlockBorderWrapper"] { border-radius: 16px; }

    /* Tombol utama */
    div.stButton > button[kind="primary"] {
        background: #b8562f; color: #ffffff !important; border: none;
        padding: 12px 28px; border-radius: 10px; font-weight: 700;
        font-size: 15px;
    }
    div.stButton > button[kind="primary"]:hover { background: #a5482a; }
    div.stButton > button[kind="secondary"] {
        background: #ffffff; color: #1c1a17 !important; border: 1px solid #e4ddd0;
        padding: 12px 28px; border-radius: 10px; font-weight: 700; font-size: 15px;
    }
    div.stButton > button[kind="secondary"]:hover { border-color: #b8562f; color: #b8562f !important; }

    hr { border-color: #ece6dc !important; }

    /* Input widgets */
    .stTextInput input, .stDateInput input, .stTimeInput input,
    .stSelectbox div[data-baseweb="select"] > div {
        border-radius: 8px !important; border-color: #e4ddd0 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ── NAV ──────────────────────────────────────────────────────
nav_l, nav_r = st.columns([4, 1.2])
with nav_l:
    st.markdown(
        '<div style="font-size:22px;font-weight:800;color:#1c1a17;padding-top:6px;">✨ Destiny Reveal</div>',
        unsafe_allow_html=True,
    )
with nav_r:
    st.selectbox("Bahasa", ["🇮🇩 Indonesia", "🇬🇧 English"], label_visibility="collapsed")

st.markdown("<hr style='margin-top:14px;'>", unsafe_allow_html=True)

tab_home, tab_form = st.tabs(["🏠  Beranda", "📝  Preview Form Screening"])

# ══════════════════════════════════════════════════════════════
# TAB 1 — BERANDA (landing page)
# ══════════════════════════════════════════════════════════════
with tab_home:

    # ── HERO ─────────────────────────────────────────────────
    st.markdown('<div class="dr-badge">✧ 7 sistem pembacaan diri, 1 laporan personal</div>', unsafe_allow_html=True)
    st.markdown('<div class="dr-hero-title">Kenali Dirimu Lewat Weton,<br>Zodiak, sampai MBTI — Sekaligus</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="dr-hero-sub">Satu kali isi data, langsung dapat pembacaan dari 7+ sistem populer. '
        'Bukan cuma label — laporan yang jawab pertanyaan "terus aku harus ngapain?"</div>',
        unsafe_allow_html=True,
    )

    col_a, col_b, col_c = st.columns([1.3, 1.3, 3])
    with col_a:
        st.button("Mulai Eksplorasi", key="cta_hero", type="primary", icon=":material/bolt:", use_container_width=True)
    with col_b:
        st.button("Lihat Contoh Hasil", key="cta_hero_secondary", type="secondary", icon=":material/visibility:", use_container_width=True)

    st.write("")
    st.markdown(
        "".join(
            f'<span class="dr-chip">{x}</span>'
            for x in ["Weton", "Zodiak", "Shio", "MBTI", "BaZi", "Zi Wei", "Numerologi", "Big Five"]
        ),
        unsafe_allow_html=True,
    )

    st.write("")
    st.write("")
    st.write("")

    # ── CARA KERJA ───────────────────────────────────────────
    st.markdown('<div class="dr-section-label">Cara Kerja</div>', unsafe_allow_html=True)
    st.markdown('<div class="dr-section-title">Tiga Langkah, Tanpa Ribet</div>', unsafe_allow_html=True)
    st.write("")

    c1, c2, c3 = st.columns(3, gap="medium")
    steps = [
        ("1", ":material/mail:", "Verifikasi Email", "Masukkan email, dapat kode verifikasi. Tanpa akun atau password."),
        ("2", ":material/edit_note:", "Isi Data & Pilih Fokus", "Nama, tanggal & jam lahir, lalu pilih fokus eksplorasimu."),
        ("3", ":material/auto_awesome:", "Buka Hasil Lengkap", "Bayar sekali, laporan langsung terbuka & dikirim ke email."),
    ]
    for col, (num, icon, title, desc) in zip([c1, c2, c3], steps):
        with col:
            st.markdown(
                f"""<div class="dr-card">
                    <div class="dr-step-num">{num}</div>
                    <b>{title}</b>
                    <p style="font-size:13.5px;margin-top:8px;line-height:1.6;">{desc}</p>
                </div>""",
                unsafe_allow_html=True,
            )

    st.write("")
    st.write("")
    st.write("")

    # ── SISTEM ───────────────────────────────────────────────
    st.markdown('<div class="dr-section-label">Yang Digabungkan</div>', unsafe_allow_html=True)
    st.markdown('<div class="dr-section-title">7 Cara Pandang, Satu Laporan</div>', unsafe_allow_html=True)
    st.markdown('<div class="dr-section-sub">Sistem turun-temurun digabung dengan tes kepribadian modern.</div>', unsafe_allow_html=True)

    sistem = [
        ("🌙", "Weton", "Watak dari hari & pasaran Jawa"),
        ("♈", "Zodiak", "Karakter dari posisi matahari"),
        ("🐉", "Shio", "Siklus 12 hewan tahunan"),
        ("🧠", "MBTI", "Gaya berpikir & kerja, 16 tipe"),
        ("☯", "BaZi", "Empat pilar takdir Tiongkok"),
        ("✨", "Zi Wei", "Astrologi bintang ungu"),
        ("🔢", "Numerologi", "Makna dari angka lahir & nama"),
        ("📊", "Big Five", "5 trait kepribadian tervalidasi"),
    ]
    row1 = st.columns(4, gap="medium")
    row2 = st.columns(4, gap="medium")
    for i, (icon, title, desc) in enumerate(sistem):
        col = row1[i] if i < 4 else row2[i - 4]
        with col:
            st.markdown(
                f"""<div class="dr-card">
                    <div style="font-size:24px;margin-bottom:8px;">{icon}</div>
                    <b>{title}</b>
                    <p style="font-size:12.5px;margin-top:4px;line-height:1.5;">{desc}</p>
                </div>""",
                unsafe_allow_html=True,
            )

    st.write("")
    st.write("")
    st.write("")

    # ── CONTOH HASIL (dummy, tanpa blur) ─────────────────────
    st.markdown('<div class="dr-section-label">Contoh Laporan</div>', unsafe_allow_html=True)
    st.markdown('<div class="dr-section-title">Ini yang Kamu Dapat</div>', unsafe_allow_html=True)
    st.write("")

    st.markdown(
        """
        <div class="dr-result-card">
            <div class="dr-result-header">✨ Laporan Personal — Contoh (Stev)</div>
            <div class="dr-result-body" style="padding:26px;">
                <span class="dr-result-tag">Zodiak: Aries</span>
                <span class="dr-result-tag">Shio: Kuda</span>
                <span class="dr-result-tag">Weton: Jumat Legi</span>
                <span class="dr-result-tag">Life Path: 7</span>
                <p style="margin-top:18px;font-size:14.5px;line-height:1.75;">
                    Kombinasi Aries dan Shio Kuda menunjukkan energi yang cepat bergerak dan
                    nggak suka nunggu lama buat eksekusi ide. Weton Jumat Legi menambahkan sisi
                    kepekaan sosial yang kuat — cocok buat kerja yang butuh negosiasi atau
                    membangun relasi. Life Path 7 menandakan kecenderungan reflektif: kamu perlu
                    waktu sendiri buat mikir sebelum ambil keputusan besar, meski secara alami
                    inginnya langsung tancap gas.
                </p>
                <p style="font-size:13px;color:#9a948a !important;margin-top:14px;">
                    Ini contoh hasil dummy untuk ilustrasi. Laporan aslimu dihitung dari data lahirmu sendiri.
                </p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")
    st.write("")
    st.write("")

    # ── CTA PENUTUP ──────────────────────────────────────────
    st.markdown("<hr>", unsafe_allow_html=True)
    st.write("")
    cta_l, cta_r = st.columns([3, 1.3])
    with cta_l:
        st.markdown('<div class="dr-section-title">Penasaran Sama Dirimu Sendiri?</div>', unsafe_allow_html=True)
        st.markdown(
            '<p style="color:#6b6459 !important;font-size:15px;">Mulai sekarang, hasil pertama muncul dalam hitungan menit.</p>',
            unsafe_allow_html=True,
        )
    with cta_r:
        st.write("")
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
