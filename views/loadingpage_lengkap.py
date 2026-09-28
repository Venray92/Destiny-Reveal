"""
Halaman Loading PAGE 3 — Mode Lengkap (semua 15 sistem sekaligus).

Beda sama Mode Instan (loadingpage.py, floating window per-field muncul
SATU-SATU pas titik yang butuh data itu kena giliran) — Mode Lengkap
SEMUA data (termasuk yang dibutuhkan 5 chip terakhir: BaZi, Zi Wei, Human
Design, Golongan Darah, Tarot) ditanya SEKALIGUS di SATU form di awal,
per instruksi Stev (27 Sep 2026 malam): "kalau dia pilih mode lengkap itu
smua pertanyaan yang dibutuhkan di tanya diawal". Mock 3 layar (form
intake, floating fallback jam lahir, reveal 15 amplop) sudah di-ACC.

Alur (state machine):
  intake (form 1 layar: tanggal lahir + nama [wajib], jam lahir [opsional,
  dropdown estimasi], kota lahir [opsional], golongan darah [opsional])
  -> jam_fallback (floating window, CUMA muncul kalau user pilih "Tidak
  Tahu Sama Sekali" buat jam lahir -- prinsip "hasil gak boleh kosong"
  karena user bayar buat laporan ini: kalau nggak mau pilih estimasi di
  floating window ini juga, sistem milih otomatis/acak)
  -> bio_animating (animasi kartu titik SAMA PERSIS kayak Mode Instan,
  lewat _animate_point() yang di-import dari loadingpage.py, buat 10
  sistem berbasis data: Zodiak, Shio, Weton, Numerologi, Matrix Destiny,
  BaZi, Zi Wei, Human Design, Golongan Darah, Tarot)
  -> lepas ke views/loadingpage_mendalam.py (dr_page="loading_mendalam")
  buat kuesioner 5 sistem (MBTI, Big Five, Enneagram, DISC, Love
  Language) -- TIDAK perlu kode baru sama sekali di sini, karena
  _quiz_systems() di loadingpage_mendalam.py sudah hardcode ke 5 sistem
  yang SAMA (RY_MODES kunci "mendalam"). Floating window payment akhir
  (_final_dialog, dari loadingpage.py) juga ke-reuse otomatis lewat jalur
  itu -- TIDAK ada floating payment dobel.

PRINSIP "HASIL GAK BOLEH KOSONG" (instruksi eksplisit Stev, 27 Sep 2026
malam) -- laporan ini berbayar, jadi walau jam lahir & golongan darah
sengaja dibikin opsional (banyak orang gak tau persis), user TETAP harus
dapat SATU hasil (bukan amplop kosong/terkunci):
- Jam lahir "Tidak Tahu Sama Sekali" -> floating window jam_fallback
  kasih pilihan cepat (Pagi/Siang/Sore/Malam) ATAU tombol "Pilihkan
  Otomatis (Acak)" -- salah satu WAJIB dipilih (dialog dismissible=False),
  jadi jam_lahir SELALU ke-isi sebelum lanjut ke animasi.
- Golongan darah "Tidak Tahu" -> langsung diacak (random.choice A/B/AB/O)
  pas submit form, TANPA floating window tambahan (beda dari jam lahir --
  golongan darah cuma 4 pilihan diskrit, gak ada konsep "perkiraan
  kasar" yang natural kayak rentang waktu pagi/siang/sore/malam).
- `loading_data["jam_lahir_estimasi"]` (bool) disimpan biar revealpage.py
  bisa nandain hasil Zi Wei/Human Design sebagai "berdasarkan estimasi"
  kalau jamnya bukan jam pasti asli user.

BAHASA: "Tidak Tahu" (bukan "Gak Tau"/slang) di semua UI, dan TIDAK ada
kata yang mengisyaratkan pembayaran di floating window jam_fallback --
sesuai revisi eksplisit Stev soal 2 hal ini.
"""

import random
from datetime import time

import streamlit as st

from views.loadingpage import (
    _animate_point,
    _inject_style,
    _input_summary_html,
    _render_nama_input,
    _render_tanggal_inputs,
    _validate_nama,
)
from views.reveal_yourself import RY_MODES

# 5 sistem kuesioner (Kelompok D) ditangani TERPISAH lewat
# views/loadingpage_mendalam.py yang sudah ada -- di sini cuma perlu tau
# namanya biar bisa DIKELUARIN dari daftar titik animasi kartu (fase
# bio_animating), bukan buat diproses ulang di sini.
_QUIZ_SYSTEMS = {"MBTI", "Big Five", "Enneagram", "DISC", "Love Language"}

