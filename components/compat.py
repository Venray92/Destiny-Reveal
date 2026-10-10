"""
Soul Match (UI25, Batch 3) — 4 entri terpisah (Asmara, Keluarga, Teman, Partner Bisnis), satu st.dialog:
  [pick, hanya dari entri umum] -> form (data 2 orang + pilih sistem + bayar) -> loading -> result.
State: dh_cp_step | dh_cp_rel_key | dh_cp_n | dh_cp_sys (list) | dh_cp_res. Skor total = rata-rata berbobot per jenis hubungan (WEIGHTS).
Skor dihitung dari engine (Zodiak/Shio/Weton/Numerologi) pakai aturan kecocokan sederhana.
DUMMY: Stardust dipotong di session saja (belum ada backend).
"""

import html
import re
import time
from datetime import date

import streamlit as st
from content import baru_loader as BL
from content import pricing as P

from components import auth
from components import form_kit
from components import close_confirm as cc
from components.dialog_bus import request_with_return
from components.modal_detail import copy_button
from components.solo_reveal import _profile
from content.result_builder import compute_raw_result
from components import result_kit as RK
from utils import trait_cards
from utils.simple_pdf import make_pdf

PRICE = P.COMPAT  # Stardust per sistem
SYSTEMS = ["Zodiak", "Shio", "Weton", "Numerologi"]
_ICON = {"Zodiak": "♈", "Shio": "🐉", "Weton": "🗓️", "Numerologi": "🔢"}
_INFO = [
    ("♈", "Zodiak", "Membaca chemistry & gaya komunikasi lewat elemen rasi bintang."),
    ("🐉", "Shio", "Membaca dinamika karakter & energi berdasarkan tahun kelahiran."),
    ("🗓️", "Weton", "Membaca kecocokan spiritual, rezeki, & garis nasib tradisi Jawa."),
    ("🔢", "Numerologi", "Membaca frekuensi angka takdir & pola hubungan secara logis."),
]
RELATIONS = ["Asmara / Pasangan", "Mitra Bisnis / Rekan Kerja", "Persahabatan", "Keluarga"]
# kunci entri -> (nama relasi, ikon, judul pendek, deskripsi)
REL_KEYS = {
    "asmara": ("Asmara / Pasangan", "💖", "Asmara", "Pasangan atau calon pasangan"),
    "keluarga": ("Keluarga", "🏡", "Keluarga", "Orang tua, saudara, atau anggota keluarga"),
    "teman": ("Persahabatan", "🤝", "Teman", "Sahabat dan lingkar pertemanan"),
    "bisnis": ("Mitra Bisnis / Rekan Kerja", "💼", "Partner Bisnis", "Rekan bisnis atau kolega kerja"),
}
# Bobot sistem per jenis hubungan (jumlah 1.0). Dinormalisasi ulang kalau cuma sebagian sistem dipilih.
# Dasar: Weton = tabel jodoh Jawa (kuat untuk asmara & keluarga); Zodiak = elemen/gaya komunikasi (teman);
# Numerologi = pola keputusan Life Path, Shio = trine/harmoni/bentrok (kerja sama dan relasi tahan lama).
WEIGHTS = {
    "Asmara / Pasangan": {"Zodiak": 0.25, "Shio": 0.25, "Weton": 0.30, "Numerologi": 0.20},
    "Keluarga": {"Zodiak": 0.20, "Shio": 0.25, "Weton": 0.35, "Numerologi": 0.20},
    "Persahabatan": {"Zodiak": 0.35, "Shio": 0.20, "Weton": 0.20, "Numerologi": 0.25},
    "Mitra Bisnis / Rekan Kerja": {"Zodiak": 0.15, "Shio": 0.30, "Weton": 0.20, "Numerologi": 0.35},
}
GENDERS = ["Perempuan", "Laki-laki", "Lainnya / Tidak ingin menyebut"]
LOADING_SEC = 2.2


def _e(t):
    return html.escape(str(t))


# ─────────────── perhitungan skor ───────────────
_ELEM_Z = {("Api", "Api"): 85, ("Air", "Air"): 85, ("Tanah", "Tanah"): 85, ("Udara", "Udara"): 85,
           ("Api", "Udara"): 88, ("Air", "Tanah"): 88, ("Api", "Tanah"): 58, ("Air", "Udara"): 58,
           ("Api", "Air"): 45, ("Tanah", "Udara"): 52}
_TRINE = [{"Tikus", "Naga", "Monyet"}, {"Kerbau", "Ular", "Ayam"}, {"Macan", "Kuda", "Anjing"},
          {"Kelinci", "Kambing", "Babi"}]
_HARMONI = [{"Tikus", "Kerbau"}, {"Macan", "Babi"}, {"Kelinci", "Anjing"}, {"Naga", "Ayam"},
            {"Ular", "Monyet"}, {"Kuda", "Kambing"}]
_SHIO = ["Tikus", "Kerbau", "Macan", "Kelinci", "Naga", "Ular", "Kuda", "Kambing", "Monyet", "Ayam", "Anjing", "Babi"]
# jumlah neptu dua orang mod 8 -> (nama, skor)
_WETON8 = {1: ("Pegat", 38), 2: ("Ratu", 90), 3: ("Jodoh", 88), 4: ("Topo", 74), 5: ("Tinari", 92),
           6: ("Padu", 56), 7: ("Sujanan", 50), 0: ("Pesthi", 95)}
