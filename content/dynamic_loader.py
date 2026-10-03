"""
Loader data dinamis & berkala: harian, mingguan, bulanan.
File: content/dynamic/<folder>/{daily,weekly,monthly}.json
Kalau file/key belum ada, fungsi balikin None (UI tinggal sembunyikan kartunya).
"""

import json
from functools import lru_cache
from pathlib import Path

from engine.rotation import (format_periode_minggu, format_tanggal, now_wib, pick,
                             today_wib, week_slot, week_start)

_DIR = Path(__file__).resolve().parent / "dynamic"
_FOLDER = {"Zodiak": "zodiak"}  # tambah sistem lain di sini kalau file-nya sudah ada

DAILY_FIELDS = ("ramalan", "hoki", "warna", "saran", "quote")
WEEKLY_FIELDS = ("timing", "prediksi", "saran", "hindari")
MONTHLY_FIELDS = ("timing", "prediksi", "saran", "peluang", "risiko")


@lru_cache(maxsize=None)
def _load(system, kind):
    folder = _FOLDER.get(system)
    if not folder:
        return {}
    try:
        with open(_DIR / folder / f"{kind}.json", encoding="utf-8") as f:
            return (json.load(f).get("data")) or {}
    except (OSError, ValueError):
        return {}


def get_daily(system, key, anonymous_id="", now=None):
    """Ramalan harian: 1 teks per kategori, dipilih dari hash(tanggal+anonymous_id+sistem+kategori)."""
    entry = _load(system, "daily").get(str(key))
    if not entry:
        return None
    d = today_wib(now)
    out = {"tanggal": format_tanggal(d), "key": d.isoformat()}
    for cat in DAILY_FIELDS:
        out[cat] = pick(entry.get(cat), d.isoformat(), anonymous_id, system, cat)
    return out if all(out[c] for c in DAILY_FIELDS) else None


def get_weekly(system, key, now=None):
    """Weekly report: slot week_1..week_5 dari Senin minggu berjalan. Sama untuk semua pengguna sepanjang minggu."""
    entry = _load(system, "weekly").get(str(key))
    d = today_wib(now)
    blk = (entry or {}).get(f"week_{week_slot(d)}")
    if not blk:
        return None
    return {"periode": format_periode_minggu(d), "key": week_start(d).isoformat(),
            **{f: blk.get(f, "") for f in WEEKLY_FIELDS}}


def get_monthly(system, key, now=None):
    """Monthly report: bulan 1-12 dari tanggal WIB."""
    entry = _load(system, "monthly").get(str(key))
    d = today_wib(now)
    blk = (entry or {}).get(str(d.month))
    if not blk:
        return None
    from engine.rotation import BULAN
    return {"periode": f"{BULAN[d.month - 1]} {d.year}", "key": f"{d.year}-{d.month:02d}",
            **{f: blk.get(f, "") for f in MONTHLY_FIELDS}}


def validate(system, kind, minimum=None):
    """Cek struktur file. Return list pesan error (kosong = lolos).
    `minimum` = dict min jumlah item daily per kategori (target produksi 50/20/10/30/20)."""
    errs, data = [], _load(system, kind)
    if not data:
        return [f"{system}/{kind}: file kosong atau tidak ada"]
    for key, entry in data.items():
        if kind == "daily":
            for cat in DAILY_FIELDS:
                items = entry.get(cat)
                if not isinstance(items, list) or not items:
                    errs.append(f"{key}.{cat}: kosong")
                    continue
                if minimum and len(items) < minimum.get(cat, 0):
                    errs.append(f"{key}.{cat}: {len(items)} < {minimum[cat]}")
                if len(set(items)) != len(items):
                    errs.append(f"{key}.{cat}: ada duplikat")
        else:
            slots, fields = ((f"week_{i}" for i in range(1, 6)), WEEKLY_FIELDS) if kind == "weekly" \
                else ((str(i) for i in range(1, 13)), MONTHLY_FIELDS)
            for sl in slots:
                blk = entry.get(sl) or {}
                for f in fields:
                    if not str(blk.get(f, "")).strip():
                        errs.append(f"{key}.{sl}.{f}: kosong")
        for text in _texts(entry):
            if "—" in text or "–" in text or text != text.strip() or "  " in text:
                errs.append(f"{key}: format teks salah: {text[:40]}")
    return errs


def _texts(o):
    if isinstance(o, str):
        yield o
    elif isinstance(o, list):
        for x in o:
            yield from _texts(x)
    elif isinstance(o, dict):
        for x in o.values():
            yield from _texts(x)
