"""
Halaman Loading — proses reveal per-titik.

Alur:
- Titik-titik yang diproses ditentukan dari mode yang dipilih di halaman
  Reveal Yourself (RY_MODES di reveal_yourself.py).
- Cuma SATU titik yang ditampilkan aktif dalam satu waktu (kartu simbol +
  teks blur, dengan animasi reveal dari atas ke bawah ~5 detik). Begitu
  titik itu selesai, tampilannya DIGANTI (bukan ditumpuk) oleh titik
  berikutnya — animasi reveal-nya ngulang dari awal tiap titik baru.
- Hasil tiap titik yang udah selesai disimpan di session_state
  (loading_results), buat dimunculin nanti semua sekaligus di halaman
  hasil akhir (revealpage.py) — bukan ditampilin numpuk di halaman ini.
- Kalau titik butuh data yang belum ada (tanggal/jam/kota lahir), muncul
  floating window (st.dialog, tidak bisa ditutup manual) minta data itu
  SEKALI — dipakai ulang buat titik lain yang butuh data yang sama,
  nggak ditanya berkali-kali.
- Proses TIDAK BISA di-skip. Refresh browser lanjut dari titik terakhir
  karena semuanya disimpan di st.session_state (bukan reset ke titik 1).

KETERBATASAN per revisi ini (sengaja, biar jelas bukan tersembunyi):
- Sistem yang butuh kuesioner sendiri (MBTI, Big Five, Enneagram, DISC,
  Love Language) belum punya kuesionernya — per instruksi Stev,
  "itu nanti kita bikin" belakangan. Titik-titik ini untuk sementara
  DILEWATI langsung tanpa nanya apa-apa (bukan beneran dihitung).
- 5 sistem berbasis tanggal lahir (Zodiak, Shio, Weton, Numerologi, Matrix
  Destiny) SUDAH dihitung beneran lewat engine/*.py + kamus konten di
  content/interpretations/ (lihat content/result_builder.py). Sistem
  lain di luar itu (BaZi, Zi Wei, Human Design, Golongan Darah, Tarot,
  dst) masih placeholder karena enginenya sendiri belum dibangun.
"""

import calendar
import time
from datetime import date

import streamlit as st
import streamlit.components.v1 as components

from content.result_builder import compute_raw_result
from utils.card_images import card_image_for_system
from utils.date_format import BULAN_NAMES_ID, format_tanggal_ddmmyyyy
from views.reveal_yourself import RY_MODES

# ── Kebutuhan data per sistem ────────────────────────────────
NEEDS_TANGGAL = {
    "Zodiak", "Shio", "Weton", "Numerologi", "Matrix Destiny",
    "BaZi", "Zi Wei", "Human Design",
}
NEEDS_JAM = {"BaZi", "Zi Wei", "Human Design"}
NEEDS_KOTA = {"BaZi", "Human Design"}
NEEDS_GOLDA = {"Golongan Darah"}
# belum ada kuesionernya — dilewati dulu (lihat catatan keterbatasan di atas)
NEEDS_KUESIONER_BELUM_ADA = {"MBTI", "Big Five", "Enneagram", "DISC", "Love Language"}

FIELD_LABEL = {
    "tanggal_lahir": "Masukkan Tanggal Lahir",
    "jam_lahir": "Masukkan Jam Lahir",
    "kota_lahir": "Masukkan Kota Lahir",
    "golongan_darah": "Masukkan Golongan Darah",
}

ANIM_SECONDS = 5


def _mode_points(mode_key):
    for key, _title, _desc, chips in RY_MODES:
        if key == mode_key:
            return list(chips)
    return []


def _ensure_state():
    if "loading_points" not in st.session_state:
        mode_key = st.session_state.get("ry_focus_mode")
        st.session_state.loading_points = _mode_points(mode_key)
        st.session_state.loading_idx = 0
        # need_check -> (asking | animating) -> need_check (titik berikutnya)
        st.session_state.loading_phase = "need_check"
        st.session_state.loading_results = {}
        st.session_state.loading_data = {}  # tanggal_lahir, jam_lahir, kota_lahir, golongan_darah


