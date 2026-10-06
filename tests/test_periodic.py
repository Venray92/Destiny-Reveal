"""Tes data baru 5 sistem: loader toleran, hitungan kalender, kelengkapan JSON, dan alur sampai build_detail."""
import datetime as dt

import pytest

from content import periodic as P
from content import profile_loader as PL
from content import safe_json as SJ
from engine import astro_lite as A
from engine import kalender_cina as K
from engine.rotation import WIB

NOW = dt.datetime(2026, 10, 6, 9, 0, tzinfo=WIB)


# ── safe_json ────────────────────────────────────────────────────
def test_safe_json_gabung_blok_list_dengan_kurung_nyasar():
    teks = '[\n  {"a": 1},\n  {\n\n[\n  {"a": 2}\n]'
    assert SJ.parse_text(teks) == [{"a": 1}, {"a": 2}]


def test_safe_json_gabung_blok_dict_dan_buang_cite():
    teks = ('{\n "system": "x",\n "data": {\n  "1": {"t": "satu[cite: 4, 5]."}\n }\n    },\n\n'
            '{\n "system": "x",\n "data": {\n  "2": {"t": "dua"}\n }\n}')
    d = SJ.parse_text(teks)
    assert d["data"] == {"1": {"t": "satu."}, "2": {"t": "dua"}}


def test_safe_json_tanpa_em_dash():
    assert SJ.bersihkan({"a": ["kenyamanan—seperti makanan", "x  y"]}) == {"a": ["kenyamanan, seperti makanan", "x y"]}


# ── astro_lite: nilai acuan dari ephemeris independen (ephem), tengah hari WIB ──
PIN = [
    ("2026-01-01", "Gemini", "Capricorn", "full_moon"),
    ("2026-03-20", "Aries", "Pisces", "new_moon"),
    ("2026-06-21", "Virgo", "Gemini", "first_quarter"),
    ("2026-10-06", "Leo", "Libra", "third_quarter"),
    ("2026-10-10", "Libra", "Libra", "new_moon"),
    ("2026-12-25", "Cancer", "Capricorn", "full_moon"),
    ("2027-02-14", "Taurus", "Aquarius", "first_quarter"),
    ("2027-07-04", "Cancer", "Cancer", "new_moon"),
]


@pytest.mark.parametrize("tgl,bulan,matahari,fase", PIN)
def test_astro_lite_cocok_ephemeris(tgl, bulan, matahari, fase):
    d = dt.date.fromisoformat(tgl)
    assert (A.tanda_bulan(d), A.tanda_matahari(d), A.fase_bulan(d)) == (bulan, matahari, fase)


def test_rumah_whole_sign():
    assert A.rumah("Sagittarius", "Leo") == 9 and A.rumah("Aries", "Aries") == 1 and A.rumah("Pisces", "Aries") == 2


# ── kalender Tionghoa vs sxtwl ───────────────────────────────────
def test_kalender_cina_cocok_sxtwl():
    sxtwl = pytest.importorskip("sxtwl")
    d = dt.date(2025, 1, 1)
    while d < dt.date(2028, 1, 1):
        assert (lambda g: (g.tg, g.dz))(sxtwl.fromSolar(d.year, d.month, d.day).getDayGZ()) == K.pilar_hari(d), d
        d += dt.timedelta(days=1)
    for y in range(1990, 2061):
        for m in range(1, 13):
            assert sxtwl.fromSolar(y, m, 15).getMonthGZ().dz == K.cabang_bulan(dt.date(y, m, 15)), (y, m)


# ── kunci periodik (tanggal konkret 6 Okt 2026, Selasa) ──────────
def test_kunci_periodik_6_okt_2026():
    assert P.kunci("Zodiak", "daily", "Sagittarius", NOW) == ("sagittarius", "9")      # Bulan di Leo
    assert P.kunci("Zodiak", "weekly", "Sagittarius", NOW) == ("sagittarius", "third_quarter")  # Senin 5 Okt
    assert P.kunci("Zodiak", "monthly", "Sagittarius", NOW) == ("sagittarius", "11")   # Matahari di Libra
    assert P.kunci("Shio", "daily", "Monyet", NOW) == ("monyet", "air")                # hari Gui
    assert P.kunci("Shio", "monthly", "Monyet", NOW) == ("monyet", "anjing")           # bulan Xu
    assert P.kunci("Weton", "weekly", "Sabtu Pon", NOW) == ("sabtu_pon", "third_quarter")


