"""
Engine: Zodiak Barat
Menentukan zodiak + elemen + modality + planet penguasa dari tanggal &
bulan lahir.
"""

from datetime import date

# (bulan_mulai, tanggal_mulai, nama, elemen, modality, planet_penguasa) — urut dari 21 Maret
_RENTANG_ZODIAK = [
    ((3, 21), (4, 19), "Aries", "Api", "Kardinal", "Mars"),
    ((4, 20), (5, 20), "Taurus", "Tanah", "Fixed", "Venus"),
    ((5, 21), (6, 20), "Gemini", "Udara", "Mutable", "Merkurius"),
    ((6, 21), (7, 22), "Cancer", "Air", "Kardinal", "Bulan"),
    ((7, 23), (8, 22), "Leo", "Api", "Fixed", "Matahari"),
    ((8, 23), (9, 22), "Virgo", "Tanah", "Mutable", "Merkurius"),
    ((9, 23), (10, 22), "Libra", "Udara", "Kardinal", "Venus"),
    ((10, 23), (11, 21), "Scorpio", "Air", "Fixed", "Mars/Pluto"),
    ((11, 22), (12, 21), "Sagittarius", "Api", "Mutable", "Jupiter"),
    ((12, 22), (1, 19), "Capricorn", "Tanah", "Kardinal", "Saturnus"),
    ((1, 20), (2, 18), "Aquarius", "Udara", "Fixed", "Saturnus/Uranus"),
    ((2, 19), (3, 20), "Pisces", "Air", "Mutable", "Jupiter/Neptunus"),
]


def hitung_zodiak(tanggal_lahir: date) -> dict:
    """
    Args:
        tanggal_lahir (date): tanggal lahir user

    Returns:
        dict: {"sign": str, "element": str, "modality": str, "ruling_planet": str}
    """
    md = (tanggal_lahir.month, tanggal_lahir.day)

    for mulai, akhir, nama, elemen, modality, planet in _RENTANG_ZODIAK:
        cocok = (
            mulai <= md <= akhir if mulai <= akhir
            # Rentang yang melewati pergantian tahun (Capricorn: 22 Des - 19 Jan)
            else md >= mulai or md <= akhir
        )
        if cocok:
            return {
                "sign": nama, "element": elemen,
                "modality": modality, "ruling_planet": planet,
            }

    raise ValueError(f"Tanggal tidak valid untuk pencocokan zodiak: {tanggal_lahir}")
