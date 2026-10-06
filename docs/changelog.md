# Changelog — Destiny Reveal

## 26 Sep 2026 (malam) — Zodiak: isi diperpanjang
Isi p1/p2/p3 tiap entri Zodiak diperpanjang 2-3x lipat dari versi awal, biar laporannya terasa lebih bernilai & aplikatif, bukan cuma label singkat.

## 27 Sep 2026 — Zodiak: tambah key "domains"
Tiap entri Zodiak ditambahin key `domains` (karir, asmara, keuangan, kesehatan) — Fase A dari fitur tiering Versi Pendek/Panjang. Sengaja baru Zodiak yang diisi dulu sebagai bukti alur (mekanisme lock/unlock + expander); 4 sistem lain (Shio/Weton/Numerologi/Matrix Destiny) awalnya belum punya `domains` — bukan bug/kelupaan, itu fase berikutnya yang nyusul (udah lengkap semua sekarang).

## 28 Sep 2026 — result_builder.py: nyambungin 10 sistem sisa
Sebelumnya cuma 5 sistem lama (Zodiak/Shio/Weton/Numerologi/Matrix Destiny) yang tersambung di `content/result_builder.py`, walau kamus konten + engine buat 10 sistem lainnya (BaZi/Zi Wei/Human Design/Golongan Darah/Tarot + MBTI/Big Five/Enneagram/DISC/Love Language) udah lengkap ada di repo. Akibatnya amplop 10 sistem itu selalu jatuh ke fallback generic walau datanya udah ada. Batch ini nyambungin semuanya.

## 2 Okt 2026 — Rapihin struktur project
File interpretations yang tadinya 1 file gemuk per sistem (zodiak.py 793 baris, shio.py 938 baris, mbti.py 1193 baris, dst) dipecah jadi 1 file per entri (per sign/shio/pasaran/angka/titik), masing-masing di bawah 50 baris. Nama file `xxx__yyy.py` (double underscore) dirapihin jadi `yyy.py`. Duplikat basi (`content__result_builder.py`, `utils__card_images.py`) dihapus. File test yang nyasar di root dipindah ke `tests/`.

## 2 Okt 2026 (ronde 2) — Pisahin CSS & notes dari app.py
CSS (~390 baris, tadinya 1 string raksasa di `app.py`) dipindah ke `assets/css/app.css`, dibaca & di-inject lewat `Path.read_text()`. Catatan dated/narrative (bug-fix dropdown, keputusan sinkronisasi Home↔Reveal Yourself 27 Sep) dipindah ke `docs/bugs-fixed.md` & diringkas di sini, digantikan pointer singkat di kode.

## 6 Okt 2026 — Library 100% JSON, bersih-bersih legacy
- Weton 35/35 profil, daily 175, weekly 140. Matrix Destiny, MBTI, Human Design, Zi Wei (Qi Sha diperbaiki, Po Jun baru) dilengkapi.
- 7 JSON rusak diperbaiki, Tarot major direkonstruksi (The World dilengkapi).
- 10 sistem non-tanggal-lahir sekarang dibaca dari JSON via `content/profile_flat.py`. Kamus .py lama dihapus (lihat DAFTAR_HAPUS_2.txt).
- Views lama dihapus (DAFTAR_HAPUS_3.txt). Exit Mode 2/3 di modal balik ke Home dengan toast.
- Em dash/en dash dibersihkan dari copy UI.
- `docs/generator_guide.md` ditulis ulang (data periodik + format flat).

## 6 Okt 2026 (lanjutan) — Fitur & data tambahan
- Laporan Mingguan/Bulanan tersambung ke UI (modal "Weekly & Monthly Report"): Zodiak, Weton, Shio, Numerologi, Tarot. Belum ada pemotongan Stardust (masih dummy).
- `components/combo.py` disambung ke detail sistem ("Kombinasi Variabelmu") untuk Zodiak, Shio, Numerologi, Matrix Destiny.
- Big Five: teks "Sedang" (5 trait) ditulis sendiri, tidak lagi pinjam sisi tinggi/rendah.
- Zi Wei monthly: Qi Sha dan Po Jun (12 istana masing-masing), total 168 record. Belum disambung ke UI (butuh hitung istana transit).
- Tarot: engine menarik dari 78 kartu; kartu minor belum punya gambar (tampil sampul / tanpa gambar). Tarot periodik deterministik per hari/pekan/bulan (`engine.tarot.kartu_periodik`).
