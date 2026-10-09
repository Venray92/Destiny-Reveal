from content import decision_calc as D
from engine.tarot import TAROT_DECK
from utils import trait_cards


def test_meta_78_kartu_valid():
    for s in TAROT_DECK:
        p, i = D.polarity(s)
        assert p in ("dukung", "netral", "waspada") and i in (1, 2, 3)


def test_skor_dan_unggul():
    # A: Ace Wands(+3) + Ace Pentacles(+3) = 6 ; B: Tower(-3) + Ten Swords(-3) = -6
    r = D.baca(["fool", "wands_01", "pentacles_01", "tower", "swords_10", "fool", "fool"])
    assert r["skor"] == {"A": 6, "B": -6} and r["unggul"] == "A" and r["jelas"] == "cukup jelas"


def test_seimbang_dan_keduanya_berat():
    r = D.baca(["fool", "wands_01", "swords_10", "wands_01", "swords_10", "fool", "fool"])
    assert r["skor"]["A"] == r["skor"]["B"] and r["unggul"] is None
    r = D.baca(["fool", "tower", "swords_10", "tower", "swords_10", "fool", "fool"])
    assert "berat" in r["verdict"]


def test_posisi_dan_fallback():
    r = D.baca(TAROT_DECK[:7])
    assert [p["judul"] for p in r["pos"]][0] == "Inti Situasi" and len(r["pos"]) == 7
    assert all(p["teks"] for p in r["pos"])


def test_kartu_png():
    b = trait_cards.kartu_keputusan("Terima tawaran", "Bertahan", 4, -2, "A", "Ambil satu langkah kecil minggu ini.")
    assert b[:4] == b"\x89PNG"
