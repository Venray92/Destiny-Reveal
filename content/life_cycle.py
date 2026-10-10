"""
Visual dashboard siklus hidup (Batch 7): Roda Takdir (Matrix Destiny) + Grafik Usia 20-60 (Matrix Destiny / Numerologi Pinnacle).
Titik & usia dihitung dari rumus yang sudah divalidasi (engine/matrix_destiny.py, engine/numerologi.py).
Titik usia Matrix: A0, F10, B20, G30, C40, I50, D60, H70 (tervalidasi). Titik antara (usia 5, 15, ...) TIDAK dipakai: rumusnya belum terverifikasi.
Teks fase = kamus 22 arketipe (sisi kuat / sisi waspada) + tema dekade + skor energi.
SKOR = interpretasi kami (tabel ARC_SKOR / PIN_SKOR), bukan data statistik. Teks panjang per fase: opsi upgrade lewat Gemini.
"""

from datetime import date

from engine.matrix_destiny import NAMA_ARKETIPE, _reduce_ke_1_22, hitung_matrix_destiny
from engine.numerologi import _reduce, hitung_life_path

# (sisi kuat, sisi waspada, skor energi 0-100)
ARC = {
    1: ("Kreatif, mandiri, perintis, mudah mewujudkan ide.", "Egois, merasa paling benar, cenderung memanipulasi.", 82),
    2: ("Intuitif, tenang, penyembuh alami, diplomatis.", "Bermuka dua, pasif-agresif, mudah terseret gosip.", 66),
    3: ("Mengayomi, berbakat bisnis, estetik, hangat.", "Dominan, materialistis, ingin mengontrol.", 84),
    4: ("Terstruktur, pemimpin alami, protektif, tangguh.", "Otoriter, kaku, takut kehilangan kendali.", 78),
    5: ("Suka belajar dan mengajar, memegang aturan, pemersatu keluarga.", "Menggurui, kaku pada cara lama.", 68),
    6: ("Ramah, komunikatif, menyukai keindahan, pandai bergaul.", "Ragu-ragu, dangkal, butuh validasi luar.", 74),
    7: ("Ambisius, cepat bertindak, fokus pada tujuan.", "Agresif, asal terjang, cepat marah bila tertunda.", 80),
    8: ("Paham hukum sebab-akibat, jujur, objektif, seimbang.", "Menyalahkan keadaan, menyimpan dendam.", 70),
    9: ("Bijaksana, pemikir mendalam, mandiri, ahli di bidangnya.", "Mengisolasi diri, takut kesepian, pelit berbagi ilmu.", 58),
    10: ("Fleksibel, adaptif, peka pada peluang dan arus.", "Malas, pasrah tanpa usaha, mudah terpengaruh.", 72),
    11: ("Energi besar, pekerja keras, stamina fisik dan mental kuat.", "Memaksakan kehendak, impulsif, mudah emosi.", 79),
    12: ("Empati tinggi, sudut pandang unik, suka menolong.", "Menempatkan diri sebagai korban, sulit menolak.", 52),
    13: ("Berani bertransformasi, adaptif, mampu melepas masa lalu.", "Takut perubahan, menimbun kenangan lama.", 55),
    14: ("Sabar, moderat, jiwa seni tinggi, penyembuh emosional.", "Ekstrem, tidak sabar, emosi naik-turun.", 76),
    15: ("Karismatik, jeli melihat peluang uang, paham psikologi manusia.", "Terjebak kebiasaan buruk, manipulatif, serakah.", 48),
    16: ("Mampu bangkit dari keruntuhan, mental sekuat baja.", "Menolak kenyataan, hidup berantakan, emosi meledak.", 42),
    17: ("Berbakat, populer, inspiratif, optimis.", "Minder atau justru merasa paling bersinar.", 86),
    18: ("Imajinatif, intuitif, punya daya tarik misterius.", "Cemas berlebihan, mudah murung, takut hal tak terlihat.", 50),
    19: ("Pemimpin hangat, membawa kebahagiaan dan kemakmuran, dermawan.", "Kelelahan, haus perhatian, egosentris.", 92),
    20: ("Terhubung kuat dengan keluarga dan leluhur, intuisi tajam.", "Menghakimi keluarga, memikul beban keturunan.", 66),
    21: ("Berpikiran luas, toleran, sukses skala luas.", "Pikiran sempit, takut menjelajah hal baru.", 88),
    22: ("Jiwa bebas, tidak terikat materi, ceria, percaya proses.", "Tidak bertanggung jawab, ceroboh, melanggar aturan.", 70),
}
TITIK = {"A": "Karakter luar", "B": "Jalur spiritual (sisi ibu)", "C": "Jalur material (sisi ayah)", "D": "Ekor karma",
         "E": "Inti jiwa", "F": "Garis pria pihak ibu", "G": "Garis pria pihak ayah", "I": "Garis wanita pihak ayah",
         "H": "Garis wanita pihak ibu"}
