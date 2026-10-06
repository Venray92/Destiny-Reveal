"""
Modal User Profile (UI26): header (Mail + Logout), tab Overview / Referral / Riwayat, form Edit Profil.
State: dh_pf_tab | dh_pf_edit | dh_pf_err | dh_pf_toast. Data profil disimpan di dh_user["profil"] dan
disinkron ke dh_solo_prof supaya autofill Solo Reveal / Cek Kecocokan ikut berubah.
DUMMY: referral, komisi, Mail, dan arsip belum ada backend (session saja).
"""

import html
from datetime import date

import streamlit as st

from components import auth
from components.dialog_bus import request_open
from components.modal_detail import copy_button

TABS = [("overview", "📊 Overview"), ("referral", "🎁 Referral"), ("riwayat", "📜 Riwayat")]
GENDERS = ["Perempuan", "Laki-laki", "Lainnya / Tidak ingin menyebut"]
GOLDA = ["A", "B", "AB", "O", "Belum tahu"]
MAIL_DEMO = 3
# (nama, min teman, komisi, hadiah)
TIERS = [("Stardust", 0, "10%", "Komisi Stardust"), ("Nebula", 10, "12%", "VIP 1 Bulan Gratis"),
         ("Galaxy", 50, "15%", "VIP 1 Tahun Gratis"), ("Cosmic", 100, "15%", "Lifetime VIP 👑")]
FILTERS = ["Semua", "Zodiak", "Shio", "Weton", "MBTI", "Numerologi", "Arsip"]


def _e(t):
    return html.escape(str(t))


def _tier(n):
    cur = 0
    for i, t in enumerate(TIERS):
        if n >= t[1]:
            cur = i
    return cur


# ─────────────── callbacks ───────────────
def _cb_tab(k):
    ss = st.session_state
    ss.dh_pf_tab = k
    ss.dh_pf_edit = False


def _cb_edit_open():
    ss = st.session_state
    u = auth.current_user()
    p = (u or {}).get("profil") or {}
    ss.dhpe_nama = (u or {}).get("nama", "")
    ss.dhpe_tgl = p.get("tgl")
    ss.dhpe_jam = p.get("jam")
    ss.dhpe_kota = p.get("kota", "")
    ss.dhpe_gender = p.get("gender")
    ss.dhpe_golda = p.get("golda") if p.get("golda") in GOLDA else None
    ss.dh_pf_err = None
    ss.dh_pf_edit = True


def _cb_edit_cancel():
    st.session_state.dh_pf_edit = False


def _cb_edit_save():
    ss = st.session_state
    u = auth.current_user()
    nama = (ss.get("dhpe_nama") or "").strip()
    if not nama or not ss.get("dhpe_tgl"):
        ss.dh_pf_err = "Nama dan Tanggal Lahir wajib diisi."
        return
    prof = {"nama": nama, "tgl": ss.dhpe_tgl, "jam": ss.get("dhpe_jam"), "kota": (ss.get("dhpe_kota") or "").strip(),
            "gender": ss.get("dhpe_gender"), "golda": ss.get("dhpe_golda") or ""}
    u["nama"] = nama
    u["profil"] = prof
    ss.dh_solo_prof = {k: prof[k] for k in ("nama", "jam", "kota", "golda", "gender", "tgl")}
    ss.dh_pf_err = None
    ss.dh_pf_edit = False
    ss.dh_pf_toast = "Profil berhasil diperbarui ✓"


def _cb_mail():
    st.session_state.dh_pf_toast = "Kotak masuk belum tersedia, masih tahap pengembangan 🚧"


def _cb_archive(i):
    h = st.session_state.dh_history
    if 0 <= i < len(h):
        h[i]["arsip"] = not h[i].get("arsip")
        st.session_state.dh_pf_toast = "Dipindahkan ke Arsip" if h[i]["arsip"] else "Dikembalikan dari Arsip"


def _cb_delete(i):
    h = st.session_state.dh_history
    if 0 <= i < len(h):
        h.pop(i)
        st.session_state.dh_pf_toast = "Riwayat dihapus"


def _cb_to_referral():
    _cb_tab("referral")


