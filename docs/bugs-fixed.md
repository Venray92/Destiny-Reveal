# Bug yang Sudah Diperbaiki — Destiny Reveal

## 26 Sep 2026 — Kartu selalu sama (generic) walau hasil beda
**Gejala:** Gambar kartu yang muncul di loading/reveal page SELALU sama per kategori sistem, nggak peduli hasil perhitungan aslinya. Misal teks bilang "Sagittarius" tapi kartunya tetap gambar Leo.
**Root cause:** `SYSTEM_CARD_IMAGE` di `utils/card_images.py` cuma punya satu path gambar tetap per kategori (bukan per hasil).
**Fix:** Tambah `card_relative_path_for_result(system, raw_result)` yang milih gambar dari hasil MENTAH (raw_result), bukan nama kategori doang.
**File:** `utils/card_images.py`

## 28 Sep 2026 — 10 dari 15 sistem jatuh ke fallback generic
**Gejala:** Amplop 10 sistem (BaZi/Zi Wei/Human Design/Golongan Darah/Tarot/MBTI/Big Five/Enneagram/DISC/Love Language) selalu nampilin pesan "belum selesai dibangun", padahal konten & engine-nya udah ada di repo.
**Root cause:** `content/result_builder.py` cuma nyambungin 5 sistem lama.
**Fix:** Nambahin import + branch logic buat 10 sistem sisanya di `compute_raw_result()` dan `build_display_data()`.
**File:** `content/result_builder.py`

## 2 Okt 2026 — Import path putus pasca-rename file
**Gejala:** App error `ModuleNotFoundError` abis rename file (`content_interpretations__bazi.py` → `bazi.py`, dst).
**Root cause:** Nama file di-rename tapi import path di 2 file pemanggil belum ikut diupdate.
**Fix:** Update import ke nama file baru.
**File:** `content/result_builder.py`, `utils/card_images.py`

## 2 Okt 2026 (ronde 2) — Dropdown Tahun kepotong, gak bisa discroll
**Gejala:** Dropdown dengan opsi banyak (mis. Tahun, ~95 opsi) kepotong dan nggak bisa discroll turun buat lihat opsi selanjutnya — user cuma lihat beberapa opsi teratas.
**Root cause:** `div[role="listbox"]` pakai `overflow: hidden !important`.
**Fix:** Ganti ke `overflow-y: auto` + `max-height: 260px` (border-radius tetap kepakai di container sendiri).
**File:** `assets/css/app.css` (dulu inline di `app.py`)
