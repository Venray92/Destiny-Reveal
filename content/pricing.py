"""Single source of truth harga (✨ Stardust & Rupiah). Ubah angka di sini saja."""

# ── harga fitur (✨) ──
SOLO = 200
WEEKLY = 300
MONTHLY = 600
BLUEPRINT = 800
BUNDLE_ALL = 1200      # Complete Bundle 15 sistem
BUNDLE_BIRTH = 200     # Mode 1: 5 sistem kelahiran
BUNDLE_PSY = 200       # Mode 2: 5 tes psikologi
DAILY_FULL = 50
SWAP = 50
TAROT = {3: 50, 5: 100, 10: 150}
TAROT_BUNDLE = 250
COMPAT = 100           # per sistem

# ── paket Stardust: (nama, badge, harga Rp, jumlah ✨, bonus, deskripsi) ──
COIN_PACKS = [
    ("Starter", "Coba Dulu", 10000, 120, "+20%", "Cocok untuk dicoba, bisa unlock Tarot 3 Kartu atau Ramalan Harian lengkap."),
    ("Basic", "Populer", 25000, 320, "+28%", "Pas untuk 1 Weekly Report atau 1 Solo Reveal + Tarot 5 Kartu."),
    ("Value", "Hemat", 50000, 700, "+40%", "Cukup untuk 3 Solo Reveal atau 1 Monthly Report + Tarot 3 Kartu."),
    ("Pro", "Best Value", 100000, 1500, "+50%", "Cukup untuk Complete Bundle (15 sistem) atau Deep Blueprint + Monthly Report."),
    ("Sultan", "Top Up / Hemat 60%", 200000, 3200, "+60%", "Akses luas untuk semua analisis, report, dan Tarot."),
    ("Kaisar", "Top Up / Bonus 70%", 500000, 8500, "+70%", "Paket ultimate dengan bonus maksimal untuk penggunaan jangka panjang."),
]

VIP_LIFETIME = 2499000


def fmt(n):
    """1500 -> '1.500'"""
    return f"{int(n):,}".replace(",", ".")


def rp(n):
    return "Rp " + fmt(n)


def per_coin(rupiah, coins):
    return f"Rp {int(rupiah / coins + 0.5)}/✨"


def coin(n):
    """1200 -> '1.200 ✨'"""
    return f"{fmt(n)} ✨"
