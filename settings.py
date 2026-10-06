"""
Konfigurasi global sementara buat tahap development/testing.

TESTING_MODE = True selama fase ini: verifikasi email & pembayaran di modal "Reveal Dirimu"
masih simulasi (belum ada Supabase / Midtrans / Xendit), jadi tidak memblokir alur.
"""

TESTING_MODE = True

# Dummy/placeholder — ganti begitu ada angka final dari Stev.
PRICE_PENDEK = 15000
PRICE_PANJANG = 29000
PRICE_UPGRADE_SELISIH = PRICE_PANJANG - PRICE_PENDEK
