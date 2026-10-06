"""Tes penggabungan variabel (components/combo.py) + posisi Bulan (engine/zodiak.py)."""
import json
import re
from datetime import date

import pytest

from components import combo
from components.combo import build_combo

ANGKA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33]
SIGNS = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
         "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
SHIO = ["Tikus", "Kerbau", "Macan", "Kelinci", "Naga", "Ular", "Kuda", "Kambing", "Monyet", "Ayam", "Anjing", "Babi"]
ELEMEN = ["Kayu", "Api", "Tanah", "Logam", "Air"]


def _teks(blocks):
    return " ".join(b["title"] + " " + b["text"] for b in blocks)


def _bersih(blocks):
    t = _teks(blocks)
    assert "—" not in t and "–" not in t and "  " not in t
    assert not re.search(r"\{|\}", t), "placeholder format belum terisi"
    assert not re.search(r"\b(?:yang yang|dan dan)\b", t)
    for b in blocks:
        assert b["title"].strip() and b["text"].strip() and b["text"].rstrip().endswith((".", "!", "?"))


# ── Numerologi ───────────────────────────────────────────────────
def test_numerologi_semua_kombinasi():
    for lp in ANGKA:
        for su in ANGKA:
            raw = {"life_path": lp, "soul_urge": su, "expression": su, "personality": lp, "birthday": 1}
            b = build_combo("Numerologi", raw)
            assert len(b) == 3
            _bersih(b)


def test_numerologi_relasi_dan_bobot():
    sama = build_combo("Numerologi", {"life_path": 4, "soul_urge": 4, "expression": 4, "personality": 4})
    beda = build_combo("Numerologi", {"life_path": 4, "soul_urge": 7, "expression": 1, "personality": 3})
    master = build_combo("Numerologi", {"life_path": 11, "soul_urge": 7, "expression": 1, "personality": 3})
    assert "sama-sama 4" in sama[0]["text"] and "angka tunggal" in sama[2]["text"]
    assert "Perbedaan" in beda[0]["text"].replace("perbedaan", "Perbedaan")
    assert "angka master" in master[2]["text"] and "angka master" in master[0]["text"]
    assert "angka master" not in beda[2]["text"].split("Karena ada")[0]


def test_numerologi_tanpa_nama_kosong():
    assert build_combo("Numerologi", {"life_path": 5}) == []


def test_kata_hubung_tidak_lowercase_istilah_baku():
    t = build_combo("Numerologi", {"life_path": 1, "soul_urge": 2, "expression": 3, "personality": 4})[0]["text"]
    assert "Soul Urge 2" in t and "soul Urge" not in t


# ── Matrix ───────────────────────────────────────────────────────
def _raw_matrix(c, love, money, main):
    return {"titik_inti": c, "love_money": {"love": love, "money": money, "balance": 1},
            "purpose": {"main_destiny": main}}


def test_matrix_semua_titik():
    for c in range(1, 23):
        for x in range(1, 23):
            b = build_combo("Matrix Destiny", _raw_matrix(c, x, 23 - x if x < 23 else 1, x))
            assert len(b) == 3
        _bersih(b)


def test_matrix_relasi_dinamis():
    sama = build_combo("Matrix Destiny", _raw_matrix(5, 5, 5, 5))
    beda = build_combo("Matrix Destiny", _raw_matrix(5, 1, 2, 3))
    assert "sama dengan inti jiwamu" in sama[0]["text"] and "titik uang ini sama dengan inti jiwamu" in sama[1]["text"]
    assert "titik cinta (1) dan uangmu (2) berbeda" in beda[1]["text"]
    assert "The Teacher (5)" in beda[0]["text"]


def test_matrix_data_kurang_kosong():
    assert build_combo("Matrix Destiny", {"titik_inti": 3}) == []


# ── Shio ─────────────────────────────────────────────────────────
def test_shio_semua_kombinasi():
    for s in SHIO:
        for e in ELEMEN:
            b = build_combo("Shio", {"shio": s, "elemen": e})
            assert len(b) == 2
            _bersih(b)
    yang = build_combo("Shio", {"shio": "Tikus", "elemen": "Air"})[0]
    yin = build_combo("Shio", {"shio": "Kerbau", "elemen": "Air"})[0]
    assert "Yang" in yang["title"] and "Yin" in yin["title"] and yang["text"] != yin["text"]


def test_shio_elemen_tidak_dikenal():
    assert build_combo("Shio", {"shio": "Tikus", "elemen": "Besi"}) == []


# ── Zodiak Matahari + Bulan ──────────────────────────────────────
def test_zodiak_semua_kombinasi_dan_relasi():
    for sun in SIGNS:
        for moon in SIGNS:
            b = build_combo("Zodiak", {"sign": sun, "moon_sign": moon})
            assert len(b) == 2
            _bersih(b)
    assert "tanda yang sama" in build_combo("Zodiak", {"sign": "Leo", "moon_sign": "Leo"})[0]["text"]
    assert "sama-sama berelemen Api" in build_combo("Zodiak", {"sign": "Leo", "moon_sign": "Aries"})[0]["text"]
    assert "saling mendukung" in build_combo("Zodiak", {"sign": "Leo", "moon_sign": "Gemini"})[0]["text"]
    assert "berbeda karakter" in build_combo("Zodiak", {"sign": "Leo", "moon_sign": "Taurus"})[0]["text"]


def test_zodiak_tanpa_bulan_kosong():
    assert build_combo("Zodiak", {"sign": "Leo"}) == []


def test_zodiak_peringatan_dekat_batas():
    b = build_combo("Zodiak", {"sign": "Leo", "moon_sign": "Aries", "moon_near_edge": True})
    assert "jam lahir" in b[1]["text"]