def test_numerologi_personal_year_dan_month():
    b = dt.date(1992, 12, 5)  # 5 + (1+2) + (2+0+2+6=10 -> 1) = 9 ; bulan Okt: 9 + 10 = 19 -> 1
    assert P.personal_year(b, 2026) == 9 and P.personal_month(b, 2026, 10) == 1
    assert P.kunci("Numerologi", "monthly", None, NOW, tgl_lahir=b) == ("9", "1")
    assert P.get_monthly("Numerologi", None, NOW, tgl_lahir=b)["fokus_bulan_ini"]
    assert P.get_monthly("Numerologi", None, NOW) is None  # tanpa tanggal lahir


def test_periode_yang_tidak_ada():
    assert P.get_weekly("Shio", "Tikus", NOW) is None and P.get_monthly("Weton", "Senin Legi", NOW) is None
    assert P.get_daily("Matrix Destiny", "1", NOW) is None and P.get_daily("Zodiak", "Bukanzodiak", NOW) is None


# ── kelengkapan JSON: sistem yang sudah lengkap ──────────────────
@pytest.mark.parametrize("system,kind", [("Zodiak", "daily"), ("Zodiak", "weekly"), ("Zodiak", "monthly"),
                                         ("Shio", "daily"), ("Shio", "monthly"), ("Numerologi", "monthly"),
                                         ("Weton", "daily"), ("Weton", "weekly")])
def test_periodik_lengkap_tanpa_duplikat(system, kind):
    a = P.audit(system, kind)
    assert a["hilang"] == [] and a["duplikat_beda_isi"] == [] and a["duplikat_sama"] == 0, a


def test_daily_zodiak_shio_terisi_setahun_penuh():
    for i in range(366):
        now = dt.datetime(2026, 1, 1, 8, tzinfo=WIB) + dt.timedelta(days=i)
        for t in A.TANDA:
            e = P.get_daily("Zodiak", t, now)
            assert e and e["pesan"] and len(e["angka_hoki"]) == 3 and e["warna_hoki"], (now.date(), t)
        for s in K.SHIO_URUT:
            assert P.get_daily("Shio", s.title(), now)["pesan"], (now.date(), s)


def test_weekly_monthly_zodiak_shio_terisi_setahun_penuh():
    for i in range(0, 366, 7):
        now = dt.datetime(2026, 1, 1, 8, tzinfo=WIB) + dt.timedelta(days=i)
        for t in A.TANDA:
            assert P.get_weekly("Zodiak", t, now)["prediksi"] and P.get_monthly("Zodiak", t, now)["prediksi"]
        for s in K.SHIO_URUT:
            assert P.get_monthly("Shio", s, now)["prediksi"]


def test_weton_weekly_lengkap_tanpa_duplikat():
    a = P.audit("Weton", "weekly")
    assert a["hilang"] == [] and a["duplikat_beda_isi"] == [] and a["duplikat_sama"] == 0, a


# ── profil statis ────────────────────────────────────────────────
@pytest.mark.parametrize("system", ["Zodiak", "Shio", "Numerologi", "Matrix Destiny"])
def test_profil_lengkap_free_dan_A_sampai_M(system):
    assert PL.audit(system) == []


def test_profil_weton_lengkap():
    assert PL.audit("Weton") == []


def test_profil_tanpa_em_dash_dan_cite():
    for system in PL.SYSTEMS:
        for e in PL._data(system).values():
            for v in e["sections"].values():
                for t in (v.values() if isinstance(v, dict) else [v]):
                    assert "—" not in t and "[cite" not in t


# ── ujung ke ujung: engine -> JSON baru -> build_detail ──────────
LD = {"tanggal_lahir": dt.date(1992, 12, 5), "nama_lengkap": "Steven Wu"}