# ─────────────── bagian tampilan ───────────────
def _header(u):
    st.markdown('<div class="dh-step dh-step-pp"></div>', unsafe_allow_html=True)
    hdr = st.container(key="dhpp_top")
    c1, c2, c3, _x = hdr.columns([3.4, 1.15, 1.55, 0.55], gap="small", vertical_alignment="center")
    with c1:
        st.markdown('<div class="dh-pp-head"><span>🏆</span><div><div class="dh-pp-brand">USER PROFILE</div>'
                    '<div class="dh-pp-sub">Destiny Reveal Cosmic Portal</div></div></div>', unsafe_allow_html=True)
    with c2:
        with st.container(key="dhpp_mail"):
            st.button(f"✉️ Mail  {MAIL_DEMO}", key="dhpp_mailbtn", on_click=_cb_mail, use_container_width=True)
    with c3:
        with st.container(key="dhpp_logout"):
            if st.button("🚪 Logout", key="dhpp_logoutbtn", use_container_width=True):
                auth._cb_logout()
    st.markdown('<div class="dh-pp-line"></div>', unsafe_allow_html=True)


def _tabs(tab):
    with st.container(key="dhpp_tabs"):
        cols = st.columns(len(TABS), gap="small")
        for col, (k, lab) in zip(cols, TABS):
            with col:
                st.button(lab, key=f"dhpp_tab_{k}", on_click=_cb_tab, args=(k,),
                          type="primary" if tab == k else "secondary", use_container_width=True)


def _render_overview(u):
    ss = st.session_state
    init = (u["nama"][:2] or "U").upper()
    nref = u.get("ref_count", 0)
    tier = TIERS[_tier(nref)]
    c1, c2 = st.columns([1.5, 1], gap="small")
    with c1:
        with st.container(key="dhpp_user"):
            st.markdown(
                f'<div class="dh-pp-user"><div class="dh-pp-av">{_e(init)}</div><div>'
                f'<div class="dh-pp-name">{_e(u["nama"])}<span>⭐ {tier[0]}</span></div>'
                f'<div class="dh-pp-mail">{_e(u["email"])}</div>'
                f'<div class="dh-pp-since">📅 Anggota sejak {_e(u["joined"])}</div></div></div>', unsafe_allow_html=True)
            st.button("✏️ Edit Profil", key="dhpp_edit", on_click=_cb_edit_open)
    with c2:
        with st.container(key="dhpp_bal"):
            st.markdown(f'<div class="dh-pp-bl">STARDUST BALANCE</div><div class="dh-pp-bv">{u["koin"]:,}'.replace(",", ".")
                        + ' <span>Stardust</span></div>', unsafe_allow_html=True)
            b1, b2 = st.columns(2, gap="small")
            with b1:
                if st.button("Top Up", key="dhpp_topup", type="primary", use_container_width=True):
                    request_open("pricing_keep", dh_pr_tab="koin")
            with b2:
                if st.button("Credits", key="dhpp_credits", use_container_width=True):
                    request_open("pricing_keep", dh_pr_tab="semua")
    st.markdown('<div class="dh-pp-sec">RINGKASAN STATISTIK AKUN</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="dh-pp-stats">'
        f'<div><span>Total Referral <i>👥</i></span><b>{nref}</b><em>Teman bergabung</em></div>'
        f'<div><span>Total Earned <i>✨</i></span><b class="acc">{u.get("earned", 0)} SD</b><em>Stardust terakumulasi</em></div>'
        f'<div><span>Tier Saat Ini <i>⭐</i></span><b>⭐ {tier[0]}</b><em class="g">{tier[2]} Komisi Stardust</em></div></div>',
        unsafe_allow_html=True)
    with st.container(key="dhpp_quick"):
        q1, q2, q3 = st.columns([1.7, 1.2, 1.5], gap="small", vertical_alignment="center")
        with q1:
            st.markdown('<div class="dh-pp-qt"><b>Aksi Cepat Takdir</b><span>Ajak teman untuk bonus komisi atau '
                        'lanjutkan penafsiran spiritualmu</span></div>', unsafe_allow_html=True)
        with q2:
            st.button("📤 Share Referral", key="dhpp_share", on_click=_cb_to_referral, use_container_width=True)
        with q3:
            with st.container(key="dhpp_read"):
                if st.button("Mulai Pembacaan", key="dhpp_readbtn", type="primary", use_container_width=True):
                    ss.dh_open_reveal = True
                    st.rerun()