def _missing_field_for(system):
    data = st.session_state.loading_data
    # Sistem yang kuesionernya belum ada (MBTI dkk) tetap butuh data DASAR
    # (tanggal lahir) biar titiknya nggak dilewat diam-diam tanpa nanya
    # apa-apa — biar urutannya jelas: titik pertama di mode manapun selalu
    # nanya tanggal lahir dulu, titik berikutnya yang butuh data sama
    # otomatis nggak nanya lagi.
    needs_tanggal = system in NEEDS_TANGGAL or system in NEEDS_KUESIONER_BELUM_ADA
    if needs_tanggal and "tanggal_lahir" not in data:
        return "tanggal_lahir"
    if system in NEEDS_JAM and "jam_lahir" not in data:
        return "jam_lahir"
    if system in NEEDS_KOTA and "kota_lahir" not in data:
        return "kota_lahir"
    if system in NEEDS_GOLDA and "golongan_darah" not in data:
        return "golongan_darah"
    return None


@st.dialog("Reveal Selesai", dismissible=False)
def _final_dialog():
    """
    Floating window paywall di akhir proses loading.

    BELUM ada integrasi payment gateway asli (Midtrans/Xendit dkk) — ini
    SENGAJA cuma 1 tombol "Bypass Payment" buat kebutuhan testing (lihat
    settings.py, TESTING_MODE). Begitu payment gateway beneran siap,
    tombol ini diganti jadi UI pembayaran asli, TIDAK ada auto-lanjut JS
    kayak dialog sebelumnya, karena ini gerbang (gate) — harus benar-benar
    diklik/dibayar, bukan dilewati otomatis.
    """
    st.markdown(
        '<div style="text-align:center;padding:6px 0 4px 0;">'
        '<div style="font-size:38px;margin-bottom:10px;">&#10024;</div>'
        '<div style="font-family:\'Fraunces\',serif;font-size:19px;font-weight:800;'
        'color:#1c1a17;letter-spacing:0.01em;line-height:1.4;">'
        'SEMUA DATA DIRIMU<br>SUDAH DIREVEAL</div>'
        '<div style="font-size:13px;color:#6b6459;margin-top:8px;">'
        'Bayar sekali buat buka laporan lengkapnya.</div>'
        '</div>',
        unsafe_allow_html=True,
    )
    st.write("")
    st.button(
        "Bayar Sekarang", key="btn_pay_real", type="secondary",
        icon=":material/lock:", use_container_width=True, disabled=True,
    )
    st.markdown(
        '<div style="text-align:center;font-size:11px;color:#c9c2b4;margin:2px 0 10px 0;">'
        'Payment gateway asli belum terpasang — pakai tombol testing di bawah dulu.</div>',
        unsafe_allow_html=True,
    )
    if st.button(
        "Bypass Payment", key="btn_bypass_payment", type="primary",
        icon=":material/bolt:", use_container_width=True,
    ):
        st.session_state.dr_page = "result"
        st.rerun()


