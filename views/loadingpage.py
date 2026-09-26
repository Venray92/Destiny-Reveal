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
- Isi tiap kartu/teks masih dummy placeholder (bukan hasil perhitungan
  asli), karena engine shio/numerologi/matrix_destiny/dst masih stub
  (lihat progress-notes.md).
"""

import time

import streamlit as st
import streamlit.components.v1 as components

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
    st.markdown(
        '<div style="text-align:center;padding:6px 0 4px 0;">'
        '<div style="font-size:38px;margin-bottom:10px;">&#10024;</div>'
        '<div style="font-family:\'Fraunces\',serif;font-size:19px;font-weight:800;'
        'color:#1c1a17;letter-spacing:0.01em;line-height:1.4;">'
        'SEMUA DATA DIRIMU<br>SUDAH DIREVEAL</div>'
        '</div>',
        unsafe_allow_html=True,
    )
    st.write("")
    if st.button(
        "REVEAL YOURSELF", key="btn_final_reveal", type="primary",
        icon=":material/auto_awesome:", use_container_width=True,
    ):
        st.session_state.dr_page = "result"
        st.rerun()
    st.markdown(
        '<div style="text-align:center;font-size:11.5px;color:#9a948a;margin-top:10px;">'
        'Kalau tidak diklik, otomatis lanjut dalam beberapa detik.</div>',
        unsafe_allow_html=True,
    )
    # Auto-lanjut kalau user nggak klik tombolnya — nyari tombol primary DI
    # DALAM dialog ini lewat DOM (sama origin, jadi window.parent.document
    # bisa diakses), lalu diklik beneran lewat JS setelah 5 detik. Dipilih
    # cara ini (bukan time.sleep di Python) supaya tombolnya TETAP bisa
    # diklik manual kapan aja selama proses ini berjalan (nggak nge-block
    # script servernya kayak time.sleep biasa).
    components.html(
        """
        <script>
        setTimeout(function () {
            try {
                var doc = window.parent.document;
                var btn = doc.querySelector('[data-testid="stDialog"] button[kind="primary"]');
                if (btn) { btn.click(); }
            } catch (e) {}
        }, 5000);
        </script>
        """,
        height=0,
    )


@st.dialog("Lengkapi Data", dismissible=False)
def _ask_field_dialog(field):
    st.markdown(
        f'<div style="font-family:\'Fraunces\',serif;font-size:20px;font-weight:700;'
        f'color:#1c1a17;margin-bottom:14px;">{FIELD_LABEL[field]}</div>',
        unsafe_allow_html=True,
    )
    if field == "tanggal_lahir":
        value = st.date_input("Tanggal Lahir", key="dlg_tanggal_lahir", label_visibility="collapsed")
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


def _inject_style():
    st.markdown(
        """
        <style>
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
            background: linear-gradient(150deg, #e9c9a6, #c9683a 55%, #8a5a2f); filter: blur(7px); opacity: 0.9; }
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
        st.markdown(
            f'<div class="ry-load-card-wrap" style="--ry-anim-s:{ANIM_SECONDS}s;">'
            '<div style="font-size:11px;font-weight:800;letter-spacing:0.08em;'
            f'text-transform:uppercase;color:#b8562f;">✓ {current} — sedang diproses</div>'
            '<div class="ry-load-card" style="--ry-anim-s:' + str(ANIM_SECONDS) + 's;">'
            '<div class="ry-load-card-inner"><div class="ry-load-card-art"></div></div>'
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
        time.sleep(ANIM_SECONDS)
        if current not in st.session_state.loading_results:
            st.session_state.loading_results[current] = {"placeholder": True}
        st.session_state.loading_idx += 1
        st.session_state.loading_phase = "need_check"
        st.rerun()
