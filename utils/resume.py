"""Lanjut kuesioner: progres fitur disimpan saat modal ditutup. Dibuang hanya kalau user
benar-benar men-scan fitur lain (hasil dibuat / koin terpotong) atau refresh browser (session baru)."""

import streamlit as st

_RESETS = {}  # fitur -> fungsi reset (hanya fitur ber-kuesioner)
_SKIP = {"pricing", "pricing_koin", "pricing_fitur", "pricing_vip", "pricing_ref", "about", "tutorial", "blog", "faq",
         "contact", "privacy", "terms", "sysinfo", "gohome", "streak"}


def register(feat, reset_fn):
    _RESETS[feat] = reset_fn


def _norm(key):
    if key.startswith("tarot_spread"):
        return "tarot_spread"
    if key.startswith("compat"):
        return "compat"
    return key


def enter(key):
    """Dipanggil tiap fitur dibuka: cuma mencatat fitur aktif (TIDAK mereset progres fitur lain)."""
    if key not in _SKIP:
        st.session_state.dh_resume_feat = _norm(key)


def scanned(key):
    """Dipanggil saat sebuah fitur selesai men-scan (koin terpotong). Progres kuesioner fitur LAIN di-reset."""
    feat = _norm(key)
    mine = _RESETS.get(feat)
    for f, fn in list(_RESETS.items()):
        if f != feat and fn is not mine:  # career & strength berbagi state -> jangan hapus hasil sendiri
            fn()
    st.session_state.dh_resume_feat = feat


def tracked(key, fn):
    def _run(*a, **k):
        enter(key)
        return fn(*a, **k)
    return _run
