"""
Career DNA + Strength & Blind Spot (Batch 4). Lapisan skor RIASEC (Holland) dari hasil kuesioner 4 sistem
(MBTI, Big Five, DISC, Enneagram) + teks dari library yang sudah ada (content/blueprint_calc._blocks).

Pemetaan sistem -> RIASEC adalah bobot interpretasi kita, disusun dari pola korelasi yang umum dilaporkan
(mis. Larson dkk. 2002 untuk Big Five x RIASEC; Holland 1997; korelasi MBTI-Holland dari Myers-Briggs Foundation).
BUKAN diagnosis psikologis dan bukan hasil validasi statistik di data kita.
"""

import hashlib
from datetime import date

from content import blueprint_calc as BC
from content import baru_loader as BL
from content.blueprint_calc import _blocks, _kal
from content.result_builder import compute_raw_result

QUIZ_SYSTEMS = ["MBTI", "Big Five", "Enneagram", "DISC"]
LETTERS = "RIASEC"
BIRTH = ["Zodiak", "Shio", "Weton", "Numerologi"]
# rata-rata share (%) hasil jawaban acak 600x (R,I,A,S,E,C), dipakai sebagai garis dasar
BASE = [12.2, 12.6, 16.2, 21.8, 20.5, 16.7]
SYS_W = {"MBTI": 0.30, "Big Five": 0.30, "DISC": 0.20, "Enneagram": 0.20}

# (R, I, A, S, E, C) per kutub MBTI
_V = lambda **k: [k.get(l, 0.0) for l in LETTERS]
_MBTI = {"E": _V(S=.35, E=.45, A=.10, C=.10), "I": _V(R=.20, I=.40, A=.25, C=.15),
         "S": _V(R=.35, C=.35, S=.15, E=.15), "N": _V(I=.35, A=.35, S=.15, E=.15),
         "T": _V(I=.30, E=.30, R=.25, C=.15), "F": _V(S=.45, A=.35, C=.10, E=.10),
         "J": _V(C=.40, E=.30, R=.15, S=.15), "P": _V(A=.30, I=.25, R=.25, S=.10, E=.10)}
_PAIRS = [("E", "I"), ("S", "N"), ("T", "F"), ("J", "P")]
_B5 = {"O": _V(I=.30, A=.48, S=.10, E=.12), "C": _V(R=.10, E=.18, C=.30, S=.10),
       "E": _V(E=.41, S=.30, A=.15), "A": _V(S=.40, C=.10)}
_B5_LOW_O = _V(R=.15, C=.15)
_DISC = {"D": _V(E=.50, R=.25, I=.15, A=.10), "I": _V(S=.35, E=.30, A=.30, C=.05),
         "S": _V(S=.45, C=.30, R=.15, A=.10), "C": _V(C=.40, I=.30, R=.20, E=.10)}
_ENN = {1: _V(C=.35, E=.20, S=.20, R=.15, I=.10), 2: _V(S=.60, E=.15, A=.10, C=.15),
        3: _V(E=.55, S=.15, C=.15, A=.15), 4: _V(A=.60, S=.20, I=.20), 5: _V(I=.55, R=.25, C=.20),
        6: _V(C=.35, S=.30, I=.15, R=.20), 7: _V(A=.30, E=.30, S=.20, I=.20),
        8: _V(E=.55, R=.30, S=.10, C=.05), 9: _V(S=.40, C=.25, A=.15, R=.20)}


def _norm(v):
    s = sum(v) or 1.0
    return [x / s for x in v]


def _add(acc, v, w):
    for i, x in enumerate(v):
        acc[i] += x * w


def _vec_mbti(raw):
    c, acc = raw.get("counts") or {}, [0.0] * 6
    for a, b in _PAIRS:
        tot = (c.get(a, 0) + c.get(b, 0)) or 1
        p = c.get(a, 0) / tot
        _add(acc, _MBTI[a], p / 4)
        _add(acc, _MBTI[b], (1 - p) / 4)
    return _norm(acc)


def _vec_b5(raw):
    sc, acc = raw.get("scores") or {}, [0.0] * 6
    p = {t: max(0.0, min(1.0, (sc.get(t, 21) - 7) / 28)) for t in "OCEAN"}
    for t, w in _B5.items():
        _add(acc, w, p[t])
    _add(acc, _B5_LOW_O, 1 - p["O"])
    return _norm(acc)


