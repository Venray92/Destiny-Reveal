"""
Engine: Matrix Destiny (Peta Takdir) — metode resmi Natalia Ladini (versi
Rusia, bukan versi Eropa/Amerika — sudah dikonfirmasi Stev ini yang mau
diikuti, rujukan https://matrix-destiny.com/).

Menghitung 8 titik Personal Square + Ancestral Square + Love/Money/Balance
+ Purpose, PLUS tabel 7 Chakra/Health Card — semuanya tervalidasi manual
(cocok persis sama screenshot hasil matrix-destiny.com yang dikasih Stev,
lihat memory project /areas/matrix-destiny-formula.md untuk detail rumus &
contoh hitungan 5 Des 1992).

GANTI dari revisi sebelumnya: dulu titik_inti dihitung pakai shortcut
(jumlah semua digit tanggal+bulan+tahun sekaligus) — TERBUKTI beda dari
metode resmi di atas (contoh 5 Des 1992: shortcut = 11 "The Brave", metode
resmi = 13 "The Transformation"). Sekarang titik_inti = Titik E (Center /
Inti Jiwa), dihitung lewat Personal Square sesuai metode resmi.

Nama arketipe (NAMA_ARKETIPE) SENGAJA BUKAN nama asli 22 Major Arcana
Tarot (The Magician, The Fool, dst) — dipakai nama orisinal biar nggak
dianggap menjiplak filosofi/branding matrix-destiny.com atau tarot,
walaupun urutan makna & nomornya (1-22) tetap mengikuti pembacaan yang
sama. Nama file gambar kartu di assets/cards/matrix_destiny/ juga
mengikuti nama orisinal ini.
"""

from datetime import date

JUMLAH_ARKETIPE = 22

# Nama arketipe I-XXII, cocok sama urutan file assets/cards/matrix_destiny/
# (01_the_beginner.png ... 22_the_unity.png).
NAMA_ARKETIPE = {
    1: "The Beginner", 2: "The Listener", 3: "The Creator", 4: "The Ruler",
    5: "The Teacher", 6: "The Partners", 7: "The Conqueror", 8: "The Balance",
    9: "The Hermit", 10: "The Wheel", 11: "The Brave", 12: "The Sacrifice",
    13: "The Transformation", 14: "The Alchemist", 15: "The Shadow",
    16: "The Collapse", 17: "The Hope", 18: "The Mystery", 19: "The Joy",
    20: "The Awakening", 21: "The Achievement", 22: "The Unity",
}


def _reduce_ke_1_22(n: int) -> int:
    while n > JUMLAH_ARKETIPE:
        n = sum(int(d) for d in str(n))
    return n


def _chakra_row(physics: int, energy: int) -> dict:
    return {
        "physics": physics,
        "energy": energy,
        "emotions": _reduce_ke_1_22(physics + energy),
    }


def hitung_matrix_destiny(tanggal_lahir: date) -> dict:
    """
    Args:
        tanggal_lahir (date): tanggal lahir user

    Returns:
        dict berisi:
        - titik_inti, nama_arketipe: Titik E (Center/Inti Jiwa), dipakai
          buat pilih kartu utama & konten interpretasi (key content dict
          masih 1-22, nggak berubah).
        - personal_square: {a, b, c, d, e} (Hari/Bulan/Tahun/Karmic Tail/Center)
        - ancestral_square: {f, g, h, i} (garis leluhur)
        - love_money: {love, money, balance}
        - purpose: {sky, earth, personal, male_line, female_line, social, main_destiny}
        - chakra: {sahasrara, ajna, vishuddha, anahata, manipura, svadhisthana,
          muladhara} masing-masing {physics, energy, emotions}
    """
    a = _reduce_ke_1_22(tanggal_lahir.day)
    b = tanggal_lahir.month
    c = _reduce_ke_1_22(sum(int(d) for d in str(tanggal_lahir.year)))
    d = _reduce_ke_1_22(a + b + c)
    e = _reduce_ke_1_22(a + b + c + d)  # Center / Inti Jiwa

    f = _reduce_ke_1_22(a + b)
    g = _reduce_ke_1_22(b + c)
    i_ = _reduce_ke_1_22(c + d)
    h = _reduce_ke_1_22(a + d)

    love = _reduce_ke_1_22(e + d)
    money = _reduce_ke_1_22(e + c)
    balance = _reduce_ke_1_22(love + money)

    sky = _reduce_ke_1_22(b + d)
    earth = _reduce_ke_1_22(a + c)
    personal_purpose = _reduce_ke_1_22(sky + earth)

    male_line = _reduce_ke_1_22(f + i_)
    female_line = _reduce_ke_1_22(g + h)
    social_purpose = _reduce_ke_1_22(male_line + female_line)

    main_destiny = _reduce_ke_1_22(personal_purpose + social_purpose)

    vishuddha = _chakra_row(_reduce_ke_1_22(e + a), _reduce_ke_1_22(e + c))
    chakra = {
        "sahasrara": _chakra_row(a, b),
        "ajna": _chakra_row(a, _reduce_ke_1_22(g + e)),
        "vishuddha": vishuddha,
        "anahata": _chakra_row(
            _reduce_ke_1_22(vishuddha["physics"] + e),
            _reduce_ke_1_22(vishuddha["energy"] + e),
        ),
        "manipura": _chakra_row(e, e),
        "svadhisthana": _chakra_row(_reduce_ke_1_22(e + c), _reduce_ke_1_22(e + d)),
        "muladhara": _chakra_row(c, d),
    }

    titik_inti = e
    return {
        "titik_inti": titik_inti,
        "nama_arketipe": NAMA_ARKETIPE[titik_inti],
        "personal_square": {"a": a, "b": b, "c": c, "d": d, "e": e},
        "ancestral_square": {"f": f, "g": g, "h": h, "i": i_},
        "love_money": {"love": love, "money": money, "balance": balance},
        "purpose": {
            "sky": sky, "earth": earth, "personal": personal_purpose,
            "male_line": male_line, "female_line": female_line,
            "social": social_purpose, "main_destiny": main_destiny,
        },
        "chakra": chakra,
    }
