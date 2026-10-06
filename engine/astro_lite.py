"""
Posisi Bulan & Matahari versi ringan (pure Python, tanpa swisseph / tanpa data eksternal).

Dipakai untuk kunci data periodik:
- Zodiak harian  : rumah transit Bulan terhadap tanda pengguna
- Zodiak/Weton mingguan : fase Bulan (4 kelompok)
- Zodiak bulanan : rumah transit Matahari

Metode: elemen orbit + suku gangguan utama (formula Schlyter). Akurasi Bulan sekitar 0.3 derajat,
Matahari sekitar 0.01 derajat. Cukup untuk menentukan tanda zodiak (lebar 30 derajat) dan fase.
Rumus & hasil validasi: docs/formula-notes.md#astro-lite
"""

import math
from datetime import datetime, timezone

TANDA = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio",
         "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
FASE = ("new_moon", "first_quarter", "full_moon", "third_quarter")


def _rad(x):
    return math.radians(x % 360.0)


def _hari_sejak_epoch(dt_utc):
    """Hari (pecahan) sejak 2000-01-00 0:00 UT (= 1999-12-31 0:00 UT)."""
    ref = datetime(1999, 12, 31, tzinfo=timezone.utc)
    return (dt_utc - ref).total_seconds() / 86400.0


def _matahari(d):
    """(bujur matahari sejati, anomali rata-rata matahari, bujur rata-rata matahari) dalam derajat."""
    w = 282.9404 + 4.70935e-5 * d
    e = 0.016709 - 1.151e-9 * d
    m = (356.0470 + 0.9856002585 * d) % 360.0
    e_anom = m + math.degrees(e) * math.sin(_rad(m)) * (1.0 + e * math.cos(_rad(m)))
    xv = math.cos(_rad(e_anom)) - e
    yv = math.sqrt(1.0 - e * e) * math.sin(_rad(e_anom))
    v = math.degrees(math.atan2(yv, xv))
    return (v + w) % 360.0, m, (w + m) % 360.0


def bujur_matahari(dt_utc):
    return _matahari(_hari_sejak_epoch(dt_utc))[0]


def bujur_bulan(dt_utc):
    """Bujur ekliptika tropis Bulan (derajat 0-360)."""
    d = _hari_sejak_epoch(dt_utc)
    n = 125.1228 - 0.0529538083 * d
    i = 5.1454
    w = 318.0634 + 0.1643573223 * d
    a = 60.2666
    e = 0.054900
    mm = (115.3654 + 13.0649929509 * d) % 360.0

    e_anom = mm + math.degrees(e) * math.sin(_rad(mm)) * (1.0 + e * math.cos(_rad(mm)))
    for _ in range(5):  # iterasi Kepler
        e_anom = e_anom - (e_anom - math.degrees(e) * math.sin(_rad(e_anom)) - mm) / (1.0 - e * math.cos(_rad(e_anom)))
    xv = a * (math.cos(_rad(e_anom)) - e)
    yv = a * math.sqrt(1.0 - e * e) * math.sin(_rad(e_anom))
    v = math.degrees(math.atan2(yv, xv))
    r = math.hypot(xv, yv)
    vw = v + w
    xh = r * (math.cos(_rad(n)) * math.cos(_rad(vw)) - math.sin(_rad(n)) * math.sin(_rad(vw)) * math.cos(_rad(i)))
    yh = r * (math.sin(_rad(n)) * math.cos(_rad(vw)) + math.cos(_rad(n)) * math.sin(_rad(vw)) * math.cos(_rad(i)))
    lon = math.degrees(math.atan2(yh, xh)) % 360.0

    _, ms, ls = _matahari(d)
    lm = (n + w + mm) % 360.0
    dd = lm - ls
    f = lm - n
    lon += (-1.274 * math.sin(_rad(mm - 2 * dd))
            + 0.658 * math.sin(_rad(2 * dd))
            - 0.186 * math.sin(_rad(ms))
            - 0.059 * math.sin(_rad(2 * mm - 2 * dd))
            - 0.057 * math.sin(_rad(mm - 2 * dd + ms))
            + 0.053 * math.sin(_rad(mm + 2 * dd))
            + 0.046 * math.sin(_rad(2 * dd - ms))
            + 0.041 * math.sin(_rad(mm - ms))
            - 0.035 * math.sin(_rad(dd))
            - 0.031 * math.sin(_rad(mm + ms))
            - 0.015 * math.sin(_rad(2 * f - 2 * dd))
            + 0.011 * math.sin(_rad(mm - 4 * dd)))
    return lon % 360.0


def tanda_dari_bujur(lon):
    return TANDA[int(lon % 360.0 // 30)]


def tengah_hari_utc(tgl):
    """Sampel waktu = 12:00 WIB (05:00 UTC) pada tanggal `tgl` (date)."""
    return datetime(tgl.year, tgl.month, tgl.day, 5, tzinfo=timezone.utc)


def tanda_bulan(tgl):
    """Tanda zodiak tempat Bulan berada pada tengah hari WIB tanggal `tgl`."""
    return tanda_dari_bujur(bujur_bulan(tengah_hari_utc(tgl)))


def tanda_matahari(tgl):
    return tanda_dari_bujur(bujur_matahari(tengah_hari_utc(tgl)))


def rumah(tanda_pengguna, tanda_transit):
    """Rumah (1-12) tanda_transit dihitung dari tanda_pengguna sebagai rumah ke-1 (whole sign)."""
    return (TANDA.index(tanda_transit) - TANDA.index(tanda_pengguna)) % 12 + 1


def fase_bulan(tgl):
    """4 kelompok fase pada tengah hari WIB: new_moon, first_quarter, full_moon, third_quarter.
    Elongasi (Bulan - Matahari) dibagi 4 sektor 90 derajat berpusat di 0/90/180/270."""
    t = tengah_hari_utc(tgl)
    elong = (bujur_bulan(t) - bujur_matahari(t)) % 360.0
    return FASE[int(((elong + 45.0) % 360.0) // 90)]
