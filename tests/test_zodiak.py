"""
Test buat engine/zodiak.py
"""

from datetime import date

from engine.zodiak import hitung_zodiak


def test_hitung_zodiak_contoh_umum():
    assert hitung_zodiak(date(1992, 12, 5)) == {"sign": "Sagittarius", "element": "Api"}
    assert hitung_zodiak(date(1992, 7, 20)) == {"sign": "Cancer", "element": "Air"}
    assert hitung_zodiak(date(1992, 8, 15)) == {"sign": "Leo", "element": "Api"}


def test_hitung_zodiak_batas_awal_dan_akhir_rentang():
    assert hitung_zodiak(date(2000, 3, 21))["sign"] == "Aries"
    assert hitung_zodiak(date(2000, 4, 19))["sign"] == "Aries"
    assert hitung_zodiak(date(2000, 4, 20))["sign"] == "Taurus"


def test_hitung_zodiak_capricorn_melewati_pergantian_tahun():
    # Capricorn itu 22 Des - 19 Jan, melewati pergantian tahun kalender.
    assert hitung_zodiak(date(2000, 12, 25))["sign"] == "Capricorn"
    assert hitung_zodiak(date(2000, 1, 10))["sign"] == "Capricorn"
