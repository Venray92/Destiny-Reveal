"""
Util buat load kartu simbol (assets/cards/...) sebagai data URI base64,
supaya bisa langsung dipasang ke tag <img> lewat st.markdown(unsafe_allow_html=True).

Dipakai bareng oleh loadingpage.py (kartu blur, versi "teaser") dan
revealpage.py (kartu jelas/full, versi hasil akhir).

Bug-fix: lihat docs/bugs-fixed.md.
"""


import base64
from pathlib import Path

import streamlit as st

from utils.watermark import watermarked_data_uri, watermarked_png

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
    "BaZi": "bazi/jia.png",
    "Zi Wei": "ziwei/ziwei.png",
    "Human Design": "human_design/generator.png",
    "Golongan Darah": "golongan_darah/o.png",
    "Tarot": "tarot/major/00_fool.jpg",
}


_MINOR_NAMA = ["ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
               "page", "knight", "queen", "king"]
_MINOR_FOLDER = {"cups": "cups", "pentacles": "pentacles", "swords": "sword", "wands": "wands"}


def tarot_image_rel(slug):
    """slug kartu (fool / hanged_man / cups_03 / swords_page) -> path relatif gambar, atau None.
    Major: tarot/major/NN_slug.jpg; Minor: tarot/<suit>/NN_<nama>_<suit>.jpg (NN 01-14; folder 'sword' tunggal)."""
    if not slug:
        return None
    from engine.tarot import TAROT_MAJOR_ARCANA
    if slug in TAROT_MAJOR_ARCANA:
        rel = f"tarot/major/{TAROT_MAJOR_ARCANA.index(slug):02d}_{slug}.jpg"
    else:
        suit, _, rank = slug.partition("_")
        if suit not in _MINOR_FOLDER:
            return None
        n = int(rank) if rank.isdigit() else 11 + ["page", "knight", "queen", "king"].index(rank) if rank in ("page", "knight", "queen", "king") else 0
        if not 1 <= n <= 14:
            return None
        f = _MINOR_FOLDER[suit]
        rel = f"tarot/{f}/{n:02d}_{_MINOR_NAMA[n - 1]}_{f}.jpg"
    f = ASSETS_ROOT / rel
    return rel if f.is_file() and f.stat().st_size > 1024 else None  # file kosong/rusak dianggap tidak ada


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

    # ── 5 sistem non-kuesioner Mode Lengkap (Kelompok B/E/F) ──
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
        golda = raw_result.get("golongan_darah")
        return f"golongan_darah/{golda.lower()}.png" if golda else None

    if system == "Tarot":
        return tarot_image_rel((raw_result or {}).get("kartu"))

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
    return watermarked_data_uri(path)


@st.cache_data(show_spinner=False)
def card_image_data_uri_small(relative_path: str, width: int = 520):
    """Versi ringan buat tampil di modal: WebP lebar `width`, watermark tetap ada.
    Aslinya ±2,3 MB base64 per kartu (bikin render telat/gagal di koneksi/server lemot)."""
    path = ASSETS_ROOT / relative_path
    if not path.is_file():
        return None
    import io

    from PIL import Image

    from utils.watermark import add_watermark
    try:
        with Image.open(path) as im:
            im = add_watermark(im)
        im = im.resize((width, round(width * im.height / im.width)), Image.LANCZOS)
        buf = io.BytesIO()
        im.save(buf, format="WEBP", quality=86, method=6)
        return "data:image/webp;base64," + base64.b64encode(buf.getvalue()).decode("ascii")
    except Exception:
        return card_image_data_uri(relative_path)  # fallback ke versi penuh


def _resolve_relative_path(system, raw_result):
    relative_path = card_relative_path_for_result(system, raw_result)
    if relative_path:
        return relative_path
    # Tarot minor (cups_03 dst) belum punya gambar: jangan pinjam gambar The Fool
    if system == "Tarot" and (raw_result or {}).get("kartu"):
        return None
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
    return watermarked_png(str(path))


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
