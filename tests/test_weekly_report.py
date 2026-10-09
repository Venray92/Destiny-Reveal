"""Tes Weekly & Monthly Report (content/weekly_calc.py + dialog)."""
from datetime import date, datetime, time

import pytest

from content import weekly_calc as W

PROF = {"nama": "Stev", "tgl": date(1992, 12, 5), "jam": time(10, 0)}
NOW = datetime(2026, 10, 9, 13, 0)


@pytest.mark.parametrize("kind", ["weekly", "monthly"])
@pytest.mark.parametrize("focus", ["harmoni", "karier", "asmara"])
def test_laporan_lengkap(kind, focus):
    r = W.build_report(kind, PROF, focus, NOW)
    assert len(r["prio"]) == 3 and 3 <= len(r["tema"]) + 1 and len(r["aspek"]) == 3
    assert len(r["dos"]) == 3 and len(r["donts"]) == 3
    assert all(a[2] for a in r["aspek"]), "kartu aspek tidak boleh kosong"
    assert all(15 <= b["pct"] <= 100 for b in r["bars"])
    assert len(r["bars"]) == (7 if kind == "weekly" else 5) and len(r["cards"]) == len(r["bars"])
    assert 0 < r["harmoni"]["idx"] <= 100 and r["hoki"]["angka"] and r["hoki"]["arah"]


def test_deterministik_dan_periode():
    a, b = W.build_report("weekly", PROF, "harmoni", NOW), W.build_report("weekly", PROF, "harmoni", NOW)
    assert a == b
    assert a["periode"].startswith("5 Oktober") and [c["label"] for c in a["cards"]][0] == "Senin, 5"
    m = W.build_report("monthly", PROF, "harmoni", NOW)
    assert m["periode"] == "Oktober 2026"


def test_golden_days_bulanan_hanya_hari_tersisa():
    m = W.build_report("monthly", PROF, "harmoni", NOW)
    assert all(int(x) >= 9 for x in m["best_txt"].replace(" Oktober", "").split(", "))


def test_dialog_terpasang_dan_harga():
    import pathlib
    from components import feature_modals, weekly_report
    from content import pricing as P
    assert feature_modals.DIALOGS["weekly"] is weekly_report.weekly_dialog
    assert weekly_report._KIND["weekly"]["price"] == P.WEEKLY and weekly_report._KIND["monthly"]["price"] == P.MONTHLY
    src = pathlib.Path("components/weekly_report.py").read_text()
    assert "Save ke Kalender" not in src and "checkbox" not in src.lower()
