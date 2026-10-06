"""
Modal info: Tentang Kami (Contact/Privacy/Terms/FAQ pindah ke help_modals.py). Dibuka dari mega menu,
kartu Explore & footer (class .dh-open-modal + data-modal -> tombol tersembunyi di navbar.py).
"""

import streamlit as st

from components.feature_modals import _close_btn, _top

def _box(inner):
    st.markdown(f'<div class="dh-fm-box">{inner}</div>', unsafe_allow_html=True)


@st.dialog("Tentang Kami: Destiny Reveal", width="small")
def about_dialog():
    _top(key="ab")
    st.markdown('<div class="dh-fm-bigtitle">Tentang Kami: Destiny Reveal</div>', unsafe_allow_html=True)
    _box("<p>Destiny Reveal didirikan oleh <b>Zio</b> bersama para pengkaji astrologi, filologi Jawa, "
         "dan praktisi psikometri modern di Indonesia.</p>"
         "<p>Misi kami adalah menghadirkan jembatan antara kearifan masa lampau nusantara dengan pemahaman "
         "psikologi masa kini agar generasi muda bisa melangkah tanpa keraguan.</p>")
    _close_btn("Mengerti & Kembali", "ab")


DIALOGS = {"about": about_dialog}
