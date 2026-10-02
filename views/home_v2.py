"""
Home v2 — redesain Beranda sesuai referensi "ui baru/1-6.png" (desain
Google AI Studio yang di-upload Stev) + font dan warna.txt. Gantiin
render Home lama di app.py (termasuk navbar, yang dipakai SEMUA halaman).

CSS: assets/css/home_v2.css (namespace "dh-", gak bentrok sama .dr-*
lama yang masih dipakai loading/reveal/tutorial page).

Konten (koin, login, referral, VIP) masih DUMMY/statis — belum ada
backend (Supabase/auth/payment), sesuai arahan Stev. Navbar default
nampilin tombol "Login" (BUKAN badge "Sync Aktif · koin · nama" yang
di mock cuma contoh kondisi SUDAH login).
"""

import base64
import math
from pathlib import Path

import streamlit as st

NODE_ORDER = [
    ("Zodiak", "star"),
    ("Shio", "pets"),
    ("Weton", "calendar_today"),
    ("Numerologi", "tag"),
    ("Matrix Destiny", "grid_view"),
    ("MBTI", "psychology"),
    ("Big Five", "insights"),
    ("DISC", "groups"),
    ("Enneagram", "category"),
    ("Love Language", "favorite"),
    ("BaZi", "account_tree"),
    ("Zi Wei", "auto_awesome"),
    ("Human Design", "hub"),
    ("Golongan Darah", "bloodtype"),
    ("Tarot", "style"),
]

# Warna khas per sistem (background ikon node di diagram radial) — biar
# ga monoton krem semua, sesuai acuan mockup.
NODE_COLOR = {
    "Zodiak": "#8B5CF6",
    "Shio": "#10B981",
    "Weton": "#3B82F6",
    "Numerologi": "#6366F1",
    "Matrix Destiny": "#0EA5E9",
    "MBTI": "#EC4899",
    "Big Five": "#14B8A6",
    "DISC": "#F97316",
    "Enneagram": "#EF4444",
    "Love Language": "#F43F5E",
    "BaZi": "#D97706",
    "Zi Wei": "#CA8A04",
    "Human Design": "#7C3AED",
    "Golongan Darah": "#DC2626",
    "Tarot": "#991B1B",
}

_CELESTIAL_IMG_PATH = Path(__file__).resolve().parent.parent / "assets" / "images" / "celestial_harmony.jpg"


def _celestial_harmony_b64():
    """Base64 poster 'Celestial Harmony' buat background kartu hero.
    None kalau file-nya belum ke-upload (fallback ke gradient polos)."""
    try:
        return base64.b64encode(_CELESTIAL_IMG_PATH.read_bytes()).decode("utf-8")
    except FileNotFoundError:
        return None


def _go(page):
    st.session_state.dr_page = page
    st.rerun()


# ══════════════════════════════════════════════════════════════
# NAVBAR — dipakai di SEMUA halaman (dipanggil dari app.py)
# ══════════════════════════════════════════════════════════════
def render_navbar(current_page):
    with st.container(key="dhnav_wrap"):
        with st.container(key="dhnavbar"):
            logo_col, links_col, right_col = st.columns([1.4, 2.2, 2.0])
            with logo_col:
                st.markdown(
                    '<div class="dh-navbar-logo"><span class="dh-spark">✦</span> Destiny Reveal</div>',
                    unsafe_allow_html=True,
                )
            with links_col:
                with st.container(key="dhnav_links"):
                    l1, d1, l2, d2, l3, d3, l4 = st.columns([2, 0.3, 2, 0.3, 2, 0.3, 2.4])
                    with l1:
                        if st.button("Home", key="dhnav_home", use_container_width=True):
                            _go("home")
                    with d1:
                        st.markdown('<div class="dh-nav-sep">|</div>', unsafe_allow_html=True)
                    with l2:
                        if st.button("Reveal", key="dhnav_reveal", use_container_width=True):
                            _go("reveal")
                    with d2:
                        st.markdown('<div class="dh-nav-sep">|</div>', unsafe_allow_html=True)
                    with l3:
                        if st.button("Tutorial", key="dhnav_tutorial", use_container_width=True):
                            _go("tutorial")
                    with d3:
                        st.markdown('<div class="dh-nav-sep">|</div>', unsafe_allow_html=True)
                    with l4:
                        with st.popover("Jelajahi ▾", use_container_width=True):
                            st.markdown("**Gratis**")
                            st.caption("Ramalan Harian · Tarot 1 Kartu · Preview Zodiak")
                            st.markdown("**Premium**")
                            st.caption("Tarot Spreads · Cek Kecocokan · Deep Blueprint")
                            if st.button("Lihat Tutorial Lengkap", key="dhnav_jelajahi_tutorial"):
                                _go("tutorial")
            with right_col:
                lb, cb = st.columns([1, 1.7])
                with lb:
                    if st.button("Login", key="dhnav_login", use_container_width=True):
                        st.toast("Login/akun belum tersedia — masih tahap pengembangan 🚧")
                with cb:
                    with st.container(key="dhnav_cta"):
                        if st.button(
                            "Mulai Reveal Takdirku →", key="dhnav_cta_btn", type="primary",
                            icon=":material/bolt:", use_container_width=True,
                        ):
                            _go("reveal")


