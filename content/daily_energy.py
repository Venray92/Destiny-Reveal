"""
Skor Energi Hari Ini (0-100) + Afirmasi Harian, gabungan 4 sistem (Zodiak, Shio, Weton, Numerologi).
Semua deterministik dari tanggal lahir + tanggal hari ini (WIB), tidak ada angka acak.

Sumber aturan (tabel skor = bobot interpretasi kita, bukan hasil riset kuantitatif):
- Zodiak   : rumah transit Bulan (whole sign, dari tanda user). Klasik Hellenistik: rumah 1,5,9,10,11 kondusif;
             rumah 6,8,12 berat (Vettius Valens, Anthologiae; Ptolemy, Tetrabiblos).
- Shio     : relasi cabang bumi pilar hari vs shio user: Liu He (6 harmoni), San He (3 harmoni),
             Chong (bentrok), Hai (rugi) — tradisi BaZi/Tong Shu (Zi Ping Zhen Quan).
- Weton    : Pancasuda dari neptu gabungan (neptu lahir + neptu hari ini) mod 5 — memakai tabel Pancasuda
             yang sama dengan engine/weton.py. Ini PERKIRAAN (penerapan harian bukan baku primbon).
- Numerologi: personal day (personal month + tanggal, direduksi 1-9) — konsisten dengan content/periodic.py.
Biorhythm dibuang di fitur harian (tidak punya dasar 4 sistem di atas).
"""

import datetime as _dt

from content import periodic
from engine.astro_lite import rumah, tanda_bulan
from engine.kalender_cina import SHIO_URUT, pilar_hari  # noqa
from engine.rotation import today_wib
from engine.shio import _shio_dari_tahun, hitung_shio
from engine.weton import _NEPTU_HARI, _NEPTU_PASARAN, _PANCASUDA, hitung_weton
from engine.zodiak import hitung_zodiak

# ─────────────── tabel skor ───────────────
RUMAH_SKOR = {1: 80, 2: 68, 3: 72, 4: 58, 5: 88, 6: 52, 7: 76, 8: 40, 9: 85, 10: 84, 11: 87, 12: 36}
RUMAH_INFO = {
    1: "Bulan di rumah dirimu: mood dan kepercayaan diri jadi pusat hari ini.",
    2: "Bulan di rumah keuangan: urusan uang dan rasa aman lagi sensitif tapi produktif.",
    3: "Bulan di rumah komunikasi: enak buat ngobrol, nulis, dan belajar hal ringan.",
    4: "Bulan di rumah privat: energi condong ke rumah dan keluarga, kurang cocok ngoyo di luar.",
    5: "Bulan di rumah kreativitas: ide, hiburan, dan romansa lagi mengalir.",
    6: "Bulan di rumah rutinitas: banyak detail dan kerjaan teknis, mudah capek kalau dipaksa.",
    7: "Bulan di rumah relasi: interaksi dan kerja sama jadi sorotan hari ini.",
    8: "Bulan di rumah transformasi: emosi lebih dalam, hindari keputusan impulsif.",
    9: "Bulan di rumah wawasan: pikiran terbuka, bagus buat belajar dan rencana jangka panjang.",
    10: "Bulan di rumah karier: kerjaan dan reputasi lagi terlihat orang.",
    11: "Bulan di rumah komunitas: dukungan teman dan jaringan lagi kuat.",
    12: "Bulan di rumah istirahat: energi tertutup, cocok buat recharge, bukan ekspansi.",
}

