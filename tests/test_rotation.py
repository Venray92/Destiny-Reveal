from datetime import datetime, timedelta, timezone

from engine.rotation import (WIB, next_reset, pick, today_wib, week_slot, week_start)

UTC = timezone.utc


def test_hari_ganti_tepat_00_wib():
    sebelum = datetime(2026, 10, 3, 16, 59, tzinfo=UTC)   # 23:59 WIB
    sesudah = datetime(2026, 10, 3, 17, 0, tzinfo=UTC)    # 00:00 WIB
    assert today_wib(sebelum).isoformat() == "2026-10-03"
    assert today_wib(sesudah).isoformat() == "2026-10-04"


def test_minggu_ganti_hari_senin():
    assert week_start(today_wib(datetime(2026, 10, 4, 23, 59, tzinfo=WIB))).isoformat() == "2026-09-28"
    assert week_start(today_wib(datetime(2026, 10, 5, 0, 0, tzinfo=WIB))).isoformat() == "2026-10-05"


def test_slot_minggu_1_sampai_5():
    slots = {week_slot(today_wib(datetime(2026, 10, 1, tzinfo=WIB) + timedelta(days=i))) for i in range(60)}
    assert slots <= {1, 2, 3, 4, 5}


def test_next_reset():
    n = datetime(2026, 10, 3, 10, 0, tzinfo=WIB)
    assert next_reset("daily", n).isoformat().startswith("2026-10-04T00:00")
    assert next_reset("weekly", n).isoformat().startswith("2026-10-05T00:00")
    assert next_reset("monthly", n).isoformat().startswith("2026-11-01T00:00")
    assert next_reset("monthly", datetime(2026, 12, 15, tzinfo=WIB)).isoformat().startswith("2027-01-01")


def test_pick_stabil_dan_tersebar():
    opts = list(range(50))
    assert pick(opts, "a", "b") == pick(opts, "a", "b")
    assert len({pick(opts, "2026-10-03", f"user{i}", "Zodiak", "ramalan") for i in range(200)}) > 30
    assert pick([], "x") is None