@st.dialog("Lengkapi Data", dismissible=False)
def _ask_field_dialog(field):
    st.markdown(
        f'<div style="font-family:\'Fraunces\',serif;font-size:20px;font-weight:700;'
        f'color:#1c1a17;margin-bottom:14px;">{FIELD_LABEL[field]}</div>',
        unsafe_allow_html=True,
    )
    if field == "tanggal_lahir":
        # Dropdown 3 bagian (Tanggal / Bulan / Tahun), BUKAN st.date_input
        # segmen ketik manual lagi — soalnya lebih gampang dipakai (nggak
        # perlu ngetik, bulan otomatis dibatasi cuma 1-12 jadi nggak bisa
        # salah ketik angka di luar itu) dan urutannya persis dd/mm/yyyy
        # (konvensi umum Indonesia).
        #
        # Opsi tanggal (hari) DIHITUNG ULANG tiap kali bulan/tahun berubah
        # (lewat calendar.monthrange), jadi user nggak akan bisa milih
        # tanggal yang nggak valid (mis. 30 Februari). Key selectbox hari
        # sengaja dibuat DINAMIS per kombinasi bulan+tahun (bukan key
        # tetap) supaya Streamlit nggak error "default value is not part
        # of options" kalau user ganti ke bulan yang jumlah harinya lebih
        # sedikit dari tanggal yang lagi kepilih sebelumnya.
        st.markdown(
            '<div style="display:flex;align-items:center;gap:6px;font-size:12.5px;'
            'font-weight:700;color:#8a5a2f;margin:-4px 0 10px 0;">'
            '<span class="material-symbols-outlined" style="font-size:16px;">calendar_month</span>'
            '<span>Urutan: Tanggal / Bulan / Tahun — contoh: 05/12/1992</span></div>',
            unsafe_allow_html=True,
        )
        this_year = date.today().year
        tahun_options = list(range(this_year, 1929, -1))  # descending, this_year..1930

        col_d, col_m, col_y = st.columns(3)
        with col_m:
            bulan = st.selectbox(
                "Bulan", options=list(range(1, 13)),
                format_func=lambda m: BULAN_NAMES_ID[m - 1],
                key="dlg_tgl_bulan", label_visibility="collapsed",
            )
        with col_y:
            default_tahun_idx = tahun_options.index(2000) if 2000 in tahun_options else 0
            tahun = st.selectbox(
                "Tahun", options=tahun_options, index=default_tahun_idx,
                key="dlg_tgl_tahun", label_visibility="collapsed",
            )
        max_hari = calendar.monthrange(tahun, bulan)[1]
        hari_options = list(range(1, max_hari + 1))
        hari_diinginkan = st.session_state.get("dlg_tgl_hari_terakhir", 1)
        hari_default = min(hari_diinginkan, max_hari)
        with col_d:
            hari = st.selectbox(
                "Tanggal", options=hari_options,
                index=hari_options.index(hari_default),
                key=f"dlg_tgl_hari_{bulan}_{tahun}", label_visibility="collapsed",
            )
        st.session_state.dlg_tgl_hari_terakhir = hari
        value = date(tahun, bulan, hari)
    elif field == "jam_lahir":
        value = st.time_input("Jam Lahir", key="dlg_jam_lahir", label_visibility="collapsed")
    elif field == "kota_lahir":
        value = st.text_input(
            "Kota Lahir", placeholder="Contoh: Jakarta",
            key="dlg_kota_lahir", label_visibility="collapsed",
        )
    else:  # golongan_darah
        value = st.selectbox(
            "Golongan Darah", ["A", "B", "AB", "O", "Tidak tahu"],
            key="dlg_golongan_darah", label_visibility="collapsed",
        )

    if st.button("Lanjutkan", key="dlg_lanjut", type="primary",
                  icon=":material/arrow_forward:", use_container_width=True):
        st.session_state.loading_data[field] = value
        st.session_state.loading_phase = "animating"
        st.rerun()


def _render_input_summary():
    """
    Ringkasan data yang udah diisi user (tanggal lahir dkk), ditampilkan di
    bawah judul "Sedang Membaca Dirimu..." biar user bisa cek ulang
    input-nya nggak salah ketik/pilih sebelum nunggu proses selesai.
    """
    data = st.session_state.get("loading_data", {})
    tanggal_str = format_tanggal_ddmmyyyy(data.get("tanggal_lahir"))
    if not tanggal_str:
        return
    st.markdown(
        '<div style="text-align:center;margin-top:8px;">'
        f'<span class="ry-load-input-summary"><span class="material-symbols-outlined" '
        'style="font-size:15px;vertical-align:-2px;">calendar_month</span> '
        f'Tanggal Kamu: <b>{tanggal_str}</b></span>'
        '</div>',
        unsafe_allow_html=True,
    )


