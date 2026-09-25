# Destiny Reveal

Web platform for self-discovery — combines Weton, Zodiac, Shio, BaZi, Numerology,
Matrix Destiny & personality tests into one personalized report.

Built with Streamlit + Supabase.

## Struktur

- `engine/` — perhitungan tiap sistem (pure function, testable)
- `synthesis/` — logika gabungin hasil lintas sistem
- `content/interpretations/` — teks interpretasi tiap hasil
- `tests/` — unit test buat validasi tiap engine
- `app.py` — entry point Streamlit
