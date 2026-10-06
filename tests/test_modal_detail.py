import datetime
from components.modal_detail import build_detail
from content.result_builder import compute_raw_result

LD = {"tanggal_lahir": datetime.date(1998, 5, 17), "nama_lengkap": "Rina"}


def test_zodiak_detail_lengkap():
    d = build_detail("Zodiak", compute_raw_result("Zodiak", LD))
    assert len(d["sections"]) == 6 and all(sec[2] for sec in d["sections"])
    assert dict(d["params"])["Rasi Bintang"] == "Taurus"


def test_sistem_lain_tetap_punya_detail():
    for s in ("Shio", "Weton", "Numerologi", "Matrix Destiny"):
        d = build_detail(s, compute_raw_result(s, LD))
        assert d and d["sections"][0][2] and d["params"]


def test_format_json_baru_mode1_hanya_A_sampai_F(monkeypatch):
    from content import profile_loader
    entry = {"sections": {"free": {"quote": "Q"}, **{k: f"isi {k}" for k in "ABCDEFGHIJKLM"}}}
    monkeypatch.setattr(profile_loader, "_data", lambda system: {"Taurus": entry} if system == "Zodiak" else {})
    d = build_detail("Zodiak", compute_raw_result("Zodiak", LD))
    texts = [t for sec in d["sections"] for t in sec[2]]
    assert texts == [f"isi {k}" for k in "ABCDEF"]  # G-M tidak ikut


def test_mini_modal_zodiak_info():
    from components.mini_modals import _zodiak_info
    d = _zodiak_info("Aquarius")
    assert d["tgl"] == "20 Jan - 18 Feb" and d["elemen"] == "Udara" and d["siapa"] and d["quote"]


def test_daily_reading_json_and_fallback(monkeypatch):
    from components import mini_modals as m
    monkeypatch.setattr(m.periodic, "get_daily", lambda s, n, now=None: {
        "pesan": "Satu. Dua. Tiga.", "angka_hoki": [9, 27, 30], "warna_hoki": "Merah Bata"})
    r = m.get_daily_reading("zodiak", "Aries", "2026-10-03")
    assert r == {"pesan": "Satu. Dua.", "angka": "9, 27 & 30", "warna": "Merah Bata"}
    monkeypatch.setattr(m.periodic, "get_daily", lambda s, n, now=None: None)
    r = m.get_daily_reading("zodiak", "Aries", "2026-10-03")
    assert r["pesan"].count(". ") == 0 and r["angka"] and r["warna"]


def test_auth_helpers():
    from components import auth
    assert auth._nama_dari_email("stevecorner512@gmail.com") == "stevecorner"
    r = auth._ref_code("stevecorner512@gmail.com")
    assert r.startswith("DR-STEVE") and len(r) == 12 and r == auth._ref_code("StevecorneR512@gmail.com")


# ---- UI14 ----
def test_ui14_weton_options():
    from components.feature_modals import WETON_OPTIONS
    assert "Senin Pon (Neptu 11)" in WETON_OPTIONS
    assert "Kamis Kliwon (Neptu 16)" in WETON_OPTIONS
    assert len(WETON_OPTIONS) == 35


def test_ui14_spreads_positions():
    from components.feature_modals import _SPREADS
    for n in (3, 5, 10):
        assert len(_SPREADS[n]["pos"]) == n


def test_ui14_dialog_registry():
    from components.feature_modals import DIALOGS
    assert {"tarot_spread", "weekly", "blueprint"} <= set(DIALOGS)
    from components.compat import DIALOGS as CP
    assert "compat" in CP


# ---- UI15 ----
def test_ui15_info_dialogs_registered():
    from components.info_modals import DIALOGS
    assert set(DIALOGS) == {"about"}
    from components.help_modals import DIALOGS as H
    assert set(H) == {"faq", "contact", "privacy", "terms", "tutorial", "blog"}


