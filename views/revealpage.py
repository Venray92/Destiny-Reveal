"""
Halaman hasil akhir — BELUM DIBUAT.

Stub sementara biar alur (Reveal Yourself -> Loading -> sini) nggak
dead-end pas semua titik selesai diproses. Nanti di sini hasil-hasil yang
udah dikumpulin di st.session_state.loading_results (dari loadingpage.py)
ditampilkan lengkap sekaligus, plus paywall buat buka versi lengkapnya.
"""

import streamlit as st


def render():
    st.markdown(
        '<div style="text-align:center;padding-top:60px;">'
        '<div style="font-family:\'Fraunces\',serif;font-size:30px;font-weight:700;color:#1c1a17;margin-bottom:10px;">'
        'Semua Titik Selesai Diproses ✧</div>'
        '<div style="font-size:14.5px;color:#6b6459;max-width:480px;margin:0 auto;">'
        'Halaman hasil akhir (ringkasan blur + paywall) belum dibuat — '
        'ini cuma stub biar alurnya nggak mentok. Next step berikutnya.</div>'
        '</div>',
        unsafe_allow_html=True,
    )
    st.write("")

    results = st.session_state.get("loading_results", {})
    if results:
        with st.expander("Debug: hasil yang udah kekumpul (sementara)"):
            st.json(results)

    col_l, col_mid, col_r = st.columns([1.6, 1.6, 1.6])
    with col_mid:
        if st.button("Kembali ke Home", key="btn_back_home_from_result",
                      type="secondary", icon=":material/arrow_back:", use_container_width=True):
            st.session_state.dr_page = "home"
            for k in ("loading_points", "loading_idx", "loading_phase", "loading_results", "loading_data"):
                st.session_state.pop(k, None)
            st.rerun()
