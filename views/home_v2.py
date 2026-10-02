"""
Home v2 — entry point tipis. Kodenya dipecah ke paket components/:
  components/navbar.py      navbar + mega menu + jembatan klik
  components/sections.py    hero, matrix, jelajahi, satu-data, testimoni, CTA, footer
  components/modal.py       modal "Reveal Dirimu" (form) + dispatcher langkah
  components/modal_steps.py verifikasi email -> pembayaran -> loading -> hasil (Mode 1)
  components/flow_state.py  state & konstanta alur modal
  components/data.py        data statis (node diagram, kategori filter)
CSS: assets/css/home_v2.css (namespace "dh-"). app.py tetap manggil
render_navbar(...) dan render(...) dari modul ini.

Konten (koin, login, referral, VIP, pembayaran) masih DUMMY — belum ada backend.
"""

import streamlit as st

from components import sections
from components.navbar import consume_pending_scroll, render_navbar  # noqa: F401 (dipakai app.py)


def render(semua_sistem_list):
    """semua_sistem_list: list tuple (nama, icon, apa_ini, topik_list, ajakan, aktif)
    persis format SEMUA_SISTEM di app.py."""
    lookup = {nama: (apa_ini, topik_list, ajakan, aktif)
              for nama, icon, apa_ini, topik_list, ajakan, aktif in semua_sistem_list}

    # Root container: 1 key buat scope SEMUA css tombol (primary/secondary pill)
    # di Home, biar gak bocor ke halaman lain (reveal/tutorial/dll).
    with st.container(key="dh_home_root"):
        st.markdown('<div id="dh-top" class="dh-anchor"></div>', unsafe_allow_html=True)
        consume_pending_scroll()
        sections.render_hero()

        # NOTE: section wrapper WAJIB st.container(key=...) asli, bukan markdown
        # div open/close terpisah — itu gak bener-bener membungkus di DOM.
        with st.container(key="dh_section_matrix"):
            sections.render_matrix_diagram(lookup)

        sections.render_social_proof()

        with st.container(key="dh_section_explore"):
            sections.render_explore()

        with st.container(key="dh_section_dataflow"):
            sections.render_dataflow()

        with st.container(key="dh_section_testimonials"):
            sections.render_testimonials()

        with st.container(key="dh_section_finalcta"):
            sections.render_final_cta()

        sections.render_footer()
