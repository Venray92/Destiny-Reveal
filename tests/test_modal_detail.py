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
    from components import modal_detail
    entry = {"sections": {"free": {"quote": "Q"}, **{k: f"isi {k}" for k in "ABCDEFGHIJKLM"}}}
    monkeypatch.setattr(modal_detail, "_zodiak_json", lambda: {"Taurus": entry})
    d = build_detail("Zodiak", compute_raw_result("Zodiak", LD))
    texts = [t for sec in d["sections"] for t in sec[2]]
    assert texts == [f"isi {k}" for k in "ABCDEF"]  # G-M tidak ikut


def test_mini_modal_zodiak_info():
    from components.mini_modals import _zodiak_info
    d = _zodiak_info("Aquarius")
    assert d["tgl"] == "20 Jan - 18 Feb" and d["elemen"] == "Udara" and d["siapa"] and d["quote"]


def test_daily_reading_json_and_fallback(monkeypatch):
    from components import mini_modals as m
    monkeypatch.setattr(m, "_daily_json", lambda: {"data": {"zodiak": {"Aries": {"2026-10-03": {
        "pesan": "Satu. Dua. Tiga.", "angka_hoki": "9 & 27", "warna_hoki": "Merah Bata"}}}}})
    r = m.get_daily_reading("zodiak", "Aries", "2026-10-03")
    assert r == {"pesan": "Satu. Dua.", "angka": "9 & 27", "warna": "Merah Bata"}
    monkeypatch.setattr(m, "_daily_json", lambda: {})
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
    assert {"tarot_spread", "compat", "weekly", "blueprint", "tutorial", "blog", "faq"} <= set(DIALOGS)


# ---- UI15 ----
def test_ui15_info_dialogs_registered():
    from components.info_modals import DIALOGS
    assert set(DIALOGS) == {"about", "contact", "privacy", "terms"}


def test_ui15_pricing_tab_dialogs():
    from components.pricing_modal import DIALOGS, TABS
    keys = {k for k, _ in TABS}
    assert {"pricing", "pricing_koin", "pricing_fitur", "pricing_vip", "pricing_ref"} <= set(DIALOGS)
    assert {"semua", "koin", "fitur", "vip", "ref"} <= keys


# ---- UI16 ----
def test_ui16_spread_triggers():
    from components.feature_modals import DIALOGS
    assert {"tarot_spread_3", "tarot_spread_5", "tarot_spread_10"} <= set(DIALOGS)
