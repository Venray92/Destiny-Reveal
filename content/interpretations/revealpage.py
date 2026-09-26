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
  cuma kalau hasil aslinya belum ada di session_state (misalnya lewat tombol
  debug "Test → Reveal/Hasil Page" di app.py yang loncat langsung ke sini
  tanpa melalui alur loading beneran).
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

from content.result_builder import build_display_data
from utils.card_images import (
    card_filename_for_system,
    card_image_bytes_for_system,
    card_image_for_system,
)

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


def _result_for(system):
    """
    Data siap-tampil buat satu sistem: pakai hasil perhitungan ASLI kalau
    ada (dari loading_results, digabung kamus konten lewat
    content/result_builder.py), fallback ke DUMMY_RESULTS kalau belum ada
    hasil asli tersimpan (mis. loncat lewat tombol debug "Test →
    Reveal/Hasil Page").
    """
    raw_result = st.session_state.get("loading_results", {}).get(system)
    data = build_display_data(system, raw_result)
    if data:
        return data
    return _dummy_for(system)


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

        .rp-cta-hint { text-align: center; font-size: 12.5px; color: #a8916a; margin-top: 18px; }
        .rp-cta-row div.stButton > button {
            border-radius: 100px !important; font-weight: 700 !important; font-size: 13.5px !important;
        }
        .rp-sent-row { display: flex; align-items: center; justify-content: center; gap: 7px;
            margin-top: 6px; font-size: 12px; color: #8a9a8c !important; }
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
            }} catch (e) {{}}
        }}
        requestAnimationFrame(function () {{ requestAnimationFrame(rpRestartBurst); }});
        </script>
        """,
        height=0,
    )


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

    image_uri = card_image_for_system(system)
    image_bytes = card_image_bytes_for_system(system)
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
                        file_name=card_filename_for_system(system),
                        mime="image/png",
                        key=f"dl_card_{system}",
                        icon=":material/download:",
                        use_container_width=True,
                    )
        with st.container(key=f"rp_detail_text_wrap_{system}"):
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
                '</div>',
                unsafe_allow_html=True,
            )


def render():
    _ensure_state()
    _inject_style()

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
    st.write("")
    _render_trophy_row(points)
    st.write("")

    opening = st.session_state.reveal_opening
    opened = st.session_state.reveal_opened

    # ── Grid amplop, maksimal 5 kolom per baris ──
    for row_start in range(0, len(points), 5):
        row_points = points[row_start:row_start + 5]
        cols = st.columns(len(row_points))
        for col, system in zip(cols, row_points):
            with col:
                if system in opened:
                    _render_opened_badge(system, system in st.session_state.reveal_visible)
                elif opening == system:
                    _render_burst(system)
                else:
                    _render_closed_envelope(system)

    # Amplop yang lagi dibuka: proses animasinya di sini, SETELAH grid
    # ke-render (biar burst-nya sempat tampil ke user dulu sebelum pindah
    # state), baru pindah ke status "sudah dibuka" dan rerun.
    if opening:
        time.sleep(OPEN_ANIM_SECONDS)
        st.session_state.reveal_opened.add(opening)
        st.session_state.reveal_visible.add(opening)  # otomatis tampil begitu dibuka
        if opening not in st.session_state.reveal_order:
            st.session_state.reveal_order.append(opening)
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
    back_l, back_mid, back_r = st.columns([1.6, 1.6, 1.6])
    with back_mid:
        if st.button(
            "Kembali ke Home", key="btn_back_home_from_result",
            type="secondary", icon=":material/arrow_back:", use_container_width=True,
        ):
            st.session_state.dr_page = "home"
            for k in (
                "loading_points", "loading_idx", "loading_phase", "loading_results",
                "loading_data", "reveal_opened", "reveal_order", "reveal_opening",
                "reveal_visible",
            ):
                st.session_state.pop(k, None)
            st.rerun()
