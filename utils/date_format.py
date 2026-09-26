"""
Util kecil buat format tanggal jadi dd/mm/yyyy (format yang dipahami
umum di Indonesia), dipakai bareng oleh loadingpage.py dan revealpage.py
biar tampilan "data yang diinput user" konsisten di kedua halaman.
"""

BULAN_NAMES_ID = [
    "Januari", "Februari", "Maret", "April", "Mei", "Juni",
    "Juli", "Agustus", "September", "Oktober", "November", "Desember",
]


def format_tanggal_ddmmyyyy(value):
    """
    Args:
        value: objek `datetime.date`, atau None/kosong.

    Returns:
        str "05/12/1992", atau None kalau value-nya kosong (biar
        pemanggil bisa milih nggak nampilin apa-apa).
    """
    if not value:
        return None
    return f"{value.day:02d}/{value.month:02d}/{value.year}"


def format_tanggal_lengkap(value):
    """Versi lebih naratif, contoh: "5 Desember 1992" — dipakai kalau
    butuh tampilan yang lebih "manusiawi" dibanding angka doang."""
    if not value:
        return None
    return f"{value.day} {BULAN_NAMES_ID[value.month - 1]} {value.year}"
