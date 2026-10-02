"""Helper kecil yang dipakai bareng oleh komponen Home."""

import streamlit as st


def go(page):
    """Pindah halaman (session_state.dr_page) lalu rerun."""
    st.session_state.dr_page = page
    st.rerun()
