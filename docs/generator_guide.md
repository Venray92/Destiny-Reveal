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
| daily | `ramalan[50] hoki[20] warna[10] saran[30] quote[20]` | 00:00 WIB | sha256(tanggal+anonymous_id+sistem+kategori) % n |
| weekly | `week_1..week_5 {timing, prediksi, saran, hindari}` | Senin 00:00 WIB | slot = minggu ke-n dari tanggal Senin |
| monthly | `"1".."12" {timing, prediksi, saran, peluang, risiko}` | tanggal 1 00:00 WIB | bulan WIB |

Aturan tulis:
- Tone sama seperti bagian 4. Satu item daily = satu kalimat (maks. 2), berdiri sendiri, tidak merujuk item lain.
- Item daily tidak boleh bergantung pada hari/tanggal tertentu ("hari ini" boleh, "Senin ini" jangan).
- Weekly: `timing` 1 kalimat, `prediksi` 1-2 kalimat dengan "cenderung/umumnya", `saran` konkret dengan ukuran, `hindari` frasa pendek tanpa tanda titik.
- Monthly: `peluang` dan `risiko` seimbang; risiko ditulis sebagai pola yang bisa diatur.
- Transisi antar-kalimat dalam satu item pakai penghubung dari bagian 2.
- Tanpa "—", "–", spasi ganda, atau duplikat dalam satu kategori.

Validasi: `dynamic_loader.validate(system, kind, minimum)`; target produksi daily `{"ramalan":50,"hoki":20,"warna":10,"saran":30,"quote":20}`.
