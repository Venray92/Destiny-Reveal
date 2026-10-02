"""
Modal "Reveal Dirimu" (SEMUA tombol/link Reveal membuka ini lewat open_reveal_modal()).
Satu st.dialog, isinya ganti-ganti per langkah (lihat components/flow_state.py).
Alur lengkap baru untuk Mode 1; Mode 2 & 3 masih diteruskan ke halaman Reveal lama.
Transisi antar langkah pakai on_click callback (rerun fragment dialog, dialog
tetap kebuka) — JANGAN pakai st.rerun() biasa, itu nutup dialog.
"""

from datetime import date

import streamlit as st

from components import modal_steps
from components.flow_state import (
    STEP_FORM, STEP_LOADING, STEP_PAY, STEP_RESULT, STEP_VERIFY, current_step, set_step,
)

# (key = ry_focus_mode di reveal_yourself.py, tag, judul, pill, bullets, ribbon, info)
MODAL_MODES = [
    ("instan", "MODE 1", "5 Sistem Kelahiran", "Tanpa Kuesioner",
     [("Zodiak", "♈️"), ("Shio", "🐉"), ("Weton", "🗓️"), ("Numerologi", "🔢"), ("Matrix Destiny", "🔹")],
     "", "1 Koin", "Proses Cepat",
     "Mode 1: Berbasis data lahir mutlak. Tidak perlu kuesioner, langsung lanjut ke verifikasi &amp; cetak biru."),
    ("mendalam", "MODE 2", "5 Sistem Psikologi", "Perlu Kuesioner",
     [("MBTI", "🧠"), ("Big Five", "📊"), ("Enneagram", "🔺"), ("DISC", "🎯"), ("Love Language", "💖")],
     "", "2 Koin", "Psikologi Jiwa",
     "Mode 2: Berbasis kuesioner singkat. Kamu akan diminta menjawab beberapa soal setelah verifikasi."),
    ("lengkap", "MODE 3", "15 Sistem Sekaligus", "",
     [("5 Sistem Kelahiran", "♈️"), ("5 Sistem Psikologi", "🧠"), ("BaZi &amp; Zi Wei", "🏮"),
      ("Human Design", "🔮"), ("Golongan Darah &amp; Tarot", "🩸")],
     "Terlengkap", "5 Koin", "Semua Terbuka",
     "Mode 3: Gabungan data lahir &amp; kuesioner. Seluruh 15 sistem dibuka dalam satu laporan."),
]
_GOLDA_OPTIONS = ["A", "B", "AB", "O", "Belum tahu"]


def _cb_pick_mode(key):
    st.session_state.dh_modal_mode = key


def _cb_form_next(mode):
    nama = (st.session_state.get("dhm_nama") or "").strip()
    tgl = st.session_state.get("dhm_tgl")
    if not nama or not tgl:
        st.session_state.dh_flow_error = "Isi Nama dan Tanggal Lahir dulu ya (bagian yang bertanda Wajib)."
        return
    st.session_state.dh_flow_error = None
    jam = st.session_state.get("dhm_jam")
    st.session_state.dh_modal_data = {
        "nama": nama, "tgl_lahir": tgl,
        "jam_lahir": jam.strftime("%H:%M") if jam else "",
        "kota_lahir": (st.session_state.get("dhm_kota") or "").strip(),
        "golongan_darah": st.session_state.get("dhm_golda") or "",
    }
    if mode == "instan":
        # email udah pernah diverifikasi (mis. habis "Scan Orang Lain") -> langsung bayar
        set_step(STEP_PAY if st.session_state.get("dh_email_verified") else STEP_VERIFY)
    else:
        # Mode 2 & 3: alur baru belum dibuat -> teruskan ke halaman Reveal lama
        st.session_state.ry_focus_mode = mode
        st.session_state.dh_flow_exit = True


