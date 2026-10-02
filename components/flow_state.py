"""
State & helper alur modal Reveal (Mode 1): form -> verify -> pay -> loading -> result.
Semua state disimpan di st.session_state (prefix dh_):
  dh_flow_step     : "form" | "verify" | "pay" | "loading" | "result"
  dh_modal_mode    : mode terpilih ("instan" | "mendalam" | "lengkap")
  dh_modal_data    : {nama, tgl_lahir, jam_lahir, kota_lahir, golongan_darah}
  dh_email / dh_email_sent / dh_email_verified
  dh_ref_code / dh_ref_applied
  dh_pay_method    : "koin" | "gopay" | "qris" | "ovo"
  dh_flow_result   : hasil 5 sistem (dihitung di step loading)
NB: magic link, kode referral, dan pembayaran masih DUMMY (belum ada backend).
"""

import re

import streamlit as st

STEP_FORM, STEP_VERIFY, STEP_PAY, STEP_LOADING, STEP_RESULT = (
    "form", "verify", "pay", "loading", "result",
)

MODE1_PRICE_BASE = 10000      # harga normal Mode 1 (Rp) = 1 Koin
REFERRAL_DISCOUNT = 0.20      # diskon kode referral
REFERRAL_BONUS_COIN = 1

_EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]{2,}$")


def valid_email(value):
    return bool(_EMAIL_RE.match((value or "").strip()))


def rp(amount):
    return "Rp " + f"{int(amount):,}".replace(",", ".")


def current_step():
    return st.session_state.get("dh_flow_step", STEP_FORM)


def set_step(step):
    st.session_state.dh_flow_step = step


def price_now():
    if st.session_state.get("dh_ref_applied"):
        return int(round(MODE1_PRICE_BASE * (1 - REFERRAL_DISCOUNT)))
    return MODE1_PRICE_BASE


_FORM_KEYS = ("dhm_nama", "dhm_tgl", "dhm_jam", "dhm_kota", "dhm_golda")


def reset_for_new_scan():
    """Tombol 'Scan Orang Lain': balik ke form, data orang sebelumnya dibersihin
    (email yang sudah terverifikasi tetap dipakai)."""
    for k in _FORM_KEYS + ("dh_modal_data", "dh_flow_result", "dh_show_summary"):
        st.session_state.pop(k, None)
    set_step(STEP_FORM)
