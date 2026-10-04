"""
Modal "Daftar Harga & Benefit VIP" (UI14). 5 tab: Semua | Koin | Fitur Koin | VIP | Referral.
Tab = tombol segmented + session_state (dh_pr_tab), pindah tab lewat on_click (dialog tetap kebuka).
Tampilan light (ngikutin mockup), bukan dark theme.
DUMMY: pembelian koin / langganan VIP / tombol "Buka" fitur belum terhubung payment (toast / buka modal fitur).
"""

import html

import streamlit as st

from components import auth
from components.dialog_bus import request_open
from components.feature_modals import _top
from components.modal_detail import copy_button

_PAY_TOAST = "Pembayaran belum tersedia — masih tahap pengembangan 🚧"
TABS = [("semua", "Semua"), ("koin", "🪙 Koin"), ("fitur", "🔓 Fitur Koin"), ("vip", "⭐ VIP"), ("ref", "🎁 Referral")]

# (jumlah koin, harga, per koin, badge, deskripsi)
COIN_PACKS = [
    (1, "Rp 10.000", "Rp 10.000/koin", "Starter", "Cocok untuk 1× Mode Instan atau Tarot 3 Kartu"),
    (5, "Rp 45.000", "Rp 9.000/koin", "Hemat 10%", "Populer: Cukup untuk Monthly Report / 5× Report"),
    (15, "Rp 120.000", "Rp 8.000/koin", "Hemat 20%", "Best Value: Pas untuk eksplorasi rutin sebulan"),
    (50, "Rp 350.000", "Rp 7.000/koin", "Sultan (Hemat 30%)", "Akses bebas untuk seluruh fitur dan laporan berkala"),
]
# (nama, koin, keterangan, dialog tujuan, state)
FEATURES = [
    ("Mode Instan Report", 1, "5 Sistem Kelahiran (Zodiak, Shio, Weton, Numerologi, Matrix)", "reveal", {"dh_modal_mode": "instan"}),
    ("Mode Mendalam Report", 2, "5 Dimensi Psikologi (MBTI, Big Five, Enneagram, DISC, Love Lang)", "reveal", {"dh_modal_mode": "mendalam"}),
    ("Tarot 3 Kartu", 1, "Masa Lalu, Masa Kini, Masa Depan + interpretasi detail", "tarot_spread", {"dh_ts_tab": 3}),
    ("Tarot 5 Kartu", 2, "Situasi, Rintangan, Bawah Sadar, Saran, Hasil", "tarot_spread", {"dh_ts_tab": 5}),
    ("Tarot Celtic Cross", 3, "10 Posisi Legendaris Celtic Cross komprehensif", "tarot_spread", {"dh_ts_tab": 10}),
    ("Compatibility Report", 3, "Komparasi kecocokan 2 orang langsung (Weton & Zodiak)", "compat", {}),
    ("Weekly Report", 3, "Panduan timing & prediksi pekanan berdasarkan chart pribadimu", "weekly", {}),
    ("Monthly Report", 5, "Prediksi bulanan komprehensif + saran strategis", "weekly", {}),
]
VIP_BENEFITS = ["Semua 15 sistem kebuka tanpa batas", "10 Deep Report / bulan",
                "Download booklet PDF personal", "Bebas iklan (No Ads) & antrean cepat"]
# (label, nama, harga, satuan, deskripsi, tombol, gaya)
VIP_PLANS = [
    ("BULANAN", "VIP Bulanan", "Rp 99.000", "/ bln", "Cocok untuk eksplorasi intensif selama 30 hari penuh.", "Pilih Bulanan", "out"),
    ("TAHUNAN", "VIP Tahunan", "Rp 499.000", "/ thn", "Pilihan paling hemat: hanya ~Rp 41rb/bulan untuk setahun penuh.", "Pilih Tahunan", "hl"),
    ("SEKALI BAYAR", "Lifetime VIP", "Rp 1.500.000", "", "Akses seumur hidup tanpa biaya langganan bulanan selamanya.", "Pilih Lifetime", "dark"),
]
COMMISSION = [("USER BIASA", "10 - 15%", "Komisi tiap teman top up koin atau buka report."),
              ("AFFILIATE PARTNER", "20 - 30%", "Untuk kreator konten, astrolog, dan komunitas."),
              ("SUBSCRIPTION", "10 - 15% recurring", "Pasif berkala selama member VIP temanmu aktif.")]
