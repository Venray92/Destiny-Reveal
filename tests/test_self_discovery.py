import random
from datetime import date

from content import blueprint_calc as BC
from content import career_calc as CC
from utils import trait_cards

PROF = {"nama": "Tes", "tgl": date(1995, 3, 14), "jam": None, "kota": ""}


def _raws(mode, seed=1):
    random.seed(seed)
    ans = {}
    for it in BC.plan(mode, CC.QUIZ_SYSTEMS):
        s, q = it["sys"], it["q"]
        v = random.random() < .5 if s in ("MBTI", "Enneagram") else random.randint(1, 5) if s == "Big Five" else random.choice("ABCD")
        ans.setdefault(s, {})[q["id"]] = v
    return CC.trait_raws(ans, mode)


def test_jumlah_soal():
    assert len(BC.plan("singkat", CC.QUIZ_SYSTEMS)) == 61
    assert len(BC.plan("lengkap", CC.QUIZ_SYSTEMS)) == 127


def test_roles_10_unik():
    for o in ("RIASEC", "IASECR", "CERISA"):
        r = CC.roles(list(o))
        assert len(r) == 10 and len(set(r)) == 10


def test_riasec_rentang_dan_top_100():
    for m in ("singkat", "lengkap"):
        r = CC.riasec(_raws(m))
        assert max(r["rel"].values()) == 100 and min(r["rel"].values()) >= 0
        assert abs(sum(r["share"].values()) - 100) < 1.0


def test_career_dan_strength_terisi():
    for m in ("singkat", "lengkap"):
        raws = _raws(m)
        c, s = CC.build_career(PROF, raws, m), CC.build_strength(PROF, raws, m)
        assert len(c["code"]) == 3 and len(c["plan"]) == 4 and len(c["peran"]) == 10 and c["sistem"] and c["sinyal"]
        assert s["tags"] and s["blind"] and s["kuat"] and s["bars"]["ocean"] and s["bars"]["disc"]


def test_ekstrem_beda_arketipe():
    # semua "tidak setuju" vs semua "setuju" harus menghasilkan kode berbeda
    def run(v):
        ans = {}
        for it in BC.plan("singkat", CC.QUIZ_SYSTEMS):
            s = it["sys"]
            val = v if s in ("MBTI", "Enneagram") else (5 if v else 1) if s == "Big Five" else "A"
            ans.setdefault(s, {})[it["q"]["id"]] = val
        return CC.riasec(CC.trait_raws(ans, "singkat"))
    assert CC.archetype(run(True))["code"] != CC.archetype(run(False))["code"]


def test_kartu_png():
    raws = _raws("singkat")
    c, s = CC.build_career(PROF, raws, "singkat"), CC.build_strength(PROF, raws, "singkat")
    for b in (trait_cards.kartu_karier("Tes", c["code"], c["arketipe"], c["rel"], c["peran"]),
              trait_cards.kartu_kekuatan("Tes", s["tags"], [x[2] for x in s["blind"]])):
        assert b[:4] == b"\x89PNG"