_GRP = {1: 0, 5: 0, 7: 0, 2: 1, 4: 1, 8: 1, 3: 2, 6: 2, 9: 2, 11: 1, 22: 1, 33: 2}


_REL_KEY = {"Asmara / Pasangan": "asmara", "Keluarga": "keluarga", "Persahabatan": "teman", "Mitra Bisnis / Rekan Kerja": "bisnis"}


def _skenario(s, a, b, sc):
    """Id skenario (untuk teks konteks per relasi), sama dengan kunci di compat/konteks.json."""
    if s == "Zodiak":
        return "selaras" if sc >= 80 else "beda_ritme" if sc < 60 else None
    if s == "Shio":
        x, y = a["shio"], b["shio"]
        if x == y:
            return "sama"
        if any({x, y} <= t for t in _TRINE):
            return "trine"
        if any({x, y} == h for h in _HARMONI):
            return "harmoni"
        return "bentrok" if (_SHIO.index(x) - _SHIO.index(y)) % 12 == 6 else "netral"
    if s == "Weton":
        return _WETON8[(a["neptu"] + b["neptu"]) % 8][0].lower()
    la, lb = a["life_path"], b["life_path"]
    return "sama" if la == lb else "satu_kelompok" if _GRP[la] == _GRP[lb] else "beda_kelompok"


def _score_zodiak(a, b):
    ea, eb = a["element"], b["element"]
    sc = _ELEM_Z.get((ea, eb)) or _ELEM_Z.get((eb, ea)) or 60
    note = f"{a['sign']} ({ea}) & {b['sign']} ({eb})"
    if sc >= 80:
        return sc, note, (f"Elemen {ea} dan {eb} kalian saling menguatkan, jadi energi terasa nyambung sejak awal. "
                          "Kalian cenderung cepat paham maksud satu sama lain tanpa perlu banyak penjelasan, "
                          "dan itu bikin suasana bareng terasa ringan serta minim drama.", None)
    if sc >= 60:
        return sc, note, (f"Elemen {ea} dan {eb} punya titik temu asalkan sama-sama mau menyesuaikan tempo. "
                          "Saat salah satu mau mengalah di waktu yang tepat, kalian bisa saling melengkapi dengan cara yang tidak dimiliki pasangan lain.",
                          "Gaya bereaksi kalian berbeda, jadi rawan salah tangkap ketika emosi sedang naik. "
                          "Hal kecil bisa terdengar seperti kritik, padahal niatnya cuma menyampaikan pendapat. "
                          "Biasakan konfirmasi dulu maksud lawan bicara sebelum menyimpulkan.")
    return sc, note, (None, f"Elemen {ea} dan {eb} cenderung beda ritme: yang satu bergerak cepat, yang lain butuh waktu mencerna. "
                      "Tanpa kesadaran ini, satu pihak bisa merasa ditinggal dan pihak lain merasa didesak. "
                      "Kuncinya adalah menyepakati tempo bersama, bukan memaksa satu cara jadi patokan.")


def _score_shio(a, b):
    x, y = a["shio"], b["shio"]
    note = f"{x} & {y}"
    if x == y:
        return 70, note, (f"Sama-sama shio {x}, kalian punya kebiasaan dan cara pandang yang mirip. "
                          "Kamu hampir tidak perlu menjelaskan panjang lebar karena lawan bicaramu sudah paham pola pikirnya.",
                          "Kelemahan yang sama bisa saling menguatkan. Kalau sama-sama gampang menunda atau sama-sama keras kepala, "
                          "tidak ada yang jadi penyeimbang. Libatkan pihak ketiga atau aturan tertulis untuk hal-hal penting.")
    if any({x, y} <= t for t in _TRINE):
        return 90, note, (f"{x} dan {y} berada dalam satu 'trine' shio, kelompok yang secara tradisi dianggap paling seirama. "
                          "Nilai, tujuan hidup, dan cara mengambil keputusan kalian gampang sejalan, "
                          "jadi rencana jangka panjang terasa lebih mudah disusun bersama.", None)
    if any({x, y} == h for h in _HARMONI):
        return 85, note, (f"{x} dan {y} termasuk pasangan harmoni shio yang saling melengkapi dan menenangkan. "
                          "Saat salah satu sedang kewalahan, yang lain biasanya hadir dengan sikap yang pas tanpa diminta. "
                          "Pola ini membuat hubungan terasa aman dan saling menopang.", None)
    if (_SHIO.index(x) - _SHIO.index(y)) % 12 == 6:
        return 40, note, (None, f"{x} dan {y} berseberangan (bentrok) dalam hitungan shio, sehingga gesekan mudah muncul kalau ego sedang naik. "
                          "Perbedaan sudut pandang bisa terasa seperti penolakan pribadi. "
                          "Atur jeda sebelum membalas saat panas, dan fokuskan diskusi pada masalah, bukan pada orangnya.")
    return 62, note, (f"Tidak ada bentrok khusus antara {x} dan {y}, jadi hubungan bisa dibentuk lewat usaha bersama. "
                      "Tidak ada keselarasan otomatis, tapi juga tidak ada penghalang bawaan. "
                      "Kualitas hubungan akan sangat ditentukan oleh kebiasaan kalian sehari-hari.", None)