def test_ui15_pricing_tab_dialogs():
    from components.pricing_modal import DIALOGS, TABS
    keys = {k for k, _ in TABS}
    assert {"pricing", "pricing_koin", "pricing_fitur", "pricing_vip", "pricing_ref"} <= set(DIALOGS)
    assert {"semua", "koin", "fitur", "vip", "ref"} <= keys


# ---- UI16 ----
def test_ui16_spread_triggers():
    from components.feature_modals import DIALOGS
    assert {"tarot_spread_3", "tarot_spread_5", "tarot_spread_10"} <= set(DIALOGS)


# ---- UI17 (Stardust) ----
def test_ui17_stardust_packs():
    from components.pricing_modal import COIN_PACKS, TABS
    assert [p[4] for p in COIN_PACKS] == [120, 350, 750, 1600, 3500, 10000]
    assert [p[2] for p in COIN_PACKS] == ["Rp 10.000", "Rp 25.000", "Rp 50.000", "Rp 100.000", "Rp 200.000", "Rp 500.000"]
    assert [t[1] for t in TABS] == ["Semua", "✨ Stardust", "🔒 Fitur Stardust", "⭐ VIP", "🎁 Referral"]


def test_ui17_fitur_and_vip():
    from components.pricing_modal import FEATURES, VIP_PLANS
    prices = {n: sd for _, rows in FEATURES for n, sd, *_ in rows}
    assert len(prices) == 15 and prices["Buka 1 Sistem (Single)"] == 150 and prices["Buka 1 Sistem (Daily) Lengkap"] == 50
    assert prices["Complete Bundle (15 Sistem)"] == 500 and prices["Deep Blueprint Report"] == 300
    assert prices["Tarot Celtic Cross"] == 150 and prices["Compatibility (3 Sistem)"] == 250
    assert [p[2] for p in VIP_PLANS] == ["Rp 99.000", "Rp 249.000", "Rp 449.000", "Rp 799.000", "Rp 1.999.000"]


# ---- UI18 ----
def test_ui18_blueprint_am():
    from components.pricing_modal import BLUEPRINT_AM, FEATURES
    assert [k for k, *_ in BLUEPRINT_AM] == list("ABCDEFGHIJKLM")
    ket = {n: k for _, rows in FEATURES for n, _, k, *_ in rows}
    assert "13 Section" in ket["Deep Blueprint Report"]


# ---- UI19 ----
def test_ui19_referral_data():
    from components.pricing_modal import COMMISSION, MILESTONES, TIERS
    assert [c[2] for c in COMMISSION] == ["10 - 15%", "20 - 30%", "10 - 15%"]
    assert [m[1] for m in MILESTONES] == ["Extra Rp 50.000", "Extra Rp 250.000", "Extra Rp 1.000.000", "Extra Rp 2.500.000"]
    assert [t[1] for t in TIERS] == ["Stardust", "Star", "Constell.", "Galaxy", "Universe"]
    assert [t[2] for t in TIERS] == ["10%", "15%", "20%", "25%", "30%"]


# ---- UI20 ----
def test_ui20_affiliate_syarat():
    from components.pricing_modal import AFF_SYARAT
    assert len(AFF_SYARAT) == 6 and AFF_SYARAT[2].startswith("Total Revenue Rp 500.000")


# ---- UI21 ----
def test_ui21_streak_weeks_total_180():
    from components.mini_modals import _WEEKS
    assert [w[2] for w in _WEEKS] == [30, 40, 50, 60] and sum(w[2] for w in _WEEKS) == 180


def test_ui21_nav_uses_sparkle():
    from components import navbar
    import inspect
    src = inspect.getsource(navbar)
    assert "Tarot 3 Kartu (50✨)" in src and "Celtic Cross (150✨)" in src and "Klaim ✨ gratis" in src
    assert "(50 SD)" not in src


def test_ui21_faq_sections():
    from components.help_modals import _FAQ
    assert len(_FAQ) == 7 and sum(len(q) for _, _, q in _FAQ) == 20


