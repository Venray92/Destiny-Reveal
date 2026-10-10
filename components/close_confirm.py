"""
Konfirmasi tutup untuk semua modal hasil akhir (Reveal Dirimu, Solo Reveal, Soul Match, Tarot, Ramalan Harian).
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


def layer(key, main_fn, on_go=None, on_stay=None, icon="❔", title="Yakin?", text="", stay="Batal", go="Ya, Lanjut",
          go_args=(), tip=None, leave=None, stay_args=()):
    """Konfirmasi sebagai LAYER di atas modal utama (modal utama tetap tampil, buram di belakang).
    main_fn() = render layar utama. on_go / on_stay = callback tombol (jalan sebelum rerun).
    leave != None -> tombol 'go' menutup beneran: flag dibuang, leave() dipanggil, rerun penuh (dialog nutup)."""
    e = html.escape
    with st.container(key=f"dhcc_bg_{key}"):
        main_fn()
    with st.container(key=f"dhcc_layer_{key}"):
        with st.container(key=f"dhcc_card_{key}"):
            st.markdown(
                '<div class="dh-nodismiss"></div>'
                f'<div class="dh-cc dh-cc-lay"><div class="dh-cc-orb"><i></i><span>{icon}</span></div>'
                f'<div class="dh-cc-t">{e(title)}</div><div class="dh-cc-s">{text}</div>'
                + (f'<div class="dh-cc-tip">💡 {e(tip)}</div>' if tip else "") + '</div>',
                unsafe_allow_html=True)
            if stay is None:  # mode satu tombol (popup info)
                st.button(go, key=f"dhccl_go_{key}", type="primary", on_click=on_go, args=go_args, use_container_width=True)
                return
            c1, c2 = st.columns(2, gap="small")
            with c1:
                st.button(stay, key=f"dhccl_stay_{key}", on_click=on_stay, args=stay_args, use_container_width=True)
            with c2:
                if leave is not None or on_go is None:
                    if st.button(go, key=f"dhccl_go_{key}", type="primary", use_container_width=True):
                        st.session_state.pop(_flag(key), None)
                        if leave:
                            leave()
                        st.rerun()  # rerun penuh = dialog nutup
                else:
                    st.button(go, key=f"dhccl_go_{key}", type="primary", on_click=on_go, args=go_args, use_container_width=True)


def wrap(key, main_fn, leave=None, icon="🌙", title="Yakin Mau Pergi Sekarang?",
         text="Hasil bacaanmu masih hangat. Kalau ditutup, halaman ini tidak bisa dibuka lagi.",
         tip="Salin atau simpan dulu kalau masih mau dibaca nanti.", stay="✨ Lanjut Baca", go="Ya, Tutup"):
    """Pengganti render(): layar hasil tetap tampil (buram), konfirmasi tutup jadi layer di atasnya."""
    if not asking(key):
        main_fn()
        return
    layer(key, main_fn, on_stay=cb_stay, stay_args=(key,), icon=icon, title=title, text=html.escape(text),
          stay=stay, go=go, tip=tip, leave=leave or (lambda: None))