# ══════════════════════════════════════════════════════════════
# HERO
# ══════════════════════════════════════════════════════════════
def _render_hero():
    st.markdown(
        '<div class="dh-hero">'
        '<div class="dh-hero-badge">'
        '<span class="material-symbols-outlined" style="font-size:15px;">schedule</span>'
        'Gratis &nbsp;·&nbsp; 3 menit &nbsp;·&nbsp; Tanpa akun'
        '</div>'
        '<div class="dh-hero-title">Ada Banyak Versi Dirimu<br>yang Belum Kamu Kenal.</div>'
        '<div class="dh-hero-sub">'
        'Masa lalu sudah menjadi pelajaran, saatnya kenali dirimu sepenuhnya sebelum melangkah ke depan.<br>'
        'Satu pembacaan lengkap dari 15 sistem ini akan menunjukkan potensi, kelebihan, '
        'kelemahan, dan langkah yang sebaiknya kamu ambil.'
        '</div>'
        '</div>',
        unsafe_allow_html=True,
    )

    hl, c1, c2, hr_ = st.columns([3.1, 1.75, 1.95, 3.1])
    with c1:
        with st.container(key="dhhero_cta_primary"):
            if st.button(
                "Mulai Reveal Takdirku →", key="dhhero_cta", type="primary",
                icon=":material/bolt:", use_container_width=True,
            ):
                _go("reveal")
    with c2:
        st.markdown(
            '<a href="#dh-matrix" class="dh-btn-anchor-secondary">Lihat 15 Sistem Matrix</a>',
            unsafe_allow_html=True,
        )

    st.markdown(
        '<p class="dh-hero-caption" style="text-align:center;">'
        'Memproses Zodiak, Shio, Weton, Numerologi, dan Matrix Destiny secara otomatis.</p>',
        unsafe_allow_html=True,
    )

    # ── Kartu hero: poster "Celestial Harmony" asli sebagai background
    # (base64, biar gak perlu static file serving di Streamlit). Fallback
    # ke gradient polos kalau aset gambarnya belum ke-upload. ──
    b64 = _celestial_harmony_b64()
    bg_style = f'background-image:url(data:image/jpeg;base64,{b64});' if b64 else ''

    st.markdown(
        f'<div class="dh-hero-card" style="{bg_style}">'
        '<div class="dh-hero-card-overlay">'
        '<div class="dh-hero-card-badge">✦ 15 PINTU KESADARAN</div>'
        '<div class="dh-hero-card-title">Satu sinkronisasi utuh antara ilmu perbintangan kuno, '
        'titen leluhur Jawa, dan psikologi modern.</div>'
        '<div class="dh-hero-card-sub">Klik node pada diagram di bawah untuk mengeksplorasi '
        'setiap dimensi takdirmu.</div>'
        '</div></div>',
        unsafe_allow_html=True,
    )


