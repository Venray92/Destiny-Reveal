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

_COIN_TOAST = "Fitur ini belum tersedia, masih tahap pengembangan 🚧"
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
        "desc": "Masa Lalu, Masa Kini, Masa Depan. Membaca alur waktu energimu dengan cepat dan akurat.",
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


# ═══════════ 3. WEEKLY & MONTHLY REPORT ═══════════
def _start_scan():
    request_open("reveal")


_HARI_W = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
_PAS_W = ["Legi", "Pahing", "Pon", "Wage", "Kliwon"]
_SHIO_W = ["Tikus", "Kerbau", "Macan", "Kelinci", "Naga", "Ular", "Kuda", "Kambing", "Monyet", "Ayam", "Anjing", "Babi"]
_ZOD_W = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn",
          "Aquarius", "Pisces"]
# (label field, key field) urutan tampil laporan berkala
_FIELDS = [("timing", "⏱️ Timing"), ("prediksi", "🔮 Prediksi"), ("peluang", "🌱 Peluang"),
           ("saran", "🧭 Saran"), ("hindari", "⚠️ Hindari"), ("hindari_risiko", "⚠️ Risiko yang Perlu Dihindari")]
_EXTRA = [("hari_terbaik", "Hari Terbaik"), ("arah_rezeki", "Arah Rezeki"), ("fokus_mingguan", "Fokus Minggu Ini"),
          ("fokus_bulan_ini", "Fokus Bulan Ini"), ("fase_kunci", "Fase Kunci")]


def _render_periodic(r):
    """Tampilkan satu laporan berkala (dict dari content.periodic)."""
    st.markdown(f'<div class="dh-fm-info"><p><b>Periode: {html.escape(str(r["periode"]))}</b></p></div>',
                unsafe_allow_html=True)
    for f, label in _FIELDS:
        if r.get(f):
            st.markdown(f"**{label}**\n\n{r[f]}")
    chips = [f"{lbl}: {r[f]}" for f, lbl in _EXTRA if r.get(f)]
    if r.get("angka_pendukung"):
        chips.append("Angka Pendukung: " + ", ".join(str(x) for x in r["angka_pendukung"]))
    if chips:
        st.caption("  ·  ".join(chips))


def _render_tarot_periodik(kind):
    """Kartu Tarot pekan/bulan ini (deterministik per periode) + uraian dari JSON."""
    from content.result_builder import build_display_data
    from engine.rotation import BULAN, format_periode_minggu, today_wib
    from engine.tarot import kartu_periodik

    d = today_wib()
    kartu = kartu_periodik(kind)
    c = build_display_data("Tarot", {"kartu": kartu}) or {}
    periode = format_periode_minggu(d) if kind == "weekly" else f"{BULAN[d.month - 1]} {d.year}"
    st.markdown(f'<div class="dh-fm-info"><p><b>Periode: {html.escape(periode)}</b></p></div>', unsafe_allow_html=True)
    st.markdown(f"**🃏 {c.get('title', kartu)}**")
    st.markdown(c.get("p1", ""))
    if c.get("quote"):
        st.caption(c["quote"])
    for lbl, k in (("💼 Karier", "karir"), ("💗 Asmara", "asmara"), ("💰 Keuangan", "keuangan"), ("🌿 Kesehatan", "kesehatan")):
        if (c.get("domains") or {}).get(k):
            st.markdown(f"**{lbl}**\n\n{c['domains'][k]}")
    st.markdown("**🧭 PR Kecil Buat Kamu**\n\n" + c.get("p3", ""))


@st.dialog("Weekly & Monthly Report", width="small")
def weekly_dialog():
    from datetime import date

    from content import periodic

    _top(key="wk")
    _title("📊", "Laporan Mingguan & Bulanan", "Panduan timing &amp; strategi eksekusi berkala")
    tab = st.radio("Periode", ["Mingguan", "Bulanan"], horizontal=True, key="dhwk_tab", label_visibility="collapsed")
    kind = "weekly" if tab == "Mingguan" else "monthly"
    opsi = (["Zodiak", "Shio", "Weton", "Numerologi", "Tarot"] if kind == "weekly"
            else ["Zodiak", "Shio", "Numerologi", "BaZi", "Zi Wei", "Tarot"])
    sistem = st.selectbox("Sistem", opsi, key=f"dhwk_sys_{kind}")
    tgl, key = None, ""
    if sistem == "Zodiak":
        key = st.selectbox("Zodiak kamu", _ZOD_W, key="dhwk_zod")
    elif sistem == "Shio":
        key = st.selectbox("Shio kamu", _SHIO_W, key="dhwk_shio")
    elif sistem == "Weton":
        c1, c2 = st.columns(2)
        h = c1.selectbox("Hari lahir", _HARI_W, key="dhwk_hari")
        p = c2.selectbox("Pasaran", _PAS_W, key="dhwk_pas")
        key = f"{h} {p}"
    elif sistem in ("Numerologi", "BaZi", "Zi Wei"):
        tgl = st.date_input("Tanggal lahir", value=date(1995, 1, 1), min_value=date(1930, 1, 1),
                            max_value=date.today(), key="dhwk_tgl")
        if sistem == "BaZi":
            try:
                from engine.bazi import hitung_bazi
                key = hitung_bazi(tgl)["day_master"]
            except Exception:
                st.info("Hitungan BaZi belum bisa dijalankan untuk tanggal ini.")
                return
        elif sistem == "Zi Wei":
            jam = st.selectbox("Jam lahir", list(range(24)), format_func=lambda j: f"{j:02d}:00", key="dhwk_jam")
            try:
                from engine.ziwei import hitung_ziwei
                zw = hitung_ziwei(tgl, jam)
                slug = {"ziwei": "zi_wei", "tianji": "tian_ji", "taiyang": "tai_yang", "wuqu": "wu_qu",
                        "tiantong": "tian_tong", "lianzhen": "lian_zhen", "tianfu": "tian_fu", "taiyin": "tai_yin",
                        "tanlang": "tan_lang", "jumen": "ju_men", "tianxiang": "tian_xiang",
                        "tianliang": "tian_liang", "qisha": "qi_sha", "pojun": "po_jun"}[zw["bintang"]]
                key = f"{slug}|{zw['ming_gong']}"
            except Exception:
                st.info("Hitungan Zi Wei belum bisa dijalankan untuk data ini.")
                return
    if sistem == "Tarot":
        _render_tarot_periodik(kind)
        return
    if kind == "weekly":
        r = periodic.get_weekly(sistem, key, tgl_lahir=tgl)
    else:
        r = periodic.get_monthly(sistem, key, tgl_lahir=tgl)
    if r:
        _render_periodic(r)
    else:
        st.info("Laporan untuk kombinasi ini belum tersedia.")


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


def _open_spread(n):
    st.session_state.dh_ts_tab = n
    tarot_spread_dialog()


DIALOGS = {
    "tarot_spread_3": lambda: _open_spread(3), "tarot_spread_5": lambda: _open_spread(5),
    "tarot_spread_10": lambda: _open_spread(10),
    "tarot_spread": tarot_spread_dialog, "weekly": weekly_dialog,
    "blueprint": blueprint_dialog, 
}