# cabang bumi: 0=Zi/Tikus ... 11=Hai/Babi
_LIU_HE = {frozenset(p) for p in [(0, 1), (2, 11), (3, 10), (4, 9), (5, 8), (6, 7)]}
_SAN_HE = [{8, 0, 4}, {11, 3, 7}, {2, 6, 10}, {5, 9, 1}]
_HAI = {frozenset(p) for p in [(0, 7), (1, 6), (2, 5), (3, 4), (8, 11), (9, 10)]}
RELASI_SKOR = {"liu_he": 92, "san_he": 85, "netral": 65, "sama": 60, "hai": 38, "chong": 25}
RELASI_INFO = {
    "liu_he": "Hari ini 'berpasangan' dengan shiomu (Liu He): urusan terasa dimudahkan orang sekitar.",
    "san_he": "Hari ini sejalan dengan shiomu (San He): kolaborasi dan dukungan mengalir.",
    "netral": "Hari ini netral terhadap shiomu: hasil ikut usahamu sendiri.",
    "sama": "Hari ini sesama shiomu (Fu Yin): energi terasa 'itu-itu lagi', jaga supaya tidak stagnan.",
    "hai": "Hari ini 'merugikan' shiomu (Hai): rawan salah paham kecil, cek ulang ucapan dan janji.",
    "chong": "Hari ini bentrok dengan shiomu (Chong): rawan gesekan dan perubahan mendadak, pelan-pelan saja.",
}

PANCA_SKOR = {"Sri": 90, "Lungguh": 80, "Gedhong": 80, "Loro": 45, "Pati": 38}
PANCA_INFO = {
    "Sri": "Neptu hari ini selaras denganmu (Sri): rezeki dan penerimaan orang lagi bagus.",
    "Lungguh": "Neptu hari ini (Lungguh) mendukung wibawa dan posisi: bagus buat tampil dan memimpin.",
    "Gedhong": "Neptu hari ini (Gedhong) menarik kecukupan: bagus buat urusan materi dan merapikan aset.",
    "Loro": "Neptu hari ini (Loro) menguji kesabaran: jaga fisik, jangan memaksakan diri.",
    "Pati": "Neptu hari ini (Pati) berat: banyak yang menguras tenaga, pilih yang penting saja.",
}

NUM_SKOR = {1: 85, 2: 60, 3: 80, 4: 65, 5: 75, 6: 78, 7: 55, 8: 88, 9: 62}
NUM_INFO = {
    1: "Personal day 1: awal baru, cocok memulai dan mengambil inisiatif.",
    2: "Personal day 2: kerja sama dan kepekaan, pelan tapi harmonis.",
    3: "Personal day 3: ekspresi dan sosial, bagus buat komunikasi dan ide.",
    4: "Personal day 4: disiplin dan struktur, cocok membereskan pekerjaan yang tertunda.",
    5: "Personal day 5: perubahan dan fleksibilitas, siap dengan kejutan.",
    6: "Personal day 6: tanggung jawab dan relasi dekat, urus orang tersayang.",
    7: "Personal day 7: refleksi, butuh waktu sendiri dan mikir tenang.",
    8: "Personal day 8: kekuatan dan hasil, bagus buat bisnis dan keputusan keuangan.",
    9: "Personal day 9: menutup siklus, lepaskan yang sudah selesai.",
}

BOBOT = {"Zodiak": 0.25, "Shio": 0.25, "Weton": 0.25, "Numerologi": 0.25}
TIERS = [(80, "Puncak", "Hari terbaikmu: tancap gas untuk hal penting."),
         (65, "Kuat", "Energi bagus: kerjakan prioritas utama lebih awal."),
         (50, "Stabil", "Energi cukup: jalani ritme normal, jangan overcommit."),
         (35, "Pelan", "Energi menurun: pilih satu hal penting dan sisanya santai."),
         (0, "Istirahat", "Hari untuk recharge: tunda keputusan besar, utamakan pulih.")]


def tier(score):
    for lo, nama, tip in TIERS:
        if score >= lo:
            return nama, tip
    return TIERS[-1][1], TIERS[-1][2]


# ─────────────── komponen per sistem ───────────────
def _relasi(a, b):
    if a == b:
        return "sama"
    if frozenset((a, b)) in _LIU_HE:
        return "liu_he"
    if (a - b) % 12 == 6:
        return "chong"
    if frozenset((a, b)) in _HAI:
        return "hai"
    if any(a in g and b in g for g in _SAN_HE):
        return "san_he"
    return "netral"


def shio_user_idx(tgl):
    try:
        nama = hitung_shio(tgl)["shio"]
    except ValueError:  # di luar tabel Imlek: pakai tahun biasa (sebelum Imlek bisa meleset 1 shio)
        nama = _shio_dari_tahun(tgl.year)
    return SHIO_URUT.index(nama.lower())


