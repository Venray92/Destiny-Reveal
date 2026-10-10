# Destiny Reveal: Progress Notes Library/Data + UI Terbaru (update 10 Okt 2026)

_Catatan ini MELENGKAPI dan, kalau bentrok, MENGGANTIKAN `progress-notes.md` untuk soal library/konten/data, batch UI 7 Okt, Deep Blueprint (REVISI06 Stage 3), dan semua revisi 9-10 Okt (bagian "Update 9-10 Okt" di bawah). Status: library 100% lengkap (A-M untuk semua 160 entri non-lahir + 5 sistem lahir). Gambar Tarot 78 kartu sudah ada di repo (semua 78 valid)._

## Status akhir library
- Semua konten 100% JSON. 15 sistem lengkap: Zodiak 12, Shio 12, Weton 35, Numerologi 12, Matrix Destiny 22, BaZi 10, Zi Wei 14, Human Design 5, Gol. Darah 4, MBTI 16, Enneagram 9, DISC 4, Love Language 5, Big Five 15, Tarot 78.
- 5 sistem lahir (Zodiak, Shio, Weton, Numerologi, Matrix): format `data[key].sections` A-M + `free`, dibaca `content/profile_loader.py`. A-F = Mode 1, G-M = Deep Blueprint.
- 10 sistem non-lahir: format `free{siapa_kamu, atribut_1, atribut_2, quote}` + `paid{kekuatan_yang_perlu_dijaga, pr_kecil_buat_kamu, karir, asmara, keuangan, kesehatan, shadow_work, nasihat_strategis}`, dibaca `content/profile_flat.py` (`get_profile` dan `get_big_five` mengembalikan `"entry"`).
- **E (`shadow_work`) dan F (`nasihat_strategis`) sudah ditulis untuk semua 160 entri non-lahir** (7 Okt). Teks Tarot/Zi Wei/MBTI-F/Big Five agak lebih pendek (~520-900 karakter) dari A-D (~1100-1200); belum dipanjangkan.
- **Deep Blueprint G-M untuk 10 sistem sudah ada** (digenerate lewat Gemini, diaudit): `<sistem>/deep.json` untuk 9 sistem + `tarot/deep_{major,wands,cups,swords,pentacles}.json`. Kunci = kunci entri profile. 7 field per entri: `ringkasan` (G), `karir_deep` (H), `asmara_deep` (I), `rezeki_deep` (J), `emosi_trigger` (K), `blindspot` (L), `latihan_harian` (M); tiap field 8 kalimat, ~900-1500 karakter. **Dibaca oleh `content/blueprint_calc.py`** (`_deep(system)`; mapping file di `_DEEP_FILE`).
- Audit 7 Okt di clone segar: semua JSON valid, profile dan deep cocok per sistem (Tarot 22+14x4 = 78), E/F ada di semua entri, `titles.json` 15 sistem.
- Audit 10 Okt di working copy terbaru: semua JSON valid (118 file di `content/`), pytest 280 pass.
- Jebakan upload yang pernah kejadian (cek kalau ada yang aneh): `profile_flat.py` salah folder (`components/` bukan `content/`), `tarot_major.json` salah isi (isinya Big Five), `bazi/deep.json` JSON rusak, `assets/cards/tarot/wands/09_nine_wands.jpg` pernah cuma 2 byte (teks CRLF); sudah diupload ulang Stev 10 Okt.

## Update 9-10 Okt 2026 (r15 s/d r28; semua dikirim sebagai zip, Stev upload manual lewat GitHub web UI)
### Data Gemini (Blueprint baru, Career, Strength, Soul Match)
- `content/interpretations/blueprint_baru/*.json` (14 sistem), `career/career_baru.json`, `career/strength_baru.json`, `compat/konteks.json`; loader `content/baru_loader.py` + `tests/test_baru_loader.py`.
- gemini3.zip di-merge ulang (redo, r23). Pembersihan kata aneh/kuno/typo di semua data baru (r25): pakai daftar ganti per kata, bukan edit massal. Sisa: 319 dari 1132 teks Blueprint redo masih terlalu mirip struktur Solo; Stev menerima asal kata-katanya beda.
- Aturan Gemini: Claude kasih prompt + info dulu, tidak mengarang data; data panjang lewat prompt pack (`gemini_pack*.zip`).

