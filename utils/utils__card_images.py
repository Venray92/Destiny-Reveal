"""
Util buat load kartu simbol (assets/cards/...) sebagai data URI base64,
supaya bisa langsung dipasang ke tag <img> lewat st.markdown(unsafe_allow_html=True)
tanpa perlu hosting file kartu secara terpisah.

Dipakai bareng oleh loadingpage.py (kartu blur, versi "teaser") dan
revealpage.py (kartu jelas/full, versi hasil akhir).

BUG YANG DIPERBAIKI (26 Sep 2026): versi sebelumnya cuma punya SATU gambar
tetap per KATEGORI sistem (SYSTEM_CARD_IMAGE, misal "Zodiak" -> selalu
"leo.png"), padahal tiap kategori itu punya banyak kemungkinan hasil
(12 zodiak, 12 shio, 5 pasaran weton, 12 angka numerologi, 22 arketipe
matrix destiny). Akibatnya gambar kartu yang muncul SELALU sama nggak
peduli hasil perhitungan aslinya apa (mis. teks bilang "Sagittarius" tapi
kartunya tetap gambar Leo). Sekarang dipilih dari hasil MENTAH (raw_result
dari content/result_builder.compute_raw_result) lewat
`card_relative_path_for_result()`, bukan dari nama kategori doang.
"""

import base64
from pathlib import Path

import streamlit as st

ASSETS_ROOT = Path(__file__).resolve().parent.parent / "assets" / "cards"

# Fallback kalau raw_result belum tersedia (mis. sistem yang belum punya
# engine sama sekali, atau placeholder) — dipakai HANYA sebagai contoh
# visual generik, bukan buat hasil beneran dari 5 sistem yang sudah lengkap.
SYSTEM_CARD_IMAGE_FALLBACK = {
    "Zodiak": "zodiak/leo.png",
    "Shio": "shio/naga.png",
    "Weton": "weton/legi.png",
    "Numerologi": "numerologi/8.png",
    "Matrix Destiny": "matrix_destiny/06_the_partners.png",
    "MBTI": "mbti/intj.png",
    "Big Five": "big_five/openness.png",
    "Enneagram": "enneagram/1.png",
    "DISC": "disc/d.png",
    "Love Language": "love_language/words_of_affirmation.png",
}


