"""
Engine: Matrix Destiny (Peta Takdir)
Menghitung TITIK INTI (arketipe utama, skala 1-22) dari tanggal lahir.

CATATAN PENTING (sudah dibahas & jadi keputusan scope awal):
Sistem Matrix Destiny versi lengkap (kursus aslinya) punya 8 titik di
octagon (inti, sosial, fisik, spiritual, garis cinta, garis uang, ekor
karma, garis leluhur) -- TAPI rumus buat 7 titik selain titik inti beda
antar sumber/kursus, nggak ada satu versi baku yang diakui semua orang.
Karena itu ENGINE INI SENGAJA CUMA MENGHITUNG TITIK INTI DULU. 7 titik
lainnya BELUM diimplementasikan -- nunggu ada sumber/kursus spesifik yang
mau dijadikan acuan resmi.

Rumus titik inti: jumlahin SEMUA digit tanggal+bulan+tahun lahir jadi
satu, terus jumlahin terus sampai hasilnya <=22 (BUKAN direduksi sampai 1
digit kayak numerologi biasa -- kalau hasilnya 22, tetap 22).
"""

from datetime import date

JUMLAH_ARKETIPE = 22

# Nama arketipe I-XXII, cocok sama urutan file assets/cards/matrix_destiny/
# (01_the_beginner.png ... 22_the_unity.png).
NAMA_ARKETIPE = {
    1: "The Beginner", 2: "The Listener", 3: "The Creator", 4: "The Ruler",
    5: "The Teacher", 6: "The Partners", 7: "The Conqueror", 8: "The Balance",
    9: "The Hermit", 10: "The Wheel", 11: "The Brave", 12: "The Sacrifice",
    13: "The Transformation", 14: "The Alchemist", 15: "The Shadow",
    16: "The Collapse", 17: "The Hope", 18: "The Mystery", 19: "The Joy",
    20: "The Awakening", 21: "The Achievement", 22: "The Unity",
}


def _reduce_ke_1_22(n: int) -> int:
    while n > JUMLAH_ARKETIPE:
        n = sum(int(d) for d in str(n))
    return n


def hitung_matrix_destiny(tanggal_lahir: date) -> dict:
    """
    Args:
        tanggal_lahir (date): tanggal lahir user

    Returns:
        dict: {"titik_inti": int, "nama_arketipe": str}
        titik_inti dalam skala 1-22, nama_arketipe nama Inggrisnya
        (cocok sama nama file gambar kartu).
    """
    semua_digit = f"{tanggal_lahir.day}{tanggal_lahir.month}{tanggal_lahir.year}"
    total = sum(int(d) for d in semua_digit)
    titik_inti = _reduce_ke_1_22(total)
    return {"titik_inti": titik_inti, "nama_arketipe": NAMA_ARKETIPE[titik_inti]}