# urutan melingkar dan usia (derajat dihitung di komponen)
WHEEL = [("A", 0), ("F", 10), ("B", 20), ("G", 30), ("C", 40), ("I", 50), ("D", 60), ("H", 70)]
TEMA_DEKADE = {20: "membangun jati diri dan jalur karier", 30: "mematangkan peran, keluarga, dan keputusan besar",
               40: "memanen hasil dan mulai berkontribusi lebih luas", 50: "merangkum pengalaman dan mewariskan kebijaksanaan",
               60: "memasuki fase pelepasan beban dan kebijaksanaan"}


def _pita(skor):
    return ("puncak peluang: waktu yang baik untuk langkah besar yang sudah kamu persiapkan" if skor >= 75 else
            "fase stabil: jaga ritme, perkuat hubungan dan fondasi" if skor >= 55 else
            "fase belajar: perlambat, kurangi risiko, dan fokus membereskan hal yang tertunda")


def _pts(tgl):
    m = hitung_matrix_destiny(tgl)
    p, a = m["personal_square"], m["ancestral_square"]
    v = {"A": p["a"], "B": p["b"], "C": p["c"], "D": p["d"], "E": p["e"], "F": a["f"], "G": a["g"], "I": a["i"], "H": a["h"]}
    return v


def roda(tgl):
    """Titik Roda Takdir: [{kode, nama_titik, usia, arcana, nama, kuat, waspada, skor, teks}] + inti."""
    v = _pts(tgl)
    out = []
    for k, usia in WHEEL:
        n = v[k]
        out.append({"kode": k, "titik": TITIK[k], "usia": usia, "arcana": n, "nama": NAMA_ARKETIPE[n], "kuat": ARC[n][0],
                    "waspada": ARC[n][1], "skor": ARC[n][2]})
    e = v["E"]
    inti = {"kode": "E", "titik": TITIK["E"], "usia": None, "arcana": e, "nama": NAMA_ARKETIPE[e], "kuat": ARC[e][0],
            "waspada": ARC[e][1], "skor": ARC[e][2]}
    return {"titik": out, "inti": inti}


def grafik_matrix(tgl):
    """Titik utama usia 20,30,40,50,60 (rumus tervalidasi) + 4 segmen dekade di antaranya.
    Titik "antara" (usia 25, 35, ...) sengaja TIDAK dipakai: rumusnya belum terverifikasi dari sumber."""
    v = _pts(tgl)
    main = {usia: v[k] for k, usia in WHEEL}
    pts = []
    for usia in range(20, 61, 10):
        n = main[usia]
        kuat, waspada, skor = ARC[n]
        dek = usia if usia < 60 else 50
        pts.append({"usia": usia, "arcana": n, "nama": NAMA_ARKETIPE[n], "skor": skor, "kuat": kuat, "waspada": waspada,
                    "teks": [f"Di usia {usia}, energi {NAMA_ARKETIPE[n]} (kode {n}) menjadi titik penting. "
                             f"Tema dekade sekitar titik ini: {TEMA_DEKADE[usia]}.",
                             f"Kekuatan yang bisa kamu pakai: {kuat}", f"Yang perlu dijaga: {waspada}",
                             f"Secara umum ini {_pita(skor)}."]})
    segs = []
    for a_, b_ in zip(pts, pts[1:]):
        mid = round((a_["skor"] + b_["skor"]) / 2)
        segs.append({"dari": a_["usia"], "sampai": b_["usia"], "skor": mid,
                     "teks": [f"Usia {a_['usia']} sampai {b_['usia']}: perjalanan dari energi {a_['nama']} menuju {b_['nama']}. "
                              f"Tema fase ini: {TEMA_DEKADE[a_['usia']]}.",
                              f"Awal fase kamu masih membawa kekuatan {a_['nama']}: {a_['kuat']}",
                              f"Menjelang akhir fase, energi {b_['nama']} mulai terasa: {b_['kuat']}",
                              f"Kewaspadaan fase ini: {a_['waspada']} Lalu: {b_['waspada']}",
                              f"Secara umum ini {_pita(mid)}."]})
    return {"titik": pts, "segmen": segs}