def _render_edit(u):
    ss = st.session_state
    st.markdown('<div class="dh-pp-edith">✏️ Edit Profil</div><div class="dh-pp-edsub">Data ini dipakai otomatis (autofill) '
                'di Solo Reveal, Cek Kecocokan, dan pembacaan lainnya.</div>', unsafe_allow_html=True)
    with st.container(key="dhpp_editcard"):
        c1, c2 = st.columns(2, gap="medium")
        with c1:
            st.text_input("Nama Lengkap / Panggilan", key="dhpe_nama")
        with c2:
            st.date_input("Tanggal Lahir", value=None, min_value=date(1900, 1, 1), max_value=date.today(),
                          format="DD/MM/YYYY", key="dhpe_tgl")
        c3, c4 = st.columns(2, gap="medium")
        with c3:
            st.time_input("Jam Lahir (Opsional)", value=None, key="dhpe_jam")
        with c4:
            st.text_input("Tempat Lahir (Opsional)", placeholder="Contoh: Jakarta", key="dhpe_kota")
        c5, c6 = st.columns(2, gap="medium")
        with c5:
            st.selectbox("Jenis Kelamin / Gender", GENDERS, index=None, placeholder="Pilih", key="dhpe_gender")
        with c6:
            st.selectbox("Golongan Darah (Opsional)", GOLDA, index=None, placeholder="Pilih", key="dhpe_golda")
    if ss.get("dh_pf_err"):
        st.error(ss.dh_pf_err)
    b1, b2 = st.columns([1, 2.2], gap="small")
    with b1:
        with st.container(key="dhpp_cancel"):
            st.button("Batal", key="dhpp_edit_no", on_click=_cb_edit_cancel, use_container_width=True)
    with b2:
        with st.container(key="dhpp_save"):
            st.button("Simpan Perubahan", key="dhpp_edit_ok", type="primary", on_click=_cb_edit_save,
                      use_container_width=True)


def _render_referral(u):
    ref = u["ref"]
    link = f"https://destiny-reveal.streamlit.app/?ref={ref}"
    nref = u.get("ref_count", 0)
    ti = _tier(nref)
    nxt = TIERS[ti + 1] if ti + 1 < len(TIERS) else None
    pct = 100 if not nxt else int((nref - TIERS[ti][1]) * 100 / (nxt[1] - TIERS[ti][1]))
    with st.container(key="dhpp_refcard"):
        st.markdown('<div class="dh-pp-rh"><b>🎁 Unique Referral ID</b><span>Dibuat setelah emailmu terverifikasi</span></div>',
                    unsafe_allow_html=True)
        c1, c2, c3 = st.columns([1.5, 1, 1.5], gap="small", vertical_alignment="center")
        with c1:
            st.markdown(f'<div class="dh-pp-codel">KODE REFERRAL PRIBADI</div><div class="dh-pp-code">{_e(ref)}</div>',
                        unsafe_allow_html=True)
        with c2:
            copy_button(ref, "📋 Salin Kode", "dhpp_cp1", fs=12, h=44)
        with c3:
            copy_button(link, "🔗 Salin Link Undangan", "dhpp_cp2", fs=12, h=44)
    tgt = f"{nxt[1] - nref} teman lagi menuju <b>{nxt[0]}</b> ({nxt[3]})" if nxt else "Tier tertinggi tercapai 🎉"
    st.markdown(
        '<div class="dh-pp-prog"><div class="dh-pp-ph"><span>Progress Milestone: <b>'
        f'{nref} Teman</b> · {tgt}</span><b>{pct}%</b></div>'
        f'<div class="dh-pp-bar"><i style="width:{max(pct, 4)}%"></i></div></div>', unsafe_allow_html=True)
    st.markdown('<div class="dh-pp-sec">TIER JOURNEY KOSMIK</div>', unsafe_allow_html=True)
    st.markdown('<div class="dh-pp-tiers">' + "".join(
        f'<div class="{"on" if i == ti else ("done" if i < ti else "")}">'
        f'<em>{"✓ Aktif" if i == ti else ("Selesai" if i < ti else "Terkunci")}</em><b>{_e(t[0])}</b>'
        f'<span>{t[1]}+ Teman</span><small>{_e(t[3])} · {t[2]}</small></div>' for i, t in enumerate(TIERS)) + '</div>',
        unsafe_allow_html=True)
    st.markdown('<div class="dh-pp-note">Komisi User Biasa: 10 sampai 15% · Affiliate: 20 sampai 30% · Recurring: 10 sampai 15% '
                '(angka demo, belum terhubung backend).</div>', unsafe_allow_html=True)


