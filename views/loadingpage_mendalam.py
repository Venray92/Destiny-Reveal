"""
Halaman Loading PAGE 2 — kuesioner Mode Mendalam (MBTI, Big Five,
Enneagram, DISC, Love Language).

Beda sama views/loadingpage.py (loading page 1, yang cuma nanya data
dasar kayak tanggal lahir lewat floating window): halaman ini beneran
nampilin SOAL kuesioner, per SISTEM (chip) sendiri-sendiri, satu LAYOUT
per sistem. Dalam 1 sistem, soal ditampilin per GRUP 10 (soal 1-10, lalu
klik "Lanjut", keluar 11-20, dst — kalau sisanya kurang dari 10, ya
keluar sebanyak sisanya). Skor dihitung lewat engine/*_scoring.py begitu
grup terakhir sistem itu selesai dijawab.

Alur (state machine):
  intro -> batch (ulang per grup 10 soal, per sistem) -> system_confirm
  (floating window "kuesioner sistem X selesai, siap lanjut ke sistem
  Y?", TIDAK bocorin hasil apapun) -> batch (sistem berikutnya) -> ...
  -> final (floating window payment, SAMA PERSIS kayak punya loading
  page 1 — lihat _final_dialog() yang di-import langsung dari
  views.loadingpage, bukan bikin ulang).

Revisi (27 Sep 2026 malam, ronde 2): versi SEBELUMNYA nampilin 1 soal
per layar buat SEMUA 157 soal berurutan tanpa jeda — menurut Stev bikin
kewalahan. Diganti jadi per-sistem (per chip) + per-grup-10 + ada
floating window "siap lanjut?" di antar sistem biar user bisa istirahat
sebentar. Kalau user pilih "Batal" di floating window itu, balik ke
Home (progress hilang, sesuai instruksi Stev — belum ada penyimpanan).

CSS (.ry-load-card, .ry-load-dot-row, dialog override dark-mode, dst) dan
helper _dots_html() DIPAKAI ULANG langsung dari views.loadingpage (bukan
disalin ulang) — biar "sama persis" gayanya kayak loading page 1.

KETERBATASAN per revisi ini (sengaja, biar jelas bukan tersembunyi):
- Kamus konten paragraf (karir/asmara/dll) buat 5 sistem ini BELUM
  ditulis, jadi di halaman hasil akhir (revealpage.py) amplopnya bakal
  nampilin tipe/skor mentahnya + pesan "detail lengkap segera hadir",
  bukan paragraf insight penuh kayak Zodiak dkk.
- Kalau user beneran keluar/refresh di tengah kuesioner sampai session
  Streamlit-nya ke-reset, progress hilang dan harus mulai dari grup
  soal pertama lagi — belum ada penyimpanan ke database (sesuai
  keputusan Stev: nunggu fitur profil+riwayat beneran dibangun nanti).
  Tombol "Batal" di floating window antar-sistem juga sengaja balik ke
  Home (bukan nyimpen progress), sesuai instruksi Stev.
- Chaining ke Mode Lengkap (loading page 1 lanjut otomatis ke loading
  page 2 tanpa floating payment dobel) SUDAH dikerjakan lewat
  views/loadingpage_lengkap.py (set dr_page = "loading_mendalam" begitu
  10 titik data non-kuesioner kelar) — halaman INI sendiri TIDAK
  diubah buat itu, karena _quiz_systems() di sini sudah mode-agnostic.

Revisi (27 Sep 2026 malam, ronde 3): tambah tombol "Lewati Semua Soal
(Testing)" (_render_testing_bypass_button / _bypass_semua_soal) di atas
tiap grup soal — testing-only (gated settings.TESTING_MODE), ngisi
otomatis semua soal yang masih kosong (sistem sekarang + sisanya)
dengan jawaban acak VALID, lalu langsung lompat ke floating window
payment (_final_dialog), biar nggak perlu jawab manual 157 soal tiap
mau ngetes. Juga fix bug CSS dark-mode di st.error (background item
pekat ikut skema warna OS/browser) — dipaksa terang senada warning box
oranye yang sudah ada (lihat _inject_style() di views/loadingpage.py).
"""

