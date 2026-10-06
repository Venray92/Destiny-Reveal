# Folder Structure, Destiny Reveal

Status (6 Okt 2026): semua 15 sistem sumber kontennya 100% JSON. Kamus .py lama dan views lama sudah dihapus. UI hidup cuma `views/home_v2.py` + `components/`.

```
destiny-reveal/
├── app.py                      (entry, navbar, toast, render home_v2)
├── settings.py
├── assets/css/app.css
├── components/                 (UI hidup: modal Reveal Dirimu, mini modal, navbar, dll)
│   ├── modal.py  modal_steps.py  modal_detail.py  mini_modals.py
│   ├── navbar.py  sections.py  solo_reveal.py  compat.py  combo.py
│   ├── auth.py  pricing_modal.py  profile.py  help_modals.py  info_modals.py  feature_modals.py
│   └── common.py  data.py  dialog_bus.py  flow_state.py
├── content/
│   ├── interpretations/
│   │   ├── titles.json         (judul, tagline, chip, ringkas per entri)
│   │   └── <sistem>/           (profile.json, daily/weekly/monthly.json bila ada)
│   ├── profile_loader.py       (format Mode-1: 5 sistem tanggal lahir)
│   ├── profile_flat.py         (format flat: 10 sistem lain)
│   ├── periodic.py             (get_daily / get_weekly / get_monthly / audit)
│   ├── safe_json.py            (loader JSON toleran)
│   ├── result_builder.py       (raw result + JSON -> display data)
│   └── questionnaires/
├── engine/                     (logic hitung per sistem)
├── utils/                      (card_images, date_format)
├── views/home_v2.py            (satu-satunya halaman)
├── synthesis/                  (stub, belum dipakai)
├── docs/                       (generator_guide, changelog, bugs-fixed, formula-notes)
└── tests/                      (zodiak, shio, weton, numerologi, matrix_destiny, periodic, profile_flat, modal_detail, mode1_flow, rotation, combo)
```

## Alur data
User input di modal -> `engine/*` hitung raw result -> `content/result_builder.py` ambil teks dari JSON (`profile_loader` / `profile_flat`) -> `components/*` render.

## Aturan
- Konten baru = JSON, bukan .py. Format lengkap di `docs/generator_guide.md`.
- Copy UI: Indonesia baku ramah ("kamu"), tanpa em dash/en dash.
