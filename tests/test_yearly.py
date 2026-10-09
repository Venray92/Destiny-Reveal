from datetime import date

from content import yearly_calc as Y
from utils import trait_cards


def test_shio_tahun():
    assert Y.shio_tahun(2026) == 6 and Y.shio_tahun(2027) == 7 and Y.shio_tahun(2020) == 0  # Kuda, Kambing, Tikus


def test_relasi_sesuai_tradisi():
    assert Y.baca(date(1990, 6, 1), 2026)["rel"] == "sama"      # Kuda x Kuda
    assert Y.baca(date(1990, 6, 1), 2027)["rel"] == "liu_he"    # Kuda x Kambing
    assert Y.baca(date(1995, 3, 14), 2027)["rel"] == "san_he"   # Babi x Kambing
    assert Y.baca(date(1990, 6, 1), 2020)["rel"] == "chong"     # Kuda x Tikus


def test_personal_year():
    assert Y.baca(date(1995, 3, 14), 2027)["py"] == 1  # 5 + 3 + 2


def test_kurva_12_bulan_dan_rentang():
    r = Y.baca(date(1995, 3, 14), 2027)
    assert len(r["kurva"]) == 12 and all(5 <= x["skor"] <= 98 for x in r["kurva"])
    assert len(r["terbaik"]) == 2 and len(r["terjaga"]) == 2
    assert max(x["skor"] for x in r["kurva"]) >= max(x["skor"] for x in r["terjaga"])
    assert r["skor"] == round(sum(x["skor"] for x in r["kurva"]) / 12)


def test_lahir_sebelum_imlek_dan_di_luar_tabel():
    for d in (date(1995, 1, 20), date(2023, 5, 5), date(1930, 7, 1)):
        assert Y.baca(d, 2027)["rel"] in Y.REL_LABEL


def test_kartu_png():
    r = Y.baca(date(1995, 3, 14), 2027)
    b = trait_cards.kartu_tahunan("Tes", 2027, r["shio_kamu"], r["shio_tahun"], r["rel_label"], r["skor"], r["tier"], ["Feb", "Jul"],
                                  ["Mei", "Agu"], [x["skor"] for x in r["kurva"]])
    assert b[:4] == b"\x89PNG"