import random
import time

import streamlit as st

from content.result_builder import build_display_data, compute_quiz_raw_result
from content.questionnaires.big_five_soal import BIG_FIVE_QUESTIONS
from content.questionnaires.disc_soal import DISC_QUESTIONS
from content.questionnaires.enneagram_soal import ENNEAGRAM_QUESTIONS
from content.questionnaires.love_language_soal import LOVE_LANGUAGE_QUESTIONS
from content.questionnaires.mbti_soal import MBTI_QUESTIONS
from views.loadingpage import _dots_html, _final_dialog, _inject_style
from views.reveal_yourself import RY_MODES
from settings import TESTING_MODE

QUESTION_BANKS = {
    "MBTI": MBTI_QUESTIONS,
    "Big Five": BIG_FIVE_QUESTIONS,
    "Enneagram": ENNEAGRAM_QUESTIONS,
    "DISC": DISC_QUESTIONS,
    "Love Language": LOVE_LANGUAGE_QUESTIONS,
}

# Berapa soal ditampilin sekaligus dalam 1 layar/grup, per instruksi Stev
# ("misal mbti 1 layout klo ada 32 soal, 1-10 trus bawahnya ada button
# submit"). Grup terakhir tiap sistem otomatis lebih pendek kalau sisa
# soalnya kurang dari angka ini (mis. DISC 24 soal -> grup 10, 10, 4).
BATCH_SIZE = 10

FINAL_PAUSE_SECONDS = 2

BIG_FIVE_SCALE_LABELS = {
    1: "Sangat Tidak Setuju", 2: "Tidak Setuju", 3: "Netral",
    4: "Setuju", 5: "Sangat Setuju",
}


def _quiz_systems():
    for key, _title, _desc, chips in RY_MODES:
        if key == "mendalam":
            return list(chips)
    return list(QUESTION_BANKS.keys())


def _system_groups(bank):
    """Pecah bank soal 1 sistem jadi grup-grup BATCH_SIZE soal."""
    return [bank[i:i + BATCH_SIZE] for i in range(0, len(bank), BATCH_SIZE)]


def _ensure_state():
    if "md_phase" not in st.session_state:
        st.session_state.md_sys_idx = 0
        st.session_state.md_group_idx = 0
        st.session_state.md_answers = {}
        st.session_state.md_phase = "intro"
        st.session_state.md_final_ready = False
    # loading_results dipakai BARENG loading page 1 (key session_state yang
    # sama) biar revealpage.py bisa baca hasil kedua mode tanpa perlu tau
    # asalnya dari halaman loading yang mana.
    if "loading_results" not in st.session_state:
        st.session_state.loading_results = {}


def _reset_and_go_home():
    for k in ("md_sys_idx", "md_group_idx", "md_answers", "md_phase", "md_final_ready"):
        st.session_state.pop(k, None)
    st.session_state.dr_page = "home"
    st.rerun()


def _random_answer_for_system(system, q):
    """Jawaban acak (tapi VALID sesuai format yang diharapkan engine
    scoring-nya) buat 1 soal — dipakai cuma sama _bypass_semua_soal(),
    testing-only, LIHAT juga settings.TESTING_MODE."""
    if system in ("MBTI", "Enneagram"):
        return random.choice([True, False])
    if system == "Big Five":
        return random.choice([1, 2, 3, 4, 5])
    if system == "DISC":
        return random.choice(["A", "B", "C", "D"])
    if system == "Love Language":
        return random.choice(["A", "B"])
    return None


