"""
Test buat engine/numerologi.py
"""

from datetime import date

from engine.numerologi import (
    hitung_birthday_number,
    hitung_expression_number,
    hitung_life_path,
    hitung_numerologi_lengkap,
    hitung_personality_number,
    hitung_soul_urge_number,
)


def test_hitung_life_path_master_number_tidak_direduce():
    # 5+3+3 = 11 -- harus berhenti di 11 (Master Number), bukan jadi 1+1=2.
    assert hitung_life_path(date(1992, 12, 5)) == 11


def test_hitung_life_path_angka_biasa():
    assert hitung_life_path(date(2000, 1, 1)) == 4
    assert hitung_life_path(date(1999, 11, 22)) == 7


def test_hitung_life_path_selalu_1_sampai_9_atau_master_number():
    for d in [date(1990, 3, 15), date(1985, 7, 4), date(2010, 9, 30)]:
        hasil = hitung_life_path(d)
        assert hasil in set(range(1, 10)) | {11, 22, 33}


def test_hitung_expression_number_dari_nama():
    # "Steven Wu" -> total nilai semua huruf = 30 -> 3+0 = 3.
    assert hitung_expression_number("Steven Wu") == 3


def test_hitung_soul_urge_number_dari_vokal():
    # Vokal di "Steven Wu": E, E, U -> 5+5+3 = 13 -> 1+3 = 4.
    assert hitung_soul_urge_number("Steven Wu") == 4


def test_hitung_personality_number_dari_konsonan():
    # Konsonan di "Steven Wu": S,T,V,N,W -> 1+2+4+5+5 = 17 -> 1+7 = 8.
    assert hitung_personality_number("Steven Wu") == 8


def test_hitung_birthday_number():
    assert hitung_birthday_number(date(1992, 12, 5)) == 5


def test_hitung_numerologi_lengkap_gabungan():
    hasil = hitung_numerologi_lengkap(date(1992, 12, 5), "Steven Wu")
    assert hasil == {
        "life_path": 11, "expression": 3, "soul_urge": 4,
        "personality": 8, "birthday": 5,
    }