### REVISI01 (r26) dan REVISI02 (r27)
- Modal kategori Explore: maks 5 item terlihat, sisanya scroll internal (header tetap); JS di `navbar.py` (`dh-ov-scroll`).
- Ramalan Harian: tombol "🔒 Buka Analisis Lengkap Per Sistem" tanpa harga, tombol "Sinkronkan" dihapus; Selesai & Tutup + konfirmasi hanya muncul kalau sudah bayar (`dh_daily_paid`, 1x per hari WIB).
- Gacha Kartu Tarot: kartu awal glowing + floating; tombol "🔒 Mau Tau Lebih Dalam?" tanpa harga, langsung buka One-System Blueprint dengan Tarot terpilih (`request_solo`); "Sinkronkan" dan "Selesai & Tutup" dihapus.
- Afirmasi: tombol "Simpan Kartu PNG" dihapus; font kartu dibawa repo (`assets/fonts/`, DejaVu + Lora) karena font sistem tidak ada di server Stev. Titik hitam di header Afirmasi: tidak bisa direproduksi lokal, penyebab belum ketemu.
- Kalender Energi: semua dalam 1 iframe (tinggi menyesuaikan konten, tanpa jarak kosong), badge "✅ Akses Terbuka", tombol copy per tanggal (`_day_text`), Selesai & Tutup + konfirmasi, kembali ke state berbayar bulan itu (`dh_cal_paid`).
- Preview Zodiak: kartu kunci/blur dan harga 200 ✨ dihapus.
- Keputusan Stev: fitur Daily Free perlu login; modal hasil = dashboard visual; tidak ada harga Stardust di halaman utama.

### Update 10 Okt (r28): CSS dipecah + gambar Tarot
- **CSS**: `assets/css/home_v2.css` (244 KB) DIHAPUS, diganti 15 file `assets/css/parts/01_... s/d 15_...css` per fitur. `app.py` memuat semua file urut nama (`sorted(glob("*.css"))`), jadi urutan cascade = urutan nomor. Gabungan 14 file pertama sudah dicek identik byte-per-byte dengan file lama. Revisi baru: edit file part yang relevan atau tambah part baru berikutnya (mis. `16_...css`). `tests/test_revisi01.py` mengecek part berurutan.
- **Gambar Tarot** (Stev upload 10 Okt): struktur baru `assets/cards/tarot/{major,cups,pentacles,sword,wands}/`, semua `.jpg` 1792x2400. Major `NN_slug.jpg` (00-21). Minor `NN_<nama>_<suit>.jpg`, NN 01-14 (ace, two..ten, page=11, knight=12, queen=13, king=14), folder suit **`sword` (tunggal)** walau slug engine `swords_*`. File lama `tarot/NN_slug.png` dihapus.
- Overlay nama gelap yang nutupin kartu di Gacha dihapus (r30): label ARCANA + nama kartu sekarang di BAWAH gambar (`assets/css/parts/15_tarot_nama_di_bawah.css`, `.dh-tr-wrap + .dh-tr-over`).
- Resolver tunggal: `utils/card_images.py` `tarot_image_rel(slug)` (slug engine -> path; None kalau file tidak ada atau <1 KB). Dipakai Gacha Kartu Tarot (`mini_modals.py`), Tarot Spread/Decision (`feature_modals.py`), dan `card_relative_path_for_result("Tarot", ...)` (detail hasil + download).
- `card_image_data_uri_small(path, width=520)`: WebP ber-watermark ±70-220 KB untuk tampil di modal (asli ±1,7 MB, base64 inline 2,3 MB per kartu bikin render berat). Download tetap pakai file penuh.
- Kartu tanpa gambar jatuh ke kartu ilustrasi bawaan (`_tarot_face`: angka romawi/simbol suit). Sekarang semua 78 kartu punya gambar; fallback hanya kalau file hilang/rusak.
- `utils/trait_cards.py` (kartu Career DNA, Strength, Decision, Yearly): font kini dimuat dari `assets/fonts/` dulu, terakhir `ImageFont.load_default(size)`.
- Verifikasi: pytest 280 pass; Playwright: Hanged Man (Major), Three of Cups dan King of Swords (Minor) tampil sebagai gambar; tes 77/78 sebelum `wands_09` diupload ulang, lalu 78/78 tampil.

### Snapshot repo (baca ulang 10 Okt, working copy terbaru)
- ~15.500 baris Python: `components/` (32 file; terbesar `compat.py`, `mini_modals.py`, `solo_reveal.py`, `blueprint.py`, `feature_modals.py`, `self_discovery.py`), `content/` (118 file, 7,4 MB), `engine/` (18), `utils/` (6), `views/` (2), `tests/` (27), `docs/`.
- `assets/` ±350 MB (kartu PNG/JPG per sistem; Tarot baru ±110 MB). Repo besar; kalau clone/deploy lambat, pertimbangkan kompres gambar.
- Bersihkan di repo GitHub: `claude_push_test.txt` (sisa tes), `docs/progress notes library.MD` versi lama (diganti file ini). `requirements.txt` tidak mencantumkan Pillow secara eksplisit (ikut dari Streamlit).

