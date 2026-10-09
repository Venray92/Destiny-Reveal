"""REVISI01: grid 6 kategori Jelajahi + smooth scroll hero."""
import re


def test_six_categories_and_items():
    from components import sections
    cats = {c[0]: c for c in sections._categories()}
    assert list(cats) == ["daily", "self", "rel", "guid", "biz", "my"]
    assert cats["daily"][2] == "Daily Free Reveal" and cats["daily"][3] == "Gratis · Aktivitas harian · Reward"
    assert cats["guid"][2] == "Guidance &amp; Timing"
    daily = cats["daily"][6]
    assert "Gacha Kartu Tarot" in daily and "Daily Checkin" in daily and "Ramalan Kartu Harian" in daily
    assert "Tarot 1 Kartu" not in daily and "Streak" not in daily
    assert 'data-modal="solo"' in cats["self"][6] and "dh-open-reveal" in cats["self"][6]
    assert all(f'data-modal="compat_{k}"' in cats["rel"][6] for k in ("asmara", "keluarga", "teman", "bisnis"))
    assert 'data-modal="tarot_spread"' in cats["guid"][6] and 'data-modal="weekly"' in cats["guid"][6]
    for k in ("biz", "my"):
        assert cats[k][4] == "COMING SOON" and "Coming Soon" in cats[k][6] and "dh-ov-item" not in cats[k][6]


def test_every_item_modal_is_a_registered_dialog():
    from components import sections
    from components.navbar import _ALL_DIALOGS
    for c in sections._categories():
        for m in re.findall(r'data-modal="([a-z_0-9]+)"', c[6]):
            assert m in _ALL_DIALOGS, m


def test_hero_cta_scrolls_not_opens_modal():
    import inspect
    from components import sections, navbar
    src = inspect.getsource(sections.render_hero)
    assert "open_reveal_modal" not in src and "dh-explore" in src
    assert "scrollIntoView" in navbar.CAT_JS and "dhhero_cta" in navbar.CAT_JS