def _score_weton(a, b):
    tot = a["neptu"] + b["neptu"]
    nama, sc = _WETON8[tot % 8]
    note = f"{a['hari']} {a['pasaran']} + {b['hari']} {b['pasaran']} (neptu {tot}) = {nama}"
    if sc >= 80:
        return sc, note, (f"Hitungan neptu kalian jatuh di '{nama}', tergolong sangat baik dalam tradisi Jawa. "
                          "Artinya ritme rezeki, kecocokan batin, dan keharmonisan sehari-hari cenderung mendukung. "
                          "Tetap rawat dengan kebiasaan baik supaya potensi ini terwujud nyata.", None)
    if sc >= 60:
        return sc, note, (f"Neptu '{nama}' tergolong cukup stabil dan punya dasar yang bisa diandalkan. "
                          "Hubungan ini tumbuh paling baik ketika kalian rutin menjaga komunikasi dan saling terbuka soal kebutuhan masing-masing.",
                          "Kestabilan ini bukan jaminan, karena mudah goyah kalau komunikasi mulai jarang. "
                          "Jangan menunggu masalah membesar sebelum membicarakannya.")
    return sc, note, (None, f"Neptu kalian jatuh di '{nama}', yang dalam hitungan Jawa butuh kesabaran ekstra dan kesepakatan yang jelas. "
                      "Pola ini sering muncul sebagai salah paham berulang atau tarik-ulur soal hal yang sama. "
                      "Tuliskan kesepakatan penting, dan evaluasi bersama secara berkala agar tidak jadi beban terpendam.")


def _score_num(a, b):
    la, lb = a["life_path"], b["life_path"]
    note = f"Life Path {la} & {lb}"
    if la == lb:
        return 78, note, (f"Life Path kalian sama-sama {la}, jadi kalian memahami ritme dan motivasi satu sama lain. "
                          "Kamu bisa melihat dirimu sendiri di pasanganmu, dan itu menumbuhkan rasa dimengerti yang jarang didapat dari orang lain.",
                          "Sifat yang sama bisa berbenturan saat sama-sama keras atau sama-sama defensif. "
                          "Kelemahan yang sama juga tidak punya penyeimbang. Libatkan masukan dari luar untuk keputusan penting.")
    if _GRP[la] == _GRP[lb]:
        return 88, note, (f"Life Path {la} dan {lb} berada dalam satu kelompok energi, sehingga visi dan gaya kerja saling mendukung. "
                          "Arah yang kalian tuju cenderung searah, dan perbedaan kecil di antara kalian justru terasa saling melengkapi.", None)
    return 62, note, (f"Life Path {la} dan {lb} berasal dari kelompok energi berbeda, yang bisa saling mengisi kalau kalian saling terbuka. "
                      "Kalian punya sudut pandang yang tidak dimiliki satu sama lain, sehingga sangat berguna sebagai pelengkap.",
                      "Cara mengambil keputusan kalian berbeda arah, jadi rawan beda prioritas. "
                      "Sepakati dulu kriteria keputusan bersama sebelum membahas pilihan, supaya diskusi tidak jadi adu cara.")


_SCORERS = {"Zodiak": _score_zodiak, "Shio": _score_shio, "Weton": _score_weton, "Numerologi": _score_num}