def komponen(tgl_lahir, d=None):
    """Dict per sistem: skor, kunci, info. d = tanggal acuan (default hari ini WIB)."""
    d = d or today_wib()
    sign = hitung_zodiak(tgl_lahir)["sign"]
    h = rumah(sign, tanda_bulan(d))
    rel = _relasi(pilar_hari(d)[1], shio_user_idx(tgl_lahir))
    nep = hitung_weton(tgl_lahir)["neptu"] + _NEPTU_HARI[_hari(d)] + _NEPTU_PASARAN[hitung_weton(d)["pasaran"]]
    panca = _PANCASUDA[nep % 5][0]
    pm = periodic.personal_month(tgl_lahir, d.year, d.month)
    pd = periodic._reduksi(pm + d.day)
    return {
        "Zodiak": {"skor": RUMAH_SKOR[h], "kunci": h, "info": RUMAH_INFO[h]},
        "Shio": {"skor": RELASI_SKOR[rel], "kunci": rel, "info": RELASI_INFO[rel]},
        "Weton": {"skor": PANCA_SKOR[panca], "kunci": panca, "info": PANCA_INFO[panca]},
        "Numerologi": {"skor": NUM_SKOR[pd], "kunci": pd, "info": NUM_INFO[pd]},
    }


def _hari(d):
    return ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"][d.weekday()]


def skor_energi(tgl_lahir, d=None):
    """Skor 0-100 (rata-rata berbobot, diregangkan supaya rentang 0-100 terpakai) + rincian."""
    d = d or today_wib()
    k = komponen(tgl_lahir, d)
    mean = sum(k[s]["skor"] * BOBOT[s] for s in k)
    skor = int(round(max(5, min(98, 58 + (mean - 66) * 1.5))))
    nama, tip = tier(skor)
    return {"tanggal": d, "skor": skor, "tier": nama, "tip": tip, "komponen": k}