MILESTONES = [("🥉", "10 Referral:", "VIP 1 Bulan Gratis"), ("🥈", "50 Referral:", "VIP 1 Tahun Gratis"),
              ("🥇", "100 Referral:", "Lifetime VIP Gratis 👑")]


def _buy(_what=""):
    st.toast(_PAY_TOAST)


def _cb_tab(t):
    st.session_state.dh_pr_tab = t


# ─────────────── bagian-bagian ───────────────
def _sec_head(icon, title, right):
    st.markdown(f'<div class="dh-pr-sec"><b>{icon} {title}</b><span>{right}</span></div>', unsafe_allow_html=True)


def _sec_coin():
    _sec_head("🪙", "Paket Koin", "Koin tidak pernah kedaluwarsa")
    for row in range(2):
        cols = st.columns(2, gap="small")
        for col, (n, harga, per, badge, desc) in zip(cols, COIN_PACKS[row * 2:(row + 1) * 2]):
            with col:
                with st.container(key=f"dhpr_coin_{n}"):
                    st.markdown(
                        f'<div class="dh-pr-chead"><b>💎 {n} Koin</b><em>{badge}</em></div>'
                        f'<div class="dh-pr-price">{harga} <small>({per})</small></div>'
                        f'<div class="dh-pr-cdesc">{desc}</div>', unsafe_allow_html=True)
                    st.button(f"Beli {n} Koin Sekarang", key=f"dhpr_buy_{n}", on_click=_buy, use_container_width=True)


def _sec_fitur():
    _sec_head("🔓", "Harga Fitur (Pakai Koin)", "Bayar sesuai kebutuhan")
    with st.container(key="dhpr_table"):
        st.markdown('<div class="dh-pr-th"><span>FITUR</span><span>HARGA</span><span>KETERANGAN</span><span>AKSI</span></div>',
                    unsafe_allow_html=True)
        for i, (nama, koin, ket, dlg, state) in enumerate(FEATURES):
            with st.container(key=f"dhpr_row_{i}"):
                c1, c2, c3, c4 = st.columns([1.7, 0.75, 2.6, 0.85], gap="small", vertical_alignment="center")
                with c1:
                    st.markdown(f'<div class="dh-pr-fn">{nama}</div>', unsafe_allow_html=True)
                with c2:
                    st.markdown(f'<span class="dh-pr-pill">{koin} Koin</span>', unsafe_allow_html=True)
                with c3:
                    st.markdown(f'<div class="dh-pr-fk">{html.escape(ket)}</div>', unsafe_allow_html=True)
                with c4:
                    if st.button("Buka →", key=f"dhpr_open_{i}"):
                        request_open(dlg, **state)


def _sec_vip():
    _sec_head("⭐", "VIP (Langganan)", '<i class="dh-pr-allacc">All Access</i>')
    items = "".join(f'<div>✓ {b}</div>' for b in VIP_BENEFITS)
    st.markdown(f'<div class="dh-pr-vipbox"><b>✦ BENEFIT VIP MEMBERSHIP ✦</b><div class="dh-pr-vipgrid">{items}</div></div>',
                unsafe_allow_html=True)
    cols = st.columns(3, gap="small")
    for i, (col, (lab, nama, harga, unit, desc, btn, style)) in enumerate(zip(cols, VIP_PLANS)):
        with col:
            with st.container(key=f"dhpr_plan_{style}"):
                ribbon = '<span class="dh-pr-ribbon">HEMAT 58%</span>' if style == "hl" else ""
                st.markdown(f'{ribbon}<div class="dh-pr-plab">{lab}</div><div class="dh-pr-pname">{nama}</div>'
                            f'<div class="dh-pr-price">{harga} <small>{unit}</small></div><div class="dh-pr-cdesc">{desc}</div>',
                            unsafe_allow_html=True)
                st.button(btn, key=f"dhpr_plan_btn_{i}", type="primary" if style == "hl" else "secondary",
                          on_click=_buy, use_container_width=True)