_ADVICE = {
    "Asmara / Pasangan": [
        "Bikin ritual komunikasi mingguan: 20 menit ngobrol tanpa gawai soal harapan dan keresahan masing-masing. "
        "Ritual yang konsisten mencegah masalah kecil menumpuk jadi ledakan di kemudian hari.",
        "Rayakan hal kecil dan sebutkan apresiasi secara langsung, jangan menunggu momen besar. "
        "Ucapan sederhana seperti terima kasih atau aku bangga sama kamu sering lebih berpengaruh daripada hadiah mahal.",
        "Saat konflik, sepakati aturan main dulu: tidak saling memotong dan tidak mengungkit masa lalu. "
        "Kalau suasana sudah panas, ambil jeda 20 menit lalu lanjutkan dengan kepala dingin.",
        "Bicarakan visi jangka panjang secara berkala, mulai dari keuangan, tempat tinggal, sampai urusan keluarga. "
        "Selaras di hal besar membuat perbedaan kecil jadi lebih gampang diterima.",
        "Sisihkan waktu berdua yang berkualitas, bukan sekadar berada di ruangan yang sama. "
        "Aktivitas baru bersama bisa menyegarkan hubungan dan menambah cerita yang hanya kalian berdua miliki.",
    ],
    "Mitra Bisnis / Rekan Kerja": [
        "Tulis pembagian peran, wewenang, dan target secara tertulis sebelum proyek berjalan. "
        "Kesepakatan tertulis mengurangi debat soal siapa yang bertanggung jawab ketika ada masalah.",
        "Pisahkan urusan pribadi dan keuangan bisnis; evaluasi berkala tiap bulan dengan data, bukan perasaan. "
        "Angka yang jelas membuat diskusi sulit jadi lebih objektif.",
        "Manfaatkan perbedaan gaya: satu fokus eksekusi, satu fokus strategi dan hubungan klien. "
        "Pembagian sesuai kekuatan masing-masing menghemat energi dan mempercepat hasil.",
        "Tetapkan mekanisme pengambilan keputusan sejak awal, termasuk apa yang dilakukan kalau pendapat kalian buntu. "
        "Tanpa aturan ini, keputusan penting bisa tertunda dan menimbulkan frustrasi.",
        "Sampaikan masukan secara langsung dan spesifik, lalu tutup dengan solusi, bukan sekadar keluhan. "
        "Budaya feedback yang sehat menjaga kerja sama tetap awet saat bisnis bertumbuh.",
    ],
    "Persahabatan": [
        "Jadwalkan waktu bertemu yang rutin supaya hubungan tidak hanya hidup saat butuh. "
        "Pertemanan yang dirawat kecil-kecil tapi konsisten biasanya lebih tahan lama.",
        "Jujur secara halus saat ada yang mengganjal; jangan menyimpan sampai meledak. "
        "Sampaikan dengan kalimat aku merasa, bukan kamu selalu, supaya lawan bicara tidak langsung defensif.",
        "Hargai batas masing-masing, termasuk waktu sendiri dan lingkaran pertemanan lain. "
        "Memberi ruang justru membuat hubungan terasa aman dan tidak menekan.",
        "Hadir di momen penting satu sama lain, baik saat senang maupun susah. "
        "Kehadiran nyata di waktu yang tepat sering jadi ingatan paling kuat dalam sebuah persahabatan.",
        "Kalau ada selisih paham, selesaikan langsung berdua sebelum cerita ke orang lain. "
        "Cara ini menjaga kepercayaan dan mencegah masalah kecil berubah jadi gosip.",
    ],
    "Keluarga": [
        "Dengarkan dulu sebelum menanggapi; banyak gesekan keluarga muncul dari asumsi, bukan niat buruk. "
        "Ulangi dengan kata-katamu sendiri apa yang kamu tangkap, lalu tanya apakah itu benar.",
        "Tentukan topik sensitif yang dibahas di waktu tenang, bukan saat acara kumpul. "
        "Suasana santai dan privat membuat percakapan berat lebih mudah diterima.",
        "Tunjukkan peduli lewat tindakan kecil yang konsisten, bukan hanya kata-kata. "
        "Telepon singkat, makan bersama, atau bantuan kecil sering lebih bermakna daripada nasihat panjang.",
        "Hormati perbedaan generasi dan cara pandang tanpa merasa harus saling menyamakan. "
        "Cukup pahami latar belakang masing-masing dan cari titik tengah yang bisa diterima semua pihak.",
        "Bagi tanggung jawab keluarga secara adil dan terbuka, termasuk soal waktu, tenaga, dan biaya. "
        "Kejelasan di awal mencegah rasa tidak adil yang menumpuk diam-diam.",
    ],
}
_KUAT_CTX = {
    "Asmara / Pasangan": "Dalam konteks asmara, kekuatan di atas paling terasa saat kalian sama-sama merasa aman untuk jujur. Rawat kebiasaan kecil yang membuat kalian merasa dipilih setiap hari.",
    "Mitra Bisnis / Rekan Kerja": "Dalam konteks kerja sama, kekuatan di atas bisa jadi modal besar untuk pembagian peran yang efisien. Manfaatkan sebagai fondasi kepercayaan di setiap keputusan penting.",
    "Persahabatan": "Dalam konteks persahabatan, kekuatan di atas membuat kalian nyaman jadi diri sendiri tanpa perlu berpura-pura. Itu aset langka yang layak dijaga.",
    "Keluarga": "Dalam konteks keluarga, kekuatan di atas membantu kalian saling memahami lintas peran dan generasi. Gunakan sebagai jembatan saat ada perbedaan pendapat.",
}
_TANTANG_CTX = {
    "Asmara / Pasangan": "Dalam konteks asmara, tantangan di atas biasanya muncul sebagai salah paham yang berulang. Sadari polanya lebih awal supaya tidak berubah jadi jarak emosional.",
    "Mitra Bisnis / Rekan Kerja": "Dalam konteks kerja sama, tantangan di atas bisa berdampak ke keputusan dan keuangan bila dibiarkan. Atur aturan main dan evaluasi berkala sejak awal.",
    "Persahabatan": "Dalam konteks persahabatan, tantangan di atas biasanya terasa saat salah satu pihak menyimpan unek-unek. Bicarakan lebih cepat sebelum jadi jarak.",
    "Keluarga": "Dalam konteks keluarga, tantangan di atas sering terselip di momen kumpul yang emosional. Pilih waktu dan cara bicara yang tenang agar tidak jadi luka lama.",
}
_CTX = {"Asmara / Pasangan": "sebagai pasangan", "Mitra Bisnis / Rekan Kerja": "sebagai rekan kerja",
        "Persahabatan": "sebagai sahabat", "Keluarga": "sebagai keluarga"}


def _label(score):
    if score >= 85:
        return "Sangat Selaras"
    if score >= 70:
        return "Cukup Selaras"
    if score >= 55:
        return "Perlu Usaha"
    return "Banyak Tantangan"


