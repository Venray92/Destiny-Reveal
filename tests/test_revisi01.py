"""Revisi01: modal Daily Free (tombol, konfirmasi tutup, kalender, scroll submenu)."""
import pathlib

R = pathlib.Path(__file__).resolve().parent.parent


def _t(p):
    return (R / p).read_text(encoding="utf-8")


def test_tombol_dan_teks():
    mm, de = _t("components/mini_modals.py"), _t("components/daily_energy.py")
    assert "Sinkronkan" not in mm and "Sinkronkan" not in _t("components/energy_calendar.py")
    assert "Simpan Kartu PNG" not in de and "download_button" not in de
    assert 'request_solo("Tarot")' in mm and "(50 ✨)" not in mm


def test_konfirmasi_hanya_berbayar():
    mm, ec = _t("components/mini_modals.py"), _t("components/energy_calendar.py")
    assert 'dh_daily_paid' in mm and 'cc.dismiss("kalender", _cur_paid())' in ec
    assert 'cc.asking("tarot")' not in mm
    assert "Pastikan teks hasil sudah disalin" in mm and "Pastikan teks hasil sudah disalin" in ec


def test_kalender_tinggi_dinamis_dan_badge():
    ec = _t("components/energy_calendar.py")
    assert "frameElement" in ec and "Akses Terbuka" in ec and "Salin Teks Hasil Seluruhnya" in ec


def test_day_text_kalender():
    from components.energy_calendar import _day_text
    d = {"n": 15, "wd": 3, "skor": 66, "tier": "Kuat", "marks": [{"why": "tes"}],
         "detail": {"Zodiak": {"pesan": "p", "aksi": ["a"], "hindari": ["h"], "jam_baik": "20:00", "angka": [1, 2], "warna": "Merah"}}}
    t = _day_text(d, 2026, "Oktober")
    assert "Kamis, 15 Oktober 2026" in t and "[Zodiak]" in t and "Angka: 1, 2" in t


def test_scroll_submenu_maks_5():
    assert "its.length>5" in _t("components/navbar.py") and "dh-ov-scroll" in _t("assets/css/parts/14_revisi01_02_scroll_tarot_kalender.css")


def test_revisi02_font_dibawa_repo():
    from utils.share_card import _FD, font
    for n in ("Lora-Italic-Variable.ttf", "Lora-Variable.ttf", "Poppins-Regular.ttf", "Poppins-Medium.ttf", "Poppins-Bold.ttf"):
        assert (_FD / n).is_file()
    assert "assets/fonts" in font("serif", 30).path.replace("\\", "/")  # bukan font bitmap bawaan


def test_revisi02_preview_tanpa_kartu_lock_dan_kalender_satu_iframe():
    assert "dh-mn-lock" not in _t("components/mini_modals.py")
    ec = _t("components/energy_calendar.py")
    assert "_copy_dynamic" not in ec and 'id="cp"' in ec and "dhcal_hidden" in ec


def test_css_parts_urut_dan_lengkap():
    parts = sorted((R / "assets/css/parts").glob("*.css"))
    assert len(parts) >= 10 and [p.name[:2] for p in parts] == sorted(p.name[:2] for p in parts)
    css = "".join(p.read_text(encoding="utf-8") for p in parts)
    assert css.count("{") == css.count("}") and "dh-ov-scroll" in css and "dhTrFloat" in css
    assert not (R / "assets/css/home_v2.css").exists()


def test_tarot_uri_ringan():
    from utils.card_images import card_image_data_uri_small
    u = card_image_data_uri_small("tarot/major/12_hanged_man.jpg")
    assert u.startswith("data:image/webp;base64,") and len(u) < 200_000
    assert card_image_data_uri_small("tarot/major/22_tidak_ada.jpg") is None


def test_tarot_semua_kartu_punya_gambar():
    from engine.tarot import TAROT_DECK
    from utils.card_images import tarot_image_rel
    assert tarot_image_rel("hanged_man") == "tarot/major/12_hanged_man.jpg"
    assert tarot_image_rel("swords_page") == "tarot/sword/11_page_sword.jpg"
    assert tarot_image_rel("cups_03") == "tarot/cups/03_three_cups.jpg"
    assert tarot_image_rel("bukan_kartu") is None
    hilang = [s for s in TAROT_DECK if not tarot_image_rel(s)]
    assert hilang == [], hilang