@pytest.mark.parametrize("system,path,key", [
    ("Zodiak", "zodiak/zodiak_profile.json", "Sagittarius"),
    ("Shio", "shio/shio_profile.json", "Monyet"),
    ("Numerologi", "numerologi/numerologi_profile.json", "11"),
    ("Matrix Destiny", "matrix_destiny/matrix_destiny.json", "13"),
])
def test_build_detail_isinya_persis_dari_json_baru(system, path, key):
    from components.modal_detail import build_detail
    from content.result_builder import compute_raw_result
    entry = SJ.load(PL._BASE / path)["data"][key]["sections"]
    d = build_detail(system, compute_raw_result(system, LD))
    assert [t for sec in d["sections"] for t in sec[2]] == [entry[h] for h in "ABCDEF"]
    assert d["quote"] == entry["free"]["quote"] and d["params"]


def test_weton_senin_legi_pakai_json_baru_dan_weton_lain_jatuh_ke_kamus_lama():
    from components.modal_detail import build_detail
    from content.result_builder import compute_raw_result
    from engine.weton import hitung_weton
    d0 = dt.date(2026, 1, 1)
    while (w := hitung_weton(d0))["hari"] != "Senin" or w["pasaran"] != "Legi":
        d0 += dt.timedelta(days=1)
    entry = SJ.load(PL._BASE / "weton/weton_profile.json")["data"]["Senin Legi"]["sections"]
    d = build_detail("Weton", compute_raw_result("Weton", {"tanggal_lahir": d0}))
    assert [t for sec in d["sections"] for t in sec[2]] == [entry[h] for h in "ABCDEF"]
    lama = build_detail("Weton", compute_raw_result("Weton", LD))  # Sabtu Pon: belum ada di JSON baru
    assert lama and lama["sections"][0][2]


def test_compute_mode1_pakai_teks_json_baru():
    from components.modal_steps import compute_mode1
    hasil = {r["system"]: r for r in compute_mode1("Steven", dt.date(1992, 12, 5))}
    z = SJ.load(PL._BASE / "zodiak/zodiak_profile.json")["data"]["Sagittarius"]["sections"]["free"]
    assert hasil["Zodiak"]["quote"] == z["quote"] and hasil["Zodiak"]["desc"].startswith(z["siapa_kamu"][:40])


# ── JSON strict valid + title/tagline dari titles.json + tampilan tanpa kamus lama ──
import json

STRICT = ["zodiak/zodiak_profile.json", "zodiak/daily.json", "zodiak/weekly.json", "zodiak/monthly.json",
          "shio/shio_profile.json", "shio/daily.json", "shio/monthly.json", "weton/daily.json", "weton/weekly.json",
          "numerologi/numerologi_profile.json", "numerologi/monthly.json", "matrix_destiny/matrix_destiny.json",
          "titles.json"]


@pytest.mark.parametrize("path", STRICT)
def test_json_valid_strict(path):
    json.loads((PL._BASE / path).read_text(encoding="utf-8"))  # tanpa loader toleran


@pytest.mark.parametrize("system", ["Zodiak", "Shio", "Numerologi", "Matrix Destiny"])
def test_titles_dan_display_ada_untuk_semua_entri(system):
    from content.result_builder import build_display_data
    for k in PL.kunci_harapan(system):
        raw = {"Zodiak": lambda: {"sign": k}, "Shio": lambda: {"shio": k}, "Numerologi": lambda: {"life_path": int(k)},
               "Matrix Destiny": lambda: {"titik_inti": int(k)}}[system]()
        t = PL.get_title(system, raw)
        d = build_display_data(system, raw)
        assert t and t["title"] and t["tagline"] and "—" not in t["title"], (system, k)
        assert d and d["p1"] and d["p2"] and d["p3"] and d["quote"] and d["domains"]["karir"], (system, k)


def test_weton_title_isi_hari_dan_neptu():
    t = PL.get_title("Weton", {"hari": "Sabtu", "pasaran": "Pon", "neptu": 18})
    assert "Sabtu Pon" in t["title"] and "18" in t["title"] and "{" not in t["title"]


def test_kamus_lama_4_sistem_sudah_dihapus():
    for d in ("zodiak", "shio", "numerologi", "matrix_destiny"):
        assert [p.name for p in (PL._BASE / d).glob("*.py")] == ["__init__.py"]


def test_weton_cadangan_kamus_lama_tanpa_em_dash():
    from content.result_builder import build_display_data
    d = build_display_data("Weton", {"hari": "Sabtu", "pasaran": "Pon", "neptu": 16})  # Sabtu Pon belum ada di JSON baru
    assert "Sabtu Pon" in d["title"] and "—" not in d["title"] and "—" not in d["p1"]