def _inject_style():
    st.markdown(
        """
        <style>
        .ry-load-input-summary { display: inline-flex; align-items: center; gap: 8px;
            padding: 6px 16px; border-radius: 100px; background: #f9f4ec; border: 1px solid #ecddc9;
            font-size: 12.5px; color: #6b6459 !important; }
        .ry-load-input-summary b { color: #1c1a17 !important; font-weight: 800; }
        .ry-load-dot-row { display: flex; flex-wrap: wrap; align-items: flex-start;
            justify-content: center; gap: 10px; row-gap: 22px; max-width: 900px;
            margin: 0 auto; }
        .ry-load-dot-unit { display: flex; flex-direction: column; align-items: center;
            flex-shrink: 0; width: 74px; }
        .ry-load-dot { width: 46px; height: 46px; border-radius: 50%; display: flex;
            align-items: center; justify-content: center; font-weight: 800; font-size: 14px;
            flex-shrink: 0; }
        .ry-load-dot-done { background: #b8562f; color: #ffffff !important; }
        .ry-load-dot-upcoming { background: #f9f4ec; border: 2px solid #ecddc9; color: #c9c2b4 !important; }
        .ry-load-dot-active-ring { width: 58px; height: 58px; border-radius: 50%;
            border: 3px dashed #e4a56e; display: flex; align-items: center; justify-content: center;
            animation: ry-spin 1.1s linear infinite; }
        .ry-load-dot-active { width: 46px; height: 46px; border-radius: 50%;
            background: #fff8ef; border: 2px solid #b8562f; color: #b8562f !important;
            display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 14px; }
        .ry-load-dot-waiting { width: 46px; height: 46px; border-radius: 50%;
            background: #fff8ef; border: 2px solid #e4a56e; color: #b8562f !important;
            display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 14px; }
        .ry-load-label { font-size: 10.5px; font-weight: 700; margin-top: 7px; text-align: center; }
        @keyframes ry-spin { to { transform: rotate(360deg); } }

        /* Rantai/garis penghubung antar dot, senada sama stepper di halaman
           Reveal Yourself — brown kalau titik kiri udah selesai, dim kalau
           belum. margin-top disamain ke tengah lingkaran dot (23px = setengah
           tinggi dot 46px). */
        .ry-load-chain { width: 26px; height: 3px; border-radius: 3px; margin-top: 23px; flex-shrink: 0; }
        .ry-load-chain-upcoming { background: #ecddc9; }
        .ry-load-chain-done { background: #b8562f; }

        .ry-load-card-wrap { display: flex; flex-direction: column; align-items: center; gap: 20px;
            margin-top: 32px; }
        .ry-load-card {
            width: 240px; height: 340px; border-radius: 18px; padding: 6px;
            background: linear-gradient(155deg, #f3d488, #c9a227 45%, #8a6a12 55%, #f3d488);
            box-shadow: 0 20px 40px -18px rgba(139,90,47,0.45);
            animation: ry-reveal var(--ry-anim-s) ease-out forwards;
        }
        .ry-load-card-inner { width: 100%; height: 100%; border-radius: 14px; padding: 3px;
            background: linear-gradient(155deg, #fdf0c8, #c9a227); }
        .ry-load-card-art { width: 100%; height: 100%; border-radius: 12px; overflow: hidden;
            background: linear-gradient(150deg, #e9c9a6, #c9683a 55%, #8a5a2f); filter: blur(3.5px); opacity: 0.9; }
        .ry-load-text-box { width: 100%; max-width: 560px; background: #fdfaf5;
            border: 2px solid #f0e6d5; border-radius: 20px; padding: 26px 30px;
            display: flex; flex-direction: column; align-items: center; gap: 10px;
            animation: ry-reveal var(--ry-anim-s) ease-out forwards;
        }
        /* Tiap baris tulisan punya filter:blur(...) sendiri lewat inline
           style (lihat _ANIM_LINES di Python) biar blur-nya gradasi makin
           tebal ke bawah — bukan rata semua kayak sebelumnya. */
        .ry-load-line { border-radius: 6px; background: #e8e0d2; }
        @keyframes ry-reveal {
            from { clip-path: inset(0 0 100% 0); }
            to { clip-path: inset(0 0 0% 0); }
        }
        .ry-load-waiting-box { width: 240px; height: 340px; border-radius: 18px;
            border: 2px dashed #ecddc9; background: #fdfaf5; display: flex;
            align-items: center; justify-content: center; color: #c9c2b4; }

        /* Floating window (st.dialog) — dipaksa terang + font kontras jelas,
           soalnya di dark mode wrapper dialognya kebawa background gelap
           default browser/OS (bug CSS dark-mode yang sama kayak sebelumnya
           di halaman lain). */
        [data-testid="stDialog"],
        [data-testid="stDialog"] > div {
            background-color: #fffaf2 !important;
        }
        [data-testid="stDialog"] * {
            color: #1c1a17 !important;
        }
        [data-testid="stDialog"] input,
        [data-testid="stDialog"] [data-baseweb="select"] > div,
        [data-testid="stDialog"] [class*="react-aria-TextField"] > div,
        [data-testid="stDialog"] [class*="react-aria-ComboBox"] > div,
        [data-testid="stDialog"] [data-testid="stDateInputField"],
        [data-testid="stDialog"] [data-testid="stTimeInputTimeDisplay"] {
            background-color: #ffffff !important;
            border-color: #e4ddd0 !important;
        }
        [data-testid="stDialog"] button[kind="primary"] * { color: #ffffff !important; }
        </style>
        """,
        unsafe_allow_html=True,
    )


