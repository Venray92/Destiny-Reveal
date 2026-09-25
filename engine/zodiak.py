"""
Engine: Zodiak Barat
Menentukan zodiak + elemen dari tanggal & bulan lahir.
"""

from datetime import date

# (bulan_mulai, tanggal_mulai, nama, elemen) — urut dari 21 Maret
_RENTANG_ZODIAK = [
    ((3, 21), (4, 19), "Aries", "Api"),
    ((4, 20), (5, 20), "Taurus", "Tanah"),
    ((5, 21), (6, 20), "Gemini", "Udara"),
    ((6, 21), (7, 22), "Cancer", "Air"),
    ((7, 23), (8, 22), "Leo", "Api"),
    ((8, 23), (9, 22), "Virgo", "Tanah"),
    ((9, 23), (10, 22), "Libra", "Udara"),
    ((10, 23), (11, 21), "Scorpio", "Air"),
    ((11, 22), (12, 21), "Sagittarius", "Api"),
    ((12, 22), (1, 19), "Capricorn", "Tanah"),
    ((1, 20), (2, 18), "Aquarius", "Udara"),
    ((2, 19), (3, 20), "Pisces", "Air"),
]


def hitung_zodiak(tanggal_lahir: date) -> dict:
    """
    Args:
        tanggal_lahir (date): tanggal lahir user

    Returns:
        dict: {"sign": str, "element": str}
    """
    md = (tanggal_lahir.month, tanggal_lahir.day)

    for mulai, akhir, nama, elemen in _RENTANG_ZODIAK:
        if mulai <= akhir:
            if mulai <= md <= akhir:
                return {"sign": nama, "element": elemen}
        else:
            # Rentang yang melewati pergantian tahun (Capricorn: 22 Des - 19 Jan)
            if md >= mulai or md <= akhir:
                return {"sign": nama, "element": elemen}

    raise ValueError(f"Tanggal tidak valid untuk pencocokan zodiak: {tanggal_lahir}")