def card_relative_path_for_result(system: str, raw_result: dict | None):
    """
    Tentukan path relatif gambar kartu (dari assets/cards/) berdasarkan
    HASIL PERHITUNGAN ASLI (raw_result, persis balikan
    content.result_builder.compute_raw_result), bukan cuma nama kategori
    sistemnya — supaya kartu yang tampil selalu cocok sama hasil beneran.

    Args:
        system: nama kategori ("Zodiak", "Shio", "Weton", "Numerologi",
            "Matrix Destiny").
        raw_result: dict mentah dari compute_raw_result(system, ...), atau
            None/placeholder kalau belum ada hasil (misal masih nunggu data
            atau sistem itu belum punya engine).

    Returns:
        str path relatif (contoh "zodiak/sagittarius.png"), atau None kalau
        nggak bisa ditentukan (raw_result kosong/placeholder/nggak
        dikenal) — caller lalu boleh fallback ke SYSTEM_CARD_IMAGE_FALLBACK.
    """
    if not raw_result or raw_result.get("placeholder"):
        return None

    if system == "Zodiak":
        sign = raw_result.get("sign")
        return f"zodiak/{sign.lower()}.png" if sign else None

    if system == "Shio":
        shio = raw_result.get("shio")
        return f"shio/{shio.lower()}.png" if shio else None

    if system == "Weton":
        pasaran = raw_result.get("pasaran")
        return f"weton/{pasaran.lower()}.png" if pasaran else None

    if system == "Numerologi":
        life_path = raw_result.get("life_path")
        return f"numerologi/{life_path}.png" if life_path else None

    if system == "Matrix Destiny":
        titik_inti = raw_result.get("titik_inti")
        nama_arketipe = raw_result.get("nama_arketipe")
        if not titik_inti or not nama_arketipe:
            return None
        slug = nama_arketipe.lower().replace(" ", "_")
        return f"matrix_destiny/{titik_inti:02d}_{slug}.png"

    # ── 5 sistem kuesioner Mode Mendalam ──
    if system == "MBTI":
        tipe = raw_result.get("tipe")
        return f"mbti/{tipe.lower()}.png" if tipe else None

    if system == "Big Five":
        slug = raw_result.get("dominant_slug")
        return f"big_five/{slug}.png" if slug else None

    if system == "Enneagram":
        tipe = raw_result.get("tipe")
        return f"enneagram/{tipe}.png" if tipe else None

    if system == "DISC":
        tipe = raw_result.get("tipe")
        return f"disc/{tipe.lower()}.png" if tipe else None

    if system == "Love Language":
        slug = raw_result.get("primary_slug")
        return f"love_language/{slug}.png" if slug else None

    # ── 3 sistem baru (BaZi, Golongan Darah, Tarot) — Ronde 4 ──
    if system == "BaZi":
        day_master = raw_result.get("day_master")
        return f"bazi/{day_master}.png" if day_master else None

    if system == "Zi Wei":
        bintang = raw_result.get("bintang")
        return f"ziwei/{bintang}.png" if bintang else None

    if system == "Human Design":
        tipe_slug = raw_result.get("tipe_slug")
        return f"human_design/{tipe_slug}.png" if tipe_slug else None

    if system == "Golongan Darah":
        golongan = raw_result.get("golongan")
        return f"golongan_darah/{golongan.lower()}.png" if golongan else None

    if system == "Tarot":
        kartu = raw_result.get("kartu")
        # Nama file pakai prefix angka 2-digit (00_fool.png dst) — slug di
        # raw_result cuma "fool" tanpa prefix, jadi cari filenya lewat
        # index di TAROT_MAJOR_ARCANA (bukan hardcode urutan angka ganda).
        from engine.tarot import TAROT_MAJOR_ARCANA
        if kartu not in TAROT_MAJOR_ARCANA:
            return None
        idx = TAROT_MAJOR_ARCANA.index(kartu)
        return f"tarot/{idx:02d}_{kartu}.png"

    return None


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


def _resolve_relative_path(system, raw_result):
    relative_path = card_relative_path_for_result(system, raw_result)
    if relative_path:
        return relative_path
    return SYSTEM_CARD_IMAGE_FALLBACK.get(system)


def card_image_for_system(system, raw_result=None):
    """Shortcut: (system, raw_result hasil beneran) -> data URI gambar
    kartu yang SESUAI hasil itu. Kalau raw_result belum ada/placeholder,
    fallback ke satu gambar contoh generik per kategori (lama), dan kalau
    sistemnya emang belum punya gambar kartu sama sekali (misal MBTI, DISC,
    dll) -> None."""
    relative_path = _resolve_relative_path(system, raw_result)
    if not relative_path:
        return None
    return card_image_data_uri(relative_path)


@st.cache_data(show_spinner=False)
def card_image_bytes(relative_path: str):
    """Sama kayak card_image_data_uri, tapi return raw bytes (bukan data URI
    base64) — dipakai buat tombol download (st.download_button butuh bytes
    mentah, bukan string data URI)."""
    path = ASSETS_ROOT / relative_path
    if not path.is_file():
        return None
    return path.read_bytes()


def card_image_bytes_for_system(system, raw_result=None):
    """Shortcut: (system, raw_result hasil beneran) -> raw bytes gambar
    kartu yang SESUAI hasil itu, atau None kalau belum ada gambarnya."""
    relative_path = _resolve_relative_path(system, raw_result)
    if not relative_path:
        return None
    return card_image_bytes(relative_path)


def card_filename_for_system(system, raw_result=None):
    """Nama file yang enak dibaca buat tombol download, contoh:
    'kartu-zodiak-sagittarius.png' (sesuai hasil beneran, bukan contoh
    generik lagi)."""
    relative_path = _resolve_relative_path(system, raw_result)
    if not relative_path:
        return f"kartu-{system.lower().replace(' ', '-')}.png"
    stem = relative_path.rsplit("/", 1)[-1]
    folder = relative_path.split("/", 1)[0]
    return f"kartu-{folder}-{stem}"
