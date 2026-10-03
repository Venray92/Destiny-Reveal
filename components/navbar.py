"""
Navbar floating (dipakai SEMUA halaman) + mega menu "Jelajahi" + jembatan klik
buat elemen HTML statis yang harus buka modal Reveal.
"""

import streamlit as st
import streamlit.components.v1 as components

from components.common import go
from components.modal import open_reveal_modal, reopen_if_pending


# ══════════════════════════════════════════════════════════════
# MEGA MENU "Jelajahi" (isi panel dropdown navbar)
# ══════════════════════════════════════════════════════════════
def _mega_item(title, sub, hl=False):
    # href dummy (fragmen yg gak ada target-nya, biar klik gak lompat ke atas).
    # Ganti href kalau halaman/fiturnya udah jadi.
    return (
        f'<a href="#dh-soon" class="dh-mega-item{" hl" if hl else ""}">'
        f'<span class="dh-mega-title">{title}</span>'
        f'<span class="dh-mega-sub">{sub}</span></a>'
    )


def _mega_menu_html():
    gratis = "".join([
        _mega_item("Ramalan Harian", "Pilih Zodiak atau Shio (1× per hari)"),
        _mega_item("Tarot 1 Kartu", "Tarik 1 kartu sinkronisitas hari ini"),
        _mega_item("Preview Zodiak", "Kelebihan &amp; kekurangan elemenmu"),
        _mega_item("Streak &amp; Reward", "Klaim 1 koin gratis tiap 5 hari"),
    ])
    koin = "".join([
        _mega_item("Tarot 3 Kartu (1 Koin)", "Masa Lalu, Kini, Masa Depan"),
        _mega_item("Tarot 5 Kartu (2 Koin)", "Situasi, Rintangan, Saran &amp; Hasil"),
        _mega_item("Celtic Cross (3 Koin)", "10 Posisi Tebaran Komprehensif"),
        _mega_item("Cek Kecocokan (3 Koin)", "Bandingkan 2 orang (Weton &amp; Zodiak)"),
        _mega_item("Weekly (3 Koin) / Monthly (5 Koin)", "Prediksi berkala &amp; timing eksekusi"),
        '<div class="dh-mega-foot"><a href="#dh-soon">🪙 Koin</a><i>·</i>'
        '<a href="#dh-soon">⭐ VIP</a><i>·</i><a href="#dh-soon">💰 List Harga</a></div>',
    ])
    lain = "".join([
        _mega_item("🎁 Program Referral", "Komisi 10-30% + Bonus VIP", hl=True),
        _mega_item("Tutorial", "Panduan pakai 15 sistem"),
        _mega_item("Blog", "Artikel self-discovery terkini"),
        _mega_item("FAQ &amp; Bantuan", "Pertanyaan yang sering ditanyakan"),
        _mega_item("Contact", "Bantuan tim Destiny Reveal"),
        _mega_item("Tentang Kami", "Kisah di balik Destiny Reveal"),
    ])
    def col(emoji, title, body):
        return (f'<div class="dh-mega-col"><div class="dh-mega-col-title">'
                f'<span class="dh-mega-emoji">{emoji}</span>{title}</div>{body}</div>')
    return (
        '<div class="dh-mega">'
        + col("🌄", "GRATIS", gratis)
        + col("💎", "PAKAI KOIN &amp; VIP", koin)
        + col("🎨", "LAINNYA", lain)
        + '</div>'
    )


# Jembatan klik: elemen HTML statis (kartu "Satu Data", link footer "Reveal") yg
# punya class .dh-open-reveal nge-klik tombol tersembunyi (key dh_modal_trigger)
# -> Python buka modal. Handler didaftarin di realm parent (w.eval) biar gak mati
# pas iframe komponen ini di-unmount, dan cuma kedaftar sekali.
_BRIDGE_JS = """<script>
(function(){var w=window.parent;if(w.__dhRevealBound)return;w.__dhRevealBound=true;
w.eval("document.addEventListener('click',function(e){var t=e.target.closest&&e.target.closest('.dh-open-reveal');if(!t)return;e.preventDefault();var b=document.querySelector('.st-key-dh_modal_trigger button');if(b)b.click();},true);");})();
</script>"""