def _render_form():
    mode = st.session_state.get("dh_modal_mode", "instan")
    st.markdown(
        '<div class="dh-step dh-step-form"></div>'
        '<div class="dh-modal-head">'
        '<div class="dh-modal-eyebrow">LANGKAH AWAL · PENEMUAN DIRI</div>'
        '<div class="dh-modal-title">Reveal Dirimu</div>'
        '<div class="dh-modal-sub">Isi tanggal lahir dan tentukan mode pembacaan yang kamu inginkan.</div>'
        '</div>',
        unsafe_allow_html=True,
    )

    with st.container(key="dhmodal_sec1"):
        st.markdown(
            '<div class="dh-modal-section"><span>📅 TANGGAL LAHIR &amp; IDENTITAS DASAR</span>'
            '<em>Wajib</em></div>',
            unsafe_allow_html=True,
        )
        c1, c2 = st.columns([1.15, 1], gap="small")
        with c1:
            st.text_input("Nama Lengkap / Panggilan", placeholder="Contoh: Rina Anggraini", key="dhm_nama")
        with c2:
            st.date_input(
                "Tanggal Lahir", value=None, min_value=date(1900, 1, 1), max_value=date.today(),
                format="DD/MM/YYYY", key="dhm_tgl",
            )
        c3, c4, c5 = st.columns(3, gap="small")
        with c3:
            st.time_input("Jam Lahir (Opsional)", value=None, key="dhm_jam")
        with c4:
            st.text_input("Kota Lahir (Opsional)", placeholder="Contoh: Jakarta", key="dhm_kota")
        with c5:
            st.selectbox("Golongan Darah", _GOLDA_OPTIONS, index=None, placeholder="Pilih", key="dhm_golda")

    with st.container(key="dhmodal_sec2"):
        st.markdown(
            '<div class="dh-modal-section"><span>✨ PILIH MODE PEMBACAAN TAKDIR</span></div>'
            '<div class="dh-modal-hint">Pilih cakupan sistem yang ingin kamu ungkap hari ini:</div>',
            unsafe_allow_html=True,
        )
        mcols = st.columns(3, gap="small")
        info = ""
        for col, (key, tag, title, pill, bullets, ribbon, coin, foot, msg) in zip(mcols, MODAL_MODES):
            selected = key == mode
            if selected:
                info = msg
            with col:
                with st.container(key=f"dhmodal_mode_{key}"):
                    pill_html = f'<span class="dh-mm-pill">{pill}</span>' if pill else ""
                    ribbon_html = f'<span class="dh-mm-ribbon">{ribbon}</span>' if ribbon else ""
                    list_html = '<ul class="dh-mm-list">' + "".join(
                        f'<li>{n} <i>{e}</i></li>' for n, e in bullets) + '</ul>'
                    st.markdown(
                        f'<div class="dh-mm{" dh-mm-sel" if selected else ""}">{ribbon_html}'
                        f'<div class="dh-mm-top"><span class="dh-mm-tag">{tag}</span>{pill_html}</div>'
                        f'<div class="dh-mm-title">{title}</div>{list_html}'
                        f'<div class="dh-mm-foot"><b>{coin}</b><span>{foot}</span></div></div>',
                        unsafe_allow_html=True,
                    )
                    # tombol transparan nutupin seluruh kartu -> kartu utuh bisa diklik
                    st.button(f"Pilih {title}", key=f"dhmodal_pick_{key}",
                              on_click=_cb_pick_mode, args=(key,))
        st.markdown(f'<div class="dh-modal-info">✓ {info}</div>', unsafe_allow_html=True)

    if st.session_state.get("dh_flow_error"):
        st.error(st.session_state.dh_flow_error)
    _l, _m, _r = st.columns([1, 2.2, 1])
    with _m:
        st.button("Lanjut ke Verifikasi & Buka Hasil →", key="dhmodal_cta", type="primary",
                  use_container_width=True, on_click=_cb_form_next, args=(mode,))


@st.dialog("Reveal Dirimu", width="large")
def _flow_dialog():
    if st.session_state.pop("dh_flow_exit", False):
        st.session_state.dr_page = "reveal"
        st.rerun()  # rerun penuh = dialog nutup, lanjut ke halaman Reveal
    step = current_step()
    if step == STEP_VERIFY:
        modal_steps.render_verify()
    elif step == STEP_PAY:
        modal_steps.render_pay()
    elif step == STEP_LOADING:
        modal_steps.render_loading()
    elif step == STEP_RESULT:
        modal_steps.render_result()
    else:
        _render_form()


def open_reveal_modal():
    """Dipanggil dari tombol/link Reveal mana pun: buka modal dari langkah awal."""
    set_step(STEP_FORM)
    st.session_state.dh_flow_error = None
    _flow_dialog()

