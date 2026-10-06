"""
Helper kalender Tionghoa untuk data periodik Shio (tanpa library eksternal).

- Pilar hari : siklus 60 hari dari nomor hari Julian (jangkar: 2000-01-01 = Wu-Wu / 戊午).
- Elemen hari: dari batang langit pilar hari (Jia/Yi kayu, Bing/Ding api, Wu/Ji tanah, Geng/Xin logam, Ren/Gui air).
- Bulan Tionghoa: ganti di tiap "jie" (solar term), ditentukan dari bujur Matahari. Bulan Macan mulai di 315 derajat (Lichun).
Divalidasi terhadap sxtwl di tests/test_periodic.py.
"""

from engine.astro_lite import bujur_matahari, tengah_hari_utc

SHIO_URUT = ["tikus", "kerbau", "macan", "kelinci", "naga", "ular",
             "kuda", "kambing", "monyet", "ayam", "anjing", "babi"]
ELEMEN_BATANG = ["kayu", "kayu", "api", "api", "tanah", "tanah", "logam", "logam", "air", "air"]


def pilar_hari(tgl):
    """(indeks batang 0-9, indeks cabang 0-11) pilar hari untuk tanggal `tgl` (date). 0 = Jia / Zi."""
    idx = (tgl.toordinal() + 1721474) % 60  # = (JDN + 49) % 60
    return idx % 10, idx % 12


def elemen_hari(tgl):
    return ELEMEN_BATANG[pilar_hari(tgl)[0]]


def cabang_bulan(tgl):
    """Indeks cabang bulan Tionghoa (0 = Zi/Tikus ... 11 = Hai/Babi) pada tengah hari WIB tanggal `tgl`."""
    lon = bujur_matahari(tengah_hari_utc(tgl))
    return (int(((lon - 315.0) % 360.0) // 30) + 2) % 12


def shio_bulan(tgl):
    return SHIO_URUT[cabang_bulan(tgl)]