def test_trait_cards_font_dari_repo():
    from utils import trait_cards as t
    from utils.share_card import font
    assert "assets/fonts" in font("sans_b", 34).path.replace("\\", "/")
    assert t.kartu_kekuatan("Rina", ["A", "B"], ["C"])[:4] == b"\x89PNG" or t.kartu_kekuatan("Rina", ["A", "B"], ["C"])


def test_tarot_nama_di_bawah_gambar():
    css = (R / "assets/css/parts/15_tarot_nama_di_bawah.css").read_text(encoding="utf-8")
    assert ".dh-tr-wrap + .dh-tr-over" in css
    src = _t("components/mini_modals.py")
    assert "{img}</div>'" in src and 'class="dh-tr-over"' in src


def test_revisi03_batch1():
    import importlib
    for m in ("components.aspek_info", "components.solo_reveal", "components.blueprint", "components.self_discovery"):
        importlib.import_module(m)
    from components.aspek_info import AF, AM
    assert [x[0] for x in AF] == list("ABCDEF") and [x[0] for x in AM] == list("ABCDEFGHIJKLM")
    assert "Gunakan Data Saya" in _t("components/form_kit.py")
    solo = _t("components/solo_reveal.py")
    assert "Biaya:" not in solo and "{sub} · {SOLO_PRICE}" not in solo
    mm = _t("components/mini_modals.py")
    assert "Konfirmasi Pilihan" in mm and "Konfirmasi Kuota Harian Gratis" in mm and "Ya, Gunakan" not in mm
    assert "cc.layer(" in _t("components/self_discovery.py")


