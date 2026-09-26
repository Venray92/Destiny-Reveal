"""
Halaman hasil akhir — "amplop bercap emas".

Konsep (sesuai mock yang disetujui, artifact Design "Reveal Page + Paywall
Mockup"): tiap sistem yang sudah diproses di halaman loading ditampilkan
sebagai amplop tertutup. User ketuk amplopnya satu per satu, ada animasi
"terbuka" singkat (efek bintang), lalu hasil lengkap sistem itu muncul di
bawah grid amplop (kartu emas + tulisan 3 paragraf + kutipan).

KETERBATASAN per revisi ini (sengaja, biar jelas bukan ditutup-tutupi):
- 5 sistem berbasis tanggal lahir (Zodiak, Shio, Weton, Numerologi, Matrix
  Destiny) SEKARANG menampilkan hasil perhitungan ASLI dari engine/*.py,
  digabung dengan kamus konten di content/interpretations/ lewat
  content/result_builder.py — bukan dummy placeholder lagi.
- DUMMY_RESULTS di bawah ini TETAP disimpan sebagai fallback contoh, dipakai
  cuma kalau hasil aslinya belum ada di session_state (mis. sesi lompat ke
  halaman ini tanpa melalui alur loading beneran).
- Sistem lain di luar 5 itu (BaZi, Zi Wei, Human Design, MBTI, Big Five,
  Enneagram, DISC, Golongan Darah, Love Language, Tarot) belum punya
  engine/konten — amplopnya tetap bisa dibuka tapi isinya jujur bilang
  "belum tersedia", bukan dikarang panjang-panjang.
- Paywall (floating window minta pembayaran sebelum halaman ini kebuka) dan
  auto-kirim PDF ke email BELUM diimplementasi di sini — itu butuh
  integrasi payment gateway + email yang belum ada infrastrukturnya. Baris
  "Hasil sudah dikirim ke email kamu" di bawah masih tampilan/teks statis.
"""

import time

import streamlit as st
import streamlit.components.v1 as components

from content.interpretations.matrix_destiny import MATRIX_DESTINY_CONTENT
from content.result_builder import build_display_data
from engine.matrix_destiny import NAMA_ARKETIPE
from utils.card_images import (
    card_filename_for_system,
    card_image_bytes_for_system,
    card_image_for_system,
)
from utils.date_format import format_tanggal_ddmmyyyy
from utils.matrix_destiny_diagram import render_octagram_svg_with_tooltips

EXAMPLE_POINTS = ["Zodiak", "Shio", "Weton", "Numerologi", "Matrix Destiny"]
OPEN_ANIM_SECONDS = 1.1

# ── Ikon cap amplop per sistem (dipakai ulang dari mock Design canvas) ──
SEAL_ICONS = {
    "Zodiak": (
        '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="#fdf3e7" '
        'stroke-width="1.6" stroke-linejoin="round"><path d="M12 3l2.2 5.6L20 10l-4.6 3.8L16.8 20 '
        '12 16.6 7.2 20l1.4-6.2L4 10l5.8-1.4L12 3Z"></path></svg>'
    ),
    "Shio": (
        '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="#fdf3e7" '
        'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="14" '
        'r="5"></circle><circle cx="7" cy="7" r="2"></circle><circle cx="17" cy="7" r="2"></circle>'
        '<circle cx="12" cy="5" r="2"></circle></svg>'
    ),
    "Weton": (
        '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="#fdf3e7" '
        'stroke-width="1.6" stroke-linecap="round"><path d="M3 12c2-3 4-3 6 0s4 3 6 0 4-3 6 0">'
        '</path><circle cx="12" cy="12" r="1.4" fill="#fdf3e7" stroke="none"></circle></svg>'
    ),
    "Numerologi": (
        '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="#fdf3e7" '
        'stroke-width="1.6" stroke-linecap="round"><path d="M9 3v18M15 3v18M3 9h18M3 15h18"></path>'
        '</svg>'
    ),
    "Matrix Destiny": (
        '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="#fdf3e7" '
        'stroke-width="1.4" stroke-linecap="round"><path d="M4 18l6-8 4 3 6-9"></path>'
        '<circle cx="4" cy="18" r="1.3" fill="#fdf3e7" stroke="none"></circle>'
        '<circle cx="10" cy="10" r="1.3" fill="#fdf3e7" stroke="none"></circle>'
        '<circle cx="14" cy="13" r="1.3" fill="#fdf3e7" stroke="none"></circle>'
        '<circle cx="20" cy="4" r="1.3" fill="#fdf3e7" stroke="none"></circle></svg>'
    ),
}
DEFAULT_ICON = (
    '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="#fdf3e7" '
    'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">'
    '<circle cx="12" cy="12" r="7"></circle></svg>'
)