def _bypass_semua_soal(systems, sys_idx):
    """TESTING ONLY (settings.TESTING_MODE) — isi semua soal yang BELUM
    dijawab (sistem sekarang + semua sisanya) dengan jawaban acak, hitung
    skornya, terus langsung lompat ke layar final (floating window
    payment/bypass di _final_dialog()). Dipakai biar Stev nggak perlu
    ngerjain 157 soal manual tiap kali mau ngetes reveal page /
    payment flow. TIDAK menyentuh jawaban yang SUDAH diisi user secara
    manual sebelumnya (cuma nambahin yang kosong)."""
    for s in systems[sys_idx:]:
        bank = QUESTION_BANKS[s]
        answers = dict(st.session_state.md_answers.get(s, {}))
        for q in bank:
            if q["id"] not in answers:
                answers[q["id"]] = _random_answer_for_system(s, q)
        st.session_state.md_answers[s] = answers
        st.session_state.loading_results[s] = compute_quiz_raw_result(s, answers)
    st.session_state.md_sys_idx = len(systems)
    st.session_state.md_group_idx = 0
    st.session_state.md_final_ready = False
    st.rerun()


def _render_testing_bypass_button(systems, sys_idx):
    """Tombol kecil testing-only buat lewatin SISA soal kuesioner (sistem
    sekarang + berikutnya) langsung ke floating window payment. HARUS
    ditaruh DI LUAR st.form (st.button biasa nggak boleh di dalam form)."""
    if not TESTING_MODE:
        return
    col_spacer, col_btn = st.columns([3, 2])
    with col_btn:
        if st.button(
            "Lewati Semua Soal (Testing)", key="md_bypass_kuesioner",
            type="secondary", icon=":material/bolt:", use_container_width=True,
        ):
            _bypass_semua_soal(systems, sys_idx)


def _anti_leave_banner():
    st.markdown(
        '<div style="background:#fff3e0;border:1.5px solid #e4a56e;border-radius:12px;'
        'padding:10px 16px;margin-bottom:18px;text-align:center;font-size:12.5px;'
        'color:#8a5a2f;font-weight:600;">'
        '<span class="material-symbols-outlined" style="font-size:15px;vertical-align:-3px;">'
        'warning</span> Jangan tutup atau refresh halaman ini sampai kuesioner selesai — '
        'progress belum tersimpan ke server, kalau keluar sekarang kamu harus mengulang '
        'dari grup soal pertama.</div>',
        unsafe_allow_html=True,
    )


@st.dialog("Sebelum Mulai Kuesioner", dismissible=False)
def _intro_dialog(systems):
    total_q = sum(len(QUESTION_BANKS[s]) for s in systems)
    rincian = "".join(
        f'<li>{s}: {len(QUESTION_BANKS[s])} soal</li>' for s in systems
    )
    st.markdown(
        f'<div style="font-family:\'Fraunces\',serif;font-size:20px;font-weight:700;'
        f'color:#1c1a17;margin-bottom:10px;">Kuesioner Mode Mendalam</div>'
        f'<div style="font-size:13.5px;color:#3a352c;line-height:1.6;margin-bottom:10px;">'
        f'Total ada <b>{total_q} pertanyaan</b> dari {len(systems)} sistem, dikerjakan '
        f'satu sistem penuh dulu baru lanjut ke sistem berikutnya (soal ditampilin '
        f'10 sekaligus per layar):</div>'
        f'<ul style="font-size:13px;color:#3a352c;line-height:1.7;margin:0 0 12px 0;padding-left:20px;">'
        f'{rincian}</ul>'
        '<div style="font-size:13px;color:#6b6459;line-height:1.6;margin-bottom:10px;">'
        '⏱️ Perkiraan waktu pengerjaan: <b>sekitar 15-20 menit</b>, tergantung seberapa '
        'cepat kamu membaca &amp; menjawab. Tiap 1 sistem selesai, ada jeda buat '
        'istirahat sebentar sebelum lanjut ke sistem berikutnya.</div>'
        '<div style="background:#fff3e0;border:1px solid #e4a56e;border-radius:10px;'
        'padding:10px 12px;font-size:12.5px;color:#8a5a2f;font-weight:600;margin-bottom:10px;">'
        '⚠️ Usahakan jangan menutup atau refresh halaman selama proses berlangsung — '
        'belum ada fitur simpan progress, jadi kalau keluar di tengah jalan kamu harus '
        'mulai dari grup soal pertama lagi.</div>'
        '<div style="font-size:13px;color:#3a352c;line-height:1.6;">'
        '💬 Jawab dengan <b>hati yang jujur</b>, sesuai dirimu yang sebenarnya — bukan '
        'jawaban yang menurutmu "seharusnya benar". Hasil paling akurat kalau kamu '
        'jawab spontan sesuai perasaan asli, bukan hasil mikir lama.</div>',
        unsafe_allow_html=True,
    )
    st.write("")
    col_back, col_start = st.columns(2)
    with col_back:
        if st.button("Kembali", key="md_intro_back", use_container_width=True,
                      icon=":material/arrow_back:"):
            st.session_state.dr_page = "reveal"
            st.rerun()
    with col_start:
        if st.button("Mulai", key="md_intro_start", type="primary",
                      use_container_width=True, icon=":material/play_arrow:"):
            st.session_state.md_phase = "batch"
            st.rerun()