def _vec_counts(raw, table):
    c = raw.get("counts") or {}
    tot = sum(c.values()) or 1
    acc = [0.0] * 6
    for k, n in c.items():
        _add(acc, table[k], n / tot)
    return _norm(acc)


def riasec(raws):
    """{R..C: 0-100} relatif (huruf tertinggi = 100) + share (jumlah 100)."""
    acc, used = [0.0] * 6, 0.0
    parts = {"MBTI": _vec_mbti, "Big Five": _vec_b5, "DISC": lambda r: _vec_counts(r, _DISC),
             "Enneagram": lambda r: _vec_counts(r, _ENN)}
    for s, fn in parts.items():
        r = raws.get(s)
        if r and not r.get("placeholder"):
            _add(acc, fn(r), SYS_W[s])
            used += SYS_W[s]
    if not used:
        return None
    share = [x / used for x in acc]
    idx = [x / (b / 100) for x, b in zip(share, BASE)]  # dibanding rata-rata penjawab acak -> tidak bias ke S/E
    top = max(idx) or 1.0
    return {"rel": {l: round(x / top * 100) for l, x in zip(LETTERS, idx)},
            "share": {l: round(x * 100, 1) for l, x in zip(LETTERS, share)}}


# ─────────────── teks karier per huruf RIASEC ───────────────
NOUN = {"R": "Pembangun", "I": "Analis", "A": "Kreator", "S": "Pembina", "E": "Penggerak", "C": "Pengatur"}
ADJ = {"R": "praktis", "I": "analitis", "A": "kreatif", "S": "peduli", "E": "ambisius", "C": "terstruktur"}
LETTER = {
    "R": {"nama": "Realistic · Pembangun", "inti": "Kamu paling hidup saat bekerja dengan hal nyata: alat, sistem, tempat, atau proses yang hasilnya bisa dilihat dan dipegang.",
          "lingkungan": "Lingkungan yang jelas aturannya, banyak kerja langsung, sedikit rapat basa-basi, dan ukuran sukses yang konkret.",
          "motivasi": "Menyelesaikan sesuatu yang berfungsi, kemandirian teknis, dan hasil yang terukur.",
          "peran": ["Teknisi / Insinyur lapangan", "Operasional & logistik", "Arsitek / Drafter / Surveyor", "Manajer produksi / manufaktur",
                    "Teknisi IT & jaringan", "Pilot / Teknisi penerbangan", "Chef / Food technologist", "Kontraktor & renovasi",
                    "Teknisi energi terbarukan", "Quality control lapangan"],
          "industri": ["Manufaktur", "Konstruksi & properti", "Logistik", "Energi", "Otomotif", "Teknologi hardware"],
          "aksi": ["Pilih satu proyek nyata 2 minggu yang hasil akhirnya bisa kamu tunjukkan (bukan laporan).",
                   "Dokumentasikan satu proses kerjamu jadi SOP satu halaman supaya keahlianmu terlihat.",
                   "Cari satu sertifikasi teknis yang diakui industri dan jadwalkan ujiannya.",
                   "Latih satu kebiasaan komunikasi: update progres singkat tiap hari ke atasan atau tim."]},
    "I": {"nama": "Investigative · Analis", "inti": "Kamu menikmati memahami cara kerja sesuatu: mencari pola, menguji gagasan, dan menyelesaikan masalah yang kompleks dengan data dan logika.",
          "lingkungan": "Ruang yang memberi waktu fokus mendalam, otonomi menentukan metode, dan rekan yang menghargai argumen berdasar bukti.",
          "motivasi": "Rasa ingin tahu, penguasaan keahlian, dan masalah sulit yang belum ada jawabannya.",
          "peran": ["Data analyst / Data scientist", "Peneliti / Research analyst", "Software engineer / Arsitek sistem", "Konsultan strategi",
                    "Analis keuangan & investasi", "Product analyst", "Ilmuwan / Teknisi laboratorium", "Analis risiko & kebijakan",
                    "Dokter / Profesional medis spesialis", "Auditor investigatif"],
          "industri": ["Teknologi & data", "Keuangan & investasi", "Riset & pendidikan tinggi", "Kesehatan", "Konsultansi", "Regulasi & kebijakan"],
          "aksi": ["Kerjakan satu studi kasus mini dari data nyata dan tulis kesimpulannya dalam satu halaman.",
                   "Bagikan satu temuanmu ke orang non-teknis dengan bahasa sederhana (latih penerjemahan insight).",
                   "Tentukan batas waktu riset: keputusan diambil saat data mencapai 80%, bukan 100%.",
                   "Gabung satu komunitas atau forum profesi untuk menguji ide dengan orang lain."]},
    "A": {"nama": "Artistic · Kreator", "inti": "Kamu bekerja terbaik saat boleh mengekspresikan ide orisinal: membuat, merancang, menulis, atau menyusun konsep yang belum ada sebelumnya.",
          "lingkungan": "Struktur longgar, ruang bereksperimen, apresiasi atas gaya personal, dan tenggat yang jelas tapi tidak mencekik.",
          "motivasi": "Ekspresi diri, kebaruan, dan melihat karya yang membawa tanda tanganmu.",
          "peran": ["UX / UI / Product designer", "Content creator & copywriter", "Brand & creative strategist", "Art director / Desainer grafis",
                    "Videografer / Editor / Produser", "Arsitek & desainer interior", "Game / Experience designer", "Jurnalis & editor",
                    "Desainer produk / fesyen", "Musisi / Sound designer"],
          "industri": ["Media & hiburan", "Branding & periklanan", "Teknologi produk", "Fesyen & desain", "Pendidikan kreatif", "Gaming"],
          "aksi": ["Bangun portofolio 3 karya terbaik dan tampilkan di satu halaman publik minggu ini.",
                   "Pasang tenggat sendiri untuk satu karya kecil tiap minggu agar ide jadi hasil.",
                   "Cari satu mentor atau komunitas kreator untuk meminta kritik terstruktur.",
                   "Latih menjelaskan nilai bisnis dari karyamu (siapa yang terbantu dan seberapa besar)."]},
    "S": {"nama": "Social · Pembina", "inti": "Energimu datang dari membantu orang lain bertumbuh: mengajar, mendampingi, menjembatani, dan membuat orang merasa didengar.",
          "lingkungan": "Tim yang hangat, kontak langsung dengan orang, misi yang bermakna, dan budaya saling mendukung.",
          "motivasi": "Dampak nyata pada orang lain, hubungan yang tulus, dan rasa menjadi bagian dari sesuatu.",
          "peran": ["HR / People & culture", "Guru / Trainer / Fasilitator", "Konselor / Coach / Mentor", "Customer success manager",
                    "Perawat / Tenaga kesehatan", "Pekerja sosial / Program NGO", "Community manager", "Talent acquisition",
                    "Learning & development", "Public relations"],
          "industri": ["Pendidikan", "Kesehatan", "Layanan sosial & NGO", "SDM & rekrutmen", "Layanan pelanggan", "Komunitas & media sosial"],
          "aksi": ["Jadwalkan satu sesi mentoring atau pendampingan rutin dan catat dampaknya.",
                   "Tetapkan batas jam kerja emosional supaya energimu tidak habis untuk semua orang.",
                   "Pelajari satu kerangka coaching (mis. GROW) agar bantuanmu lebih terarah.",
                   "Minta umpan balik tertulis dari orang yang pernah kamu bantu untuk bahan portofolio."]},
    "E": {"nama": "Enterprising · Penggerak", "inti": "Kamu tumbuh saat memimpin, meyakinkan, dan mengambil risiko terukur untuk mencapai target yang ambisius.",
          "lingkungan": "Target jelas, wewenang mengambil keputusan, insentif atas hasil, dan tim yang bergerak cepat.",
          "motivasi": "Pencapaian, pengaruh, kompetisi sehat, dan imbalan yang sebanding dengan hasil.",
          "peran": ["Founder / Wirausahawan", "Business development & sales lead", "Product / Program manager", "General manager / Kepala unit",
                    "Marketing & growth lead", "Konsultan bisnis", "Venture / Investor relations", "Agen properti & broker",
                    "Politik, advokasi & negosiator", "Corporate strategy"],
          "industri": ["Startup & venture", "Penjualan & ritel", "Properti", "Keuangan & investasi", "Media & pemasaran", "Konsultansi"],
          "aksi": ["Tetapkan satu target angka 90 hari dan pecah jadi 3 milestone mingguan.",
                   "Rekrut atau cari satu orang detail-oriented untuk menutup celah eksekusimu.",
                   "Uji satu ide bisnis kecil dalam 14 hari tanpa modal besar (validasi dulu).",
                   "Latih mendengarkan: di tiap rapat, tanya dua pertanyaan sebelum menyampaikan keputusan."]},
    "C": {"nama": "Conventional · Pengatur", "inti": "Kamu unggul menjaga keteraturan: data rapi, proses konsisten, dan detail yang tidak terlewat sehingga orang lain bisa mengandalkanmu.",
          "lingkungan": "Aturan dan ekspektasi yang jelas, alur kerja stabil, prioritas yang tidak berubah-ubah, dan tugas yang bisa diselesaikan tuntas.",
          "motivasi": "Ketepatan, keandalan, kestabilan, dan penghargaan atas ketelitian.",
          "peran": ["Akuntan / Auditor", "Project coordinator / PMO", "Operations & process manager", "Administrator & office manager",
                    "Analis kepatuhan & manajemen risiko", "Financial controller", "Supply chain planner", "Database & sistem administrator",
                    "Legal / Contract administrator", "Quality assurance"],
          "industri": ["Keuangan & perbankan", "Pemerintahan & BUMN", "Asuransi", "Manufaktur & rantai pasok", "Hukum & kepatuhan", "Kesehatan administratif"],
          "aksi": ["Rapikan satu proses yang selama ini berantakan jadi checklist dan bagikan ke tim.",
                   "Ambil satu kewenangan keputusan kecil yang biasanya kamu serahkan ke atasan.",
                   "Pelajari satu alat otomasi (spreadsheet lanjutan, otomasi alur kerja) untuk menghemat jam rutin.",
                   "Latih toleransi ambigu: kerjakan satu hal baru tanpa instruksi lengkap dan catat hasilnya."]},
}


