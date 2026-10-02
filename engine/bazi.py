"""
Engine BaZi (八字) — versi simplifikasi: cuma hitung DAY MASTER (Heavenly
Stem hari lahir / 日主), bukan 4 pilar penuh (tahun/bulan/hari/jam). Day
Master ini yang jadi "kartu" utama BaZi di produk kita (10 kemungkinan:
Jia/Yi/Bing/Ding/Wu/Ji/Geng/Xin/Ren/Gui), sesuai keputusan awal biar
konsisten sama sistem lain yang berbasis tanggal lahir saja.

Kenapa cuma Day Master, bukan 4 pilar penuh + analisa elemen kuat/lemah:
- 4 pilar penuh butuh jam lahir + interpretasi elemen yang jauh lebih
  kompleks (bukan cuma "kartu tunggal"), di luar scope produk ini.
- Day Master sendiri secara tradisi emang dianggap representasi paling
  inti dari "diri sendiri" dalam BaZi, jadi tetap bermakna sebagai satu
  hasil utuh meski disederhanakan.

Perhitungan pakai library `sxtwl` (寿星天文历 - port dari kalender astronomi
Shou Xing yang dipakai luas di kalkulator BaZi/kalender Imlek Tionghoa),
BUKAN rumus manual/tabel yang kita bikin sendiri -- ini penting karena
rumus Ganzhi (60 siklus hari) butuh presisi astronomis kalender Imlek yang
gampang salah kalau dihitung manual. Sudah di-cross-check manual: batas
pergantian tahun Ganzhi memakai Li Chun (立春, awal musim semi astronomis),
BUKAN Tahun Baru Imlek -- ini sesuai konvensi BaZi yang benar (contoh:
1984-02-02, sebelum Li Chun 4 Feb 1984, masih dihitung tahun Gui-Hai/1983,
baru masuk Jia-Zi/1984 mulai 1984-02-04). Day Master sendiri (siklus 60
hari, independen dari batas tahun) tidak kena isu ini sama sekali.

Kalau nanti mau dikembangkan ke 4 pilar penuh, sxtwl sudah nyediain
getYearGZ()/getMonthGZ()/getDayGZ()/getHourGZ() semua -- tinggal pakai jam
lahir buat getHourGZ().
"""

from datetime import date

import sxtwl

# Urutan index Tiangan (Heavenly Stem) sesuai sxtwl: 0=Jia s/d 9=Gui.
# Elemen & polaritas ikut aturan baku BaZi: index genap = Yang, ganjil = Yin,
# berpasangan 2-2 per elemen (Kayu, Api, Tanah, Logam, Air).
TIANGAN = [
    {"pinyin": "jia", "hanzi": "甲", "elemen": "Kayu", "polaritas": "Yang"},
    {"pinyin": "yi", "hanzi": "乙", "elemen": "Kayu", "polaritas": "Yin"},
    {"pinyin": "bing", "hanzi": "丙", "elemen": "Api", "polaritas": "Yang"},
    {"pinyin": "ding", "hanzi": "丁", "elemen": "Api", "polaritas": "Yin"},
    {"pinyin": "wu", "hanzi": "戊", "elemen": "Tanah", "polaritas": "Yang"},
    {"pinyin": "ji", "hanzi": "己", "elemen": "Tanah", "polaritas": "Yin"},
    {"pinyin": "geng", "hanzi": "庚", "elemen": "Logam", "polaritas": "Yang"},
    {"pinyin": "xin", "hanzi": "辛", "elemen": "Logam", "polaritas": "Yin"},
    {"pinyin": "ren", "hanzi": "壬", "elemen": "Air", "polaritas": "Yang"},
    {"pinyin": "gui", "hanzi": "癸", "elemen": "Air", "polaritas": "Yin"},
]


def hitung_bazi(tanggal_lahir: date) -> dict:
    """
    Hitung Day Master (日主) dari tanggal lahir Gregorian.

    Args:
        tanggal_lahir: objek datetime.date.

    Returns:
        dict: {
            "day_master": "jia" (pinyin lowercase, dipakai jadi key lookup
                kartu/konten, sama pola kayak "sign"/"shio"/dll di sistem
                lain),
            "hanzi": "甲",
            "elemen": "Kayu",
            "polaritas": "Yang",
        }
    """
    day = sxtwl.fromSolar(tanggal_lahir.year, tanggal_lahir.month, tanggal_lahir.day)
    tg_index = day.getDayGZ().tg  # 0-9
    tg = TIANGAN[tg_index]
    return {
        "day_master": tg["pinyin"],
        "hanzi": tg["hanzi"],
        "elemen": tg["elemen"],
        "polaritas": tg["polaritas"],
    }
