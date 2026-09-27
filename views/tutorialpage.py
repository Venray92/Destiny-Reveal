"""
Halaman Tutorial — daftar semua sistem pembacaan (chip) beserta ikon,
penjelasan singkat, dan apa yang bisa didapatkan dari tiap sistem.

Kontennya REUSE dari data SEMUA_SISTEM yang sudah ada di app.py (dipakai
juga buat popover chip di homepage) — bukan konten baru, cuma ditampilkan
lengkap di satu halaman biar user nggak perlu klik satu-satu buat baca
semua penjelasannya.
"""

import streamlit as st


def _inject_style():
    st.markdown(
        """
        <style>
        .tp-header { text-align: center; display: flex; flex-direction: column;
            align-items: center; gap: 10px; margin-bottom: 26px; }
        .tp-badge { display: inline-flex; align-items: center; gap: 6px; padding: 7px 18px;
            border-radius: 100px; background: #fdf3e7; border: 1px solid #ecddc9;
            font-size: 12.5px; font-weight: 700; color: #b8562f !important; }
        .tp-h1 { margin: 0; font-size: 30px; font-weight: 700; color: #1c1a17 !important;
            max-width: 640px; line-height: 1.25; }
        .tp-sub { margin: 0; font-size: 14px; color: #6b6459 !important; max-width: 560px;
            line-height: 1.7; }

        .tp-card { padding: 22px 22px 20px 22px; border-radius: 18px; background: #ffffff;
            border: 2px solid #ece6dc; height: 100%; box-sizing: border-box; }
        .tp-card-head { display: flex; align-items: center; gap: 12px; margin-bottom: 4px; }
        .tp-card-icon { width: 42px; height: 42px; border-radius: 12px; background: #fdf3e7;
            display: flex; align-items: center; justify-content: center; color: #b8562f !important;
            flex-shrink: 0; overflow: hidden; white-space: nowrap; }
        .tp-card-title { font-family: 'Fraunces', serif; font-size: 17px; font-weight: 700;
            color: #1c1a17 !important; }
        .tp-card-status { font-size: 10px; font-weight: 800; letter-spacing: 0.05em;
            text-transform: uppercase; margin-top: 2px; }
        .tp-card-status-aktif { color: #8a5a2f !important; }
        .tp-card-status-segera { color: #9a948a !important; }
        .tp-card-desc { font-size: 13px; color: #5c564d !important; line-height: 1.65;
            margin: 10px 0 12px 0; }
        .tp-card-label { font-size: 11.5px; font-weight: 800; color: #3a362f !important;
            text-transform: uppercase; letter-spacing: 0.04em; margin-bottom: 6px; }
        .tp-card-topik { font-size: 13px; color: #3a362f !important; margin: 3px 0; }
        .tp-card-topik span { color: #b8562f !important; }
        .tp-card-ajakan { font-size: 12px; color: #8a5a2f !important; font-style: italic;
            margin-top: 12px; padding-top: 10px; border-top: 1px dashed #ecddc9; }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render(semua_sistem):
    """
    semua_sistem: list of tuple (nama, icon_material, apa_ini, topik_list,
    ajakan, aktif) — sama persis struktur SEMUA_SISTEM di app.py, dilempar
    dari sana biar datanya cuma didefinisikan sekali di satu tempat.
    """
    _inject_style()

    st.markdown(
        '<div class="tp-header">'
        '<span class="tp-badge">&#10022; Panduan Baca Hasil</span>'
        '<h1 class="tp-h1 rp-serif">Kenalan Dulu Sama 15 Sistemnya</h1>'
        '<p class="tp-sub">Tiap sistem membaca sisi yang beda dari dirimu. Klik "Mulai Reveal" '
        'kalau sudah siap, atau baca dulu di sini biar tahu apa yang bakal kamu dapatkan dari '
        'tiap sistemnya.</p>'
        '</div>',
        unsafe_allow_html=True,
    )

    n_per_row = 3
    for i in range(0, len(semua_sistem), n_per_row):
        chunk = semua_sistem[i:i + n_per_row]
        cols = st.columns(n_per_row)
        for col, (nama, icon, apa_ini, topik_list, ajakan, aktif) in zip(cols, chunk):
            with col:
                status_label = "Sudah Aktif" if aktif else "Segera Hadir"
                status_cls = "tp-card-status-aktif" if aktif else "tp-card-status-segera"
                topik_html = "".join(
                    f'<div class="tp-card-topik"><span>&#8226;</span> {topik}</div>'
                    for topik in topik_list
                )
                st.markdown(
                    '<div class="tp-card">'
                    '<div class="tp-card-head">'
                    f'<div class="tp-card-icon"><span class="material-symbols-outlined">{icon}</span></div>'
                    '<div>'
                    f'<div class="tp-card-title">{nama}</div>'
                    f'<div class="tp-card-status {status_cls}">{status_label}</div>'
                    '</div></div>'
                    f'<div class="tp-card-desc">{apa_ini}</div>'
                    '<div class="tp-card-label">Bisa bantu kamu tahu</div>'
                    f'{topik_html}'
                    f'<div class="tp-card-ajakan">{ajakan}</div>'
                    '</div>',
                    unsafe_allow_html=True,
                )
        st.write("")

    st.write("")
    cta_l, cta_mid, cta_r = st.columns([1.5, 1.4, 1.5])
    with cta_mid:
        if st.button(
            "Mulai Reveal Sekarang", key="tp_cta_reveal",
            type="primary", icon=":material/bolt:", use_container_width=True,
        ):
            st.session_state.dr_page = "reveal"
            st.rerun()
