"""
Penghubung antara engine (perhitungan) dan kamus konten (paragraf) untuk
5 sistem berbasis tanggal lahir yang sudah lengkap: Zodiak, Shio, Weton,
Numerologi, Matrix Destiny.

Dipakai oleh:
- views/loadingpage.py -> compute_raw_result(), dipanggil begitu animasi
  satu titik selesai, hasil MENTAH-nya (dict dari engine) disimpan ke
  st.session_state.loading_results[system].
- views/revealpage.py -> build_display_data(), dipanggil saat amplop
  dibuka/ditampilkan, menggabungkan hasil mentah + kamus konten jadi dict
  siap-render (tagline, chip, title, p1, p2, quote, p3, dst — struktur yang
  sama seperti DUMMY_RESULTS lama).

Sistem lain (BaZi, Zi Wei, Human Design, Golongan Darah, Tarot, ...) belum
masuk sini karena enginenya sendiri belum dibangun (lihat
progress-notes.md) -- compute_raw_result() akan selalu balikin
{"placeholder": True} untuk sistem-sistem itu.

5 sistem KUESIONER Mode Mendalam (MBTI, Big Five, Enneagram, DISC, Love
Language) enginenya SUDAH ada (engine/mbti.py dkk) tapi butuh JAWABAN
user, bukan tanggal lahir -- makanya dipanggil lewat fungsi TERPISAH,
compute_quiz_raw_result(), dari views/loadingpage_mendalam.py (bukan
compute_raw_result() yang di atas, yang emang khusus data tanggal lahir).
Kamus konten paragraf (karir/asmara/dll) buat 5 sistem ini BELUM ditulis
-- build_display_data() makanya masih balikin None buat kelimanya,
sama kayak sistem lain yang belum ada kamus kontennya.
"""

from content.interpretations.bazi import BAZI_CONTENT
from content.interpretations.golongan_darah import GOLONGAN_DARAH_CONTENT
from content.interpretations.human_design import HUMAN_DESIGN_CONTENT
from content.interpretations.matrix_destiny import MATRIX_DESTINY_CONTENT
from content.interpretations.numerologi import NUMEROLOGI_CONTENT
from content.interpretations.shio import SHIO_CONTENT
from content.interpretations.tarot import TAROT_CONTENT
from content.interpretations.weton import WETON_CONTENT
from content.interpretations.ziwei import ZIWEI_CONTENT
from content.interpretations.zodiak import ZODIAK_CONTENT
from engine.bazi import hitung_bazi
from engine.human_design import hitung_human_design
from engine.ziwei import hitung_ziwei
from engine.big_five_scoring import score_big_five
from engine.disc_scoring import score_disc
from engine.enneagram_scoring import score_enneagram
from engine.love_language_scoring import score_love_language
from engine.matrix_destiny import hitung_matrix_destiny
from engine.mbti_scoring import score_mbti
from engine.numerologi import hitung_numerologi_lengkap
from engine.shio import hitung_shio
from engine.tarot import tarik_tarot
from engine.weton import hitung_weton
from engine.zodiak import hitung_zodiak

# Sistem kuesioner Mode Mendalam -> fungsi scoring engine masing2.
QUIZ_SCORERS = {
    "MBTI": score_mbti,
    "Big Five": score_big_five,
    "Enneagram": score_enneagram,
    "DISC": score_disc,
    "Love Language": score_love_language,
}


def compute_quiz_raw_result(system: str, answers: dict) -> dict:
    """
    Hitung hasil MENTAH salah satu dari 5 sistem kuesioner Mode Mendalam,
    dari jawaban user (answers = {question_id: jawaban}, format jawaban
    beda2 per sistem -- lihat docstring tiap engine/*.py).

    Returns:
        dict mentah persis balikan engine/<system>.py, atau
        {"placeholder": True} kalau system bukan salah satu dari 5 ini.
    """
    scorer = QUIZ_SCORERS.get(system)
    if not scorer:
        return {"placeholder": True}
    return scorer(answers)

# Sistem yang sudah punya engine + kamus konten lengkap DAN butuh
# tanggal_lahir buat dihitung.
COMPUTABLE_SYSTEMS = {"Zodiak", "Shio", "Weton", "Numerologi", "Matrix Destiny", "BaZi", "Zi Wei", "Human Design"}

# Sistem yang enginenya udah ada tapi TIDAK butuh tanggal_lahir sama sekali
# -- Golongan Darah (input langsung dari user) & Tarot (random draw).
# Ditangani TERPISAH dari gate tanggal_lahir di bawah, sebelum gate itu
# sempat nge-placeholder-in keduanya cuma gara2 tanggal_lahir kosong.
NON_TANGGAL_LAHIR_SYSTEMS = {"Golongan Darah", "Tarot"}


