# Formula Notes — Destiny Reveal

Detail rumus tiap sistem didokumentasikan langsung di docstring file engine masing-masing (udah ringkas, semua <130 baris):

- **Zodiak** → `engine/zodiak.py`
- **Shio** → `engine/shio.py` — pakai tanggal Imlek asli (bukan 1 Jan), sumber & cross-check ada di docstring.
- **Weton** → `engine/weton.py` — pasaran dihitung dari tanggal acuan 17 Agustus 1945 = Jumat Legi (neptu 11).
- **Numerologi** → `engine/numerologi.py` — Pythagoras, Master Number 11/22/33 nggak direduce lebih lanjut.
- **Matrix Destiny** → `engine/matrix_destiny.py` — metode resmi Natalia Ladini (versi Rusia), `titik_inti` = Titik E (Center), BUKAN shortcut jumlah digit.

Rujukan lengkap & contoh hitungan manual ada di memory project (`/areas/matrix-destiny-formula.md`, `/areas/weton-formula.md`, `/areas/numerologi-formula.md`, `/areas/zodiak-shio-formula.md`) dan `claude/progress-notes.md`.
