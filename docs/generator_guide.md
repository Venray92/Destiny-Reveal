# Panduan Generator Teks Profil: Destiny Reveal

Berlaku untuk 5 sistem: Zodiak, Shio, Numerologi, Matrix Destiny, Weton.
Tujuan: teks mengalir, saran sesuai bobot indikator, tone konsisten.

## 1. Struktur Output

```
{"system": "<nama>", "data": {"<Key>": {"sections": {
  "free": {siapa_kamu, atribut_1, atribut_2, quote},
  "A".."M": "teks"}}}}
```

| Kunci | Isi | Panjang acuan |
|---|---|---|
| A | Aspek utama | 200-300 karakter |
| B | Karier dan uang | 300-350 |
| C | Asmara | 200-250 |
| D | Kekuatan | 180-230 |
| E | Shadow work | 200-260 |
| F | Nasihat strategis | 250-600 |
| G | Preview satu kalimat | 45-75 |
| H | Karier mendalam | 400-600 |
| I | Asmara mendalam | 450-540 |
| J | Keuangan | 220-420 |
| K | Pemicu shadow | 200-310 |
| L | Blindspot | 160-270 |
| M | Latihan kecil | 150-330 |

Key lookup: Zodiak `sign`, Shio `shio`, Weton `"{hari} {pasaran}"`, Numerologi `str(life_path)`, Matrix `str(titik_inti)`.

## 2. Aturan Transisi (Penggabungan Modul)

Berlaku saat teks dirakit dari dua variabel atau lebih (Weton: Hari + Pasaran) dan saat menambah kalimat ke teks yang sudah ada.

1. Jangan menempel dua kalimat mentah. Selalu beri penghubung di awal kalimat kedua.
2. Pilih penghubung sesuai hubungan antar-kalimat.

| Hubungan | Penghubung |
|---|---|
| Menambah (A, B, D, J) | Selain itu, / Di samping itu, / Ditambah lagi, |
| Sisi bayang (E, K, L) | Di sisi lain, / Pada saat yang sama, |
| Asmara (C, I) | Sementara itu, / Soal kecocokan, |
| Langkah aksi (H) | Karena itu, dalam 90 hari ke depan, ... |
| Penutup saran (F) | Terakhir, ... |
| Latihan (M) | Lalu, / Setelah itu, / Sebagai pelengkap, |

3. Rotasi penghubung per entry (jangan satu kata dipakai terus).
4. Huruf pertama kalimat setelah penghubung ditulis kecil ("Selain itu, pasaran Wage ...").
5. Jangan ada penghubung ganda dalam satu kalimat ("Sebagai pelengkap, dengan pasaran ...": hindari).
6. Jangan mengulang aksi yang sama di dua kalimat dalam satu bagian. Cek: kata kerja utama (bagikan, tetapkan, sisihkan) tidak muncul dua kali.

## 3. Saran Dinamis per Indikator

Bobot indikator ditulis sebagai kalimat penekanan di bagian F (dan H, J, M bila variabel dirakit otomatis). Kalimat ini menentukan **fokus**, bukan menambah aksi baru.

| Sistem | Indikator | Kelompok | Fokus saran |
|---|---|---|---|
| Weton | Neptu 7-10 | Kecil | Kepercayaan diri, keberanian tampil |
| Weton | Neptu 11-14 | Menengah | Konsistensi, keseimbangan |
| Weton | Neptu 15-18 | Besar | Pengelolaan emosi, ambisi |
| Numerologi | 1-9 | Angka tunggal | Kedalaman, satu kebiasaan sampai jadi |
| Numerologi | 11, 22, 33 | Angka master | Keberlanjutan, jeda pemulihan, kurangi tekanan |
| Zodiak | Kardinal | Inisiatif | Penyelesaian (tanggal selesai) |
| Zodiak | Fixed | Keteguhan | Kelenturan (eksperimen yang dievaluasi) |
| Zodiak | Mutable | Adaptasi | Fokus (satu prioritas) |
| Shio | Yang | Energi ke luar | Pengendalian tempo, beri jeda |
| Shio | Yin | Energi ke dalam | Keberanian tampil |
| Matrix | Aksi (1,4,7,11,21) | Dorongan | Keberlanjutan tenaga |
| Matrix | Relasi (2,3,6,12,19) | Empati | Batas diri |
| Matrix | Refleksi (5,8,9,15,18,20) | Pemikiran | Dari renungan ke tindakan |
| Matrix | Transformasi (10,13,14,16,17,22) | Perubahan | Stabilitas, perubahan bertahap |

