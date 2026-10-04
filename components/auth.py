"""
Auth flow (UI13): modal Masuk (email) -> Verifikasi OTP -> Profil User.
Satu st.dialog, transisi antar langkah lewat on_click callback (dialog tetap kebuka).
State: dh_user {email, nama, joined, koin, ref}, dh_auth_step ("email"|"otp"), dh_auth_code, dh_history.
DUMMY: kode OTP dibuat lokal & ditampilkan di layar (belum ada pengiriman email), koin/top up/komisi belum ada backend.
"""

import hashlib
import random
import re
from datetime import datetime, timedelta, timezone

import streamlit as st

from components.dialog_bus import request_open
from components.flow_state import STEP_RESULT, set_step, valid_email
from components.modal_detail import copy_button

_WIB = timezone(timedelta(hours=7))
_BLN = ["", "Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September",
        "Oktober", "November", "Desember"]
BONUS_KOIN = 250  # SD (setara 5 koin lama)
_SOON = "Fitur ini belum tersedia — masih tahap pengembangan 🚧"


# ─────────────── state helper ───────────────
def current_user():
    return st.session_state.get("dh_user")


def _nama_dari_email(email):
    return (re.sub(r"[^a-zA-Z]", "", email.split("@")[0]) or "User").lower()


def _ref_code(email):
    h = int(hashlib.md5(email.lower().encode()).hexdigest(), 16) % 10000
    return f"DR-{_nama_dari_email(email)[:5].upper()}{h:04d}"


def ensure_user(email):
    """Buat akun baru (250 SD bonus + ID referral) atau pakai yang ada. Dipanggil juga dari alur Reveal."""
    ss = st.session_state
    email = email.strip()
    if not ss.get("dh_user") or ss.dh_user["email"] != email:
        now = datetime.now(_WIB)
        ss.dh_user = {"email": email, "nama": _nama_dari_email(email), "koin": BONUS_KOIN,
                      "joined": f"{_BLN[now.month]} {now.year}", "ref": _ref_code(email)}
    ss.dh_email = email
    ss.dh_email_verified = True
    return ss.dh_user


def add_history(nama, tgl, results):
    """Dicatat tiap hasil Mode 1 selesai dihitung (dipanggil dari modal_steps.render_loading)."""
    now = datetime.now(_WIB)
    ss = st.session_state
    hist = ss.setdefault("dh_history", [])
    tags = [r["short"] for r in results[:3]]
    waktu = f"{now.day} {_BLN[now.month]} {now.year} pukul {now:%H.%M}"
    hist.insert(0, {"nama": nama, "tgl": tgl, "waktu": waktu, "tags": tags,
                    "data": dict(ss.get("dh_modal_data") or {}), "results": results})
    del hist[20:]


def _new_code():
    st.session_state.dh_auth_code = f"{random.randint(0, 999999):06d}"


# ─────────────── callbacks ───────────────
def _cb_send():
    ss = st.session_state
    email = (ss.get("dha_email") or "").strip()
    if not valid_email(email):
        ss.dh_auth_error = "Format email belum valid, contoh: nama@email.com"
        return
    ss.dh_auth_error = None
    ss.dh_auth_email = email
    _new_code()
    ss.dha_otp = ss.dh_auth_code
    ss.dh_auth_step = "otp"


def _cb_change_email():
    st.session_state.dha_email = st.session_state.get("dh_auth_email", "")
    st.session_state.dh_auth_error = None
    st.session_state.dh_auth_step = "email"


def _cb_resend():
    _new_code()
    st.session_state.dha_otp = st.session_state.dh_auth_code
    st.session_state.dh_auth_error = None


def _login():
    ss = st.session_state
    ensure_user(ss.dh_auth_email)
    ss.dh_auth_step = "email"
    ss.dh_auth_error = None
    ss.dh_auth_done = True  # dialog dibuka ulang sebagai profil di run berikutnya


def _cb_verify():
    ss = st.session_state
    if (ss.get("dha_otp") or "").strip() != ss.get("dh_auth_code"):
        ss.dh_auth_error = "Kode verifikasi tidak cocok. Cek lagi atau kirim ulang kode."
        return
    _login()


def _cb_quick():
    _login()


def _soon(msg=_SOON):
    st.toast(msg)


# ─────────────── Langkah 2: input email ───────────────
def _render_email():
    ss = st.session_state
    st.markdown(
        '<div class="dh-step dh-step-auth"></div>'
        '<div class="dh-au-ico">🔑</div><div class="dh-au-title">Masuk ke Akun</div>'
        '<div class="dh-au-sub">Masuk via email untuk membuka akun &amp; melihat isi profil</div>',
        unsafe_allow_html=True)
    st.markdown('<div class="dh-au-label">Alamat Email Kamu</div>', unsafe_allow_html=True)
    st.text_input("Alamat Email", placeholder="nama@email.com", key="dha_email", icon=":material/mail:",
                  label_visibility="collapsed")
    if ss.get("dh_auth_error"):
        st.error(ss.dh_auth_error)
    st.markdown(
        '<div class="dh-au-notice"><b>🛡️ Autentikasi Verifikasi Email Langsung</b>'
        'Kami akan mengirimkan kode verifikasi 6-digit &amp; tautan instan ke emailmu. Setelah masuk, '
        'profil dan saldo Stardust-mu otomatis terbuka.</div>', unsafe_allow_html=True)
    st.button("Lanjutkan Verifikasi Email →", key="dha_send", type="primary", use_container_width=True,
              on_click=_cb_send)
    st.markdown('<div class="dh-au-foot">Belum punya akun? Cukup masukkan emailmu di atas, akun barumu akan '
                f'otomatis dibuat dengan <b>{BONUS_KOIN} SD Bonus &amp; ID Referral</b>.</div>',
                unsafe_allow_html=True)