# ══════════════════════════════════════════════════════════════
# MATRIX DIAGRAM
# ══════════════════════════════════════════════════════════════
def _render_matrix_diagram(sistem_lookup):
    st.markdown('<div id="dh-matrix"></div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="dh-section-head">'
        '<div class="dh-section-title">Satu Dirimu, 15 Cara Memandang</div>'
        '<div class="dh-section-sub">Klik tiap sistem untuk melihat penjelasannya.</div>'
        '</div>',
        unsafe_allow_html=True,
    )

    chips = ["Semua 15 Sistem", "Astrologi & Kosmik", "Kearifan Nusantara & Timur", "Psikologi Modern", "Energi & Intuisi"]
    chip_html = "".join(
        f'<span class="dh-filter-chip{" active" if i == 0 else ""}">{c}</span>'
        for i, c in enumerate(chips)
    )
    st.markdown(f'<div class="dh-filter-row">{chip_html}</div>', unsafe_allow_html=True)

    n = len(NODE_ORDER)
    radius = 42
    pos_css = []
    positions = []
    for i in range(n):
        angle = math.radians(-90 + i * (360 / n))
        top = 50 + radius * math.sin(angle)
        left = 50 + radius * math.cos(angle)
        positions.append((top, left))
        nama = NODE_ORDER[i][0]
        warna = NODE_COLOR.get(nama, "#C86235")
        pos_css.append(
            f'.st-key-dhnode_{i} {{ top: {top:.2f}%; left: {left:.2f}%; }}'
            f'.st-key-dhnode_{i} div[data-testid="stPopover"] button {{'
            f' background: {warna} !important; border-color: {warna} !important; }}'
            f'.st-key-dhnode_{i} div[data-testid="stPopover"] button span[data-testid="stIconMaterial"] {{'
            f' color: #fff !important; }}'
        )
    st.markdown(f"<style>{''.join(pos_css)}</style>", unsafe_allow_html=True)

    # Garis dashed statis dari pusat ke tiap node (SVG, viewBox 0-100 biar
    # ngikutin persentase posisi node — bukan garis solid-interaktif, lihat
    # keputusan Stev: Opsi A, popover tetep dipakai). HARUS dirender di
    # dalam dhmatrix_wrap (bukan sebelum with-block-nya) biar jadi anak DOM
    # beneran dari positioning context-nya — lihat docs/bugs-fixed.md.
    lines_svg = "".join(
        f'<line x1="50" y1="50" x2="{left:.2f}" y2="{top:.2f}" />' for top, left in positions
    )

    with st.container(key="dhmatrix_card"):
        with st.container(key="dhmatrix_wrap"):
            st.markdown(
                f'<svg class="dh-matrix-lines" viewBox="0 0 100 100" preserveAspectRatio="none">{lines_svg}</svg>'
                '<div class="dh-matrix-center"><b>KAMU</b><span>Pusat dari semua sistem</span></div>',
                unsafe_allow_html=True,
            )
            for i, (nama, icon) in enumerate(NODE_ORDER):
                with st.container(key=f"dhnode_{i}"):
                    with st.popover(" ", icon=f":material/{icon}:", use_container_width=False):
                        info = sistem_lookup.get(nama)
                        st.markdown(f"**{nama}**")
                        if info:
                            apa_ini, topik_list, ajakan, aktif = info
                            st.write(apa_ini)
                            for topik in topik_list:
                                st.markdown(f"- {topik}")
                            st.caption(ajakan)
                    st.markdown(f'<div class="dh-matrix-node-label">{nama}</div>', unsafe_allow_html=True)

    st.markdown(
        '<div class="dh-matrix-caption">Klik pada ikon lingkaran untuk membaca ringkasan sistem</div>',
        unsafe_allow_html=True,
    )


# ══════════════════════════════════════════════════════════════
# SOCIAL PROOF
# ══════════════════════════════════════════════════════════════
def _render_social_proof():
    st.markdown(
        '<div class="dh-proof-bar"><span class="dh-proof-dot">●</span>'
        '4.996+ Orang telah menemukan versi terbaik mereka minggu ini.</div>',
        unsafe_allow_html=True,
    )


