"""
Loader profil statis 5 sistem Mode 1 dari JSON baru (satu-satunya sumber teks profil).

File: content/interpretations/<sistem>/...  (lihat _FILES)
Bentuk entri: {"sections": {"free": {siapa_kamu, atribut_1, atribut_2, quote}, "A".."M": teks}, ...meta}
  A-F = Mode 1 (Cetak Biru), G-M = Deep Blueprint.

Kalau entri belum ada di JSON (mis. Weton baru 5 dari 35), get_profile() return None dan pemanggil
boleh jatuh ke kamus lama selama ALLOW_LEGACY_FALLBACK = True.
"""

from pathlib import Path

from content import safe_json

_BASE = Path(__file__).resolve().parent / "interpretations"
_FILES = {
    "Zodiak": "zodiak/zodiak_profile.json",
    "Shio": "shio/shio_profile.json",
    "Weton": "weton/weton_profile.json",
    "Numerologi": "numerologi/numerologi_profile.json",
    "Matrix Destiny": "matrix_destiny/matrix_destiny.json",
}
SYSTEMS = tuple(_FILES)
ALLOW_LEGACY_FALLBACK = True  # False = entri yang belum ada di JSON baru tampil kosong, bukan dari kamus lama
HURUF = tuple("ABCDEFGHIJKLM")
MODE1 = HURUF[:6]  # A-F


def _data(system):
    """{key: entri} untuk satu sistem. Dipisah supaya gampang di-monkeypatch di tes."""
    f = _FILES.get(system)
    d = safe_json.load(_BASE / f) if f else None
    return (d or {}).get("data") or {}


def profile_key(system, raw):
    """Key entri JSON dari hasil engine (raw), atau None kalau raw belum lengkap."""
    raw = raw or {}
    if system == "Zodiak":
        return raw.get("sign")
    if system == "Shio":
        return raw.get("shio")
    if system == "Weton":
        h, p = raw.get("hari"), raw.get("pasaran")
        return f"{h} {p}" if h and p else None
    if system == "Numerologi":
        lp = raw.get("life_path")
        return str(lp) if lp is not None else None
    if system == "Matrix Destiny":
        t = raw.get("titik_inti")
        return str(t) if t is not None else None
    return None


def get_profile(system, raw):
    """Return {"key", "free": {...}, "sections": {"A": teks, ...}, "meta": {...}} atau None."""
    key = profile_key(system, raw)
    entry = _data(system).get(key) if key else None
    if not isinstance(entry, dict):
        return None
    sec = entry.get("sections") or {}
    free = sec.get("free") if isinstance(sec.get("free"), dict) else {}
    teks = {h: sec[h].strip() for h in HURUF if isinstance(sec.get(h), str) and sec[h].strip()}
    if not teks and not free:
        return None
    meta = {k: v for k, v in entry.items() if k != "sections"}
    return {"key": key, "free": free, "sections": teks, "meta": meta}


def pertama_kalimat(teks, batas=170):
    """Kalimat pertama (dipotong rapi kalau kepanjangan)."""
    teks = (teks or "").strip()
    cut = teks.find(". ")
    out = teks if cut == -1 else teks[: cut + 1]
    return out if len(out) <= batas else out[: batas - 1].rstrip() + "…"


def kunci_harapan(system):
    """Semua key entri yang HARUS ada di JSON profil sistem ini."""
    if system == "Zodiak":
        return ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio",
                "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
    if system == "Shio":
        return ["Tikus", "Kerbau", "Macan", "Kelinci", "Naga", "Ular", "Kuda", "Kambing", "Monyet", "Ayam", "Anjing", "Babi"]
    if system == "Weton":
        return [f"{h} {p}" for h in ("Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu")
                for p in ("Legi", "Pahing", "Pon", "Wage", "Kliwon")]
    if system == "Numerologi":
        return [str(n) for n in (1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33)]
    return [str(n) for n in range(1, 23)]  # Matrix Destiny


def audit(system):
    """Cek kelengkapan satu sistem. Return list pesan masalah (kosong = lolos)."""
    data = _data(system)
    if not data:
        return [f"{system}: file kosong / tidak terbaca"]
    errs = [f"{system}.{k}: entri tidak ada" for k in kunci_harapan(system) if k not in data]
    for key, e in data.items():
        sec = (e or {}).get("sections") or {}
        free = sec.get("free") or {}
        errs += [f"{system}.{key}.free.{f}: kosong" for f in ("siapa_kamu", "atribut_1", "atribut_2", "quote")
                 if not str(free.get(f, "")).strip()]
        errs += [f"{system}.{key}.{h}: kosong" for h in HURUF if not str(sec.get(h, "")).strip()]
    return errs