# ── Konten dummy 5 sistem contoh ──
DUMMY_RESULTS = {
    "Zodiak": {
        "tagline": "☉ Matahari di Leo",
        "chip": "ZODIAK",
        "title": "Leo — Sang Pemimpin yang Hangat",
        "p1_label": "Siapa Kamu",
        "p1": "Kamu lahir saat matahari berada di rasi Leo, dan hal itu terlihat jelas dari cara "
              "orang-orang merespons kehadiranmu. Ada kehangatan alami dalam dirimu yang membuat "
              "orang di sekitarmu merasa lebih bersemangat begitu kamu masuk ke dalam ruangan. Kamu "
              "juga bukan tipe yang suka menunggu arahan; begitu sebuah ide muncul, kamu biasanya "
              "sudah lebih dulu bergerak.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kepemimpinan memang terasa seperti bagian alami dari dirimu. Kamu mampu membuat orang "
              "lain percaya pada arah yang kamu tunjukkan, bahkan sebelum kamu sendiri sepenuhnya "
              "yakin. Namun semangat besar itu terkadang membuatmu lupa untuk mendengarkan lebih dulu "
              "sebelum mengambil keputusan, padahal orang-orang di sekitarmu juga ingin didengar, "
              "bukan hanya diarahkan.",
        "quote": "Kepemimpinan yang paling kuat adalah yang tahu kapan harus diam dan mendengarkan.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Minggu ini, coba sekali saja menahan diri untuk tidak langsung memberi solusi ketika "
              "ada teman yang bercerita tentang masalahnya. Dengarkan saja sampai selesai. Kamu "
              "mungkin akan terkejut, karena terkadang orang hanya butuh didengar, bukan diarahkan, "
              "dan hal kecil ini justru akan membuat mereka semakin percaya padamu sebagai sosok "
              "pemimpin.",
    },
    "Shio": {
        "tagline": "🐉 Shio Naga",
        "chip": "SHIO",
        "title": "Naga — Sosok yang Sulit Diabaikan",
        "p1_label": "Siapa Kamu",
        "p1": "Dalam kepercayaan Tionghoa, shio Naga dianggap sebagai simbol keberuntungan dan "
              "kekuatan. Kamu punya aura yang membuat orang lain memperhatikanmu tanpa harus berusaha "
              "keras. Rasa percaya diri itu bukan sekadar tampilan luar, tapi tumbuh dari keyakinan "
              "bahwa kamu memang mampu mencapai hal-hal besar kalau diberi kesempatan.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Ambisimu jarang setengah-setengah, dan itu yang membuat orang lain mempercayakan "
              "tanggung jawab besar padamu. Sayangnya, standar tinggi yang kamu pasang untuk diri "
              "sendiri kadang ikut dibebankan ke orang lain tanpa sadar, sehingga mereka bisa merasa "
              "tertekan berada di dekatmu kalau kamu tidak sedikit melunakkan cara menyampaikannya.",
        "quote": "Kekuatan yang sesungguhnya terlihat justru saat kamu memilih untuk lebih lembut.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba luangkan waktu untuk memuji usaha orang lain sebelum menunjukkan apa yang masih "
              "kurang. Kebiasaan kecil ini akan membuat orang-orang di sekitarmu merasa dihargai, "
              "bukan cuma dinilai dari hasil akhirnya saja.",
    },
    "Weton": {
        "tagline": "☾ Jumat Legi",
        "chip": "WETON",
        "title": "Jumat Legi — Neptu 11, Pembawa Ketenangan",
        "p1_label": "Siapa Kamu",
        "p1": "Menurut primbon Jawa, weton Jumat Legi punya neptu 11, gabungan dari hari Jumat "
              "(neptu 6) dan pasaran Legi (neptu 5). Kombinasi ini sering dikaitkan dengan sosok yang "
              "membawa ketenangan bagi lingkungan sekitarnya, tempat orang lain nyaman bercerita dan "
              "meminta pendapat.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kepekaanmu terhadap perasaan orang lain adalah kekuatan besar yang tidak semua orang "
              "punya. Namun karena terlalu sering memikirkan perasaan orang lain, kamu kadang menunda "
              "kepentinganmu sendiri, dan itu bisa membuatmu kelelahan tanpa disadari oleh orang di "
              "sekelilingmu.",
        "quote": "Menjaga perasaan orang lain itu baik, asal tidak sampai melupakan perasaanmu sendiri.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Sesekali, latih diri untuk mengatakan apa yang sebenarnya kamu butuhkan, bukan hanya "
              "apa yang membuat orang lain nyaman. Orang-orang terdekatmu justru akan lebih menghargai "
              "kejujuran itu.",
    },
    "Numerologi": {
        "tagline": "✦ Angka Hidup 8",
        "chip": "NUMEROLOGI",
        "title": "Angka Hidup 8 — Pengelola yang Rapi",
        "p1_label": "Siapa Kamu",
        "p1": "Angka hidup 8 dihitung dari penjumlahan digit tanggal lahirmu, dan dalam numerologi "
              "angka ini identik dengan kemampuan mengelola sesuatu secara terstruktur, baik itu "
              "waktu, uang, maupun rencana jangka panjang. Kamu cenderung berpikir realistis dan "
              "senang melihat hasil yang bisa diukur.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Disiplin dan tanggung jawabmu membuat orang lain merasa aman menitipkan urusan penting "
              "kepadamu. Meski begitu, fokus yang terlalu besar pada hasil kadang membuatmu lupa "
              "menikmati proses, sehingga pencapaian yang seharusnya membanggakan malah terasa "
              "biasa saja.",
        "quote": "Pencapaian akan terasa lebih berarti kalau kamu sempat menikmati perjalanannya.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Coba beri dirimu waktu untuk merayakan pencapaian kecil sebelum langsung berpindah ke "
              "target berikutnya. Kebiasaan ini akan membuat perjalananmu terasa lebih ringan.",
    },
    "Matrix Destiny": {
        "tagline": "✧ The Partners",
        "chip": "MATRIX DESTINY",
        "title": "The Partners — Fondasi bagi Orang-Orang di Sekitarmu",
        "p1_label": "Siapa Kamu",
        "p1": "Dalam pembacaan Matrix Destiny, susunan titik dari tanggal lahirmu membentuk arketipe "
              "The Partners, sosok yang secara alami jadi tempat bersandar bagi keluarga maupun "
              "teman dekat. Kehadiranmu memberi rasa aman, bahkan tanpa kamu perlu berkata banyak.",
        "p2_label": "Kekuatan & yang Perlu Dijaga",
        "p2": "Kesetiaanmu pada orang-orang terdekat jarang tergoyahkan, dan itu membuatmu jadi sosok "
              "yang bisa diandalkan dalam situasi sulit sekalipun. Namun karena terbiasa menjaga "
              "orang lain, kamu kadang lupa bahwa dirimu sendiri juga butuh dijaga oleh seseorang.",
        "quote": "The Partners sejati juga tahu kapan waktunya untuk diam-diam dijaga balik.",
        "p3_label": "PR Kecil Buat Kamu",
        "p3": "Izinkan satu orang terdekatmu untuk benar-benar membantumu minggu ini, tanpa buru-buru "
              "menolak dengan alasan bahwa kamu bisa mengurus semuanya sendiri.",
    },
}


def _dummy_for(system):
    return DUMMY_RESULTS.get(system)


def _raw_result_for(system):
    """Hasil MENTAH (dari engine, sebelum digabung kamus konten) buat satu
    sistem — dipakai buat milih gambar kartu yang SESUAI hasil beneran
    (lihat utils/card_images.card_relative_path_for_result), bukan cuma
    data siap-tampil (_result_for) yang isinya paragraf/teks."""
    return st.session_state.get("loading_results", {}).get(system)


def _result_for(system):
    """
    Data siap-tampil buat satu sistem: pakai hasil perhitungan ASLI kalau
    ada (dari loading_results, digabung kamus konten lewat
    content/result_builder.py), fallback ke DUMMY_RESULTS kalau belum ada
    hasil asli tersimpan (mis. loncat lewat tombol debug "Test →
    Reveal/Hasil Page").
    """
    raw_result = _raw_result_for(system)
    data = build_display_data(system, raw_result)
    if data:
        return data
    return _dummy_for(system)


def _env_col_key(system):
    """Key kontainer per-amplop, dipakai buat target CSS lebar-tetap dan
    target JS auto-scroll (nama sistem bisa ada spasi, mis. 'Matrix
    Destiny', jadi diganti underscore biar aman dipakai di selector)."""
    return f"env_col_{system.replace(' ', '_')}"


def _seal_icon(system):
    return SEAL_ICONS.get(system, DEFAULT_ICON)


def _big_icon(system):
    """Versi ikon cap yang sama tapi diperbesar, dipakai di kartu detail."""
    import re

    icon = _seal_icon(system)
    icon = re.sub(r'width="\d+"', 'width="64"', icon)
    icon = re.sub(r'height="\d+"', 'height="64"', icon)
    return icon


def _ensure_state():
    if "reveal_opened" not in st.session_state:
        st.session_state.reveal_opened = set()
    if "reveal_order" not in st.session_state:
        st.session_state.reveal_order = []
    if "reveal_opening" not in st.session_state:
        st.session_state.reveal_opening = None
    if "reveal_visible" not in st.session_state:
        # Amplop yang sudah dibuka TAPI kartu detailnya lagi ditampilkan.
        # Dipisah dari reveal_opened supaya "Tutup Amplop" cuma nyembunyiin
        # detailnya (biar user gampang toggle tanpa scroll jauh), bukan
        # ngereset status "sudah dibuka" (jadi animasi burst nggak
        # keulang kalau dibuka lagi).
        st.session_state.reveal_visible = set()
    if "reveal_open_all_queue" not in st.session_state:
        # Antrean sistem yang masih perlu dibuka otomatis berurutan lewat
        # tombol "Buka Semua Amplop". Dikosongkan lagi begitu antreannya habis.
        st.session_state.reveal_open_all_queue = []
    if "reveal_confirm_open_all" not in st.session_state:
        # Flag buat nampilin floating window konfirmasi ("Iya"/"Tidak")
        # sebelum proses buka-semua beneran mulai.
        st.session_state.reveal_confirm_open_all = False


def _points():
    points = st.session_state.get("loading_points")
    if points:
        return list(points)
    results = st.session_state.get("loading_results")
    if results:
        return list(results.keys())
    return list(EXAMPLE_POINTS)