# ══════════════════════════════════════════════════════════════
# EXPLORE SECTION
# ══════════════════════════════════════════════════════════════
def _render_explore():
    st.markdown(
        '<div class="dh-section-head">'
        '<div class="dh-section-title">Jelajahi Destiny Reveal</div>'
        '<div class="dh-section-sub">Dari yang gratis sampai premium, semua ada di sini.</div>'
        '</div>',
        unsafe_allow_html=True,
    )

    ec1, ec2, ec3 = st.columns(3, gap="medium")

    with ec1:
        with st.container(key="dhexplore_col_gratis"):
            st.markdown(
                '<div class="dh-explore-card">'
                '<div class="dh-explore-head">'
                '<div class="dh-explore-icon" style="background:#FDF6E3;">🆓</div>'
                '<div><div class="dh-explore-title">GRATIS</div>'
                '<div class="dh-explore-subtitle">Eksplorasi tanpa biaya harian</div></div></div>'
                '<div class="dh-explore-item"><div><div class="dh-explore-item-title">Ramalan Harian Gratis</div>'
                '<div class="dh-explore-item-sub">1x per hari, pilih Zodiak atau Shio</div></div>'
                '<span class="dh-explore-item-arrow">→</span></div>'
                '<div class="dh-explore-item"><div><div class="dh-explore-item-title">Tarot 1 Kartu Harian</div>'
                '<div class="dh-explore-item-sub">Tarik kartu deck tertutup dengan animasi shuffle</div></div>'
                '<span class="dh-explore-item-arrow">→</span></div>'
                '<div class="dh-explore-item"><div><div class="dh-explore-item-title">Preview Zodiak</div>'
                '<div class="dh-explore-item-sub">12 rasi, modality, planet &amp; quote</div></div>'
                '<span class="dh-explore-item-arrow">→</span></div>'
                '<div class="dh-explore-item"><div><div class="dh-explore-item-title">Streak &amp; Reward</div>'
                '<div class="dh-explore-item-sub">5 hari berturut = 1 koin gratis</div></div>'
                '<span class="dh-explore-item-arrow">→</span></div>'
                '<div class="dh-explore-foot"></div>'
                '</div>',
                unsafe_allow_html=True,
            )
            if st.button("Mulai Pembacaan Gratis →", key="dhexplore_gratis_btn", use_container_width=True):
                _go("reveal")

    with ec2:
        with st.container(key="dhexplore_col_premium"):
            st.markdown(
                '<div class="dh-explore-card">'
                '<div class="dh-explore-card-badge">PAKAI KOIN &amp; VIP</div>'
                '<div class="dh-explore-head">'
                '<div class="dh-explore-icon" style="background:#eef2fb;">💎</div>'
                '<div><div class="dh-explore-title">PREMIUM</div>'
                '<div class="dh-explore-subtitle">Panduan mendalam &amp; akurasi tinggi</div></div></div>'
                '<div class="dh-explore-item"><div><div class="dh-explore-item-title">Tarot Spreads Multi-Kartu</div>'
                '<div class="dh-explore-item-sub">3 Kartu (1 Koin), 5 Kartu (2 Koin), Celtic Cross (3 Koin)</div></div>'
                '<span class="dh-explore-item-price">1-3 Koin</span></div>'
                '<div class="dh-explore-item"><div><div class="dh-explore-item-title">Cek Kecocokan</div>'
                '<div class="dh-explore-item-sub">Bandingkan 2 orang langsung (Weton &amp; Zodiak)</div></div>'
                '<span class="dh-explore-item-price">3 Koin</span></div>'
                '<div class="dh-explore-item"><div><div class="dh-explore-item-title">Weekly &amp; Monthly Report</div>'
                '<div class="dh-explore-item-sub">Timing pekan (3 Koin) &amp; analisis bulan (5 Koin)</div></div>'
                '<span class="dh-explore-item-price">3-5 Koin</span></div>'
                '<div class="dh-explore-item"><div><div class="dh-explore-item-title">Deep Blueprint (15 Sistem)</div>'
                '<div class="dh-explore-item-sub">Laporan lengkap 15 sistem sekaligus + PDF</div></div>'
                '<span class="dh-explore-item-price vip">VIP</span></div>'
                '</div>',
                unsafe_allow_html=True,
            )
            pb1, pb2 = st.columns(2)
            with pb1:
                if st.button("Paket Koin", key="dhexplore_koin_btn", use_container_width=True):
                    st.toast("Paket koin belum tersedia — masih tahap pengembangan 🚧")
            with pb2:
                if st.button("Upgrade VIP", key="dhexplore_vip_btn", type="primary", use_container_width=True):
                    st.toast("Upgrade VIP belum tersedia — masih tahap pengembangan 🚧")
            st.markdown(
                '<a href="#" class="dh-explore-pricelink" onclick="return false;">'
                '🔒 Lihat Daftar Harga Final Lengkap →</a>',
                unsafe_allow_html=True,
            )

    with ec3:
        with st.container(key="dhexplore_col_lainnya"):
            st.markdown(
                '<div class="dh-explore-card">'
                '<div class="dh-explore-head">'
                '<div class="dh-explore-icon" style="background:#f3eefc;">✨</div>'
                '<div><div class="dh-explore-title">LAINNYA</div>'
                '<div class="dh-explore-subtitle">Referral, wawasan &amp; bantuan pengguna</div></div></div>'
                '<div class="dh-explore-item highlight"><div><div class="dh-explore-item-title">🎁 Program Referral &amp; Affiliate</div>'
                '<div class="dh-explore-item-sub">Komisi 10-30% + Bonus Milestone VIP</div></div>'
                '<span class="dh-explore-item-arrow">→</span></div>'
                '<div class="dh-explore-item"><div><div class="dh-explore-item-title">Tutorial</div>'
                '<div class="dh-explore-item-sub">Panduan pakai website &amp; cara baca hasil</div></div>'
                '<span class="dh-explore-item-arrow">→</span></div>'
                '<div class="dh-explore-item"><div><div class="dh-explore-item-title">Blog</div>'
                '<div class="dh-explore-item-sub">Artikel tentang self-discovery &amp; potensi diri</div></div>'
                '<span class="dh-explore-item-arrow">→</span></div>'
                '<div class="dh-explore-item"><div><div class="dh-explore-item-title">FAQ &amp; Bantuan</div>'
                '<div class="dh-explore-item-sub">Pertanyaan yang sering ditanya</div></div>'
                '<span class="dh-explore-item-arrow">→</span></div>'
                '</div>',
                unsafe_allow_html=True,
            )
            if st.button("Tentang Kami — Destiny Reveal", key="dhexplore_about_btn", use_container_width=True):
                st.toast("Halaman Tentang Kami belum tersedia — masih tahap pengembangan 🚧")