def _compute(systems, pa, pb, rel):
    """Return dict hasil, atau None kalau data salah satu orang di luar jangkauan engine."""
    rows, kuat, tantang = [], [], []
    for s in systems:
        ra = compute_raw_result(s, {"tanggal_lahir": pa["tgl"], "nama_lengkap": pa["nama"]})
        rb = compute_raw_result(s, {"tanggal_lahir": pb["tgl"], "nama_lengkap": pb["nama"]})
        if ra.get("placeholder") or rb.get("placeholder"):
            return None
        sc, note, (k, t) = _SCORERS[s](ra, rb)
        ctx = BL.compat_konteks(s, _skenario(s, ra, rb, sc) or "", _REL_KEY[rel])  # konteks per jenis hubungan (Gemini)
        if ctx:
            p1, _, p2 = ctx.partition(". ")
            if k and t:
                k, t = f"{k} {p1.rstrip('.')}.", f"{t} {p2 or p1}"
            elif k:
                k = f"{k} {ctx}"
            elif t:
                t = f"{t} {ctx}"
        rows.append({"system": s, "score": sc, "note": note})  # bobot diisi setelah semua sistem terkumpul
        if k:
            kuat.append(f"{_ICON[s]} {s}: {k}")
        if t:
            tantang.append(f"{_ICON[s]} {s}: {t}")
    wsum = sum(WEIGHTS[rel][r["system"]] for r in rows)
    for r in rows:
        r["w"] = round(WEIGHTS[rel][r["system"]] / wsum * 100)
    total = round(sum(r["score"] * WEIGHTS[rel][r["system"]] for r in rows) / wsum)
    if not kuat:
        kuat.append("Perbedaan kalian bisa jadi bahan belajar dan saling melengkapi kalau dikelola dengan baik. "
                    "Titik kuat hubungan ini bukan datang dari kemiripan otomatis, tapi dari kemauan kalian memahami cara pandang satu sama lain.")
    if not tantang:
        tantang.append("Tidak ada tantangan besar dari sistem yang dipilih, tapi waspadai rasa terlalu nyaman yang bikin lupa merawat hubungan. "
                       "Hubungan yang terlihat mulus tetap butuh percakapan jujur dan usaha rutin supaya tidak jadi datar.")
    ctx = _CTX[rel]
    ringkas = (f"{pa['nama']} & {pb['nama']} {ctx} berada di level “{_label(total)}” ({total}/100) "
               f"berdasarkan {len(rows)} sistem: {', '.join(systems)}.")
    kuat.append(_KUAT_CTX[rel])
    tantang.append(_TANTANG_CTX[rel])
    nasihat = list(_ADVICE[rel])
    if total < 60:
        nasihat.insert(0, "Skor ini bukan vonis. Anggap sebagai peta area yang perlu dijaga lebih sadar. "
                          "Banyak hubungan dengan skor rendah tetap berjalan baik karena kedua pihak tahu persis di mana titik rawannya.")
    return {"total": total, "label": _label(total), "rows": rows, "kuat": kuat, "tantang": tantang,
            "nasihat": nasihat, "ringkas": ringkas, "rel": rel, "a": pa["nama"], "b": pb["nama"], "systems": list(systems)}


# ─────────────── callbacks ───────────────
def _go(step):
    st.session_state.dh_cp_step = step


def _rel_name():
    k = st.session_state.get("dh_cp_rel_key")
    return REL_KEYS[k][0] if k in REL_KEYS else None


def _cb_count(n):
    ss = st.session_state
    ss.dh_cp_n = n
    cur = ss.get("dh_cp_sys", [])
    ss.dh_cp_sys = cur[-n:] if len(cur) > n else cur  # kelebihan -> buang yang paling awal
    ss.dh_cp_err = None


def _cb_toggle(name):
    ss = st.session_state
    cur = list(ss.get("dh_cp_sys", []))
    n = ss.get("dh_cp_n", 2)
    if name in cur:
        cur.remove(name)
    else:
        cur.append(name)
        if len(cur) > n:
            cur = cur[-n:]
    ss.dh_cp_sys = cur
    ss.dh_cp_err = None


def _cb_pick_rel(key):
    st.session_state.dh_cp_rel_key = key
    st.session_state.dh_cp_err = None
    _go("form")


def _cb_change_rel():
    st.session_state.dh_cp_rel_key = None
    _go("pick")


def _person(side):
    ss = st.session_state
    return {"nama": (ss.get(f"dhcp_{side}_nama") or "").strip(), "tgl": ss.get(f"dhcp_{side}_tgl"),
            "gender": ss.get(f"dhcp_{side}_gender")}