def archetype(r):
    order = sorted(LETTERS, key=lambda l: (-r["rel"][l], LETTERS.index(l)))
    code = "".join(order[:3])
    return {"order": order, "code": code, "nama": f"{NOUN[order[0]]} yang {ADJ[order[1]].title()}",
            "tipis": r["rel"][order[2]] - r["rel"][order[3]] < 5}


def roles(order):
    """10 peran: 5 dari huruf teratas, 3 dari kedua, 2 dari ketiga (tanpa duplikat)."""
    out = []
    for letter, n in ((order[0], 5), (order[1], 3), (order[2], 2)):
        out += [x for x in LETTER[letter]["peran"] if x not in out][:n]
    return out


# ─────────────── kekuatan & titik buta ───────────────
STRENGTH_TAG = {"R": ["Eksekusi nyata", "Mandiri secara teknis", "Tenang di lapangan"],
                "I": ["Berpikir analitis", "Cepat menangkap pola", "Menguasai topik mendalam"],
                "A": ["Ide orisinal", "Peka estetika & makna", "Fleksibel dalam cara"],
                "S": ["Empati & mendengarkan", "Membangun kepercayaan", "Membuat orang berkembang"],
                "E": ["Berani memimpin", "Meyakinkan orang", "Berorientasi hasil"],
                "C": ["Teliti & rapi", "Dapat diandalkan", "Disiplin menyelesaikan"]}