# ─────────────── Langkah 3: OTP ───────────────
def _render_otp():
    ss = st.session_state
    code = ss.get("dh_auth_code", "")
    st.markdown(
        '<div class="dh-step dh-step-auth"></div>'
        '<div class="dh-au-ico dh-au-green">✉️</div><div class="dh-au-eyebrow">VERIFIKASI TERKIRIM</div>'
        '<div class="dh-au-title">Cek Kotak Masuk Email</div>', unsafe_allow_html=True)
    _a, m1, m2, _b = st.columns([0.5, 2.3, 0.8, 0.5], gap="small", vertical_alignment="center")
    with m1:
        st.markdown(f'<div class="dh-au-mail">{ss.get("dh_auth_email", "")}</div>', unsafe_allow_html=True)
    with m2:
        with st.container(key="dha_change"):
            st.button("✏️ Ubah", key="dha_change_btn", on_click=_cb_change_email)
    st.markdown(
        '<div class="dh-au-sim"><div class="dh-au-simhead"><b>📩 VERIFIKASI EMAIL MASUK:</b><span>Baru saja</span></div>'
        '<div class="dh-au-simtxt">&ldquo;Gunakan kode verifikasi berikut untuk masuk ke akun Destiny Reveal milikmu:&rdquo;</div>'
        f'<div class="dh-au-code">{code}</div></div>'
        '<div class="dh-au-label">Masukkan Kode Verifikasi 6-Digit:</div>', unsafe_allow_html=True)
    st.text_input("Kode OTP", key="dha_otp", max_chars=6, label_visibility="collapsed")
    if ss.get("dh_auth_error"):
        st.error(ss.dh_auth_error)
    st.button("✓ Verifikasi Email & Masuk ke Profil", key="dha_verify", type="primary",
              use_container_width=True, on_click=_cb_verify)
    st.button(f"⚡ Klik Cepat untuk Masuk Otomatis ({code})", key="dha_quick", use_container_width=True,
              on_click=_cb_quick)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="dh-au-small">Tidak menerima kode?</div>', unsafe_allow_html=True)
    with c2:
        with st.container(key="dha_resend"):
            st.button("🔄 Kirim Ulang Kode", key="dha_resend_btn", on_click=_cb_resend)


# ─────────────── Langkah 4: profil ───────────────
def _cb_logout():
    ss = st.session_state
    for k in ("dh_user", "dh_email", "dh_email_verified", "dh_history", "dh_auth_step", "dh_auth_done"):
        ss.pop(k, None)
    st.rerun()


def _open_history(i):
    ss = st.session_state
    h = ss.dh_history[i]
    ss.dh_modal_data = h["data"]
    ss.dh_flow_result = h["results"]
    ss.dh_show_summary = False
    set_step(STEP_RESULT)
    ss.dh_reopen = True
    st.rerun()  # rerun penuh: profil nutup, Modal Hasil kebuka (navbar.reopen_if_pending)


