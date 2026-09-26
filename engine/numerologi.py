"""
Engine: Numerologi
Life Path Number dari tanggal lahir (pola Pythagoras/Barat yang umum
dipakai): reduce tanggal, bulan, tahun MASING-MASING dulu ke 1 digit
(kecuali ketemu Master Number 11/22/33 di tengah jalan -- berhenti di
situ, jangan direduce lebih lanjut), baru dijumlah semuanya dan direduce
lagi pakai aturan yang sama.

Scope saat ini: Life Path Number aja. BELUM termasuk Expression Number
dari nama lengkap, karena alur pengambilan data user sekarang belum
nanya nama (cuma tanggal lahir) -- lihat hitung_expression_number di
bawah, masih sengaja distub sampai ada keputusan mau dipakai atau nggak.
"""

from datetime import date

_MASTER_NUMBERS = {11, 22, 33}


def _reduce(n: int) -> int:
    while n > 9 and n not in _MASTER_NUMBERS:
        n = sum(int(d) for d in str(n))
    return n


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


def hitung_expression_number(nama_lengkap: str):
    """
    BELUM DIPAKAI -- masih stub. Nunggu keputusan apakah Numerologi di
    aplikasi ini mau menggabungkan Expression Number (dari nama) atau
    cukup Life Path Number aja (dari tanggal lahir).

    Args:
        nama_lengkap (str): nama lengkap user

    Returns:
        int: expression number
    """
    raise NotImplementedError
