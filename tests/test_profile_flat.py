"""Tes 9 sistem non-Mode-1 + Tarot: teks 100% dari JSON baru (profile_flat), kamus .py lama sudah dihapus."""
import json
from pathlib import Path

import pytest

from content import profile_flat as PF
from content.result_builder import build_display_data

ROOT = Path(__file__).resolve().parent.parent / "content" / "interpretations"

RAW = {
    "BaZi": [{"day_master": k} for k in ("jia", "yi", "bing", "ding", "wu", "ji", "geng", "xin", "ren", "gui")],
    "Zi Wei": [{"bintang": k} for k in PF._ZIWEI],
    "Human Design": [{"tipe_slug": k} for k in ("generator", "manifesting_generator", "manifestor", "projector", "reflector")],
    "Golongan Darah": [{"golongan_darah": k} for k in ("A", "B", "AB", "O")],
    "MBTI": [{"tipe": t} for t in ("INTJ", "INTP", "ENTJ", "ENTP", "INFJ", "INFP", "ENFJ", "ENFP",
                                   "ISTJ", "ISFJ", "ESTJ", "ESFJ", "ISTP", "ISFP", "ESTP", "ESFP")],
    "Enneagram": [{"tipe": n} for n in range(1, 10)],
    "DISC": [{"tipe": k} for k in "DISC"],
    "Love Language": [{"primary": k} for k in ("WA", "QT", "RG", "AS", "PT")],
}


@pytest.mark.parametrize("system", PF.SYSTEMS)
def test_audit_lengkap(system):
    assert PF.audit(system) == []


@pytest.mark.parametrize("system", list(RAW))
def test_semua_entri_tampil(system):
    for raw in RAW[system]:
        d = build_display_data(system, raw)
        assert d, (system, raw)
        assert d["p1"] and d["p2"] and d["p3"] and d["title"] and d["chip"]
        assert set(d["domains"]) == {"karir", "asmara", "keuangan", "kesehatan"}


def test_tarot_22_major_tampil():
    from engine.tarot import TAROT_MAJOR_ARCANA
    for k in TAROT_MAJOR_ARCANA:
        d = build_display_data("Tarot", {"kartu": k})
        assert d and ", " in d["title"]


def test_tarot_78_kartu_ada_di_json():
    assert len(PF._data("Tarot")) == 78


@pytest.mark.parametrize("lv", ["Rendah", "Sedang", "Tinggi"])
@pytest.mark.parametrize("trait", list("OCEAN"))
def test_big_five_semua_level(trait, lv):
    levels = {t: "Sedang" for t in "OCEAN"}
    levels[trait] = lv
    scores = {t: 20 for t in "OCEAN"}
    scores[trait] = {"Rendah": 12, "Sedang": 21, "Tinggi": 28}[lv]
    d = build_display_data("Big Five", {"levels": levels, "scores": scores, "dominant_trait": trait})
    assert d and d["p1"] and "empat dimensi lain" in d["p1"]


def test_kamus_py_lama_sudah_hilang():
    for f in ("bazi/bazi", "ziwei/ziwei", "human_design/human_design", "golongan_darah/golongan_darah", "mbti/mbti",
              "enneagram/enneagram", "disc/disc", "love_language/love_language", "big_five/big_five", "tarot/tarot",
              "weton/legi", "weton/pahing", "weton/pon", "weton/wage", "weton/kliwon"):
        assert not (ROOT / f"{f}.py").exists(), f


def test_titles_tanpa_em_dash():
    t = json.loads((ROOT / "titles.json").read_text(encoding="utf-8"))
    assert "—" not in json.dumps(t, ensure_ascii=False)


def test_big_five_sedang_punya_teks_sendiri():
    assert PF.bf_key("O", "Sedang", 21) == "openness_sedang"
    for t in "OCEAN":
        r = PF.get_big_five({"levels": {k: "Sedang" for k in "OCEAN"}, "scores": {k: 21 for k in "OCEAN"},
                             "dominant_trait": t})
        assert r and r["key"].endswith("_sedang") and len(r["paid"]) == 6
        assert len(r["ringkas"]) == 4


def test_tarot_78_kartu_semua_punya_teks():
    from engine.tarot import TAROT_DECK, kartu_periodik, tarik_tarot
    from content.result_builder import build_display_data
    assert len(TAROT_DECK) == 78 and len(set(TAROT_DECK)) == 78
    for k in TAROT_DECK:
        d = build_display_data("Tarot", {"kartu": k})
        assert d and d["p1"] and d["title"] and len(d["domains"]) == 4, k
    assert tarik_tarot()["kartu"] in TAROT_DECK


def test_tarot_periodik_deterministik():
    from engine.tarot import TAROT_DECK, kartu_periodik
    import datetime as dt
    n = dt.datetime(2026, 10, 6, 10)
    for kind in ("daily", "weekly", "monthly"):
        assert kartu_periodik(kind, n) == kartu_periodik(kind, n) in TAROT_DECK
    # hari beda di minggu sama -> kartu mingguan sama
    assert kartu_periodik("weekly", n) == kartu_periodik("weekly", n + dt.timedelta(days=1))