def _render_dots(points, idx, waiting=False):
    total = len(points)
    dots_html = ['<div class="ry-load-dot-row">']
    for i, system in enumerate(points):
        if i < idx:
            dot = f'<div class="ry-load-dot ry-load-dot-done">✓</div>'
            label_color = "#1c1a17"
        elif i == idx:
            if waiting:
                dot = f'<div class="ry-load-dot ry-load-dot-waiting">{i + 1}</div>'
                label_color = "#b8562f"
            else:
                dot = (
                    '<div class="ry-load-dot-active-ring">'
                    f'<div class="ry-load-dot-active">{i + 1}</div></div>'
                )
                label_color = "#b8562f"
        else:
            dot = f'<div class="ry-load-dot ry-load-dot-upcoming">{i + 1}</div>'
            label_color = "#b0aa9d"
        dots_html.append(
            f'<div class="ry-load-dot-unit">{dot}'
            f'<div class="ry-load-label" style="color:{label_color} !important;">{system}</div></div>'
        )
        if i < total - 1:
            # Rantai antar titik jadi coklat kalau titik di kirinya udah kelar.
            chain_cls = "ry-load-chain-done" if i < idx else "ry-load-chain-upcoming"
            dots_html.append(f'<div class="ry-load-chain {chain_cls}"></div>')
    dots_html.append("</div>")
    st.markdown("".join(dots_html), unsafe_allow_html=True)


