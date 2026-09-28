"""
Penghubung antara engine (perhitungan) dan kamus konten (paragraf) untuk
SEMUA 15 sistem: 10 sistem berbasis data lahir (Zodiak, Shio, Weton,
Numerologi, Matrix Destiny, BaZi, Zi Wei, Human Design, Golongan Darah,
Tarot) + 5 sistem kuesioner Mode Mendalam (MBTI, Big Five, Enneagram,
DISC, Love Language).

Dipakai oleh:
- views/loadingpage.py / views/loadingpage_lengkap.py -> compute_raw_result(),
  dipanggil begitu animasi satu titik selesai, hasil MENTAH-nya (dict dari
  engine) disimpan ke st.session_state.loading_results[system].
- views/loadingpage_mendalam.py -> compute_quiz_raw_result(), khusus 5
  sistem kuesioner (butuh jawaban user, bukan tanggal lahir).
- views/revealpage.py -> build_display_data(), dipanggil saat amplop
  dibuka/ditampilkan, menggabungkan hasil mentah + kamus konten jadi dict
  siap-render (tagline, chip, title, p1, p2, quote, p3, dst — struktur yang
  sama seperti DUMMY_RESULTS lama).

REVISI (28 Sep 2026): sebelumnya cuma 5 sistem lama yang tersambung di sini
walau kamus konten + engine buat 10 sistem lainnya sudah lengkap ada di
GitHub (BaZi/Zi Wei/Human Design/Golongan Darah/Tarot ditulis di sesi
sebelumnya, MBTI/Big Five/Enneagram/DISC/Love Language baru ditulis batch
ini) -- akibatnya amplop 10 sistem itu selalu jatuh ke fallback generic
walau datanya sudah ada. Batch ini nyambungin SEMUANYA.
"""

