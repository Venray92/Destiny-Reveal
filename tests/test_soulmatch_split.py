"""Batch 3: Soul Match 4 jenis (bobot per hubungan, entri, state)."""
import datetime as dt

from components import compat as CP
from components import navbar, sections

PA = {"nama": "Rina", "tgl": dt.date(1995, 3, 14), "gender": None}
PB = {"nama": "Budi", "tgl": dt.date(1990, 8, 2), "gender": None}


def test_bobot_jumlah_satu_dan_semua_relasi_ada():
    assert set(CP.WEIGHTS) == set(CP.RELATIONS) == {v[0] for v in CP.REL_KEYS.values()}
    for rel, w in CP.WEIGHTS.items():
        assert abs(sum(w.values()) - 1) < 1e-9 and set(w) == set(CP.SYSTEMS)


def test_total_berbobot_dihitung_benar():
    for rel in CP.RELATIONS:
        r = CP._compute(CP.SYSTEMS, PA, PB, rel)
        exp = round(sum(x["score"] * CP.WEIGHTS[rel][x["system"]] for x in r["rows"]))
        assert r["total"] == exp and sum(x["w"] for x in r["rows"]) in (99, 100, 101)


def test_subset_sistem_dinormalisasi():
    r = CP._compute(["Weton", "Numerologi"], PA, PB, "Keluarga")
    w = CP.WEIGHTS["Keluarga"]
    exp = round((r["rows"][0]["score"] * w["Weton"] + r["rows"][1]["score"] * w["Numerologi"]) / (w["Weton"] + w["Numerologi"]))
    assert r["total"] == exp


def test_bobot_beda_menghasilkan_skor_beda():
    totals = {rel: CP._compute(CP.SYSTEMS, PA, PB, rel)["total"] for rel in CP.RELATIONS}
    assert len(set(totals.values())) >= 2
    assert all(0 <= t <= 100 for t in totals.values())


def test_entri_terdaftar():
    for k in CP.REL_KEYS:
        assert f"compat_{k}" in navbar._ALL_DIALOGS
        assert f'data-modal="compat_{k}"' in sections._categories()[2][6]
    assert "compat" in navbar._ALL_DIALOGS
