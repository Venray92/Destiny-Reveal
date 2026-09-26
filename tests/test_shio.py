"""
Test buat engine/shio.py

Nilai pembanding divalidasi dari themalatree.com/chinese-new-year-dates-1930-to-2030
(tabel tanggal Imlek 1945-2020, dicek silang lewat rumus modulo 12 --
1945=Ayam, 1992=Monyet, 1996=Tikus, 2020=Tikus semua konsisten).
"""

from datetime import date

import pytest

from engine.shio import hitung_shio


def test_hitung_shio_pertengahan_tahun():
    # Tanggal jauh dari Imlek (Juni), jadi shio-nya pasti tahun kalender itu sendiri.
    assert hitung_shio(date(1992, 12, 5)) == {"shio": "Monyet"}
    assert hitung_shio(date(1945, 6, 1)) == {"shio": "Ayam"}
    assert hitung_shio(date(1996, 6, 1)) == {"shio": "Tikus"}
    assert hitung_shio(date(2020, 6, 1)) == {"shio": "Tikus"}


def test_hitung_shio_sebelum_imlek_geser_ke_tahun_sebelumnya():
    # Imlek 1995 jatuh 31 Januari -- lahir sebelum itu masih shio 1994 (Anjing).
    assert hitung_shio(date(1995, 1, 15)) == {"shio": "Anjing"}


def test_hitung_shio_tepat_hari_imlek_sudah_tahun_baru():
    # Persis di hari Imlek -- sudah dianggap tahun baru (shio 1995 = Babi).
    assert hitung_shio(date(1995, 1, 31)) == {"shio": "Babi"}


def test_hitung_shio_sesudah_imlek():
    assert hitung_shio(date(1995, 2, 1)) == {"shio": "Babi"}


def test_hitung_shio_di_luar_rentang_data_error():
    with pytest.raises(ValueError):
        hitung_shio(date(2021, 6, 1))
    with pytest.raises(ValueError):
        hitung_shio(date(1944, 6, 1))
