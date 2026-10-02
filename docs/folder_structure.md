# Folder Structure — Destiny Reveal

Status: 5 sistem berbasis tanggal lahir (Zodiak, Shio, Weton, Numerologi, Matrix Destiny) udah dirapihin. 10 sistem sisa (MBTI, Big Five, Enneagram, DISC, Love Language, BaZi, Zi Wei, Human Design, Golongan Darah, Tarot) masih 1 file per sistem, nyusul.

```
destiny-reveal/
├── app.py
├── settings.py
├── requirements.txt
├── README.md
├── docs/
│   ├── folder_structure.md
│   ├── changelog.md
│   ├── bugs-fixed.md
│   └── formula-notes.md
├── content/
│   ├── interpretations/
│   │   ├── zodiak/            (12 file, selesai dipecah)
│   │   ├── shio/               (12 file, selesai dipecah)
│   │   ├── weton/               (5 file, selesai dipecah)
│   │   ├── numerologi/         (12 file, selesai dipecah)
│   │   ├── matrix_destiny/     (22 file, selesai dipecah)
│   │   ├── mbti.py              (1 file gemuk, belum dipecah)
│   │   ├── big_five.py
│   │   ├── enneagram.py         (1 file gemuk, belum dipecah)
│   │   ├── disc.py
│   │   ├── love_language.py     (1 file gemuk, belum dipecah)
│   │   ├── bazi.py
│   │   ├── ziwei.py
│   │   ├── human_design.py
│   │   ├── golongan_darah.py
│   │   └── tarot.py
│   ├── questionnaires/
│   └── result_builder.py
├── engine/
│   ├── zodiak.py  shio.py  weton.py  numerologi.py  matrix_destiny.py
│   ├── mbti_scoring.py  big_five_scoring.py  enneagram_scoring.py
│   ├── disc_scoring.py  love_language_scoring.py
│   └── bazi.py  ziwei.py  human_design.py  tarot.py
├── utils/
│   ├── card_images.py
│   ├── date_format.py
│   └── matrix_destiny_diagram.py
├── views/
│   ├── loadingpage.py           (980 baris, belum dipecah)
│   ├── loadingpage_lengkap.py
│   ├── loadingpage_mendalam.py  (568 baris, belum dipecah)
│   ├── reveal_yourself.py       (506 baris, belum dipecah)
│   ├── revealpage.py            (1621 baris, belum dipecah)
│   └── tutorialpage.py
└── tests/
    ├── test_zodiak.py  test_shio.py  test_weton.py
    ├── test_numerologi.py  test_matrix_destiny.py
```

## Fungsi tiap folder
- `docs/` — Dokumentasi (changelog, bug-fix, formula)
- `content/` — Data 15 sistem (konten paragraf) + penghubung ke engine
- `engine/` — Logic hitung (zodiak, shio, dll)
- `utils/` — Helper (card image, date format)
- `views/` — UI Pages (Streamlit)
- `tests/` — Unit test

## Alur data
User input → `engine/*` hitung raw result → `content/result_builder.py` gabungin raw result + kamus konten → `views/*` render.