# ── Umum ─────────────────────────────────────────────────────────
def test_sistem_lain_dan_data_rusak_kosong():
    assert build_combo("Weton", {"hari": "Senin"}) == []
    assert build_combo("Numerologi", None) == []
    assert build_combo("Zodiak", {"sign": "Leo", "moon_sign": "XXX"}) == []


def test_file_json_hilang_aman(monkeypatch):
    monkeypatch.setattr(combo, "_data", lambda system: {})
    assert build_combo("Shio", {"shio": "Tikus", "elemen": "Air"}) == []


def test_kata_hubung_berotasi():
    """Tidak semua kombinasi memakai kata hubung yang sama."""
    pakai = set()
    for sun in SIGNS:
        t = build_combo("Zodiak", {"sign": sun, "moon_sign": "Cancer"})[0]["text"]
        pakai |= set(re.findall(r"(Sementara itu|Pada saat yang sama|Selain itu),", t))
    assert len(pakai) >= 2


# ── engine.hitung_bulan ──────────────────────────────────────────
def test_hitung_bulan_tanpa_jam_kosong():
    from engine.zodiak import hitung_bulan
    assert hitung_bulan(date(2000, 1, 1), "") == {}
    assert hitung_bulan(date(2000, 1, 1), None) == {}
    assert hitung_bulan(date(2000, 1, 1), "bukan-jam") == {}


def test_hitung_bulan_swisseph_palsu(monkeypatch):
    """Logika tanda & zona waktu, dengan swisseph palsu (longitudenya bisa diatur)."""
    import sys
    import types
    from engine import human_design  # noqa: F401  (import lazily needed by hitung_bulan)
    from engine.zodiak import hitung_bulan

    fake = types.ModuleType("swisseph")
    fake.MOON, fake.FLG_MOSEPH = 1, 4
    seen = {}
    fake.julday = lambda y, m, d, h: seen.setdefault("h", h) or h
    fake.calc_ut = lambda jd, b, f: ((seen["lon"], 0, 0, 0, 0, 0), f)
    monkeypatch.setitem(sys.modules, "swisseph", fake)

    seen["lon"] = 223.3
    assert hitung_bulan(date(2000, 1, 1), "19:00", "Jakarta") == {"moon_sign": "Scorpio", "moon_near_edge": False}
    assert seen["h"] == 12.0                      # 19:00 WIB -> 12:00 UTC
    seen.clear(); seen["lon"] = 0.4
    r = hitung_bulan(date(2000, 1, 1), "20:00", "Makassar")
    assert r == {"moon_sign": "Aries", "moon_near_edge": True} and seen["h"] == 12.0   # WITA +8
    seen["lon"] = 359.9
    assert hitung_bulan(date(2000, 1, 1), "00:00")["moon_sign"] == "Pisces"


# ── combo 8 sistem tambahan ──
import datetime as _dt

_RAW_BARU = {
    "Weton": lambda: __import__("engine.weton", fromlist=["x"]).hitung_weton(_dt.date(1992, 12, 5)),
    "Zi Wei": lambda: {"bintang": "qisha", "ming_gong": "Zi", "bureau_elemen": "Api", "dipinjam": True},
    "Human Design": lambda: {"tipe": "Projector", "otoritas": "Splenic"},
    "MBTI": lambda: {"tipe": "ENFP", "counts": {"E": 6, "I": 2, "S": 3, "N": 5, "T": 4, "F": 4, "J": 2, "P": 6}},
    "Big Five": lambda: {"levels": {"O": "Tinggi", "C": "Rendah", "E": "Sedang", "A": "Tinggi", "N": "Sedang"},
                         "dominant_trait": "O"},
    "Enneagram": lambda: {"tipe": 1, "counts": {9: 1, 1: 5, 2: 3}, "tipe_tied": None},
    "DISC": lambda: {"tipe": "C", "counts": {"D": 2, "I": 1, "S": 5, "C": 6}},
    "Love Language": lambda: {"primary": "PT", "secondary": "AS"},
}


def test_combo_sistem_baru_semua_terisi():
    for sistem, mk in _RAW_BARU.items():
        blok = build_combo(sistem, mk())
        assert blok, sistem
        for b in blok:
            assert b["title"] and len(b["text"]) > 60, (sistem, b)
            assert "—" not in b["text"] and "–" not in b["text"]


def test_combo_sistem_tanpa_variabel_ganda_kosong():
    for sistem in ("BaZi", "Golongan Darah", "Tarot"):
        assert build_combo(sistem, {"kartu": "fool"}) == []


def test_combo_semua_kombinasi_tidak_error():
    import itertools
    for a, b in itertools.permutations("WA QT RG AS PT".split(), 2):
        assert build_combo("Love Language", {"primary": a, "secondary": b})
    for a, b in itertools.permutations("DISC", 2):
        c = {k: 0 for k in "DISC"}; c[a] = 5; c[b] = 3
        assert build_combo("DISC", {"tipe": a, "counts": c})
    for t in range(1, 10):
        assert build_combo("Enneagram", {"tipe": t, "counts": {t: 4}, "tipe_tied": [t, 1]})
    for tp in ("Generator", "Manifesting Generator", "Manifestor", "Projector", "Reflector"):
        for o in ("Emotional / Solar Plexus", "Sacral", "Splenic", "Ego / Heart", "G-Center / Self-Projected",
                  "Lunar / Environmental", "Mental Projector / Outer Authority"):
            assert build_combo("Human Design", {"tipe": tp, "otoritas": o})
    lv = ["Rendah", "Sedang", "Tinggi"]
    for combo in itertools.product(lv, repeat=5):
        assert len(build_combo("Big Five", {"levels": dict(zip("OCEAN", combo)), "dominant_trait": "N"})) == 6
