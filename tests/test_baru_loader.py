import json
from datetime import date
from pathlib import Path

from content import baru_loader as BL

_I = Path(__file__).resolve().parents[1] / "content" / "interpretations"


def test_jumlah_kunci_data_baru():
    assert len(json.loads((_I / "compat/konteks.json").read_text(encoding="utf-8"))) == 18
    assert len(json.loads((_I / "career/career_baru.json").read_text(encoding="utf-8"))) == 115
    assert len(json.loads((_I / "career/strength_baru.json").read_text(encoding="utf-8"))) == 113
    n = {"zodiak": 12, "shio": 12, "weton": 35, "numerologi": 12, "matrix_destiny": 22, "bazi": 10, "zi_wei": 14,
         "human_design": 5, "golongan_darah": 4, "mbti": 16, "enneagram": 9, "disc": 4, "love_language": 5, "big_five": 15}
    for s, c in n.items():
        assert len(json.loads((_I / f"blueprint_baru/{s}.json").read_text(encoding="utf-8"))) == c, s


def test_fallback_aman():
    assert BL.compat_konteks("Zodiak", "tidak_ada", "asmara") == ""
    assert BL.career_baru("career", "X|y") == ""
    assert BL.bp_baru("Sistem Fiktif", "a") == {}


def test_soulmatch_konteks_per_relasi_beda():
    from components import compat as C
    a, b = {"nama": "A", "tgl": date(1995, 3, 14)}, {"nama": "B", "tgl": date(1992, 12, 5)}
    hasil = {rel: C._compute(C.SYSTEMS, a, b, rel) for rel in C.RELATIONS}
    teks = {rel: " ".join(r["kuat"] + r["tantang"]) for rel, r in hasil.items()}
    assert len(set(teks.values())) == 4
    sama = {rel: BL.compat_konteks("Shio", "netral", C._REL_KEY[rel]) for rel in C.RELATIONS}
    assert all(sama.values()) and len(set(sama.values())) == 4


def test_blueprint_beda_dari_solo():
    from content import blueprint_calc as BC
    from content.result_builder import compute_raw_result
    raw = compute_raw_result("Zodiak", {"tanggal_lahir": date(1995, 4, 1), "nama_lengkap": "Tes"})
    asli, bp = BC._blocks("Zodiak", raw), BC._blocks("Zodiak", raw, bp=True)
    assert asli and bp and asli["key"] == bp["key"]
    assert asli["utama"] != bp["utama"] and asli["karier"] != bp["karier"]