def _inject_style():
    st.markdown(
        """
        <style>
        .rp-serif { font-family: 'Fraunces', serif; }
        .rp-header { text-align: center; display: flex; flex-direction: column;
            align-items: center; gap: 12px; margin-bottom: 6px; }
        .rp-badge { display: inline-flex; align-items: center; gap: 6px; padding: 7px 18px;
            border-radius: 100px; background: #fdf3e7; border: 1px solid #ecddc9;
            font-size: 12.5px; font-weight: 700; color: #b8562f; }
        .rp-h1 { margin: 0; font-size: 32px; font-weight: 700; color: #1c1a17;
            max-width: 640px; line-height: 1.25; }
        .rp-sub { margin: 0; font-size: 14px; color: #6b6459; max-width: 520px; line-height: 1.7; }
        .rp-input-summary { display: inline-flex; align-items: center; gap: 8px; margin-top: 2px;
            padding: 6px 16px; border-radius: 100px; background: #f9f4ec; border: 1px solid #ecddc9;
            font-size: 12.5px; color: #6b6459 !important; }
        .rp-input-summary b { color: #1c1a17 !important; font-weight: 800; }

        .rp-trophy-row { display: flex; align-items: flex-start; justify-content: center;
            flex-wrap: wrap; max-width: 760px; margin: 0 auto 4px auto; }
        .rp-trophy-unit { display: flex; flex-direction: column; align-items: center; width: 88px; }
        .rp-trophy-dot { width: 36px; height: 36px; border-radius: 50%; color: #ffffff !important;
            display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 14px; }
        .rp-trophy-dot-done { background: #b8562f; }
        .rp-trophy-label { margin-top: 6px; font-size: 10.5px; font-weight: 700; text-align: center;
            color: #1c1a17 !important; }
        .rp-trophy-chain { width: 28px; height: 3px; background: #b8562f; margin-top: 17px;
            border-radius: 3px; flex-shrink: 0; }

        .rp-env {
            position: relative; height: 220px; background: linear-gradient(160deg, #fdf6e8, #f6e9d2);
            border: 1.5px solid #e8d4ae; border-radius: 16px 16px 0 0;
            box-shadow: 0 14px 30px -18px rgba(139,90,47,0.35); overflow: hidden;
        }
        .rp-env-flap { position: absolute; top: 0; left: 0; width: 100%; height: 92px;
            background: linear-gradient(160deg, #f6e9d2, #ecd8ac);
            clip-path: polygon(0 0, 50% 62%, 100% 0); }
        .rp-env-seal { position: absolute; top: 58px; left: 50%; transform: translateX(-50%);
            width: 52px; height: 52px; border-radius: 50%;
            background: radial-gradient(circle at 35% 30%, #e2a24a, #b8562f 60%, #8a3f1f 100%);
            box-shadow: 0 6px 14px -4px rgba(138,63,31,0.55);
            display: flex; align-items: center; justify-content: center; }
        .rp-env-foot { position: absolute; bottom: 0; left: 0; width: 100%; padding-bottom: 16px;
            display: flex; flex-direction: column; align-items: center; }
        .rp-env-name { font-weight: 800; font-size: 13.5px; color: #5c4326 !important; text-align: center; }
        .rp-env-hint { margin-top: 3px; font-size: 10px; color: #a8916a !important; }

        .rp-env-done {
            position: relative; height: 220px; background: #f3ede0;
            border: 1.5px solid #e4ddd0; border-radius: 16px 16px 0 0; overflow: hidden;
            display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 8px;
        }
        .rp-env-done-check { width: 46px; height: 46px; border-radius: 50%; background: #d9cdb3;
            display: flex; align-items: center; justify-content: center; color: #8a5a2f !important;
            font-weight: 800; font-size: 18px; }

        .rp-env-burst {
            position: relative; height: 220px; border-radius: 16px 16px 0 0;
            background: radial-gradient(circle, #fff6e0, #f3d488 45%, #c9a227 75%, #8a6a12);
            display: flex; align-items: center; justify-content: center; overflow: hidden;
        }
        .rp-burst-star { position: absolute; color: #ffffff; font-size: 16px;
            animation: rp-burst-fly 0.9s ease-out forwards; opacity: 0; }
        @keyframes rp-burst-fly {
            0% { opacity: 1; transform: translate(0,0) scale(0.4); }
            100% { opacity: 0; transform: translate(var(--rp-x), var(--rp-y)) scale(1.3); }
        }
        .rp-env-btn div.stButton > button {
            border-radius: 0 0 16px 16px !important; border: 1.5px solid #e8d4ae !important;
            border-top: none !important; background: #fffaf2 !important; color: #b8562f !important;
            font-weight: 700 !important; font-size: 12.5px !important;
        }

        .rp-detail-hint { display: flex; flex-direction: column; align-items: center; gap: 8px;
            margin-top: 6px; }
        .rp-detail-hint-line { width: 1.5px; height: 22px;
            background: repeating-linear-gradient(to bottom, #d8c7a8 0 6px, transparent 6px 12px); }
        .rp-detail-hint-text { font-size: 12px; color: #a8916a; font-style: italic; }

        .rp-detail { display: flex; gap: 36px; align-items: flex-start; background: #ffffff;
            border: 2px solid #f0e6d5; border-radius: 24px; padding: 34px; margin-top: 4px;
            box-shadow: 0 26px 60px -34px rgba(139,90,47,0.3); flex-wrap: wrap; }
        /* Wadah kartu+teks yang sudah punya gambar asli — dibungkus st.container
           (bukan satu blok HTML datar lagi) supaya tombol "Simpan Gambar" bisa
           disisipkan sebagai widget Streamlit beneran, persis di bawah kartunya. */
        div[class*="st-key-rp_detail_outer_"] {
            display: flex; gap: 36px; align-items: flex-start; background: #ffffff;
            border: 2px solid #f0e6d5; border-radius: 24px; padding: 34px; margin-top: 4px;
            box-shadow: 0 26px 60px -34px rgba(139,90,47,0.3); flex-wrap: wrap;
        }
        /* Ukuran kartu 2x lipat dari sebelumnya (220x300 -> 440x600).
           Wadahnya sekarang st.container (rp_detail_left_...), bukan div
           class biasa, supaya tombol download bisa ikut jadi anak
           Streamlit di dalamnya. */
        div[class*="st-key-rp_detail_left_"] { flex-shrink: 0; width: 440px; display: flex;
            flex-direction: column; align-items: center; margin: 0 auto; }
        div[class*="st-key-rp_detail_text_wrap_"] { flex-grow: 1; min-width: 280px; }
        .rp-detail-card { width: 440px; height: 600px; border-radius: 28px; padding: 14px;
            background: linear-gradient(155deg, #f3d488, #c9a227 45%, #8a6a12 55%, #f3d488);
            box-shadow: 0 22px 45px -20px rgba(139,90,47,0.5); }
        .rp-detail-card-inner { width: 100%; height: 100%; border-radius: 22px; padding: 6px;
            background: linear-gradient(155deg, #fdf0c8, #c9a227); }
        .rp-detail-card-art { width: 100%; height: 100%; border-radius: 18px;
            background: radial-gradient(circle at 30% 22%, #fbead0, transparent 55%),
            linear-gradient(150deg, #f3b56a, #c9683a 55%, #7a3d22);
            display: flex; align-items: center; justify-content: center; }
        .rp-detail-tagline { margin-top: 16px; font-size: 13px; letter-spacing: 0.07em;
            text-transform: uppercase; color: #b8562f !important; font-weight: 800; text-align: center; }
        /* Tombol "Simpan Gambar", dipasang tepat di bawah tagline, lebar
           ngikutin kartu (440px) lewat wadah rp-detail-card-wrap di atasnya. */
        div[class*="st-key-rp_dl_wrap_"] { width: 440px; margin: 10px auto 0 auto; }
        div[class*="st-key-rp_dl_wrap_"] div.stDownloadButton > button {
            border-radius: 100px !important; border: 1.5px solid #ecddc9 !important;
            background: #fdf3e7 !important; color: #b8562f !important;
            font-weight: 700 !important; font-size: 12.5px !important;
        }
        .rp-detail-text { flex-grow: 1; min-width: 280px; display: flex; flex-direction: column; gap: 14px; }
        .rp-detail-chip { display: inline-flex; align-self: flex-start; padding: 6px 16px;
            border-radius: 100px; background: #fdf3e7; border: 1px solid #ecddc9; font-size: 11px;
            font-weight: 800; letter-spacing: 0.04em; color: #b8562f !important; }
        .rp-detail-title { margin: 0; font-size: 25px; font-weight: 700; color: #1c1a17 !important;
            line-height: 1.25; }
        .rp-detail-label { font-size: 11.5px; font-weight: 800; text-transform: uppercase;
            letter-spacing: 0.05em; color: #8a5a2f !important; margin-bottom: 5px; }
        .rp-detail-p { margin: 0; font-size: 13.5px; line-height: 1.75; color: #3a352c !important; }
        .rp-detail-quote { border-left: 4px solid #b8562f; background: #fdf9f2; padding: 12px 18px;
            border-radius: 0 12px 12px 0; }
        .rp-detail-quote p { margin: 0; font-size: 15px; font-style: italic; color: #5c4326 !important;
            line-height: 1.6; font-family: 'Fraunces', serif; }
        .rp-detail-empty { font-size: 13.5px; color: #6b6459 !important; line-height: 1.7;
            font-style: italic; }

        /* Badge kecil buat data tambahan (elemen Shio, modality/planet
           Zodiak, Pancasuda Weton) — ditaruh di bawah PR Kecil, di dalam
           kolom teks yang sama. */
        .rp-supp-badges { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 2px; }
        .rp-supp-badge { display: inline-flex; flex-direction: column; gap: 1px;
            padding: 7px 14px; border-radius: 12px; background: #fdf3e7;
            border: 1px solid #ecddc9; }
        .rp-supp-badge-label { font-size: 9.5px; font-weight: 800; text-transform: uppercase;
            letter-spacing: 0.05em; color: #a8916a !important; }
        .rp-supp-badge-value { font-size: 13px; font-weight: 700; color: #1c1a17 !important; }

        /* Grid angka tambahan (Numerologi lengkap) */
        .rp-supp-stat-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(110px, 1fr));
            gap: 10px; margin-top: 2px; }
        .rp-supp-stat { padding: 10px 12px; border-radius: 12px; background: #fdf9f2;
            border: 1px solid #f0e6d5; text-align: center; }
        .rp-supp-stat-label { font-size: 10px; font-weight: 700; color: #a8916a !important;
            text-transform: uppercase; letter-spacing: 0.04em; }
        .rp-supp-stat-value { font-size: 20px; font-weight: 800; color: #b8562f !important;
            font-family: 'Fraunces', serif; margin-top: 2px; }

        /* Section full-width tambahan buat Matrix Destiny (octagram + chakra) */
        .rp-md-extra { max-width: 900px; margin: 26px auto 0 auto; padding: 26px 28px;
            border-radius: 20px; background: #fffaf2; border: 1.5px solid #f0e6d5; }
        .rp-md-extra-title { font-family: 'Fraunces', serif; font-size: 18px; font-weight: 700;
            color: #1c1a17 !important; margin-bottom: 4px; text-align: center; }
        .rp-md-extra-desc { font-size: 12px; color: #8a7f6d !important; text-align: center;
            margin-bottom: 18px; }
        .rp-md-legend { display: flex; justify-content: center; gap: 20px; margin-top: 10px;
            flex-wrap: wrap; }
        .rp-md-legend-item { display: flex; align-items: center; gap: 6px; font-size: 11.5px;
            color: #6b6459 !important; }
        .rp-md-legend-dot { width: 10px; height: 10px; border-radius: 3px; display: inline-block; }
        .rp-md-stat-row { display: grid; grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
            gap: 10px; margin-top: 20px; }
        .rp-md-stat { padding: 12px 14px; border-radius: 14px; background: #ffffff;
            border: 1px solid #ecddc9; text-align: center; }
        .rp-md-stat-label { font-size: 10px; font-weight: 700; color: #a8916a !important;
            text-transform: uppercase; letter-spacing: 0.04em; }
        .rp-md-stat-value { font-size: 19px; font-weight: 800; color: #1c1a17 !important;
            font-family: 'Fraunces', serif; margin-top: 2px; }
        .rp-md-chakra-title { font-family: 'Fraunces', serif; font-size: 16px; font-weight: 700;
            color: #1c1a17 !important; margin: 24px 0 10px 0; text-align: center; }
        table.rp-md-chakra { width: 100%; border-collapse: collapse; font-size: 12.5px; }
        table.rp-md-chakra th { background: #fdf3e7; color: #8a5a2f !important; font-weight: 800;
            padding: 8px 10px; text-align: center; border-bottom: 2px solid #ecddc9; }
        table.rp-md-chakra td { padding: 8px 10px; text-align: center; border-bottom: 1px solid #f0e6d5;
            color: #3a352c !important; }
        table.rp-md-chakra td:first-child, table.rp-md-chakra th:first-child {
            text-align: left; font-weight: 700; color: #1c1a17 !important; }

        /* Hover zone + tooltip custom di atas tiap titik octagram, biar
           angkanya nggak cuma keliatan tapi langsung kejelasin artinya
           pas mouse lewat (nggak perlu buka expander di bawah). */
        .md-diagram-wrap { position: relative; margin: 0 auto; }
        .md-hz { position: absolute; transform: translate(-50%, -50%);
            display: flex; align-items: center; justify-content: center; cursor: help; z-index: 5; }
        .md-hz .md-tip { visibility: hidden; opacity: 0; position: absolute; bottom: 132%;
            background: #fffaf2; border: 1.5px solid #c9a227; border-radius: 12px;
            padding: 10px 13px; width: 172px; text-align: left; pointer-events: none;
            box-shadow: 0 10px 26px rgba(28,26,23,0.16);
            transition: opacity .15s ease, visibility .15s ease; z-index: 40; }
        .md-hz:hover .md-tip { visibility: visible; opacity: 1; }
        .md-hz.md-align-mid .md-tip { left: 50%; transform: translateX(-50%); }
        .md-hz.md-align-left .md-tip { right: 0; left: auto; }
        .md-hz.md-align-right .md-tip { left: 0; }
        .md-hz.md-center .md-tip { bottom: auto; top: 132%; }
        .md-tip-title { display: block; font-family: 'Fraunces', serif; font-weight: 700;
            font-size: 12px; color: #8a5a2f !important; margin-bottom: 3px; }
        .md-tip-body { display: block; font-family: 'Inter', sans-serif; font-size: 11.5px;
            line-height: 1.45; color: #3a352c !important; }

        /* Baris penjelasan arti tiap angka, di dalam st.expander (dilipat
           default biar halaman nggak kepanjangan). */
        .rp-md-arti-row { display: flex; align-items: baseline; gap: 10px;
            padding: 9px 0; border-bottom: 1px solid #f0e6d5; }
        .rp-md-arti-row:last-child { border-bottom: none; }
        .rp-md-arti-label { flex: 0 0 190px; font-size: 12px; font-weight: 700;
            color: #8a5a2f !important; }
        .rp-md-arti-value { flex: 0 0 28px; font-size: 13px; font-weight: 800;
            color: #b8562f !important; }
        .rp-md-arti-desc { font-size: 12.5px; color: #3a352c !important; }
        .st-key-rp_md_arti_wrap { max-width: 900px; margin: 12px auto 0 auto; }
        .st-key-rp_md_arti_wrap [data-testid="stExpander"] {
            border-radius: 16px !important; border: 1.5px solid #f0e6d5 !important;
            background: #fffaf2 !important;
        }

        /* Kontainer grid amplop: satu baris yang bisa discroll ke samping
           (bukan wrap tiap 5 kolom lagi), supaya siap nampung sampai 15
           amplop nanti tanpa desain berubah. */
        div[class*="st-key-rp_envelope_scroll"] [data-testid="stHorizontalBlock"] {
            flex-wrap: nowrap !important;
            overflow-x: auto !important;
            gap: 16px !important;
            padding: 4px 4px 14px 4px !important;
            scroll-behavior: smooth;
            /* Rata tengah selama amplopnya belum sampai penuh 1 baris (mis.
               baru 5 dari kapasitas 15) — begitu amplop lebih banyak dari
               lebar layar, overflow-x: auto di atas tetap bikin bisa
               discroll, browser otomatis pakai flex-start begitu konten
               melebihi lebar container jadi nggak kepotong di awal. */
            justify-content: center;
        }
        div[class*="st-key-rp_envelope_scroll"] [data-testid="stColumn"] {
            flex: 0 0 168px !important;
            width: 168px !important;
            min-width: 168px !important;
        }

        .rp-cta-hint { text-align: center; font-size: 12.5px; color: #a8916a; margin-top: 18px; }
        .rp-cta-row div.stButton > button {
            border-radius: 100px !important; font-weight: 700 !important; font-size: 13.5px !important;
        }
        .rp-sent-row { display: flex; align-items: center; justify-content: center; gap: 7px;
            margin-top: 6px; font-size: 12px; color: #8a9a8c !important; }

        /* Floating window (st.dialog) di halaman ini — dipaksa terang +
           font kontras jelas, bug CSS dark-mode yang sama kayak sebelumnya
           di dialog "Lengkapi Data" (loadingpage.py). Dialog "Buka Semua
           Amplop?" belum kena fix ini sebelumnya karena style-nya cuma
           diinjeksi lokal per halaman, bukan global. */
        [data-testid="stDialog"],
        [data-testid="stDialog"] > div {
            background-color: #fffaf2 !important;
        }
        [data-testid="stDialog"] * {
            color: #1c1a17 !important;
        }
        [data-testid="stDialog"] button[kind="primary"] * { color: #ffffff !important; }
        </style>
        """,
        unsafe_allow_html=True,
    )


