"""
Modal fitur (UI14): Tarot Spreads Multi-Kartu, Cek Kecocokan, Weekly & Monthly Report,
Deep Blueprint, Tutorial, Blog, FAQ & Bantuan. Dibuka dari kartu di section Jelajahi
(class .dh-open-modal + data-modal -> tombol tersembunyi di navbar.py).
DUMMY: Stardust belum dipotong, tebaran/sinergi/laporan belum ada backend (toast).
"""

import html

import streamlit as st

from components import auth
from components.dialog_bus import request_open

_COIN_TOAST = "Fitur ini belum tersedia — masih tahap pengembangan 🚧"
_LOGIN_LINK = "Login buat Sync Data"


# ─────────────── header & helper bersama ───────────────
def _top(login_link=True, key="x"):
    """Baris status atas modal: badge akun/tamu (kiri) + link 'Login buat Sync Data' (kanan)."""
    u = auth.current_user()
    if u:
        badge = f'<b class="dh-fm-ok">✓ Akun Terhubung ({html.escape(u["email"])})</b>'
    else:
        badge = '<b class="dh-fm-guest">👤 Mode Tamu (Disimpan di Browser)</b>'
    show_link = login_link and not u
    st.markdown('<div class="dh-step dh-step-fm"></div>', unsafe_allow_html=True)
    c1, c2, _x = st.columns([3.2, 1.5, 0.4], gap="small", vertical_alignment="center")
    with c1:
        st.markdown(f'<div class="dh-fm-status"><span>Status:</span>{badge}</div>', unsafe_allow_html=True)
    with c2:
        if show_link:
            with st.container(key=f"dhfm_login_{key}"):
                if st.button(_LOGIN_LINK, key=f"dhfm_loginbtn_{key}"):
                    request_open("auth")
    st.markdown('<div class="dh-fm-div"></div>', unsafe_allow_html=True)


def _title(icon, title, sub, badge=""):
    b = f'<span class="dh-fm-badge">{badge}</span>' if badge else ""
    st.markdown(
        f'<div class="dh-fm-title"><div class="dh-fm-ico">{icon}</div><div>'
        f'<div class="dh-fm-h">{title}{b}</div><div class="dh-fm-sub">{sub}</div></div></div>',
        unsafe_allow_html=True)


def _close_btn(label, key, outline=False):
    with st.container(key=f"dhfm_{'outline' if outline else 'cta'}_{key}"):
        if st.button(label, key=f"dhfm_btn_{key}", type="secondary" if outline else "primary",
                     use_container_width=True):
            st.rerun()  # rerun penuh = dialog nutup


def _soon(msg=_COIN_TOAST):
    st.toast(msg)


def saldo():
    u = auth.current_user()
    return u["koin"] if u else 0


# ═══════════ 1. TAROT SPREADS MULTI-KARTU ═══════════
_SPREADS = {
    3: {
        "tab": "Tarot 3 Kartu", "koin": 50, "title": "Tarot 3 Kartu",
        "desc": "Masa Lalu, Masa Kini, Masa Depan — Membaca alur waktu energimu dengan cepat dan akurat.",
        "pos": [
            ("1. Masa Lalu", "Fondasi, pengalaman lampau, atau karma awal yang membentuk situasimu saat ini."),
            ("2. Masa Kini", "Energi dominan, tantangan langsung, dan keadaan batinmu hari ini."),
            ("3. Masa Depan", "Arah potensi perkembangan dan hasil terdekat jika energimu tetap konsisten."),
        ],
    },
    5: {
        "tab": "Tarot 5 Kartu", "koin": 100, "title": "Tarot 5 Kartu",
        "desc": "Analisis mendalam 5 dimensi: Situasi, Rintangan, Fondasi Bawah Sadar, Solusi Tindakan, dan Hasil.",
        "pos": [
            ("1. Situasi Saat Ini", "Kondisi riil yang sedang kamu hadapi dan pusat perhatian pikiranmu."),
            ("2. Rintangan / Hambatan", "Halangan eksternal atau keraguan batin yang menghambat laju langkahmu."),
            ("3. Fondasi Bawah Sadar", "Motivasi tersembunyi, trauma masa lampau, atau keyakinan yang mengakar kuat."),
            ("4. Saran & Nasihat Praktis", "Langkah taktis terbaik yang disarankan semesta untuk kamu ambil sekarang."),
            ("5. Hasil Potensial", "Resolusi puncak dan transformasi yang akan terwujud dari tindakanmu."),
        ],
    },
    10: {
        "tab": "Tarot Celtic Cross", "koin": 150, "title": "Tarot Celtic Cross",
        "desc": "Format tebaran 10 kartu legendaris paling komprehensif dalam sejarah esoteris Barat.",
        "pos": [
            ("1. Situasi Inti", "Pusat permasalahan atau tema utama hidupmu saat ini."),
            ("2. Rintangan (Crossing)", "Kekuatan yang bertentangan atau menguji ketahananmu."),
            ("3. Mahkota (Pikiran Sadar)", "Tujuan, aspirasi terbaik, atau apa yang kamu harapkan tercapai."),
            ("4. Fondasi (Bawah Sadar)", "Akar psikologis terdalam yang tak terlihat di permukaan."),
            ("5. Masa Lalu Terdekat", "Kejadian baru saja yang efeknya masih terasa kuat hingga kini."),
            ("6. Masa Depan Terdekat", "Peristiwa atau fase baru yang akan segera menyapa dalam hitungan pekan."),
            ("7. Sikap & Kuasa Diri", "Bagaimana caramu memandang dirimu sendiri dalam dinamika ini."),
            ("8. Lingkungan Eksternal", "Pengaruh orang-orang terdekat, keluarga, dan suasana lingkungan sekitarmu."),
            ("9. Harapan & Ketakutan", "Kecemasan terdalam yang perlu dirangkul serta harapan nuraninmu."),
            ("10. Hasil Akhir (Resolusi)", "Klimaks perjalanan takdir dan pelajaran jiwa terbesar yang kamu petik."),
        ],
    },
}


