"""Test Deep Blueprint (REVISI06 bagian 3): rencana soal, build, harga."""
from datetime import date

from content import blueprint_calc as BC
from content import pricing as P

PROF = {"nama": "Rina", "tgl": date(1995, 8, 17), "jam": None, "kota": "Jakarta", "golda": "O"}


def test_plan_counts():
    assert len(BC.plan("singkat", BC.NAMES)) == 73
    assert len(BC.plan("lengkap", BC.NAMES)) == 157
    assert BC.plan("singkat", ["Zodiak"]) == []


def test_deep_dive_birth_system():
    r = BC.build_blueprint(PROF, ["Zodiak"], {}, "lengkap", 2026)
    assert r and not r["complete"] and r["systems"][0]["ok"]
    assert r["systems"][0]["utama"] and r["systems"][0]["karier"]


def test_complete_with_quiz_short():
    ans = {}
    for it in BC.plan("singkat", BC.NAMES):
        s, q = it["sys"], it["q"]
        v = {"MBTI": True, "Enneagram": True, "Big Five": 4, "DISC": "A", "Love Language": "A"}[s]
        ans.setdefault(s, {})[q["id"]] = v
    r = BC.build_blueprint(PROF, BC.NAMES, ans, "singkat", 2026)
    assert r["complete"] and r["n_ok"] >= 13
    assert len(r["synth"]["roadmap"]) == 3 and any(x["star"] for x in r["synth"]["roadmap"])


def test_prices():
    assert P.BLUEPRINT == 800 and P.BLUEPRINT_ALL > P.BLUEPRINT