def _render_trophy_row(points):
    total = len(points)
    html = ['<div class="rp-trophy-row">']
    for i, system in enumerate(points):
        html.append(
            '<div class="rp-trophy-unit">'
            '<div class="rp-trophy-dot rp-trophy-dot-done">&#10003;</div>'
            f'<div class="rp-trophy-label">{system}</div></div>'
        )
        if i < total - 1:
            html.append('<div class="rp-trophy-chain"></div>')
    html.append("</div>")
    st.markdown("".join(html), unsafe_allow_html=True)


def _render_closed_envelope(system):
    st.markdown(
        f'<div class="rp-env"><div class="rp-env-flap"></div>'
        f'<div class="rp-env-seal">{_seal_icon(system)}</div>'
        f'<div class="rp-env-foot"><div class="rp-env-name">{system}</div>'
        '<div class="rp-env-hint">Ketuk untuk buka</div></div></div>',
        unsafe_allow_html=True,
    )
    with st.container(key=f"env_btn_wrap_{system}"):
        clicked = st.button(
            "Buka Amplop", key=f"env_open_{system}", use_container_width=True,
        )
    if clicked:
        st.session_state.reveal_opening = system
        st.rerun()


def _render_opened_badge(system, visible):
    st.markdown(
        '<div class="rp-env-done"><div class="rp-env-done-check">&#10003;</div>'
        f'<div class="rp-env-name">{system}</div>'
        '<div class="rp-env-hint">Sudah dibuka</div></div>',
        unsafe_allow_html=True,
    )
    label = "Tutup Amplop" if visible else "Buka Amplop"
    with st.container(key=f"env_btn_wrap_{system}"):
        clicked = st.button(
            label, key=f"env_toggle_{system}", use_container_width=True,
        )
    if clicked:
        if visible:
            st.session_state.reveal_visible.discard(system)
        else:
            st.session_state.reveal_visible.add(system)
        st.rerun()