# Titik buta per kutub Big Five (level) dan DISC dominan (label singkat untuk kartu + kalimat gejala + penawar)
B5_BLIND = {
    ("O", "Tinggi"): ("Banyak ide, sedikit tuntas", "Mudah beralih ke gagasan baru sebelum yang lama rampung.", "Pilih 1 ide per bulan untuk diselesaikan sampai ada hasil yang bisa dilihat orang."),
    ("O", "Rendah"): ("Berat menerima cara baru", "Cenderung bertahan pada cara lama walau ada opsi yang lebih efisien.", "Uji satu cara baru per minggu pada tugas berisiko rendah."),
    ("C", "Tinggi"): ("Perfeksionis & kaku", "Standar tinggi bisa membuat pekerjaan lambat dan sulit mendelegasikan.", "Tetapkan 'cukup baik' 85% untuk pekerjaan rutin, sisakan 100% untuk yang krusial."),
    ("C", "Rendah"): ("Mudah menunda detail", "Detail dan tenggat bisa terlewat karena fokus pada gambaran besar.", "Pakai satu daftar harian maksimal 3 prioritas dan cek tiap sore."),
    ("E", "Tinggi"): ("Dominan di percakapan", "Antusiasme bisa menutup ruang bicara orang yang lebih pendiam.", "Tanya satu pertanyaan dan tunggu 5 detik sebelum bicara lagi di rapat."),
    ("E", "Rendah"): ("Kurang terlihat", "Hasil kerja bagus bisa luput dari perhatian karena jarang dibicarakan.", "Kirim ringkasan hasil mingguan ke atasan atau tim dalam 3 kalimat."),
    ("A", "Tinggi"): ("Sulit berkata tidak", "Mengutamakan keharmonisan bisa membuatmu menyimpan keberatan sendiri.", "Latih kalimat 'Boleh aku pikirkan dulu?' sebelum menyetujui permintaan."),
    ("A", "Rendah"): ("Terlalu blak-blakan", "Ketegasan bisa terbaca sebagai dingin atau meremehkan.", "Awali masukan dengan satu hal yang berjalan baik sebelum menyampaikan kritik."),
    ("N", "Tinggi"): ("Mudah cemas & overthinking", "Tekanan kecil terasa besar dan menguras energi sebelum tindakan dimulai.", "Tulis kekhawatiran, lalu tandai mana yang bisa kamu kendalikan hari ini."),
    ("N", "Rendah"): ("Kurang waspada risiko", "Ketenangan tinggi bisa membuat sinyal bahaya dianggap remeh.", "Buat checklist risiko 3 poin sebelum keputusan besar."),
}
DISC_BLIND = {
    "D": ("Terlalu menekan & tidak sabar", "Tempo cepat dan tegas bisa membuat orang merasa didesak atau tidak didengar.", "Beri ruang 24 jam untuk keputusan non-urgent dan minta pendapat tim dulu."),
    "I": ("Janji banyak, tindak lanjut kurang", "Antusias di awal, detail dan tindak lanjut sering tertinggal.", "Catat setiap komitmen di satu tempat dan beri tanggal selesai."),
    "S": ("Menghindari konflik", "Menahan ketidaksetujuan demi suasana bisa membuat masalah menumpuk diam-diam.", "Sampaikan satu keberatan kecil per minggu dengan kalimat 'aku merasa...'"),
    "C": ("Analisis berlebihan", "Menunggu data sempurna bisa membuat keputusan terlambat.", "Tetapkan batas waktu riset dan putuskan dengan 80% informasi."),
}
# kekuatan yang bisa jadi bumerang (overuse), per DISC dominan
OVERUSE = {"D": "Ketegasanmu adalah kekuatan, tapi dipakai terus-menerus ia berubah jadi dominasi dan membuat tim berhenti memberi masukan.",
           "I": "Kehangatan dan pengaruhmu adalah kekuatan, tapi tanpa penutup yang rapi ia terasa seperti janji yang tidak ditepati.",
           "S": "Kesetiaan dan kesabaranmu adalah kekuatan, tapi tanpa batas ia berubah jadi menahan diri sampai lelah.",
           "C": "Ketelitianmu adalah kekuatan, tapi tanpa batas waktu ia berubah jadi perfeksionisme yang menunda hasil."}


