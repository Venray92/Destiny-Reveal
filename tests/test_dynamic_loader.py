from datetime import datetime

from content import dynamic_loader as dl
from engine.rotation import WIB

HARI_INI = datetime(2026, 10, 3, 9, 0, tzinfo=WIB)


BULAN = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September",
         "Oktober", "November", "Desember"]
import re
import pytest

HARI = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
KEYS = {
    "Shio": ["Tikus", "Kerbau", "Macan", "Kelinci", "Naga", "Ular", "Kuda", "Kambing", "Monyet", "Ayam", "Anjing", "Babi"],
    "Numerologi": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "11", "22", "33"],
    "Weton": [f"{h} {p}" for h in HARI for p in ["Legi", "Pahing", "Pon", "Wage", "Kliwon"]],
}
BANNED = {"Shio": r"elemen|kayu|logam", "Weton": r"pancasuda", "Numerologi": r"(?!x)x"}
SIGNS = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio",
         "Sagittarius", "Capricorn", "Aquarius", "Pisces"]


def test_12_zodiak_lolos_validasi_dan_kuota_produksi():
    for kind in ("daily", "weekly", "monthly"):
        assert dl.validate("Zodiak", kind, dl.QUOTA_PRODUKSI if kind == "daily" else None) == []
        assert set(dl._load("Zodiak", kind)) == set(SIGNS)


def test_kuota_daily_per_zodiak():
    for sg in SIGNS:
        e = dl._load("Zodiak", "daily")[sg]
        assert {k: len(v) for k, v in e.items()} == dl.QUOTA_PRODUKSI, sg


def test_monthly_punya_tanggal_penting_dan_variasi_kalimat():
    for sg in SIGNS:
        e = dl._load("Zodiak", "monthly")[sg]
        assert len(e) == 12 and all(e[str(m)]["tanggal_penting"] for m in range(1, 13)), sg
        # kerangka kalimat tidak boleh sama untuk dua bulan berurutan
        for f in ("timing", "prediksi", "saran", "peluang", "risiko"):
            awal = []
            for m in range(1, 13):
                t = e[str(m)][f]
                for b in BULAN:
                    t = t.replace(b, "B")
                awal.append(t.split()[:4])
            assert all(awal[i] != awal[i + 1] for i in range(11)), (sg, f)


def test_get_monthly_memuat_tanggal_penting():
    m = dl.get_monthly("Zodiak", "Leo", datetime(2026, 10, 3, tzinfo=WIB))
    assert m["tanggal_penting"] and "Oktober" in m["tanggal_penting"]


def test_daily_stabil_per_hari_dan_user():
    a = dl.get_daily("Zodiak", "Aries", "user1", HARI_INI)
    assert a == dl.get_daily("Zodiak", "Aries", "user1", HARI_INI)
    assert a["tanggal"] == "Sabtu, 3 Oktober 2026" and all(a[c] for c in dl.DAILY_FIELDS)


def test_daily_beda_hari_atau_user_bisa_beda():
    hasil = {dl.get_daily("Zodiak", "Aries", f"u{i}", HARI_INI)["ramalan"] for i in range(30)}
    assert len(hasil) > 1
    besok = datetime(2026, 10, 4, 0, 0, tzinfo=WIB)
    assert dl.get_daily("Zodiak", "Aries", "u1", besok)["key"] == "2026-10-04"


def test_weekly_sama_sepanjang_minggu_ganti_senin():
    sen = dl.get_weekly("Zodiak", "Aries", datetime(2026, 9, 28, 0, 0, tzinfo=WIB))
    min_ = dl.get_weekly("Zodiak", "Aries", datetime(2026, 10, 4, 23, 59, tzinfo=WIB))
    assert sen == min_ and sen["periode"] == "28 September sampai 4 Oktober 2026"
    assert dl.get_weekly("Zodiak", "Aries", datetime(2026, 10, 5, tzinfo=WIB))["key"] == "2026-10-05"


def test_monthly_ganti_tanggal_1():
    assert dl.get_monthly("Zodiak", "Aries", datetime(2026, 10, 31, 23, 59, tzinfo=WIB))["periode"] == "Oktober 2026"
    assert dl.get_monthly("Zodiak", "Aries", datetime(2026, 11, 1, tzinfo=WIB))["periode"] == "November 2026"


def test_key_atau_sistem_tidak_ada_balikin_none():
    assert dl.get_daily("Zodiak", "Naga", "u", HARI_INI) is None
    assert dl.get_weekly("Shio", "Naga Emas", HARI_INI) is None
    assert dl.get_weekly("Primbon", "X", HARI_INI) is None
    assert dl.get_monthly("Zodiak", "Naga", HARI_INI) is None