def _render_burst(system):
    import random

    stars = []
    for i in range(10):
        angle = random.uniform(0, 360)
        dist = random.uniform(60, 110)
        x = round(dist, 1)
        y = round(dist, 1)
        # sebar arah pakai sudut acak lewat translate campuran + delay kecil
        dx = round(dist * random.choice([-1, 1]) * random.uniform(0.4, 1), 1)
        dy = round(-abs(dist) * random.uniform(0.4, 1), 1)
        delay = round(random.uniform(0, 0.15), 2)
        left = round(random.uniform(30, 70), 1)
        top = round(random.uniform(30, 70), 1)
        stars.append(
            f'<div class="rp-burst-star" style="left:{left}%;top:{top}%;'
            f'--rp-x:{dx}px;--rp-y:{dy}px;animation-delay:{delay}s;">&#10022;</div>'
        )
    st.markdown(
        f'<div class="rp-env-burst">{"".join(stars)}'
        '<div style="position:relative;z-index:2;color:#fffaf2;font-family:\'Fraunces\',serif;'
        f'font-weight:700;font-size:13px;">Membuka {system}...</div></div>',
        unsafe_allow_html=True,
    )
    # Sama seperti di loading page: kalau lebih dari satu amplop dibuka
    # berturut-turut di slot grid yang bentuknya identik, DOM-nya bisa
    # dipakai ulang oleh Streamlit sehingga animasi CSS yang sudah pernah
    # jalan tidak otomatis restart. Marker unik per sistem+timestamp
    # memaksa iframe components.html reload tiap kali, jadi animasi
    # bintangnya beneran jalan ulang dari awal setiap amplop yang dibuka.
    col_key = _env_col_key(system)
    components.html(
        f"""
        <script>
        // rp-open-marker:{system}:{time.time()}
        function rpRestartBurst() {{
            try {{
                var doc = window.parent.document;
                var els = doc.querySelectorAll('.rp-burst-star');
                els.forEach(function (el) {{
                    el.style.animation = 'none';
                    void el.offsetWidth;
                    el.style.animation = '';
                }});
                // Selama mode "Buka Semua Amplop", grid amplop bisa discroll
                // ke samping — pastikan amplop yang lagi dianimasikan tetap
                // kelihatan dengan auto-scroll container-nya ke posisi ini.
                var target = doc.querySelector('div[class*="st-key-{col_key}"]');
                if (target) {{
                    target.scrollIntoView({{behavior: 'smooth', inline: 'center', block: 'nearest'}});
                }}
            }} catch (e) {{}}
        }}
        requestAnimationFrame(function () {{ requestAnimationFrame(rpRestartBurst); }});
        </script>
        """,
        height=0,
    )