Aturan:
- Shio: elemen berasal dari engine (tahun lahir). **Jangan** menyebut elemen tetap di A-M. Pakai polaritas saja.
- Kalimat bobot ditaruh **di akhir** bagian, diawali "Selain itu," lalu menyebut indikatornya ("sebagai tanda Fixed", "karena polaritasmu Yin").
- Jangan menulis nasib. Pakai "cenderung", "umumnya", "bobot sarannya".

## 4. Tone of Voice

Empati, lugas, profesional, mudah dipahami pengguna umum.

Wajib:
- Sapaan "kamu". Indonesia baku yang ramah, bukan bahasa gaul.
- Kalimat pendek-menengah (maks. sekitar 30 kata).
- Saran konkret: ada kata kerja, ukuran (tiap hari, seminggu sekali), atau tenggat (90 hari).
- Sisi negatif ditulis sebagai pola yang bisa diubah ("Di baliknya sering ada ketakutan ..."), bukan label.

Dilarang:
- Tanda "—" dan "–".
- Kata vonis atau menakut-nakuti: "pasti", "ditakdirkan gagal", "sial", "vonis".
- Pernyataan medis, finansial, atau hukum yang bersifat nasihat profesional.
- Istilah teknis tanpa penjelasan singkat.
- Menyebut fixed element di Shio atau pancasuda di Weton (sudah ditampilkan engine).

Kecocokan (bagian I), format tetap:
> "Soal kecocokan, secara tradisi dalam <sistem>, <X> umumnya dianggap selaras dengan <A> dan <B> karena <alasan>, sementara pasangan <C> mungkin perlu usaha ekstra menyamakan <hal>. Ini hanya gambaran kecenderungan, bukan penentu hubungan, dan bisa diatasi dengan komunikasi yang jujur."

## 5. Checklist Validasi Sebelum Dikirim

- [ ] Urutan kunci: `free` lalu A-M, semua string tidak kosong.
- [ ] Jumlah entry: Zodiak 12, Shio 12, Numerologi 12, Matrix 22, Weton 35.
- [ ] Tidak ada "—", "–", spasi ganda, atau spasi di ujung teks.
- [ ] Tidak ada teks sama persis antar bagian atau antar entry.
- [ ] H memuat "dalam 90 hari"; I memuat "Soal kecocokan" dan "bukan penentu hubungan".
- [ ] F memuat satu kalimat bobot indikator sesuai tabel.
- [ ] Tidak ada aksi duplikat dalam satu bagian.
- [ ] `build_detail` jalan untuk semua key: 6 section + 7 bagian mendalam.
- [ ] `pytest tests/test_modal_detail.py` lulus.

## 6. Data Dinamis & Berkala

Lokasi: `content/dynamic/<folder>/{daily,weekly,monthly}.json`. Wrapper: `{"system","kind","data":{"<Key>":...}}`. Key sama dengan profil (Zodiak `sign`, dst).

| File | Struktur per key | Ganti | Pemilihan |
|---|---|---|---|
| daily | `ramalan[100] saran[20] hoki[30] warna[20] quote[10]` | 00:00 WIB | sha256(tanggal+anonymous_id+sistem+kategori) % n |
| weekly | `week_1..week_5 {timing, prediksi, saran, hindari}` | Senin 00:00 WIB | slot = minggu ke-n dari tanggal Senin |
| monthly | `"1".."12" {timing, prediksi, saran, peluang, risiko, tanggal_penting}` | tanggal 1 00:00 WIB | bulan WIB |

### 6.1 Kuota daily (per key)
Ramalan 100, saran 20, hoki 30, warna 20, quote 10. Semua unik dalam satu kategori. Konstanta: `dynamic_loader.QUOTA_PRODUKSI`.

