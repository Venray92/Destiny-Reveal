# Destiny Reveal: Progress Notes Library/Data + UI Terbaru (update 8 Okt 2026)
 
_Catatan ini MELENGKAPI dan, kalau bentrok, MENGGANTIKAN `progress-notes.md` untuk soal library/konten/data dan batch UI 7 Okt. Status: library 100% lengkap (A-M untuk semua 160 entri non-lahir + 5 sistem lahir). Deep Blueprint G-M belum ditampilkan di UI (fitur tersendiri, Stev yang implementasi nanti)._
 
## Status akhir library
- Semua konten 100% JSON. 15 sistem lengkap: Zodiak 12, Shio 12, Weton 35, Numerologi 12, Matrix Destiny 22, BaZi 10, Zi Wei 14, Human Design 5, Gol. Darah 4, MBTI 16, Enneagram 9, DISC 4, Love Language 5, Big Five 15, Tarot 78.
- 5 sistem lahir (Zodiak, Shio, Weton, Numerologi, Matrix): format `data[key].sections` A-M + `free`, dibaca `content/profile_loader.py`. A-F = Mode 1, G-M = Deep Blueprint.
- 10 sistem non-lahir: format `free{siapa_kamu, atribut_1, atribut_2, quote}` + `paid{kekuatan_yang_perlu_dijaga, pr_kecil_buat_kamu, karir, asmara, keuangan, kesehatan, shadow_work, nasihat_strategis}`, dibaca `content/profile_flat.py` (`get_profile` dan `get_big_five` mengembalikan `"entry"`).
- **E (`shadow_work`) dan F (`nasihat_strategis`) sudah ditulis untuk semua 160 entri non-lahir** (7 Okt). Teks Tarot/Zi Wei/MBTI-F/Big Five agak lebih pendek (~520-900 karakter) dari A-D (~1100-1200); belum dipanjangkan.
- **Deep Blueprint G-M untuk 10 sistem sudah ada** (digenerate lewat Gemini, diaudit): `<sistem>/deep.json` untuk 9 sistem + `tarot/deep_{major,wands,cups,swords,pentacles}.json`. Kunci = kunci entri profile. 7 field per entri: `ringkasan` (G), `karir_deep` (H), `asmara_deep` (I), `rezeki_deep` (J), `emosi_trigger` (K), `blindspot` (L), `latihan_harian` (M); tiap field 8 kalimat, ~900-1500 karakter. **Belum dibaca kode mana pun**; menunggu Stev implementasi fiturnya.
- Audit 7 Okt di clone segar: semua JSON valid, profile dan deep cocok per sistem (Tarot 22+14x4 = 78), E/F ada di semua entri, `titles.json` 15 sistem. pytest: 200 pass.
- Jebakan upload yang pernah kejadian (cek kalau ada yang aneh): `profile_flat.py` salah folder (`components/` bukan `content/`), `tarot_major.json` salah isi (isinya Big Five), `bazi/deep.json` JSON rusak. Semua sudah diperbaiki.
## Combo (kartu pelangi)
- `components/combo.py` `build_combo(system, raw)` untuk 12 sistem. BaZi, Gol. Darah, Tarot **tidak punya combo** (1 variabel; Tarot spread pakai `components/tarot_combo.py`). Human Design combo tidak bisa dites di sandbox.
- Tampil di detail Reveal dan di bawah analisis A-F hasil Solo Reveal (`.dh-dt-combo`). Kalau Stev mau combo untuk BaZi/Gol. Darah/Tarot Solo, perlu konten baru.
## Matriks periodik (data siap)
- Daily: Zodiak, Shio, Weton, Numerologi (+ Tarot harian terpisah). Weekly: Zodiak, Shio, Weton, Numerologi, Tarot. Monthly: Zodiak, Shio, Numerologi, BaZi, Zi Wei, Tarot.
- Statis: Matrix Destiny, Human Design, MBTI, Big Five, Enneagram, DISC, Love Language, Gol. Darah. Kunci periodik di `content/periodic.py`, kalender WIB.
- Daftar "paling akurat" versi Stev (hindari kata "akurat" di copy): Daily Zodiak/Weton/Shio/Tarot; Weekly Tarot/Zodiak/Weton; Monthly Tarot/Zodiak/Shio/Numerologi/BaZi/Zi Wei.
- Data disimpan belum dipakai UI: `shio/weekly.json`, `numerologi/daily.json`, `numerologi/weekly.json`.
## Solo Reveal (update)
- Sekarang **semua 15 sistem aktif** (bukan 5 lagi). Hasil A-F; 10 sistem non-lahir dibaca dari `entry` lewat `_entry_aspek` di `components/solo_reveal.py` (E dan F pakai `shadow_work` dan `nasihat_strategis`).
- Alur: pilih sistem, (kuesioner untuk 5 sistem psikologi), bayar 150 ✨, **loading ~3 detik (baru)**, hasil. Saldo dipotong setelah hasil berhasil dihitung.
## Batch UI 7 Okt 2026 (round 6), dikirim sebagai 10 file, tes UI Playwright + pytest 200 pass
- `components/close_confirm.py` (BARU): konfirmasi tutup bertema untuk semua modal hasil akhir (Solo Reveal, Reveal Dirimu, Cek Kecocokan, Tarot harian, Tarot spread, Ramalan Harian). Jalur: tombol Selesai & Tutup (layar konfirmasi di dalam dialog) dan tombol X (`on_dismiss` -> `dh_cc_reopen` -> `navbar.py` buka ulang dialog). X di layar konfirmasi = keluar beneran.
- Tombol "Selesai & Tutup" baru: Tarot harian dan Tarot spread (paling bawah), Reveal Dirimu (kanan "Scan Orang Lain"; baris bawah disusun ulang: teks "Tersimpan di akun" naik).
- Cek Kecocokan: teks Kekuatan, Tantangan, Nasihat Strategis dipanjangkan (2-3 kalimat per poin, nasihat 5 poin per jenis hubungan + kalimat penutup per konteks).
- Check-in dan klaim reward Streak: toast diganti popup bertema yang tutup sendiri 2,5 detik (`dh_sk_pop`).
- File: `components/{close_confirm,solo_reveal,modal_steps,modal,mini_modals,feature_modals,compat,navbar}.py`, `assets/css/home_v2.css`, `tests/test_close_confirm.py`. Status upload belum dikonfirmasi Stev.
## Item lama di `progress-notes.md` yang SUDAH BASI
- "Tarot/Gol. Darah belum dibangun", "narasi 5 kuesioner belum ditulis", "BaZi/Zi Wei/Human Design belum", "`synthesis/synthesizer.py` stub", "`TESTING_MODE`/`settings.py`", "`daily.json` belum ada": semua sudah ada/dihapus.
- "Solo hanya 5 sistem aktif, 10 lainnya dalam pengembangan": basi, sekarang 15 aktif.
- "Beberapa seksi Solo kosong untuk BaZi/Zi Wei/Gol. Darah/Tarot": basi, E/F sudah terisi.
- Daftar file legacy konten `.py`, `questionnaires/mbti.py`, dst: sudah dibersihkan, jangan diupload lagi.
- Catatan "update progress-notes hanya dengan izin eksplisit" tetap berlaku; update ini atas permintaan Stev 8 Okt.
## Open items
- Implementasi tampilan Deep Blueprint G-M (Stev, nanti). Tombol Blueprint di `feature_modals.py` masih ke Mode 3 jalur lama.
- Gambar Tarot minor (56 kartu): PR dari Stev. `loadingcard.png` masih ada teks baked-in. `tarot_combo.json` konten starter.
- Nama "Stardust" di FAQ/help/pricing/tier masih belum diputuskan diganti atau tidak.
- Tes live Bulan dengan jam lahir dan Human Design (swisseph tidak ada di sandbox).
- Backend B1-B5 menunggu jawaban Stev: Supabase, OTP email, Stardust, payment gateway, referral. Saldo masih dummy (`DUMMY_SALDO = 20000`).
- Alur Mode 2/3 Reveal belum dibangun. Weton bulanan dilewati. Zi Wei: aturan istana transit disederhanakan.
- Review manual konten oleh Stev: belum. Opsional: panjangkan teks E/F yang lebih pendek.
- Ide fitur baru (8 Okt, dari gambar tabel "tanpa AI"): Career Path Finder, Money Personality, Daily Affirmation, Habit Tracker, Family Match, Energy Forecast, Sleep Optimizer, Breakup Recovery. Penilaian kelayakan ada di chat 8 Okt; belum ada keputusan dikerjakan.