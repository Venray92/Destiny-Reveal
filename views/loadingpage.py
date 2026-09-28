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
import textwrap
import time
from datetime import date

import streamlit as st
import streamlit.components.v1 as components

from content.result_builder import build_display_data, compute_raw_result
from settings import PRICE_PANJANG, PRICE_PENDEK
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
# Numerologi versi lengkap (Expression/Soul Urge/Personality Number) butuh
# nama lengkap (sesuai nama lahir) selain tanggal lahir.
NEEDS_NAMA = {"Numerologi"}
# belum ada kuesionernya — dilewati dulu (lihat catatan keterbatasan di atas)
NEEDS_KUESIONER_BELUM_ADA = {"MBTI", "Big Five", "Enneagram", "DISC", "Love Language"}

FIELD_LABEL = {
    "tanggal_lahir": "Masukkan Tanggal Lahir",
    "nama_lengkap": "Masukkan Nama Lengkap",
    "tanggal_lahir_dan_nama": "Lengkapi Data Dasar",
    "jam_lahir": "Masukkan Jam Lahir",
    "kota_lahir": "Masukkan Kota Lahir",
    "golongan_darah": "Masukkan Golongan Darah",
}

ANIM_SECONDS = 5
# Jeda diam setelah 1 kartu titik selesai reveal-in, sebelum pindah ke
# titik berikutnya — biar transisinya nggak kerasa hentakan/jolt.
PAUSE_BETWEEN_POINTS_SECONDS = 2
# Jeda diam setelah titik TERAKHIR selesai, sebelum floating window
# payment (_final_dialog) muncul — dipisah dari PAUSE_BETWEEN_POINTS_SECONDS
# karena ini cuma dipakai SEKALI di akhir, dijaga lewat flag
# session_state.final_ready biar nggak keulang tiap rerun selama dialog
# masih kebuka (lihat render()).
FINAL_PAUSE_SECONDS = 3


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
        st.session_state.final_ready = False


def _points_need_nama():
    """True kalau SALAH SATU titik di mode yang lagi jalan butuh nama
    lengkap (skr cuma Numerologi) — dipakai buat mutusin apa nama harus
    ikut ditanya di dialog pertama (bareng tanggal lahir), bukan ditunda
    sampai titik yang beneran butuh nama kena giliran."""
    return any(s in NEEDS_NAMA for s in st.session_state.get("loading_points", []))


def _missing_field_for(system):
    data = st.session_state.loading_data
    # Sistem yang kuesionernya belum ada (MBTI dkk) tetap butuh data DASAR
    # (tanggal lahir) biar titiknya nggak dilewat diam-diam tanpa nanya
    # apa-apa — biar urutannya jelas: titik pertama di mode manapun selalu
    # nanya tanggal lahir dulu, titik berikutnya yang butuh data sama
    # otomatis nggak nanya lagi.
    needs_tanggal = system in NEEDS_TANGGAL or system in NEEDS_KUESIONER_BELUM_ADA
    if needs_tanggal and "tanggal_lahir" not in data:
        # Kalau mode ini bakal ketemu titik yang butuh nama (mis. Numerologi)
        # di titik manapun, nama-nya SEKALIAN ditanya bareng tanggal di
        # dialog pertama ini juga — bukan nunggu sampai titik Numerologi
        # kena giliran (biar user nggak diinterupsi lagi di tengah jalan).
        if _points_need_nama() and "nama_lengkap" not in data:
            return "tanggal_lahir_dan_nama"
        return "tanggal_lahir"
    if system in NEEDS_NAMA and "nama_lengkap" not in data:
        return "nama_lengkap"
    if system in NEEDS_JAM and "jam_lahir" not in data:
        return "jam_lahir"
    if system in NEEDS_KOTA and "kota_lahir" not in data:
        return "kota_lahir"
    if system in NEEDS_GOLDA and "golongan_darah" not in data:
        return "golongan_darah"
    return None


def _validate_nama(nama):
    """Return pesan error (string) kalau nama nggak valid, None kalau
    valid. Syarat: minimal 4 huruf, nggak boleh ada angka."""
    nama = (nama or "").strip()
    if not nama:
        return "Nama lengkap belum diisi."
    if len(nama) < 4:
        return "Nama lengkap minimal 4 huruf."
    if any(ch.isdigit() for ch in nama):
        return "Nama lengkap tidak boleh mengandung angka."
    return None