# ─────────────── builder ───────────────
def trait_raws(answers, mode):
    """{sistem: raw} dari jawaban kuesioner {sistem: {id: val}}."""
    out = {}
    for s in QUIZ_SYSTEMS:
        try:
            out[s] = BC.quiz_raw(s, answers.get(s) or {}, mode)
        except Exception:
            out[s] = {}
    return out


def _birth_raws(prof):
    ld = {"tanggal_lahir": prof["tgl"], "jam_lahir": prof.get("jam"), "kota_lahir": prof.get("kota"),
          "nama_lengkap": prof["nama"]}
    out = {}
    for s in BIRTH:
        try:
            out[s] = compute_raw_result(s, ld)
        except Exception:
            out[s] = {}
    return out


def _sid(prof, pre):
    return f"{pre}-{hashlib.md5((prof['nama'] + str(prof['tgl'])).encode()).hexdigest()[:5].upper()}"


def _plan30(order):
    ak = LETTER[order[0]]["aksi"]
    return [("Minggu 1", ak[0]), ("Minggu 2", ak[1]), ("Minggu 3", ak[2]), ("Minggu 4", ak[3])]


def build_career(prof, raws, mode):
    r = riasec(raws)
    if not r:
        return None
    a = archetype(r)
    o = a["order"]
    sistem, sinyal = [], []
    for s in QUIZ_SYSTEMS:
        b = _blocks(s, raws.get(s) or {})
        if b and b.get("karier"):
            sistem.append({"name": s, "icon": BC.ICON[s], "title": b["title"],
                           "teks": BL.career_baru("career", f"{s}|{b['key']}") or _kal(b["karier"][0], 2, 360)})
    for s, raw in _birth_raws(prof).items():
        b = _blocks(s, raw)
        if b and b.get("karier"):
            sinyal.append({"name": s, "icon": BC.ICON[s], "title": b["title"],
                           "teks": BL.career_baru("career", f"{s}|{b['key']}") or _kal(b["karier"][0], 2, 320)})
    L = LETTER[o[0]]
    return {"id": _sid(prof, "CD"), "nama": prof["nama"], "mode": mode, "rel": r["rel"], "share": r["share"], "order": o,
            "code": a["code"], "arketipe": a["nama"], "tipis": a["tipis"], "inti": L["inti"], "lingkungan": L["lingkungan"],
            "motivasi": L["motivasi"], "kedua": LETTER[o[1]]["nama"], "peran": roles(o),
            "industri": (L["industri"][:4] + LETTER[o[1]]["industri"][:2]), "sistem": sistem, "sinyal": sinyal,
            "plan": _plan30(o), "tags": {k: LETTER[k]["nama"] for k in LETTERS}}


