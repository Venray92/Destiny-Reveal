"""
Analisis kombinasi kartu untuk Tarot Spread (3 / 5 / 10 kartu).
Baca content/interpretations/tarot/tarot_combo.json. File tidak ada / kosong -> [] (tombol combo tidak muncul).
"""
import json
from functools import lru_cache
from pathlib import Path

from engine.tarot import TAROT_MAJOR_ARCANA

_FILE = Path(__file__).resolve().parent.parent / "content" / "interpretations" / "tarot" / "tarot_combo.json"
_THRESH = {3: 2, 5: 3, 10: 4}


@lru_cache(maxsize=1)
def _data():
    try:
        d = json.loads(_FILE.read_text(encoding="utf-8"))
        return d if isinstance(d, dict) else {}
    except (OSError, ValueError):
        return {}


def build_tarot_combo(slugs):
    """slugs = daftar slug kartu tebaran. Return [{"title","text"}]."""
    d = _data()
    n = len(slugs)
    if not d or n not in _THRESH:
        return []

    def blk(x):
        return {"title": x["title"], "text": x["text"]} if isinstance(x, dict) and x.get("title") and x.get("text") else None

    out = []
    majors = [s for s in slugs if s in TAROT_MAJOR_ARCANA]
    counts = {}
    for s in slugs:
        if s not in TAROT_MAJOR_ARCANA:
            counts[s.split("_")[0]] = counts.get(s.split("_")[0], 0) + 1
    suit = max(counts, key=counts.get) if counts else None
    if suit and counts[suit] >= _THRESH[n]:
        b = blk((d.get("suit_dominant") or {}).get(suit))
        if b:
            out.append(b)
    if len(majors) / n >= 0.6:
        b = blk(d.get("major_heavy"))
        if b:
            out.append(b)
    elif not majors:
        b = blk(d.get("minor_only"))
        if b:
            out.append(b)
    pairs = d.get("pairs") or {}
    for i in range(n):
        for j in range(i + 1, n):
            b = blk(pairs.get("+".join(sorted((slugs[i], slugs[j])))))
            if b:
                out.append(b)
    if not out:
        b = blk(d.get("balanced"))
        if b:
            out.append(b)
    return out