# ─────────────── Numerologi: Pinnacle ───────────────
# (tema, peluang, tantangan)
PIN = {
    1: ("Kemandirian & Awal Baru", "Memimpin, merintis, mengambil inisiatif sendiri.", "Terlalu mengandalkan diri dan sulit menerima bantuan."),
    2: ("Kemitraan & Kesabaran", "Kerja sama, diplomasi, relasi yang mendukung.", "Ragu mengambil keputusan dan terlalu mengalah."),
    3: ("Ekspresi & Kreativitas", "Berkarya, berkomunikasi, tampil dan bersosialisasi.", "Energi tersebar dan sulit menuntaskan."),
    4: ("Fondasi & Disiplin", "Membangun sistem, kestabilan, kerja keras yang terukur.", "Kaku, terlalu keras pada diri sendiri."),
    5: ("Perubahan & Kebebasan", "Bergerak, mencoba hal baru, memperluas jaringan.", "Tidak konsisten dan mudah bosan."),
    6: ("Tanggung Jawab & Keluarga", "Merawat, membina hubungan, menciptakan harmoni.", "Memikul beban orang lain terlalu banyak."),
    7: ("Refleksi & Pendalaman", "Belajar mendalam, riset, spiritualitas, pemahaman diri.", "Menarik diri dan terlalu banyak menganalisis."),
    8: ("Otoritas & Keuangan", "Karier, kepemimpinan, hasil materi yang nyata.", "Terlalu fokus pada status dan kendali."),
    9: ("Penyelesaian & Pelepasan", "Menutup siklus lama, berbagi, kontribusi untuk orang banyak.", "Sulit melepas masa lalu."),
    11: ("Inspirasi & Intuisi", "Intuisi tajam, inspirasi untuk orang lain, wawasan spiritual.", "Sensitivitas tinggi dan tegang saraf."),
    22: ("Pembangun Besar", "Mewujudkan visi berskala besar dengan struktur yang kuat.", "Tekanan ekspektasi tinggi dan beban berat."),
    33: ("Pembimbing & Pelayan", "Membimbing dan melayani dengan welas asih.", "Mengorbankan diri berlebihan."),
}
PIN_SKOR = {1: 80, 2: 60, 3: 78, 4: 62, 5: 72, 6: 74, 7: 55, 8: 86, 9: 60, 11: 80, 22: 90, 33: 84}


def pinnacle(tgl):
    """4 periode Pinnacle: [{no, angka, usia_awal, usia_akhir (None=seterusnya), ...}]."""
    d, m = _reduce(tgl.day), _reduce(tgl.month)
    y = _reduce(sum(int(c) for c in str(tgl.year)))
    p1, p2 = _reduce(m + d), _reduce(d + y)
    nums = [p1, p2, _reduce(p1 + p2), _reduce(m + y)]
    lp = hitung_life_path(tgl)
    lp1 = {11: 2, 22: 4, 33: 6}.get(lp, lp)
    e1 = 36 - lp1
    rng = [(0, e1), (e1 + 1, e1 + 9), (e1 + 10, e1 + 18), (e1 + 19, None)]
    out = []
    for i, (n, (a, b)) in enumerate(zip(nums, rng), 1):
        tema, peluang, tantangan = PIN[n]
        out.append({"no": i, "angka": n, "usia_awal": a, "usia_akhir": b, "tema": tema, "skor": PIN_SKOR[n],
                    "teks": [f"Pinnacle {i} (angka {n}) berlaku {'usia %d sampai %d' % (a, b) if b is not None else 'dari usia %d seterusnya' % a}. "
                             f"Temanya {tema.lower()}.", f"Peluang: {peluang}", f"Tantangan: {tantangan}",
                             f"Secara umum ini {_pita(PIN_SKOR[n])}."]})
    return out


def usia(tgl, today):
    return today.year - tgl.year - ((today.month, today.day) < (tgl.month, tgl.day))


def konteks(tgl, today):
    """Konteks personal hari ini: usia, fase Pinnacle yang sedang berjalan, Personal Year tahun ini."""
    from content import periodic
    from content.yearly_calc import TEMA_PY
    u = usia(tgl, today)
    fase = next((p for p in pinnacle(tgl) if u >= p["usia_awal"] and (p["usia_akhir"] is None or u <= p["usia_akhir"])), None)
    py = periodic.personal_year(tgl, today.year)
    return {"usia": u, "fase": fase, "py": py, "py_tema": TEMA_PY.get(py, "")}
