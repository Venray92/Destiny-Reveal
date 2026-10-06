"""
Penghubung antara engine (perhitungan) dan kamus konten (paragraf) untuk
SEMUA 15 sistem: 10 sistem berbasis data lahir (Zodiak, Shio, Weton,
Numerologi, Matrix Destiny, BaZi, Zi Wei, Human Design, Golongan Darah,
Tarot) + 5 sistem kuesioner Mode Mendalam (MBTI, Big Five, Enneagram,
DISC, Love Language).

Dipakai oleh:
- views/loadingpage.py / views/loadingpage_lengkap.py -> compute_raw_result()
- views/loadingpage_mendalam.py -> compute_quiz_raw_result() (5 sistem kuesioner)
- views/revealpage.py -> build_display_data()

Changelog & bug-fix: lihat docs/changelog.md.
"""

from content import profile_flat
from content.profile_loader import get_profile, get_title
from engine.big_five_scoring import score_big_five
from engine.disc_scoring import score_disc
from engine.bazi import hitung_bazi
from engine.human_design import hitung_human_design
from engine.tarot import tarik_tarot
from engine.ziwei import hitung_ziwei
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


def _display_flat(system, raw_result):
    """Dict siap-tampil 9 sistem non-Mode-1 + Tarot dari JSON baru (free/paid) + titles.json.
    p1=free.siapa_kamu, p2=paid.kekuatan, p3=paid.pr_kecil, domains=karir/asmara/keuangan/kesehatan."""
    if system == "Big Five":
        prof = profile_flat.get_big_five(raw_result)
        judul = prof and prof["title"]
    else:
        prof = profile_flat.get_profile(system, raw_result)
        judul = profile_flat.get_title(system, raw_result)
    if not prof or not judul:
        return None
    free, paid = prof["free"], prof["paid"]
    if not free.get("siapa_kamu") or not paid.get("kekuatan_yang_perlu_dijaga") or not paid.get("pr_kecil_buat_kamu"):
        return None
    p1 = free["siapa_kamu"]
    if system == "Big Five" and prof["ringkas"]:
        p1 += (" Selain sisi yang paling menonjol itu, ada empat dimensi lain dari kepribadianmu yang juga membentuk "
               "caramu menjalani hidup: " + " ".join(prof["ringkas"]))
    return {
        "tagline": judul["tagline"], "chip": judul["chip"], "title": judul["title"],
        "p1_label": "Siapa Kamu", "p1": p1,
        "p2_label": "Kekuatan & yang Perlu Dijaga", "p2": paid["kekuatan_yang_perlu_dijaga"],
        "quote": free.get("quote", ""),
        "p3_label": "PR Kecil Buat Kamu", "p3": paid["pr_kecil_buat_kamu"],
        "domains": {k: paid[k] for k in ("karir", "asmara", "keuangan", "kesehatan") if paid.get(k)},
    }


_JSON_SYSTEMS = ("Zodiak", "Shio", "Weton", "Numerologi", "Matrix Destiny")


def _display_dari_json(system, raw_result):
    """Dict siap-tampil (bentuk sama dengan kamus lama) dari JSON profil baru + titles.json.
    Peta seksi: p1=free.siapa_kamu, p2=D (kekuatan), p3=F (nasihat), domains karir=B, asmara=C.
    None kalau profil / judul entri ini belum ada."""
    prof = get_profile(system, raw_result)
    judul = get_title(system, raw_result)
    sec = (prof or {}).get("sections") or {}
    if not prof or not judul or not prof["free"].get("siapa_kamu") or not all(h in sec for h in "BCDF"):
        return None
    return {
        **judul,
        "p1_label": "Siapa Kamu", "p1": prof["free"]["siapa_kamu"],
        "p2_label": "Kekuatan & yang Perlu Dijaga", "p2": sec["D"],
        "quote": prof["free"].get("quote", ""),
        "p3_label": "PR Kecil Buat Kamu", "p3": sec["F"],
        "domains": {"karir": sec["B"], "asmara": sec["C"]},
    }


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

    if system in _JSON_SYSTEMS:
        return _display_dari_json(system, raw_result)  # sumber tunggal: JSON baru

    if system in profile_flat.SYSTEMS:
        return _display_flat(system, raw_result)

    return None