def test_validate_deteksi_kurang_dari_target():
    errs = dl.validate("Zodiak", "daily", {k: 1000 for k in dl.DAILY_FIELDS})
    assert len(errs) == 5 * 12


def test_validate_tanggal_di_luar_bulan_ditolak():
    assert dl._cek_tanggal("X", "2", "8-14 Februari untuk a, 22 ke atas untuk b") == []
    assert dl._cek_tanggal("X", "2", "8-14 Februari untuk a, 30 ke atas untuk b")
    assert dl._cek_tanggal("X", "1", "14-8 Januari untuk a, 22 ke atas untuk b")


def test_monthly_weekly_tidak_ada_teks_kembar_antar_zodiak():
    for kind in ("monthly", "weekly"):
        seen = {}
        for sg, e in dl._load("Zodiak", kind).items():
            for slot, blk in e.items():
                for f, t in blk.items():
                    assert t not in seen, (kind, sg, slot, f, seen[t])
                    seen[t] = (sg, slot, f)


def test_hindari_weekly_tanpa_titik():
    for sg, e in dl._load("Zodiak", "weekly").items():
        assert all(not b["hindari"].endswith(".") for b in e.values()), sg


@pytest.mark.parametrize("system", list(KEYS))
def test_sistem_baru_lolos_validasi_kuota_dan_key_lengkap(system):
    for kind in ("daily", "weekly", "monthly"):
        assert dl.validate(system, kind, dl.QUOTA_PRODUKSI if kind == "daily" else None) == []
        assert set(dl._load(system, kind)) == set(KEYS[system])


@pytest.mark.parametrize("system", list(KEYS))
def test_sistem_baru_struktur_weekly_monthly_dan_tanggal(system):
    for key in KEYS[system]:
        d = dl._load(system, "daily")[key]
        assert {k: len(v) for k, v in d.items()} == dl.QUOTA_PRODUKSI, key
        w = dl._load(system, "weekly")[key]
        assert set(w) == {f"week_{i}" for i in range(1, 6)}, key
        assert all(not b["hindari"].endswith(".") for b in w.values()), key
        m = dl._load(system, "monthly")[key]
        assert set(m) == {str(i) for i in range(1, 13)}, key
        assert all(m[str(i)]["tanggal_penting"] and BULAN[i - 1] in m[str(i)]["tanggal_penting"] for i in range(1, 13)), key


@pytest.mark.parametrize("system", list(KEYS))
def test_sistem_baru_variasi_kalimat_antar_bulan(system):
    for key in KEYS[system]:
        e = dl._load(system, "monthly")[key]
        for f in ("timing", "prediksi", "saran", "peluang", "risiko"):
            awal = []
            for m in range(1, 13):
                t = e[str(m)][f]
                for b in BULAN:
                    t = t.replace(b, "B")
                awal.append(t.split()[:4])
            assert all(awal[i] != awal[i + 1] for i in range(11)), (system, key, f)


@pytest.mark.parametrize("system", list(KEYS))
def test_sistem_baru_tanpa_teks_kembar_dan_kata_terlarang(system):
    for kind in ("monthly", "weekly"):
        seen = {}
        for key, e in dl._load(system, kind).items():
            for slot, blk in e.items():
                for f, t in blk.items():
                    assert t not in seen, (system, kind, key, slot, f, seen[t])
                    seen[t] = (key, slot, f)
                    assert not re.search(BANNED[system], t, re.I), (system, key, t)
    for key, e in dl._load(system, "daily").items():
        for f, items in e.items():
            if f == "warna":  # nama warna (mis. "Cokelat kayu") bukan klaim elemen
                continue
            for t in items:
                assert not re.search(BANNED[system], t, re.I), (system, key, t)
    for f in ("ramalan", "saran", "quote"):
        seen = {}
        for key, e in dl._load(system, "daily").items():
            for t in e[f]:
                assert t not in seen, (system, key, f, seen[t])
                seen[t] = key


def test_get_sistem_baru_jalan_end_to_end():
    assert dl.get_daily("Weton", "Senin Legi", "u", HARI_INI)["ramalan"]
    assert dl.get_weekly("Shio", "Tikus", HARI_INI)["prediksi"]
    assert "Oktober" in dl.get_monthly("Numerologi", "33", HARI_INI)["tanggal_penting"]