# Pilihan jam lahir di form intake -> jam representatif (buat dihitung)
# + apa hasilnya perlu ditandai "estimasi" atau nggak.
JAM_PILIHAN = {
    "Pagi (sekitar 08:00)": (time(8, 0), True),
    "Siang (sekitar 13:00)": (time(13, 0), True),
    "Sore (sekitar 16:00)": (time(16, 0), True),
    "Malam (sekitar 20:00)": (time(20, 0), True),
}
JAM_OPSI_MANUAL = "Tahu Jam Pastinya (Isi Manual)"
JAM_OPSI_TIDAK_TAHU = "Tidak Tahu Sama Sekali"
JAM_OPSI_LIST = (
    [JAM_OPSI_MANUAL] + list(JAM_PILIHAN.keys()) + [JAM_OPSI_TIDAK_TAHU]
)

GOLDA_OPSI_LIST = ["A", "B", "AB", "O", "Tidak Tahu"]


def _lengkap_points():
    for key, _title, _desc, chips in RY_MODES:
        if key == "lengkap":
            return list(chips)
    return []


def _bio_points():
    """10 sistem berbasis data yang diproses di halaman INI (di luar 5
    sistem kuesioner, yang ditangani loadingpage_mendalam.py setelahnya).
    Urutannya ikut urutan RY_MODES "lengkap" (Kelompok A -> B -> E -> F),
    cuma sistem kuesionernya di-skip di sini."""
    return [s for s in _lengkap_points() if s not in _QUIZ_SYSTEMS]


def _ensure_state():
    if "lengkap_phase" not in st.session_state:
        st.session_state.lengkap_phase = "intake"
        st.session_state.lengkap_bio_idx = 0
        st.session_state.loading_results = {}
        st.session_state.loading_data = {}
        # Amplop di revealpage.py ngikut loading_points -- diisi LANGSUNG
        # ke urutan LENGKAP 15 sistem (bukan cuma 10 sistem yang diproses
        # di halaman ini), soalnya 5 sistem kuesioner nanti diproses di
        # halaman LAIN (loadingpage_mendalam.py) yang gak nyentuh
        # loading_points sama sekali -- kalau gak diisi di sini dari
        # awal, amplop kuesionernya gak bakal ketampil holistik bareng.
        st.session_state.loading_points = _lengkap_points()


@st.dialog("Yakin Tidak Tahu Jam Lahir?", dismissible=False)
def _jam_fallback_dialog():
    st.markdown(
        '<div style="font-size:13.5px;color:#3a352c;line-height:1.6;margin-bottom:16px;">'
        'Hasil tidak bisa kosong. Akan lebih baik jika kamu bisa memberikan perkiraan '
        'waktu di bawah ini, supaya Zi Wei dan Human Design tetap bisa dihitung (hasilnya '
        'akan ditandai sebagai "estimasi"). Jika tidak, hasil akan dipilih secara acak '
        'dengan kemungkinan terbesar.</div>',
        unsafe_allow_html=True,
    )

    def _pilih(jam_value):
        st.session_state.loading_data["jam_lahir"] = jam_value
        st.session_state.loading_data["jam_lahir_estimasi"] = True
        st.session_state.lengkap_phase = "bio_animating"
        st.rerun()

    c1, c2 = st.columns(2)
    with c1:
        if st.button("🌅 Pagi (~08:00)", key="fb_pagi", use_container_width=True):
            _pilih(time(8, 0))
        if st.button("🌇 Sore (~16:00)", key="fb_sore", use_container_width=True):
            _pilih(time(16, 0))
    with c2:
        if st.button("☀️ Siang (~13:00)", key="fb_siang", use_container_width=True):
            _pilih(time(13, 0))
        if st.button("🌙 Malam (~20:00)", key="fb_malam", use_container_width=True):
            _pilih(time(20, 0))
    st.write("")
    if st.button("🎲 Pilihkan Otomatis (Acak)", key="fb_random", type="primary",
                  use_container_width=True):
        _pilih(random.choice([time(8, 0), time(13, 0), time(16, 0), time(20, 0)]))


