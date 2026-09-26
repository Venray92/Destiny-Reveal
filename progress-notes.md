# Destiny Reveal — Progress Notes

_Terakhir diupdate: 26 September 2026 (batch: testing mode + payment-bypass + buka-semua-amplop sekuensial + reveal-lagi)_

## Cara kerja proyek ini

- Kode ditulis oleh Claude di sandbox, dikirim sebagai file (`app.py`, dll) lewat chat.
- Stev **upload manual** ke GitHub lewat web UI (bukan git/terminal): buka file di GitHub → edit (ikon pensil) → select all → paste isi baru → commit. Untuk file gambar, pakai "Add file → Upload files" (drag-drop), beda mekanisme dari edit teks.
- Repo: `github.com/Venray92/Destiny-Reveal` (public).
- Hosting: Streamlit Community Cloud → `destiny-reveal.streamlit.app` (public, viewer access sudah dibuka).
- Setelah commit, kadang perlu **reboot manual** app-nya di share.streamlit.io (Manage app → Reboot) kalau perubahan tidak muncul otomatis.

## Cara kerja Claude mulai sekarang (workflow, per instruksi Stev)

1. **Baca detail instruksi dengan teliti dulu**, jangan langsung eksekusi.
2. **Tunggu ACC/approval eksplisit** dari Stev sebelum mulai ngoding (kecuali diminta langsung gas).
3. **Kalau ada bagian instruksi yang belum jelas/ambigu, tanya dulu sampai benar-benar clear** sebelum mulai kerjain — jangan asumsi sendiri lalu jalan.
4. Beberapa revisi sengaja **ditahan/disimpan dulu** sampai Stev kasih revisi lain, baru dikerjakan sekaligus dalam satu batch. Kalau Stev bilang "simpan dulu" / "nanti sekalian", itu artinya JANGAN dieksekusi dulu — cuma dicatat di sini, tunggu instruksi lanjutan.
5. **PENTING**: sebelum ngedit ulang sebuah file, CEK dulu apakah ada revisi yang sebelumnya udah "disimpan"/ditahan yang nyentuh file yang sama (lihat bagian "Revisi yang ditahan" di bawah). Kalau ada:
   - kerjain SEKALIAN dalam batch yang sama, ATAU
   - kalau ragu apakah harus digabung sekarang, TANYA ACC dulu ke Stev sebelum mulai.
   JANGAN diam-diam skip terus baru ketauan pas Stev nanya — itu buang-buang waktu & token karena file yang sama jadi harus dikirim ulang dua kali.
