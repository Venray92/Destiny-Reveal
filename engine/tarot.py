"""
Engine Tarot — sistem "acak" (Kelompok F), gak butuh data lahir sama
sekali. Satu kartu Arcana Mayor ditarik random tiap kali user minta hasil.

Hasil tarikan disimpan di session_state (loading_data/loading_results,
sama kayak sistem lain) begitu ditarik, SUPAYA gak berubah-ubah tiap kali
halaman di-rerun (Streamlit rerun banyak kali per interaksi) -- kartu
harus tetap sama selama satu sesi reveal yang sama.
"""

import random

# Urutan sama persis kayak urutan file gambar (00_fool.png s/d 21_world.png)
# dan urutan prompt yang sudah dikasih ke Stev.
TAROT_MAJOR_ARCANA = [
    "fool", "magician", "high_priestess", "empress", "emperor",
    "hierophant", "lovers", "chariot", "strength", "hermit",
    "wheel_of_fortune", "justice", "hanged_man", "death", "temperance",
    "devil", "tower", "star", "moon", "sun", "judgement", "world",
]


# Minor Arcana: slug = key di JSON tarot (cups_01..cups_10, cups_page/knight/queen/king, dst)
TAROT_SUITS = ["cups", "pentacles", "swords", "wands"]
_RANK = [f"{n:02d}" for n in range(1, 11)] + ["page", "knight", "queen", "king"]
TAROT_MINOR_ARCANA = [f"{s}_{r}" for s in TAROT_SUITS for r in _RANK]
TAROT_DECK = TAROT_MAJOR_ARCANA + TAROT_MINOR_ARCANA  # 78 kartu


def tarik_tarot() -> dict:
    """Tarik 1 kartu acak dari 78 kartu. Return {"kartu": slug} (major: "fool"; minor: "cups_03")."""
    return {"kartu": random.choice(TAROT_DECK)}


def kartu_periodik(kind, now=None, user_key="") -> str:
    """Kartu deterministik per periode (kind: daily/weekly/monthly), dari 78 kartu.
    Periode = tanggal WIB / Senin minggu itu / bulan; user_key opsional supaya tiap orang beda."""
    import hashlib

    from engine.rotation import today_wib, week_start
    d = today_wib(now)
    per = {"daily": d.isoformat(), "weekly": week_start(d).isoformat(), "monthly": f"{d.year}-{d.month:02d}"}[kind]
    h = hashlib.sha256(f"{kind}|{per}|{user_key}".encode()).digest()
    return TAROT_DECK[int.from_bytes(h[:4], "big") % len(TAROT_DECK)]


def kartu_harian(tgl_lahir=None, user_key="", now=None) -> str:
    """Kartu harian deterministik dari 78 kartu (stabil sepanjang hari WIB).
    Ada tgl_lahir: seed = tanggal lahir + tanggal hari ini (personal, sama di device mana pun).
    Tanpa tgl_lahir: seed = tanggal hari ini + user_key (email / id sesi)."""
    import hashlib

    from engine.rotation import today_wib
    d = today_wib(now)
    if tgl_lahir is not None and hasattr(tgl_lahir, "day"):
        basis = f"lahir|{tgl_lahir.isoformat()}|{d.isoformat()}"
    else:
        basis = f"user|{user_key}|{d.isoformat()}"
    h = hashlib.sha256(f"tarot|{basis}".encode()).digest()
    return TAROT_DECK[int.from_bytes(h[:4], "big") % len(TAROT_DECK)]
