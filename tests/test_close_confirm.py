"""Tes konfirmasi tutup modal hasil + teks Soul Match yang lebih panjang."""
from datetime import date

import streamlit as st

from components import close_confirm as cc
from components import compat


class _SS(dict):
    __getattr__ = dict.get

    def __setattr__(self, k, v):
        self[k] = v


def _fake(monkeypatch):
    ss = _SS()
    monkeypatch.setattr(st, "session_state", ss)
    return ss


def test_x_di_hasil_nanya_dulu(monkeypatch):
    ss = _fake(monkeypatch)
    cc.dismiss("solo", True)
    assert cc.asking("solo") and ss["dh_cc_reopen"] == "solo"


def test_x_di_konfirmasi_keluar_beneran(monkeypatch):
    ss = _fake(monkeypatch)
    called = []
    cc.cb_ask("solo")
    cc.dismiss("solo", True, leave=lambda: called.append(1))
    assert not cc.asking("solo") and called == [1] and "dh_cc_reopen" not in ss


def test_x_bukan_di_hasil_tidak_nanya(monkeypatch):
    ss = _fake(monkeypatch)
    cc.dismiss("solo", False)
    assert not cc.asking("solo") and "dh_cc_reopen" not in ss


def test_stay_membersihkan_flag(monkeypatch):
    _fake(monkeypatch)
    cc.cb_ask("compat")
    cc.cb_stay("compat")
    assert not cc.asking("compat")


def test_teks_kecocokan_lebih_panjang():
    pa = {"tgl": date(1992, 12, 5), "nama": "A"}
    pb = {"tgl": date(1995, 3, 9), "nama": "B"}
    for rel in compat.RELATIONS:
        r = compat._compute(compat.SYSTEMS, pa, pb, rel)
        for k in ("kuat", "tantang", "nasihat"):
            assert all(len(t) >= 120 for t in r[k]), (rel, k)
        assert len(r["nasihat"]) >= 5
