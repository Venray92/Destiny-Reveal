"""
Loader JSON toleran untuk file konten hasil paste beberapa batch AI.

Masalah yang diperbaiki otomatis (file aslinya tidak diubah):
- beberapa blok `{ "system": ... }` atau `[ ... ]` ditempel berurutan dalam satu file
- kurung penutup kelebihan / kurang di ujung tiap blok, koma menggantung, `{` menggantung
- sisa penanda sitasi AI seperti `[cite: 4, 5]`

Hasil: dict (file ber-`data`) digabung per key, list digabung berurutan.
"""

import json
import re
from functools import lru_cache
from pathlib import Path

_CITE = re.compile(r"\s*\[cite:[^\]]*\]")
_BLOCK_START = re.compile(r"(?m)^(?=[\[{]\s*$)")


def _balance(chunk):
    """Buang `{`/koma menggantung di ujung, tutup kurung yang masih terbuka, abaikan penutup berlebih."""
    s = chunk.rstrip()
    while s and s[-1] in ",{":
        s = s[:-1].rstrip()
    out, stack, in_str, esc = [], [], False, False
    for ch in s:
        if in_str:
            out.append(ch)
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == '"':
                in_str = False
            continue
        if ch == '"':
            in_str = True
        elif ch in "[{":
            stack.append("]" if ch == "[" else "}")
        elif ch in "]}":
            if not stack or stack[-1] != ch:
                continue  # penutup berlebih -> buang
            stack.pop()
        out.append(ch)
    return "".join(out) + "".join(reversed(stack))


def parse_text(text):
    """Parse teks JSON; kalau gagal, pecah per blok lalu perbaiki dan gabungkan. Raise ValueError kalau tetap gagal."""
    text = _CITE.sub("", text)
    try:
        return json.loads(text)
    except ValueError:
        pass
    parts = []
    for chunk in _BLOCK_START.split(text):
        if not chunk.strip():
            continue
        try:
            parts.append(json.loads(_balance(chunk)))
        except ValueError as e:
            raise ValueError(f"blok tidak bisa diperbaiki: {e}") from e
    if not parts:
        raise ValueError("file kosong")
    return _merge(parts)


def _merge(parts):
    if all(isinstance(p, list) for p in parts):
        return [x for p in parts for x in p]
    if all(isinstance(p, dict) for p in parts):
        merged = {}
        for p in parts:
            for k, v in p.items():
                if isinstance(v, dict) and isinstance(merged.get(k), dict):
                    merged[k].update(v)
                else:
                    merged[k] = v
        return merged
    raise ValueError("campuran list dan dict dalam satu file")


_EM_DASH = re.compile(r"\s*—\s*")


def bersihkan(obj):
    """Rapikan teks sesuai gaya situs: tanpa em dash (diganti koma), spasi ganda dibuang. Rekursif."""
    if isinstance(obj, str):
        return re.sub(r"[ \t]{2,}", " ", _EM_DASH.sub(", ", obj)).strip()
    if isinstance(obj, list):
        return [bersihkan(x) for x in obj]
    if isinstance(obj, dict):
        return {k: bersihkan(v) for k, v in obj.items()}
    return obj


@lru_cache(maxsize=64)
def load(path):
    """Baca file JSON (toleran + teks dibersihkan). Return None kalau file tidak ada / tidak bisa dibaca.
    Hasilnya di-cache: jangan dimodifikasi oleh pemanggil."""
    try:
        return bersihkan(parse_text(Path(path).read_text(encoding="utf-8")))
    except (OSError, ValueError):
        return None
