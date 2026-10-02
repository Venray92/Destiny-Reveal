"""
Test buat engine/matrix_destiny.py (metode resmi Ladini).

Nilai pembanding buat 5 Desember 1992 divalidasi manual & cocok dengan
screenshot hasil matrix-destiny.com yang dikasih Stev (titik_inti = 13,
"The Transformation" -- BEDA dari hasil shortcut versi lama yang salah,
yaitu 11 "The Brave"). Lihat memory project
/areas/matrix-destiny-formula.md untuk detail rumus & sumber validasinya.
"""

from datetime import date

from engine.matrix_destiny import hitung_matrix_destiny


def test_titik_inti_5_desember_1992():
    hasil = hitung_matrix_destiny(date(1992, 12, 5))
    assert hasil["titik_inti"] == 13
    assert hasil["nama_arketipe"] == "The Transformation"


def test_personal_square_5_desember_1992():
    hasil = hitung_matrix_destiny(date(1992, 12, 5))
    assert hasil["personal_square"] == {"a": 5, "b": 12, "c": 21, "d": 11, "e": 13}


def test_ancestral_square_5_desember_1992():
    hasil = hitung_matrix_destiny(date(1992, 12, 5))
    assert hasil["ancestral_square"] == {"f": 17, "g": 6, "h": 16, "i": 5}


def test_love_money_balance_5_desember_1992():
    hasil = hitung_matrix_destiny(date(1992, 12, 5))
    assert hasil["love_money"] == {"love": 6, "money": 7, "balance": 13}


def test_purpose_5_desember_1992():
    hasil = hitung_matrix_destiny(date(1992, 12, 5))
    assert hasil["purpose"] == {
        "sky": 5, "earth": 8, "personal": 13,
        "male_line": 22, "female_line": 22, "social": 8,
        "main_destiny": 21,
    }


def test_chakra_5_desember_1992():
    hasil = hitung_matrix_destiny(date(1992, 12, 5))
    assert hasil["chakra"] == {
        "sahasrara": {"physics": 5, "energy": 12, "emotions": 17},
        "ajna": {"physics": 5, "energy": 19, "emotions": 6},
        "vishuddha": {"physics": 18, "energy": 7, "emotions": 7},
        "anahata": {"physics": 4, "energy": 20, "emotions": 6},
        "manipura": {"physics": 13, "energy": 13, "emotions": 8},
        "svadhisthana": {"physics": 7, "energy": 6, "emotions": 13},
        "muladhara": {"physics": 21, "energy": 11, "emotions": 5},
    }


def test_angka_22_tidak_direduksi_lagi():
    # Aturan dasar: 22 TIDAK disederhanakan lebih lanjut (tetap 22).
    hasil = hitung_matrix_destiny(date(1992, 12, 5))
    assert hasil["purpose"]["male_line"] == 22
    assert hasil["purpose"]["female_line"] == 22


def test_titik_inti_selalu_1_sampai_22():
    for d in [date(1990, 3, 15), date(1985, 7, 4), date(2010, 9, 30), date(2000, 1, 1)]:
        hasil = hitung_matrix_destiny(d)
        assert 1 <= hasil["titik_inti"] <= 22
        assert hasil["nama_arketipe"]
