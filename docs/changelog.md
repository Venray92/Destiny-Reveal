# Changelog — Destiny Reveal

## 26 Sep 2026 (malam) — Zodiak: isi diperpanjang
Isi p1/p2/p3 tiap entri Zodiak diperpanjang 2-3x lipat dari versi awal, biar laporannya terasa lebih bernilai & aplikatif, bukan cuma label singkat.

## 27 Sep 2026 — Zodiak: tambah key "domains"
Tiap entri Zodiak ditambahin key `domains` (karir, asmara, keuangan, kesehatan) — Fase A dari fitur tiering Versi Pendek/Panjang. Sengaja baru Zodiak yang diisi dulu sebagai bukti alur (mekanisme lock/unlock + expander); 4 sistem lain (Shio/Weton/Numerologi/Matrix Destiny) awalnya belum punya `domains` — bukan bug/kelupaan, itu fase berikutnya yang nyusul (udah lengkap semua sekarang).

## 28 Sep 2026 — result_builder.py: nyambungin 10 sistem sisa
Sebelumnya cuma 5 sistem lama (Zodiak/Shio/Weton/Numerologi/Matrix Destiny) yang tersambung di `content/result_builder.py`, walau kamus konten + engine buat 10 sistem lainnya (BaZi/Zi Wei/Human Design/Golongan Darah/Tarot + MBTI/Big Five/Enneagram/DISC/Love Language) udah lengkap ada di repo. Akibatnya amplop 10 sistem itu selalu jatuh ke fallback generic walau datanya udah ada. Batch ini nyambungin semuanya.

## 2 Okt 2026 — Rapihin struktur project
File interpretations yang tadinya 1 file gemuk per sistem (zodiak.py 793 baris, shio.py 938 baris, mbti.py 1193 baris, dst) dipecah jadi 1 file per entri (per sign/shio/pasaran/angka/titik), masing-masing di bawah 50 baris. Nama file `xxx__yyy.py` (double underscore) dirapihin jadi `yyy.py`. Duplikat basi (`content__result_builder.py`, `utils__card_images.py`) dihapus. File test yang nyasar di root dipindah ke `tests/`.