def _cb_go():
    ss = st.session_state
    u = auth.current_user()
    systems = ss.get("dh_cp_sys", [])
    n = ss.get("dh_cp_n", 2)
    cost = PRICE * len(systems)
    pa, pb = _person("a"), _person("b")
    rel = _rel_name()
    for lab, p in (("Pihak Pertama", pa), ("Pihak Kedua", pb)):
        if not p["nama"] or not p["tgl"]:
            ss.dh_cp_err = f"Nama dan Tanggal Lahir {lab} wajib diisi."
            return
    if len(systems) != n:
        ss.dh_cp_err = f"Pilih tepat {n} sistem dulu ya."
        return
    if not u:
        ss.dh_cp_err = "Masuk akun dulu supaya saldo ✨ bisa dipakai."
        return
    if u.get("koin", 0) < cost:
        ss.dh_cp_err = f"Saldo belum cukup, kurang {cost - u['koin']} ✨."
        return
    res = _compute(systems, pa, pb, rel)
    if not res:
        ss.dh_cp_err = "Tanggal lahir salah satu pihak di luar jangkauan data sistem (mis. Shio 1945-2020). Saldo tidak dipotong."
        return
    u["koin"] -= cost
    res["cost"] = cost
    ss.dh_cp_res = res
    ss.dh_cp_err = None
    _go("loading")


def _cb_reset():
    """Bersihkan form & hasil; jenis hubungan tetap (kembali ke form kalau sudah dipilih)."""
    ss = st.session_state
    for k in ("dh_cp_res", "dh_cp_sys", "dh_cp_n", "dh_cp_err", *_FORM_KEYS, *("_sv_" + k for k in _FORM_KEYS)):
        ss.pop(k, None)
    _go("form" if ss.get("dh_cp_rel_key") in REL_KEYS else "pick")


# ─────────────── tampilan ───────────────
def _head(sub):
    key = st.session_state.get("dh_cp_rel_key")
    ico, ttl = (REL_KEYS[key][1], f"Soul Match · {REL_KEYS[key][2]}") if key in REL_KEYS else ("💖", "Soul Match")
    st.markdown('<div class="dh-step dh-step-cp"></div>'
                f'<div class="dh-cp-head"><span class="dh-cp-ico">{ico}</span><div><div class="dh-cp-brand">{_e(ttl)}</div>'
                f'<div class="dh-cp-hsub">{sub}</div></div></div><div class="dh-cp-line"></div>', unsafe_allow_html=True)


def _stepper(n):
    labels = ["Data & Sistem", "Hasil"]
    st.markdown('<div class="dh-cp-steps">' + "".join(
        f'<span class="{"on" if i == n else ("done" if i < n else "")}"><b>{i + 1}</b>{_e(t)}</span>'
        for i, t in enumerate(labels)) + '</div>', unsafe_allow_html=True)


def _err():
    if st.session_state.get("dh_cp_err"):
        st.error(st.session_state.dh_cp_err)


def _render_pick():
    """Dibuka lewat entri umum (menu/footer): pilih jenis hubungan dulu."""
    _head("Pilih jenis hubungan yang mau dicek")
    with st.container(key="dhcp_pick"):
        for key, (_nm, ico, ttl, desc) in REL_KEYS.items():
            st.button(f"{ico}  **{ttl}**  \n{desc}", key=f"dhcp_pk_{key}", on_click=_cb_pick_rel, args=(key,),
                      use_container_width=True)


def _systems_picker():
    ss = st.session_state
    n = ss.setdefault("dh_cp_n", 2)
    sel = ss.setdefault("dh_cp_sys", [])
    w = WEIGHTS[_rel_name()]
    st.markdown('<div class="dh-cp-lab">Mau pakai berapa sistem?</div>', unsafe_allow_html=True)
    with st.container(key="dhcp_cnt"):
        cols = st.columns(4, gap="small")
        for i, col in enumerate(cols, 1):
            with col:
                st.button(f"{i} Sistem  \n**{PRICE * i} ✨**", key=f"dhcp_n{i}", on_click=_cb_count, args=(i,),
                          type="primary" if n == i else "secondary", use_container_width=True)
    lc, ic, _sp, cc = st.columns([2.1, 0.8, 2.6, 2.2], gap="small", vertical_alignment="center")
    with lc:
        st.markdown(f'<div class="dh-cp-lab" style="margin:0">Pilih {n} Sistem</div>', unsafe_allow_html=True)
    with ic:
        with st.container(key="dhcp_info"):
            with st.popover("ⓘ", help=None):
                st.markdown('<div class="dh-cp-pop"><b>Beda ke-4 sistem</b>' + "".join(
                    f'<div><span>{i}</span><p><b>{_e(n_)}:</b> {_e(d)}</p></div>' for i, n_, d in _INFO) + '</div>',
                    unsafe_allow_html=True)
    with cc:
        st.markdown(f'<div class="dh-cp-cnt" style="text-align:center">{len(sel)}/{n} terpilih</div>', unsafe_allow_html=True)
    with st.container(key="dhcp_sys"):
        for r in range(0, len(SYSTEMS), 2):
            cols = st.columns(2, gap="small")
            for col, name in zip(cols, SYSTEMS[r:r + 2]):
                with col:
                    st.button(f"{_ICON[name]}  **{name}** · bobot {round(w[name] * 100)}%", key=f"dhcp_s_{name}",
                              on_click=_cb_toggle, args=(name,), type="primary" if name in sel else "secondary",
                              use_container_width=True)
    st.markdown('<div class="dh-cp-hint">Bobot menunjukkan seberapa besar tiap sistem menentukan skor untuk jenis hubungan ini.</div>',
                unsafe_allow_html=True)


