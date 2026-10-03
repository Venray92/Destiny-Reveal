from datetime import datetime

from content import dynamic_loader as dl
from engine.rotation import WIB

HARI_INI = datetime(2026, 10, 3, 9, 0, tzinfo=WIB)


def test_file_aries_lolos_validasi():
    for kind in ("daily", "weekly", "monthly"):
        assert dl.validate("Zodiak", kind) == []


def test_daily_stabil_per_hari_dan_user():
    a = dl.get_daily("Zodiak", "Aries", "user1", HARI_INI)
    assert a == dl.get_daily("Zodiak", "Aries", "user1", HARI_INI)
    assert a["tanggal"] == "Sabtu, 3 Oktober 2026" and all(a[c] for c in dl.DAILY_FIELDS)


def test_daily_beda_hari_atau_user_bisa_beda():
    hasil = {dl.get_daily("Zodiak", "Aries", f"u{i}", HARI_INI)["ramalan"] for i in range(30)}
    assert len(hasil) > 1
    besok = datetime(2026, 10, 4, 0, 0, tzinfo=WIB)
    assert dl.get_daily("Zodiak", "Aries", "u1", besok)["key"] == "2026-10-04"


def test_weekly_sama_sepanjang_minggu_ganti_senin():
    sen = dl.get_weekly("Zodiak", "Aries", datetime(2026, 9, 28, 0, 0, tzinfo=WIB))
    min_ = dl.get_weekly("Zodiak", "Aries", datetime(2026, 10, 4, 23, 59, tzinfo=WIB))
    assert sen == min_ and sen["periode"] == "28 September sampai 4 Oktober 2026"
    assert dl.get_weekly("Zodiak", "Aries", datetime(2026, 10, 5, tzinfo=WIB))["key"] == "2026-10-05"


def test_monthly_ganti_tanggal_1():
    assert dl.get_monthly("Zodiak", "Aries", datetime(2026, 10, 31, 23, 59, tzinfo=WIB))["periode"] == "Oktober 2026"
    assert dl.get_monthly("Zodiak", "Aries", datetime(2026, 11, 1, tzinfo=WIB))["periode"] == "November 2026"


def test_key_atau_sistem_tidak_ada_balikin_none():
    assert dl.get_daily("Zodiak", "Leo", "u", HARI_INI) is None
    assert dl.get_weekly("Shio", "Tikus", HARI_INI) is None
    assert dl.get_monthly("Zodiak", "Leo", HARI_INI) is None


def test_validate_deteksi_kurang_dari_target_produksi():
    errs = dl.validate("Zodiak", "daily", {"ramalan": 50, "hoki": 20, "warna": 10, "saran": 30, "quote": 20})
    assert len(errs) == 5