# ══════════════════════════════════════════════════════════════
# DATA FLOW ("Satu Data, Banyak Cara Pandang")
# ══════════════════════════════════════════════════════════════
def _render_dataflow():
    st.markdown(
        '<div class="dh-section-head">'
        '<div class="dh-section-title">Satu Data, Banyak Cara Pandang</div>'
        '<div class="dh-section-sub">Cukup isi sekali, semua sistem langsung diproses.</div>'
        '</div>',
        unsafe_allow_html=True,
    )

    groups = [
        ("calendar_month", "Langkah Dasar", "Tanggal Lahir & Nama Lengkap",
         "Isi tanggal lahir dan nama lengkap, langsung dapat:",
         ["Zodiak", "Shio", "Weton", "Numerologi", "Matrix Destiny"],
         "Otomatis dihitung dalam &lt;1 detik"),
        ("schedule", "Presisi Tinggi", "+ Tambah Jam Lahir",
         "Opsional, tapi bikin hasil berikut lebih presisi:",
         ["BaZi", "Zi Wei Dou Shu", "Human Design"],
         "BaZi &amp; Human Design makin akurat kalau ditambah kota lahir."),
        ("quiz", "Psikologi Jiwa", "Kuesioner Singkat",
         "Isi kuesioner singkat (2-3 menit), dapat:",
         ["MBTI", "Big Five", "Enneagram", "DISC", "Love Language"],
         "5 pertanyaan ringan berbasis skenario nyata"),
        ("water_drop", "Instan Praktis", "Input Langsung",
         "Udah tau hasilnya? Input langsung:",
         ["Golongan Darah (A, B, AB, O)"],
         "(Ga perlu tes ulang, langsung disinkronkan)"),
        ("casino", "Sinkronisitas", "Tarikan Acak",
         "Tarik kartu secara acak:",
         ["Tarot (Major Arcana)"],
         "Setiap tarikan kasih pesan &amp; bimbingan berbeda."),
    ]

    cols = st.columns(3, gap="medium")
    for idx, (icon, tag, title, desc, items, foot) in enumerate(groups):
        with cols[idx % 3]:
            with st.container(key=f"drfillheight_flow{idx}"):
                items_html = "".join(f"<li>{it}</li>" for it in items)
                st.markdown(
                    '<div class="dh-flow-card">'
                    '<div class="dh-flow-head">'
                    f'<div class="dh-flow-icon"><span class="material-symbols-outlined">{icon}</span></div>'
                    f'<span class="dh-flow-tag">{tag}</span></div>'
                    f'<div class="dh-flow-title">{title}</div>'
                    f'<div class="dh-flow-desc">{desc}</div>'
                    f'<ul class="dh-flow-list">{items_html}</ul>'
                    f'<div class="dh-flow-foot"><span>{foot}</span><span>→</span></div>'
                    '</div>',
                    unsafe_allow_html=True,
                )
        if idx % 3 == 2 and idx != len(groups) - 1:
            cols = st.columns(3, gap="medium")

    with st.container(key="dhflow_banner"):
        bl, br_ = st.columns([3, 1.3])
        with bl:
            st.markdown(
                '<div class="dh-flow-banner-text">'
                '<b>Siap memproses peta takdirmu secara bersamaan?</b>'
                '<span>Hanya perlu nama dan tanggal lahir untuk mulai melihat perpaduan 15 sistem.</span>'
                '</div>',
                unsafe_allow_html=True,
            )
        with br_:
            if st.button("Mulai Input Sekali →", key="dhflow_banner_btn", type="primary", use_container_width=True):
                _go("reveal")