@st.dialog("Profil", width="small")
def profile_dialog():
    ss = st.session_state
    u = current_user()
    if not u:
        st.rerun()
    init = (u["nama"][:2] or "U").upper()
    st.markdown('<div class="dh-step dh-step-profile"></div>', unsafe_allow_html=True)
    ua, ub = st.columns([1.35, 1], gap="small", vertical_alignment="center")
    with ua:
        st.markdown(
            f'<div class="dh-pf-user"><div class="dh-pf-av">{init}</div><div><div class="dh-pf-name">{u["nama"]}'
            f'<span>Terverifikasi</span></div><div class="dh-pf-mail">{u["email"]} · Anggota sejak {u["joined"]}</div></div></div>',
            unsafe_allow_html=True)
    with ub:
        with st.container(key="dhpf_coin"):
            c1, c2 = st.columns([0.85, 1.25], gap="small", vertical_alignment="bottom")
            with c1:
                st.markdown(f'<div class="dh-pf-coinl">SALDO STARDUST</div><div class="dh-pf-coinv">✨ <b>{u["koin"]}</b> '
                            '<span>SD</span></div>', unsafe_allow_html=True)
            with c2:
                if st.button("➕ Top Up", key="dhpf_topup", type="primary"):
                    request_open("pricing_keep", dh_pr_tab="koin")
    st.markdown('<div class="dh-pf-line"></div>', unsafe_allow_html=True)

    ref = u["ref"]
    link = f"https://destiny-reveal.streamlit.app/?ref={ref}"
    with st.container(key="dhpf_ref"):
        st.markdown(
            '<div class="dh-pf-refhead"><b>🎁 ID Referral Khusus Kamu</b><span>User Biasa</span></div>'
            '<div class="dh-pf-refsub">Dibuat khusus setelah emailmu terverifikasi. Bagikan ke teman untuk dapat komisi &amp; VIP gratis.</div>',
            unsafe_allow_html=True)
        with st.container(key="dhpf_codebox"):
            c1, c2, c3 = st.columns([1.45, 0.95, 1.6], gap="small", vertical_alignment="center")
            with c1:
                st.markdown(f'<div class="dh-pf-codel">KODE REFERRAL PRIBADI:</div><div class="dh-pf-code">{ref}</div>',
                            unsafe_allow_html=True)
            with c2:
                copy_button(ref, "📋 Salin Kode", "dhpf_cp1", fs=11)
            with c3:
                copy_button(link, "🔗 Salin Link Undangan", "dhpf_cp2", fs=11)
        st.markdown(
            '<div class="dh-pf-prog"><div class="dh-pf-proghead"><span>Progress Milestone: <b>0 / 10 Teman</b> menuju '
            '<b>VIP 1 Bulan Gratis</b></span><b>0%</b></div><div class="dh-pf-bar"><i></i></div>'
            '<div class="dh-pf-ms"><div><b>10 Referral</b><span>VIP 1 Bulan</span></div>'
            '<div><b>50 Referral</b><span>VIP 1 Tahun</span></div>'
            '<div><b>100 Referral</b><span>Lifetime VIP 👑</span></div></div>'
            '<div class="dh-pf-comm"><span>Komisi User Biasa: 10–15% · Affiliate: 20–30% · Recurring: 10–15%</span>'
            '<a>Detail Komisi Lengkap →</a></div></div>', unsafe_allow_html=True)

    hist = ss.get("dh_history", [])
    h1, h2 = st.columns([3, 1], vertical_alignment="center")
    with h1:
        st.markdown(f'<div class="dh-pf-sec">⏱️ RIWAYAT PEMBACAAN TAKDIR ({len(hist)})</div>', unsafe_allow_html=True)
    with h2:
        with st.container(key="dhpf_newscan"):
            if st.button("+ Scan Baru", key="dhpf_newscan_btn"):
                st.session_state.dh_open_reveal = True
                st.rerun()
    if not hist:
        st.markdown('<div class="dh-pf-empty">Belum ada pembacaan. Mulai Reveal pertamamu lewat “+ Scan Baru”.</div>',
                    unsafe_allow_html=True)
    for i, h in enumerate(hist[:5]):
        with st.container(key=f"dhpf_h{i}"):
            a, b = st.columns([3.2, 1], vertical_alignment="center")
            with a:
                st.markdown(f'<div class="dh-pf-hn"><b>{h["nama"]}</b><em>Mode 1 (5 Kelahiran)</em></div>'
                            f'<div class="dh-pf-hw">🗓️ {h["waktu"]}</div>'
                            f'<div class="dh-pf-ht">{" · ".join(h["tags"])}</div>', unsafe_allow_html=True)
            with b:
                if st.button("Buka Hasil →", key=f"dhpf_open{i}"):
                    _open_history(i)
    st.markdown('<div class="dh-pf-line"></div>', unsafe_allow_html=True)
    f1, f2, f3, f4 = st.columns([1.8, 1.25, 1.35, 0.8], gap="small", vertical_alignment="center")
    with f1:
        st.markdown('<div class="dh-pf-priv">Data takdirmu terlindungi aman secara enkripsi privat.</div>',
                    unsafe_allow_html=True)
    with f2:
        with st.container(key="dhpf_price"):
            if st.button("List Harga & VIP", key="dhpf_pricebtn"):
                request_open("pricing_keep", dh_pr_tab="semua")
    with f3:
        with st.container(key="dhpf_logout"):
            if st.button("🚪 Keluar Akun", key="dhpf_logoutbtn"):
                _cb_logout()
    with f4:
        with st.container(key="dhpf_close"):
            if st.button("Tutup", key="dhpf_closebtn"):
                st.rerun()


# ─────────────── dialog masuk (email -> OTP) ───────────────
@st.dialog("Masuk", width="small")
def auth_dialog():
    if st.session_state.pop("dh_auth_done", False) or current_user():
        st.session_state.dh_auth_done = True
        st.rerun()
    if st.session_state.get("dh_auth_step") == "otp":
        _render_otp()
    else:
        _render_email()


def open_auth():
    """Dari tombol navbar: sudah login -> profil, belum -> modal masuk."""
    if current_user():
        profile_dialog()
    else:
        st.session_state.dh_auth_step = "email"
        st.session_state.dh_auth_error = None
        auth_dialog()


def reopen_if_pending():
    """Dipanggil di akhir navbar: habis login berhasil, buka profil."""
    if st.session_state.pop("dh_auth_done", False) and current_user():
        profile_dialog()
    elif st.session_state.pop("dh_open_profile", False) and current_user():
        profile_dialog()
