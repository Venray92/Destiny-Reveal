"""
Section-section halaman Home v2 (hero, diagram matrix, social proof, jelajahi,
satu-data, testimoni, CTA akhir, footer). Dipanggil dari views/home_v2.py.
CSS: assets/css/parts/*.css, dimuat urut nama (namespace "dh-").
"""

import base64
import math
from functools import lru_cache
from pathlib import Path

import streamlit as st

from components.system_info import open_from_node
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
        '<span class="dh-hero-sub-dark">Satu pembacaan lengkap dari 15 sistem ini akan menunjukkan potensi, kelebihan, '
        'kelemahan, dan langkah yang sebaiknya kamu ambil.</span>'
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
                # normalnya diambil alih JS (smooth scroll tanpa rerun); ini fallback kalau JS belum aktif
                st.session_state.dh_pending_scroll = "dh-explore"
                st.rerun()
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
            f'.st-key-dhmatrix_wrap:has(.st-key-dhnode_{i}:hover) .dh-matrix-lines line:nth-child({i + 1})'
            f' {{ stroke: #C25E00; stroke-width: 2.5; stroke-dasharray: none; opacity: 1; }}'
            f'.st-key-dhnode_{i} {{ top: {top:.2f}%; left: {left:.2f}%; }}'
            f'.st-key-dhmatrix_wrap .st-key-dhnode_{i} div.stButton > button {{'
            f' background: {warna} !important; border-color: {warna} !important; }}'
            f'.st-key-dhmatrix_wrap .st-key-dhnode_{i} div.stButton > button span[data-testid="stIconMaterial"] {{'
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
                    st.button(" ", key=f"dhnbtn_{i}", icon=f":material/{icon}:", on_click=open_from_node, args=(nama,))
                    st.markdown(f'<div class="dh-matrix-node-label">{nama}</div>', unsafe_allow_html=True)
        st.markdown('<div class="dh-matrix-caption">Klik pada ikon lingkaran untuk membaca ringkasan sistem</div>',
                    unsafe_allow_html=True)



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
# EXPLORE SECTION (REVISI01: grid 6 kategori + modal hero-animation)
# Kartu = HTML statis; animasi kartu -> modal dikerjakan JS di navbar.py (CAT_JS).
# Isi modal disimpan di .dh-cat-data (tersembunyi) dan diklon JS saat kartu diklik.
# ══════════════════════════════════════════════════════════════
_WRENCH_D = ("M22.7 19l-9.1-9.1c.9-2.3.4-5-1.5-6.9-2-2-5-2.4-7.4-1.3L9 6 6 9 1.9 4.9C.8 7.3 1.2 10.2 3.2 12.1"
             "c1.9 1.9 4.6 2.4 6.9 1.5l9.1 9.1c.4.4 1 .4 1.4 0l2.1-2.1c.5-.4.5-1 0-1.6z")


def _wrench(size, color="#C86235"):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="{color}"><path d="{_WRENCH_D}"/></svg>'


def _ov_item(title, sub, right, modal=None, reveal=False):
    cls = "dh-open-reveal" if reveal else ("dh-open-modal" if modal else "")
    dm = f' data-modal="{modal}"' if modal and not reveal else ""
    return (f'<a href="#dh-soon" class="dh-ov-item {cls}"{dm}><div><div class="dh-ov-item-title">{title}</div>'
            f'<div class="dh-ov-item-sub">{sub}</div></div>{right}</a>')


def _ov_price(txt):
    return f'<span class="dh-ov-price">{txt}</span>'


_ARROW = '<span class="dh-ov-arrow">→</span>'


