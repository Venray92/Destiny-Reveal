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
