"""
Engine: Numerologi (Pythagoras)

Life Path Number dari tanggal lahir: reduce tanggal, bulan, tahun
MASING-MASING dulu ke 1 digit (kecuali ketemu Master Number 11/22/33 di
tengah jalan -- berhenti di situ, jangan direduce lebih lanjut), baru
dijumlah semuanya dan direduce lagi pakai aturan yang sama.

Numerologi lengkap (butuh nama lahir lengkap, lihat views/loadingpage.py
field "nama_lengkap"):
- Expression/Destiny Number: dari SEMUA huruf nama lengkap.
- Soul Urge Number: dari huruf VOKAL (A E I O U) saja.
- Personality Number: dari huruf KONSONAN saja.
- Birthday Number: dari tanggal lahir aja (trivial), direduce tapi tetap
  hormatin Master Number.

Simplifikasi yang disengaja: huruf "Y" selalu dihitung sebagai konsonan.
Sebagian sistem numerologi memperlakukan Y kondisional (vokal kalau nggak
ada vokal lain di satu suku kata) -- itu belum diimplementasi di sini
biar tetap sederhana & konsisten, bisa direvisi kalau diminta.
"""

from datetime import date

_MASTER_NUMBERS = {11, 22, 33}

# Tabel huruf -> angka Pythagoras standar.
_LETTER_ROWS = ["AJS", "BKT", "CLU", "DMV", "ENW", "FOX", "GPY", "HQZ", "IR"]
_LETTER_VALUES = {
    huruf: nilai
    for nilai, baris in enumerate(_LETTER_ROWS, start=1)
    for huruf in baris
}
_VOKAL = set("AEIOU")


def _reduce(n: int) -> int:
    while n > 9 and n not in _MASTER_NUMBERS:
        n = sum(int(d) for d in str(n))
    return n


def _huruf_saja(nama: str) -> str:
    return "".join(ch for ch in nama.upper() if ch.isalpha())


def hitung_life_path(tanggal_lahir: date) -> int:
    """
    Args:
        tanggal_lahir (date): tanggal lahir user

    Returns:
        int: life path number (1-9, atau master number 11/22/33)
    """
    tgl = _reduce(tanggal_lahir.day)
    bln = _reduce(tanggal_lahir.month)
    thn = _reduce(sum(int(d) for d in str(tanggal_lahir.year)))
    return _reduce(tgl + bln + thn)


def hitung_expression_number(nama_lengkap: str) -> int:
    """Expression/Destiny Number: jumlah nilai SEMUA huruf nama lengkap."""
    huruf = _huruf_saja(nama_lengkap)
    total = sum(_LETTER_VALUES[ch] for ch in huruf)
    return _reduce(total)


def hitung_soul_urge_number(nama_lengkap: str) -> int:
    """Soul Urge Number: jumlah nilai huruf VOKAL (A E I O U) saja."""
    huruf = _huruf_saja(nama_lengkap)
    total = sum(_LETTER_VALUES[ch] for ch in huruf if ch in _VOKAL)
    return _reduce(total)


def hitung_personality_number(nama_lengkap: str) -> int:
    """Personality Number: jumlah nilai huruf KONSONAN saja."""
    huruf = _huruf_saja(nama_lengkap)
    total = sum(_LETTER_VALUES[ch] for ch in huruf if ch not in _VOKAL)
    return _reduce(total)


def hitung_birthday_number(tanggal_lahir: date) -> int:
    """Birthday Number: langsung dari tanggal lahir, direduce (hormat Master Number)."""
    return _reduce(tanggal_lahir.day)


def hitung_numerologi_lengkap(tanggal_lahir: date, nama_lengkap: str) -> dict:
    """
    Gabungan 5 angka inti numerologi.

    Returns:
        dict: {"life_path", "expression", "soul_urge", "personality", "birthday"}
    """
    return {
        "life_path": hitung_life_path(tanggal_lahir),
        "expression": hitung_expression_number(nama_lengkap),
        "soul_urge": hitung_soul_urge_number(nama_lengkap),
        "personality": hitung_personality_number(nama_lengkap),
        "birthday": hitung_birthday_number(tanggal_lahir),
    }
