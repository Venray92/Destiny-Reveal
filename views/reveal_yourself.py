"""
Halaman "Reveal Yourself" — form screening 3 langkah.

Dipisah dari app.py (bukan ditaruh di file utama) biar app.py nggak makin
gemuk tiap ada halaman baru. Visual/layout di sini ngikutin mock design yang
dibuat di Design canvas (kartu-kartu langkah dengan icon badge, background
gradient cream + blob dekoratif, "Pilih Fokus" jadi kartu bukan radio polos).

Logic submit (OTP, simpan ke Supabase, dst) masih belum jalan — itu next step
terpisah, bukan bagian dari revisi visual ini.
"""

import streamlit as st


def _inject_style():
    st.markdown(
        """
        <style>
        /* Wrapper seluruh halaman: background gradient cream + 2 blob
           dekoratif lewat ::before/::after (dekorasi doang, gak ganggu
           konten), biar gak polos putih kayak sebelumnya. */
        .st-key-reveal_page_wrap {
            position: relative;
            background: linear-gradient(180deg, #fdf3e4 0%, #fdf9f2 30%, #fbf6ec 100%);
            border-radius: 32px;
            padding: 44px 52px 52px 52px;
            overflow: hidden;
            box-shadow: 0 30px 70px -40px rgba(139,90,47,0.35);
        }
        .st-key-reveal_page_wrap::before {
            content: "";
            position: absolute; top: -160px; right: -140px;
            width: 420px; height: 420px; border-radius: 50%;
            background: radial-gradient(circle at 30% 30%, rgba(201,104,58,0.16), rgba(201,104,58,0) 70%);
            pointer-events: none; z-index: 0;
        }
        .st-key-reveal_page_wrap::after {
            content: "";
            position: absolute; bottom: -160px; left: -140px;
            width: 380px; height: 380px; border-radius: 50%;
            background: radial-gradient(circle at 50% 50%, rgba(228,165,110,0.2), rgba(228,165,110,0) 70%);
            pointer-events: none; z-index: 0;
        }
        .st-key-reveal_page_wrap [data-testid="stVerticalBlockBorderWrapper"],
        .st-key-reveal_page_wrap > div {
            position: relative; z-index: 1;
        }

        .ry-hero-badge {
            display: inline-flex; align-items: center; gap: 8px;
            padding: 7px 18px; border-radius: 100px; background: #ffffff;
            border: 1px solid #ecddc9; font-size: 12.5px; font-weight: 700;
            color: #b8562f !important;
            box-shadow: 0 6px 18px -10px rgba(184,86,47,0.35);
            margin-bottom: 14px;
        }
        .ry-hero-title {
            font-family: 'Fraunces', serif; font-size: 36px; font-weight: 700;
            color: #1c1a17 !important; margin-bottom: 10px;
        }
        .ry-hero-sub {
            font-size: 15px; color: #6b6459 !important; max-width: 560px;
            margin: 0 auto 26px auto; line-height: 1.7;
        }

        .ry-stepper { display: flex; align-items: flex-start; max-width: 520px; margin: 0 auto; }
        .ry-step-unit { display: flex; flex-direction: column; align-items: center; flex-shrink: 0; }
        .ry-step-dot {
            width: 38px; height: 38px; border-radius: 50%; background: #b8562f;
            color: #ffffff !important; display: flex; align-items: center; justify-content: center;
            font-weight: 800; font-size: 14.5px; flex-shrink: 0;
        }
        .ry-step-label {
            font-size: 11px; font-weight: 700; color: #6b6459 !important;
            margin-top: 6px; text-align: center; white-space: nowrap;
        }
        .ry-step-line { flex-grow: 1; height: 3px; background: #ecddc9; margin: 19px 8px 0 8px; border-radius: 3px; }

        /* Kartu tiap langkah */
        .st-key-ry_card_1, .st-key-ry_card_2, .st-key-ry_card_3 {
            background: #ffffff; border: 2px solid #f0e6d5; border-radius: 22px;
            padding: 28px 32px 8px 32px; box-shadow: 0 22px 55px -30px rgba(139,90,47,0.28);
            margin-bottom: 4px;
        }
        .ry-card-head { display: flex; gap: 18px; align-items: flex-start; margin-bottom: 6px; }
        .ry-card-icon {
            width: 52px; height: 52px; border-radius: 15px;
            background: linear-gradient(135deg, #fdf3e7, #f6dfc2);
            display: flex; align-items: center; justify-content: center; flex-shrink: 0;
            color: #b8562f !important; overflow: hidden;
        }
        /* overflow:hidden di atas + font-size kecil ini jaga-jaga kalau font
           Material Symbols gagal load (mis. jaringan diblokir): teksnya
           kepotong rapi di dalam kotak, bukan meluber keluar. */
        .ry-card-icon .material-symbols-outlined { font-size: 24px; white-space: nowrap; }
        .ry-card-icon svg { width: 24px; height: 24px; }
        .ry-card-step-label { font-size: 11px; font-weight: 800; letter-spacing: 0.08em; text-transform: uppercase; color: #b8562f !important; }
        .ry-card-title { font-family: 'Fraunces', serif; font-size: 20px; font-weight: 700; color: #1c1a17 !important; margin-top: 3px; }
        .ry-card-desc { font-size: 13px; color: #6b6459 !important; margin-top: 3px; }

        /* Tombol "Kirim Kode" default-nya pakai padding global button (14px 32px)
           yang bikin tingginya 54px, jauh lebih gede dari kolom Alamat Email
           di sebelahnya yang cuma 40px. Disamakan tingginya di sini, scoped
           lewat container key biar tombol lain (mode, back, dst) nggak ikut. */
        .st-key-ry_otp_btn button[kind="secondary"] {
            height: 40px !important; min-height: 40px !important;
            padding: 0 18px !important; font-size: 14px !important;
        }

        /* OTP boxes dekoratif */
        .ry-otp-row { display: flex; gap: 8px; margin: 4px 0 14px 0; }
        .ry-otp-box {
            width: 42px; height: 46px; border: 1.5px solid #ecddc9; border-radius: 10px;
            background: #fdf9f2;
        }

        /* "Pilih Fokus" -> 3 kartu mode (bukan radio native, karena label
           radio Streamlit cuma bisa teks polos, nggak bisa dikasih daftar
           chip sistem di dalamnya). Pilihannya tetap fungsional lewat
           tombol "Pilih" di tiap kartu + session_state, bukan cuma dekorasi. */
        [data-testid="stHorizontalBlock"]:has([class*="ry-mode-fill"]) { align-items: stretch !important; }
        [data-testid="stColumn"]:has([class*="ry-mode-fill"]) {
            display: flex !important; flex-direction: column !important;
        }
        [data-testid="stVerticalBlock"]:has([class*="ry-mode-fill"]),
        [data-testid="stLayoutWrapper"]:has([class*="ry-mode-fill"]) {
            display: flex !important; flex-direction: column !important;
            flex: 1 !important; min-height: 0 !important;
        }
        [class*="ry-mode-fill"] {
            display: flex !important; flex-direction: column !important;
            flex: 1 !important; min-height: 0 !important;
        }
        /* Propagasi flex:1 harus nyambung sampai elemen kartunya sendiri —
           kalau cuma dipasang di ry-mode-fill doang, pembungkus di antaranya
           (stElementContainer, stMarkdown, dst) nggak ikut melar, jadi
           tinggi kartu tetap ngikut kontennya sendiri-sendiri, bukan ke
           kartu paling tinggi di barisnya (ini persis bug yang ketemu waktu
           nyamain tinggi kartu step/bulk di homepage dulu). */
        .st-key-ry_mode_instan, .st-key-ry_mode_mendalam, .st-key-ry_mode_lengkap {
            display: flex !important; flex-direction: column !important; flex: 1 !important;
        }
        /* :has(.stMarkdown) supaya cuma stElementContainer pembungkus
           kartunya yang ikut melar — punya tombol "Pilih Mode Ini" di
           bawahnya sengaja TIDAK disentuh, biar tombol tetap ukuran
           natural, nempel rapi di bawah kartu. */
        .st-key-ry_mode_instan [data-testid="stElementContainer"]:has(.stMarkdown),
        .st-key-ry_mode_mendalam [data-testid="stElementContainer"]:has(.stMarkdown),
        .st-key-ry_mode_lengkap [data-testid="stElementContainer"]:has(.stMarkdown),
        .st-key-ry_mode_instan .stMarkdown,
        .st-key-ry_mode_mendalam .stMarkdown,
        .st-key-ry_mode_lengkap .stMarkdown,
        .st-key-ry_mode_instan .stMarkdown > div,
        .st-key-ry_mode_mendalam .stMarkdown > div,
        .st-key-ry_mode_lengkap .stMarkdown > div,
        .st-key-ry_mode_instan [data-testid="stMarkdownContainer"],
        .st-key-ry_mode_mendalam [data-testid="stMarkdownContainer"],
        .st-key-ry_mode_lengkap [data-testid="stMarkdownContainer"] {
            display: flex !important; flex-direction: column !important;
            flex: 1 !important; min-height: 0 !important;
        }
        .ry-mode-card {
            border: 2px solid #ecddc9; border-radius: 18px; padding: 20px 20px 16px 20px;
            background: #fdfaf5; display: flex; flex-direction: column; gap: 10px;
            flex-grow: 1;
        }
        .ry-mode-card-active {
            border-color: #b8562f; background: #fff8ef;
            box-shadow: 0 16px 34px -18px rgba(184,86,47,0.45);
        }
        .ry-mode-title { font-weight: 700; font-size: 15.5px; color: #1c1a17 !important; }
        .ry-mode-desc { font-size: 12.5px; color: #6b6459 !important; line-height: 1.55; }
        .ry-mode-chips { display: flex; flex-wrap: wrap; gap: 6px; flex-grow: 1; align-content: flex-start; }
        .ry-mode-chip {
            display: inline-block; padding: 5px 12px; border-radius: 100px;
            background: #ffffff; border: 1px solid #e4ddd0; color: #1c1a17 !important;
            font-size: 11.5px; font-weight: 600; white-space: nowrap;
        }
        .st-key-ry_mode_instan div.stButton > button,
        .st-key-ry_mode_mendalam div.stButton > button,
        .st-key-ry_mode_lengkap div.stButton > button {
            margin-top: 12px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


# 15 sistem dibagi jadi 3 mode. "Instan" = cukup tanggal lahir, "Mendalam" =
# nambah kuesioner buat kenal karakter, "Lengkap" = semua 15 sistem sekaligus
# (samain kategori yang udah ada di homepage, section "Satu Data, Banyak Cara
# Pandang", biar konsisten).
RY_MODES = [
    (
        "instan", "Mode Instan",
        "Cepat, cukup dari tanggal lahir.",
        ["Zodiak", "Shio", "Weton", "Numerologi", "Matrix Destiny"],
    ),
    (
        "mendalam", "Mode Mendalam",
        "Tambah kuesioner buat kenal karaktermu lebih jauh.",
        ["MBTI", "Big Five", "Enneagram", "DISC", "Golongan Darah", "Love Language"],
    ),
    (
        "lengkap", "Mode Lengkap",
        "Semua sistem sekaligus, paling menyeluruh.",
        [
            "Zodiak", "Shio", "Weton", "Numerologi", "Matrix Destiny", "BaZi",
            "Zi Wei", "Human Design", "MBTI", "Big Five", "Enneagram", "DISC",
            "Golongan Darah", "Love Language", "Tarot",
        ],
    ),
]


def render():
    """Render halaman Reveal Yourself (form screening 3 langkah)."""
    _inject_style()

    with st.container(key="reveal_page_wrap"):

        back_l, back_r = st.columns([1.6, 5.4])
        with back_l:
            if st.button(
                "Kembali ke Home", key="btn_back_home", type="secondary",
                icon=":material/arrow_back:", use_container_width=True,
            ):
                st.session_state.dr_page = "home"
                st.rerun()

        st.markdown(
            '<div style="text-align:center;padding-top:8px;">'
            '<span class="ry-hero-badge">✧ Butuh 3 menit, tanpa akun</span>'
            '<div class="ry-hero-title">Reveal Yourself</div>'
            '<div class="ry-hero-sub">Ikuti tiga langkah singkat ini untuk membuka pembacaan '
            'lengkap dari 15 sistem sekaligus.</div>'
            '</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<div class="ry-stepper">'
            '<div class="ry-step-unit"><div class="ry-step-dot">1</div>'
            '<div class="ry-step-label">Verifikasi<br>Email</div></div>'
            '<div class="ry-step-line"></div>'
            '<div class="ry-step-unit"><div class="ry-step-dot">2</div>'
            '<div class="ry-step-label">Isi Data<br>Lahir</div></div>'
            '<div class="ry-step-line"></div>'
            '<div class="ry-step-unit"><div class="ry-step-dot">3</div>'
            '<div class="ry-step-label">Pilih Fokus<br>Eksplorasi</div></div>'
            '</div>',
            unsafe_allow_html=True,
        )
        st.write("")

        # ── STEP 1 — Verifikasi Email ──
        with st.container(key="ry_card_1"):
            st.markdown(
                '<div class="ry-card-head">'
                '<div class="ry-card-icon">'
                '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
                'stroke-linecap="round" stroke-linejoin="round">'
                '<rect x="3" y="5" width="18" height="14" rx="2.5"></rect>'
                '<path d="M3.5 6.5 12 13l8.5-6.5"></path>'
                '</svg></div>'
                '<div><div class="ry-card-step-label">Langkah 1 dari 3</div>'
                '<div class="ry-card-title">Verifikasi Email</div>'
                '<div class="ry-card-desc">Tidak perlu membuat akun. Cukup email untuk '
                'menyimpan &amp; membuka hasilmu nanti.</div></div></div>',
                unsafe_allow_html=True,
            )
            vcol1, vcol2 = st.columns([3, 1.2])
            with vcol1:
                st.text_input("Alamat Email", placeholder="nama@email.com", key="ry_email")
            with vcol2:
                st.markdown('<div style="height:28px;"></div>', unsafe_allow_html=True)
                with st.container(key="ry_otp_btn"):
                    st.button(
                        "Kirim Kode", key="btn_send_otp", type="secondary",
                        icon=":material/send:", use_container_width=True,
                    )
            st.markdown('<div class="ry-otp-row">' + '<div class="ry-otp-box"></div>' * 6 + '</div>', unsafe_allow_html=True)

        st.write("")

        # ── STEP 2 — Isi Data Lahir ──
        with st.container(key="ry_card_2"):
            st.markdown(
                '<div class="ry-card-head">'
                '<div class="ry-card-icon">'
                '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
                'stroke-linecap="round" stroke-linejoin="round">'
                '<path d="M6 4h9l4 4v12a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1Z"></path>'
                '<path d="M14 4v4h4"></path>'
                '<path d="M8.5 13h7M8.5 16.5h4.5"></path>'
                '</svg></div>'
                '<div><div class="ry-card-step-label">Langkah 2 dari 3</div>'
                '<div class="ry-card-title">Isi Data Lahir</div>'
                '<div class="ry-card-desc">3 kolom pertama wajib diisi. Sisanya opsional, namun '
                'membuat hasil BaZi &amp; Human Design lebih akurat.</div></div></div>',
                unsafe_allow_html=True,
            )
            fcol1, fcol2 = st.columns(2)
            with fcol1:
                st.text_input("Nama Lengkap *", placeholder="Nama sesuai identitas", key="ry_nama")
                st.date_input("Tanggal Lahir *", key="ry_tanggal")
                st.selectbox("Jenis Kelamin (opsional)", ["— Pilih —", "Laki-laki", "Perempuan"], key="ry_gender")
            with fcol2:
                st.time_input("Jam Lahir (opsional, tapi disarankan)", key="ry_jam")
                st.text_input("Kota Lahir (opsional)", placeholder="Contoh: Jakarta", key="ry_kota")
                st.selectbox("Bahasa Laporan", ["Bahasa Indonesia", "English"], key="ry_bahasa")
            st.write("")

        st.write("")

        # ── STEP 3 — Pilih Fokus Eksplorasi ──
        with st.container(key="ry_card_3"):
            st.markdown(
                '<div class="ry-card-head">'
                '<div class="ry-card-icon">'
                '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
                'stroke-linecap="round" stroke-linejoin="round">'
                '<path d="M12 3.5 13.7 9l5.3 1.7-5.3 1.7L12 18l-1.7-5.6L5 10.7 10.3 9Z"></path>'
                '<path d="M19 15.5 19.7 18l2.3.8-2.3.8L19 22l-.7-2.4-2.3-.8 2.3-.8Z"></path>'
                '</svg></div>'
                '<div><div class="ry-card-step-label">Langkah 3 dari 3</div>'
                '<div class="ry-card-title">Pilih Fokus Eksplorasi</div>'
                '<div class="ry-card-desc">Pilihan ini menentukan sistem mana yang dihitung '
                'untuk laporanmu.</div></div></div>',
                unsafe_allow_html=True,
            )
            if "ry_focus_mode" not in st.session_state:
                st.session_state.ry_focus_mode = None

            mode_cols = st.columns(3, gap="medium")
            for col, (mode_key, title, desc, chips) in zip(mode_cols, RY_MODES):
                with col:
                    with st.container(key=f"ry_mode_{mode_key}"):
                        active = st.session_state.ry_focus_mode == mode_key
                        chips_html = "".join(f'<span class="ry-mode-chip">{c}</span>' for c in chips)
                        st.markdown(
                            f'<div class="ry-mode-fill ry-mode-card{" ry-mode-card-active" if active else ""}">'
                            f'<div class="ry-mode-title">{title}</div>'
                            f'<div class="ry-mode-desc">{desc}</div>'
                            f'<div class="ry-mode-chips">{chips_html}</div>'
                            f'</div>',
                            unsafe_allow_html=True,
                        )
                        if st.button(
                            "Terpilih ✓" if active else "Pilih Mode Ini",
                            key=f"btn_mode_{mode_key}",
                            type="primary" if active else "secondary",
                            use_container_width=True,
                        ):
                            st.session_state.ry_focus_mode = mode_key
                            st.rerun()
            st.write("")

        st.write("")
        cta_l, cta_mid, cta_r = st.columns([1.6, 1.6, 1.6])
        with cta_mid:
            st.button(
                "Lanjut ke Ringkasan", key="btn_lanjut_form", type="primary",
                icon=":material/arrow_forward:", use_container_width=True,
            )

        st.write("")
        st.markdown(
            '<p class="dr-footer-copyright">© 2026 Destiny Reveal '
            '<span class="dr-footer-byline">· By Zio</span></p>',
            unsafe_allow_html=True,
        )
