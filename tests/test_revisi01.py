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
    assert "its.length>5" in _t("components/navbar.py") and "dh-ov-scroll" in _t("assets/css/home_v2.css")


def test_revisi02_font_dibawa_repo():
    from utils.affirmation_card import _FONT_DIR, _font
    for n in ("Lora-Italic-Variable.ttf", "DejaVuSerif-Bold.ttf", "DejaVuSans-Bold.ttf", "DejaVuSerif-Italic.ttf"):
        assert (_FONT_DIR / n).is_file()
    assert _font(["Lora-Italic-Variable.ttf"], 30).size == 30  # bukan font bitmap bawaan


def test_revisi02_preview_tanpa_kartu_lock_dan_kalender_satu_iframe():
    assert "dh-mn-lock" not in _t("components/mini_modals.py")
    ec = _t("components/energy_calendar.py")
    assert "_copy_dynamic" not in ec and 'id="cp"' in ec and "dhcal_hidden" in ec