def _side(side, title):
    with st.container(key=f"dhcp_card_{side}"):
        st.markdown(f'<div class="dh-cp-side">{title}</div>', unsafe_allow_html=True)
        st.text_input("Nama Lengkap", placeholder="Contoh: Rina Anggraini", key=f"dhcp_{side}_nama")
        st.date_input("Tanggal Lahir", value=None, min_value=date(1900, 1, 1), max_value=date.today(),
                      format="DD/MM/YYYY", key=f"dhcp_{side}_tgl")
        st.time_input("Jam Lahir (Opsional)", value=None, key=f"dhcp_{side}_jam")
        st.text_input("Tempat Lahir (Opsional)", placeholder="Contoh: Jakarta", key=f"dhcp_{side}_kota")
        st.selectbox("Jenis Kelamin (Opsional)", GENDERS, index=None, placeholder="Pilih", key=f"dhcp_{side}_gender")


_FORM_KEYS = [f"dhcp_{x}_{f}" for x in "ab" for f in ("nama", "tgl", "jam", "kota", "gender")]


def _restore():
    """Widget yang tidak tampil (mis. pindah ke modal login/top-up) kehilangan isinya -> pulihkan dari salinan."""
    ss = st.session_state
    for k in _FORM_KEYS:
        if k not in ss and ("_sv_" + k) in ss:
            ss[k] = ss["_sv_" + k]


def _save():
    ss = st.session_state
    for k in _FORM_KEYS:
        if k in ss:
            ss["_sv_" + k] = ss[k]


def _render_form():
    ss = st.session_state
    _restore()
    u = auth.current_user()
    rel_key = ss.get("dh_cp_rel_key")
    systems = ss.get("dh_cp_sys", [])
    cost = PRICE * len(systems)
    _head(f"{REL_KEYS[rel_key][3]} · isi data kedua belah pihak")
    _stepper(0)
    st.markdown('<div class="dh-modal-section"><span>📅 DATA KALIAN</span><em>Wajib</em></div>', unsafe_allow_html=True)
    form_kit.data_bar("dhcp_a", f"compat_{rel_key}")
    c1, c2 = st.columns(2, gap="medium")
    with c1:
        _side("a", "Pihak Pertama (Kamu)")
    with c2:
        _side("b", "Pihak Kedua")
    _systems_picker()
    _save()
    if not u:
        st.markdown('<div class="dh-cp-note">🔒 Kamu perlu masuk akun untuk membayar dengan ✨.</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="dh-cp-note ok">Saldo: <b>{u["koin"]} ✨</b> · Biaya: <b>{cost} ✨</b></div>', unsafe_allow_html=True)
    _err()
    b1, b2 = st.columns([1, 2.2], gap="small")
    with b1:
        with st.container(key="dhcp_back"):
            st.button("Ganti Jenis", key="dhcp_b_back", on_click=_cb_change_rel, use_container_width=True)
    with b2:
        with st.container(key="dhcp_cta"):
            if not u:
                if st.button("Masuk / Daftar untuk Bayar →", key="dhcp_login", type="primary", use_container_width=True):
                    request_with_return("auth", f"compat_{rel_key}")
            elif u["koin"] < cost:
                if st.button("Top-up Saldo →", key="dhcp_topup", type="primary", use_container_width=True):
                    request_with_return("pricing_keep", f"compat_{rel_key}", dh_pr_tab="koin")
            else:
                st.button(f"Hitung Sinergi {REL_KEYS[rel_key][2]} ({cost} ✨)", key="dhcp_go", type="primary",
                          use_container_width=True, on_click=_cb_go)


def _render_loading():
    st.markdown('<div class="dh-step dh-step-cp"></div><div class="dh-nodismiss"></div>'
                '<div class="dh-cp-load"><div class="dh-cp-orb"><i></i><i></i><span>💖</span></div>'
                '<div class="dh-cp-lt">Menghitung energi sinergi &amp; kecocokan profil...</div>'
                '<div class="dh-cp-ls">Menyelaraskan sistem pilihanmu</div></div>', unsafe_allow_html=True)
    time.sleep(LOADING_SEC)
    _go("result")
    st.rerun(scope="fragment")


def _plain(r):
    out = [f"CEK KECOCOKAN: {r['a']} & {r['b']}", r["ringkas"], "", f"SKOR: {r['total']}/100 ({r['label']})", ""]
    out += [f"- {x['system']}: {x['score']} ({x['note']})" for x in r["rows"]]
    out += ["", "KEKUATAN", *r["kuat"], "", "TANTANGAN", *r["tantang"], "", "NASIHAT STRATEGIS", *r["nasihat"]]
    return "\n".join(out)