# ══════════════════════════════════════════════════════════════
# TESTIMONIALS
# ══════════════════════════════════════════════════════════════
def _render_testimonials():
    st.markdown(
        '<div class="dh-section-head">'
        '<div class="dh-section-title">Kata Mereka yang Udah Reveal</div>'
        '<div class="dh-section-sub">Kisah nyata dari mereka yang telah menemukan kejernihan arah hidup.</div>'
        '</div>',
        unsafe_allow_html=True,
    )

    testis = [
        ("RN", "Rina, 24, Jakarta", "UX Researcher",
         "Gila, akurat banget! Aku yang biasanya skeptis sama ramalan, ternyata MBTI-ku sama Weton-ku nyambung. Jadi lebih paham kenapa aku begini."),
        ("BD", "Budi, 28, Surabaya", "Brand Strategist",
         "Awalnya cuma iseng, tapi hasilnya bikin aku mikir. Saran kariernya masuk akal, dan aku jadi tau harus fokus ke mana."),
        ("SR", "Sarah, 22, Bandung", "Content Creator",
         "Suka banget sama fitur Cek Kecocokan! Aku sama pacar jadi lebih ngerti cara komunikasi masing-masing."),
    ]
    cols = st.columns(3, gap="medium")
    for col, (initials, name, role, quote) in zip(cols, testis):
        with col:
            with st.container(key=f"drfillheight_testi_{initials}"):
                st.markdown(
                    '<div class="dh-testi-card">'
                    '<div class="dh-testi-quote-mark">&ldquo;</div>'
                    f'<div class="dh-testi-text">{quote}</div>'
                    '<div class="dh-testi-foot">'
                    f'<div class="dh-testi-avatar">{initials}</div>'
                    f'<div><div class="dh-testi-name">— {name}</div>'
                    f'<div class="dh-testi-role">{role}</div></div>'
                    '</div></div>',
                    unsafe_allow_html=True,
                )