@st.dialog("Reveal Selesai", dismissible=False)
def _final_dialog():
    """
    Floating window paywall di akhir proses loading.

    BELUM ada integrasi payment gateway asli (Midtrans/Xendit dkk) — ini
    SENGAJA cuma tombol "Bypass Payment" buat kebutuhan testing (lihat
    settings.py, TESTING_MODE). Begitu payment gateway beneran siap,
    tombol ini diganti jadi UI pembayaran asli, TIDAK ada auto-lanjut JS
    kayak dialog sebelumnya, karena ini gerbang (gate) — harus benar-benar
    diklik/dibayar, bukan dilewati otomatis.

    Sekarang ada 2 pilihan tier (Versi Pendek vs Versi Panjang) — harga di
    PRICE_PENDEK/PRICE_PANJANG (settings.py) MASIH DUMMY, nunggu angka
    final. Pilihan disimpan ke session_state.report_tier, dipakai
    revealpage.py buat nentuin expander insight domain (Karir/Asmara/dll)
    kebuka langsung atau kekunci per-amplop.
    """
    st.markdown(
        '<div style="text-align:center;padding:6px 0 4px 0;">'
        '<div style="font-size:38px;margin-bottom:10px;">&#10024;</div>'
        '<div style="font-family:\'Fraunces\',serif;font-size:19px;font-weight:800;'
        'color:#1c1a17;letter-spacing:0.01em;line-height:1.4;">'
        'SEMUA DATA DIRIMU<br>SUDAH DIREVEAL</div>'
        '<div style="font-size:13px;color:#6b6459;margin-top:8px;">'
        'Pilih versi laporan buat buka hasil lengkapnya.</div>'
        '</div>',
        unsafe_allow_html=True,
    )
    st.write("")

    harga_pendek = f"{PRICE_PENDEK:,.0f}".replace(",", ".")
    harga_panjang = f"{PRICE_PANJANG:,.0f}".replace(",", ".")

    # ── Kotak "Versi Pendek" vs "Versi Lengkap" DIPAKSA sama tinggi ──
    # Sebelumnya masing2 cuma <div style="height:100%"> polos di dalam
    # kolom Streamlit — tapi height:100% nggak ngaruh kalau parent
    # (stColumn/stVerticalBlock/stElementContainer) sendiri nggak diregangkan
    # (stretch) dulu secara eksplisit. Reuse teknik "drfillheight" yang udah
    # ada di app.py (kelasnya match lewat [class*="drfillheight"], CSS-nya
    # global jadi kepakai juga di sini): tiap kotak dibungkus
    # st.container(key="drfillheight_tier_...") + div-nya sendiri dikasih
    # flex:1 biar beneran ngisi penuh tinggi kolom yang udah di-stretch.
    col_pendek, col_panjang = st.columns(2)
    with col_pendek:
        with st.container(key="drfillheight_tier_pendek"):
            st.markdown(
                '<div class="dr-card" style="border:1.5px solid #ecddc9;border-radius:14px;'
                'padding:14px 12px;background:#fdfaf5;box-sizing:border-box;text-align:left;">'
                '<div style="font-size:11px;font-weight:800;letter-spacing:0.04em;'
                'text-transform:uppercase;color:#8a5a2f;">Versi Pendek</div>'
                f'<div style="font-size:17px;font-weight:800;color:#1c1a17;margin-top:2px;">Rp {harga_pendek}</div>'
                '<div style="font-size:11.5px;color:#6b6459;margin-top:6px;line-height:1.5;">'
                'Mendapatkan semua hasil inti (siapa diri kamu, kekuatan pada dirimu, dan PR '
                'apa yg harus dikerjakan).</div></div>',
                unsafe_allow_html=True,
            )
        st.write("")
        if st.button(
            "Bypass (Pendek)", key="btn_bypass_pendek",
            type="secondary", icon=":material/bolt:", use_container_width=True,
        ):
            st.session_state.report_tier = "pendek"
            st.session_state.dr_page = "result"
            st.rerun()
    with col_panjang:
        with st.container(key="drfillheight_tier_panjang"):
            st.markdown(
                '<div class="dr-card" style="border:1.5px solid #e4a56e;border-radius:14px;'
                'padding:14px 12px;background:#fff8ef;box-sizing:border-box;text-align:left;">'
                '<div style="font-size:11px;font-weight:800;letter-spacing:0.04em;'
                'text-transform:uppercase;color:#b8562f;">Versi Lengkap</div>'
                f'<div style="font-size:17px;font-weight:800;color:#1c1a17;margin-top:2px;">Rp {harga_panjang}</div>'
                '<div style="font-size:11.5px;color:#6b6459;margin-top:6px;line-height:1.5;">'
                'Mendapatkan semua hasil inti, plus insight Karir, Asmara, Keuangan &amp; '
                'Kesehatan buat tiap sistem — langsung kebuka semua amplop tanpa perlu bayar '
                'satu-satu lagi.</div></div>',
                unsafe_allow_html=True,
            )
        st.write("")
        if st.button(
            "Bypass (Lengkap)", key="btn_bypass_panjang",
            type="primary", icon=":material/bolt:", use_container_width=True,
        ):
            st.session_state.report_tier = "panjang"
            st.session_state.dr_page = "result"
            st.rerun()

    st.markdown(
        '<div style="text-align:center;font-size:11px;color:#c9c2b4;margin:10px 0 2px 0;">'
        'Payment gateway asli belum terpasang — kedua tombol di atas masih tombol testing. '
        'Harga di kartu juga masih dummy, nunggu angka final.</div>',
        unsafe_allow_html=True,
    )


