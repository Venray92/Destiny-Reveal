"""Batch 2: Kalender Energi (content/energy_calendar.py, components/energy_calendar.py)."""
import datetime as dt

from content import energy_calendar as C
from content import pricing as P
from engine.kalender_cina import cabang_bulan, pilar_hari

TGL = dt.date(1995, 3, 14)


def test_pejabat_hari_rumus():
    for n in range(1, 200, 7):
        d = dt.date(2026, 1, 1) + dt.timedelta(n)
        i, off = C.pejabat(d)
        assert i == (pilar_hari(d)[1] - cabang_bulan(d)) % 12 and off[0] in {o[0] for o in C.OFFICERS}
    # hari yang cabangnya sama dengan cabang bulan = Jian
    d = next(dt.date(2026, 3, 1) + dt.timedelta(k) for k in range(60)
             if pilar_hari(dt.date(2026, 3, 1) + dt.timedelta(k))[1] == cabang_bulan(dt.date(2026, 3, 1) + dt.timedelta(k)))
    assert C.pejabat(d)[1][0] == "Jian"


def test_tanda_valid_dan_jumlah_wajar():
    tot = {"bisnis": 0, "konflik": 0, "romansa": 0}
    for m in range(1, 13):
        h = C.bulan(TGL, 2026, m)
        assert len(h) == (dt.date(2026, m % 12 + 1, 1) if m < 12 else dt.date(2027, 1, 1)).__sub__(dt.date(2026, m, 1)).days
        for x in h:
            for t, lv, why in x["marks"]:
                assert t in tot and lv and why
        for k, v in C.ringkas(h).items():
            tot[k] += v
    assert 20 <= tot["bisnis"] <= 70 and 40 <= tot["konflik"] <= 90 and 15 <= tot["romansa"] <= 60


def test_aturan_bisnis_dan_konflik():
    for m in range(1, 13):
        for x in C.bulan(TGL, 2026, m):
            kinds = {t: lv for t, lv, _ in x["marks"]}
            if "bisnis" in kinds:
                assert x["off"]["id"] in C.GOOD
                if kinds["bisnis"] == "prima":
                    assert x["pd"] in (1, 8)
            if "konflik" in kinds:
                assert x["rel"] in ("Chong", "Hai")
            if "romansa" in kinds:
                assert x["rel"] in ("Liu He", "San He")


def test_detail_hari_empat_sistem():
    d = C.detail_hari(TGL, dt.date(2026, 10, 9))
    assert set(d) == {"Zodiak", "Shio", "Weton", "Numerologi"}
    assert all(v["pesan"] for v in d.values())


def test_payload_detail_hanya_kalau_paid():
    from components import energy_calendar as EC
    free = EC._payload(TGL, 2026, 10, False)
    paid = EC._payload(TGL, 2026, 10, True)
    assert all("detail" not in r for r in free["days"])
    assert all(len(r["detail"]) == 4 for r in paid["days"])
    html = EC._calendar_html(free)
    assert "Detail per hari" in html and '"detail"' not in html


def test_harga_dan_registrasi():
    from components import navbar, sections
    assert P.CALENDAR_MONTH > 0
    assert "kalender" in navbar._ALL_DIALOGS
    assert 'data-modal="kalender"' in sections._categories()[0][6]