def _render_supplementary_badges(system, raw_result):
    """
    Badge kecil buat data tambahan yang barusan ditambahkan ke engine
    (elemen Wu Xing Shio, modality+ruling planet Zodiak, Pancasuda Weton,
    4 angka nama Numerologi) — ditaruh di bawah "PR Kecil Buat Kamu".
    Return None kalau sistemnya nggak punya data tambahan (biar caller
    nggak nambah div kosong).
    """
    if not raw_result:
        return None

    if system == "Shio":
        elemen = raw_result.get("elemen")
        if not elemen:
            return None
        return (
            '<div class="rp-supp-badges">'
            '<div class="rp-supp-badge"><span class="rp-supp-badge-label">Elemen Wu Xing</span>'
            f'<span class="rp-supp-badge-value">{elemen}</span></div>'
            '</div>'
        )

    if system == "Zodiak":
        modality = raw_result.get("modality")
        planet = raw_result.get("ruling_planet")
        if not modality and not planet:
            return None
        badges = []
        if modality:
            badges.append(
                '<div class="rp-supp-badge"><span class="rp-supp-badge-label">Modality</span>'
                f'<span class="rp-supp-badge-value">{modality}</span></div>'
            )
        if planet:
            badges.append(
                '<div class="rp-supp-badge"><span class="rp-supp-badge-label">Planet Penguasa</span>'
                f'<span class="rp-supp-badge-value">{planet}</span></div>'
            )
        return '<div class="rp-supp-badges">' + "".join(badges) + '</div>'

    if system == "Weton":
        pancasuda = raw_result.get("pancasuda")
        if not pancasuda:
            return None
        return (
            '<div class="rp-supp-badges">'
            '<div class="rp-supp-badge"><span class="rp-supp-badge-label">Pancasuda</span>'
            f'<span class="rp-supp-badge-value">{pancasuda["nama"]}</span></div>'
            '</div>'
            f'<p class="rp-detail-p" style="margin-top:6px;">{pancasuda["arti"]}</p>'
        )

    if system == "Numerologi":
        keys = ("expression", "soul_urge", "personality", "birthday")
        labels = {
            "expression": "Expression", "soul_urge": "Soul Urge",
            "personality": "Personality", "birthday": "Birthday",
        }
        if not all(k in raw_result for k in keys):
            # Data lama (cuma life_path, belum ada nama) -- jangan
            # nampilin grid kosong.
            return None
        stats = "".join(
            '<div class="rp-supp-stat">'
            f'<div class="rp-supp-stat-label">{labels[k]}</div>'
            f'<div class="rp-supp-stat-value">{raw_result[k]}</div></div>'
            for k in keys
        )
        return (
            '<div><div class="rp-detail-label">Angka Numerologi Lainnya</div>'
            f'<div class="rp-supp-stat-grid">{stats}</div></div>'
        )

    return None


def _render_matrix_destiny_extra(raw_result):
    """
    Section full-width TAMBAHAN buat Matrix Destiny -- octagram (Personal
    Square + Ancestral Square) + Love/Money/Purpose + tabel 7 Chakra.
    Ditaruh di LUAR kolom kartu+teks (rp_detail_outer_) biar dapet lebar
    penuh, soalnya diagram & tabelnya nggak muat kalau dipepetin ke
    setengah kolom.
    """
    if not raw_result or "personal_square" not in raw_result:
        return

    ps = raw_result["personal_square"]
    asq = raw_result["ancestral_square"]
    lm = raw_result["love_money"]
    purpose = raw_result["purpose"]
    chakra = raw_result["chakra"]

    def _arti_singkat(nilai):
        konten = MATRIX_DESTINY_CONTENT.get(nilai)
        if konten:
            return konten["title"]
        return NAMA_ARKETIPE.get(nilai, "-")

    # Label singkat per titik -- dipakai bareng buat tooltip diagram DAN
    # baris "Apa Arti Tiap Angka" di bawah (satu sumber data, dua tampilan).
    _label_titik = {
        "a": "Karakter Luar · Usia 0", "f": "Garis Kakek (Ibu) · Usia 10",
        "b": "Spiritual / Ibu · Usia 20", "g": "Garis Kakek (Ayah) · Usia 30",
        "c": "Material / Ayah · Usia 40", "i": "Garis Nenek (Ayah) · Usia 50",
        "d": "Karmic Tail · Usia 60", "h": "Garis Nenek (Ibu) · Usia 70",
        "e": "Titik Pusat (Inti Jiwa)",
    }
    titik_semua = dict(ps)
    titik_semua.update(asq)
    tooltip_info = {
        kode: {"label": label, "nilai": titik_semua[kode], "arti": _arti_singkat(titik_semua[kode])}
        for kode, label in _label_titik.items()
    }

    svg = render_octagram_svg_with_tooltips(ps, asq, tooltip_info)

    stat_defs = [
        ("Love Point", lm["love"]), ("Money Point", lm["money"]), ("Balance Point", lm["balance"]),
        ("Personal Purpose", purpose["personal"]), ("Social Purpose", purpose["social"]),
        ("Main Destiny", purpose["main_destiny"]),
    ]
    stats_html = "".join(
        f'<div class="rp-md-stat"><div class="rp-md-stat-label">{label}</div>'
        f'<div class="rp-md-stat-value">{value}</div></div>'
        for label, value in stat_defs
    )

    chakra_rows = [
        ("Sahasrara (Mahkota)", "sahasrara"), ("Ajna (Alis)", "ajna"),
        ("Vishuddha (Tenggorokan)", "vishuddha"), ("Anahata (Jantung)", "anahata"),
        ("Manipura (Pusar)", "manipura"), ("Svadhisthana (Sakral)", "svadhisthana"),
        ("Muladhara (Akar)", "muladhara"),
    ]
    chakra_html = "".join(
        f'<tr><td>{label}</td><td>{chakra[key]["physics"]}</td>'
        f'<td>{chakra[key]["energy"]}</td><td>{chakra[key]["emotions"]}</td></tr>'
        for label, key in chakra_rows
    )

    st.markdown(
        '<div class="rp-md-extra">'
        '<div class="rp-md-extra-title">Peta Matrix Destiny Lengkap</div>'
        '<div class="rp-md-extra-desc">Personal Square (garis coklat) &amp; Ancestral Square '
        '(garis emas) — 8 titik di sekeliling usia 0&ndash;70, ketemu di Titik Pusat (Inti Jiwa) '
        'di tengah.</div>'
        f'{svg}'
        '<div class="rp-md-legend">'
        '<div class="rp-md-legend-item"><span class="rp-md-legend-dot" style="background:#b8562f;"></span>'
        'Personal Square (Karakter, Spiritual, Material, Karma)</div>'
        '<div class="rp-md-legend-item"><span class="rp-md-legend-dot" style="background:#c9a227;"></span>'
        'Ancestral Square (Garis Leluhur)</div>'
        '</div>'
        f'<div class="rp-md-stat-row">{stats_html}</div>'
        '<div class="rp-md-chakra-title">Tabel 7 Chakra / Health Card</div>'
        '<table class="rp-md-chakra"><thead><tr>'
        '<th>Chakra</th><th>Physics</th><th>Energy</th><th>Emotions</th>'
        f'</tr></thead><tbody>{chakra_html}</tbody></table>'
        '</div>',
        unsafe_allow_html=True,
    )

    # Penjelasan arti tiap angka -- DILIPAT (st.expander) biar halaman nggak
    # kepanjangan, tapi tetap ada buat yang penasaran kenapa angkanya segitu.
    titik_arti = [
        ("Karakter Luar · Usia 0", ps["a"]),
        ("Garis Kakek (Ibu) · Usia 10", asq["f"]),
        ("Spiritual / Ibu · Usia 20", ps["b"]),
        ("Garis Kakek (Ayah) · Usia 30", asq["g"]),
        ("Material / Ayah · Usia 40", ps["c"]),
        ("Garis Nenek (Ayah) · Usia 50", asq["i"]),
        ("Karmic Tail · Usia 60", ps["d"]),
        ("Garis Nenek (Ibu) · Usia 70", asq["h"]),
        ("Titik Pusat (Inti Jiwa)", ps["e"]),
        ("Love Point", lm["love"]),
        ("Money Point", lm["money"]),
        ("Balance Point", lm["balance"]),
        ("Personal Purpose", purpose["personal"]),
        ("Social Purpose", purpose["social"]),
        ("Main Destiny", purpose["main_destiny"]),
    ]

    arti_rows_html = "".join(
        '<div class="rp-md-arti-row">'
        f'<span class="rp-md-arti-label">{label}</span>'
        f'<span class="rp-md-arti-value">{nilai}</span>'
        f'<span class="rp-md-arti-desc">{_arti_singkat(nilai)}</span>'
        '</div>'
        for label, nilai in titik_arti
    )

    with st.container(key="rp_md_arti_wrap"):
        with st.expander("Apa Arti Tiap Angka di Peta Ini?"):
            st.markdown(arti_rows_html, unsafe_allow_html=True)