def _render_tanggal_inputs():
    """Dropdown 3 bagian (Tanggal / Bulan / Tahun), BUKAN st.date_input
    segmen ketik manual lagi — soalnya lebih gampang dipakai (nggak
    perlu ngetik, bulan otomatis dibatasi cuma 1-12 jadi nggak bisa
    salah ketik angka di luar itu) dan urutannya persis dd/mm/yyyy
    (konvensi umum Indonesia). Dipisah jadi fungsi sendiri karena dipakai
    di dua tempat: dialog tanggal-saja DAN dialog gabungan tanggal+nama."""
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
    # Opsi tanggal (hari) DIHITUNG ULANG tiap kali bulan/tahun berubah
    # (lewat calendar.monthrange), jadi user nggak akan bisa milih
    # tanggal yang nggak valid (mis. 30 Februari). Key selectbox hari
    # sengaja dibuat DINAMIS per kombinasi bulan+tahun (bukan key
    # tetap) supaya Streamlit nggak error "default value is not part
    # of options" kalau user ganti ke bulan yang jumlah harinya lebih
    # sedikit dari tanggal yang lagi kepilih sebelumnya.
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
    return date(tahun, bulan, hari)


def _render_nama_input():
    st.markdown(
        '<div style="font-size:12.5px;color:#6b6459;margin:-4px 0 10px 0;">'
        'Pakai nama lahir lengkap kamu — dipakai buat hitung Numerologi versi lengkap.</div>',
        unsafe_allow_html=True,
    )
    return st.text_input(
        "Nama Lengkap", placeholder="Contoh: Budi Santoso (min. 4 huruf, tanpa angka)",
        key="dlg_nama_lengkap", label_visibility="collapsed",
    ).strip()


@st.dialog("Lengkapi Data", dismissible=False)
def _ask_field_dialog(field):
    st.markdown(
        f'<div style="font-family:\'Fraunces\',serif;font-size:20px;font-weight:700;'
        f'color:#1c1a17;margin-bottom:14px;">{FIELD_LABEL[field]}</div>',
        unsafe_allow_html=True,
    )
    tanggal_value = None
    nama_value = None
    if field == "tanggal_lahir":
        tanggal_value = _render_tanggal_inputs()
    elif field == "nama_lengkap":
        nama_value = _render_nama_input()
    elif field == "tanggal_lahir_dan_nama":
        tanggal_value = _render_tanggal_inputs()
        st.write("")
        nama_value = _render_nama_input()
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
        if field == "tanggal_lahir_dan_nama":
            err = _validate_nama(nama_value)
            if err:
                st.warning(err, icon=":material/error:")
            else:
                st.session_state.loading_data["tanggal_lahir"] = tanggal_value
                st.session_state.loading_data["nama_lengkap"] = nama_value
                st.session_state.loading_phase = "animating"
                st.rerun()
        elif field == "tanggal_lahir":
            st.session_state.loading_data[field] = tanggal_value
            st.session_state.loading_phase = "animating"
            st.rerun()
        elif field == "nama_lengkap":
            err = _validate_nama(nama_value)
            if err:
                st.warning(err, icon=":material/error:")
            else:
                st.session_state.loading_data[field] = nama_value
                st.session_state.loading_phase = "animating"
                st.rerun()
        else:
            st.session_state.loading_data[field] = value
            st.session_state.loading_phase = "animating"
            st.rerun()