# ─────────────── afirmasi (gabungan 4 sistem) ───────────────
AFF_NUM = {
    1: "Aku berani memulai dari satu langkah kecil, tanpa menunggu semuanya sempurna.",
    2: "Aku mendengarkan dengan tenang, dan kerja samaku membuat semuanya lebih ringan.",
    3: "Aku mengungkapkan ide dan perasaanku dengan jujur, dan aku layak didengar.",
    4: "Aku membangun hasil lewat kebiasaan rapi yang kujaga satu per satu.",
    5: "Aku luwes menghadapi perubahan, dan setiap kejutan jadi ruang belajar.",
    6: "Aku merawat orang-orang terdekat tanpa melupakan kebutuhanku sendiri.",
    7: "Aku memberi diriku waktu hening untuk mendengar jawaban yang sudah ada di dalam.",
    8: "Aku mengambil keputusan dengan yakin, dan aku siap menerima hasil dari usahaku.",
    9: "Aku melepaskan yang sudah selesai dengan lega, supaya ada tempat untuk yang baru.",
}
AFF_ACT = {
    1: "Mulai satu hal yang sudah lama kamu tunda, cukup 10 menit pertama.",
    2: "Kirim satu pesan apresiasi ke orang yang kamu andalkan.",
    3: "Tulis atau ceritakan satu ide yang lagi kamu pikirkan ke seseorang.",
    4: "Bereskan satu tugas kecil yang menggantung dan coret dari daftar.",
    5: "Coba satu rute, cara, atau kebiasaan baru yang beda dari biasanya.",
    6: "Luangkan 15 menit penuh perhatian untuk orang terdekat, tanpa gawai.",
    7: "Duduk 10 menit tanpa layar, lalu catat satu hal yang paling kamu rasakan.",
    8: "Ambil satu keputusan yang tertunda soal uang atau pekerjaan, lalu eksekusi.",
    9: "Hapus atau rapikan satu hal yang sudah tidak kamu butuhkan.",
}
AFF_RUMAH = {
    1: "Aku boleh menjadi pusat perhatianku sendiri hari ini dan percaya pada instingku.",
    2: "Aku cukup, dan rasa aman kubangun dari hal-hal yang sudah kupunya.",
    3: "Aku berbicara dengan jernih, dan aku siap belajar dari siapa pun yang kutemui.",
    4: "Aku menjaga rumah dan batinku sebagai tempat pulang yang hangat.",
    5: "Aku memberi ruang untuk bermain, berkarya, dan menikmati prosesnya.",
    6: "Aku menjalani rutinitas dengan sabar, satu hal selesai satu hal.",
    7: "Aku terbuka pada hubungan yang saling menghargai dan seimbang.",
    8: "Aku berani jujur pada perasaanku, dan tidak terburu-buru memutuskan.",
    9: "Aku terus memperluas pandanganku, dan hari ini adalah bagian dari perjalanan panjang.",
    10: "Aku layak dilihat atas kerja kerasku, dan aku melangkah dengan tujuan jelas.",
    11: "Aku dikelilingi orang yang mendukungku, dan aku pun mendukung mereka.",
    12: "Aku boleh berhenti sejenak untuk memulihkan diri tanpa rasa bersalah.",
}
AFF_SHIO = {
    "liu_he": ["Aku terbuka menerima bantuan, dan orang yang pas datang di waktu yang pas.",
               "Aku melangkah ringan, karena hari ini banyak jalan yang terbuka."],
    "san_he": ["Aku bekerja bersama orang lain dengan percaya diri, dan tim kami saling menguatkan.",
               "Aku menjadi bagian dari lingkaran yang membuatku bertumbuh."],
    "netral": ["Aku mengandalkan usahaku sendiri, dan itu sudah cukup kuat.",
               "Aku menjalani hari dengan seimbang, tanpa terlalu berharap atau cemas."],
    "sama": ["Aku mengenali pola lamaku dan memilih satu hal baru untuk dicoba hari ini.",
             "Aku menyegarkan caraku, supaya hari yang sama tidak terasa membosankan."],
    "hai": ["Aku memilih kata dengan hati-hati, dan aku memeriksa ulang sebelum berjanji.",
            "Aku menjaga ketenangan saat ada salah paham kecil, dan menyelesaikannya dengan kepala dingin."],
    "chong": ["Aku tetap tenang di tengah perubahan mendadak, dan memilih respons yang bijak.",
              "Aku tidak menanggapi gesekan dengan emosi, dan memilih jalan yang damai."],
}
AFF_WETON = {
    "Sri": "Aku terbuka pada rezeki dan kebaikan yang datang lewat jalan yang tidak kuduga.",
    "Lungguh": "Aku pantas dipercaya, dan aku memimpin dengan rendah hati.",
    "Gedhong": "Aku mengelola yang kupunya dengan bijak, dan kecukupan datang dari ketekunan.",
    "Loro": "Aku sabar pada tubuh dan pikiranku, dan beristirahat adalah bagian dari kemajuan.",
    "Pati": "Aku memilih yang paling penting saja, dan aku tahan banting meski hari terasa berat.",
}


def afirmasi(tgl_lahir, d=None):
    """Afirmasi gabungan: kalimat utama (Numerologi) + fokus (Zodiak) + nuansa (Shio) + penutup (Weton)."""
    d = d or today_wib()
    k = komponen(tgl_lahir, d)
    shio_opts = AFF_SHIO[k["Shio"]["kunci"]]
    kalimat = [AFF_NUM[k["Numerologi"]["kunci"]], AFF_RUMAH[k["Zodiak"]["kunci"]],
               shio_opts[d.toordinal() % len(shio_opts)], AFF_WETON[k["Weton"]["kunci"]]]
    return {"tanggal": d, "kalimat": kalimat, "langkah": AFF_ACT[k["Numerologi"]["kunci"]],
            "sumber": {"Numerologi": f"Personal day {k['Numerologi']['kunci']}",
                       "Zodiak": f"Bulan di rumah {k['Zodiak']['kunci']}",
                       "Shio": k["Shio"]["kunci"].replace("_", " ").title(),
                       "Weton": k["Weton"]["kunci"]}}
