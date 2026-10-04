"""
Modal info (UI15): Tentang Kami, Contact, Privacy, Terms. Dibuka dari mega menu,
kartu Explore & footer (class .dh-open-modal + data-modal -> tombol tersembunyi di navbar.py).
"""

import streamlit as st

from components.feature_modals import _close_btn, _top

_PRIVACY = ("Kami menjunjung tinggi kerahasiaan data privasi pengguna. Semua data diproses secara privat "
            "melalui Anonymous ID atau Magic Link terverifikasi.")


def _box(inner):
    st.markdown(f'<div class="dh-fm-box">{inner}</div>', unsafe_allow_html=True)


@st.dialog("Tentang Kami — Destiny Reveal", width="small")
def about_dialog():
    _top(key="ab")
    st.markdown('<div class="dh-fm-bigtitle">Tentang Kami — Destiny Reveal</div>', unsafe_allow_html=True)
    _box("<p>Destiny Reveal didirikan oleh <b>Zio</b> bersama para pengkaji astrologi, filologi Jawa, "
         "dan praktisi psikometri modern di Indonesia.</p>"
         "<p>Misi kami adalah menghadirkan jembatan antara kearifan masa lampau nusantara dengan pemahaman "
         "psikologi masa kini agar generasi muda bisa melangkah tanpa keraguan.</p>")
    _close_btn("Mengerti & Kembali", "ab")


@st.dialog("Contact", width="small")
def contact_dialog():
    _top(key="ct")
    st.markdown('<div class="dh-fm-bigtitle">Contact</div>', unsafe_allow_html=True)
    _box("<p>Ada kendala, pertanyaan seputar pembacaan, atau tawaran kolaborasi?</p>"
         "<p>Hubungi tim kami melalui email: <b>halo@destinyreveal.id</b> atau Telegram: <b>@destinyreveal_id</b>.</p>")
    _close_btn("Mengerti & Kembali", "ct")


@st.dialog("Privacy", width="small")
def privacy_dialog():
    _top(key="pv")
    st.markdown('<div class="dh-fm-bigtitle">Privacy</div>', unsafe_allow_html=True)
    _box(f"<p>{_PRIVACY}</p>")
    _close_btn("Mengerti & Kembali", "pv")


@st.dialog("Terms", width="small")
def terms_dialog():
    _top(key="tm")
    st.markdown('<div class="dh-fm-bigtitle">Terms</div>', unsafe_allow_html=True)
    _box(f"<p>{_PRIVACY}</p>")  # teks sama persis dengan spec UI15
    _close_btn("Mengerti & Kembali", "tm")


DIALOGS = {"about": about_dialog, "contact": contact_dialog, "privacy": privacy_dialog, "terms": terms_dialog}