# ══════════════════════════════════════════════════════════════
# FINAL CTA
# ══════════════════════════════════════════════════════════════
def _render_final_cta():
    st.markdown(
        '<div class="dh-finalcta">'
        '<div class="dh-finalcta-eyebrow">✦ LANGKAH PERTAMA MENUJU KEJELASAN</div>'
        '<div class="dh-finalcta-title">Penasaran Sama Dirimu Sendiri?</div>'
        '<div class="dh-finalcta-sub">Mulai sekarang, hasil pertama muncul dalam hitungan menit.</div>'
        '</div>',
        unsafe_allow_html=True,
    )
    with st.container(key="dhfinal_cta_row"):
        cl, cm, cr = st.columns([1, 1.3, 1])
        with cm:
            if st.button("→ Reveal Yours ←", key="dhfinal_cta_btn", type="primary", use_container_width=True):
                _go("reveal")
    st.markdown(
        '<p class="dh-finalcta-caption" style="text-align:center;">Gratis · Tanpa akun · 3 menit</p>',
        unsafe_allow_html=True,
    )


# ══════════════════════════════════════════════════════════════
# FOOTER
# ══════════════════════════════════════════════════════════════
def _render_footer():
    st.markdown(
        '<div class="dh-footer">'
        '<div style="display:grid;grid-template-columns:1.6fr 1fr 1fr 1fr;gap:24px;">'
        '<div><div class="dh-footer-brand">✦ Destiny Reveal</div>'
        '<div class="dh-footer-tagline">Kenali dirimu, temukan versi terbaikmu.</div>'
        '<div class="dh-footer-note">Satu portal terpadu untuk 15 sistem refleksi jiwa '
        'dan peta takdir holistik.</div></div>'
        '<div><div class="dh-footer-col-title">NAVIGASI</div>'
        '<span class="dh-footer-link">Home</span><span class="dh-footer-link">Reveal</span>'
        '<span class="dh-footer-link">Tutorial</span><span class="dh-footer-link">Blog</span></div>'
        '<div><div class="dh-footer-col-title">FITUR</div>'
        '<span class="dh-footer-link">Ramalan Harian</span>'
        '<span class="dh-footer-link">Tarot 1 Kartu</span>'
        '<span class="dh-footer-link">Tarot Spreads Multi-Kartu</span>'
        '<span class="dh-footer-link">Cek Kecocokan</span>'
        '<span class="dh-footer-link highlight">🎁 Program Referral</span>'
        '<span class="dh-footer-link">Daftar Harga &amp; VIP</span></div>'
        '<div><div class="dh-footer-col-title">BANTUAN</div>'
        '<span class="dh-footer-link">FAQ</span><span class="dh-footer-link">Contact</span>'
        '<span class="dh-footer-link">Privacy Policy</span><span class="dh-footer-link">Terms of Service</span></div>'
        '</div>'
        '<div class="dh-footer-bottom">'
        '<span>© 2026 Destiny Reveal · By Zio</span>'
        '<em>Dirancang dengan cinta untuk eksplorasi diri sejati</em>'
        '</div></div>',
        unsafe_allow_html=True,
    )


# ══════════════════════════════════════════════════════════════
# ENTRY POINT
# ══════════════════════════════════════════════════════════════
def render(semua_sistem_list):
    """semua_sistem_list: list tuple (nama, icon, apa_ini, topik_list, ajakan, aktif)
    persis format SEMUA_SISTEM di app.py."""
    lookup = {nama: (apa_ini, topik_list, ajakan, aktif) for nama, icon, apa_ini, topik_list, ajakan, aktif in semua_sistem_list}

    # Root container: 1 key buat scope SEMUA css tombol (primary/secondary
    # pill) di Home, biar gak bocor ke halaman lain (reveal/tutorial/dll).
    with st.container(key="dh_home_root"):
        _render_hero()

        with st.container(key="dh_section_matrix"):
            _render_matrix_diagram(lookup)

        _render_social_proof()

        # NOTE: section wrapper WAJIB st.container(key=...) asli, bukan
        # markdown div open/close di 2 pemanggilan terpisah — itu gak
        # bener-bener membungkus di DOM (lihat docs/bugs-fixed.md).
        with st.container(key="dh_section_explore"):
            _render_explore()

        with st.container(key="dh_section_dataflow"):
            _render_dataflow()

        with st.container(key="dh_section_testimonials"):
            _render_testimonials()

        with st.container(key="dh_section_finalcta"):
            _render_final_cta()

        _render_footer()