Cara menyusun supaya tidak terasa template:
- Ramalan = kalimat kecenderungan khas key (20 per key, 2 per ranah: kerja, uang, asmara, teman, energi, belajar, keputusan, komunikasi, kreativitas, ritme) + 1 dari 5 saran praktis ranah yang sama, disambung penghubung bergilir ("Karena itu,", "Sebagai langkah kecil,", "Supaya tetap terarah,", "Untuk hasil yang lebih baik,", "Kalau sempat,").
- Hoki 30 = 12 angka + 8 jam + 5 arah + 5 kata kunci. Warna 20 dari palet elemen.
- Item daily tidak boleh menyebut nama hari atau tanggal tertentu.

### 6.2 Aturan monthly
- Dilarang satu pola kalimat dipakai di semua bulan. Tiap field punya minimal 6 kerangka kalimat (deklaratif, kondisional "Jika...", imperatif, dua kalimat berurutan), dipilih bergeser per bulan sehingga dua bulan berurutan tidak pernah memakai kerangka yang sama.
- Isi tiap bulan wajib khas bulan itu (suasana, fokus, risiko) dan khas key (kekuatan, pola yang diwaspadai, cara mengatur diri).
- `prediksi` memakai "cenderung" atau "umumnya". `risiko` ditulis sebagai pola yang bisa diatur.
- `tanggal_penting`: dua rentang tanggal. Format: `8-14 Januari untuk diskusi penting, 22 ke atas untuk rehat`. Pakai tanda hubung biasa (bukan "–"). Tanggal tidak boleh melebihi jumlah hari bulan itu (Februari maks. 28), urutan naik, rentang pertama sebelum rentang kedua. Ada 3 variasi susunan, bergilir.

### 6.2a Standar benchmark (Aries) untuk monthly dan weekly
Berlaku untuk semua key. Naskah ditulis per teks, bukan dirakit dari template.
- Khas sifat key (pola kebiasaan, mekanisme risiko) dan khas bulan atau minggunya (skenario konkret sesuai tema).
- Panjang acuan monthly: timing 95-155 karakter, prediksi 270-420, saran 190-270, peluang 145-215, risiko 155-240.
- Saran selalu berukuran (menit, hari, jam, jumlah). Risiko selalu disertai mekanisme ("biasanya bermula dari ...").
- Detail astrologi tradisional boleh, selalu berhati-hati ("secara tradisi astrologi", "sekitar"): hanya musim Matahari (Aries 21 Mar-19 Apr, Taurus 20 Apr-20 Mei, Gemini 21 Mei-20 Jun, Cancer 21 Jun-22 Jul, Leo 23 Jul-22 Agu, Virgo 23 Agu-22 Sep, Libra 23 Sep-22 Okt, Scorpio 23 Okt-21 Nov, Sagittarius 22 Nov-21 Des, Capricorn 22 Des-19 Jan, Aquarius 20 Jan-18 Feb, Pisces 19 Feb-20 Mar). Tidak menyebut retrograde atau tanggal astronomi lain.
- Dua bulan berurutan tidak boleh dibuka dengan empat kata yang sama (nama bulan dihitung sama). Tidak ada teks kembar antar bulan atau antar key.
- Tanggal penting: tiga angka naik, nama bulan wajib ada, tidak ada angka lain.
- Dicek otomatis oleh `dynamic_loader.validate` dan `tests/test_dynamic_loader.py`.

### 6.3 Aturan weekly
`timing` 1 kalimat, `prediksi` 1-2 kalimat dengan "cenderung/umumnya", `saran` konkret dengan ukuran, `hindari` frasa pendek tanpa titik.

### 6.4 Umum
- Tone sama seperti bagian 4. Item daily berdiri sendiri, tidak merujuk item lain.
- Tanpa "—", "–", spasi ganda, duplikat dalam satu kategori, dan kata vonis (pasti, sial, vonis, ditakdirkan).
- Validasi: `dynamic_loader.validate(system, kind, QUOTA_PRODUKSI)`.