def _sec_ref():
    _sec_head("🎁", "Program Referral & Affiliate", '<i class="dh-pr-comm">Komisi Menarik</i>')
    cards = "".join(f'<div><span>{a}</span><b>{b}</b><p>{c}</p></div>' for a, b, c in COMMISSION)
    ms = "".join(f'<div><i>{ic}</i><span><b>{a}</b><em>{b}</em></span></div>' for ic, a, b in MILESTONES)
    st.markdown(
        f'<div class="dh-pr-refwrap"><div class="dh-pr-refcards">{cards}</div>'
        f'<div class="dh-pr-ms"><div class="dh-pr-mshead">🏆 BONUS MILESTONE REFERRAL:</div><div class="dh-pr-msgrid">{ms}</div></div></div>',
        unsafe_allow_html=True)
    u = auth.current_user()
    with st.container(key="dhpr_refcode"):
        c1, c2 = st.columns([1.5, 1.2], gap="small", vertical_alignment="center")
        if u:
            with c1:
                st.markdown(f'<div class="dh-pr-rcl">ID REFERRAL KHUSUS KAMU:</div><div class="dh-pr-rc">{u["ref"]}</div>',
                            unsafe_allow_html=True)
            with c2:
                copy_button(u["ref"], "📋 Salin Kode Referral", "dhpr_cp", fs=12)
        else:
            with c1:
                st.markdown('<div class="dh-pr-rcl">ID REFERRAL KHUSUS KAMU:</div>'
                            '<div class="dh-pr-rc dh-pr-rcoff">Masuk dulu untuk dapat kode</div>', unsafe_allow_html=True)
            with c2:
                if st.button("Masuk / Login", key="dhpr_login", type="primary", use_container_width=True):
                    request_open("auth")


# ─────────────── dialog ───────────────
@st.dialog("Daftar Harga & Benefit VIP", width="large")
def pricing_dialog():
    ss = st.session_state
    _top(login_link=False, key="pr")
    st.markdown('<div class="dh-step dh-step-price"></div><div class="dh-pr-eyebrow">✦ TRANSPARANSI BIAYA DESTINY REVEAL ✦</div>'
                '<div class="dh-pr-title">Daftar Harga &amp; Benefit VIP</div>'
                '<div class="dh-pr-sub">Mulai dari eksplorasi gratis, fleksibilitas paket koin tanpa kedaluwarsa, '
                'hingga membership VIP tak terbatas.</div><div class="dh-fm-div"></div>', unsafe_allow_html=True)
    tab = ss.setdefault("dh_pr_tab", "semua")
    with st.container(key="dhpr_tabs"):
        cols = st.columns(len(TABS), gap="small")
        for col, (k, lab) in zip(cols, TABS):
            with col:
                st.button(lab, key=f"dhpr_tab_{k}", on_click=_cb_tab, args=(k,),
                          type="primary" if tab == k else "secondary", use_container_width=True)
    if tab in ("semua", "koin"):
        _sec_coin()
    if tab in ("semua", "fitur"):
        _sec_fitur()
    if tab in ("semua", "vip"):
        _sec_vip()
    if tab in ("semua", "ref"):
        _sec_ref()
    with st.container(key="dhfm_outline_pr"):
        if st.button("Tutup & Kembali", key="dhpr_close", use_container_width=True):
            st.rerun()


def open_pricing(tab="semua"):
    """Dipanggil dari tombol biasa di halaman (bukan dari dalam dialog)."""
    st.session_state.dh_pr_tab = tab
    pricing_dialog()


def _open_all():
    open_pricing("semua")


DIALOGS = {
    "pricing": _open_all,
    "pricing_koin": lambda: open_pricing("koin"),
    "pricing_fitur": lambda: open_pricing("fitur"),
    "pricing_vip": lambda: open_pricing("vip"),
    "pricing_ref": lambda: open_pricing("ref"),
}
