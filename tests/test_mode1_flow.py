"""Tes alur Mode 1 (5 Sistem Kelahiran) di modal Reveal: helper + hasil engine."""

from datetime import date

from components.flow_state import rp, valid_email
from components.modal_steps import MODE1_SYSTEMS, compute_mode1


def test_valid_email():
    assert valid_email("steven@gmail.com")
    assert valid_email(" nama.belakang@mail.co.id ")
    for bad in ("", None, "bukan-email", "a@b", "a@@b.com", "a b@c.com"):
        assert not valid_email(bad)


def test_rp_format():
    assert rp(8000) == "Rp 8.000"
    assert rp(10000) == "Rp 10.000"


def test_mode1_results_1998_05_17():
    res = {r["system"]: r for r in compute_mode1("Rina Anggraini", date(1998, 5, 17))}
    assert [r for r in res] == [s for s, _ in MODE1_SYSTEMS]
    assert res["Zodiak"]["raw"]["sign"] == "Taurus"
    assert res["Shio"]["raw"]["shio"] == "Macan"
    assert (res["Weton"]["raw"]["hari"], res["Weton"]["raw"]["pasaran"], res["Weton"]["raw"]["neptu"]) == ("Minggu", "Pahing", 14)
    assert res["Numerologi"]["raw"]["life_path"] == 22
    assert res["Matrix Destiny"]["raw"]["titik_inti"] == 8
    for r in res.values():
        assert r["title"] and r["title"] != "Belum bisa dihitung"
        assert r["desc"] and r["tag"]


def test_mode1_out_of_range_year_does_not_crash():
    # shio cuma ada 1945-2020 -> kartunya "Belum bisa dihitung", sistem lain tetap jalan
    res = {r["system"]: r for r in compute_mode1("Kakek", date(1930, 3, 3))}
    assert res["Shio"]["title"] == "Belum bisa dihitung"
    assert res["Zodiak"]["raw"]["sign"] == "Pisces"