def consume_pending_scroll():
    """Dipanggil dari Home: kalau user klik 'Tutorial' dari halaman lain, abis balik
    ke Home langsung smooth-scroll ke section tujuan."""
    tgt = st.session_state.pop("dh_pending_scroll", None)
    if tgt:
        components.html(
            "<script>setTimeout(function(){var e=window.parent.document.getElementById('"
            + tgt + "');if(e)e.scrollIntoView({behavior:'smooth'});},800);</script>",
            height=0,
        )


# ══════════════════════════════════════════════════════════════
# NAVBAR — dipakai di SEMUA halaman (dipanggil dari app.py)
# ══════════════════════════════════════════════════════════════
def render_navbar(current_page):
    with st.container(key="dhnav_wrap"):
        with st.container(key="dhnavbar"):
            logo_col, links_col, right_col = st.columns([1.5, 2.4, 2.4])
            with logo_col:
                st.markdown(
                    '<div class="dh-navbar-logo"><span class="dh-spark">✦</span> Destiny Reveal</div>',
                    unsafe_allow_html=True,
                )
            with links_col:
                with st.container(key="dhnav_links"):
                    l1, d1, l2, d2, l3, d3, l4 = st.columns([2, 0.4, 2, 0.4, 2, 0.4, 3.4])
                    with l1:
                        if current_page == "home":
                            # di Home: smooth scroll ke paling atas (anchor, bukan rerun/modal)
                            st.markdown('<a class="dh-nav-link" href="#dh-top">Home</a>', unsafe_allow_html=True)
                        elif st.button("Home", key="dhnav_home", use_container_width=True):
                            go("home")
                    with d1:
                        st.markdown('<div class="dh-nav-sep"></div>', unsafe_allow_html=True)
                    with l2:
                        if st.button("Reveal", key="dhnav_reveal", use_container_width=True):
                            open_reveal_modal()
                    with d2:
                        st.markdown('<div class="dh-nav-sep"></div>', unsafe_allow_html=True)
                    with l3:
                        if current_page == "home":
                            # smooth scroll ke section "Satu Data, Banyak Cara Pandang"
                            st.markdown('<a class="dh-nav-link" href="#dh-dataflow">Tutorial</a>', unsafe_allow_html=True)
                        elif st.button("Tutorial", key="dhnav_tutorial", use_container_width=True):
                            st.session_state.dh_pending_scroll = "dh-dataflow"
                            go("home")
                    with d3:
                        st.markdown('<div class="dh-nav-sep"></div>', unsafe_allow_html=True)
                    with l4:
                        with st.popover("🔮 Jelajahi", use_container_width=True):
                            st.markdown(_mega_menu_html(), unsafe_allow_html=True)
            with right_col:
                with st.container(key="dhnav_right"):
                    lb, cb = st.columns(2)
                    with lb:
                        if st.button("Login", key="dhnav_login"):
                            st.toast("Login/akun belum tersedia — masih tahap pengembangan 🚧")
                    with cb:
                        with st.container(key="dhnav_cta"):
                            if st.button(
                                "Mulai Reveal Takdirku →", key="dhnav_cta_btn", type="primary",
                                icon=":material/bolt:",
                            ):
                                open_reveal_modal()
        with st.container(key="dh_modal_trigger_wrap"):
            if st.button("buka modal", key="dh_modal_trigger"):
                open_reveal_modal()
            components.html(_BRIDGE_JS, height=0)
    reopen_if_pending()  # balik ke Modal Hasil setelah sub-modal detail ditutup (X/backdrop)
