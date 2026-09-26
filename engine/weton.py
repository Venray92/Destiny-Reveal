"""
Engine: Weton (Primbon Jawa)
Menghitung hari (siklus 7 hari) + pasaran (siklus 5 hari Jawa) + neptu
dari tanggal lahir Masehi.

Pasaran dihitung dari selisih hari terhadap tanggal ACUAN yang sudah
divalidasi lewat sumber independen: 17 Agustus 1945 = Jumat Legi, neptu
11 (Jumat=6 + Legi=5). Lihat progress-notes.md untuk sumbernya.
"""

from datetime import date

_HARI = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
_NEPTU_HARI = {
    "Minggu": 5, "Senin": 4, "Selasa": 3, "Rabu": 7,
    "Kamis": 8, "Jumat": 6, "Sabtu": 9,
}
_PASARAN = ["Legi", "Pahing", "Pon", "Wage", "Kliwon"]
_NEPTU_PASARAN = {"Legi": 5, "Pahing": 9, "Pon": 7, "Wage": 4, "Kliwon": 8}

# Tanggal acuan tervalidasi: 17 Agustus 1945 = Jumat Legi.
_ACUAN_TANGGAL = date(1945, 8, 17)
_ACUAN_PASARAN_INDEX = _PASARAN.index("Legi")  # = 0


def hitung_weton(tanggal_lahir: date) -> dict:
    """
    Args:
        tanggal_lahir (date): tanggal lahir user

    Returns:
        dict: {"hari": str, "pasaran": str, "neptu": int}
    """
    # Python: Senin=0 ... Minggu=6 -- urutannya sudah cocok sama _HARI.
    hari = _HARI[tanggal_lahir.weekday()]

    selisih_hari = (tanggal_lahir - _ACUAN_TANGGAL).days
    pasaran_index = (_ACUAN_PASARAN_INDEX + selisih_hari) % 5
    pasaran = _PASARAN[pasaran_index]

    neptu = _NEPTU_HARI[hari] + _NEPTU_PASARAN[pasaran]

    return {"hari": hari, "pasaran": pasaran, "neptu": neptu}