from content.interpretations.big_five import BIG_FIVE_CONTENT
from content.interpretations.content_interpretations__bazi import BAZI_CONTENT
from content.interpretations.content_interpretations__golongan_darah import (
    GOLONGAN_DARAH_CONTENT,
)
from content.interpretations.content_interpretations__human_design import (
    HUMAN_DESIGN_CONTENT,
)
from content.interpretations.content_interpretations__tarot import TAROT_CONTENT
from content.interpretations.content_interpretations__ziwei import ZIWEI_CONTENT
from content.interpretations.disc import DISC_CONTENT
from content.interpretations.enneagram import ENNEAGRAM_CONTENT
from content.interpretations.love_language import LOVE_LANGUAGE_CONTENT
from content.interpretations.matrix_destiny import MATRIX_DESTINY_CONTENT
from content.interpretations.mbti import MBTI_CONTENT
from content.interpretations.numerologi import NUMEROLOGI_CONTENT
from content.interpretations.shio import SHIO_CONTENT
from content.interpretations.weton import WETON_CONTENT
from content.interpretations.zodiak import ZODIAK_CONTENT
from engine.big_five_scoring import score_big_five
from engine.disc_scoring import score_disc
from engine.engine__bazi import hitung_bazi
from engine.engine__human_design import hitung_human_design
from engine.engine__tarot import TAROT_MAJOR_ARCANA, tarik_tarot
from engine.engine__ziwei import hitung_ziwei
from engine.enneagram_scoring import score_enneagram
from engine.love_language_scoring import score_love_language
from engine.matrix_destiny import hitung_matrix_destiny
from engine.mbti_scoring import score_mbti
from engine.numerologi import hitung_numerologi_lengkap
from engine.shio import hitung_shio
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
    beda2 per sistem -- lihat docstring tiap engine/*_scoring.py).

    Returns:
        dict mentah persis balikan engine/<system>_scoring.py, atau
        {"placeholder": True} kalau system bukan salah satu dari 5 ini.
    """
    scorer = QUIZ_SCORERS.get(system)
    if not scorer:
        return {"placeholder": True}
    return scorer(answers)


# Sistem berbasis tanggal lahir yang sudah punya engine + kamus konten
# lengkap. "Golongan Darah" & "Tarot" masuk sini juga walau gak butuh
# rumus tanggal lahir beneran (golongan darah cuma lookup langsung dari
# input user, tarot acak) -- disatukan di sini karena SAMA-SAMA dipanggil
# lewat compute_raw_result() dari alur animasi titik yang sama
# (views/loadingpage_lengkap.py), dan tanggal_lahir tetap selalu ada di
# loading_data pada titik itu (wajib diisi di form intake).
COMPUTABLE_SYSTEMS = {
    "Zodiak", "Shio", "Weton", "Numerologi", "Matrix Destiny",
    "BaZi", "Zi Wei", "Human Design", "Golongan Darah", "Tarot",
}


def compute_raw_result(system: str, loading_data: dict) -> dict:
    """
    Hitung hasil MENTAH dari engine untuk satu sistem, berdasarkan data yang
    sudah dikumpulkan di halaman loading (loading_data — isinya tanggal_lahir,
    jam_lahir, kota_lahir, golongan_darah, sesuai kebutuhan tiap sistem).

    Returns:
        dict mentah persis seperti balikan engine/*.py masing2 sistem, atau
        {"placeholder": True} kalau sistem ini belum ada di COMPUTABLE_SYSTEMS,
        datanya belum lengkap (mis. jam lahir belum keisi buat Zi Wei/Human
        Design), atau kalau tanggal lahirnya di luar jangkauan data engine
        (mis. shio di luar 1945-2020, atau tahun terlalu lawas buat sxtwl).
    """
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

        if system == "Golongan Darah":
            # Bukan hasil hitungan — cuma diteruskan langsung dari input
            # user (sudah dijamin selalu keisi oleh form intake Mode
            # Lengkap, diacak otomatis kalau user pilih "Tidak Tahu").
            golongan_darah = loading_data.get("golongan_darah")
            if not golongan_darah:
                return {"placeholder": True}
            return {"golongan_darah": golongan_darah}

        if system == "Tarot":
            # random.choice sekali doang di sini -- caller (_animate_point)
            # sudah jamin fungsi ini cuma dipanggil SEKALI per sesi per
            # sistem (hasil di-cache ke session_state.loading_results),
            # jadi kartu yang ketarik gak berubah-ubah tiap rerun.
            return tarik_tarot()

    except ValueError:
        # Contoh: tahun lahir di luar rentang tabel Imlek (shio 1945-2020,
        # atau di luar rentang yang didukung sxtwl/pyswisseph).
        # Dianggap belum bisa dihitung untuk tahun ini, bukan error yang
        # bikin aplikasi crash.
        return {"placeholder": True, "error": "di_luar_jangkauan_data"}

    return {"placeholder": True}


_BIG_FIVE_ID_NAMES = {
    "O": "keterbukaan terhadap pengalaman baru",
    "C": "kehati-hatian/kedisiplinan",
    "E": "ekstraversi",
    "A": "keramahan",
    "N": "kepekaan emosi",
}


def _build_big_five_display(raw_result):
    """
    Big Five beda dari sistem lain: hasilnya 5 nilai (trait) sekaligus,
    bukan 1 tipe tunggal, jadi gak bisa langsung lookup 1 dict kayak
    ZODIAK_CONTENT dkk.

    Pendekatan: trait yang skornya PALING TINGGI ("dominant_trait",
    sudah dihitung engine/big_five_scoring.py) dipakai sebagai judul &
    narasi utama (p1/p2/quote/p3/domains, persis kayak sistem lain),
    LALU 4 trait lainnya dirangkum singkat (field "ringkas" di kamus
    konten) dan disambung ke akhir p1 -- supaya laporan tetap
    merepresentasikan seluruh 5 dimensi kepribadian, bukan cuma 1 label.
    """
    levels = raw_result.get("levels") or {}
    dominant_trait = raw_result.get("dominant_trait")
    if not dominant_trait or dominant_trait not in levels:
        return None

    dominant_level = levels[dominant_trait]
    base = BIG_FIVE_CONTENT.get(dominant_trait, {}).get(dominant_level)
    if not base:
        return None

    data = dict(base)
    ringkasan_lain = []
    for trait in ("O", "C", "E", "A", "N"):
        if trait == dominant_trait:
            continue
        level = levels.get(trait)
        entry = BIG_FIVE_CONTENT.get(trait, {}).get(level)
        if entry and entry.get("ringkas"):
            ringkasan_lain.append(
                f"Dari sisi {_BIG_FIVE_ID_NAMES[trait]} ({level.lower()}), "
                f"{entry['ringkas']}"
            )

    if ringkasan_lain:
        data["p1"] = (
            data["p1"]
            + " Selain sisi yang paling menonjol itu, ada empat dimensi lain "
            "dari kepribadianmu yang juga membentuk caramu menjalani hidup: "
            + " ".join(ringkasan_lain)
        )
    return data


def build_display_data(system: str, raw_result):
    """
    Gabungkan hasil MENTAH dari engine + kamus konten jadi dict siap-tampil,
    dengan struktur yang sama persis seperti DUMMY_RESULTS lama di
    views/revealpage.py: tagline, chip, title, p1_label, p1, p2_label, p2,
    quote, p3_label, p3, domains.

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
        content = GOLONGAN_DARAH_CONTENT.get(raw_result.get("golongan_darah"))
        return dict(content) if content else None

    if system == "Tarot":
        content = TAROT_CONTENT.get(raw_result.get("kartu"))
        return dict(content) if content else None

    if system == "MBTI":
        content = MBTI_CONTENT.get(raw_result.get("tipe"))
        return dict(content) if content else None

    if system == "Enneagram":
        content = ENNEAGRAM_CONTENT.get(raw_result.get("tipe"))
        return dict(content) if content else None

    if system == "DISC":
        content = DISC_CONTENT.get(raw_result.get("tipe"))
        return dict(content) if content else None

    if system == "Love Language":
        content = LOVE_LANGUAGE_CONTENT.get(raw_result.get("primary"))
        return dict(content) if content else None

    if system == "Big Five":
        return _build_big_five_display(raw_result)

    return None