def _cb_ts_tab(n):
    st.session_state.dh_ts_tab = n


@st.dialog("Tarot Spreads Multi-Kartu", width="small")
def tarot_spread_dialog():
    ss = st.session_state
    _top(key="ts")
    tab = ss.setdefault("dh_ts_tab", 3)
    if tab not in _SPREADS:
        tab = ss.dh_ts_tab = 3
    with st.container(key="dhts_tabs"):
        cols = st.columns(3, gap="small")
        for col, (n, sp) in zip(cols, _SPREADS.items()):
            with col:
                coin = f"{sp['koin']} SD" if n == tab else f":orange[{sp['koin']} SD]"
                st.button(f"{sp['tab']}  \n{coin}", key=f"dhts_tab_{n}", on_click=_cb_ts_tab, args=(n,),
                          type="primary" if n == tab else "secondary", use_container_width=True)
    sp = _SPREADS[tab]
    st.markdown(
        '<div class="dh-fm-center"><div class="dh-fm-ico dh-fm-ico-lg">🎴</div>'
        f'<div class="dh-fm-h2">{sp["title"]}<span class="dh-fm-badge">{sp["koin"]} ✨ SD</span></div>'
        f'<div class="dh-fm-desc">{sp["desc"]}</div></div>', unsafe_allow_html=True)
    cards = "".join(f'<div><b>{html.escape(a)}</b><span>{html.escape(b)}</span></div>' for a, b in sp["pos"])
    st.markdown(f'<div class="dh-fm-pos"><div class="dh-fm-poshead">POSISI KARTU DALAM TEBARAN ({tab} KARTU):</div>'
                f'<div class="dh-fm-posgrid">{cards}</div></div>', unsafe_allow_html=True)
    with st.container(key="dhfm_cta_ts"):
        st.button(f"✨ Kocok & Buka Tebaran ({sp['koin']} SD)", key="dhts_go", type="primary",
                  use_container_width=True, on_click=_soon)
    st.markdown(f'<div class="dh-fm-saldo">Saldo Stardust-mu saat ini: <b>{saldo()} ✨ SD</b></div>', unsafe_allow_html=True)


# ═══════════ 2. CEK KECOCOKAN ═══════════
_HARI = {"Minggu": 5, "Senin": 4, "Selasa": 3, "Rabu": 7, "Kamis": 8, "Jumat": 6, "Sabtu": 9}
_PASARAN = {"Legi": 5, "Pahing": 9, "Pon": 7, "Wage": 4, "Kliwon": 8}
WETON_OPTIONS = [f"{h} {p} (Neptu {nh + npn})" for h, nh in _HARI.items() for p, npn in _PASARAN.items()]


@st.dialog("Cek Kecocokan", width="small")
def compat_dialog():
    _top(key="cp")
    _title("💖", "Cek Kecocokan", "Bandingkan 2 orang langsung tanpa perlu scan sebelumnya", badge="100 ✨ SD")
    c1, c2 = st.columns(2, gap="small")
    with c1:
        st.markdown('<div class="dh-fm-label">Orang Pertama</div>', unsafe_allow_html=True)
        st.selectbox("Orang Pertama", WETON_OPTIONS, index=WETON_OPTIONS.index("Senin Pon (Neptu 11)"),
                     key="dhcp_a", label_visibility="collapsed")
    with c2:
        st.markdown('<div class="dh-fm-label">Orang Kedua</div>', unsafe_allow_html=True)
        st.selectbox("Orang Kedua", WETON_OPTIONS, index=WETON_OPTIONS.index("Kamis Kliwon (Neptu 16)"),
                     key="dhcp_b", label_visibility="collapsed")
    with st.container(key="dhfm_cta_cp"):
        st.button("Hitung Sinergi Pasangan (100 SD)", key="dhcp_go", type="primary", use_container_width=True,
                  on_click=_soon)


