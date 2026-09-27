"""
Halaman Tutorial — sekarang dipecah jadi 2 tab (per instruksi Stev,
27 Sep 2026):
- Tab 1 "Kenalan Sistemnya": daftar semua sistem pembacaan (chip) beserta
  ikon, penjelasan singkat, dan apa yang bisa didapatkan — REUSE dari data
  SEMUA_SISTEM yang sudah ada di app.py (dipakai juga buat popover chip di
  homepage), bukan konten baru.
- Tab 2 "Alur & Pilihan": penjelasan alur dari awal (Verifikasi Email)
  sampai akhir (pilih Versi Pendek/Lengkap), sekalian nyebutin pilihan apa
  aja yang tersedia di tiap langkah (mode Instan/Mendalam/Lengkap, tier
  laporan Pendek/Lengkap) — REUSE data dari RY_MODES (reveal_yourself.py)
  dan PRICE_PENDEK/PRICE_PANJANG/PRICE_UPGRADE_SELISIH (settings.py) biar
  harga & pilihan yang ditampilkan selalu sinkron sama yang beneran jalan
  di app, bukan angka/teks yang diketik ulang manual dan gampang basi.
"""

import streamlit as st

from settings import PRICE_PANJANG, PRICE_PENDEK, PRICE_UPGRADE_SELISIH
from views.reveal_yourself import RY_MODES


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

        /* ── Tab 2: alur & pilihan ── */
        .tp-flow-step { display: flex; gap: 16px; padding: 20px 0; border-bottom: 1px solid #f0e6d5; }
        .tp-flow-step:last-of-type { border-bottom: none; }
        .tp-flow-num { width: 36px; height: 36px; border-radius: 50%; background: #b8562f;
            color: #ffffff !important; display: flex; align-items: center; justify-content: center;
            font-weight: 800; font-size: 15px; flex-shrink: 0; }
        .tp-flow-title { font-family: 'Fraunces', serif; font-size: 17px; font-weight: 700;
            color: #1c1a17 !important; margin-bottom: 4px; }
        .tp-flow-desc { font-size: 13.5px; color: #5c564d !important; line-height: 1.65;
            margin-bottom: 10px; }
        .tp-opt-row { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 4px; }
        .tp-opt-card { flex: 1 1 220px; min-width: 200px; border: 1.5px solid #ecddc9;
            border-radius: 12px; padding: 12px 14px; background: #fdfaf5; }
        .tp-opt-title { font-size: 12.5px; font-weight: 800; color: #8a5a2f !important;
            text-transform: uppercase; letter-spacing: 0.03em; }
        .tp-opt-price { font-size: 15px; font-weight: 800; color: #1c1a17 !important; margin: 2px 0 6px 0; }
        .tp-opt-desc { font-size: 12.5px; color: #6b6459 !important; line-height: 1.55; }
        .tp-opt-chips { display: flex; flex-wrap: wrap; gap: 5px; margin-top: 8px; }
        .tp-opt-chip { font-size: 10.5px; font-weight: 700; color: #8a5a2f !important;
            background: #fdf3e7; border: 1px solid #ecddc9; border-radius: 100px; padding: 3px 9px; }
        .tp-note { font-size: 12px; color: #9a948a !important; font-style: italic; margin-top: 14px; }
        </style>
        """,
        unsafe_allow_html=True,
    )


def _render_chip_directory(semua_sistem):
    """Tab 1 — isi persis konten lama (daftar 15 sistem/chip)."""
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
            "Mulai Reveal Sekarang", key="tp_cta_reveal_tab1",
            type="primary", icon=":material/bolt:", use_container_width=True,
        ):
            st.session_state.dr_page = "reveal"
            st.rerun()


def _render_flow_guide():
    """Tab 2 — alur reveal dari awal (Verifikasi Email) sampai akhir
    (pilih Versi Pendek/Lengkap), plus pilihan yang tersedia di tiap
    langkah. Data mode & harga di-reuse dari RY_MODES/settings.py biar
    nggak ada 2 sumber kebenaran yang bisa beda sendiri-sendiri."""
    st.markdown(
        '<div class="tp-header">'
        '<span class="tp-badge">&#10022; Panduan Alur</span>'
        '<h1 class="tp-h1 rp-serif">Begini Alurnya, dari Awal sampai Akhir</h1>'
        '<p class="tp-sub">5 langkah, kira-kira 3-5 menit — nggak perlu bikin akun, '
        'dan progresmu otomatis kesimpen kalau halaman ke-refresh.</p>'
        '</div>',
        unsafe_allow_html=True,
    )

    harga_pendek = f"{PRICE_PENDEK:,.0f}".replace(",", ".")
    harga_panjang = f"{PRICE_PANJANG:,.0f}".replace(",", ".")
    harga_selisih = f"{PRICE_UPGRADE_SELISIH:,.0f}".replace(",", ".")

    mode_opts_html = "".join(
        '<div class="tp-opt-card">'
        f'<div class="tp-opt-title">{title}</div>'
        f'<div class="tp-opt-desc">{desc}</div>'
        '<div class="tp-opt-chips">'
        + "".join(f'<span class="tp-opt-chip">{chip}</span>' for chip in chips)
        + '</div></div>'
        for _key, title, desc, chips in RY_MODES
    )

    steps_html = (
        '<div class="tp-flow-step">'
        '<div class="tp-flow-num">1</div>'
        '<div style="flex:1;">'
        '<div class="tp-flow-title">Verifikasi Email</div>'
        '<div class="tp-flow-desc">Cukup masukin email buat nyimpen & buka hasil nanti — '
        'nggak perlu bikin akun/password. Kalau ada kode referal dari teman, bisa dimasukin '
        'di sini juga (opsional).</div>'
        '</div></div>'

        '<div class="tp-flow-step">'
        '<div class="tp-flow-num">2</div>'
        '<div style="flex:1;">'
        '<div class="tp-flow-title">Pilih Fokus Eksplorasi (Mode)</div>'
        '<div class="tp-flow-desc">Pilihan ini menentukan sistem mana yang dihitung untuk '
        'laporanmu:</div>'
        f'<div class="tp-opt-row">{mode_opts_html}</div>'
        '</div></div>'

        '<div class="tp-flow-step">'
        '<div class="tp-flow-num">3</div>'
        '<div style="flex:1;">'
        '<div class="tp-flow-title">Proses Reveal (Loading per Titik)</div>'
        '<div class="tp-flow-desc">Tiap sistem di mode yang kamu pilih diproses satu per satu '
        '(kalau perlu data tambahan seperti tanggal lahir, bakal ditanya sekali lewat jendela '
        'kecil, dipakai ulang buat titik lain yang butuh data sama). Proses ini nggak bisa '
        'di-skip, tapi kalau halamannya ke-refresh nggak perlu ulang dari awal — lanjut dari '
        'titik terakhir.</div>'
        '</div></div>'

        '<div class="tp-flow-step">'
        '<div class="tp-flow-num">4</div>'
        '<div style="flex:1;">'
        '<div class="tp-flow-title">Hasil Reveal (Buka Amplop)</div>'
        '<div class="tp-flow-desc">Semua titik yang udah diproses muncul sebagai amplop '
        'tersegel. Bisa dibuka satu-satu, atau langsung "Buka Semua Amplop" sekaligus kalau '
        'nggak sabar.</div>'
        '</div></div>'

        '<div class="tp-flow-step">'
        '<div class="tp-flow-num">5</div>'
        '<div style="flex:1;">'
        '<div class="tp-flow-title">Pilih Versi Laporan</div>'
        '<div class="tp-flow-desc">Sebelum amplop kebuka, pilih dulu versi laporannya:</div>'
        '<div class="tp-opt-row">'
        '<div class="tp-opt-card">'
        '<div class="tp-opt-title">Versi Pendek</div>'
        f'<div class="tp-opt-price">Rp {harga_pendek}</div>'
        '<div class="tp-opt-desc">Semua hasil inti — siapa diri kamu, kekuatan pada dirimu, '
        'dan PR apa yang harus dikerjakan.</div>'
        '</div>'
        '<div class="tp-opt-card">'
        '<div class="tp-opt-title">Versi Lengkap</div>'
        f'<div class="tp-opt-price">Rp {harga_panjang}</div>'
        '<div class="tp-opt-desc">Semua hasil inti, plus insight Karir, Asmara, Keuangan & '
        'Kesehatan buat tiap sistem — langsung kebuka semua amplop tanpa perlu bayar satu-satu '
        'lagi.</div>'
        '</div>'
        '</div>'
        f'<div class="tp-note">Sudah kadung ambil Versi Pendek? Masih bisa upgrade belakangan '
        f'per-amplop dengan bayar selisihnya (Rp {harga_selisih}) — begitu bayar, insight '
        'tambahan itu langsung kebuka di SEMUA amplop sekaligus, bukan cuma yang lagi dibuka.</div>'
        '</div></div>'
    )
    st.markdown(steps_html, unsafe_allow_html=True)

    st.write("")
    cta_l, cta_mid, cta_r = st.columns([1.5, 1.4, 1.5])
    with cta_mid:
        if st.button(
            "Mulai Reveal Sekarang", key="tp_cta_reveal_tab2",
            type="primary", icon=":material/bolt:", use_container_width=True,
        ):
            st.session_state.dr_page = "reveal"
            st.rerun()


def render(semua_sistem):
    """
    semua_sistem: list of tuple (nama, icon_material, apa_ini, topik_list,
    ajakan, aktif) — sama persis struktur SEMUA_SISTEM di app.py, dilempar
    dari sana biar datanya cuma didefinisikan sekali di satu tempat.
    """
    _inject_style()

    tab1, tab2 = st.tabs(["📖 Kenalan Sistemnya", "🧭 Alur & Pilihan"])
    with tab1:
        _render_chip_directory(semua_sistem)
    with tab2:
        _render_flow_guide()
