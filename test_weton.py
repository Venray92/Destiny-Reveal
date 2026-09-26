"""
Test buat engine/weton.py
Nilai pembanding: 17 Agustus 1945 = Jumat Legi, neptu 11 -- dikonfirmasi
lewat berita independen (bisnis.com, jawapos.com, dicek 26 Sep 2026),
bukan cuma diasumsikan dari catatan lama.
"""

from datetime import date

from engine.weton import hitung_weton


def test_hitung_weton_tanggal_acuan():
    assert hitung_weton(date(1945, 8, 17)) == {
        "hari": "Jumat", "pasaran": "Legi", "neptu": 11,
        "pancasuda": {
            "nama": "Sri",
            "arti": "Murah rejeki, selamat, dan dicintai lingkungan sekitar.",
        },
    }


def test_hitung_weton_neptu_selalu_dalam_rentang_wajar():
    # Neptu = neptu hari (3-9) + neptu pasaran (4-9), jadi selalu 7-18.
    hasil = hitung_weton(date(1992, 12, 5))
    assert 7 <= hasil["neptu"] <= 18
    assert hasil["hari"] in {"Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"}
    assert hasil["pasaran"] in {"Legi", "Pahing", "Pon", "Wage", "Kliwon"}


def test_hitung_weton_pancasuda_sri_untuk_5_desember_1992():
    # Neptu Sabtu Pon = 16 -> 16 % 5 = 1 -> Sri.
    hasil = hitung_weton(date(1992, 12, 5))
    assert hasil["pancasuda"]["nama"] == "Sri"


def test_hitung_weton_pancasuda_semua_kategori_kebagian():
    # Sisa 0-4 dari neptu 7..18 -- pastikan semua 5 kategori kepakai
    # (bukan cuma sebagian) dan namanya sesuai tabel acuan Stev.
    from engine.weton import _PANCASUDA
    assert {v[0] for v in _PANCASUDA.values()} == {
        "Sri", "Lungguh", "Gedhong", "Loro", "Pati",
    }


def test_hitung_weton_konsisten_tiap_5_hari():
    # Pasaran itu siklus 5 hari -- tanggal yang berjarak persis 5 hari
    # harus punya pasaran yang sama.
    a = hitung_weton(date(2000, 1, 1))
    b = hitung_weton(date(2000, 1, 6))
    assert a["pasaran"] == b["pasaran"]


def test_hitung_weton_konsisten_tiap_7_hari():
    # Hari itu siklus 7 hari -- tanggal yang berjarak persis 7 hari
    # harus punya nama hari yang sama.
    a = hitung_weton(date(2000, 1, 1))
    b = hitung_weton(date(2000, 1, 8))
    assert a["hari"] == b["hari"]