## Combo (kartu pelangi)
- `components/combo.py` `build_combo(system, raw)` untuk 12 sistem. BaZi, Gol. Darah, Tarot **tidak punya combo** (1 variabel; Tarot spread pakai `components/tarot_combo.py`). Human Design combo tidak bisa dites di sandbox.
- Tampil di detail Reveal dan di bawah analisis A-F hasil Solo Reveal (`.dh-dt-combo`). Kalau Stev mau combo untuk BaZi/Gol. Darah/Tarot Solo, perlu konten baru.

## Matriks periodik (data siap)
- Daily: Zodiak, Shio, Weton, Numerologi (+ Tarot harian terpisah). Weekly: Zodiak, Shio, Weton, Numerologi, Tarot. Monthly: Zodiak, Shio, Numerologi, BaZi, Zi Wei, Tarot.
- Statis: Matrix Destiny, Human Design, MBTI, Big Five, Enneagram, DISC, Love Language, Gol. Darah. Kunci periodik di `content/periodic.py`, kalender WIB.
- Daftar "paling akurat" versi Stev (hindari kata "akurat" di copy): Daily Zodiak/Weton/Shio/Tarot; Weekly Tarot/Zodiak/Weton; Monthly Tarot/Zodiak/Shio/Numerologi/BaZi/Zi Wei.
- Data disimpan belum dipakai UI: `shio/weekly.json`, `numerologi/daily.json`, `numerologi/weekly.json`.

## Solo Reveal (update)
- Semua 15 sistem aktif. Hasil A-F; 10 sistem non-lahir dibaca dari `entry` lewat `_entry_aspek` di `components/solo_reveal.py` (E dan F pakai `shadow_work` dan `nasihat_strategis`).
- Alur: pilih sistem, (kuesioner untuk 5 sistem psikologi), bayar, loading ~3 detik, hasil. Saldo dipotong setelah hasil berhasil dihitung. `request_solo(system)` (di `mini_modals.py`) membuka Solo dengan sistem terpilih.
- **Harga Solo 200 ✨** (sumber tunggal `content/pricing.py`, `SOLO = 200`).

## Harga (REVISI06, single source of truth `content/pricing.py`)
- Solo 200, Weekly 300, Monthly 600, Blueprint (Deep Dive 1 sistem) 800, Complete 15 sistem 1.200, Bundle 15 sistem 1.200, Daily full 50, Swap 50, Compat 100/sistem, Tarot 3/5/10 kartu = 50/100/150, Tarot bundle 250. Tampil di web selalu pakai ikon ✨ (bukan tulisan SD).
- Paket Stardust: Starter 10rb=120, Basic 25rb=320, Value 50rb=700, Pro 100rb=1.500, Sultan 200rb=3.200, Kaisar 500rb=8.500. VIP Lifetime Rp 2.499.000.
- **`BLUEPRINT_ALL = 1200` adalah ASUMSI Claude** (REVISI06 hanya menyebut "Complete Bundle 15 Sistem" 1.200). Perlu konfirmasi Stev.

## Batch UI 7 Okt 2026 (round 6)
- `components/close_confirm.py`: konfirmasi tutup bertema untuk modal hasil akhir. Jalur: tombol Selesai & Tutup (layar konfirmasi di dalam dialog) dan tombol X (`on_dismiss` -> `dh_cc_reopen` -> `navbar.py` buka ulang dialog). Kunci modul = nama dialog. Penanda `.dh-nodismiss` memblok backdrop/Esc (hanya kalau `_head(block=True)`).
- Check-in dan klaim reward Streak: popup bertema yang tutup sendiri 2,5 detik (`dh_sk_pop`).
- Cek Kecocokan (kini Soul Match): teks Kekuatan, Tantangan, Nasihat Strategis dipanjangkan.

## REVISI06 (8-9 Okt 2026): rename fitur, Weekly/Monthly, Deep Blueprint
- Rename: "Tarot Spreads", "Soul Match" (ex Cek Kecocokan), "Weekly & Monthly Report", "Blueprint Mendalam".
- Weekly & Monthly Report: `components/weekly_report.py` + `content/weekly_calc.py` (tab Weekly/Monthly, hasil 4 tab, wajib login).

