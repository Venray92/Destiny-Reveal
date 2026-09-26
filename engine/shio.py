"""
Engine: Shio (Astrologi Tiongkok)
Menentukan shio dari tanggal lahir. Pergantian tahun shio mengikuti
tanggal Imlek (Tahun Baru Cina) yang bergerak tiap tahun (sekitar akhir
Januari - pertengahan Februari) — BUKAN 1 Januari. Orang yang lahir
sebelum tanggal Imlek di tahun kalender itu masih kena shio tahun
sebelumnya.

Sumber tanggal Imlek 1945-2020: themalatree.com/chinese-new-year-dates-1930-to-2030
(dicek silang lewat rumus siklus 12 tahun di bawah — semua entri yang
dites cocok, termasuk 1945=Ayam, 1992=Monyet, 1996=Tikus, 2020=Tikus).

Kalau tanggal lahir di luar rentang 1945-2020, dilempar ValueError
(sengaja, bukan ditebak/diekstrapolasi) — tambahkan dulu tanggal Imleknya
di _TANGGAL_IMLEK kalau butuh cover tahun di luar rentang ini.

Scope saat ini: nama shio aja (Tikus, Kerbau, dst). BELUM termasuk elemen
Wu Xing (Kayu/Api/Tanah/Logam/Air, siklus 2 tahun) — gambar kartu yang
sudah ada juga cuma dibedakan per-hewan, bukan per-elemen.
"""

from datetime import date

# (bulan, tanggal) Imlek per tahun, 1945-2020.
_TANGGAL_IMLEK = {
    1945: (2, 13), 1946: (2, 1), 1947: (1, 22), 1948: (2, 10), 1949: (1, 29),
    1950: (2, 17), 1951: (2, 6), 1952: (1, 27), 1953: (2, 14), 1954: (2, 3),
    1955: (1, 24), 1956: (2, 12), 1957: (1, 31), 1958: (2, 18), 1959: (2, 8),
    1960: (1, 28), 1961: (2, 15), 1962: (2, 5), 1963: (1, 25), 1964: (2, 13),
    1965: (2, 2), 1966: (1, 21), 1967: (2, 9), 1968: (1, 30), 1969: (2, 17),
    1970: (2, 6), 1971: (1, 27), 1972: (2, 15), 1973: (2, 3), 1974: (1, 23),
    1975: (2, 11), 1976: (1, 31), 1977: (2, 18), 1978: (2, 7), 1979: (1, 28),
    1980: (2, 16), 1981: (2, 5), 1982: (1, 25), 1983: (2, 13), 1984: (2, 2),
    1985: (2, 20), 1986: (2, 9), 1987: (1, 29), 1988: (2, 17), 1989: (2, 6),
    1990: (1, 27), 1991: (2, 15), 1992: (2, 4), 1993: (1, 23), 1994: (2, 10),
    1995: (1, 31), 1996: (2, 19), 1997: (2, 7), 1998: (1, 28), 1999: (2, 16),
    2000: (2, 5), 2001: (1, 24), 2002: (2, 12), 2003: (2, 1), 2004: (1, 22),
    2005: (2, 9), 2006: (1, 29), 2007: (2, 18), 2008: (2, 7), 2009: (1, 26),
    2010: (2, 14), 2011: (2, 3), 2012: (1, 23), 2013: (2, 10), 2014: (1, 31),
    2015: (2, 19), 2016: (2, 8), 2017: (1, 28), 2018: (2, 16), 2019: (2, 5),
    2020: (1, 25),
}

_URUTAN_SHIO = [
    "Tikus", "Kerbau", "Macan", "Kelinci", "Naga", "Ular",
    "Kuda", "Kambing", "Monyet", "Ayam", "Anjing", "Babi",
]

_TAHUN_MIN = min(_TANGGAL_IMLEK)
_TAHUN_MAX = max(_TANGGAL_IMLEK)


def _shio_dari_tahun(tahun: int) -> str:
    # 1900 = Tikus. Tervalidasi lewat tabel Imlek di atas (1996 & 1984 &
    # 1948 = Tikus, 1992 = Monyet, 1985 = Kerbau — semua konsisten dengan
    # rumus modulo ini).
    return _URUTAN_SHIO[(tahun - 1900) % 12]


def hitung_shio(tanggal_lahir: date) -> dict:
    """
    Args:
        tanggal_lahir (date): tanggal lahir user

    Returns:
        dict: {"shio": str}

    Raises:
        ValueError: kalau tahun lahir di luar rentang data Imlek yang
        tersedia (1945-2020).
    """
    tahun = tanggal_lahir.year
    if not (_TAHUN_MIN <= tahun <= _TAHUN_MAX):
        raise ValueError(
            f"Tahun {tahun} di luar rentang data Imlek yang tersedia "
            f"({_TAHUN_MIN}-{_TAHUN_MAX}). Tambahkan dulu tanggal Imleknya "
            "di _TANGGAL_IMLEK sebelum bisa dipakai untuk tahun ini."
        )

    bulan_imlek, tanggal_imlek = _TANGGAL_IMLEK[tahun]
    sudah_lewat_imlek = (tanggal_lahir.month, tanggal_lahir.day) >= (bulan_imlek, tanggal_imlek)

    tahun_shio = tahun if sudah_lewat_imlek else tahun - 1
    return {"shio": _shio_dari_tahun(tahun_shio)}
