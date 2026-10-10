"""Lanjut kuesioner: progres fitur disimpan saat modal ditutup, dibuang kalau user buka fitur LAIN."""

import streamlit as st

_RESETS = {}  # fitur -> fungsi reset (hanya fitur ber-kuesioner)
_SKIP = {"pricing", "pricing_koin", "pricing_fitur", "pricing_vip", "pricing_ref", "about", "tutorial", "blog", "faq",
         "contact", "privacy", "terms", "sysinfo", "gohome", "streak"}  # bukan fitur: tidak memutus progres


def register(feat, reset_fn):
    _RESETS[feat] = reset_fn


def _norm(key):
    if key.startswith("tarot_spread"):
        return "tarot_spread"
    if key.startswith("compat"):
        return "compat"
    return key


def enter(key):
    """Dipanggil tiap fitur dibuka. Fitur sebelumnya (beda) di-reset progresnya."""
    if key in _SKIP:
        return
    feat = _norm(key)
    ss = st.session_state
    prev = ss.get("dh_resume_feat")
    if prev and prev != feat and prev in _RESETS:
        _RESETS[prev]()
    ss.dh_resume_feat = feat


def tracked(key, fn):
    def _run(*a, **k):
        enter(key)
        return fn(*a, **k)
    return _run
