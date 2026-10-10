"""Batch 1: Skor Energi + Afirmasi (content/daily_energy.py, utils/affirmation_card.py)."""
import datetime as dt
import io

from PIL import Image

from content import daily_energy as DE
from utils.affirmation_card import buat_kartu

TGL = dt.date(1995, 3, 14)
HARI = dt.date(2026, 10, 9)


def test_relasi_shio():
    assert DE._relasi(0, 1) == "liu_he" and DE._relasi(0, 6) == "chong"
    assert DE._relasi(0, 7) == "hai" and DE._relasi(0, 4) == "san_he"
    assert DE._relasi(3, 3) == "sama" and DE._relasi(0, 2) == "netral"


def test_skor_deterministik_dan_dalam_rentang():
    assert DE.skor_energi(TGL, HARI) == DE.skor_energi(TGL, HARI)
    xs = [DE.skor_energi(TGL, HARI + dt.timedelta(i))["skor"] for i in range(120)]
    assert all(0 <= x <= 100 for x in xs) and max(xs) - min(xs) >= 30


def test_komponen_empat_sistem_dan_bobot():
    r = DE.skor_energi(TGL, HARI)
    assert set(r["komponen"]) == {"Zodiak", "Shio", "Weton", "Numerologi"}
    assert abs(sum(DE.BOBOT.values()) - 1) < 1e-9
    mean = sum(v["skor"] * 0.25 for v in r["komponen"].values())
    assert r["skor"] == int(round(max(5, min(98, 58 + (mean - 66) * 1.5))))


def test_tabel_lengkap():
    assert set(DE.RUMAH_SKOR) == set(DE.RUMAH_INFO) == set(DE.AFF_RUMAH) == set(range(1, 13))
    assert set(DE.NUM_SKOR) == set(DE.NUM_INFO) == set(DE.AFF_NUM) == set(DE.AFF_ACT) == set(range(1, 10))
    assert set(DE.RELASI_SKOR) == set(DE.RELASI_INFO) == set(DE.AFF_SHIO)
    assert set(DE.PANCA_SKOR) == set(DE.PANCA_INFO) == set(DE.AFF_WETON)
    for v in list(DE.AFF_NUM.values()) + list(DE.AFF_RUMAH.values()) + list(DE.AFF_WETON.values()) + [x for l in DE.AFF_SHIO.values() for x in l]:
        assert v.startswith("Aku")


def test_afirmasi_empat_kalimat_dan_semua_hari_jalan():
    for i in range(400):
        a = DE.afirmasi(dt.date(1990, 6, 1) + dt.timedelta(i * 3), HARI + dt.timedelta(i))
        assert len(a["kalimat"]) == 4 and a["langkah"]


def test_kartu_png_ukuran_dan_watermark():
    a = DE.afirmasi(TGL, HARI)
    png = buat_kartu("Rina", "Jumat, 9 Oktober 2026", a["kalimat"], a["langkah"])
    im = Image.open(io.BytesIO(png))
    assert im.size == (2160, 3840)
    ref = Image.open(io.BytesIO(buat_kartu("Rina", "Jumat, 9 Oktober 2026", a["kalimat"], a["langkah"])))
    assert im.tobytes() == ref.tobytes()


def test_terdaftar_di_navbar_dan_grid():
    from components import navbar, sections
    assert "energi" in navbar._ALL_DIALOGS and "afirmasi" in navbar._ALL_DIALOGS
    body = sections._categories()[0][6]
    assert 'data-modal="energi"' in body and 'data-modal="afirmasi"' in body