# --- Renderer per tipe soal ------------------------------------------------
# Dipanggil di DALAM st.form(), jadi WAJIB pakai widget non-tombol (radio),
# karena st.button biasa gak boleh dipakai di dalam st.form. Tiap fungsi
# nge-render satu soal + return nilai jawabannya (format persis yang
# diharapkan engine/*_scoring.py — lihat docstring tiap engine), atau None
# kalau belum dipilih.

def _render_yesno_question(q, num):
    st.markdown(
        f'<div style="font-family:\'Fraunces\',serif;font-size:16.5px;font-weight:700;'
        f'color:#1c1a17;line-height:1.5;margin-bottom:6px;">{num}. {q["text"]}</div>',
        unsafe_allow_html=True,
    )
    val = st.radio(
        f"jawaban_{q['id']}", options=["Setuju", "Tidak Setuju"], index=None,
        key=f"md_w_{q['id']}", horizontal=True, label_visibility="collapsed",
    )
    if val == "Setuju":
        return True
    if val == "Tidak Setuju":
        return False
    return None


def _render_scale_question(q, num):
    st.markdown(
        f'<div style="font-family:\'Fraunces\',serif;font-size:16.5px;font-weight:700;'
        f'color:#1c1a17;line-height:1.5;margin-bottom:2px;">{num}. {q["text"]}</div>'
        '<div style="font-size:11px;color:#8a5a2f;margin-bottom:6px;">'
        '1 = Sangat Tidak Setuju &nbsp;·&nbsp; 5 = Sangat Setuju</div>',
        unsafe_allow_html=True,
    )
    return st.radio(
        f"skor_{q['id']}", options=[1, 2, 3, 4, 5],
        format_func=lambda i: f"{i} — {BIG_FIVE_SCALE_LABELS[i]}",
        index=None, key=f"md_w_{q['id']}", horizontal=True,
        label_visibility="collapsed",
    )


def _render_disc_question(q, num):
    st.markdown(
        f'<div style="font-family:\'Fraunces\',serif;font-size:16.5px;font-weight:700;'
        f'color:#1c1a17;line-height:1.5;margin-bottom:6px;">{num}. Pilih SATU kata yang '
        'PALING menggambarkan dirimu sehari-hari:</div>',
        unsafe_allow_html=True,
    )
    return st.radio(
        f"pilihan_{q['id']}", options=["A", "B", "C", "D"],
        format_func=lambda letter: q["options"][letter],
        index=None, key=f"md_w_{q['id']}", horizontal=True,
        label_visibility="collapsed",
    )


def _render_love_language_question(q, num):
    st.markdown(
        f'<div style="font-family:\'Fraunces\',serif;font-size:16.5px;font-weight:700;'
        f'color:#1c1a17;line-height:1.5;margin-bottom:8px;">{num}. Baca kedua pernyataan '
        'berikut, lalu pilih yang paling menggambarkan dirimu:</div>',
        unsafe_allow_html=True,
    )
    for letter in ("A", "B"):
        st.markdown(
            '<div style="border:1.5px solid #ecddc9;border-radius:12px;'
            'padding:10px 14px;background:#fdfaf5;margin-bottom:6px;font-size:13px;'
            f'color:#1c1a17;line-height:1.5;"><b>{letter}.</b> {q[letter]["text"]}</div>',
            unsafe_allow_html=True,
        )
    return st.radio(
        f"pilihan_{q['id']}", options=["A", "B"],
        format_func=lambda letter: f"Pilih Pernyataan {letter}",
        index=None, key=f"md_w_{q['id']}", horizontal=True,
        label_visibility="collapsed",
    )