### Stage 3: Deep Blueprint (Blueprint Mendalam), selesai 9 Okt
- **Alur** (`components/blueprint.py`, wajib login): start (tab Deep Dive / Complete + form profil: nama, tgl, jam, kota, gol. darah) -> mode kuesioner (Singkat 73 soal / Lengkap 157 soal, hanya 5 sistem psikologi) -> bayar -> loading 15 ikon (~3,6 dtk) -> hasil.
- **Hasil**: kartu identitas + 2 tab (Grand Synthesis & Arsitektur Hidup; 15 Dimensi accordion). Aksi: Download PDF (halaman dinamis), Share WhatsApp, Tutup (konfirmasi).
- **Deep Dive** = 1 sistem (800 ✨). **Complete** = 15 sistem (1.200 ✨, asumsi).
- **Data** (`content/blueprint_calc.py`): profil A-M 5 sistem lahir + `profile_flat` + `deep.json` G-M. Grand Synthesis, siklus panen, roadmap pakai Personal Year Numerologi; scoring kuesioner Singkat (`_short_raw`) disusun Claude, belum divalidasi ahli.
- 9 Okt: review kode terhadap REVISI6, BUKAN audit ulang angka rumus per sistem dan BUKAN tes live.

## Item lama di `progress-notes.md` yang SUDAH BASI
- "Tarot/Gol. Darah belum dibangun", "narasi 5 kuesioner belum ditulis", "BaZi/Zi Wei/Human Design belum", "`synthesis/synthesizer.py` stub", "`TESTING_MODE`/`settings.py`", "`daily.json` belum ada": semua sudah ada/dihapus.
- "Solo hanya 5 sistem aktif" dan "seksi Solo kosong untuk BaZi/Zi Wei/Gol. Darah/Tarot": basi.
- Harga lama (Solo 150, Weekly 100, Monthly 200, Blueprint 300, Bundle 500, VIP 1.999.000): basi.
- Nama "Cek Kecocokan" / "Deep Blueprint (15 Sistem)": basi, sekarang "Soul Match" / "Blueprint Mendalam".
- "Gambar Tarot minor (56 kartu) belum ada": basi, sudah ada sejak 10 Okt.
- `assets/css/home_v2.css` sebagai satu file: basi, sekarang `assets/css/parts/*.css`.
- Catatan "update progress-notes hanya dengan izin eksplisit" tetap berlaku; update ini atas permintaan Stev 10 Okt.

## Open items
- Konfirmasi harga Complete Blueprint (1.200 ✨ asumsi).
- Upload zip r28 (CSS parts + Tarot + trait_cards) lalu hard reload. Pastikan `assets/css/home_v2.css` lama dihapus di GitHub.
- Tarot Spread/Decision: kartu tanpa gambar (kalau file hilang) tampil kotak kosong.
- Solo: header masih menampilkan "· 200 ✨" saat dibuka ulang gratis; deskripsi `REL_KEYS` di form Soul Match belum disinkron ke subtext baru; typo "alaimu" ada di file Solo asli (`golongan_darah/profile.json`, dll), belum disentuh.
- Titik hitam di header Afirmasi (belum ketemu penyebab, tidak muncul di tes lokal).
- Verifikasi Human Design dan tes live Bulan dengan jam lahir (swisseph tidak ada di sandbox); kartu identitas Blueprint menampilkan "-" kalau HD tidak bisa dihitung.
- 4 bug lama menunggu putusan Stev: VIP ribbon, harga Soul Match, hemat% Bundle, warna VIP box.
- `loadingcard.png` masih ada teks baked-in. `tarot_combo.json` konten starter.
- Nama "Stardust" di FAQ/help/pricing/tier belum diputuskan diganti atau tidak.
- Backend B1-B5 menunggu jawaban Stev: Supabase, OTP email, Stardust, payment gateway, referral. Saldo masih dummy (`DUMMY_SALDO = 20000`); hasil hanya di `session_state`.
- Alur Mode 2/3 Reveal belum dibangun. Weton bulanan dilewati. Zi Wei: aturan istana transit disederhanakan.
- Review manual konten oleh Stev: belum. Opsional: panjangkan teks E/F yang lebih pendek.
- Ide fitur baru (8 Okt): Career Path Finder, Money Personality, Daily Affirmation, Habit Tracker, Family Match, Energy Forecast, Sleep Optimizer, Breakup Recovery; belum ada keputusan.
