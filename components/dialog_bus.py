"""
Penghubung antar dialog (Streamlit cuma izinkan 1 dialog sekali waktu).
request_open(nama) -> set flag + rerun penuh (dialog lama nutup); navbar.render_navbar
manggil pop_pending() di akhir run, lalu membuka dialog yang diminta.
"""

import streamlit as st


def request_open(name, **state):
    """Minta buka dialog `name` di run berikutnya. **state = session_state yang di-set dulu."""
    for k, v in state.items():
        st.session_state[k] = v
    st.session_state.dh_open_dialog = name
    st.rerun()


def pop_pending():
    return st.session_state.pop("dh_open_dialog", None)
