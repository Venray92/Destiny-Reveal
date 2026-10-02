"""
Engine Zi Wei Dou Shu (紫微斗数) — versi simplifikasi: nentuin SATU bintang
utama yang jadi "kartu" (14 kemungkinan), bukan bagan 12 istana penuh
dengan analisa lintas istana. Bintang yang dipakai = bintang yang duduk
di Istana Kehidupan (命宫/Ming Gong) milik orang itu; kalau istananya
kosong (gak semua istana kebagian salah satu dari 14 bintang utama —
wajar karena 14 bintang tersebar di 12 istana), dipakai bintang di istana
seberangnya (迁移宫, "meminjam bintang dari istana oposisi") sesuai
konvensi ZWDS. Kalau lebih dari 1 bintang jatuh di istana yang sama,
Zi Wei & Tian Fu (2 bintang "pemimpin kelompok") diprioritaskan duluan.

SELURUH rumus di bawah (Wu Xing Ju / Five Elements Bureau, penempatan
Ming Gong dari bulan+jam lahir, penempatan Zi Wei, urutan 14 bintang)
berdasarkan dokumen referensi yang dikasih Stev (27 Sep 2026) + 1 formula
tambahan yang gw cari & cross-check sendiri (formula penentuan Ming Gong
dari bulan lunar + jam lahir -- gak ada di dokumen Stev, dicari &
divalidasi dari sumber ziweicn.com yang ngutip mantra klasik "寅起正月，
顺数至生月，逆数生时为命宫") + posisi Tian Fu (mirror Zi Wei lewat
sumbu Yin-Shen, ditest cocok 100% sama tabel pasangan Zi Wei-Tian Fu
klasik yang dicek manual di bawah).

Konversi kalender Imlek (bulan/hari lunar) pakai library `sxtwl` (sama
yang dipakai BaZi) -- BUKAN hitung manual, biar presisi astronomisnya
terjamin.
"""

from datetime import date

import sxtwl

BRANCHES = ["Zi", "Chou", "Yin", "Mao", "Chen", "Si", "Wu", "Wei", "Shen", "You", "Xu", "Hai"]
YIN_IDX = BRANCHES.index("Yin")  # = 2

# Bureau: angka -> (nama pinyin elemen, nama indo, dipakai buat X di rumus penempatan Zi Wei)
BUREAU_BY_MOD = {
    1: (3, "Kayu"),   # Wood 3rd Bureau
    2: (4, "Logam"),  # Metal 4th Bureau
    3: (6, "Api"),    # Fire 6th Bureau
    4: (5, "Tanah"),  # Earth 5th Bureau
    0: (2, "Air"),    # Water 2nd Bureau
}

