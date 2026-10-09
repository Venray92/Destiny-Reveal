"""
Modal fitur (UI14): Tarot Spreads, Soul Match, Weekly & Monthly Report,
Deep Blueprint, Tutorial, Blog, FAQ & Bantuan. Dibuka dari kartu di section Jelajahi
(class .dh-open-modal + data-modal -> tombol tersembunyi di navbar.py).
DUMMY: saldo belum dipotong, tebaran/sinergi/laporan belum ada backend (toast).
"""

import html

import streamlit as st
from content import pricing as P

from components import auth
from components import close_confirm as cc
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
        "tab": "Tarot 3 Kartu", "koin": P.TAROT[3], "title": "Tarot 3 Kartu",
        "desc": "Masa Lalu, Masa Kini, Masa Depan. Membaca alur waktu energimu dengan cepat dan akurat.",
        "pos": [
            ("1. Masa Lalu", "Fondasi, pengalaman lampau, atau karma awal yang membentuk situasimu saat ini."),
            ("2. Masa Kini", "Energi dominan, tantangan langsung, dan keadaan batinmu hari ini."),
            ("3. Masa Depan", "Arah potensi perkembangan dan hasil terdekat jika energimu tetap konsisten."),
        ],
    },
    5: {
        "tab": "Tarot 5 Kartu", "koin": P.TAROT[5], "title": "Tarot 5 Kartu",
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
        "tab": "Tarot Celtic Cross", "koin": P.TAROT[10], "title": "Tarot Celtic Cross",
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


_TS_KEYS = ("dh_ts_step", "dh_ts_cards", "dh_ts_open", "dh_ts_seen", "dh_ts_pending", "dh_ts_showcombo", "dh_ts_active", "dh_ts_new")


def _ts_reset():
    for k in _TS_KEYS:
        st.session_state.pop(k, None)
    cc.cb_stay("tarot_spread")


def _cb_ts_dismiss():
    """X / klik luar: hasil tebaran -> tanya konfirmasi dulu; layar peringatan -> buang hasil (loading nggak bisa ditutup)."""
    step = st.session_state.get("dh_ts_step")
    if step == "result":
        cc.dismiss("tarot_spread", True, leave=_ts_reset)
    elif step == "warn":
        _ts_reset()


def _cb_ts_go():
    """Bayar (potong SD dummy) lalu tarik kartu & masuk layar loading."""
    import random
    from engine.tarot import TAROT_DECK
    ss = st.session_state
    n = ss.get("dh_ts_tab", 3)
    u = auth.current_user()
    if not u or u.get("koin", 0) < _SPREADS[n]["koin"]:
        return
    u["koin"] -= _SPREADS[n]["koin"]
    ss.dh_ts_cards = random.sample(TAROT_DECK, n)
    ss.dh_ts_open, ss.dh_ts_seen, ss.dh_ts_showcombo = [], False, False
    ss.dh_ts_step = "loading"


def _cb_ts_pick(i):
    """Klik kartu: kalau masih tertutup -> terbuka (flip); lalu jadi kartu aktif."""
    ss = st.session_state
    o = ss.setdefault("dh_ts_open", [])
    if i not in o:
        o.append(i)
        ss.dh_ts_new = i
    ss.dh_ts_active = i


def _cb_ts_all():
    ss = st.session_state
    n = len(ss.get("dh_ts_cards", []))
    ss.dh_ts_open = list(range(n))
    ss.dh_ts_new = None
    if ss.get("dh_ts_active") is None:
        ss.dh_ts_active = 0


def _cb_ts_combo():
    st.session_state.dh_ts_seen = True
    st.session_state.dh_ts_showcombo = True


def _ts_need_warn(combo):
    ss = st.session_state
    return bool(combo) and not ss.get("dh_ts_seen")


def _cb_ts_leave(action, combo):
    """Tebar ulang / sinkron: kalau ada combo yang belum dibuka -> layar peringatan dulu."""
    ss = st.session_state
    if _ts_need_warn(combo):
        ss.dh_ts_pending, ss.dh_ts_step = action, "warn"
    else:
        ss.dh_ts_pending = action
        _ts_do_pending()


def _ts_do_pending():
    ss = st.session_state
    act = ss.pop("dh_ts_pending", None)
    if act == "again":
        keep = ss.get("dh_ts_tab", 3)
        _ts_reset()
        ss.dh_ts_tab, ss.dh_ts_step = keep, "intro"
    elif act == "sync":
        _ts_reset()
        ss.dh_ts_sync = True
    elif act == "close":  # Selesai & Tutup -> layar konfirmasi tutup
        ss.dh_ts_step = "result"
        cc.cb_ask("tarot_spread")


def _cb_ts_see_combo():
    st.session_state.dh_ts_step = "result"
    _cb_ts_combo()
    st.session_state.pop("dh_ts_pending", None)


def _ts_intro():
    ss = st.session_state
    _top(key="ts")
    tab = ss.setdefault("dh_ts_tab", 3)
    if tab not in _SPREADS:
        tab = ss.dh_ts_tab = 3
    with st.container(key="dhts_tabs"):
        cols = st.columns(3, gap="small")
        for col, (n, sp) in zip(cols, _SPREADS.items()):
            with col:
                coin = f"{sp['koin']} ✨" if n == tab else f":orange[{sp['koin']} ✨]"
                st.button(f"{sp['tab']}  \n{coin}", key=f"dhts_tab_{n}", on_click=_cb_ts_tab, args=(n,),
                          type="primary" if n == tab else "secondary", use_container_width=True)
    sp = _SPREADS[tab]
    st.markdown(
        '<div class="dh-fm-center dh-ts-short"><div class="dh-fm-ico dh-fm-ico-lg">🎴</div>'
        f'<div class="dh-fm-h2">{sp["title"]}<span class="dh-fm-badge">{sp["koin"]} ✨</span></div>'
        f'<div class="dh-fm-desc">{sp["desc"]}</div></div>', unsafe_allow_html=True)
    cards = "".join(f'<div><b>{html.escape(a)}</b><span>{html.escape(b)}</span></div>' for a, b in sp["pos"])
    st.markdown(f'<div class="dh-fm-pos dh-ts-short"><div class="dh-fm-poshead">POSISI KARTU DALAM TEBARAN ({tab} KARTU):</div>'
                f'<div class="dh-fm-posgrid">{cards}</div></div>', unsafe_allow_html=True)
    u = auth.current_user()
    with st.container(key="dhfm_cta_ts"):
        if not u:
            if st.button("Masuk / Daftar untuk Membuka Tebaran →", key="dhts_login", type="primary", use_container_width=True):
                from components.dialog_bus import request_with_return
                request_with_return("auth", "tarot_spread")
        elif u.get("koin", 0) < sp["koin"]:
            if st.button("Top-up Saldo →", key="dhts_topup", type="primary", use_container_width=True):
                from components.dialog_bus import request_with_return
                request_with_return("pricing_keep", "tarot_spread", dh_pr_tab="koin")
        else:
            st.button(f"✨ Kocok & Buka Tebaran ({sp['koin']} ✨)", key="dhts_go", type="primary",
                      use_container_width=True, on_click=_cb_ts_go)
    st.markdown(f'<div class="dh-fm-saldo">Saldo-mu saat ini: <b>{saldo()} ✨</b></div>', unsafe_allow_html=True)


def _ts_loading():
    import time
    from components.mini_modals import _loadcard_uri
    ss = st.session_state
    sp = _SPREADS[ss.get("dh_ts_tab", 3)]
    lc = _loadcard_uri()
    st.markdown(
        '<div class="dh-step dh-step-fm dh-step-tsload"></div><div class="dh-nodismiss"></div>'
        f'<div class="dh-ts-badgewrap"><span class="dh-fm-badge dh-ts-badge">{sp["tab"]}</span></div>'
        + (f'<div class="dh-tr-shuf"><img src="{lc}" alt="Deck kosmik"></div>' if lc else '<div class="dh-tr-shuf"><i></i></div>')
        + '<div class="dh-tr-shuft">Mengocok 78 Arcana Kosmik...</div>'
        '<div class="dh-tr-shufs">Menghubungkan frekuensi batinmu dengan tebaran kartu</div>',
        unsafe_allow_html=True)
    time.sleep(3)
    ss.dh_ts_step = "result"
    st.rerun(scope="fragment")


def _ts_info(slug):
    from content.result_builder import build_display_data
    from engine.tarot import TAROT_MAJOR_ARCANA
    c = build_display_data("Tarot", {"kartu": slug}) or {}
    nama, _, arti = (c.get("title") or slug).partition(", ")
    idx = TAROT_MAJOR_ARCANA.index(slug) if slug in TAROT_MAJOR_ARCANA else None
    return c, nama, arti, idx


def _ts_tile(slug, i, is_open, is_active, is_new):
    """HTML 1 kartu: tertutup = sunmoon + BUKA; terbuka = art kartu (Minor: kotak kosong) + nama."""
    from components.mini_modals import _cover_uri
    from utils.card_images import card_image_data_uri, tarot_relative_path
    e = html.escape
    cls = "dh-ts-tile" + (" is-open" if is_open else "") + (" is-active" if is_active else "")
    if not is_open:
        uri = _cover_uri()
        art = (f'<div class="dh-tr-crop"><img class="dh-tr-cimg" src="{uri}" alt="Kartu tertutup"></div>' if uri
               else '<div class="dh-tr-img dh-tr-ph">🂠</div>')
        return (f'<div class="{cls}"><div class="dh-ts-num">{i + 1}</div><div class="dh-ts-art">{art}'
                '<span class="dh-ts-buka">BUKA</span></div><div class="dh-ts-name dh-ts-lock">Terkunci</div></div>')
    _c, nama, _arti, idx = _ts_info(slug)
    _rp = tarot_relative_path(slug)
    uri = card_image_data_uri(_rp) if _rp else None
    if uri:
        _tag = f'<span class="dh-ts-idx">#{idx}</span>' if idx is not None else ""
        art = f'<img class="dh-tr-img dh-ts-img" src="{uri}" alt="{e(nama)}">{_tag}'
    else:  # Minor: gambar belum ada -> kotak kosong
        art = '<div class="dh-tr-img dh-tr-ph dh-ts-img" style="aspect-ratio:870/1164"></div>'
    flip = " dh-ts-flip" if is_new else ""
    return (f'<div class="{cls}"><div class="dh-ts-num">{i + 1}</div><div class="dh-ts-art{flip}">{art}</div>'
            f'<div class="dh-ts-name">{e(nama)}</div></div>')


def _ts_reading(slug, pos):
    from components.mini_modals import _first_sentences
    c, nama, arti, idx = _ts_info(slug)
    dom = c.get("domains") or {}
    e = html.escape
    judul = f"Arcana #{idx}: {nama}" if idx is not None else nama
    chip = f'<span class="dh-ts-chip">{e(arti)}</span>' if arti else ""
    blocks = [("Tentang Kartu Ini", _first_sentences(c.get("p1", ""), 2)),
              ("Karier & Rezeki", _first_sentences(dom.get("karir", ""), 2)),
              ("Asmara & Relasi", _first_sentences(dom.get("asmara", ""), 2))]
    rest = "".join(f'<div class="dh-ts-rl"><b>{a}</b><p>{e(t)}</p></div>' for a, t in blocks if t)
    adv = f'<div class="dh-ts-adv"><b>💬 Nasihat Utama:</b> {e(c["quote"])}</div>' if c.get("quote") else ""
    return (f'<div class="dh-ts-read"><div class="dh-ts-rpos">{e(pos[0].upper())}</div>'
            f'<div class="dh-ts-rhead"><div class="dh-ts-rname">{e(judul)}</div>{chip}</div>'
            f'<div class="dh-ts-rl dh-ts-rmean"><b>Makna Posisi Ini:</b> {e(pos[1])}</div>{adv}{rest}</div>')


def _ts_result():
    from components.modal_detail import render_combo_card
    from components.tarot_combo import build_tarot_combo
    ss = st.session_state
    tab = ss.get("dh_ts_tab", 3)
    sp = _SPREADS[tab]
    cards = ss.get("dh_ts_cards") or []
    if len(cards) != tab:
        _ts_reset()
        st.rerun(scope="fragment")
    opened = ss.setdefault("dh_ts_open", [])
    active, new = ss.get("dh_ts_active"), ss.get("dh_ts_new")
    combo = build_tarot_combo(cards)
    st.markdown('<div class="dh-step dh-step-detail dh-step-tsres"></div><div class="dh-nodismiss"></div>',
                unsafe_allow_html=True)
    h1, h2 = st.columns([2.6, 1.3], gap="small", vertical_alignment="center")
    with h1:
        st.markdown(f'<div class="dh-ts-eyebrow">{html.escape(sp["tab"]).upper()}</div>'
                    '<div class="dh-ts-hint">Ketuk kartu untuk membukanya, atau buka sekaligus.</div>', unsafe_allow_html=True)
    with h2:
        if len(opened) < tab:
            with st.container(key="dhts_openall"):
                st.button("Buka Semua Kartu", key="dhts_all", on_click=_cb_ts_all, use_container_width=True)
    st.markdown('<div class="dh-ts-sep"></div>', unsafe_allow_html=True)
    per_row = 3 if tab == 3 else 5
    with st.container(key="dhts_grid"):
        for r0 in range(0, tab, per_row):
            cols = st.columns(per_row, gap="small")
            for j, col in enumerate(cols):
                i = r0 + j
                if i >= tab:
                    continue
                with col:
                    with st.container(key=f"dhtsk_{i}"):
                        st.markdown(_ts_tile(cards[i], i, i in opened, active == i, new == i), unsafe_allow_html=True)
                        st.button("Pilih", key=f"dhtso_{i}", on_click=_cb_ts_pick, args=(i,))
    if active is not None and active in opened:
        st.markdown(_ts_reading(cards[active], sp["pos"][active]), unsafe_allow_html=True)
    else:
        st.markdown('<div class="dh-ts-empty">Pilih satu kartu untuk membaca penjelasannya.</div>', unsafe_allow_html=True)
    if combo and len(opened) >= tab:
        if ss.get("dh_ts_showcombo"):
            with st.container(key="dhts_combo"):
                render_combo_card(sp["title"], combo)
        else:
            with st.container(key="dhts_combobtn"):
                st.button("✨ Lihat Hasil Analisis Kombinasi Kartu ✨", key="dhts_combo_btn", on_click=_cb_ts_combo)
    with st.container(key="dhts_acts"):
        st.button("← Tebar Ulang / Pilih Jenis Spread Lain", key="dhts_again", use_container_width=True,
                  on_click=_cb_ts_leave, args=("again", combo))
        st.button("Sinkronkan ke Cetak Biru Takdir →", key="dhts_sync", type="primary", use_container_width=True,
                  on_click=_cb_ts_leave, args=("sync", combo))
        st.button("Selesai & Tutup", key="dhts_done", type="primary", use_container_width=True,
                  on_click=_cb_ts_leave, args=("close", combo))


def _ts_warn():
    st.markdown('<div class="dh-step dh-step-fm"></div><div class="dh-nodismiss"></div>'
                '<div class="dh-ts-warn"><div class="dh-ts-warnico">⚠️</div>'
                '<div class="dh-ts-warnt">Ada Analisis Kombinasi yang Belum Kamu Lihat</div>'
                '<div class="dh-ts-warns">Kombinasi kartu di tebaranmu punya pembacaan khusus. Kalau lanjut sekarang, '
                'hasil tebaran ini akan hilang dan kamu tidak bisa membukanya lagi.</div></div>', unsafe_allow_html=True)
    st.button("✨ Lihat Analisis Kombinasi Dulu", key="dhts_w_see", type="primary", use_container_width=True,
              on_click=_cb_ts_see_combo)
    st.button("Tetap Lanjut", key="dhts_w_go", use_container_width=True, on_click=_ts_do_pending)


@st.dialog("Tarot Spreads", width="large", on_dismiss=_cb_ts_dismiss)
def tarot_spread_dialog():
    ss = st.session_state
    step = ss.get("dh_ts_step", "intro")
    if step == "loading" and ss.get("dh_ts_cards"):
        _ts_loading()
    elif step == "result" and ss.get("dh_ts_cards"):
        if cc.asking("tarot_spread"):
            cc.render("tarot_spread", leave=_ts_reset, icon="🃏", title="Yakin Mau Tutup Tebaran Kartumu?",
                      text="Kartu-kartu yang baru kamu buka membawa pesan khusus untukmu. Kalau ditutup, tebaran ini hilang dan tidak bisa dibuka lagi.",
                      tip="Baca semua kartu dan analisis kombinasinya dulu sebelum pergi.",
                      stay="✨ Lanjut Baca Kartu", go="Ya, Tutup Tebaran")
        else:
            _ts_result()
    elif step == "warn" and ss.get("dh_ts_cards"):
        _ts_warn()
    else:
        if ss.get("dh_ts_sync"):  # habis "Tetap Lanjut" -> sinkron
            ss.pop("dh_ts_sync", None)
            request_open("reveal")
        _ts_intro()


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


# Weekly/Monthly Report & Deep Blueprint: versi baru (modal besar) ada di file sendiri
from components.weekly_report import weekly_dialog  # noqa: E402
from components.blueprint import blueprint_dialog  # noqa: E402


def _open_spread(n):
    _ts_reset()  # buka dari kartu Jelajahi = mulai dari awal
    st.session_state.dh_ts_tab = n
    tarot_spread_dialog()


DIALOGS = {
    "tarot_spread_3": lambda: _open_spread(3), "tarot_spread_5": lambda: _open_spread(5),
    "tarot_spread_10": lambda: _open_spread(10),
    "tarot_spread": tarot_spread_dialog, "weekly": weekly_dialog,
    "blueprint": blueprint_dialog, 
}
