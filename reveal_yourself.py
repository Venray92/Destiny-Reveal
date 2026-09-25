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

        .ry-stepper { display: flex; align-items: center; max-width: 520px; margin: 0 auto; }
        .ry-step-dot {
            width: 38px; height: 38px; border-radius: 50%; background: #b8562f;
            color: #ffffff !important; display: flex; align-items: center; justify-content: center;
            font-weight: 800; font-size: 14.5px; flex-shrink: 0;
        }
        .ry-step-line { flex-grow: 1; height: 3px; background: #ecddc9; margin: 0 8px; border-radius: 3px; }

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
        .ry-card-step-label { font-size: 11px; font-weight: 800; letter-spacing: 0.08em; text-transform: uppercase; color: #b8562f !important; }
        .ry-card-title { font-family: 'Fraunces', serif; font-size: 20px; font-weight: 700; color: #1c1a17 !important; margin-top: 3px; }
        .ry-card-desc { font-size: 13px; color: #6b6459 !important; margin-top: 3px; }

        /* OTP boxes dekoratif */
        .ry-otp-row { display: flex; gap: 8px; margin: 4px 0 14px 0; }
        .ry-otp-box {
            width: 42px; height: 46px; border: 1.5px solid #ecddc9; border-radius: 10px;
            background: #fdf9f2;
        }

        /* Radio "Pilih Fokus" -> dibikin kartu pilihan, bukan bulatan radio polos */
        .st-key-ry_focus_radio div[data-testid="stRadio"] > div[role="radiogroup"] {
            gap: 14px !important; flex-wrap: wrap; flex-direction: row !important;
        }
        .st-key-ry_focus_radio div[data-testid="stRadio"] label {
            flex: 1 1 0; min-width: 230px;
            border: 2px solid #ecddc9 !important; border-radius: 16px !important;
            padding: 16px 18px !important; background: #fdfaf5 !important;
            margin: 0 !important;
        }
        .st-key-ry_focus_radio div[data-testid="stRadio"] label:has(input:checked) {
            border-color: #b8562f !important; background: #fff8ef !important;
            box-shadow: 0 14px 30px -16px rgba(184,86,47,0.4);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


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
            '<div class="ry-step-dot">1</div><div class="ry-step-line"></div>'
            '<div class="ry-step-dot">2</div><div class="ry-step-line"></div>'
            '<div class="ry-step-dot">3</div>'
            '</div>',
            unsafe_allow_html=True,
        )
        st.write("")

        # ── STEP 1 — Verifikasi Email ──
        with st.container(key="ry_card_1"):
            st.markdown(
                '<div class="ry-card-head">'
                '<div class="ry-card-icon"><span class="material-symbols-outlined">mail</span></div>'
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
                '<div class="ry-card-icon"><span class="material-symbols-outlined">edit_note</span></div>'
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
                '<div class="ry-card-icon"><span class="material-symbols-outlined">auto_awesome</span></div>'
                '<div><div class="ry-card-step-label">Langkah 3 dari 3</div>'
                '<div class="ry-card-title">Pilih Fokus Eksplorasi</div>'
                '<div class="ry-card-desc">Pilihan ini menentukan sistem mana yang dihitung '
                'untuk laporanmu.</div></div></div>',
                unsafe_allow_html=True,
            )
            with st.container(key="ry_focus_radio"):
                st.radio(
                    "Mode Eksplorasi",
                    [
                        "Mode Instan — Weton, Zodiak, Shio & Numerologi",
                        "Mode Mendalam — MBTI, Big Five & Enneagram",
                        "Mode Lengkap — Semua sistem + skor kecocokan",
                    ],
                    label_visibility="collapsed",
                    key="ry_focus",
                )
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