def _render_history():
    ss = st.session_state
    hist = ss.get("dh_history", [])
    with st.container(key="dhpp_filter"):
        f1, f2 = st.columns([3, 1.1], gap="small", vertical_alignment="center")
        with f1:
            st.text_input("Cari", placeholder="Cari berdasarkan zodiak, weton, tarot, atau MBTI...", key="dhpp_q",
                          label_visibility="collapsed")
        with f2:
            order = st.selectbox("Urutan", ["Terbaru", "Terlama"], key="dhpp_sort", label_visibility="collapsed")
        flt = st.pills("Filter", FILTERS, default="Semua", key="dhpp_f", label_visibility="collapsed") or "Semua"
    q = (ss.get("dhpp_q") or "").strip().lower()
    rows = []
    for i, h in enumerate(hist):
        text = " ".join([h["nama"], *h["tags"]]).lower()
        if (flt == "Arsip") != bool(h.get("arsip")):
            continue
        if flt not in ("Semua", "Arsip") and flt.lower() not in text:
            continue
        if q and q not in text:
            continue
        rows.append((i, h))
    if order == "Terlama":
        rows.reverse()
    if not rows:
        st.markdown('<div class="dh-pp-empty">Belum ada riwayat yang cocok. Mulai pembacaan pertamamu lewat '
                    '“Mulai Pembacaan” di tab Overview.</div>', unsafe_allow_html=True)
    for i, h in rows:
        with st.container(key=f"dhpp_h{i}"):
            a, b = st.columns([4, 1.5], gap="small", vertical_alignment="center")
            with a:
                badge = '<i class="arc">📦 Diarsipkan</i>' if h.get("arsip") else '<i class="ok">✓ Selesai</i>'
                st.markdown(f'<div class="dh-pp-hm">✦ MODE 1: INTI <small>· {_e(h["waktu"])}</small>{badge}</div>'
                            f'<div class="dh-pp-hn">{_e(h["nama"])}</div>', unsafe_allow_html=True)
            with b:
                with st.container(key=f"dhpp_ho{i}"):
                    if st.button("Buka Detail →", key=f"dhpp_open{i}"):
                        auth._open_history(i)
            st.markdown('<div class="dh-pp-hl"></div>', unsafe_allow_html=True)
            t, o1, o2 = st.columns([6, 0.8, 0.8], gap="small", vertical_alignment="center")
            with t:
                st.markdown('<div class="dh-pp-tags">' + "".join(f"<span>{_e(x)}</span>" for x in h["tags"]) + '</div>',
                            unsafe_allow_html=True)
            with o1:
                with st.container(key=f"dhpp_ar{i}"):
                    st.button("📦" if not h.get("arsip") else "↩️", key=f"dhpp_arbtn{i}", on_click=_cb_archive, args=(i,),
                              help="Arsipkan / kembalikan")
            with o2:
                with st.container(key=f"dhpp_de{i}"):
                    st.button("🗑️", key=f"dhpp_debtn{i}", on_click=_cb_delete, args=(i,), help="Hapus riwayat")


@st.dialog("Profil", width="large")
def profile_dialog():
    ss = st.session_state
    u = auth.current_user()
    if not u:
        st.rerun()
    if ss.get("dh_pf_toast"):
        st.toast(ss.pop("dh_pf_toast"))
    _header(u)
    tab = ss.setdefault("dh_pf_tab", "overview")
    if ss.get("dh_pf_edit"):
        _render_edit(u)
        return
    _tabs(tab)
    if tab == "referral":
        _render_referral(u)
    elif tab == "riwayat":
        _render_history()
    else:
        _render_overview(u)
