"""
Section-section halaman Home v2 (hero, diagram matrix, social proof, jelajahi,
satu-data, testimoni, CTA akhir, footer). Dipanggil dari views/home_v2.py.
CSS: assets/css/home_v2.css (namespace "dh-").
"""

import base64
import math
from functools import lru_cache
from pathlib import Path

import streamlit as st

from components.common import go
from components.data import CATEGORY_SYSTEMS, NODE_COLOR, NODE_ORDER
from components.modal import open_reveal_modal


def _set_category(name):
    st.session_state.dh_cat = name


_CELESTIAL_IMG_PATH = Path(__file__).resolve().parent.parent / "assets" / "images" / "celestial_harmony.jpg"


@lru_cache(maxsize=1)
def _celestial_harmony_b64():
    """Base64 poster 'Celestial Harmony' buat background kartu hero.
    None kalau file-nya belum ke-upload (fallback ke gradient polos)."""
    try:
        return base64.b64encode(_CELESTIAL_IMG_PATH.read_bytes()).decode("utf-8")
    except FileNotFoundError:
        return None


# ══════════════════════════════════════════════════════════════
# HERO
# ══════════════════════════════════════════════════════════════
def render_hero():
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
                open_reveal_modal()
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
def render_matrix_diagram(sistem_lookup):
    st.markdown('<div id="dh-matrix"></div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="dh-section-head">'
        '<div class="dh-section-title">Satu Dirimu, 15 Cara Memandang</div>'
        '<div class="dh-section-sub">Klik tiap sistem untuk melihat penjelasannya.</div>'
        '</div>',
        unsafe_allow_html=True,
    )

    if "dh_cat" not in st.session_state:
        st.session_state.dh_cat = "Semua 15 Sistem"
    active_cat = st.session_state.dh_cat
    lit = CATEGORY_SYSTEMS.get(active_cat)

    # Chip filter = st.button beneran (state di session_state), bukan span statis
    with st.container(key="dhfilter_row"):
        fcols = st.columns(len(CATEGORY_SYSTEMS))
        for col, name in zip(fcols, CATEGORY_SYSTEMS):
            with col:
                st.button(
                    name, key=f"dhfilter_{name}", on_click=_set_category, args=(name,),
                    type="primary" if name == active_cat else "secondary",
                )

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
        dim_css = (
            f'.st-key-dhnode_{i} {{ opacity: 0.25; filter: grayscale(1); }}'
            f'.dh-matrix-lines line:nth-child({i + 1}) {{ opacity: 0.25; }}'
        ) if (lit is not None and nama not in lit) else ''
        label_above = top < 46  # node separuh atas: label di atas ikon
        flip_css = (
            f'.st-key-dhnode_{i} .dh-matrix-node-label {{ position: absolute; bottom: 100%;'
            f' left: 50%; transform: translateX(-50%); margin: 0 0 4px 0; }}'
        ) if label_above else ''
        pos_css.append(
            dim_css + flip_css +
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
def render_social_proof():
    st.markdown(
        '<div class="dh-proof-bar"><span class="dh-proof-dot">●</span>'
        '4.996+ Orang telah menemukan versi terbaik mereka minggu ini.</div>',
        unsafe_allow_html=True,
    )


# ══════════════════════════════════════════════════════════════
# EXPLORE SECTION
# ══════════════════════════════════════════════════════════════
def render_explore():
    st.markdown('<div id="dh-explore" class="dh-anchor"></div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="dh-section-head">'
        '<div class="dh-section-title">Jelajahi Destiny Reveal</div>'
        '<div class="dh-section-sub">Dari yang gratis sampai premium, semua ada di sini.</div>'
        '</div>',
        unsafe_allow_html=True,
    )

    ec1, ec2, ec3 = st.columns(3, gap="medium")

    def _item(title, sub, right):
        # Seluruh kotak = link dummy (href fragmen kosong yang gak ada target-nya,
        # biar klik gak lompat ke atas halaman). Ganti href kalau fiturnya udah jadi.
        return (
            '<a href="#dh-soon" class="dh-explore-item"><div>'
            f'<div class="dh-explore-item-title">{title}</div>'
            f'<div class="dh-explore-item-sub">{sub}</div></div>{right}</a>'
        )

    arrow = '<span class="dh-explore-item-arrow">→</span>'

    def _price(txt, vip=False):
        return f'<span class="dh-explore-item-price{" vip" if vip else ""}">{txt}</span>'

    def _head(icon, bg, title, sub):
        return (
            '<div class="dh-explore-head">'
            f'<div class="dh-explore-icon" style="background:{bg};">{icon}</div>'
            f'<div><div class="dh-explore-title">{title}</div>'
            f'<div class="dh-explore-subtitle">{sub}</div></div></div>'
        )

    # Tiap kartu = st.container(key="dhexplore_card_*") beneran, jadi tombol
    # footer ikut kebungkus di dalam kartu (bukan nongol di luar border).
    with ec1:
        with st.container(key="dhexplore_card_gratis"):
            st.markdown(
                _head("🆓", "#FDF6E3", "GRATIS", "Eksplorasi tanpa biaya harian")
                + _item("Ramalan Harian Gratis", "1x per hari, pilih Zodiak atau Shio", arrow)
                + _item("Tarot 1 Kartu Harian", "Tarik kartu deck tertutup dengan animasi shuffle", arrow)
                + _item("Preview Zodiak", "12 rasi, modality, planet &amp; quote", arrow)
                + _item("Streak &amp; Reward", "5 hari berturut = 1 koin gratis", arrow),
                unsafe_allow_html=True,
            )
            with st.container(key="dhexplore_foot_gratis"):
                if st.button("Mulai Pembacaan Gratis →", key="dhexplore_gratis_btn", use_container_width=True):
                    go("reveal")

    with ec2:
        with st.container(key="dhexplore_card_premium"):
            st.markdown(
                '<div class="dh-explore-card-badge">PAKAI KOIN &amp; VIP</div>'
                + _head("💎", "#eef2fb", "PREMIUM", "Panduan mendalam &amp; akurasi tinggi")
                + _item("Tarot Spreads Multi-Kartu", "3 Kartu (1 Koin), 5 Kartu (2 Koin), Celtic Cross (3 Koin)", _price("1-3 Koin"))
                + _item("Cek Kecocokan", "Bandingkan 2 orang langsung (Weton &amp; Zodiak)", _price("3 Koin"))
                + _item("Weekly &amp; Monthly Report", "Timing pekan (3 Koin) &amp; analisis bulan (5 Koin)", _price("3-5 Koin"))
                + _item("Deep Blueprint (15 Sistem)", "Laporan lengkap 15 sistem sekaligus + PDF", _price("VIP", vip=True)),
                unsafe_allow_html=True,
            )
            with st.container(key="dhexplore_foot_premium"):
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
        with st.container(key="dhexplore_card_lainnya"):
            st.markdown(
                _head("✨", "#f3eefc", "LAINNYA", "Referral, wawasan &amp; bantuan pengguna")
                + _item("🎁 Program Referral &amp; Affiliate", "Komisi 10-30% + Bonus Milestone VIP", arrow)
                + _item("Tutorial", "Panduan pakai website &amp; cara baca hasil", arrow)
                + _item("Blog", "Artikel tentang self-discovery &amp; potensi diri", arrow)
                + _item("FAQ &amp; Bantuan", "Pertanyaan yang sering ditanya", arrow),
                unsafe_allow_html=True,
            )
            with st.container(key="dhexplore_foot_lainnya"):
                if st.button("Tentang Kami — Destiny Reveal", key="dhexplore_about_btn", use_container_width=True):
                    st.toast("Halaman Tentang Kami belum tersedia — masih tahap pengembangan 🚧")


# ══════════════════════════════════════════════════════════════
# DATA FLOW ("Satu Data, Banyak Cara Pandang")
# ══════════════════════════════════════════════════════════════
def render_dataflow():
    st.markdown('<div id="dh-dataflow" class="dh-anchor"></div>', unsafe_allow_html=True)
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

    # 1 markdown = 1 CSS grid (3 kolom). Kartu terakhir ("Tarikan Acak")
    # span 2 kolom biar baris 2 gak bolong; tinggi per baris otomatis sama.
    cards_html = ""
    for idx, (icon, tag, title, desc, items, foot) in enumerate(groups):
        items_html = "".join(f"<li>{it}</li>" for it in items)
        wide = " wide" if idx == len(groups) - 1 else ""
        cards_html += (
            f'<a href="#dh-soon" class="dh-flow-card dh-open-reveal{wide}">'
            '<div class="dh-flow-head">'
            f'<div class="dh-flow-icon"><span class="material-symbols-outlined">{icon}</span></div>'
            f'<span class="dh-flow-tag">{tag}</span></div>'
            f'<div class="dh-flow-title">{title}</div>'
            f'<div class="dh-flow-desc">{desc}</div>'
            f'<ul class="dh-flow-list">{items_html}</ul>'
            f'<div class="dh-flow-foot"><span>{foot}</span><span>→</span></div>'
            '</a>'
        )
    st.markdown(f'<div class="dh-flow-grid">{cards_html}</div>', unsafe_allow_html=True)

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
                open_reveal_modal()


# ══════════════════════════════════════════════════════════════
# TESTIMONIALS
# ══════════════════════════════════════════════════════════════
def render_testimonials():
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
def render_final_cta():
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
            if st.button("→ Reveal Yours~", key="dhfinal_cta_btn", type="primary"):
                open_reveal_modal()
    st.markdown(
        '<p class="dh-finalcta-caption" style="text-align:center;">Gratis · Tanpa akun · 3 menit</p>',
        unsafe_allow_html=True,
    )


# ══════════════════════════════════════════════════════════════
# FOOTER
# ══════════════════════════════════════════════════════════════
def render_footer():
    st.markdown(
        '<div class="dh-footer">'
        '<div style="display:grid;grid-template-columns:1.6fr 1fr 1fr 1fr;gap:24px;">'
        '<div><div class="dh-footer-brand">✦ Destiny Reveal</div>'
        '<div class="dh-footer-tagline">Kenali dirimu, temukan versi terbaikmu.</div>'
        '<div class="dh-footer-note">Satu portal terpadu untuk 15 sistem refleksi jiwa '
        'dan peta takdir holistik.</div></div>'
        '<div><div class="dh-footer-col-title">NAVIGASI</div>'
        '<a href="#dh-top" class="dh-footer-link">Home</a><a href="#dh-soon" class="dh-footer-link dh-open-reveal">Reveal</a>'
        '<a href="#dh-dataflow" class="dh-footer-link">Tutorial</a><a href="#dh-soon" class="dh-footer-link">Blog</a></div>'
        '<div><div class="dh-footer-col-title">FITUR</div>'
        '<a href="#dh-explore" class="dh-footer-link">Ramalan Harian</a><a href="#dh-explore" class="dh-footer-link">Tarot 1 Kartu</a>'
        '<a href="#dh-explore" class="dh-footer-link">Tarot Spreads Multi-Kartu</a><a href="#dh-explore" class="dh-footer-link">Cek Kecocokan</a>'
        '<a href="#dh-explore" class="dh-footer-link highlight">🎁 Program Referral</a><a href="#dh-explore" class="dh-footer-link">Daftar Harga &amp; VIP</a></div>'
        '<div><div class="dh-footer-col-title">BANTUAN</div>'
        '<a href="#dh-soon" class="dh-footer-link">FAQ</a><a href="#dh-soon" class="dh-footer-link">Contact</a>'
        '<a href="#dh-soon" class="dh-footer-link">Privacy Policy</a><a href="#dh-soon" class="dh-footer-link">Terms of Service</a></div>'
        '</div>'
        '<div class="dh-footer-bottom">'
        '<span>© 2026 Destiny Reveal · By Zio</span>'
        '<em>Dirancang dengan cinta untuk eksplorasi diri sejati</em>'
        '</div></div>',
        unsafe_allow_html=True,
    )
