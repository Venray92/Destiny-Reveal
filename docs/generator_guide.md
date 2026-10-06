# Panduan Generator Teks Profil: Destiny Reveal

Bagian 1-5 berlaku untuk 5 sistem Mode 1: Zodiak, Shio, Numerologi, Matrix Destiny, Weton. Bagian 6 untuk data periodik, bagian 7 untuk 10 sistem lain.
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

## 6. Data Periodik (harian, mingguan, bulanan)

Lokasi: `content/interpretations/<sistem>/{daily,weekly,monthly}.json`. Isi: list record (bukan dict per key). Loader: `content/periodic.py` (`get_daily`, `get_weekly`, `get_monthly`, `audit`). Pemilihan record dari kalender (WIB), bukan acak.

| Sistem | Periode | Kunci record | Jumlah |
|---|---|---|---|
| Zodiak | daily | `sign_user` + `house` (rumah Bulan 1-12) | 144 |
| Zodiak | weekly | `sign_user` + `fase_bulan` (Senin minggu itu) | 48 |
| Zodiak | monthly | `sign_user` + `sun_house` (tgl 15) | 144 |
| Shio | daily | `shio_user` + `elemen_hari_ini` | 60 |
| Shio | weekly | `shio_user` + `fase_bulan` | 48 |
| Shio | monthly | `shio_user` + `shio_bulan_ini` | 144 |
| Weton | daily | `weton_user` + `pasaran_hari_ini` | 175 |
| Weton | weekly | `weton_user` + `fase_bulan` | 140 |
| Numerologi | daily | `personal_month` + `personal_day` (butuh tgl lahir) | 81 |
| Numerologi | weekly | `personal_month` + `fase_bulan` | 36 |
| Numerologi | monthly | `personal_year` + `personal_month` | 81 |
| BaZi | monthly | `day_master` + `elemen_bulan` | 120 |
| Zi Wei | monthly | `bintang_utama` + `istana_transit` (= (cabang bulan - cabang Ming Gong) mod 12 + 1) | 168 |

Field record daily: `pesan, aksi[], hindari[], jam_baik, angka_hoki, warna_hoki`. Weekly: `timing, prediksi, saran, hindari, hari_terbaik` + `arah_rezeki` (Weton) / `fokus_mingguan` (Zodiak, Shio, Numerologi). Monthly: `timing, prediksi, peluang, hindari_risiko, saran, fokus_bulan_ini, fase_kunci`.

### 6.1 Aturan isi
- Satu record = satu kombinasi kunci. Tidak boleh ada record kembar dan tidak boleh ada pesan/prediksi yang sama persis antar record dalam satu file.
- Khas kunci user (sifat tanda, shio, weton, dst) dan khas konteks kalender (rumah, pasaran, fase Bulan).
- `prediksi` memakai "cenderung" atau "umumnya". `hindari` ditulis sebagai pola yang bisa diatur, bukan vonis.
- Saran selalu berukuran (menit, hari, jam, jumlah).
- Detail astrologi tradisional boleh, selalu berhati-hati ("secara tradisi", "sekitar"). Tidak menyebut retrograde.
- Tanpa "—", "–", spasi ganda, atau kata vonis (pasti, sial, vonis, ditakdirkan).
- Weton: tidak menyebut pancasuda. Shio: tidak menyebut elemen tetap, pakai polaritas Yang/Yin.

### 6.2 Validasi
- `pytest tests/test_periodic.py`: kelengkapan kombinasi, tanpa duplikat, JSON strict valid, tanpa em dash.
- `tests/test_periodic.py::test_semua_json_interpretasi_valid_strict` memeriksa semua JSON di `content/interpretations/`.

## 7. Profil 10 Sistem Non-Mode-1

Sistem: BaZi, Zi Wei, Human Design, Golongan Darah, MBTI, Enneagram, DISC, Love Language, Big Five, Tarot.
Lokasi: `content/interpretations/<sistem>/profile.json` (Tarot: `tarot_major.json`, `tarot_cups.json`, `tarot_pentacles.json`, `tarot_swords.json`, `tarot_wands.json`). Loader: `content/profile_flat.py`.

```
{"system": "<nama>", "version": 1, "data": {"<key>": {
  "nama": "...",
  "free": {siapa_kamu, atribut_1, atribut_2, quote},
  "paid": {kekuatan_yang_perlu_dijaga, pr_kecil_buat_kamu, karir, asmara, keuangan, kesehatan}}}}
```

Pemetaan tampilan: p1 = `free.siapa_kamu`, p2 = `paid.kekuatan_yang_perlu_dijaga`, p3 = `paid.pr_kecil_buat_kamu`, domains = karir, asmara, keuangan, kesehatan. Judul, tagline, dan chip dari `content/interpretations/titles.json`.

| Sistem | Key JSON | Jumlah |
|---|---|---|
| BaZi | `jia, yi, bing, ding, wu, ji, geng, xin, ren, gui` | 10 |
| Zi Wei | `zi_wei, tian_ji, tai_yang, wu_qu, tian_tong, lian_zhen, tian_fu, tai_yin, tan_lang, ju_men, tian_xiang, tian_liang, qi_sha, po_jun` | 14 |
| Human Design | `generator, manifesting_generator, manifestor, projector, reflector` | 5 |
| Golongan Darah | `a, b, ab, o` | 4 |
| MBTI | 4 huruf huruf kecil, mis. `intj` | 16 |
| Enneagram | `tipe_1` sampai `tipe_9` | 9 |
| DISC | `dominance, influence, steadiness, conscientiousness` | 4 |
| Love Language | `words_of_affirmation, quality_time, receiving_gifts, acts_of_service, physical_touch` | 5 |
| Big Five | `<trait>_tinggi`, `<trait>_rendah` (openness, conscientiousness, extraversion, agreeableness, neuroticism). Level Sedang dialihkan ke sisi terdekat | 10 |
| Tarot | `major_00` sampai `major_21`, `cups_01..14`, `pentacles_01..14`, `swords_01..14`, `wands_01..14` | 78 |

Tiap field paid sekitar 1.000 sampai 1.300 karakter. Aturan tanda baca dan kata vonis sama seperti bagian 4. Dicek oleh `profile_flat.audit(sistem)` dan `tests/test_profile_flat.py`.


## 8. Combo (penggabungan variabel dalam satu sistem)

File: `content/interpretations/<sistem>/<sistem>_combo.json`, dibaca `components/combo.py` (`build_combo(system, raw)`), tampil sebagai kartu pelangi terakhir di detail sistem. 12 sistem: Zodiak, Shio, Numerologi, Matrix Destiny, Weton, Zi Wei, Human Design, MBTI, Big Five, Enneagram, DISC, Love Language. BaZi, Golongan Darah, Tarot tidak punya (1 variabel).

Aturan: semua string kalimat lengkap berawal huruf kapital (disambung spasi, kecuali 4 sistem lama yang pakai kata hubung otomatis); 230-450 karakter per entri; tanpa em/en dash; semua kombinasi harus terisi (tes: `tests/test_combo.py`). Key tiap file bisa dilihat langsung dari builder-nya di `components/combo.py`.