def _input_summary_html():
    """
    Ringkasan data yang udah diisi user (tanggal lahir dkk), ditampilkan di
    bawah judul "Sedang Membaca Dirimu..." biar user bisa cek ulang
    input-nya nggak salah ketik/pilih sebelum nunggu proses selesai.

    Return HTML string (BUKAN langsung st.markdown) — dipanggil bareng
    header/dots/kartu dalam SATU st.markdown gabungan (lihat catatan
    "kenapa digabung" di render()), biar semuanya nyampe ke browser
    sebagai satu potongan DOM, bukan elemen-elemen terpisah yang bisa
    ke-update nggak bareng.
    """
    data = st.session_state.get("loading_data", {})
    tanggal_str = format_tanggal_ddmmyyyy(data.get("tanggal_lahir"))
    nama = data.get("nama_lengkap")
    if not tanggal_str and not nama:
        return ""
    badges = []
    if tanggal_str:
        badges.append(
            '<span class="ry-load-input-summary"><span class="material-symbols-outlined" '
            'style="font-size:15px;vertical-align:-2px;">calendar_month</span> '
            f'Tanggal Kamu: <b>{tanggal_str}</b></span>'
        )
    if nama:
        badges.append(
            '<span class="ry-load-input-summary"><span class="material-symbols-outlined" '
            'style="font-size:15px;vertical-align:-2px;">badge</span> '
            f'Nama Kamu: <b>{nama}</b></span>'
        )
    return (
        '<div style="text-align:center;margin-top:8px;display:flex;gap:8px;'
        f'justify-content:center;flex-wrap:wrap;">{"".join(badges)}</div>'
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
            flex-shrink: 0; transition: background-color 0.25s ease, border-color 0.25s ease; }
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
            margin-top: 32px;
            /* Fade-in halus tiap kali titik baru mulai — biar transisi
               antar titik nggak kerasa "hentakan"/nge-jolt pas kartu lama
               digantikan kartu baru secara instan (DOM-nya dipakai ulang
               oleh Streamlit, lihat catatan restart-animasi di bawah). */
            animation: ry-fadein 0.5s ease;
        }
        .ry-load-card {
            width: 240px; height: 340px; border-radius: 18px; padding: 6px;
            background: linear-gradient(155deg, #f3d488, #c9a227 45%, #8a6a12 55%, #f3d488);
            box-shadow: 0 20px 40px -18px rgba(139,90,47,0.45);
            /* clip-path STATIS (bukan cuma lewat animasi) disamain persis
               sama keyframe "from" ry-reveal di bawah — BUG YANG
               DIPERBAIKI (27 Sep 2026, kekonfirmasi lewat rekaman video
               Stev: kartu titik BARU sempet kelihatan FULL TERBUKA
               sekilas dulu, baru tiba-tiba blank total, baru pelan-pelan
               kebuka lagi — bukan cuma "kedip" biasa, kartu lama beneran
               "flash" full sebelum di-reset). Root cause: DOM kartu
               dipakai ulang Streamlit antar titik (cuma konten yang
               di-patch), jadi begitu HTML titik baru masuk, elemennya
               masih mewarisi clip-path HASIL AKHIR animasi titik
               SEBELUMNYA (0% = full terbuka, ke-persist lewat
               animation-fill-mode:forwards) SAMPAI trik JS restart di
               bawah beneran jalan (E2 requestAnimationFrame, telat
               1-2 frame). Window itu yang bikin konten baru sempet
               "flash" full duluan sebelum di-reset ke tertutup buat
               direveal ulang. Fix: paksa clip-path mulai TERTUTUP
               dari HTML/CSS-nya sendiri (bukan nunggu animasi/JS),
               jadi begitu konten titik baru di-patch ke DOM, LANGSUNG
               ketutup — nggak ada window buat "flash" muncul duluan. */
            clip-path: inset(0 0 100% 0);
            animation: ry-reveal var(--ry-anim-s) ease-out forwards;
        }
        .ry-load-card-inner { width: 100%; height: 100%; border-radius: 14px; padding: 3px;
            background: linear-gradient(155deg, #fdf0c8, #c9a227); }
        .ry-load-card-art { width: 100%; height: 100%; border-radius: 12px; overflow: hidden;
            background: linear-gradient(150deg, #e9c9a6, #c9683a 55%, #8a5a2f); filter: blur(3.5px); opacity: 0.9; }
        .ry-load-text-box { width: 100%; max-width: 560px; background: #fdfaf5;
            border: 2px solid #f0e6d5; border-radius: 20px; padding: 26px 30px;
            display: flex; flex-direction: column; align-items: flex-start; gap: 6px;
            /* Sama kayak .ry-load-card di atas — clip-path statis biar
               nggak sempet "flash" nunjukin teks titik lama/baru full
               sebelum direset animasinya. */
            clip-path: inset(0 0 100% 0);
            animation: ry-reveal var(--ry-anim-s) ease-out forwards;
        }
        /* Teaser sekarang pakai TEKS ASLI (bukan bar kosong lagi) — judul
           di atas kebaca jelas, tiap paragraf di bawahnya punya
           filter:blur(...) sendiri lewat inline style (gradasi makin
           tebal ke bawah, lihat blur_steps di Python), bukan indikator
           persen. */
        .ry-load-teaser-title { font-family: 'Fraunces', serif; font-size: 15.5px; font-weight: 700;
            color: #8a5a2f; margin: 0 0 4px 0; text-align: left; }
        .ry-load-line-text { margin: 0; font-size: 13px; line-height: 1.65; color: #3a352c;
            text-align: left; }
        @keyframes ry-reveal {
            from { clip-path: inset(0 0 100% 0); }
            to { clip-path: inset(0 0 0% 0); }
        }
        @keyframes ry-fadein {
            from { opacity: 0; transform: translateY(4px); }
            to { opacity: 1; transform: translateY(0); }
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

        /* st.error/st.warning/st.info/st.success (dipakai buat pesan validasi
           soal kuesioner belum lengkap, dst) — BUG CSS DARK-MODE YANG SAMA
           kayak stDialog di atas: widget-nya ikut skema warna dark-mode
           browser/OS (background jadi item pekat, teks susah kebaca),
           bukan tema terang brand. Dipaksa terang + border/warna senada
           sama .ry-load warning box (oranye) yang udah dipakai di tempat
           lain (mis. _anti_leave_banner di loadingpage_mendalam.py). */
        [data-testid="stAlert"], [data-testid="stAlertContainer"] {
            background-color: #fff3e0 !important;
            border: 1.5px solid #e4a56e !important;
            border-radius: 12px !important;
        }
        [data-testid="stAlert"] *, [data-testid="stAlertContainer"] * {
            color: #8a5a2f !important;
            fill: #8a5a2f !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def _dots_html(points, idx, waiting=False):
    """Return HTML string dot-row (BUKAN langsung st.markdown) — lihat
    catatan di _input_summary_html() soal kenapa ini digabung jadi satu
    potongan HTML sama header/kartu, bukan dipanggil terpisah lagi."""
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
    return "".join(dots_html)


def _animate_point(points, idx, header_html):
    """
    Render kartu teaser 1 titik (idx dari points), hitung hasil ASLI-nya
    (compute_raw_result, disimpan ke loading_results), lalu tunggu
    ANIM_SECONDS + PAUSE_BETWEEN_POINTS_SECONDS.

    DIEKSTRAK (27 Sep 2026, batch Loading Page 3/Mode Lengkap) dari isi
    branch "animating" di render() di bawah — SAMA PERSIS isinya, cuma
    dipindah jadi fungsi sendiri biar bisa dipakai ULANG oleh
    views/loadingpage_lengkap.py (Mode Lengkap butuh animasi titik yang
    SAMA PERSIS buat 10 sistem berbasis data, sebelum lanjut ke kuesioner)
    tanpa nyalin ulang ~150 baris kode delicate (3 lapis fix hentakan/kedip
    dkk, lihat catatan di bawah). TIDAK ADA perubahan behavior/tampilan
    dari versi sebelumnya, murni pemindahan kode.
    """
    total = len(points)
    current = points[idx]
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

    # ── Teaser teks PAKAI TEKS ASLI (bukan bar kosong lagi) — cuma
    # baris paling atas yang kebaca jelas, sisanya diblur progresif
    # makin ke bawah makin tebal sampai nggak kebaca sama sekali.
    # SENGAJA bukan indikator persen (sempat diusulkan, tapi
    # dibatalkan) — cuma teks asli + blur gradasi. Sumber teksnya
    # paragraf "Kekuatan & yang Perlu Dijaga" (p2), fallback ke p1
    # kalau p2 nggak ada, dan ke teks generik kalau sistemnya belum
    # punya konten sama sekali (mis. kuesioner yang belum dibangun).
    display_data = build_display_data(current, current_raw_result) or {}
    teaser_title = display_data.get("title") or current
    teaser_body = display_data.get("p2") or display_data.get("p1") or (
        f"Sedang menghitung insight {current}mu..."
    )
    wrapped_lines = textwrap.wrap(teaser_body, width=56)[:8] or [teaser_body]
    blur_steps = [0, 0.8, 2, 3.5, 5.2, 7, 9, 11]
    lines_html = "".join(
        f'<p class="ry-load-line-text" style="filter:blur({blur_steps[min(i, len(blur_steps) - 1)]}px);">{line}</p>'
        for i, line in enumerate(wrapped_lines)
    )

    st.markdown(
        header_html
        + _dots_html(points, idx, waiting=False)
        + f'<div class="ry-load-card-wrap" style="--ry-anim-s:{ANIM_SECONDS}s;">'
        '<div style="font-size:11px;font-weight:800;letter-spacing:0.08em;'
        f'text-transform:uppercase;color:#b8562f;">✓ {current} — sedang diproses</div>'
        f'<div class="ry-load-card" data-point-idx="{idx}" style="--ry-anim-s:' + str(ANIM_SECONDS) + 's;">'
        f'<div class="ry-load-card-inner"><div class="ry-load-card-art">{card_art_inner}</div></div>'
        '</div>'
        f'<div class="ry-load-text-box" data-point-idx="{idx}" style="--ry-anim-s:' + str(ANIM_SECONDS) + 's;">'
        f'<div class="ry-load-teaser-title">{teaser_title}</div>'
        f'{lines_html}'
        '</div>'
        '</div>',
        unsafe_allow_html=True,
    )
    # BUG YANG DIPERBAIKI (27 Sep 2026, rekaman video Stev nunjukin
    # kartu titik baru "flash" full terbuka sekilas dulu baru tiba-tiba
    # blank total, baru pelan-pelan direveal ulang — bukan cuma
    # "kedip", beneran nge-jolt drastis):
    #
    # 3 lapis root cause yang KEKONFIRMASI langsung lewat inspeksi DOM
    # (dites: tag elemen kartu titik-1 dengan marker custom, cek lagi
    # setelah pindah titik-2 — hasilnya SAMA OBJECT DOM, cuma
    # attribute/isinya yang di-patch, bukan dibuat ulang):
    # 1) Streamlit/React makai ULANG elemen DOM kartu+text-box yang
    #    sama persis antar titik (cuma konten yang di-patch in-place).
    # 2) Animasi CSS (clip-path reveal) yang udah kelar di titik
    #    SEBELUMNYA nge-persist ("forwards" fill-mode) di elemen itu
    #    dan TETAP menang/override apapun rule CSS statis lain SAMPAI
    #    animasinya beneran di-disable eksplisit — jadi begitu konten
    #    titik BARU di-patch masuk, kartu itu SEMPAT kelihatan full
    #    terbuka dulu (masih mewarisi status "selesai" dari titik
    #    lama), padahal isinya udah titik baru.
    # 3) Trik reset lama (iframe components.html dengan komentar unik
    #    per titik biar reload) BARU jalan beberapa frame KEMUDIAN
    #    (iframe baru butuh waktu dibuat+dimuat), jadi ada window nyata
    #    dimana user lihat "kartu baru full terbuka -> tiba-tiba di-reset
    #    ke tertutup -> pelan-pelan kebuka lagi" — itu yang kerasa jolt.
    #
    # FIX: pasang SATU iframe PERSISTEN (srcdoc-nya SENGAJA statis/sama
    # tiap titik, BUKAN dikasih komentar unik lagi) yang isinya cuma
    # masang MutationObserver SEKALI di awal, mengamati atribut
    # data-point-idx di kartu/text-box (di-set di HTML atas). Karena
    # srcdoc-nya sama, Streamlit TIDAK reload iframe-nya tiap titik
    # (beda dari sebelumnya) — jadi observer-nya tetap hidup dari titik
    # pertama sampai terakhir. Callback MutationObserver jalan sebagai
    # microtask SEGERA setelah DOM di-patch, SEBELUM browser sempat
    # nge-paint frame berikutnya — jadi reset animasinya kejadian
    # duluan sebelum sempat kelihatan "flash" kartu lama yang masih
    # terbuka.
    # ── Ghost floating-window (st.dialog "Lengkapi Data") yang kedip
    # sekilas di titik-titik SETELAH titik pertama (dilaporkan Stev,
    # 27 Sep 2026 — "kedipannya kaya kedipan floating windows") ──
    # DIBUKTIKAN lewat log server (loading_phase/missing dicatat tiap
    # rerun): dari sisi Python, dialog "Lengkapi Data" CUMA dipanggil
    # SEKALI (titik pertama, pas datanya beneran belum ada) — titik
    # ke-2 dst selalu missing=None, dialognya TIDAK dipanggil lagi.
    # TAPI dari sisi browser, elemen [data-testid="stDialog"] yang
    # ISINYA SAMA PERSIS (dialog titik-1 yang udah kelar) kedetect
    # nongol lagi sekilas (~0.4 detik) pas titik lain lagi animating —
    # ini murni artefak sisi Streamlit-nya sendiri (DOM dialog lama
    # ke-cache/nyangkut, sempat ke-render ulang pas rerun besar),
    # BUKAN dialog baru yang beneran diminta app.
    #
    # FIX: karena iframe ini CUMA hidup selama fase "animating" (fase
    # dimana TIDAK ADA dialog yang seharusnya muncul sama sekali —
    # dialog data cuma legit di fase "asking" di titik pertama, dan
    # dialog payment cuma legit di layar akhir setelah SEMUA titik
    # kelar, keduanya di luar fase "animating" jadi iframe ini otomatis
    # sudah dilepas Streamlit sebelum keduanya render) — SELAMA iframe
    # ini hidup, floating window apapun yang nongol sudah pasti ghost,
    # aman langsung dipaksa disembunyikan tanpa perlu cek fase lagi.
    components.html(
        """
        <script>
        (function () {
            var doc = window.parent.document;
            var lastIdx = {};
            function resetAnim(el) {
                if (!el) return;
                var pid = el.getAttribute('data-point-idx');
                var key = el.className;
                if (lastIdx[key] === pid) return;
                lastIdx[key] = pid;
                el.style.animation = 'none';
                void el.offsetWidth;
                el.style.animation = '';
            }
            function killGhostDialogs() {
                // BUG BARU YANG DIKETEMUKAN (28 Sep 2026 pagi, dilaporkan
                // Stev di Mode Lengkap: floating window kuesioner/payment
                // rusak -- muncul sebagai blok biasa DI BAWAH konten,
                // bukan ngambang di tengah layar): observer ini disimpen
                // di window.parent (bukan di iframe-nya sendiri) SUPAYA
                // nggak pasang ulang tiap titik, TAPI itu artinya begitu
                // observer ini kepasang, dia HIDUP TERUS SELAMANYA --
                // nggak otomatis mati pas Mode Lengkap pindah dari fase
                // animasi bio (halaman ini) ke halaman kuesioner
                // (loadingpage_mendalam.py). Akibatnya observer LAMA ini
                // masih jalan pas dialog LEGIT (intro kuesioner/"siap
                // lanjut?"/payment akhir) muncul di halaman baru, dan
                // langsung di-display:none-in paksa karena dikira ghost
                // dialog juga -- padahal itu dialog asli yang seharusnya
                // ngambang normal.
                //
                // FIX: cuma anggap "masih di fase animasi" kalau kartu
                // titiknya (.ry-load-card / .ry-load-text-box) MASIH ada
                // di DOM. Begitu itu nggak ketemu lagi (pindah halaman),
                // observer ini langsung disconnect + hapus referensinya
                // sendiri -- self-cleanup, biar dialog di halaman
                // berikutnya nggak pernah kesentuh lagi.
                if (!doc.querySelector('.ry-load-card') &&
                    !doc.querySelector('.ry-load-text-box')) {
                    if (window.parent.__ryObserver) {
                        try { window.parent.__ryObserver.disconnect(); } catch (e) {}
                        delete window.parent.__ryObserver;
                    }
                    return;
                }
                var dlgs = doc.querySelectorAll('[data-testid="stDialog"]');
                dlgs.forEach(function (d) {
                    d.style.setProperty('display', 'none', 'important');
                });
            }
            function checkAll() {
                resetAnim(doc.querySelector('.ry-load-card'));
                resetAnim(doc.querySelector('.ry-load-text-box'));
                killGhostDialogs();
            }
            if (window.parent.__ryObserver) {
                // Observer sebelumnya udah kepasang (iframe ini dipakai
                // ulang, bukan baru) — cukup jalanin cek sekali buat
                // titik yang baru masuk, observer lamanya tetap jalan.
                checkAll();
                return;
            }
            var mo = new MutationObserver(function () { checkAll(); });
            try {
                mo.observe(doc.body, {
                    attributes: true, childList: true, subtree: true,
                });
                window.parent.__ryObserver = mo;
            } catch (e) {}
            checkAll();
        })();
        </script>
        """,
        height=0,
    )
    time.sleep(ANIM_SECONDS)
    # Jeda TAMBAHAN setelah kartu ini selesai reveal-in (animasi
    # clip-path-nya udah kelar penuh), biar kartu yang udah jadi sempat
    # "diam" dulu sebentar sebelum digantikan kartu titik berikutnya —
    # mengurangi kesan hentakan/jolt pas transisi (dilaporkan Stev:
    # pergantian kartu kerasa kayak ada hentakan kalau langsung diganti
    # sedetik itu juga).
    time.sleep(PAUSE_BETWEEN_POINTS_SECONDS)
    # (hasil sudah dihitung di atas, sebelum kartu teaser dirender)


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
            '</div>'
            f'{_input_summary_html()}'
            '<div style="height:16px;"></div>'
            f'{_dots_html(points, idx, waiting=False)}',
            unsafe_allow_html=True,
        )
        if not st.session_state.get("final_ready"):
            st.markdown(
                '<div style="text-align:center;margin-top:22px;font-size:13px;'
                'color:#8a5a2f;font-style:italic;">Menyusun laporan akhir...</div>',
                unsafe_allow_html=True,
            )
            time.sleep(FINAL_PAUSE_SECONDS)
            st.session_state.final_ready = True
            st.rerun()
        _final_dialog()
        return

    current = points[idx]

    # ── Header ("Sedang Membaca Dirimu...") + ringkasan input — DIGABUNG
    # jadi satu string HTML bareng dots/kartu di bawah (bukan dipanggil
    # st.markdown terpisah lagi kayak sebelumnya). ──
    # BUG YANG DIPERBAIKI (27 Sep 2026, dilaporkan Stev sebagai "hentakan"/
    # "kedip" pas ganti titik, kejadian random di titik manapun — sudah
    # dibuktikan lewat rekaman + pengukuran, BUKAN cuma tebakan): Streamlit
    # ngirim tiap st.markdown/komponen sebagai elemen ("delta") TERPISAH ke
    # browser saat itu juga diproses, BUKAN nunggu semua elemen di satu
    # rerun selesai baru dikirim bareng. Header+dot-row (teks kecil, cepat
    # sampai) sebelumnya dipanggil LEWAT st.markdown SENDIRI, sedangkan
    # kartu di bawahnya (isinya gambar base64 ~2MB, lebih berat/lambat
    # sampai) lewat st.markdown TERPISAH lagi. Akibatnya ada window
    # (~0.5-0.7 detik, terukur lewat Playwright) dimana header/dot udah
    # nunjuk ke titik BARU tapi kartu di bawahnya masih nampilin titik LAMA
    # — begitu kartu akhirnya nyusul ganti, itu yang kerasa sebagai
    # hentakan. Fix-nya: gabung header+summary+dots+kartu jadi SATU
    # st.markdown (satu delta), biar browser nge-patch semuanya BARENG,
    # bukan kepisah-pisah kayak sebelumnya.
    header_html = (
        '<div style="text-align:center;">'
        '<div style="font-family:\'Fraunces\',serif;font-size:30px;font-weight:700;color:#1c1a17;margin-bottom:8px;">'
        'Sedang Membaca Dirimu...</div>'
        f'<div style="font-size:14.5px;color:#6b6459;">Titik {idx + 1} dari {total} sedang diproses '
        '— jangan tutup halaman ini ya.</div>'
        '</div>'
        f'{_input_summary_html()}'
        '<div style="height:16px;"></div>'
    )

    # ── STATE MACHINE per titik ──
    if st.session_state.loading_phase == "need_check":
        # Fase ini nggak nampilin apa-apa ke user (langsung rerun ke fase
        # berikutnya), jadi header nggak perlu dirender di sini — biar
        # nggak sempat kelihatan sekilas dengan dots/kartu titik LAMA yang
        # belum sempat diganti (bakal langsung ketimpa rerun berikutnya).
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
        st.markdown(
            header_html
            + _dots_html(points, idx, waiting=True)
            + '<div class="ry-load-card-wrap">'
            '<div class="ry-load-waiting-box">Menunggu data...</div>'
            '</div>',
            unsafe_allow_html=True,
        )
        missing = _missing_field_for(current)
        _ask_field_dialog(missing)

    elif st.session_state.loading_phase == "animating":
        _animate_point(points, idx, header_html)
        st.session_state.loading_idx += 1
        st.session_state.loading_phase = "need_check"
        st.rerun()
