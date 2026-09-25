"""
Destiny Reveal — entry point Streamlit app.
Homepage layout dulu, engine ditambahin pelan-pelan dari sini.
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
    .block-container { padding-top: 2rem; max-width: 1100px; }

    .dr-badge {
        display: inline-flex; align-items: center; gap: 6px;
        padding: 6px 16px; border: 1px solid #ecddc9; border-radius: 100px;
        font-size: 13px; color: #8a5a2f; background: #fdf3e7;
        margin-bottom: 20px;
    }
    .dr-hero-title {
        font-size: 42px; font-weight: 700; line-height: 1.15;
        margin: 0 0 16px 0; letter-spacing: -0.01em; color: #1c1a17;
    }
    .dr-hero-sub {
        font-size: 17px; line-height: 1.6; color: #5c564d;
        max-width: 560px; margin: 0 0 8px 0;
    }
    .dr-chip {
        display: inline-block; padding: 6px 14px; border-radius: 100px;
        background: #f6f1e9; font-size: 13px; color: #5c564d;
        font-weight: 600; margin: 4px 4px 0 0;
    }
    .dr-section-label {
        font-size: 13px; font-weight: 700; letter-spacing: 0.08em;
        text-transform: uppercase; color: #b8562f; margin-bottom: 8px;
    }
    .dr-section-title {
        font-size: 28px; font-weight: 700; color: #1c1a17;
        margin: 0 0 8px 0;
    }
    .dr-card {
        padding: 22px; border: 1px solid #ece6dc; border-radius: 14px;
        background: #ffffff; height: 100%;
    }
    .dr-step-num {
        width: 34px; height: 34px; border-radius: 9px; background: #fdf3e7;
        display: flex; align-items: center; justify-content: center;
        font-weight: 700; color: #b8562f; margin-bottom: 10px; font-size: 14px;
    }
    .dr-result-card {
        border: 1px solid #ece6dc; border-radius: 16px; overflow: hidden;
        box-shadow: 0 16px 40px -18px rgba(28,26,23,0.15);
    }
    .dr-result-header {
        padding: 18px 24px; background: #1c1a17; color: #ffffff;
        font-size: 14px; font-weight: 600;
    }
    .dr-result-tag {
        display: inline-block; padding: 6px 14px; border-radius: 100px;
        background: #fdf3e7; color: #8a5a2f; font-size: 13px; font-weight: 700;
        margin: 4px 8px 4px 0;
    }
    div.stButton > button {
        background: #b8562f; color: #ffffff; border: none;
        padding: 12px 26px; border-radius: 10px; font-weight: 700;
        font-size: 15px;
    }
    div.stButton > button:hover { background: #a5482a; color: #ffffff; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ── NAV ──────────────────────────────────────────────────────
nav_l, nav_r = st.columns([3, 1])
with nav_l:
    st.markdown("### ✨ Destiny Reveal")
with nav_r:
    st.write("")

st.markdown("<hr style='margin-top:0;border-color:#ece6dc;'>", unsafe_allow_html=True)

# ── HERO ─────────────────────────────────────────────────────
st.markdown('<div class="dr-badge">✧ 7 sistem pembacaan diri, 1 laporan personal</div>', unsafe_allow_html=True)
st.markdown('<div class="dr-hero-title">Kenali Dirimu Lewat Weton, Zodiak, sampai MBTI — Sekaligus</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="dr-hero-sub">Satu kali isi data, langsung dapat pembacaan dari 7+ sistem populer. '
    'Bukan cuma label — laporan yang jawab pertanyaan "terus aku harus ngapain?"</div>',
    unsafe_allow_html=True,
)

col_a, col_b = st.columns([1, 4])
with col_a:
    st.button("Mulai Eksplorasi →", key="cta_hero")

st.markdown(
    "".join(
        f'<span class="dr-chip">{x}</span>'
        for x in ["Weton", "Zodiak", "Shio", "MBTI", "BaZi", "Zi Wei", "Numerologi", "Big Five"]
    ),
    unsafe_allow_html=True,
)

st.write("")
st.write("")

# ── CARA KERJA ───────────────────────────────────────────────
st.markdown('<div class="dr-section-label">Cara Kerja</div>', unsafe_allow_html=True)
st.markdown('<div class="dr-section-title">Tiga Langkah, Tanpa Ribet</div>', unsafe_allow_html=True)
st.write("")

c1, c2, c3 = st.columns(3)
steps = [
    ("1", "Verifikasi Email", "Masukkan email, dapat kode verifikasi. Tanpa akun atau password."),
    ("2", "Isi Data & Pilih Fokus", "Nama, tanggal & jam lahir, lalu pilih fokus eksplorasimu."),
    ("3", "Buka Hasil Lengkap", "Bayar sekali, laporan langsung terbuka & dikirim ke email."),
]
for col, (num, title, desc) in zip([c1, c2, c3], steps):
    with col:
        st.markdown(
            f"""<div class="dr-card">
                <div class="dr-step-num">{num}</div>
                <b>{title}</b>
                <p style="font-size:13.5px;color:#6b6459;margin-top:6px;">{desc}</p>
            </div>""",
            unsafe_allow_html=True,
        )

st.write("")
st.write("")

# ── SISTEM ───────────────────────────────────────────────────
st.markdown('<div class="dr-section-label">Yang Digabungkan</div>', unsafe_allow_html=True)
st.markdown('<div class="dr-section-title">7 Cara Pandang, Satu Laporan</div>', unsafe_allow_html=True)
st.write("")

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
cols = st.columns(4)
for i, (icon, title, desc) in enumerate(sistem):
    with cols[i % 4]:
        st.markdown(
            f"""<div class="dr-card">
                <div style="font-size:22px;margin-bottom:6px;">{icon}</div>
                <b>{title}</b>
                <p style="font-size:12.5px;color:#6b6459;margin-top:4px;">{desc}</p>
            </div>""",
            unsafe_allow_html=True,
        )
    if i % 4 == 3 and i != len(sistem) - 1:
        st.write("")

st.write("")
st.write("")

# ── CONTOH HASIL (dummy, tanpa blur) ────────────────────────
st.markdown('<div class="dr-section-label">Contoh Laporan</div>', unsafe_allow_html=True)
st.markdown('<div class="dr-section-title">Ini yang Kamu Dapat</div>', unsafe_allow_html=True)
st.write("")

st.markdown(
    """
    <div class="dr-result-card">
        <div class="dr-result-header">Laporan Personal — Contoh (Stev)</div>
        <div style="padding:24px;">
            <span class="dr-result-tag">Zodiak: Aries</span>
            <span class="dr-result-tag">Shio: Kuda</span>
            <span class="dr-result-tag">Weton: Jumat Legi</span>
            <span class="dr-result-tag">Life Path: 7</span>
            <p style="margin-top:16px;font-size:14.5px;line-height:1.7;color:#3a362f;">
                Kombinasi Aries dan Shio Kuda menunjukkan energi yang cepat bergerak dan
                nggak suka nunggu lama buat eksekusi ide. Weton Jumat Legi menambahkan sisi
                kepekaan sosial yang kuat — cocok buat kerja yang butuh negosiasi atau
                membangun relasi. Life Path 7 menandakan kecenderungan reflektif: kamu perlu
                waktu sendiri buat mikir sebelum ambil keputusan besar, meski secara alami
                inginnya langsung tancap gas.
            </p>
            <p style="font-size:13px;color:#9a948a;margin-top:12px;">
                Ini contoh hasil dummy untuk ilustrasi. Laporan aslimu dihitung dari data lahirmu sendiri.
            </p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")
st.write("")

# ── CTA PENUTUP ──────────────────────────────────────────────
st.markdown("<hr style='border-color:#ece6dc;'>", unsafe_allow_html=True)
st.write("")
cta_l, cta_r = st.columns([3, 1])
with cta_l:
    st.markdown('<div class="dr-section-title">Penasaran Sama Dirimu Sendiri?</div>', unsafe_allow_html=True)
    st.markdown(
        '<p style="color:#6b6459;font-size:15px;">Mulai sekarang, hasil pertama muncul dalam hitungan menit.</p>',
        unsafe_allow_html=True,
    )
with cta_r:
    st.write("")
    st.button("Mulai Eksplorasi Gratis →", key="cta_footer")

st.write("")
st.markdown(
    '<p style="text-align:center;color:#9a948a;font-size:12.5px;">© 2026 Destiny Reveal</p>',
    unsafe_allow_html=True,
)
