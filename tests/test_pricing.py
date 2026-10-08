"""Tes config harga (single source of truth)."""
from content import pricing as P


def test_fitur_baru():
    assert (P.SOLO, P.WEEKLY, P.MONTHLY, P.BLUEPRINT, P.BUNDLE_ALL) == (200, 300, 600, 800, 1200)
    assert P.VIP_LIFETIME == 2499000


def test_paket_dan_rate():
    assert [(r, c) for _, _, r, c, *_ in P.COIN_PACKS] == [(10000, 120), (25000, 320), (50000, 700), (100000, 1500), (200000, 3200), (500000, 8500)]
    assert [P.per_coin(r, c) for _, _, r, c, *_ in P.COIN_PACKS] == ["Rp 83/✨", "Rp 78/✨", "Rp 71/✨", "Rp 67/✨", "Rp 63/✨", "Rp 59/✨"]
    assert P.fmt(1200) == "1.200" and P.rp(2499000) == "Rp 2.499.000"


def test_terpasang_di_ui():
    import pathlib
    from components import solo_reveal, compat, mini_modals, pricing_modal
    assert solo_reveal.SOLO_PRICE == P.SOLO and compat.PRICE == P.COMPAT and mini_modals.SWAP_PRICE == P.SWAP
    assert any(v[2] == "Rp 2.499.000" for v in pricing_modal.VIP_PLANS)
    sec = pathlib.Path("components/sections.py").read_text()
    for t in ("Soul Match", "Blueprint Mendalam", "Tarot Spreads"):
        assert t in sec
    for f in pathlib.Path("components").glob("*.py"):
        assert "Cek Kecocokan" not in f.read_text(), f.name
