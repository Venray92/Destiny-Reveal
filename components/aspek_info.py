"""Tombol info "!" + popup penjelas isi aspek A-F (Solo/Multi) dan A-M (Blueprint Mendalam).
Dipakai di samping judul tiap layar yang menyebut A-F / A-M. CSS: assets/css/parts/15_*.css (.st-key-dhai_*)."""

import html

import streamlit as st

AF = [
    ("A", "Aspek Utama", "Siapa kamu sebenarnya: esensi jiwa, gaya hidup, dan watak dasar dari sistem ini."),
    ("B", "Karier & Keuangan", "Arah karier yang cocok, cara kamu mengelola uang, dan peluang rezekimu."),
    ("C", "Asmara & Hubungan", "Pola kamu dalam cinta, tipe pasangan yang selaras, dan jebakan hubungan."),
    ("D", "Kekuatan Karakter", "Kekuatan utama yang perlu dijaga dan dipakai maksimal."),
    ("E", "Shadow Work", "Sisi bayangan: kebiasaan yang diam-diam menghambat dan cara menyembuhkannya."),
    ("F", "Nasihat Strategis", "Langkah praktis yang bisa langsung kamu jalankan mulai hari ini."),
]
AM = AF[:5] + [("F", "Nasihat Strategis", AF[5][2])] + [
    ("G", "Ringkasan Mendalam", "Rangkuman inti hasil analisis dalam satu gambaran utuh."),
    ("H", "Karier (Deep)", "Peta karier detail: peran, lingkungan kerja, dan strategi naik level."),
    ("I", "Asmara (Deep)", "Dinamika cinta lebih dalam: kebutuhan emosional dan cara membangun hubungan sehat."),
    ("J", "Rezeki (Deep)", "Pola rezeki, kebiasaan finansial, dan siklus panen."),
    ("K", "Emosi & Pemicu", "Apa yang memicu reaksimu dan cara meredakannya."),
    ("L", "Blindspot", "Titik buta yang sering tidak kamu sadari."),
    ("M", "Latihan Harian", "Kebiasaan kecil terukur untuk mengubah pola."),
]


def aspek_info(key, kind="AF"):
    """Render tombol bulat "!" (popover). key unik per layar."""
    rows = AF if kind == "AF" else AM
    judul = "Isi 6 Aspek (A-F)" if kind == "AF" else "Isi 13 Aspek (A-M)"
    with st.container(key=f"dhai_{key}"):
        with st.popover("!"):
            st.markdown(
                f'<div class="dh-ai-head">{judul}</div><div class="dh-ai-list">' + "".join(
                    f'<div><i>{k}</i><span><b>{html.escape(n)}</b>{html.escape(d)}</span></div>' for k, n, d in rows)
                + '</div>', unsafe_allow_html=True)


def heading_with_info(html_heading, key, kind="AF"):
    """Judul + tombol "!" tepat di kanan teks judul (tanpa merusak layout sekitarnya)."""
    try:
        box = st.container(key=f"dhaih_{key}", horizontal=True, vertical_alignment="center", gap="small")
    except TypeError:  # Streamlit lama tanpa container horizontal
        box = st.container(key=f"dhaih_{key}")
    with box:
        st.markdown(html_heading, unsafe_allow_html=True)
        aspek_info(key, kind)
