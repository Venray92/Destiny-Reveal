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


# ── format JSON baru A-M ─────────────────────────────────────────
from components import modal_detail as md  # noqa: E402

_AM = {k: f"teks {k}" for k in "ABCDEFGHIJKLM"}


def _fake_profile(entry_key, entry):
    return lambda folder: {entry_key: entry}


def test_profile_key_cocok_dengan_json(monkeypatch):
    """Key entri JSON (Weton 'Senin Legi', Numerologi '5', dst) harus cocok sama hasil engine."""
    for s, folder in md._PROFILE_FOLDER.items():
        raw = compute_raw_result(s, LD)
        key = md._profile_key(s, raw)
        assert key in md._profile_json(folder), (s, key)


def test_format_baru_am_dipakai_sendirian(monkeypatch):
    raw = compute_raw_result("Zodiak", LD)
    entry = {"sections": {"free": {"siapa_kamu": "TEASER FREE"}, **_AM}}
    monkeypatch.setattr(md, "_profile_json", _fake_profile(raw["sign"], entry))
    d = md.build_detail("Zodiak", raw)
    assert [sec[2] for sec in d["sections"]] == [[f"teks {k}"] for k in "ABCDEF"]
    assert "TEASER FREE" not in str(d["sections"])


def test_format_baru_am_non_zodiak(monkeypatch):
    raw = compute_raw_result("Shio", LD)
    monkeypatch.setattr(md, "_profile_json", _fake_profile(raw["shio"], {"sections": {"free": {}, **_AM}}))
    d = md.build_detail("Shio", raw)
    assert [sec[2] for sec in d["sections"]] == [[f"teks {k}"] for k in "ABCDEF"]


def test_format_lama_non_zodiak_tidak_berubah(monkeypatch):
    """JSON format lama (free/paid/deep) buat sistem selain Zodiak tetap diabaikan."""
    raw = compute_raw_result("Shio", LD)
    monkeypatch.setattr(md, "_profile_json", lambda folder: {})  # tanpa profil = kamus Python doang
    before = md.build_detail("Shio", raw)["sections"]
    old = {"sections": {"free": {"siapa_kamu": "LAMA"}, "paid": {"karir": "LAMA"}, "deep": {"blindspot": "LAMA"}}}
    monkeypatch.setattr(md, "_profile_json", _fake_profile(raw["shio"], old))
    assert md.build_detail("Shio", raw)["sections"] == before


def test_am_sebagian_fallback_ke_key_lama(monkeypatch):
    """Kalau cuma A-C yang terisi, section D-F jatuh ke key lama / kamus Python."""
    raw = compute_raw_result("Zodiak", LD)
    entry = {"sections": {"free": {}, "A": "teks A", "B": "teks B", "C": "teks C"}}
    monkeypatch.setattr(md, "_profile_json", _fake_profile(raw["sign"], entry))
    secs = md.build_detail("Zodiak", raw)["sections"]
    assert [secs[i][2] for i in range(3)] == [["teks A"], ["teks B"], ["teks C"]]
    assert secs[3][2] and secs[3][2] != ["teks D"]


# ── G-M (Analisis Mendalam) ──────────────────────────────────────
def test_deep_gm_tampil_urut(monkeypatch):
    raw = compute_raw_result("Zodiak", LD)
    entry = {"sections": {"free": {}, **_AM}}
    monkeypatch.setattr(md, "_profile_json", _fake_profile(raw["sign"], entry))
    d = md.build_detail("Zodiak", raw)
    assert [x[2] for x in d["deep"]] == [[f"teks {k}"] for k in "GHIJKLM"]
    assert len(d["sections"]) == 6
    txt = md._plain_text("Zodiak Barat", d)
    assert "ANALISIS MENDALAM" in txt and "teks M" in txt


def test_deep_kosong_kalau_format_lama(monkeypatch):
    raw = compute_raw_result("Shio", LD)
    monkeypatch.setattr(md, "_profile_json", lambda folder: {})
    assert md.build_detail("Shio", raw)["deep"] == []
    entry = {"sections": {"free": {}, "A": "a", "G": "g"}}
    monkeypatch.setattr(md, "_profile_json", _fake_profile(raw["shio"], entry))
    assert [x[2] for x in md.build_detail("Shio", raw)["deep"]] == [["g"]]


def test_build_detail_combo_zodiak_dan_numerologi():
    from components.modal_detail import _plain_text, build_detail
    d = build_detail("Zodiak", {"sign": "Leo", "element": "Api", "modality": "Fixed", "ruling_planet": "Matahari",
                                 "moon_sign": "Gemini"})
    assert [b["title"] for b in d["combo"]][0] == "Matahari di Leo × Bulan di Gemini"
    assert ("Bulan", "Gemini") in d["params"] and "PERPADUAN VARIABEL" in _plain_text("Zodiak", d)
    tanpa = build_detail("Zodiak", {"sign": "Leo", "element": "Api", "modality": "Fixed", "ruling_planet": "Matahari"})
    assert tanpa["combo"] == [] and "PERPADUAN VARIABEL" not in _plain_text("Zodiak", tanpa)
    n = build_detail("Numerologi", {"life_path": 7, "expression": 3, "soul_urge": 9, "personality": 6, "birthday": 1})
    assert len(n["combo"]) == 3
    assert build_detail("Weton", {"hari": "Senin", "pasaran": "Legi", "neptu": 9,
                                   "pancasuda": {"nama": "Sri", "arti": "x"}})["combo"] == []
