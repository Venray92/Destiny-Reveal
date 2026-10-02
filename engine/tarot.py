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


def tarik_tarot() -> dict:
    """
    Tarik 1 kartu Arcana Mayor secara acak.

    Returns:
        dict: {"kartu": "fool"} (key pinyin/slug-nya, dipakai buat lookup
        konten & gambar kartu -- sama pola kayak "sign"/"shio"/dll).
    """
    return {"kartu": random.choice(TAROT_MAJOR_ARCANA)}
