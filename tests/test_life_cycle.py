from datetime import date

from components import life_chart
from content import life_cycle as L


def test_titik_matrix_cocok_contoh_tervalidasi():
    # contoh 5 Des 1992 dari referensi Stev: A5 F17 B12 G6 C21 I5 D11 H16, E13
    r = L.roda(date(1992, 12, 5))
    assert [(p["kode"], p["arcana"]) for p in r["titik"]] == [("A", 5), ("F", 17), ("B", 12), ("G", 6), ("C", 21), ("I", 5), ("D", 11), ("H", 16)]
    assert r["inti"]["arcana"] == 13 and [p["usia"] for p in r["titik"]] == [0, 10, 20, 30, 40, 50, 60, 70]


def test_grafik_usia_titik_utama_dan_segmen():
    g = L.grafik_matrix(date(1992, 12, 5))
    assert [p["usia"] for p in g["titik"]] == [20, 30, 40, 50, 60]
    assert [p["arcana"] for p in g["titik"]] == [12, 6, 21, 5, 11]  # B G C I D
    assert [(s["dari"], s["sampai"]) for s in g["segmen"]] == [(20, 30), (30, 40), (40, 50), (50, 60)]
    assert all(0 <= p["skor"] <= 100 and len(p["teks"]) == 4 for p in g["titik"])


def test_kamus_22_lengkap():
    assert sorted(L.ARC) == list(range(1, 23)) and all(len(v) == 3 and v[0] and v[1] for v in L.ARC.values())


def test_pinnacle_contoh_manual():
    # 14 Mar 1995: m3 d5 y6 -> P1 8, P2 11, P3 1, P4 9 ; Life Path 5 -> P1 sampai usia 31
    p = L.pinnacle(date(1995, 3, 14))
    assert [x["angka"] for x in p] == [8, 11, 1, 9]
    assert [(x["usia_awal"], x["usia_akhir"]) for x in p] == [(0, 31), (32, 40), (41, 49), (50, None)]


def test_pinnacle_semua_angka_punya_teks():
    assert all(n in L.PIN and n in L.PIN_SKOR for n in (1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33))
    for d in (date(1990, 11, 29), date(2001, 2, 2), date(1985, 6, 30)):
        assert len(L.pinnacle(d)) == 4


def test_usia_dan_payload():
    assert L.usia(date(1995, 3, 14), date(2026, 3, 13)) == 30 and L.usia(date(1995, 3, 14), date(2026, 3, 14)) == 31
    assert life_chart.payload("Numerologi", date(1995, 3, 14), date(2026, 10, 9))["age"] == 31
    assert "roda" in life_chart.payload("Matrix Destiny", date(1995, 3, 14), date(2026, 10, 9))