QUESTION_RENDERERS = {
    "MBTI": _render_yesno_question,
    "Big Five": _render_scale_question,
    "Enneagram": _render_yesno_question,
    "DISC": _render_disc_question,
    "Love Language": _render_love_language_question,
}


def _header_html(systems, sys_idx, current_system, start_num, end_num, total_q,
                  group_idx, total_groups):
    return (
        '<div style="text-align:center;">'
        '<div style="font-family:\'Fraunces\',serif;font-size:26px;font-weight:700;'
        'color:#1c1a17;margin-bottom:6px;">Kuesioner Mode Mendalam</div>'
        f'<div style="font-size:13px;color:#6b6459;">Sistem {sys_idx + 1} dari '
        f'{len(systems)}: <b>{current_system}</b> &mdash; Soal {start_num}-{end_num} dari '
        f'{total_q} &nbsp;(grup {group_idx + 1}/{total_groups})</div></div>'
        '<div style="height:14px;"></div>'
        f'{_dots_html(systems, sys_idx, waiting=False)}'
        '<div style="height:20px;"></div>'
    )


@st.dialog("Belum Lengkap", dismissible=True)
def _incomplete_answers_dialog(missing_count, group_total):
    """Revisi (28 Sep 2026 sore, instruksi Stev poin 1): SEBELUMNYA
    peringatan "masih ada soal belum dijawab" pakai st.error() (kotak
    oranye nempel di halaman) -- sekarang dipindah jadi floating window
    (@st.dialog), SAMA gaya desainnya kayak floating window lain di
    kuesioner ini (dismissible=True karena ini cuma notice, bukan
    keputusan wajib kayak _jam_fallback_dialog/_intro_dialog)."""
    st.markdown(
        '<div style="text-align:center;padding:4px 0 2px 0;">'
        '<div style="width:52px;height:52px;border-radius:50%;background:#fff3e0;'
        'border:1.5px solid #e4a56e;display:flex;align-items:center;justify-content:center;'
        'margin:0 auto 14px auto;">'
        '<span class="material-symbols-outlined" style="font-size:26px;color:#b8562f;">'
        'error</span></div>'
        '<div style="font-family:\'Fraunces\',serif;font-size:18px;font-weight:800;'
        'color:#1c1a17;margin-bottom:8px;">Masih Ada yang Kosong</div>'
        f'<div style="font-size:13.5px;color:#6b6459;line-height:1.7;max-width:320px;'
        f'margin:0 auto;">Masih ada <b style="color:#1c1a17;">{missing_count} dari '
        f'{group_total} soal</b> di grup ini yang belum kamu jawab — lengkapi dulu '
        'semuanya sebelum lanjut ke soal berikutnya.</div>'
        '</div>',
        unsafe_allow_html=True,
    )
    st.write("")
    st.button(
        "Kembali ke Kuesioner", key="md_missing_ok", type="primary",
        use_container_width=True, icon=":material/edit:",
    )