def _render_intake_form():
    # BUG YANG DIPERBAIKI (28 Sep 2026, dilaporkan Stev sebagai "kotak
    # kosong nyangkut di atas form"): SEBELUMNYA div pembungkus kartu
    # dibuka lewat st.markdown('<div class="lengkap-intake-card">') dan
    # baru DITUTUP lewat st.markdown('</div>') di paling bawah, jauh
    # setelah semua widget Streamlit lain (selectbox, text_input, dst) di
    # antaranya. Ini TIDAK bekerja seperti div HTML biasa di halaman
    # statis — Streamlit ngirim TIAP panggilan st.markdown() sebagai
    # fragment HTML TERPISAH yang di-render/parse browser SENDIRI-SENDIRI,
    # jadi tag <div> yang dibuka di satu panggilan otomatis DITUTUP
    # SENDIRI oleh browser di akhir fragment ITU JUGA (karena nggak ada
    # apa-apa lagi di dalam fragment yang sama) -- hasilnya div itu
    # ke-render KOSONG (cuma keliatan padding-nya doang, kotak kosong
    # ngambang), sementara semua konten (judul, form, dst) yang
    # "harusnya" ada di dalamnya sebenarnya jadi elemen-elemen TERPISAH
    # yang cuma kebetulan tampil di bawahnya karena alur dokumen normal,
    # bukan beneran nested di dalam div itu.
    #
    # FIX: pakai st.container(key=...) BENERAN (bukan div HTML manual)
    # buat bungkus semua widget di dalam satu blok `with` -- container
    # Streamlit ini beneran satu elemen DOM utuh yang membungkus semua
    # childnya, jadi CSS lewat class .st-key-<key> kena ke satu kotak
    # yang benar-benar berisi semua konten di dalamnya, bukan kotak
    # kosong terpisah.
    st.markdown(
        """
        <style>
        .st-key-lengkap_intake_card { max-width: 620px; margin: 30px auto; background: #fffaf2;
            border: 2px solid #f0e6d5; border-radius: 22px; padding: 34px 36px; }
        .lengkap-intake-title { font-family: 'Fraunces', serif; font-size: 27px; font-weight: 800;
            color: #1c1a17; text-align: center; margin-bottom: 6px; }
        .lengkap-intake-sub { font-size: 13.5px; color: #6b6459; text-align: center;
            margin-bottom: 26px; line-height: 1.6; }
        .lengkap-intake-section-label { display:flex; align-items:center; gap:8px; font-size: 12.5px;
            font-weight: 800; letter-spacing: 0.03em; text-transform: uppercase; color: #b8562f;
            margin: 22px 0 8px 0; }
        .lengkap-intake-hint { font-size: 12px; color: #9a9282; margin: -2px 0 10px 0; line-height: 1.5; }
        </style>
        """,
        unsafe_allow_html=True,
    )

    with st.container(key="lengkap_intake_card"):
        st.markdown('<div class="lengkap-intake-title">Lengkapi Data Dirimu</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="lengkap-intake-sub">Isi semua data di bawah sekali saja. Setelah ini, '
            'semua 15 sistem akan langsung diproses tanpa perlu tanya-tanya lagi di tengah '
            'jalan.</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            '<div class="lengkap-intake-section-label">'
            '<span class="material-symbols-outlined" style="font-size:16px;">calendar_month</span>'
            'Tanggal Lahir dan Nama (Wajib)</div>',
            unsafe_allow_html=True,
        )
        tanggal_value = _render_tanggal_inputs()
        st.write("")
        nama_value = _render_nama_input()

        st.markdown(
            '<div class="lengkap-intake-section-label">'
            '<span class="material-symbols-outlined" style="font-size:16px;">schedule</span>'
            'Jam Lahir (Opsional, untuk BaZi, Zi Wei dan Human Design)</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<div class="lengkap-intake-hint">Tidak tahu jam pastinya? Tidak masalah, pilih '
            'perkiraan di bawah ini. Hasilnya tetap dihitung, hanya akan ditandai sebagai '
            '"estimasi".</div>',
            unsafe_allow_html=True,
        )
        jam_opsi = st.selectbox(
            "Jam Lahir", JAM_OPSI_LIST, key="lengkap_jam_opsi", label_visibility="collapsed",
        )
        jam_manual_value = None
        if jam_opsi == JAM_OPSI_MANUAL:
            jam_manual_value = st.time_input(
                "Jam Lahir Pasti", key="lengkap_jam_manual", label_visibility="collapsed",
            )

        st.markdown(
            '<div class="lengkap-intake-section-label">'
            '<span class="material-symbols-outlined" style="font-size:16px;">location_on</span>'
            'Kota Lahir (Opsional, untuk Akurasi Human Design)</div>',
            unsafe_allow_html=True,
        )
        kota_value = st.text_input(
            "Kota Lahir", placeholder="Contoh: Jakarta (kosongkan jika tidak tahu)",
            key="lengkap_kota", label_visibility="collapsed",
        ).strip()

        st.markdown(
            '<div class="lengkap-intake-section-label">'
            '<span class="material-symbols-outlined" style="font-size:16px;">water_drop</span>'
            'Golongan Darah (Opsional)</div>',
            unsafe_allow_html=True,
        )
        golda_opsi = st.selectbox(
            "Golongan Darah", GOLDA_OPSI_LIST, index=4,
            key="lengkap_golda", label_visibility="collapsed",
        )

        st.write("")
        submitted = st.button(
            "Mulai Proses Reveal", key="lengkap_submit", type="primary",
            icon=":material/arrow_forward:", use_container_width=True,
        )

    if not submitted:
        return

    err = _validate_nama(nama_value)
    if err:
        st.warning(err, icon=":material/error:")
        return

    data = st.session_state.loading_data
    data["tanggal_lahir"] = tanggal_value
    data["nama_lengkap"] = nama_value
    if kota_value:
        data["kota_lahir"] = kota_value
    if golda_opsi == "Tidak Tahu":
        # Golongan darah cuma 4 pilihan diskrit -- gak ada konsep
        # "perkiraan kasar" kayak rentang waktu jam lahir, jadi langsung
        # diacak di sini (TANPA floating window tambahan), tetap demi
        # prinsip "hasil gak boleh kosong".
        data["golongan_darah"] = random.choice(["A", "B", "AB", "O"])
    else:
        data["golongan_darah"] = golda_opsi

    if jam_opsi == JAM_OPSI_MANUAL:
        data["jam_lahir"] = jam_manual_value
        data["jam_lahir_estimasi"] = False
        st.session_state.lengkap_phase = "bio_animating"
        st.rerun()
    elif jam_opsi == JAM_OPSI_TIDAK_TAHU:
        st.session_state.lengkap_phase = "jam_fallback"
        st.rerun()
    else:
        jam_value, is_estimasi = JAM_PILIHAN[jam_opsi]
        data["jam_lahir"] = jam_value
        data["jam_lahir_estimasi"] = is_estimasi
        st.session_state.lengkap_phase = "bio_animating"
        st.rerun()