# ═══════════ 3. WEEKLY & MONTHLY REPORT ═══════════
def _start_scan():
    request_open("reveal")


@st.dialog("Weekly & Monthly Report", width="small")
def weekly_dialog():
    _top(key="wk")
    _title("📊", "Weekly Report (100-200 SD)", "Panduan timing &amp; strategi eksekusi berkala")
    with st.container(key="dhwk_box"):
        st.markdown('<div class="dh-fm-warn"><b>❗ Kamu butuh melakukan scan takdir terlebih dahulu!</b>'
                    '<p>Laporan berkala disusun berdasarkan titik komparasi Weton, BaZi, dan Zodiak hasil scan '
                    'unikmu agar prediksi timing 100% presisi.</p></div>', unsafe_allow_html=True)
        if st.button("Mulai Scan Takdir Dulu →", key="dhwk_go", type="primary", use_container_width=True):
            _start_scan()


# ═══════════ 4. DEEP BLUEPRINT ═══════════
@st.dialog("Deep Blueprint", width="small")
def blueprint_dialog():
    _top(key="bp")
    _title("🔷", "Deep Blueprint", "15 Sistem sekaligus dalam 1 laporan lengkap (VIP Only)")
    st.markdown(
        '<div class="dh-fm-info"><p>Deep Blueprint menggabungkan seluruh 15 dimensi: Zodiak, Shio, Weton, Numerologi, '
        'Matrix Destiny, BaZi, Zi Wei, Human Design, MBTI, Big Five, Enneagram, DISC, Love Language, Golongan Darah, '
        'dan Tarot.</p><p class="mut">Disajikan dalam bentuk booklet PDF personal ~18 halaman dengan analisis jalur '
        'kekayaan, penyembuhan luka masa lalu, dan panduan belahan jiwa.</p></div>', unsafe_allow_html=True)
    with st.container(key="dhfm_cta_bp"):
        if st.button("Mulai Pembacaan Mode Lengkap (Mode 3) →", key="dhbp_go", type="primary",
                     use_container_width=True):
            request_open("reveal", dh_modal_mode="lengkap")


# ═══════════ 5-7. TUTORIAL, BLOG, FAQ ═══════════
@st.dialog("Tutorial", width="small")
def tutorial_dialog():
    _top(login_link=False, key="tu")
    st.markdown('<div class="dh-fm-bigtitle">Tutorial</div>'
                '<div class="dh-fm-box"><p><b>Langkah 1:</b> Akses fitur gratis harian (Tarot 1 Kartu, Ramalan Harian, '
                'Streak) tanpa perlu login sama sekali.</p>'
                '<p><b>Langkah 2:</b> Pilih \'Reveal Takdirku\' (Mode 1, Mode 2, atau Mode 3) saat ingin membedah '
                'takdir lengkap.</p>'
                '<p><b>Langkah 3:</b> Masuk via Magic Link instan hanya saat ingin unlock konten berbayar atau '
                'menyimpan hasil cetak biru.</p></div>', unsafe_allow_html=True)
    _close_btn("Mengerti & Kembali", "tu")


@st.dialog("Blog", width="small")
def blog_dialog():
    _top(login_link=False, key="bl")
    st.markdown('<div class="dh-fm-bigtitle">Blog</div>'
                '<div class="dh-fm-box"><p class="dh-fm-q"><b>Kenapa Weton dan MBTI Sering Saling Melengkapi?</b></p>'
                '<p>Weton memetakan temperamen bawaan siklus bumi nusantara, sementara MBTI memotret cara otakmu '
                'mengolah data saat ini. Ketika disandingkan, kita melihat benang merah yang menakjubkan.</p></div>',
                unsafe_allow_html=True)
    _close_btn("Mengerti & Kembali", "bl")


def _open_spread(n):
    st.session_state.dh_ts_tab = n
    tarot_spread_dialog()


DIALOGS = {
    "tarot_spread_3": lambda: _open_spread(3), "tarot_spread_5": lambda: _open_spread(5),
    "tarot_spread_10": lambda: _open_spread(10),
    "tarot_spread": tarot_spread_dialog, "compat": compat_dialog, "weekly": weekly_dialog,
    "blueprint": blueprint_dialog, "tutorial": tutorial_dialog, "blog": blog_dialog,
}