def _render_batch_phase(systems, sys_idx, current_system, bank):
    groups = _system_groups(bank)
    group_idx = st.session_state.md_group_idx
    group = groups[group_idx]
    total_groups = len(groups)
    total_q = len(bank)
    start_num = group_idx * BATCH_SIZE + 1
    end_num = start_num + len(group) - 1
    is_last_group = group_idx + 1 == total_groups

    st.markdown(
        _header_html(systems, sys_idx, current_system, start_num, end_num, total_q,
                      group_idx, total_groups),
        unsafe_allow_html=True,
    )
    _anti_leave_banner()
    _render_testing_bypass_button(systems, sys_idx)

    # Revisi (28 Sep 2026 sore, instruksi Stev poin 3): grup soal TERAKHIR
    # tiap sistem (bukan cuma sistem terakhir keseluruhan) labelnya "Submit"
    # (bukan "Lanjut" lagi) -- lebih jelas nunjukkin ini penutup 1 sistem
    # penuh, sama berlaku buat MBTI, Big Five, Enneagram, DISC, Love
    # Language (semua lewat fungsi yang sama ini).
    btn_label = "Submit" if is_last_group else "Lanjut"
    btn_icon = ":material/check_circle:" if is_last_group else ":material/arrow_forward:"

    renderer = QUESTION_RENDERERS[current_system]
    with st.form(key=f"md_form_{current_system}_{group_idx}"):
        collected = {}
        for local_i, q in enumerate(group):
            collected[q["id"]] = renderer(q, start_num + local_i)
            st.write("")
        # Revisi (28 Sep 2026 sore, instruksi Stev poin 2): tombol
        # SEBELUMNYA use_container_width=True (selebar form, kelewat
        # lebar) -- dipersempit lewat kolom tengah, sama pola kayak tombol
        # "Buka Semua Amplop" di revealpage.py. Warna tetap ikut tema
        # (type="primary", udah kena CSS brand global di app.py).
        # Revisi (28 Sep 2026 sore, instruksi Stev poin 2 ronde 2): warna
        # solid oren tombol ini kerasa nabrak sama tema halaman kuesioner
        # yang lebih ke cream (warning banner, kotak radio, dst semua
        # cream + border tipis, bukan solid oren) -- diganti jadi cream
        # senada, TAPI dikasih key khusus (md_submit_btn_row) biar CSS-nya
        # cuma nempel di tombol INI doang, gak ikut ubah tombol primary
        # lain di halaman/halaman lain (mis. "Mulai Proses Reveal").
        with st.container(key="md_submit_btn_row"):
            btn_l, btn_mid, btn_r = st.columns([1, 1.1, 1])
            with btn_mid:
                submitted = st.form_submit_button(
                    btn_label, type="primary", use_container_width=True, icon=btn_icon,
                )

    if not submitted:
        return

    missing = [qid for qid, val in collected.items() if val is None]
    if missing:
        _incomplete_answers_dialog(len(missing), len(group))
        return

    st.session_state.md_answers.setdefault(current_system, {}).update(collected)

    if group_idx + 1 < total_groups:
        st.session_state.md_group_idx += 1
        st.rerun()
        return

    # Grup terakhir sistem ini kelar semua -- hitung skor SEKARANG.
    st.session_state.loading_results[current_system] = compute_quiz_raw_result(
        current_system, st.session_state.md_answers[current_system],
    )
    st.session_state.md_group_idx = 0
    if sys_idx + 1 < len(systems):
        st.session_state.md_phase = "system_confirm"
    else:
        # Sistem TERAKHIR kelar -- majuin md_sys_idx ngelewatin batas biar
        # render() nangkep kondisi "sys_idx >= len(systems)" dan langsung ke
        # layar final (payment), TANPA lewat dialog "siap lanjut?" (karena
        # emang gak ada sistem berikutnya).
        st.session_state.md_sys_idx += 1
    st.rerun()


