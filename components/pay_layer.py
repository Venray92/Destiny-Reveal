"""Layer konfirmasi pembayaran Stardust (gaya Multi-System Blueprint): tampil di atas layar awal yang di-blur.
Dipakai Tarot Spread & Decision Reveal. key harus diawali 'mxpay' supaya CSS 21_revisi_mx_pay_layer.css ikut berlaku."""

import html

import streamlit as st

from components import auth
from components import close_confirm as cc
from components.dialog_bus import request_with_return
from content import pricing as P

_E = html.escape


def render(key, bg_fn, *, icon, brand, rows, price, on_pay, on_back, return_to, pay_label="Bayar & Buka Hasil"):
    """rows = [(label, nilai)] ditampilkan di atas Harga/Saldo/Sisa. on_pay/on_back = callback tombol."""
    u = auth.current_user()
    with cc.bg(key):
        bg_fn()
    with st.container(key=f"dhcc_layer_{key}"):
        with st.container(key=f"dhcc_card_{key}"):
            st.markdown(
                '<div class="dh-nodismiss"></div>'
                f'<div class="dh-bp-head"><span class="dh-bp-ico">{icon}</span><div><div class="dh-bp-h">{_E(brand)}</div>'
                '<div class="dh-bp-hs">Konfirmasi pembayaran</div></div></div>', unsafe_allow_html=True)
            saldo = int((u or {}).get("koin", 0))
            sisa = saldo - price
            body = "".join(f'<div class="dh-bp-row"><span>{_E(a)}:</span><b>{_E(b)}</b></div>' for a, b in rows)
            st.markdown(
                '<div class="dh-bp-price">' + body + '<div class="dh-bp-line"></div>'
                f'<div class="dh-bp-row"><span>Harga:</span><b class="big">{P.coin(price)}</b></div>'
                f'<div class="dh-bp-row"><span>Saldo Kamu:</span><b>{P.coin(saldo)}</b></div>'
                f'<div class="dh-bp-row"><span>Sisa Setelah Transaksi:</span><b class="{"ok" if sisa >= 0 else "bad"}">{P.coin(sisa)}</b></div></div>',
                unsafe_allow_html=True)
            with st.container(key=f"dhbp_cta_{key}"):
                if sisa < 0:
                    st.markdown(f'<div class="dh-bp-warn">Saldo belum cukup, kurang {P.coin(-sisa)}.</div>', unsafe_allow_html=True)
                    if st.button("Top-up Saldo →", key=f"{key}_topup", type="primary", use_container_width=True):
                        request_with_return("pricing_keep", return_to, dh_pr_tab="koin")
                else:
                    st.button(f"{pay_label} {price:,}✨".replace(",", "."), key=f"{key}_pay", type="primary",
                              on_click=on_pay, use_container_width=True)
            st.button("← Kembali", key=f"{key}_back", on_click=on_back, type="tertiary")