def render():
    _ensure_state()
    _inject_style()

    points = st.session_state.loading_points
    idx = st.session_state.loading_idx
    total = len(points)

    if not points:
        st.warning("Mode belum dipilih. Kembali ke halaman Reveal Yourself dulu ya.")
        if st.button("Kembali ke Reveal Yourself", icon=":material/arrow_back:"):
            st.session_state.dr_page = "reveal"
            st.rerun()
        return

    if idx >= total:
        st.markdown(
            '<div style="text-align:center;">'
            '<div style="font-family:\'Fraunces\',serif;font-size:30px;font-weight:700;color:#1c1a17;margin-bottom:8px;">'
            'Sedang Membaca Dirimu...</div>'
            '<div style="font-size:14.5px;color:#6b6459;">Semua titik selesai diproses.</div>'
            '</div>',
            unsafe_allow_html=True,
        )
        _render_input_summary()
        st.write("")
        _render_dots(points, idx, waiting=False)
        _final_dialog()
        return

    current = points[idx]

    st.markdown(
        '<div style="text-align:center;">'
        '<div style="font-family:\'Fraunces\',serif;font-size:30px;font-weight:700;color:#1c1a17;margin-bottom:8px;">'
        'Sedang Membaca Dirimu...</div>'
        f'<div style="font-size:14.5px;color:#6b6459;">Titik {idx + 1} dari {total} sedang diproses '
        '— jangan tutup halaman ini ya.</div>'
        '</div>',
        unsafe_allow_html=True,
    )
    _render_input_summary()
    st.write("")

    # ── STATE MACHINE per titik ──
    if st.session_state.loading_phase == "need_check":
        # Urutan dicek data DULU, baru status kuesioner — biar titik apapun
        # yang kena giliran duluan (termasuk MBTI dkk yang kuesionernya
        # belum ada) tetap nanya data dasar (tanggal lahir) sekali di
        # floating window. Titik berikutnya yang butuh data sama otomatis
        # skip nanya lagi karena udah kesimpen di loading_data.
        missing = _missing_field_for(current)
        if missing:
            st.session_state.loading_phase = "asking"
        else:
            if current in NEEDS_KUESIONER_BELUM_ADA:
                # kuesionernya belum dibuat — dilewati, hasil placeholder
                st.session_state.loading_results[current] = {"placeholder": True, "skipped": True}
            st.session_state.loading_phase = "animating"
        st.rerun()

    elif st.session_state.loading_phase == "asking":
        _render_dots(points, idx, waiting=True)
        st.markdown('<div class="ry-load-card-wrap">', unsafe_allow_html=True)
        st.markdown('<div class="ry-load-waiting-box">Menunggu data...</div>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        missing = _missing_field_for(current)
        _ask_field_dialog(missing)

    elif st.session_state.loading_phase == "animating":
        _render_dots(points, idx, waiting=False)
        # Hitung hasil ASLI-nya DULUAN (sebelum kartu teaser dirender),
        # bukan nunggu sampai animasi selesai — biar gambar kartu yang
        # ditampilin (walau masih blur/teaser) sudah PASTI sesuai hasil
        # perhitungan yang bakal ditampilkan nanti di halaman hasil, bukan
        # kartu contoh generik yang beda-beda tiap sistem (bug yang sudah
        # diperbaiki, lihat utils/card_images.py).
        if current not in st.session_state.loading_results:
            st.session_state.loading_results[current] = compute_raw_result(
                current, st.session_state.loading_data,
            )
        current_raw_result = st.session_state.loading_results[current]
        image_uri = card_image_for_system(current, current_raw_result)
        card_art_inner = (
            f'<img src="{image_uri}" alt="Kartu {current}" '
            'style="width:100%;height:100%;object-fit:cover;">'
            if image_uri else ""
        )
        st.markdown(
            f'<div class="ry-load-card-wrap" style="--ry-anim-s:{ANIM_SECONDS}s;">'
            '<div style="font-size:11px;font-weight:800;letter-spacing:0.08em;'
            f'text-transform:uppercase;color:#b8562f;">✓ {current} — sedang diproses</div>'
            '<div class="ry-load-card" style="--ry-anim-s:' + str(ANIM_SECONDS) + 's;">'
            f'<div class="ry-load-card-inner"><div class="ry-load-card-art">{card_art_inner}</div></div>'
            '</div>'
            # Blur tiap baris SENGAJA gradasi (bukan rata) — makin ke bawah
            # makin tebal, biar menjelang ~85% tinggi kotak udah nggak
            # kebaca sama sekali (efek "teaser", cuma judul yang agak jelas).
            '<div class="ry-load-text-box" style="--ry-anim-s:' + str(ANIM_SECONDS) + 's;">'
            '<div class="ry-load-line" style="width:200px;height:17px;margin-bottom:4px;filter:blur(0.5px);"></div>'
            '<div class="ry-load-line" style="width:460px;height:12px;filter:blur(1.5px);"></div>'
            '<div class="ry-load-line" style="width:430px;height:12px;filter:blur(2.5px);"></div>'
            '<div class="ry-load-line" style="width:480px;height:12px;filter:blur(3.5px);"></div>'
            '<div class="ry-load-line" style="width:300px;height:12px;margin-bottom:8px;filter:blur(4.5px);"></div>'
            '<div class="ry-load-line" style="width:160px;height:14px;margin-top:4px;filter:blur(6px);"></div>'
            '<div class="ry-load-line" style="width:440px;height:12px;filter:blur(8px);"></div>'
            '<div class="ry-load-line" style="width:400px;height:12px;filter:blur(10px);"></div>'
            '</div>'
            '</div>',
            unsafe_allow_html=True,
        )
        # PENTING — 2 lapis bug yang kekonfirmasi langsung lewat inspeksi DOM
        # (bukan tebakan):
        # 1) Streamlit/React makai ULANG elemen DOM kartu-teks yang sama
        #    antar titik (cuma isi teksnya yang di-patch), jadi animasi CSS
        #    clip-path yang udah kelar di titik sebelumnya TIDAK otomatis
        #    restart pas titik baru mulai.
        # 2) components.html JUGA kena masalah yang sama: kalau isi
        #    <script>-nya PERSIS SAMA tiap titik, iframe-nya ikut dipakai
        #    ulang (nggak reload), jadi script restart itu sendiri cuma
        #    kejalan SEKALI aja di titik pertama, nggak pernah jalan lagi.
        # Makanya di titik #2 ini kode di dalam iframe SENGAJA dikasih
        # komentar unik (nomor+nama titik) biar srcdoc-nya beda tiap kali,
        # maksa iframe-nya reload & script restart-nya beneran kejalan
        # ulang tiap titik baru.
        components.html(
            f"""
            <script>
            // ry-point-marker:{idx}:{current}
            function ryRestartRevealAnim() {{
                try {{
                    var doc = window.parent.document;
                    var els = doc.querySelectorAll('.ry-load-card, .ry-load-text-box');
                    els.forEach(function (el) {{
                        el.style.animation = 'none';
                        void el.offsetWidth;
                        el.style.animation = '';
                    }});
                }} catch (e) {{}}
            }}
            requestAnimationFrame(function () {{ requestAnimationFrame(ryRestartRevealAnim); }});
            </script>
            """,
            height=0,
        )
        time.sleep(ANIM_SECONDS)
        # (hasil sudah dihitung di atas, sebelum kartu teaser dirender)
        st.session_state.loading_idx += 1
        st.session_state.loading_phase = "need_check"
        st.rerun()