# ---- UI22 ----
def test_ui22_faq_unlock_prices():
    from components.help_modals import _FAQ
    txt = str(_FAQ)
    assert "1 Sistem (A-F): 150✨" in txt and "1 Sistem (A-M): 300✨" in txt and "sebesar 150✨" in txt
    assert "sebesar 100✨" not in txt


def test_ui22_blog_posts():
    from components.help_modals import _BLOG_POSTS, _BLOG_CATS
    assert len(_BLOG_POSTS) == 5 and len(_BLOG_CATS) == 9


# ---- UI23 ----
def test_ui23_solo_systems_and_price():
    from components.solo_reveal import SYSTEMS, SOLO_PRICE, DIALOGS
    assert SOLO_PRICE == 150 and len(SYSTEMS) == 15 and len({n for n, _i, _k in SYSTEMS}) == 15
    assert [n for n, _i, k in SYSTEMS if k == "quiz"] == ["MBTI", "Big Five", "Enneagram", "DISC", "Love Language"]
    assert "solo" in DIALOGS


def test_ui23_solo_result_has_six_sections():
    from datetime import date
    from components.modal_detail import build_detail
    from content.result_builder import compute_raw_result
    d = build_detail("Zodiak", compute_raw_result("Zodiak", {"tanggal_lahir": date(1992, 12, 5)}))
    assert d and len(d["sections"]) == 6


def test_ui23_premium_card_no_old_buttons():
    import inspect
    from components import sections
    src = inspect.getsource(sections)
    assert 'modal="solo"' in src and "dhexplore_koin_btn" not in src and "dhexplore_vip_btn" not in src


def test_ui24_labels_and_pdf():
    import pathlib
    from utils.simple_pdf import make_pdf
    mm = pathlib.Path("components/mini_modals.py").read_text()
    assert "Buka Analisis Lengkap Per Sistem (150 ✨)" in mm
    assert "Sinkronkan dengan Sistem Lainnya →" in mm
    assert "Konfirmasi Kuota Harian Gratis" in mm and "Ya, Buka Ramalan" in mm
    assert "Weton & Shio Milikmu" not in mm and "Weton & Numerologi Lengkap" not in mm
    pdf = make_pdf("T", "S", [("A", ["halo dunia"])])
    assert pdf.startswith(b"%PDF") and pdf.rstrip().endswith(b"%%EOF")


def test_ui25_compat_and_solo_active():
    from datetime import date
    from components.compat import _compute, PRICE, SYSTEMS
    from components.solo_reveal import ACTIVE
    assert PRICE == 100 and len(SYSTEMS) == 4
    assert set(ACTIVE) == {"Zodiak", "Shio", "Weton", "Numerologi", "Matrix Destiny"}
    pa = {"nama": "A", "tgl": date(1992, 12, 5)}; pb = {"nama": "B", "tgl": date(1995, 3, 14)}
    for rel in ("Asmara / Pasangan", "Keluarga"):
        r = _compute(SYSTEMS, pa, pb, rel)
        assert 0 <= r["total"] <= 100 and len(r["rows"]) == 4 and r["nasihat"] and r["tantang"]
    assert _compute(["Shio"], pa, {"nama": "C", "tgl": date(1930, 1, 1)}, "Keluarga") is None


def test_ui26_profile_and_return_flow():
    import pathlib
    from components.profile import _tier, TIERS, FILTERS
    from components import dialog_bus
    assert [_tier(n) for n in (0, 9, 10, 49, 50, 100)] == [0, 0, 1, 1, 2, 3] and len(TIERS) == 4
    assert "Arsip" in FILTERS and hasattr(dialog_bus, "request_with_return")
    cp = pathlib.Path("components/compat.py").read_text()
    assert "help=_TIP" not in cp and "dhcp_info" in cp and "dhcp_card_" in cp
    assert 'request_with_return("auth", "compat")' in cp
    assert "Kotak Masuk Mail" not in pathlib.Path("components/profile.py").read_text()
