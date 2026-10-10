"""
Pembaca data teks baru dari Gemini (opsional). File belum ada atau kunci hilang -> pemanggil jatuh ke teks lama.
  compat/konteks.json            : Soul Match, kalimat konteks per skenario x jenis hubungan
  career/career_baru.json        : Career DNA, "sistem|entri" -> {"teks"}
  career/strength_baru.json      : Strength, "sistem|entri|kuat|latihan|blindspot" -> {"teks"}
  blueprint_baru/<sistem>.json   : Blueprint, parafrase aspek A-F (sistem lahir) / field paid (sistem lain)
"""

import json
from functools import lru_cache
from pathlib import Path

_BASE = Path(__file__).resolve().parent / "interpretations"


@lru_cache(maxsize=None)
def _load(rel):
    try:
        d = json.loads((_BASE / rel).read_text(encoding="utf-8"))
        return d if isinstance(d, dict) else {}
    except (OSError, ValueError):
        return {}


def compat_konteks(sistem, skenario, rel):
    """Teks konteks (str) atau ''. rel: asmara|keluarga|teman|bisnis."""
    t = (_load("compat/konteks.json").get(f"{sistem.lower()}__{skenario}") or {}).get(rel)
    return t.strip() if isinstance(t, str) else ""


def career_baru(kind, key):
    """kind: 'career' (key 'MBTI|intj') atau 'strength' (key 'MBTI|intj|kuat'). Return str atau ''."""
    f = "career/career_baru.json" if kind == "career" else "career/strength_baru.json"
    t = (_load(f).get(key) or {}).get("teks")
    return t.strip() if isinstance(t, str) else ""


def bp_baru(system, key):
    """{field: teks} parafrase Blueprint untuk satu entri, atau {}."""
    slug = system.lower().replace(" ", "_")
    e = _load(f"blueprint_baru/{slug}.json").get(key)
    return {k: v.strip() for k, v in e.items() if isinstance(v, str) and v.strip()} if isinstance(e, dict) else {}