@st.dialog("Satu Sistem Selesai!", dismissible=False)
def _system_confirm_dialog(current_system, next_system):
    # Revisi (28 Sep 2026 sore, instruksi Stev poin 4): desain & alignment
    # dipercantik -- SEBELUMNYA cuma paragraf rata-kiri polos, sekarang
    # ikon lingkaran + judul serif + deskripsi center-align, senada sama
    # gaya floating window lain yang udah "elegan" (mis. _upgrade_dialog
    # di revealpage.py).
    st.markdown(
        '<div style="text-align:center;padding:4px 0 6px 0;">'
        '<div style="width:56px;height:56px;border-radius:50%;background:#fdf3e7;'
        'border:1.5px solid #ecddc9;display:flex;align-items:center;justify-content:center;'
        'margin:0 auto 14px auto;">'
        '<span class="material-symbols-outlined" style="font-size:28px;color:#b8562f;">'
        'task_alt</span></div>'
        f'<div style="font-family:\'Fraunces\',serif;font-size:19px;font-weight:800;'
        f'color:#1c1a17;margin-bottom:8px;">Kuesioner {current_system} Selesai!</div>'
        '<div style="font-size:13.5px;color:#6b6459;line-height:1.7;max-width:340px;'
        'margin:0 auto;">Semua jawabanmu sudah diproses. Selanjutnya kamu lanjut ke '
        f'kuesioner <b style="color:#1c1a17;">{next_system}</b>. Siap lanjut sekarang?'
        '</div></div>',
        unsafe_allow_html=True,
    )
    st.write("")
    col_batal, col_lanjut = st.columns(2)
    with col_batal:
        if st.button("Batal", key="md_confirm_batal", use_container_width=True,
                      icon=":material/close:"):
            _reset_and_go_home()
    with col_lanjut:
        if st.button("Lanjut", key="md_confirm_lanjut", type="primary",
                      use_container_width=True, icon=":material/arrow_forward:"):
            st.session_state.md_sys_idx += 1
            st.session_state.md_group_idx = 0
            st.session_state.md_phase = "batch"
            st.rerun()


def _render_system_confirm_phase(systems, sys_idx, current_system):
    next_system = systems[sys_idx + 1]
    st.markdown(
        '<div style="text-align:center;">'
        '<div style="font-family:\'Fraunces\',serif;font-size:26px;font-weight:700;'
        'color:#1c1a17;margin-bottom:6px;">Kuesioner Mode Mendalam</div>'
        f'<div style="font-size:13.5px;color:#6b6459;">✓ {current_system} selesai</div>'
        '</div>'
        '<div style="height:14px;"></div>'
        f'{_dots_html(systems, sys_idx + 1, waiting=True)}',
        unsafe_allow_html=True,
    )
    _system_confirm_dialog(current_system, next_system)


def _render_final_screen(systems):
    st.markdown(
        '<div style="text-align:center;">'
        '<div style="font-family:\'Fraunces\',serif;font-size:28px;font-weight:700;'
        'color:#1c1a17;margin-bottom:8px;">Semua Kuesioner Selesai!</div>'
        '<div style="font-size:14px;color:#6b6459;">Sedang menyusun hasil...</div>'
        '</div>'
        '<div style="height:16px;"></div>'
        f'{_dots_html(systems, len(systems), waiting=False)}',
        unsafe_allow_html=True,
    )
    if not st.session_state.md_final_ready:
        time.sleep(FINAL_PAUSE_SECONDS)
        st.session_state.md_final_ready = True
        st.rerun()
    # Floating window payment -- DIIMPOR LANGSUNG dari views/loadingpage.py,
    # SAMA PERSIS (termasuk bypass testing), bukan dibikin ulang, sesuai
    # instruksi Stev. Hasil (tipe/skor) TIDAK ditampilkan di sini — baru
    # kelihatan di reveal page setelah "bayar" (atau bypass).
    _final_dialog()


def render():
    _ensure_state()
    _inject_style()

    systems = _quiz_systems()
    phase = st.session_state.md_phase

    if phase == "intro":
        st.markdown(
            '<div style="text-align:center;">'
            '<div style="font-family:\'Fraunces\',serif;font-size:28px;font-weight:700;'
            'color:#1c1a17;margin-bottom:8px;">Menyiapkan Kuesioner...</div>'
            '</div>'
            '<div style="height:16px;"></div>'
            f'{_dots_html(systems, 0, waiting=True)}',
            unsafe_allow_html=True,
        )
        _intro_dialog(systems)
        return

    sys_idx = st.session_state.md_sys_idx
    if sys_idx >= len(systems):
        _render_final_screen(systems)
        return

    current_system = systems[sys_idx]
    if phase == "batch":
        _render_batch_phase(systems, sys_idx, current_system, QUESTION_BANKS[current_system])
    elif phase == "system_confirm":
        _render_system_confirm_phase(systems, sys_idx, current_system)
    else:
        # phase nggak dikenal (harusnya nggak pernah kejadian) -- reset aman
        st.session_state.md_phase = "batch"
        st.rerun()