6. Setelah beneran mulai ngoding (dapat ACC), **test dulu di background** sebelum kirim ke Stev:
   - Jalankan `streamlit run app.py` di sandbox sendiri (localhost)
   - Pakai Playwright buat screenshot & inspeksi DOM langsung (cek CSS, ukuran, warna, dsb secara terprogram, bukan cuma lihat sekilas)
   - Kalau ada yang berhubungan dengan lebar layar/responsive, tes di beberapa ukuran viewport
   - Kalau ada yang berhubungan dengan dark/light mode browser, tes dengan `color_scheme="dark"` juga
   - Buat fitur interaktif (tombol, toggle, download, input form), tes BENERAN diklik/diisi lewat Playwright (bukan cuma baca kode) dan cek elemen/hasil-nya beneran berubah/muncul sebelum kirim
   - **Kalau ada logic perhitungan (engine), tes pakai tanggal/data KONKRET (bukan cuma unit test isolated), tarik sampai ke UI paling akhir, dan cek hasil akhirnya benar-benar sesuai perhitungan manual** — jangan berhenti di "unit test pytest hijau semua", karena itu cuma membuktikan engine-nya sendiri benar, bukan bahwa alur data dari input user sampai ke tampilan akhir juga benar.
   - **Buat fitur yang melibatkan beberapa rerun berantai (animasi sekuensial, antrean, dsb), tes proses TENGAHNYA juga lewat screenshot per-tick, bukan cuma cek kondisi awal & akhir** — ketauan dari batch ini, bug bisa cuma muncul di TENGAH proses (lihat catatan bug "tombol nyangkut" di bawah, ditemukan justru dari screenshot mid-sequence, bukan dari cek state awal/akhir doang.
   - Baru kirim file ke Stev **setelah** dikonfirmasi benar-benar berhasil
7. Keterbatasan: sandbox Claude nggak bisa akses Google Fonts (ikon Material Symbols nggak kelihatan di preview lokal — bukan bug, cuma keterbatasan jaringan sandbox, sudah terbukti jalan normal di situs live).
8. **Update project notes (`progress-notes.md`) HANYA di akhir sesi**, setelah satu batch pekerjaan coding besar benar-benar selesai — bukan di tengah-tengah sesi setiap kali ada keputusan kecil.
9. Clone repo lewat `add_repo` (read-only, publik) itu HANYA buat verifikasi/ngecek isi repo — Claude TIDAK punya akses push ke repo ini. Semua kode tetap dikirim lewat chat buat di-paste manual oleh Stev (lihat poin workflow di atas). Kalau ada notifikasi/hook soal "uncommitted changes" atau "unverified commit" di clone verifikasi itu, itu tidak relevan (bukan alur kerja project ini).

## Revisi yang ditahan (belum dikerjakan, per 26 Sep 2026)

Per pesan Stev 25 Sep 2026 malam — belum dieksekusi, nunggu revisi tambahan buat digabung:

**Hero section:**
- Judul baru (fix): "Ada Banyak Versi Dirimu yang Belum Kamu Kenal."
- Subteks baru (fix, draf 2): "Masa lalu sudah menjadi pelajaran, saatnya kenali dirimu sepenuhnya sebelum melangkah ke depan. Satu pembacaan lengkap dari 15 sistem ini akan menunjukkan potensi, kelebihan, kelemahan, dan langkah yang sebaiknya kamu ambil."
- Badge "✧ 15 sistem pembacaan diri, 1 laporan personal" di atas judul → **dihapus**

**Area dropdown bahasa (nav kanan atas):**
- Icon bintang (✧) dari badge yang dihapus → dipindah, dipasang di kiri DAN kanan area bahasa (dekorasi)
- Label dropdown diganti dari "🇮🇩 ID" / "🇬🇧 EN" → jadi "🇮🇩 Indonesian" / "🇬🇧 English"
- Alignment "mid" (vertikal tengah) untuk elemen-elemen ini

## Lesson learned soal Streamlit CSS (biar nggak keulang)

- Kolom: testid aslinya **`stColumn`**, bukan `"column"`
- Tombol popover: testid **`stPopoverButton`** ada di elemen `<button>`, bukan `<div>`
- Ikon popover & panah dropdown (chevron) **sama-sama** pakai `data-testid="stIconMaterial"` — bedanya panah dibungkus `div[aria-hidden="true"]` terpisah
- Supaya kolom/kartu punya tinggi yang sama persis, perlu flex-grow manual sampai ke `stElementContainer` — solusinya bungkus dengan `st.container(key="...")` biar bisa ditarget presisi via `div[class*="st-key-..."]`, dipadukan `:has()` buat ancestor-nya. **Teknik ini juga yang dipakai buat nyisipin tombol Streamlit asli (download button, toggle button) di tengah-tengah layout kartu yang tadinya HTML mentah** (lihat `_render_detail` di `revealpage.py`) — kalau butuh widget Streamlit beneran (bukan cuma teks/gambar) di dalam suatu layout custom, jangan render satu blok HTML gede pakai `st.markdown`, pecah jadi beberapa `st.container(key=...)` bersarang dan taruh CSS flex di container key-nya, bukan di class HTML biasa.
- **Selectbox (`st.selectbox`) di Streamlit 1.64.0 sudah pindah ke React Aria ComboBox** — target lewat `[class*="react-aria-ComboBox"] > div`, bukan `div[data-baseweb="select"]` lagi (tetap dipasang paralel buat jaga-jaga).
- Panel/dropdown yang di-render lewat portal (popover, listbox) sering ikut dark-mode OS/browser kalau warnanya nggak dipaksa eksplisit.
- **`st.date_input` di versi Streamlit ini juga sudah pindah ke React Aria DateField** (spinbutton segmen year/month/day yang bisa diketik terpisah, bukan satu kotak teks biasa). Kalau butuh tes Playwright: isi tiap segmen lewat elemen `[aria-label*="year"]` / `[aria-label*="month"]` / `[aria-label*="day"]` (klik lalu ketik angkanya), JANGAN pakai `Escape` sesudahnya (Escape membatalkan/revert seluruh input kembali ke nilai sebelumnya di komponen ini) — cukup klik ke elemen netral lain di dialog buat nutup popup kalendernya.
- **BARU (batch ini) — kontainer ber-`key` yang KADANG diisi widget, KADANG dikosongkan (kondisional), TAPI dipanggil terus tiap render, bisa "nyangkut" isi lamanya**: `st.container(key="X")` yang badan kondisionalnya nggak selalu nulis apa-apa (mis. `if kondisi: with st.container(key="X"): st.button(...)`) TIDAK otomatis membersihkan widget dari render sebelumnya kalau di render sekarang kondisinya jadi False — soalnya Streamlit cuma ngirim "delta" buat apa yang benar-benar dipanggil skrip di run ini; kalau container-nya nggak dipanggil isi apapun, nggak ada delta "clear" yang dikirim, jadi kontennya kepake dari cache render lama. **Solusinya**: pakai `st.empty()` sebagai placeholder yang SELALU dipanggil (`ph = st.empty()`), baru isi lewat `with ph.container(): ...` kalau kondisinya True, atau panggil `ph.empty()` eksplisit kalau kondisinya False — jangan cuma skip manggil apa-apa. Ketauan dari bug tombol "Buka Semua Amplop" yang keliatan masih nempel di posisi grid amplop pas proses buka-semua sekuensial lagi jalan (screenshot mid-sequence), padahal kondisi Python-nya sudah jelas False di render itu.

## Bug ditemukan & diperbaiki (26 Sep 2026): `st.date_input` tanpa `min_value`/`max_value`

Saat tes end-to-end beneran (isi tanggal lahir lewat browser, bukan cuma pytest), ketauan `st.date_input("Tanggal Lahir", ...)` di `views/loadingpage.py` (`_ask_field_dialog`) dipanggil **tanpa** `min_value`/`max_value` eksplisit. Default Streamlit kalau parameter ini kosong adalah membatasi rentang ke **±10 tahun dari hari ini**. Akibatnya: siapa pun yang lahir sebelum ~10 tahun lalu (yaitu HAMPIR SEMUA calon user beneran) akan dianggap tanggalnya "invalid" begitu ketik tahun lahirnya, dan diam-diam kembali ke tanggal hari ini tanpa notifikasi — jadi hasil semua sistem yang dihitung dari tanggal lahir ikutan salah total.

**Sudah diperbaiki**: ditambahkan `min_value=date(1930, 1, 1)`, `max_value=date.today()`, dan default `value=date(2000, 1, 1)` (biar nggak default ke hari ini yang aneh buat field "tanggal lahir"). Sudah dites ulang lewat Playwright end-to-end (isi 5 Desember 1992 lewat UI beneran) dan hasilnya sekarang benar di semua 5 sistem.

## Batch baru (26 Sep 2026): testing mode, payment-bypass, buka-semua-amplop sekuensial, reveal-lagi

Batch ini murni revisi UI/UX alur screening → loading → hasil, biar bisa dites end-to-end tanpa nunggu infrastruktur asli (email OTP, payment gateway) selesai dibangun. **Tidak ada perubahan di 5 engine perhitungan** — semua tetap sama & tetap tervalidasi.

### Yang dikerjakan

1. **Hapus expander debug "🧪 Testing sementara (hapus nanti)"** di `app.py` — sudah nggak dipakai lagi, digantikan `TESTING_MODE` (poin 3) yang lebih rapi karena tetap lewat alur normal (bukan loncat halaman).
2. **Fix CSS gap OTP**: 6 kotak kode di kartu "Verifikasi Email" dulu nempel ke border bawah kartu — sudah dikasih jarak (padding-bottom kartu `8px`→`24px`, margin-bottom baris OTP `14px`→`0`, karena sekarang jaraknya datang dari padding kartu, bukan margin OTP-nya sendiri).
3. **`settings.py` (file baru)** — flag `TESTING_MODE = True`. Selama `True`:
   - `views/reveal_yourself.py`: langkah "Verifikasi Email" & "Pilih Fokus Eksplorasi" TETAP ditampilkan visualnya, tapi tombol "Mulai Proses Reveal" nggak diblokir kalau email kosong / mode belum diklik manual (mode otomatis default ke "Instan", karena cuma mode ini yang enginenya lengkap).
   - `views/loadingpage.py`: dialog akhir loading BUKAN payment gateway asli — cuma 1 tombol "Bypass Payment" buat lanjut ke halaman hasil (belum ada integrasi Midtrans/Xendit).
   - **Matikan `TESTING_MODE` (ganti ke `False`, jangan hapus flag-nya)** begitu OTP email asli + mode Mendalam/Lengkap + payment gateway beneran sudah siap dipasang.
4. **Dialog akhir loading diganti total**: dulu "SEMUA DATA DIRIMU SUDAH DIREVEAL" auto-lanjut sendiri lewat timer JS 5 detik — sekarang jadi dialog gaya paywall (`dismissible=False`, jadi user WAJIB pilih tombol, nggak bisa di-klik-luar buat nutup): ada 1 tombol "Bayar Sekarang" yang sengaja `disabled=True` (placeholder, nunggu payment gateway asli) + 1 tombol "Bypass Payment" yang beneran jalan (langsung ke halaman hasil). Tidak ada auto-continue lagi.
5. **Halaman hasil (`revealpage.py`)**:
   - Amplop mulai dari kondisi TERTUTUP semua seperti biasa (bukan auto-terbuka), user tetap bisa buka manual satu-satu.
   - **Tombol baru "Buka Semua Amplop"** (muncul di atas grid amplop, cuma kalau masih ada yang belum dibuka & lagi nggak proses apa-apa) → memicu **dialog konfirmasi kustom** (`@st.dialog`, BUKAN `st.warning`/`st.toast` bawaan Streamlit) dengan tombol "Iya, buka semua" / "Tidak".
   - Klik "Iya" → semua amplop yang belum dibuka masuk **antrean** (`session_state.reveal_open_all_queue`) dan terbuka **SATU PER SATU OTOMATIS secara berurutan** (animasi burst masing-masing main penuh dulu, baru lanjut ke amplop berikutnya, sampai antrean habis) — tanpa perlu klik lagi.
   - **Grid amplop diubah jadi satu baris yang bisa discroll ke samping** (bukan wrap per 5 kolom kayak dulu), lewat `st.container(key="rp_envelope_scroll")` + CSS `flex-wrap: nowrap; overflow-x: auto`, tiap amplop lebar tetap 168px — didesain siap nampung sampai 15 amplop nanti (skr baru 5) tanpa perlu ubah layout lagi.
   - Selama proses buka-semua sekuensial, container amplop **auto-scroll ke kanan** mengikuti amplop yang lagi dianimasikan (lewat JS `scrollIntoView`, dipicu tiap amplop mulai animasi, pakai trik marker unik yang sama seperti animasi burst).
   - **Tombol baru "Reveal Lagi"** di pojok kiri bawah (sebelah tombol "Kembali ke Home" yang tetap ada di tengah) — reset semua session state terkait (loading_*, reveal_*, DAN status verifikasi email/mode di reveal_yourself) lalu balik ke halaman Reveal Yourself buat mulai reveal orang lain dari nol.

### Bug ditemukan & diperbaiki DALAM batch ini (sebelum dikirim)

Saat tes Playwright mid-sequence (screenshot per ~800ms selama proses "Buka Semua Amplop" jalan), ketauan tombol "Buka Semua Amplop" masih keliatan nempel di posisi amplop meskipun harusnya udah disembunyikan (lihat penjelasan teknis lengkap di bagian "Lesson learned soal Streamlit CSS" di atas — kasusnya container `key`-nya nggak dibersihkan Streamlit kalau kondisinya berubah jadi False). **Sudah diperbaiki** pakai pola `st.empty()` + `.container()`/`.empty()` eksplisit, dites ulang lewat screenshot mid-sequence dan sekarang bersih di semua tick.

### Sudah dites (Playwright end-to-end, bukan cuma pytest)

- Alur penuh: isi tanggal lahir 5 Des 1992 → lewati email/mode (TESTING_MODE) → loading → dialog "Bypass Payment" → hasil.
- CSS gap OTP — screenshot close-up dikonfirmasi ada jarak sekarang.
- "Buka Semua Amplop" → dialog konfirmasi muncul → "Iya, buka semua" → kelima amplop terbuka BERURUTAN otomatis (diverifikasi lewat screenshot per-tick, bukan cuma cek akhir) → hasil yang tampil di tiap kartu detail cocok dengan perhitungan manual (Sagittarius, Monyet, Sabtu Pon neptu 16, Angka Hidup 11, The Brave).
- Dialog konfirmasi tombol "Tidak" → dikonfirmasi batal, amplop tetap tertutup semua, tombol "Buka Semua Amplop" tetap ada.
- Buka 1 amplop manual (tanpa buka-semua) — masih jalan normal seperti sebelumnya.
- "Reveal Lagi" — dikonfirmasi reset & balik ke halaman Reveal Yourself dengan langkah 1&2 kembali ke kondisi awal.
- "Kembali ke Home" — masih jalan seperti sebelumnya (skr sudah termasuk 2 key baru di reset list).
- `pytest tests/ -v` — 16/16 tetap PASSED (batch ini nggak nyentuh logic engine sama sekali).
- Dicek log server Streamlit — nggak ada error/traceback selama seluruh sesi tes.

### Keterbatasan yang masih ada (jujur, biar jelas)

- "Bypass Payment" itu BENERAN cuma bypass — belum ada payment gateway asli (Midtrans/Xendit dkk) di baliknya. Tombol "Bayar Sekarang" sengaja di-disable sebagai placeholder visual doang.
- Auto-scroll horizontal pas buka-semua sudah dites & jalan di viewport desktop biasa (1400px) dengan 5 amplop — belum dites di viewport HP/tablet, dan belum dites dengan skenario 15 amplop penuh (skr baru ada 5 sistem yang punya engine).

## Status fitur (per 26 Sep 2026)

### Sudah jadi

- **5 engine berbasis tanggal lahir — SEMUA SUDAH JADI & TERVALIDASI** (bukan stub lagi):
  - `engine/zodiak.py` — 12 zodiak + elemen.
  - `engine/shio.py` — 12 shio, pakai tabel tanggal Imlek 1945-2020 (sumber: themalatree.com, tervalidasi silang), raise `ValueError` kalau tahun lahir di luar 1945-2020 (bukan ditebak).
  - `engine/weton.py` — hari + pasaran + neptu, anchor tervalidasi ke 17 Agustus 1945 = Jumat Legi neptu 11 (sumber berita independen).
  - `engine/numerologi.py` — Life Path Number (1-9, 11/22/33 Master Number tidak direduksi). Expression Number (butuh nama lengkap) sengaja masih stub — belum ada keputusan scope, alur data saat ini cuma nanya tanggal lahir.
  - `engine/matrix_destiny.py` — HANYA titik inti/arketipe utama (skala 1-22) dari 8 titik octagon Matrix Destiny yang sebenarnya. 7 titik lain (sosial, fisik, spiritual, garis cinta, garis uang, ekor karma, garis leluhur) BELUM diimplementasikan — nunggu ada 1 sumber/kursus spesifik yang mau dijadikan acuan resmi, karena rumusnya beda-beda antar sumber.
  - Semua 5 engine punya test otomatis di `tests/test_*.py` (16 test, semua PASSED), plus dites manual lewat browser beneran (bukan cuma pytest).
- **Kamus konten lengkap (`content/interpretations/`) — 63 paragraf, semua sudah ditulis**:
  - Zodiak (12), Shio (12), Weton (5 — dikelompokkan per PASARAN: Legi/Pahing/Pon/Wage/Kliwon, BUKAN per neptu atau kombinasi hari+pasaran; keputusan ini karena secara tradisi primbon, pasaran yang dipakai buat baca watak, neptu lebih ke hitungan kecocokan/hari baik), Numerologi (12: 1-9 + 11/22/33), Matrix Destiny (22).
  - Tiap kategori formatnya sama: tagline, chip, title, "Siapa Kamu", "Kekuatan & yang Perlu Dijaga", quote, "PR Kecil Buat Kamu" — bahasa halus/sopan, tidak menyakiti, sepanjang mungkin sesuai instruksi Stev.
  - Weton pakai placeholder `{hari}`/`{neptu}` di title & paragraf pertama, di-`.format()` saat dipakai karena hari & neptu spesifik per orang meski pasarannya sama.
- **Wiring engine → konten → UI — SUDAH JADI, hasil di halaman reveal SEKARANG PERHITUNGAN ASLI** (bukan dummy 1 contoh tetap lagi):
  - `content/result_builder.py` — `compute_raw_result()` manggil engine yang sesuai berdasarkan tanggal lahir yang dikumpulkan di halaman loading; `build_display_data()` gabungin hasil mentah + kamus konten jadi dict siap-tampil.
  - `views/loadingpage.py` — begitu animasi 1 titik selesai, hasil ASLI dihitung & disimpan ke `session_state.loading_results` (bukan placeholder lagi untuk 5 sistem ini).
  - `views/revealpage.py` — `_render_detail()` pakai `_result_for()` (hasil asli, fallback ke `DUMMY_RESULTS` lama kalau belum ada hasil tersimpan — sekarang cuma kepake kalau sesi lompat ke halaman ini tanpa lewat alur loading beneran, bukan lewat tombol debug lagi karena tombol itu sudah dihapus batch ini).
  - Sudah dites end-to-end lewat Playwright beneran berkali-kali dengan tanggal 5 Desember 1992 — hasil selalu persis sesuai perhitungan manual.
- **Alur screening + hasil sekarang bisa dites penuh tanpa infrastruktur asli** (`TESTING_MODE` di `settings.py`, lihat bagian "Batch baru" di atas untuk detail): skip email/mode, payment-bypass, buka-semua-amplop sekuensial dengan auto-scroll, tombol reveal-lagi.
- Homepage (`app.py`, tab "Beranda") — hero, chip 15 sistem, section "Tiga Langkah", "Satu Data Banyak Cara Pandang", "Contoh Laporan", CTA penutup.
- Tab "Preview Form Screening" — layout 3 langkah — **UI doang, logic belum jalan**.
- Deploy pipeline GitHub → Streamlit Cloud sudah jalan.
- **63 gambar "kartu simbol"** (12 zodiak, 12 shio, 5 weton, 12 numerologi, 22 matrix destiny) — sudah diupload Stev ke `assets/cards/` di GitHub, sudah diverifikasi penamaan filenya persis sesuai spec.
- **Integrasi gambar kartu ke UI**:
  - `utils/card_images.py` — helper load gambar kartu jadi data URI/bytes, cached.
  - `views/revealpage.py` — kartu detail nampilin gambar kartu asli, ukuran 440x600, tombol "Simpan Gambar Kartu" (download PNG asli), amplop yang sudah dibuka punya toggle "Buka Amplop"/"Tutup Amplop", plus tombol "Buka Semua Amplop" (buka berurutan otomatis).
  - `views/loadingpage.py` — kartu teaser (blur 3.5px) juga pakai gambar kartu asli.

### Belum jadi (stub / belum ada)

- `synthesis/synthesizer.py` — masih stub (fitur "mixing logic" antar sistem, mis. kesamaan Sagitarius+Api dengan Monyet — sudah dibahas konsepnya sama Stev, butuh tambahan field `tags` di tiap entri konten, sengaja DITUNDA sampai konten per-sistem selesai semua).
- Sistem selain 5 yang sudah lengkap:
  - BaZi, Zi Wei Dou Shu, Human Design — butuh jam+lokasi lahir presisi, kompleksitas tinggi. **DITUNDA** ("nanti aja", keputusan Stev 26 Sep 2026).
  - MBTI, Big Five, Enneagram, DISC, Love Language — butuh sistem kuesioner yang belum ada. **DITUNDA** ("nanti aja").
  - Golongan Darah — cuma lookup input langsung (A/B/AB/O), belum dibangun, belum termasuk batch mana pun.
  - Tarot — keputusan Stev: metode **acak/random tiap dibuka** (bukan dari tanggal lahir), belum dibangun.
- Verifikasi email OTP asli (Resend/Brevo) — skr masih di-skip lewat `TESTING_MODE`.
- Koneksi form ke Supabase.
- Logic user lama vs baru (by email).
- **Payment gateway asli (Midtrans/Xendit)** — skr masih placeholder "Bypass Payment" via `TESTING_MODE`, tombol "Bayar Sekarang" sengaja disabled.
- Auto-kirim hasil ke email setelah bayar — baris "Hasil sudah dikirim ke email kamu" di `revealpage.py` masih teks statis, belum ada logic email beneran.
- Toggle Global vs Mingguan yang beneran jalan (AI pipeline + cache + fallback 3 lapis) — Mode Mendalam & Lengkap juga masih belum ada enginenya (baru Mode Instan).
- Reminder email bulanan + job hapus data 3 bulan.
- Fitur cek jodoh/kompatibilitas.
- Badge diskon & harga di halaman paywall.
- Revisi hero + dropdown bahasa (lihat bagian "Revisi yang ditahan" di atas).
- Sistem di luar 5 yang sudah ada gambar kartu (BaZi, Zi Wei, Human Design, MBTI, Big Five, Enneagram, DISC, Golongan Darah, Love Language, Tarot) — belum ada konten dummy panjang maupun gambar kartu.
- Auto-scroll horizontal grid amplop belum dites di viewport HP/tablet, dan belum dites skenario 15 amplop penuh.

## Keputusan bisnis/produk yang sudah difiksasi

- Tanpa login — identifikasi via email, bukan WhatsApp (alasan biaya OTP).
- Bayar dulu baru bisa lihat hasil lengkap (no free tier penuh).
- Hasil ditampilkan di web + dikirim ke email.
- Supabase buat data storage, retensi 3 bulan + backup bulanan.
- Konten mingguan digenerate via AI: batch per kategori, personalisasi 1x/minggu per user pakai data non-PII, fallback 3 lapis LLM gratis sebelum jatuh ke template murni.
- Copy website: bahasa Indonesia umum & sopan (bukan gaul/slang), tanpa em dash.
- Repo GitHub terpisah dari Z-QUANT, tapi 1 akun GitHub yang sama (`venray92`).
- Scope 15 sistem total dipecah jadi 5 kategori berdasarkan kebutuhan data (keputusan 26 Sep 2026): (A) murni tanggal lahir — Zodiak/Shio/Weton/Numerologi/Matrix Destiny, dikerjakan duluan & sudah selesai; (B) butuh jam+lokasi presisi — BaZi/Zi Wei/Human Design, ditunda; (C) butuh kuesioner — MBTI/Big Five/Enneagram/DISC/Love Language, ditunda; (D) input langsung — Golongan Darah; (E) acak — Tarot.

## Aset gambar kartu — status lengkap (26 Sep 2026)

- Prompt AI-image buat 63 kartu (gaya kartu koleksi premium, frame beda-beda per sistem) sudah selesai dibikin, digenerate satu-satu oleh Stev di AI image tool eksternal.
- Struktur final di GitHub: `assets/cards/{zodiak,shio,weton,numerologi,matrix_destiny}/`, semua lowercase, matrix_destiny pakai prefix nomor `01_..22_`.
- Sudah diintegrasikan ke `revealpage.py` dan `loadingpage.py`, dan sekarang muncul sesuai hasil perhitungan ASLI (bukan 1 contoh tetap lagi).
- Next kalau mau lanjut sistem lain: bikin prompt gambar buat 10 sistem sisanya (BaZi, Zi Wei, Human Design, MBTI, Big Five, Enneagram, DISC, Golongan Darah, Love Language, Tarot) — belum dimulai.

## File baru di batch ini (26 Sep 2026) — perlu diupload ke GitHub

- `settings.py` (di root, sejajar `app.py`) — flag `TESTING_MODE`.

## File yang diedit di batch ini — perlu di-replace isinya di GitHub

- `app.py` — hapus expander debug "Testing sementara" + dead code import zodiak yang nggak kepake.
- `views/reveal_yourself.py` — fix CSS gap OTP, pakai `TESTING_MODE` buat skip email/mode, tambah 2 key baru ke reset list.
- `views/loadingpage.py` — dialog akhir loading diganti jadi payment-bypass placeholder (bukan auto-continue lagi).
- `views/revealpage.py` — grid amplop jadi scrollable, tombol "Buka Semua Amplop" + dialog konfirmasi + buka sekuensial otomatis + auto-scroll, tombol "Reveal Lagi", fix bug tombol "nyangkut" (lihat lesson learned).

## Next step yang disarankan

Alur screening → loading → hasil sekarang bisa dites/didemo penuh dari awal sampai akhir tanpa infrastruktur asli (berkat `TESTING_MODE`). Kandidat pekerjaan berikutnya (belum diputuskan, tunggu arahan Stev):
1. Mulai bangun 10 sistem sisanya secara bertahap (per keputusan Stev: gradual, bukan sekaligus) — perlu tentu urutannya duluan yang mana.
2. Mulai kerjakan `synthesis/synthesizer.py` (mixing logic antar sistem) sekarang bahwa konten 5 sistem sudah ada.
3. Gabungkan revisi hero+dropdown bahasa yang masih ditahan.
4. Mulai kerjakan infrastruktur non-engine (Supabase, OTP email, payment gateway) yang selama ini belum disentuh sama sekali — begitu ini beres, `TESTING_MODE` di `settings.py` tinggal di-set `False`.
