"""
Daily Free: Skor Energi Hari Ini + Afirmasi Harian (Batch 1). Gratis, wajib login.
Data hitung: content/daily_energy.py (4 sistem). Tanggal lahir diambil dari profil akun.
"""

import html
from datetime import date, datetime

import streamlit as st

from components import auth, form_kit
from components.mini_modals import _head, _title
from components.modal_detail import copy_button
from content import daily_energy as DE
from engine.rotation import format_tanggal, today_wib
from utils.affirmation_card import buat_kartu

_E = html.escape
_ICON = {"Zodiak": "♈", "Shio": "🐲", "Weton": "🗓️", "Numerologi": "🔢"}


def _tgl_lahir():
    p = form_kit.my_data() or {}
    t = p.get("tgl")
    if t is not None and not hasattr(t, "day"):
        try:
            t = datetime.fromisoformat(str(t)).date()
        except ValueError:
            t = None
    return t


def _cb_save_tgl():
    ss = st.session_state
    u = auth.current_user()
    if not ss.get("dhen_tgl"):
        ss.dhen_err = "Isi tanggal lahir dulu ya."
        return
    form_kit.save_profile((u or {}).get("nama", "User").title(), ss.dhen_tgl)
    ss.dhen_err = None


def _need_tgl():
    """True kalau tanggal lahir sudah ada. Kalau belum: tampilkan form kecil & return False."""
    if _tgl_lahir():
        return True
    ss = st.session_state
    st.markdown('<div class="dh-au-sub">Fitur ini dihitung dari tanggal lahirmu. Isi sekali, tersimpan di profil.</div>',
                unsafe_allow_html=True)
    st.date_input("Tanggal Lahir", value=None, min_value=date(1900, 1, 1), max_value=date.today(),
                  format="DD/MM/YYYY", key="dhen_tgl")
    if ss.get("dhen_err"):
        st.error(ss.dhen_err)
    st.button("Simpan & Lihat Hasil →", key="dhen_save", type="primary", use_container_width=True, on_click=_cb_save_tgl)
    return False


def _loaded(key):
    """Loading modal sekali per fitur per hari (per sesi)."""
    ss = st.session_state
    tag = (key, today_wib().isoformat())
    if tag in ss.setdefault("dh_en_seen", set()):
        return True
    ph = st.empty()
    with ph.container():
        form_kit.loading_view("Menyelaraskan energimu...", "Membaca Zodiak, Shio, Weton, dan Numerologi hari ini.", 1.8)
    ph.empty()
    ss.dh_en_seen.add(tag)
    return True


# ═══════════ Skor Energi ═══════════
def _ring(score):
    return (f'<div class="dh-en-ring" style="--p:{score}"><div class="dh-en-ringin"><b>{score}</b><span>/ 100</span></div></div>')


@st.dialog("Skor Energi Hari Ini", width="small")
def energi_dialog():
    if not form_kit.login_gate("energi"):
        return
    _head()
    _title("⚡", "Skor Energi Hari Ini", "Gabungan Zodiak · Shio · Weton · Numerologi")
    if not _need_tgl():
        return
    _loaded("energi")
    r = DE.skor_energi(_tgl_lahir())
    rows = ""
    for s, v in r["komponen"].items():
        rows += (f'<div class="dh-en-row"><div class="dh-en-rh"><span>{_ICON[s]} {s}</span><b>{v["skor"]}</b></div>'
                 f'<div class="dh-en-bar"><i style="width:{v["skor"]}%"></i></div><p>{_E(v["info"])}</p></div>')
    st.markdown(
        f'<div class="dh-en-top">{_ring(r["skor"])}<div><div class="dh-en-tier">{_E(r["tier"])}</div>'
        f'<div class="dh-en-tip">{_E(r["tip"])}</div><div class="dh-en-date">{_E(format_tanggal(r["tanggal"]))}</div></div></div>'
        f'<div class="dh-en-rows">{rows}</div>'
        '<div class="dh-en-note">Skor dihitung dari 4 sistem dengan bobot sama (25% tiap sistem). Ini panduan refleksi, '
        'bukan kepastian.</div>', unsafe_allow_html=True)


# ═══════════ Afirmasi Harian ═══════════
@st.cache_data(show_spinner=False)
def _kartu(nama, tanggal_txt, kalimat, langkah):
    return buat_kartu(nama, tanggal_txt, list(kalimat), langkah)


@st.dialog("Afirmasi Harian", width="small")
def afirmasi_dialog():
    if not form_kit.login_gate("afirmasi"):
        return
    _head()
    _title("🌙", "Afirmasi Harian", "Dirangkai dari 4 sistem untuk harimu")
    if not _need_tgl():
        return
    _loaded("afirmasi")
    a = DE.afirmasi(_tgl_lahir())
    nama = (auth.current_user() or {}).get("nama", "").title()
    tgl_txt = format_tanggal(a["tanggal"])
    img = _kartu(nama, tgl_txt, tuple(a["kalimat"]), a["langkah"])
    st.image(img, use_container_width=True)
    chips = "".join(f'<span><i>{_ICON[k]}</i>{_E(v)}</span>' for k, v in a["sumber"].items())
    st.markdown(f'<div class="dh-en-chips">{chips}</div>', unsafe_allow_html=True)
    teks = "\n".join(a["kalimat"]) + f"\n\nLangkah kecil: {a['langkah']}\n#DestinyReveal"
    copy_button(teks, "📋 Salin Teks Afirmasi", "dhen_copy")


DIALOGS = {"energi": energi_dialog, "afirmasi": afirmasi_dialog}