def _render_detail(system):
    data = _result_for(system)
    st.markdown(
        '<div class="rp-detail-hint"><div class="rp-detail-hint-line"></div>'
        f'<div class="rp-detail-hint-text">Hasil {system}</div></div>',
        unsafe_allow_html=True,
    )
    if not data:
        st.markdown(
            '<div class="rp-detail">'
            '<div class="rp-detail-text">'
            f'<span class="rp-detail-chip">{system.upper()}</span>'
            f'<h2 class="rp-detail-title rp-serif">{system}</h2>'
            '<p class="rp-detail-empty">Amplop ini sudah terbuka, tapi mesin pembacaannya untuk '
            f'{system} belum selesai dibangun, jadi hasil lengkapnya belum bisa ditampilkan di sini. '
            'Bagian ini akan terisi begitu perhitungannya sudah tersedia.</p>'
            '</div></div>',
            unsafe_allow_html=True,
        )
        return

    raw_result = _raw_result_for(system)
    image_uri = card_image_for_system(system, raw_result)
    image_bytes = card_image_bytes_for_system(system, raw_result)
    if image_uri:
        card_art = (
            f'<img src="{image_uri}" alt="Kartu {system}" '
            'style="width:100%;height:100%;object-fit:cover;border-radius:18px;">'
        )
    else:
        # Fallback ke ikon lama kalau sistem ini belum punya file gambar
        # kartu di assets/cards/ (misal sistem yang belum digarap).
        card_art = _big_icon(system)

    # Dibungkus st.container beneran (bukan satu blok HTML datar) supaya
    # tombol "Simpan Gambar" bisa disisipkan sebagai widget Streamlit asli
    # tepat di bawah kartunya, bukan cuma ikut nempel di HTML mentah.
    with st.container(key=f"rp_detail_outer_{system}"):
        with st.container(key=f"rp_detail_left_{system}"):
            st.markdown(
                '<div class="rp-detail-card"><div class="rp-detail-card-inner">'
                f'<div class="rp-detail-card-art">{card_art}</div>'
                '</div></div>'
                f'<div class="rp-detail-tagline">{data["tagline"]}</div>',
                unsafe_allow_html=True,
            )
            if image_bytes:
                with st.container(key=f"rp_dl_wrap_{system}"):
                    st.download_button(
                        "Simpan Gambar Kartu",
                        data=image_bytes,
                        file_name=card_filename_for_system(system, raw_result),
                        mime="image/png",
                        key=f"dl_card_{system}",
                        icon=":material/download:",
                        use_container_width=True,
                    )
        with st.container(key=f"rp_detail_text_wrap_{system}"):
            supplementary = _render_supplementary_badges(system, raw_result) or ""
            st.markdown(
                '<div class="rp-detail-text">'
                f'<span class="rp-detail-chip">{data["chip"]}</span>'
                f'<h2 class="rp-detail-title rp-serif">{data["title"]}</h2>'
                f'<div><div class="rp-detail-label">{data["p1_label"]}</div>'
                f'<p class="rp-detail-p">{data["p1"]}</p></div>'
                f'<div><div class="rp-detail-label">{data["p2_label"]}</div>'
                f'<p class="rp-detail-p">{data["p2"]}</p></div>'
                f'<div class="rp-detail-quote"><p>&ldquo;{data["quote"]}&rdquo;</p></div>'
                f'<div><div class="rp-detail-label">{data["p3_label"]}</div>'
                f'<p class="rp-detail-p">{data["p3"]}</p></div>'
                f'{supplementary}'
                '</div>',
                unsafe_allow_html=True,
            )

    if system == "Matrix Destiny":
        _render_matrix_destiny_extra(raw_result)


@st.dialog("Buka Semua Amplop?", dismissible=False)
def _confirm_open_all_dialog():
    """
    Floating window konfirmasi SEBELUM proses "Buka Semua Amplop" beneran
    jalan. Sengaja dibikin sebagai @st.dialog kustom (bukan st.warning /
    st.toast bawaan Streamlit) sesuai permintaan, dengan tombol "Iya"/"Tidak"
    sendiri.
    """
    st.markdown(
        '<p style="font-size:13.5px;color:#3a352c;line-height:1.7;margin:2px 0 18px 0;">'
        'Semua amplop yang belum dibuka akan terbuka otomatis satu per satu. '
        'Kalau kamu scroll ke bawah setelah ini, hasil lengkapnya bakal langsung '
        'muncul banyak sekaligus. Yakin mau lanjut?</p>',
        unsafe_allow_html=True,
    )
    yes_col, no_col = st.columns(2)
    with yes_col:
        confirm = st.button(
            "Iya, buka semua", key="btn_confirm_open_all_yes",
            type="primary", use_container_width=True,
        )
    with no_col:
        cancel = st.button(
            "Tidak", key="btn_confirm_open_all_no",
            type="secondary", use_container_width=True,
        )
    if confirm:
        points = _points()
        opened = st.session_state.reveal_opened
        queue = [s for s in points if s not in opened]
        st.session_state.reveal_confirm_open_all = False
        if queue:
            st.session_state.reveal_opening = queue.pop(0)
            st.session_state.reveal_open_all_queue = queue
        st.rerun()
    if cancel:
        st.session_state.reveal_confirm_open_all = False
        st.rerun()