def compute_raw_result(system: str, loading_data: dict) -> dict:
    """
    Hitung hasil MENTAH dari engine untuk satu sistem, berdasarkan data yang
    sudah dikumpulkan di halaman loading (loading_data — isinya tanggal_lahir,
    jam_lahir, kota_lahir, golongan_darah, sesuai kebutuhan tiap sistem).

    Returns:
        dict mentah persis seperti balikan engine/*.py masing2 sistem, atau
        {"placeholder": True} kalau sistem ini belum punya engine (Zi Wei,
        Human Design, kuesioner, dst -- lihat progress-notes), atau kalau
        tanggal lahirnya di luar jangkauan data engine (mis. shio di luar
        1945-2020).
    """
    # ── Golongan Darah & Tarot: TIDAK butuh tanggal_lahir sama sekali ──
    if system == "Golongan Darah":
        golongan = loading_data.get("golongan_darah")
        if not golongan or golongan not in ("A", "B", "AB", "O"):
            return {"placeholder": True}
        return {"golongan": golongan}

    if system == "Tarot":
        return tarik_tarot()

    tanggal_lahir = loading_data.get("tanggal_lahir")
    if system not in COMPUTABLE_SYSTEMS or not tanggal_lahir:
        return {"placeholder": True}

    try:
        if system == "Zodiak":
            return hitung_zodiak(tanggal_lahir)
        if system == "Shio":
            return hitung_shio(tanggal_lahir)
        if system == "Weton":
            return hitung_weton(tanggal_lahir)
        if system == "Numerologi":
            nama_lengkap = loading_data.get("nama_lengkap")
            if not nama_lengkap:
                # Fallback kalau field nama entah kenapa belum keisi —
                # tetap kasih Life Path Number aja daripada nge-placeholder
                # semua (life_path nggak butuh nama).
                from engine.numerologi import hitung_life_path
                return {"life_path": hitung_life_path(tanggal_lahir)}
            return hitung_numerologi_lengkap(tanggal_lahir, nama_lengkap)
        if system == "Matrix Destiny":
            return hitung_matrix_destiny(tanggal_lahir)
        if system == "BaZi":
            return hitung_bazi(tanggal_lahir)
        if system == "Zi Wei":
            jam_lahir = loading_data.get("jam_lahir")
            if not jam_lahir:
                return {"placeholder": True}
            return hitung_ziwei(tanggal_lahir, jam_lahir.hour)
        if system == "Human Design":
            jam_lahir = loading_data.get("jam_lahir")
            if not jam_lahir:
                return {"placeholder": True}
            kota_lahir = loading_data.get("kota_lahir")
            return hitung_human_design(tanggal_lahir, jam_lahir, kota_lahir)
    except ValueError:
        # Contoh: tahun lahir di luar rentang tabel Imlek (shio 1945-2020).
        # Dianggap belum bisa dihitung untuk tahun ini, bukan error yang
        # bikin aplikasi crash.
        return {"placeholder": True, "error": "di_luar_jangkauan_data"}

    return {"placeholder": True}


def build_display_data(system: str, raw_result):
    """
    Gabungkan hasil MENTAH dari engine + kamus konten jadi dict siap-tampil,
    dengan struktur yang sama persis seperti DUMMY_RESULTS lama di
    views/revealpage.py: tagline, chip, title, p1_label, p1, p2_label, p2,
    quote, p3_label, p3.

    Returns:
        dict siap-tampil, atau None kalau hasilnya masih placeholder/belum
        bisa dipetakan ke kamus konten (caller yang menampilkan pesan
        "belum tersedia" dalam kasus ini).
    """
    if not raw_result or raw_result.get("placeholder"):
        return None

    if system == "Zodiak":
        content = ZODIAK_CONTENT.get(raw_result.get("sign"))
        return dict(content) if content else None

    if system == "Shio":
        content = SHIO_CONTENT.get(raw_result.get("shio"))
        return dict(content) if content else None

    if system == "Weton":
        content = WETON_CONTENT.get(raw_result.get("pasaran"))
        if not content:
            return None
        data = dict(content)
        hari = raw_result.get("hari", "")
        neptu = raw_result.get("neptu", "")
        data["title"] = data["title"].format(hari=hari, neptu=neptu)
        data["p1"] = data["p1"].format(hari=hari, neptu=neptu)
        return data

    if system == "Numerologi":
        content = NUMEROLOGI_CONTENT.get(raw_result.get("life_path"))
        return dict(content) if content else None

    if system == "Matrix Destiny":
        content = MATRIX_DESTINY_CONTENT.get(raw_result.get("titik_inti"))
        return dict(content) if content else None

    if system == "BaZi":
        content = BAZI_CONTENT.get(raw_result.get("day_master"))
        return dict(content) if content else None

    if system == "Zi Wei":
        content = ZIWEI_CONTENT.get(raw_result.get("bintang"))
        return dict(content) if content else None

    if system == "Human Design":
        content = HUMAN_DESIGN_CONTENT.get(raw_result.get("tipe_slug"))
        return dict(content) if content else None

    if system == "Golongan Darah":
        content = GOLONGAN_DARAH_CONTENT.get(raw_result.get("golongan"))
        return dict(content) if content else None

    if system == "Tarot":
        content = TAROT_CONTENT.get(raw_result.get("kartu"))
        return dict(content) if content else None

    return None