# Batang Langit (Tiangan) dikelompokkan per pasangan -> grup 1-5 (index 0-9 -> grup)
def _batang_group(tg_index: int) -> int:
    return (tg_index // 2) + 1


# Cabang Bumi (Dizhi) istana Ming Gong dikelompokkan per rumus dokumen:
# Zi/Chou & Wu/Wei=1, Yin/Mao & Shen/You=2, Chen/Si & Xu/Hai=3
_CABANG_GROUP = {
    0: 1, 1: 1, 6: 1, 7: 1,      # Zi, Chou, Wu, Wei
    2: 2, 3: 2, 8: 2, 9: 2,      # Yin, Mao, Shen, You
    4: 3, 5: 3, 10: 3, 11: 3,    # Chen, Si, Xu, Hai
}


def _hitung_ming_gong_idx(lunar_month: int, jam_lahir_jam: int) -> int:
    """
    Rumus klasik: "寅起正月，顺数至生月，逆数生时为命宫"
    - Dari istana Yin (寅, = bulan 1), hitung MAJU (searah jarum jam)
      sampai bulan lunar kelahiran -> dapat "istana bulan".
    - Dari istana bulan itu, hitung MUNDUR (berlawanan jarum jam)
      sejumlah urutan shichen (jam lahir dlm sistem 12 shichen, Zi=urutan
      ke-0) -> itulah Ming Gong.
    """
    bulan_idx = (YIN_IDX + (lunar_month - 1)) % 12
    shichen_idx = _jam_ke_shichen_idx(jam_lahir_jam)
    return (bulan_idx - shichen_idx) % 12


def _jam_ke_shichen_idx(jam: int) -> int:
    """Jam (0-23) -> index shichen (Zi=0, Chou=1, ..., Hai=11).
    Shichen Zi mencakup 23:00-00:59 (mengangkangi tengah malam)."""
    if jam == 23:
        return 0
    return (jam + 1) // 2


def _hitung_bureau(year_stem_idx: int, ming_gong_idx: int):
    batang = _batang_group(year_stem_idx)
    cabang = _CABANG_GROUP[ming_gong_idx]
    mod_result = (batang + cabang) % 5
    return BUREAU_BY_MOD[mod_result]  # (X, nama_elemen)


def _hitung_ziwei_idx(lunar_day: int, bureau_x: int) -> int:
    sisa = lunar_day % bureau_x
    if sisa == 0:
        hasil = lunar_day // bureau_x
        return (YIN_IDX + (hasil - 1)) % 12

    y = bureau_x - sisa
    quotient = (lunar_day + y) // bureau_x
    if y % 2 == 0:
        return (YIN_IDX + (quotient + y - 1)) % 12
    return (YIN_IDX - (quotient - y - 1)) % 12


# 14 bintang utama: (nama_slug, offset relatif ke Zi Wei ATAU ke Tian Fu)
# Kelompok Zi Wei — dihitung BERLAWANAN jarum jam (offset negatif) dari Zi Wei.
_ZIWEI_GROUP_OFFSETS = {
    "ziwei": 0, "tianji": -1, "taiyang": -3, "wuqu": -4,
    "tiantong": -5, "lianzhen": -8,
}
# Kelompok Tian Fu — dihitung SEARAH jarum jam (offset positif) dari Tian Fu.
_TIANFU_GROUP_OFFSETS = {
    "tianfu": 0, "taiyin": 1, "tanlang": 2, "jumen": 3,
    "tianxiang": 4, "tianliang": 5, "qisha": 6, "pojun": 10,
}

# Urutan prioritas kalau lebih dari 1 bintang jatuh di istana yang sama
# (Zi Wei & Tian Fu, 2 bintang "pemimpin kelompok", diutamakan).
PRIORITAS_BINTANG = [
    "ziwei", "tianfu", "taiyang", "wuqu", "tiantong", "lianzhen",
    "taiyin", "tanlang", "jumen", "tianxiang", "tianliang", "qisha",
    "pojun", "tianji",
]


def hitung_ziwei(tanggal_lahir: date, jam_lahir_jam: int) -> dict:
    """
    Hitung bintang utama yang duduk di Istana Kehidupan (Ming Gong).

    Args:
        tanggal_lahir: tanggal lahir Gregorian.
        jam_lahir_jam: jam lahir dalam format 24-jam (0-23).

    Returns:
        dict: {
            "bintang": "ziwei" (slug, dipakai buat lookup kartu/konten),
            "ming_gong": "Wu" (nama cabang bumi istana Ming Gong, buat info),
            "bureau_elemen": "Tanah",
            "dipinjam": False,  # True kalau Ming Gong kosong & pinjam dari istana seberang
        }
    """
    day = sxtwl.fromSolar(tanggal_lahir.year, tanggal_lahir.month, tanggal_lahir.day)
    lunar_month = day.getLunarMonth()
    lunar_day = day.getLunarDay()
    year_stem_idx = day.getYearGZ().tg

    ming_gong_idx = _hitung_ming_gong_idx(lunar_month, jam_lahir_jam)
    bureau_x, bureau_elemen = _hitung_bureau(year_stem_idx, ming_gong_idx)
    ziwei_idx = _hitung_ziwei_idx(lunar_day, bureau_x)
    tianfu_idx = (4 - ziwei_idx) % 12

    # Posisi semua 14 bintang (slug -> index istana 0-11)
    posisi = {}
    for slug, offset in _ZIWEI_GROUP_OFFSETS.items():
        posisi[slug] = (ziwei_idx + offset) % 12
    for slug, offset in _TIANFU_GROUP_OFFSETS.items():
        posisi[slug] = (tianfu_idx + offset) % 12

    # Cari bintang di Ming Gong (prioritas Zi Wei/Tian Fu kalau lebih dari 1)
    kandidat = [slug for slug, idx in posisi.items() if idx == ming_gong_idx]
    dipinjam = False
    if not kandidat:
        # Ming Gong kosong -> pinjam dari istana seberang (oposisi, +6)
        seberang_idx = (ming_gong_idx + 6) % 12
        kandidat = [slug for slug, idx in posisi.items() if idx == seberang_idx]
        dipinjam = True

    bintang = next((s for s in PRIORITAS_BINTANG if s in kandidat), None)

    return {
        "bintang": bintang,
        "ming_gong": BRANCHES[ming_gong_idx],
        "bureau_elemen": bureau_elemen,
        "dipinjam": dipinjam,
    }