def render():
    _ensure_state()
    _inject_style()

    if st.session_state.reveal_confirm_open_all:
        _confirm_open_all_dialog()

    points = _points()
    if not points:
        st.warning("Belum ada hasil yang bisa ditampilkan. Kembali ke halaman Reveal Yourself dulu ya.")
        if st.button("Kembali ke Reveal Yourself", icon=":material/arrow_back:"):
            st.session_state.dr_page = "reveal"
            st.rerun()
        return

    st.markdown(
        '<div class="rp-header">'
        '<span class="rp-badge">&#10022; Laporan Reveal Kamu Sudah Siap</span>'
        '<h1 class="rp-h1 rp-serif">Semua Rahasia Dirimu, Sudah Terbuka</h1>'
        '<p class="rp-sub">Semua titik sudah selesai dibaca. Buka amplopnya satu per satu untuk '
        'melihat hasil lengkapnya.</p>'
        '</div>',
        unsafe_allow_html=True,
    )

    # Ringkasan data yang diinput user (tanggal lahir), biar dia bisa cek
    # ulang input-nya nggak salah ketik sebelum baca hasil.
    tanggal_lahir = st.session_state.get("loading_data", {}).get("tanggal_lahir")
    tanggal_str = format_tanggal_ddmmyyyy(tanggal_lahir)
    if tanggal_str:
        st.markdown(
            '<div style="text-align:center;margin-top:10px;">'
            f'<span class="rp-input-summary"><span class="material-symbols-outlined" '
            'style="font-size:15px;vertical-align:-2px;">calendar_month</span> '
            f'Tanggal Kamu: <b>{tanggal_str}</b></span>'
            '</div>',
            unsafe_allow_html=True,
        )

    st.write("")
    _render_trophy_row(points)
    st.write("")

    opening = st.session_state.reveal_opening
    opened = st.session_state.reveal_opened

    # ── Tombol "Buka Semua Amplop" — cuma muncul kalau masih ada amplop
    # yang belum dibuka, dan nggak lagi di tengah proses buka-satu/buka-semua.
    # SENGAJA pakai st.empty() sebagai placeholder yang selalu dipanggil
    # tiap render, lalu diisi ATAU di-.empty()-kan secara eksplisit —
    # soalnya kalau blok kondisional ini kadang nulis widget kadang nggak
    # tanpa placeholder yang dikosongkan secara eksplisit, Streamlit nggak
    # otomatis membersihkan widget lama di slot itu (nggak ada "delta"
    # yang dikirim buat run yang kondisinya False), jadi tombolnya
    # keliatan "nyangkut"/nggak ilang meski kondisinya sudah false.
    # Ketauan lewat testing Playwright: tombol ini masih keliatan padahal
    # env lagi di-generate secara berurutan lewat "Buka Semua Amplop". ──
    belum_dibuka = [s for s in points if s not in opened]
    open_all_slot = st.empty()
    if belum_dibuka and not opening and not st.session_state.reveal_open_all_queue:
        with open_all_slot.container():
            oa_l, oa_mid, oa_r = st.columns([1, 1.6, 1])
            with oa_mid:
                if st.button(
                    "Buka Semua Amplop", key="btn_open_all",
                    type="secondary", icon=":material/mark_email_read:", use_container_width=True,
                ):
                    st.session_state.reveal_confirm_open_all = True
                    st.rerun()
            st.write("")
    else:
        open_all_slot.empty()

    # ── Grid amplop: satu baris yang bisa discroll ke samping (bukan wrap
    # per 5 kolom lagi), supaya siap nampung sampai 15 amplop nanti ──
    with st.container(key="rp_envelope_scroll"):
        cols = st.columns(len(points))
        for col, system in zip(cols, points):
            with col:
                with st.container(key=_env_col_key(system)):
                    if system in opened:
                        _render_opened_badge(system, system in st.session_state.reveal_visible)
                    elif opening == system:
                        _render_burst(system)
                    else:
                        _render_closed_envelope(system)

    # Amplop yang lagi dibuka: proses animasinya di sini, SETELAH grid
    # ke-render (biar burst-nya sempat tampil ke user dulu sebelum pindah
    # state), baru pindah ke status "sudah dibuka" dan rerun. Kalau lagi
    # jalan mode "Buka Semua Amplop", begitu satu amplop selesai animasinya,
    # amplop berikutnya di antrean langsung dipop dan mulai dianimasikan di
    # rerun yang sama — jadi berjalan berurutan tanpa perlu klik lagi.
    if opening:
        time.sleep(OPEN_ANIM_SECONDS)
        st.session_state.reveal_opened.add(opening)
        st.session_state.reveal_visible.add(opening)  # otomatis tampil begitu dibuka
        if opening not in st.session_state.reveal_order:
            st.session_state.reveal_order.append(opening)
        queue = st.session_state.reveal_open_all_queue
        if queue:
            st.session_state.reveal_opening = queue.pop(0)
        else:
            st.session_state.reveal_opening = None
        st.rerun()

    # ── Detail hasil yang sudah dibuka DAN lagi ditampilkan (bukan
    # ditutup lewat toggle "Tutup Amplop"), sesuai urutan dibuka ──
    for system in st.session_state.reveal_order:
        if system not in st.session_state.reveal_visible:
            continue
        st.write("")
        _render_detail(system)

    st.write("")
    all_opened = len(opened) == len(points) and not opening

    if all_opened:
        cta_l, cta_mid, cta_r = st.columns([1, 2.4, 1])
        with cta_mid:
            with st.container(key="rp_cta_row"):
                share_col, save_col = st.columns(2)
                with share_col:
                    st.button(
                        "Bagikan ke IG Story", key="btn_share_ig",
                        type="secondary", icon=":material/share:", use_container_width=True,
                    )
                with save_col:
                    st.button(
                        "Simpan Hasil (PDF)", key="btn_save_pdf",
                        type="primary", icon=":material/download:", use_container_width=True,
                    )
            st.markdown(
                '<div class="rp-sent-row">'
                '<svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="#8a9a8c" '
                'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">'
                '<rect x="3" y="5" width="18" height="14" rx="2.5"></rect>'
                '<path d="M3.5 6.5 12 13l8.5-6.5"></path></svg>'
                '<span>Hasil sudah dikirim ke email kamu</span></div>',
                unsafe_allow_html=True,
            )
    else:
        remaining = len(points) - len(opened) - (1 if opening else 0)
        if remaining > 0:
            st.markdown(
                f'<div class="rp-cta-hint">Buka {remaining} amplop lagi untuk menyimpan '
                'hasil lengkapnya.</div>',
                unsafe_allow_html=True,
            )

    st.write("")
    # Reveal Lagi mentok kiri, Kembali ke Home mentok kanan (bukan
    # berdekatan di tengah lagi) — kolom tengah sengaja dikosongkan cuma
    # buat jadi spacer/jarak.
    back_l, _back_spacer, back_r = st.columns([1.4, 2.2, 1.4])
    with back_l:
        if st.button(
            "Reveal Lagi", key="btn_reveal_again",
            type="secondary", icon=":material/refresh:", use_container_width=True,
        ):
            # Reset total buat mulai reveal orang lain dari awal — beda dari
            # "Kembali ke Home" karena langsung balik ke halaman Reveal
            # Yourself, dan ikut ngereset step email/mode-nya juga.
            st.session_state.dr_page = "reveal"
            for k in (
                "loading_points", "loading_idx", "loading_phase", "loading_results",
                "loading_data", "reveal_opened", "reveal_order", "reveal_opening",
                "reveal_visible", "reveal_open_all_queue", "reveal_confirm_open_all",
                "ry_focus_mode", "ry_step1_done", "ry_step3_done", "ry_email",
                # Widget key dialog "Lengkapi Data" (tanggal/jam/kota lahir,
                # golongan darah) — kalau nggak ikut direset, dropdown-nya
                # bakal masih nunjukkin pilihan lama pas user reveal orang
                # lain, padahal loading_data-nya udah kosong.
                "dlg_tgl_bulan", "dlg_tgl_tahun", "dlg_tgl_hari_terakhir",
                "dlg_nama_lengkap", "dlg_jam_lahir", "dlg_kota_lahir", "dlg_golongan_darah",
            ):
                st.session_state.pop(k, None)
            # Key selectbox "Tanggal" dibuat dinamis (dlg_tgl_hari_<bulan>_<tahun>),
            # jadi ikut disapu semua biar nggak ada sisa state kombinasi lama.
            for k in [k for k in st.session_state.keys() if k.startswith("dlg_tgl_hari_")]:
                st.session_state.pop(k, None)
            st.rerun()
    with back_r:
        if st.button(
            "Kembali ke Home", key="btn_back_home_from_result",
            type="secondary", icon=":material/arrow_back:", use_container_width=True,
        ):
            st.session_state.dr_page = "home"
            for k in (
                "loading_points", "loading_idx", "loading_phase", "loading_results",
                "loading_data", "reveal_opened", "reveal_order", "reveal_opening",
                "reveal_visible", "reveal_open_all_queue", "reveal_confirm_open_all",
            ):
                st.session_state.pop(k, None)
            st.rerun()