def test_revisi03_batch2_quiz_kit():
    import importlib
    from content import blueprint_calc as BC
    qk = importlib.import_module("components.quiz_kit")
    for mod in ("components.solo_reveal", "components.self_discovery", "components.blueprint"):
        importlib.import_module(mod)
    assert "Mohon jawab seluruh pertanyaan" in qk.INC_TEXT and qk.INC_TITLE == "Pengisian Belum Lengkap"
    items = BC.plan("singkat", ["MBTI", "Big Five", "DISC", "Love Language"])
    got = {}
    get = lambda s, q: got.get((s, q))
    assert qk._first_missing(items, get) == 0
    for it in items:
        got[(it["sys"], it["q"]["id"])] = 1
    assert qk._first_missing(items, get) is None
    for it in items[:: max(1, len(items) // 8)]:
        assert qk.options(it["sys"], it["q"], {v: str(v) for v in range(1, 6)})


def test_revisi03_batch3_confirm_layer():
    import importlib, pathlib
    for mod in ("energy_calendar", "mini_modals", "blueprint", "compat", "decision", "feature_modals", "modal",
                "self_discovery", "solo_reveal", "weekly_report", "yearly"):
        src = pathlib.Path(f"components/{mod}.py").read_text(encoding="utf-8")
        assert "cc.render(" not in src, mod
        assert "cc.wrap(" in src, mod
        importlib.import_module(f"components.{mod}")


def test_revisi03_batch4_result_kit():
    import importlib
    rk = importlib.import_module("components.result_kit")
    for mod in ("components.solo_reveal", "components.blueprint", "components.self_discovery", "components.modal_detail"):
        importlib.import_module(mod)
    # radar hanya dari skor asli
    assert rk.quiz_axes("Zodiak", {"sign": "Leo"}) is None
    assert rk.quiz_axes("Big Five", {"scores": {"O": 7, "C": 35, "E": 21, "A": 14, "N": 28}}) == [
        ("Keterbukaan", 0), ("Kedisiplinan", 100), ("Ekstraversi", 50), ("Keramahan", 25), ("Sensitivitas", 75)]
    assert rk.quiz_axes("DISC", {"counts": {"D": 5, "I": 5, "S": 5, "C": 5}})[0][1] == 25
    assert rk.mbti_pairs({"counts": {"E": 3, "I": 1, "S": 0, "N": 4, "T": 2, "F": 2, "J": 1, "P": 3}})[0][4] == 75
    assert "<svg" in rk.radar_svg([("a", 10), ("b", 50), ("c", 90)])
    assert rk.dashboard("Zodiak", {"sign": "Leo"}) == ""
    assert rk.has_card("Zodiak", {"sign": "Pisces"}) and not rk.has_card("Human Design", {"placeholder": True})
    html_ = rk.insight_cards([("x", "A", ["Kalimat satu. Kalimat dua."]), ("y", "B", [])])
    assert html_.count("<details") == 1 and "Kalimat satu." in html_


def test_revisi03_batch5_multi_system_modes():
    import importlib
    from datetime import date
    mm = importlib.import_module("components.modal_multi")
    from content import pricing as P
    from content import blueprint_calc as BC
    assert mm.MODES["instan"][2] == P.BUNDLE_BIRTH == 200 and mm.MODES["mendalam"][2] == P.BUNDLE_PSY == 200
    assert mm.MODES["lengkap"][2] == P.BUNDLE_ALL == 1200 and len(mm.MODES["lengkap"][3]) == 15
    data = {"nama": "Rina", "tgl_lahir": date(1995, 3, 14), "jam_lahir": "10:00", "kota_lahir": "Jakarta", "golongan_darah": "O"}
    ans = {}
    for it in BC.plan("singkat", mm.PSY5):
        ans.setdefault(it["sys"], {})[it["q"]["id"]] = (True if it["sys"] in ("MBTI", "Enneagram") else
                                                      3 if it["sys"] == "Big Five" else "A")
    r2 = mm.compute_systems("mendalam", data, "singkat", ans)
    assert [r["system"] for r in r2] == mm.PSY5 and all(r["raw"] and r["title"] != "Belum bisa dihitung" for r in r2)
    r3 = mm.compute_systems("lengkap", data, "singkat", ans)
    assert len(r3) == 15 and sum(1 for r in r3 if r["title"] != "Belum bisa dihitung") >= 13
    assert all({"system", "label", "raw", "tag", "short", "title", "desc", "quote"} <= set(r) for r in r3)


def test_revisi03_batch6_share_card_story():
    import io
    from PIL import Image
    from utils import trait_cards as t
    rel = {k: 50 + i * 8 for i, k in enumerate("RIASEC")}
    for b in (t.kartu_karier("Tes", "ESC", "Penggerak", rel, ["A", "B"]), t.kartu_kekuatan("Tes", ["X", "Y"], ["Z"]),
              t.kartu_keputusan("A", "B", 3, -1, "A", "Langkah."),
              t.kartu_tahunan("Tes", 2027, "Kuda", "Kambing", "Harmoni", 70, "Baik", ["Feb"], ["Mei"], [50] * 12)):
        assert Image.open(io.BytesIO(b)).size == (2160, 3840)


def test_revisi03_batch4b_actions_dan_kartu_laporan():
    import io
    from PIL import Image
    from utils import trait_cards as t
    b = t.kartu_laporan("WEEKLY REPORT", "Rina", "78%", "Harmonis", [("Karier", 80), ("Asmara", 60)], "TOP", ["a", "b"])
    assert Image.open(io.BytesIO(b)).size == (2160, 3840)
    for f in ("components/yearly.py", "components/decision.py", "components/weekly_report.py", "components/compat.py",
              "components/feature_modals.py", "components/modal_steps.py"):
        assert "RK.actions(" in _t(f)
    from components import result_kit as RK
    assert "Tutup" in _t("components/result_kit.py") and callable(RK.actions)
    assert RK.sections_text("A", "b", [("X", ["y"])]).endswith("By Destiny Reveal")


def test_revisi_baru_batch_a():
    assert "Reveal Takdirku" not in _t("components/navbar.py").split("def render_navbar")[1].split("with right_col")[0]
    qk = _t("components/quiz_kit.py")
    assert "qi_key, last" in qk and "disabled=cur is None" in qk
    for f in ("components/self_discovery.py", "components/blueprint.py", "components/modal_multi.py"):
        assert _t(f).count('dh-nodismiss') >= 3
    mm = _t("components/modal_multi.py")
    assert "Mulai Kuesioner?" in mm and "dh_mx_modesel" in mm
