"""
Util buat load kartu simbol (assets/cards/...) sebagai data URI base64,
supaya bisa langsung dipasang ke tag <img> lewat st.markdown(unsafe_allow_html=True)
tanpa perlu hosting file kartu secara terpisah.

Dipakai bareng oleh loadingpage.py (kartu blur, versi "teaser") dan
revealpage.py (kartu jelas/full, versi hasil akhir).
"""

import base64
from pathlib import Path

import streamlit as st

ASSETS_ROOT = Path(__file__).resolve().parent.parent / "assets" / "cards"

# Kartu contoh yang dipakai buat 5 sistem yang sudah ada gambarnya.
# Kalau nanti hasil perhitungan asli sudah jalan (bukan dummy lagi), bagian
# yang milih file per-user (misal shio user = "Naga" -> "shio/naga.png")
# tinggal disambungin ke sini, formatnya persis sama.
SYSTEM_CARD_IMAGE = {
    "Zodiak": "zodiak/leo.png",
    "Shio": "shio/naga.png",
    "Weton": "weton/legi.png",
    "Numerologi": "numerologi/8.png",
    "Matrix Destiny": "matrix_destiny/06_the_partners.png",
}


@st.cache_data(show_spinner=False)
def card_image_data_uri(relative_path: str):
    """
    Args:
        relative_path: path relatif dari assets/cards/, contoh "zodiak/leo.png"

    Returns:
        str: data URI base64 siap dipakai di src="...".
        None: kalau filenya belum ada di assets/cards/ — biar UI tetap
        fallback ke placeholder lama (gradient/ikon), bukan error/crash.
    """
    path = ASSETS_ROOT / relative_path
    if not path.is_file():
        return None
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:image/png;base64,{encoded}"


def card_image_for_system(system):
    """Shortcut: system name ("Zodiak", dst) -> data URI, atau None kalau
    sistem itu belum punya gambar kartu (misal MBTI, DISC, dll)."""
    relative_path = SYSTEM_CARD_IMAGE.get(system)
    if not relative_path:
        return None
    return card_image_data_uri(relative_path)