def _render_result():
    ss = st.session_state
    r = ss.get("dh_cp_res")
    if not r:
        _cb_reset()
        return _render_form() if ss.get("dh_cp_step") == "form" else _render_pick()
    _head("Hasil analisis kecocokan")
    st.markdown('<div class="dh-nodismiss"></div>', unsafe_allow_html=True)
    ang = round(r["total"] * 3.6)
    st.markdown(
        '<div class="dh-cp-banner">'
        f'<div class="dh-cp-ring" style="background:conic-gradient(#C85A32 {ang}deg,#F3E4D3 0)"><div><b>{r["total"]}</b><span>/100</span></div></div>'
        f'<div class="dh-cp-bt"><div class="dh-cp-eyebrow">SKOR SINERGI · {_e(r["rel"].upper())}</div>'
        f'<div class="dh-cp-names">{_e(r["a"])} &amp; {_e(r["b"])}</div>'
        f'<div class="dh-cp-lab2">{_e(r["label"])}</div></div></div>'
        f'<div class="dh-cp-card"><div class="dh-cp-ct">📖 Ringkasan</div><p>{_e(r["ringkas"])}</p></div>', unsafe_allow_html=True)
    rows = "".join(
        f'<div class="dh-cp-row"><div class="dh-cp-rh"><span>{_ICON[x["system"]]} {_e(x["system"])} <small>· bobot {x["w"]}%</small></span><b>{x["score"]}</b></div>'
        f'<div class="dh-cp-bar"><i style="width:{x["score"]}%"></i></div><div class="dh-cp-rn">{_e(x["note"])}</div></div>'
        for x in r["rows"])
    st.markdown(f'<div class="dh-cp-card"><div class="dh-cp-ct">📊 Skor Per Sistem</div>{rows}</div>', unsafe_allow_html=True)
    for ico, ttl, items in (("💪", "Poin Kekuatan Hubungan", r["kuat"]), ("⚠️", "Poin Tantangan", r["tantang"]),
                            ("⚖️", "Nasihat Strategis", r["nasihat"])):
        st.markdown(f'<div class="dh-cp-card"><div class="dh-cp-ct">{ico} {ttl}</div>'
                    + "".join(f"<p>{_e(t)}</p>" for t in items) + '</div>', unsafe_allow_html=True)
    secs = [("Ringkasan", [r["ringkas"]]), ("Skor Per Sistem", [f"{x['system']}: {x['score']} - {x['note']}" for x in r["rows"]]),
            ("Poin Kekuatan", r["kuat"]), ("Poin Tantangan", r["tantang"]), ("Nasihat Strategis", r["nasihat"])]
    if not r.get("_png"):
        r["_png"] = trait_cards.kartu_laporan("SOUL MATCH", f'{r["a"]} & {r["b"]}', f'{r["total"]}/100', f'{r["label"]} · {r["rel"]}',
                                              [(x["system"], x["score"]) for x in r["rows"]], "KEKUATAN HUBUNGAN", [t for t in r["kuat"][:3]])
    wa = f'Soul Match {r["a"]} & {r["b"]}: {r["total"]}/100 ({r["label"]}). Cek takdirmu di destinyreveal.id #DestinyReveal'
    RK.actions("dhcp", (cc.cb_ask, ("compat",)), pdf=make_pdf(f"Soul Match - {r['a']} & {r['b']}", f"Skor {r['total']}/100 - {r['label']}", secs),
               text=_plain(r), png=r["_png"], wa=wa, name="soul-match",
               extra=lambda: st.button("🔄 Cek Orang Lain", key="dhcp_again", on_click=_cb_reset, use_container_width=True))


def _cb_close():
    step = st.session_state.get("dh_cp_step")
    if step == "loading":
        _cb_reset()
    elif step == "result":
        cc.dismiss("compat", True, leave=_cb_reset)


@st.dialog("Soul Match", width="large", on_dismiss=_cb_close)
def compat_dialog():
    ss = st.session_state
    step = ss.get("dh_cp_step", "pick")
    if ss.get("dh_cp_rel_key") not in REL_KEYS:
        step = "pick"
    if step == "loading" and ss.get("dh_cp_res"):
        _render_loading()
    elif step == "result" and ss.get("dh_cp_res"):
        cc.wrap("compat", _render_result, leave=_cb_reset, icon="💞", title="Yakin Mau Tutup Hasil Kecocokan?",
                      text="Skor sinergi dan analisis kalian baru saja terbuka. Kalau ditutup, hasil ini hilang dan perlu dihitung ulang.",
                      tip="Download PDF atau salin hasilnya dulu biar bisa dibaca bareng orangnya.",
                      stay="✨ Lanjut Baca", go="Ya, Tutup Hasil")
    elif step == "pick":
        _render_pick()
    else:
        _render_form()


def open_compat(rel_key=None):
    """rel_key=None: entri umum (pilih jenis dulu). Ganti jenis dibanding sebelumnya -> form & hasil direset."""
    ss = st.session_state
    ss.dh_cp_err = None
    if rel_key is None:
        if ss.get("dh_cp_step") not in ("result", "loading"):
            ss.dh_cp_rel_key = None
            _go("pick")
    elif ss.get("dh_cp_rel_key") != rel_key:
        for k in ("dh_cp_res", "dh_cp_sys", "dh_cp_n", *_FORM_KEYS, *("_sv_" + k for k in _FORM_KEYS)):
            ss.pop(k, None)
        ss.dh_cp_rel_key = rel_key
        _go("form")
    elif ss.get("dh_cp_step") not in ("result", "loading"):
        _go("form")
    compat_dialog()


DIALOGS = {"compat": open_compat, **{f"compat_{k}": (lambda k=k: open_compat(k)) for k in REL_KEYS}}