def _categories():
    soon = ('<div class="dh-ov-soon"><div class="dh-ov-soon-ic">' + _wrench(30) + '</div>'
            '<div class="dh-ov-soon-t">Coming Soon</div>'
            '<div class="dh-ov-soon-s">Fitur ini sedang dalam pengembangan.</div></div>')
    # (key, ikon, judul, sub, badge, kelas badge, isi modal)
    return [
        ("daily", "🌅", "Daily Free Reveal", "Gratis · Aktivitas harian · Reward", "GRATIS", "free",
         _ov_item("Ramalan Kartu Harian", "Cek pesan harian &amp; energi takdirmu hari ini", _ARROW, "daily")
         + _ov_item("Gacha Kartu Tarot", "Tarik 1 kartu tarot harianmu untuk petunjuk singkat hari ini", _ARROW, "tarot")
         + _ov_item("Skor Energi Hari Ini", "Ukur skor energi harianmu 0–100 dari 4 sistem", _ARROW, "energi")
         + _ov_item("Afirmasi Harian", "Dapatkan kalimat penguat jiwa &amp; panduan langkah kecil harian", _ARROW, "afirmasi")
         + _ov_item("Kalender Energi", "Peta tanggal baik bisnis, potensi konflik &amp; hari hoki romansa", _ARROW, "kalender")
         + _ov_item("Preview Zodiak", "Ringkasan karakter rasi bintang, elemen &amp; quote inspiratif", _ARROW, "preview")
         + _ov_item("Daily Checkin", "Klaim bonus Stardust gratis dengan check-in rutin", _ARROW, "streak")),
        ("self", "🎯", "Self Discovery", "Karakter · Potensi · Identitas · Siklus hidup", "PREMIUM", "prem",
         _ov_item("One-System Blueprint", "Analisis Standar 6 aspek kehidupan dari 1 sistem pilihanmu", _ARROW, "solo")
         + _ov_item("Career DNA", "Bedah potensi karier, peran ideal &amp; rencana sukses 30 hari", _ARROW, "career")
         + _ov_item("Strength &amp; Blind Spot", "Mengenali kekuatan tersembunyi &amp; titik buta yang perlu dikelola", _ARROW, "strength")
         + _ov_item("Blueprint Mendalam", "Laporan 13 aspek (A–M) untuk 1 atau 15 sistem, plus Grand Synthesis &amp; roadmap 10 tahun", _ARROW, "blueprint")
         + _ov_item("Multi-System Blueprint", "Baca 5 sistem kelahiran, 5 sistem psikologi, atau 15 sistem sekaligus dalam satu laporan", _ARROW, reveal=True)),
        ("rel", "💞", "Relationships", "Pasangan · Sahabat · Keluarga · Partner bisnis", "PREMIUM", "prem",
         _ov_item("Soul Match Asmara", "Cek tingkat kecocokan, dinamika hubungan &amp; potensi konflik pasangan", _ARROW, "compat_asmara")
         + _ov_item("Soul Match Keluarga", "Pahami pola komunikasi &amp; cara mempererat hubungan dengan keluarga", _ARROW, "compat_keluarga")
         + _ov_item("Soul Match Teman", "Cek chemistry, kekuatan &amp; tantangan persahabatan plus saran merawatnya", _ARROW, "compat_teman")
         + _ov_item("Soul Match Partner Bisnis", "Cek kecocokan kerja sama, saran pembagian peran &amp; potensi gesekan", _ARROW, "compat_bisnis")),
        ("guid", "🧭", "Guidance &amp; Timing", "Tarot · Weekly · Monthly · Decision Reveal", "PREMIUM", "prem",
         _ov_item("Tarot Spread", "Pembacaan 3, 5, hingga 10 kartu untuk gambaran alur situasi rumit", _ARROW, "tarot_spread")
         + _ov_item("Decision Reveal", "Bimbang dua pilihan? Bandingkan opsi A vs B dengan tebaran 7 kartu tarot", _ARROW, "decision")
         + _ov_item("Yearly Forecast", "Proyeksi 12 bulan kurva energi, siklus keberuntungan &amp; tantangan personalmu", _ARROW, "yearly")
         + _ov_item("Weekly &amp; Monthly Report", "Panduan timing mingguan &amp; bulanan: navigasi siklus rezeki, energi puncak, serta momentum keputusan terbaik",
                    _ARROW, "weekly")),
        ("biz", "💼", "Destiny Business", "Team insights · Leadership · Organizational development", "COMING SOON", "soon", soon),
        ("my", "📔", "My Destiny", "Journal · Timeline · Goals · History · Reflection", "COMING SOON", "soon", soon),
    ]


def render_explore():
    st.markdown('<div id="dh-explore" class="dh-anchor"></div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="dh-section-head">'
        '<div class="dh-section-title">Jelajahi Destiny Reveal</div>'
        '<div class="dh-section-sub">Pilih kategori yang mau kamu eksplorasi hari ini.</div>'
        '</div>',
        unsafe_allow_html=True,
    )
    cards = ""
    for key, icon, title, sub, badge, bcls, body in _categories():
        wrench = _wrench(11, "#8A8178") + " " if bcls == "soon" else ""
        cards += (
            f'<div class="dh-cat" data-cat="{key}" role="button" tabindex="0">'
            '<span class="dh-cat-deco"></span>'
            f'<div class="dh-cat-icon">{icon}</div>'
            f'<div class="dh-cat-title">{title}</div>'
            f'<div class="dh-cat-sub">{sub}</div>'
            '<div class="dh-cat-line"></div>'
            f'<span class="dh-cat-badge {bcls}">{wrench}{badge}</span>'
            f'<div class="dh-cat-data" style="display:none">{body}</div></div>'
        )
    st.markdown(f'<div class="dh-cat-grid">{cards}</div>', unsafe_allow_html=True)


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
         "Suka banget sama fitur Soul Match! Aku sama pacar jadi lebih ngerti cara komunikasi masing-masing."),
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
                    f'<div><div class="dh-testi-name">{name}</div>'
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
        '<a href="#dh-soon" class="dh-footer-link dh-open-modal" data-modal="tutorial">Tutorial</a><a href="#dh-soon" class="dh-footer-link dh-open-modal" data-modal="blog">Blog</a></div>'
        '<div><div class="dh-footer-col-title">FITUR</div>'
        '<a href="#dh-soon" class="dh-footer-link dh-open-modal" data-modal="daily">Ramalan Kartu Harian</a><a href="#dh-soon" class="dh-footer-link dh-open-modal" data-modal="tarot">Gacha Kartu Tarot</a>'
        '<a href="#dh-soon" class="dh-footer-link dh-open-modal" data-modal="tarot_spread">Tarot Spread</a><a href="#dh-soon" class="dh-footer-link dh-open-modal" data-modal="compat">Soul Match</a>'
        '<a href="#dh-soon" class="dh-footer-link highlight dh-open-modal" data-modal="pricing_ref">🎁 Program Referral</a><a href="#dh-soon" class="dh-footer-link dh-open-modal" data-modal="pricing">Daftar Harga &amp; VIP</a></div>'
        '<div><div class="dh-footer-col-title">BANTUAN</div>'
        '<a href="#dh-soon" class="dh-footer-link dh-open-modal" data-modal="faq">FAQ</a><a href="#dh-soon" class="dh-footer-link dh-open-modal" data-modal="contact">Contact</a>'
        '<a href="#dh-soon" class="dh-footer-link dh-open-modal" data-modal="privacy">Privacy Policy</a><a href="#dh-soon" class="dh-footer-link dh-open-modal" data-modal="terms">Terms of Service</a></div>'
        '</div>'
        '<div class="dh-footer-bottom">'
        '<span>© 2026 Destiny Reveal · By Zio</span>'
        '<em>Dirancang dengan cinta untuk eksplorasi diri sejati</em>'
        '</div></div>',
        unsafe_allow_html=True,
    )