def build_strength(prof, raws, mode):
    r = riasec(raws)
    if not r:
        return None
    o = archetype(r)["order"]
    kuat, blind, seen = [], [], set()
    for s in QUIZ_SYSTEMS:  # kekuatan dari teks library per sistem
        b = _blocks(s, raws.get(s) or {})
        if b and b.get("kuat"):
            kuat.append({"name": s, "icon": BC.ICON[s], "title": b["title"],
                         "teks": BL.career_baru("strength", f"{s}|{b['key']}|kuat") or _kal(b["kuat"][0], 2, 300)})
    tags = []
    for l in o[:3]:
        tags += [t for t in STRENGTH_TAG[l] if t not in tags][:2 if l == o[0] else 1]
    b5 = raws.get("Big Five") or {}
    lv = b5.get("levels") or {}
    for t in "OCEAN":
        key = (t, lv.get(t))
        if key in B5_BLIND:
            blind.append(("Big Five", t, *B5_BLIND[key]))
    d = raws.get("DISC") or {}
    dom = d.get("tipe")
    if dom in DISC_BLIND:
        blind.insert(0, ("DISC", dom, *DISC_BLIND[dom]))
    for s in ("MBTI", "Enneagram"):
        b = _blocks(s, raws.get(s) or {})
        if b and b.get("shadow"):
            blind.append((s, b["title"], b["title"] or s,
                          BL.career_baru("strength", f"{s}|{b['key']}|blindspot") or _kal(b["shadow"][0], 2, 300), ""))
    blind = blind[:5]
    practice = []
    for s in QUIZ_SYSTEMS:
        b = _blocks(s, raws.get(s) or {})
        if b and b.get("nasihat"):
            practice.append({"name": s, "icon": BC.ICON[s],
                             "teks": BL.career_baru("strength", f"{s}|{b['key']}|latihan") or _kal(b["nasihat"][0], 2, 260)})
    bars = {}
    if b5.get("scores"):
        names = {"O": "Keterbukaan", "C": "Ketelitian", "E": "Ekstraversi", "A": "Keramahan", "N": "Sensitivitas Emosi"}
        bars["ocean"] = [(names[t], round((b5["scores"].get(t, 21) - 7) / 28 * 100)) for t in "OCEAN"]
    if d.get("counts"):
        tot = sum(d["counts"].values()) or 1
        dn = {"D": "D · Dominan", "I": "I · Influence", "S": "S · Steady", "C": "C · Conscientious"}
        bars["disc"] = [(dn.get(k, k), round(v / tot * 100)) for k, v in d["counts"].items()]
    return {"id": _sid(prof, "SB"), "nama": prof["nama"], "mode": mode, "tags": tags[:6], "kuat": kuat, "blind": blind,
            "overuse": OVERUSE.get(dom, ""), "practice": practice, "bars": bars, "rel": r["rel"], "order": o,
            "disc": dom, "mbti": (raws.get("MBTI") or {}).get("tipe"), "enn": (raws.get("Enneagram") or {}).get("tipe")}
