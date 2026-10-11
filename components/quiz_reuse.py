"""Layar tawaran pakai jawaban kuesioner lama (pola sama dengan Career DNA / Strength). Dipakai Deep Blueprint & Multi-System."""

import html

import streamlit as st

_E = html.escape


def screen(prefix, offer, on_use, on_redo, on_back):
    """offer dari utils.quiz_store.offer(). Header (judul modal) digambar pemanggil."""
    nm = "Deep" if offer["mode"] == "lengkap" else "Cepat"
    cov, tot = offer["cov"], offer["systems"]
    n = sum(len(e["ids"]) for e in cov.values())
    if offer["full"]:
        ttl, sub = f"✓ Kuesioner {nm} · {n} soal", "Tersimpan di akunmu, tanpa isi lagi"
        desc = "Kamu pernah mengisinya dengan data yang sama. Pakai lagi, atau isi baru kalau ingin hasil yang lebih akurat."
        go = "Pakai Jawaban Ini →"
    else:
        ttl, sub = f"✓ {len(cov)} dari {len(tot)} sistem sudah pernah diisi", f"Kuesioner {nm} · {n} soal terpakai"
        desc = "Sisanya tinggal kamu isi sekarang. Atau isi semuanya dari awal."
        go = "Pakai & Lengkapi Sisanya →"
    rows = "".join(f'<li><b style="display:inline;font-size:12px;color:#3A2A20">{_E(s)}</b> · {_E(e["feat"])} · {_E(e["waktu"])}</li>' for s, e in cov.items())
    st.markdown(f'<div class="dh-bp-mcard"><b>{_E(ttl)}</b><em>{_E(sub)}</em><p>{_E(desc)}</p>'
                f'<ul style="margin:6px 0 0 16px;padding:0;font-size:12px;color:#8B7B6B;line-height:1.6">{rows}</ul></div>',
                unsafe_allow_html=True)
    with st.container(key="dhbp_cta"):
        st.button(go, key=f"{prefix}_reuse", type="primary", on_click=on_use, use_container_width=True)
    st.button("Isi Baru (ulangi kuesioner)", key=f"{prefix}_redo", on_click=on_redo, use_container_width=True)
    st.button("← Kembali", key=f"{prefix}_reuse_back", on_click=on_back, type="tertiary")
