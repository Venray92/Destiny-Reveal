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

## 6 Okt 2026 (malam) — Combo 12 sistem + kartu pelangi
- `components/combo.py` diperluas dari 4 ke 12 sistem: tambah Weton, Zi Wei, Human Design, MBTI, Big Five, Enneagram, DISC, Love Language (data: `<sistem>/<sistem>_combo.json`). BaZi, Golongan Darah, Tarot tanpa combo (cuma 1 variabel).
- Kartu "COMBO" muncul sebagai kartu terakhir setelah seksi hasil di detail sistem, border pelangi bersinar (`.dh-dt-combo`). Ikut masuk ke "Salin Seluruh Analisis Lengkap".

## 6 Okt 2026 (tengah malam) — Periodik lengkap, combo Zodiak, perbaikan alur
- Periodik baru: Shio mingguan (48), Numerologi harian (81) dan mingguan (36). BaZi bulanan (120) dan Zi Wei bulanan (168) disambung ke `content/periodic.py` dan modal "Weekly & Monthly Report" (BaZi dari tgl lahir, Zi Wei dari tgl + jam lahir).
- Modal Weekly & Monthly: tambah Shio, Numerologi, BaZi, Zi Wei. Tes setahun penuh untuk semua kombinasi baru.
- Perbaikan: `compute_mode1` sekarang memakai jam/kota lahir dari form untuk menghitung Bulan Zodiak (sebelumnya form menerima jam tapi tidak pernah dipakai, tes `test_mode1_zodiak_bulan_hanya_jika_jam_diisi` gagal). Tanpa jam, combo Zodiak tampil versi Matahari + unsur.
- Teks diperpanjang: Big Five Sedang, Po Jun/Qi Sha (profil dan bulanan), semua combo yang di bawah 230 karakter.

## 6 Okt 2026 (akhir) — Bersih-bersih
- Import tak terpakai dihapus (auth, solo_reveal, sections, data, human_design, simple_pdf).
- `settings.py` (TESTING_MODE tidak dibaca file mana pun) dan folder `synthesis/` (stub kosong) dihapus. Lihat DAFTAR_HAPUS_4.txt.
- CSS mati dibuang: 36 aturan `.dr-*` di `app.css` (halaman lama) dan 71 aturan di `home_v2.css` (profil lama `.dh-pf-*`, `.dh-sk-ms`, FAQ lama, dll). Ukuran total 202,9 KB menjadi 191,0 KB. Dicek lewat screenshot sebelum/sesudah (home, modal laporan, form, 4 langkah alur, hasil, detail, profil): identik.
