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

Sistem lain (BaZi, Zi Wei, Human Design, Golongan Darah, MBTI dkk,
Tarot, ...) belum masuk sini karena enginenya sendiri belum dibangun
(lihat progress-notes.md) -- compute_raw_result() akan selalu balikin
{"placeholder": True} untuk sistem-sistem itu.
"""

from content.interpretations.matrix_destiny import MATRIX_DESTINY_CONTENT
from content.interpretations.numerologi import NUMEROLOGI_CONTENT
from content.interpretations.shio import SHIO_CONTENT
from content.interpretations.weton import WETON_CONTENT
from content.interpretations.zodiak import ZODIAK_CONTENT
from engine.matrix_destiny import hitung_matrix_destiny
from engine.numerologi import hitung_life_path
from engine.shio import hitung_shio
from engine.weton import hitung_weton
from engine.zodiak import hitung_zodiak

# Sistem yang sudah punya engine + kamus konten lengkap (berbasis tanggal
# lahir saja, tidak butuh jam/kota/kuesioner).
COMPUTABLE_SYSTEMS = {"Zodiak", "Shio", "Weton", "Numerologi", "Matrix Destiny"}


def compute_raw_result(system: str, loading_data: dict) -> dict:
    """
    Hitung hasil MENTAH dari engine untuk satu sistem, berdasarkan data yang
    sudah dikumpulkan di halaman loading (loading_data — isinya tanggal_lahir,
    jam_lahir, kota_lahir, golongan_darah, sesuai kebutuhan tiap sistem).

    Returns:
        dict mentah persis seperti balikan engine/*.py masing2 sistem, atau
        {"placeholder": True} kalau sistem ini belum punya engine (BaZi, Zi
        Wei, Human Design, Golongan Darah, kuesioner, Tarot, dst), atau
        kalau tanggal lahirnya di luar jangkauan data engine (mis. shio di
        luar 1945-2020).
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
            return {"life_path": hitung_life_path(tanggal_lahir)}
        if system == "Matrix Destiny":
            return hitung_matrix_destiny(tanggal_lahir)
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

    return None
