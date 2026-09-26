"""
Test buat engine/numerologi.py
"""

from datetime import date

import pytest

from engine.numerologi import hitung_expression_number, hitung_life_path


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


def test_hitung_expression_number_belum_diimplementasi():
    # Masih stub -- lihat catatan di engine/numerologi.py soal keputusan
    # scope (Expression Number belum dipakai, cuma Life Path).
    with pytest.raises(NotImplementedError):
        hitung_expression_number("Contoh Nama")
