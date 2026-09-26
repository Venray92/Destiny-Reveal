"""
Konfigurasi global sementara buat tahap development/testing.

TESTING_MODE = True selama fase ini:
- views/reveal_yourself.py: langkah "Verifikasi Email" & "Pilih Fokus
  Eksplorasi" tetap DITAMPILKAN visualnya, TAPI tidak memblokir user buat
  lanjut ke "Mulai Proses Reveal" (email boleh kosong, mode otomatis
  ke-default "Instan" tanpa harus diklik manual — karena baru mode ini
  yang enginenya beneran lengkap).
- views/loadingpage.py: floating window di akhir proses loading BUKAN
  payment gateway asli, cuma 1 tombol "Bypass Payment" buat lanjut ke
  halaman hasil (belum ada integrasi Midtrans/Xendit).

Matikan (set ke False) begitu OTP email asli, mode Mendalam/Lengkap, dan
payment gateway beneran sudah siap dipasang — jangan hapus flag-nya,
cukup ganti nilainya, biar gampang dites bolak-balik.
"""

TESTING_MODE = True