def render():
    _ensure_state()
    _inject_style()

    # BUG YANG DIPERBAIKI (28 Sep 2026 siang, dilaporkan Stev lewat 2
    # screenshot -- kartu/teks form "Lengkapi Data Dirimu" masih nyangkut
    # kebawa ke layar animasi titik/scan di bawahnya, padahal fase sudah
    # pindah): akar masalahnya SAMA PERSIS kayak bug tombol "Buka Semua
    # Amplop" yang udah pernah diperbaiki di revealpage.py (lihat komentar
    # di sana) -- _render_intake_form() sebelumnya dipanggil LANGSUNG tanpa
    # placeholder st.empty() yang dikosongkan eksplisit begitu fase pindah.
    # Streamlit TIDAK otomatis membersihkan widget lama di slot itu kalau
    # kondisinya jadi False tanpa ada sinyal "delta kosong" yang dikirim ke
    # slot yang sama -- jadi container form (beserta semua widget di
    # dalamnya) bisa nyangkut/ke-render ulang di rerun berikutnya walau
    # phase-nya udah bukan "intake" lagi.
    #
    # FIX: taruh SATU st.empty() placeholder tetap (posisi ini selalu
    # dipanggil di rerun manapun, apapun fasenya), isi kalau fase == intake,
    # ATAU eksplisit di-.empty()-kan kalau bukan -- persis pola yang sudah
    # terbukti jalan di revealpage.py punya "belum_dibuka".
    intake_slot = st.empty()
    if st.session_state.lengkap_phase == "intake":
        with intake_slot.container():
            _render_intake_form()
        return
    intake_slot.empty()

    if st.session_state.lengkap_phase == "jam_fallback":
        # Kartu/dots belum ada apa-apanya buat ditampilin di titik ini
        # (data masih dilengkapi) -- cukup panggil dialognya langsung,
        # sama polanya kayak fase "asking" di loadingpage.py.
        st.markdown(
            '<div style="text-align:center;">'
            '<div style="font-family:\'Fraunces\',serif;font-size:24px;font-weight:700;'
            'color:#1c1a17;">Melengkapi Data...</div></div>',
            unsafe_allow_html=True,
        )
        _jam_fallback_dialog()
        return

    points = _bio_points()
    total = len(points)
    idx = st.session_state.lengkap_bio_idx

    if idx >= total:
        # 10 sistem berbasis data kelar -- lepas ke halaman kuesioner
        # (loadingpage_mendalam.py) yang SUDAH ADA, biar 5 sistem
        # kuesioner + floating window payment akhir ke-reuse otomatis
        # tanpa kode baru.
        st.session_state.dr_page = "loading_mendalam"
        st.rerun()
        return

    current = points[idx]
    header_html = (
        '<div style="text-align:center;">'
        '<div style="font-family:\'Fraunces\',serif;font-size:30px;font-weight:700;color:#1c1a17;margin-bottom:8px;">'
        'Sedang Membaca Dirimu...</div>'
        f'<div style="font-size:14.5px;color:#6b6459;">Titik {idx + 1} dari {total} sedang diproses '
        '(bagian data dasar dari 15 sistem) — jangan tutup halaman ini ya.</div>'
        '</div>'
        f'{_input_summary_html()}'
        '<div style="height:16px;"></div>'
    )
    _animate_point(points, idx, header_html)
    st.session_state.lengkap_bio_idx += 1
    st.rerun()
