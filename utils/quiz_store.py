"""Jawaban kuesioner tersimpan di akun (dh_user["quiz_store"]) supaya bisa ditawarkan lagi.
Syarat pakai ulang: akun, nama + tgl lahir, daftar soal (id) dan jumlah soal sama (per sistem).
Keluarga: "bp" = Deep Dive <-> Complete Blueprint, "mx" = Multi-System Mode 2 <-> Mode 3."""

from datetime import datetime, timedelta, timezone

import streamlit as st

_WIB = timezone(timedelta(hours=7))
_BLN = ["", "Jan", "Feb", "Mar", "Apr", "Mei", "Jun", "Jul", "Agu", "Sep", "Okt", "Nov", "Des"]


def pkey(nama, tgl):
    return f"{(nama or '').strip().lower()}|{tgl.isoformat() if hasattr(tgl, 'isoformat') else tgl}"


def _root(fam):
    u = st.session_state.get("dh_user")
    if u is None:
        return {}
    return u.setdefault("quiz_store", {}).setdefault(fam, {})


def _now_txt():
    n = datetime.now(_WIB)
    return f"{n.day} {_BLN[n.month]} {n.year}, {n:%H.%M}"


def _ids(items, sys_):
    return sorted(str(it["q"]["id"]) for it in items if it["sys"] == sys_)


def save(fam, prof_key, mode, items, ans, feat):
    """Simpan jawaban per sistem yang SELURUH soalnya sudah terjawab. items = [{sys, q}]."""
    root = _root(fam).setdefault(prof_key, {})
    for s in dict.fromkeys(it["sys"] for it in items):
        mine = {str(it["q"]["id"]): (ans.get(s) or {}).get(it["q"]["id"]) for it in items if it["sys"] == s}
        if any(v is None for v in mine.values()):
            continue
        root[f"{s}|{mode}"] = {"ids": _ids(items, s), "ans": {it["q"]["id"]: ans[s][it["q"]["id"]] for it in items if it["sys"] == s},
                               "feat": feat, "waktu": _now_txt()}


def offer(fam, prof_key, plan_fn):
    """plan_fn(mode) -> items. Return tawaran terbaik {mode, cov{sys: entry}, systems, full} atau None."""
    root = _root(fam).get(prof_key) or {}
    best = None
    for mode in ("lengkap", "singkat"):
        items = plan_fn(mode)
        systems = list(dict.fromkeys(it["sys"] for it in items))
        cov = {}
        for s in systems:
            e = root.get(f"{s}|{mode}")
            if e and e["ids"] == _ids(items, s):
                cov[s] = e
        if not cov:
            continue
        cand = {"mode": mode, "cov": cov, "systems": systems, "full": len(cov) == len(systems)}
        if best is None or (cand["full"] and not best["full"]) or (cand["full"] == best["full"] and len(cov) > len(best["cov"])):
            best = cand
    return best


def first_missing(items, ans):
    for i, it in enumerate(items):
        if (ans.get(it["sys"]) or {}).get(it["q"]["id"]) is None:
            return i
    return max(0, len(items) - 1)


def fill(offer_, items):
    """Jawaban dari tawaran -> dict ans siap dipakai, plus indeks soal pertama yang belum terjawab."""
    ans = {s: dict(e["ans"]) for s, e in offer_["cov"].items()}
    return ans, first_missing(items, ans)
