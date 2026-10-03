"""
Kunci rotasi data dinamis (semua pakai WIB / UTC+7).
- Harian  : ganti jam 00:00 WIB
- Mingguan: ganti tiap Senin 00:00 WIB
- Bulanan : ganti tiap tanggal 1 00:00 WIB
Pemilihan teks pakai sha256 (bukan hash() bawaan Python yang berubah tiap proses),
jadi hasil stabil: pengguna yang sama di hari yang sama selalu dapat teks yang sama.
"""

import hashlib
from datetime import date, datetime, timedelta, timezone

WIB = timezone(timedelta(hours=7))
HARI = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
BULAN = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli",
         "Agustus", "September", "Oktober", "November", "Desember"]


def now_wib(now=None):
    """Waktu WIB. `now` opsional (untuk test); naive dianggap sudah WIB."""
    if now is None:
        return datetime.now(WIB)
    return now.astimezone(WIB) if now.tzinfo else now.replace(tzinfo=WIB)


def today_wib(now=None):
    return now_wib(now).date()


def week_start(d):
    """Tanggal Senin untuk minggu yang memuat d."""
    return d - timedelta(days=d.weekday())


def week_slot(d):
    """Slot week_1..week_5 dari Senin minggu itu (minggu ke-n dalam bulan Senin tsb)."""
    return (week_start(d).day - 1) // 7 + 1


def pick(options, *parts):
    """Pilih satu elemen deterministik dari hash(parts) % len(options)."""
    if not options:
        return None
    h = hashlib.sha256("|".join(str(p) for p in parts).encode("utf-8")).hexdigest()
    return options[int(h, 16) % len(options)]


def next_reset(kind, now=None):
    """Waktu (WIB) reset berikutnya untuk 'daily' | 'weekly' | 'monthly'. Berguna buat countdown UI."""
    n = now_wib(now)
    d = n.date()
    if kind == "daily":
        nxt = d + timedelta(days=1)
    elif kind == "weekly":
        nxt = week_start(d) + timedelta(days=7)
    elif kind == "monthly":
        nxt = date(d.year + (d.month == 12), d.month % 12 + 1, 1)
    else:
        raise ValueError(kind)
    return datetime(nxt.year, nxt.month, nxt.day, tzinfo=WIB)


def format_tanggal(d):
    return f"{HARI[d.weekday()]}, {d.day} {BULAN[d.month - 1]} {d.year}"


def format_periode_minggu(d):
    a = week_start(d)
    b = a + timedelta(days=6)
    return f"{a.day} {BULAN[a.month - 1]} sampai {b.day} {BULAN[b.month - 1]} {b.year}"
