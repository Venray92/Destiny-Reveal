"""
Kit bersama (Batch 0): Gunakan Data Saya, gate login fitur harian, simpan profil, layar loading.
Dipakai semua modal fitur. Data profil: dh_user["profil"] + dh_solo_prof (sumber autofill).
"""

import html
import time
from datetime import date

import streamlit as st

from components import auth
from components.dialog_bus import request_with_return, request_open

GENDERS = ["Perempuan", "Laki-laki", "Lainnya / Tidak ingin menyebut"]
GOLDA = ["A", "B", "AB", "O", "Belum tahu"]


def my_data():
    u = auth.current_user()
    return (u or {}).get("profil") or None


def save_profile(nama, tgl, jam=None, kota="", gender=None, golda=""):
    """Simpan data diri akun (dipakai register & edit profil) + sinkron ke autofill."""
    ss = st.session_state
    u = auth.current_user()
    prof = {"nama": nama.strip(), "tgl": tgl, "jam": jam, "kota": (kota or "").strip(),
            "gender": gender, "golda": golda or ""}
    if u:
        u["nama"] = prof["nama"]
        u["profil"] = prof
    ss.dh_solo_prof = {k: prof[k] for k in ("nama", "jam", "kota", "golda", "gender", "tgl")}
    return prof


# ─────────────── Gunakan Data Saya ───────────────
def _cb_fill(prefix, back):
    ss = st.session_state
    p = my_data() or {}
    for f in ("nama", "tgl", "jam", "kota", "gender", "golda"):
        v = p.get(f)
        if f == "golda" and v not in GOLDA:
            v = None
        ss[f"{prefix}_{f}"] = v if v not in ("",) else None
    ss[f"{prefix}_filled"] = True


def data_bar(prefix, back):
    """Baris tombol di atas form data diri. Key widget form harus `{prefix}_nama|tgl|jam|kota|gender|golda`.
    Login + profil ada -> Gunakan Data Saya; login tanpa profil -> info; belum login -> tombol Masuk."""
    u = auth.current_user()
    with st.container(key=f"{prefix}_databar"):
        if not u:
            if st.button("🔑 Masuk untuk isi data otomatis", key=f"{prefix}_bar_login", use_container_width=True):
                request_with_return("auth", back)
        elif my_data():
            st.button("📥 Gunakan Data Saya", key=f"{prefix}_bar_fill", on_click=_cb_fill, args=(prefix, back),
                      use_container_width=True)
            if st.session_state.pop(f"{prefix}_filled", False):
                st.caption("✓ Data akunmu sudah diisikan ke form.")
        else:
            st.caption("Data profil akunmu belum lengkap. Lengkapi lewat menu profil supaya bisa diisi otomatis.")


# ─────────────── gate login (fitur Daily Free) ───────────────
def login_gate(back, title="Masuk Dulu Ya", text="Fitur harian gratis ini butuh akun supaya reward dan streak-mu tersimpan."):
    """True kalau sudah login. Kalau belum: gambar kartu ajakan masuk & return False (caller `return`)."""
    if auth.current_user():
        return True
    st.markdown(
        '<div class="dh-step dh-step-mini"></div>'
        f'<div class="dh-au-ico">🔑</div><div class="dh-au-title">{html.escape(title)}</div>'
        f'<div class="dh-au-sub">{html.escape(text)}</div>', unsafe_allow_html=True)
    if st.button("Masuk / Daftar Gratis →", key=f"dhgate_{back}", type="primary", use_container_width=True):
        request_with_return("auth", back)
    return False


# ─────────────── loading screen ───────────────
def loading_view(title, sub="Menghitung peta takdirmu...", seconds=2.5):
    """Layar loading seragam untuk semua proses screening (blok `seconds` detik)."""
    st.markdown(
        '<div class="dh-step dh-step-loading"></div><div class="dh-nodismiss"></div>'
        '<div class="dh-dl-load"><div class="dh-dl-orb"><i></i><span>✦</span></div>'
        f'<div class="dh-dl-t">{html.escape(title)}</div><div class="dh-dl-s">{html.escape(sub)}</div></div>',
        unsafe_allow_html=True)
    time.sleep(seconds)


# ─────────────── register (langkah setelah email terverifikasi) ───────────────
def _cb_register_save():
    ss = st.session_state
    nama = (ss.get("dhrg_nama") or "").strip()
    if not nama or not ss.get("dhrg_tgl"):
        ss.dh_auth_error = "Nama dan Tanggal Lahir wajib diisi."
        return
    save_profile(nama, ss.dhrg_tgl, ss.get("dhrg_jam"), ss.get("dhrg_kota"), ss.get("dhrg_gender"), ss.get("dhrg_golda"))
    ss.dh_auth_error = None
    ss.dh_auth_step = "email"
    ss.dh_auth_done = True


def render_register():
    ss = st.session_state
    u = auth.current_user()
    st.markdown(
        '<div class="dh-step dh-step-auth"></div>'
        '<div class="dh-au-ico dh-au-green">🪪</div><div class="dh-au-eyebrow">SATU KALI ISI</div>'
        '<div class="dh-au-title">Lengkapi Data Dirimu</div>'
        '<div class="dh-au-sub">Data ini dipakai otomatis di semua fitur (kecuali kuesioner) lewat tombol '
        '&ldquo;Gunakan Data Saya&rdquo;. Bisa diubah kapan saja di profil.</div>', unsafe_allow_html=True)
    st.text_input("Nama Lengkap / Panggilan", value=(u or {}).get("nama", "").title(), key="dhrg_nama")
    c1, c2 = st.columns(2, gap="small")
    with c1:
        st.date_input("Tanggal Lahir", value=None, min_value=date(1900, 1, 1), max_value=date.today(),
                      format="DD/MM/YYYY", key="dhrg_tgl")
    with c2:
        st.time_input("Jam Lahir (Opsional)", value=None, key="dhrg_jam")
    c3, c4 = st.columns(2, gap="small")
    with c3:
        st.text_input("Tempat Lahir (Opsional)", placeholder="Contoh: Jakarta", key="dhrg_kota")
    with c4:
        st.selectbox("Golongan Darah (Opsional)", GOLDA, index=None, placeholder="Pilih", key="dhrg_golda")
    st.selectbox("Jenis Kelamin / Gender (Opsional)", GENDERS, index=None, placeholder="Pilih", key="dhrg_gender")
    st.markdown('<div class="dh-au-notice">Jam &amp; tempat lahir bikin BaZi, Zi Wei, dan Human Design lebih akurat. '
                'Boleh dikosongkan dulu.</div>', unsafe_allow_html=True)
    if ss.get("dh_auth_error"):
        st.error(ss.dh_auth_error)
    st.button("Simpan & Mulai →", key="dhrg_save", type="primary", use_container_width=True, on_click=_cb_register_save)
