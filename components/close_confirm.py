"""
Konfirmasi tutup untuk semua modal hasil akhir (Reveal Dirimu, Solo Reveal, Cek Kecocokan, Tarot, Ramalan Harian).
Dipakai dua jalur:
  - tombol "Selesai & Tutup"  -> on_click=cb_ask(key)  -> layar konfirmasi tampil di dalam dialog yang sama
  - X di pojok dialog         -> on_dismiss=dismiss(...) -> dialog dibuka ulang (navbar) dengan layar konfirmasi
State: dh_cc_<key> (True = lagi nanya) | dh_cc_reopen (key dialog yang harus dibuka ulang setelah X).
"""

import html

import streamlit as st


def _flag(key):
    return f"dh_cc_{key}"


def asking(key):
    return bool(st.session_state.get(_flag(key)))


def cb_ask(key):
    st.session_state[_flag(key)] = True


def cb_stay(key):
    st.session_state.pop(_flag(key), None)


def dismiss(key, at_result, leave=None, reopen=None):
    """Isi on_dismiss dialog (X). at_result = lagi di layar hasil.
    X di layar konfirmasi = keluar beneran (leave dipanggil). X di layar hasil = tanya dulu."""
    ss = st.session_state
    if ss.get(_flag(key)):
        ss.pop(_flag(key), None)
        if leave:
            leave()
        return
    if at_result:
        ss[_flag(key)] = True
        if reopen:
            reopen()
        else:
            ss.dh_cc_reopen = key


def render(key, leave, icon="🌙", title="Yakin Mau Pergi Sekarang?",
           text="Hasil bacaanmu masih hangat. Kalau ditutup, halaman ini tidak bisa dibuka lagi.",
           tip="Salin atau simpan dulu kalau masih mau dibaca nanti.",
           stay="✨ Lanjut Baca", go="Ya, Tutup"):
    """Layar konfirmasi. leave() dipanggil kalau user pilih keluar, lalu rerun penuh (dialog nutup)."""
    e = html.escape
    st.markdown(
        '<div class="dh-step dh-step-fm"></div><div class="dh-nodismiss"></div>'
        f'<div class="dh-cc"><div class="dh-cc-orb"><i></i><span>{icon}</span></div>'
        f'<div class="dh-cc-t">{e(title)}</div><div class="dh-cc-s">{e(text)}</div>'
        + (f'<div class="dh-cc-tip">💡 {e(tip)}</div>' if tip else "") + '</div>',
        unsafe_allow_html=True)
    with st.container(key=f"dhcc_btns_{key}"):
        c1, c2 = st.columns(2, gap="small")
        with c1:
            st.button(stay, key=f"dhcc_stay_{key}", type="primary", on_click=cb_stay, args=(key,),
                      use_container_width=True)
        with c2:
            if st.button(go, key=f"dhcc_go_{key}", use_container_width=True):
                st.session_state.pop(_flag(key), None)
                if leave:
                    leave()
                st.rerun()  # rerun penuh = dialog nutup
