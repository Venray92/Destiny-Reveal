"""
Penggabungan variabel per sistem (12 sistem; BaZi, Golongan Darah, Tarot cuma punya 1 variabel jadi tanpa combo):
Zodiak, Shio, Numerologi, Matrix Destiny, Weton, Zi Wei, Human Design, MBTI, Big Five, Enneagram, DISC, Love Language.

Fragmen teks dibaca dari content/interpretations/<folder>/<folder>_combo.json.
Antar-fragmen disambung kata hubung (rotasi deterministik, tidak berulang dalam
satu blok), saran dipilih dinamis dari bobot/relasi indikator. Kalau data kurang
atau file JSON belum ada, build_combo() balikin [] dan detail tampil seperti biasa.
"""

import json
from functools import lru_cache
from pathlib import Path

_DIR = Path(__file__).resolve().parent.parent / "content" / "interpretations"
_FOLDER = {"Zodiak": "zodiak", "Shio": "shio", "Numerologi": "numerologi", "Matrix Destiny": "matrix_destiny",
           "Weton": "weton", "Zi Wei": "ziwei", "Human Design": "human_design", "MBTI": "mbti",
           "Big Five": "big_five", "Enneagram": "enneagram", "DISC": "disc", "Love Language": "love_language"}

# Kata awal yang JANGAN di-lowercase setelah kata hubung.
_KEEP = ("Life Path", "Soul Urge", "Expression", "Personality", "Matahari", "Bulan", "Shio")

CONN = {
    "tambah": ["Sementara itu,", "Pada saat yang sama,", "Selain itu,"],
    "lanjut": ["Selain itu,", "Di samping itu,", "Ditambah lagi,", "Lebih jauh,"],
    "kontras": ["Di sisi lain,", "Namun,", "Meski begitu,"],
}


@lru_cache(maxsize=None)
def _data(system):
    folder = _FOLDER.get(system)
    if not folder:
        return {}
    try:
        with open(_DIR / folder / f"{folder}_combo.json", encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return {}


def _soft(s):
    """Huruf pertama kecil setelah kata hubung, kecuali istilah baku."""
    return s if s.startswith(_KEEP) else s[:1].lower() + s[1:]


def _seed(*parts):
    return sum(ord(c) for p in parts for c in str(p))


def _link(a, b, kind, seed, used, shift=0):
    """Sambung kalimat a dan b dengan kata hubung (rotasi deterministik).
    `used` = set kata hubung yang sudah dipakai di blok ini, supaya tidak berulang."""
    lst = CONN[kind]
    for i in range(len(lst)):
        c = lst[(seed + shift + i) % len(lst)]
        if c not in used:
            break
    used.add(c)
    return f"{a} {c} {_soft(b)}"


def _block(title, text):
    return {"title": title, "text": text}


# ── Numerologi ───────────────────────────────────────────────────
_MASTER = {11, 22, 33}


def _numerologi(raw, d):
    lp, su, ex, pe = (raw.get(k) for k in ("life_path", "soul_urge", "expression", "personality"))
    if None in (lp, su, ex, pe):
        return []
    g = lambda grp, n: d.get(grp, {}).get(str(n), "")
    if not all(g(x, n) for x, n in (("lp", lp), ("su", su), ("ex", ex), ("pe", pe))):
        return []
    rel, adv, s = d["relation"], d["advice"], _seed(lp, su, ex, pe)

    u = set()
    t1 = _link(f"Life Path {lp} menunjukkan jalan hidupmu: {g('lp', lp)}.",
               f"Soul Urge {su} menggambarkan dorongan terdalam hatimu, yaitu {g('su', su)}.", "tambah", s, u)
    if lp == su:
        t1 += " " + rel["sama"].format(a=lp)
    else:
        t1 = _link(t1, rel["beda"].format(a=lp, b=su), "kontras", s, u)
    if lp in _MASTER or su in _MASTER:
        t1 = _link(t1, rel["master"], "lanjut", s, u, 1)

    u = set()
    t2 = _link(f"Expression {ex} menunjukkan bakat yang kamu bawa ke dunia: kemampuan {g('ex', ex)}.",
               f"Personality {pe} menggambarkan kesan pertama yang orang tangkap darimu: {g('pe', pe)}.",
               "tambah", s, u, 1)
    if ex == pe:
        t2 += " " + rel["ex_sama"].format(a=ex)
    else:
        t2 = _link(t2, rel["ex_beda"].format(pe_tail=g("pe", pe), ex_tail=g("ex", ex)), "kontras", s, u, 1)

    master = any(n in _MASTER for n in (lp, su, ex, pe))
    t3 = _link(adv["master"] if master else adv["tunggal"],
               adv["selaras"] if (lp == su or ex == pe) else adv["tegang"], "lanjut", s, set())
    return [_block(f"Life Path {lp} × Soul Urge {su}", t1),
            _block(f"Expression {ex} × Personality {pe}", t2),
            _block("Saran sesuai Bobot Angkamu", t3)]


# ── Matrix Destiny ───────────────────────────────────────────────
def _matrix(raw, d):
    from engine.matrix_destiny import NAMA_ARKETIPE
    c = raw.get("titik_inti")
    lm = raw.get("love_money") or {}
    love, money = lm.get("love"), lm.get("money")
    main = (raw.get("purpose") or {}).get("main_destiny")
    if None in (c, love, money, main):
        return []
    grp, rel, adv, s = d["group"], d["relation"], d["advice"], _seed(c, love, money, main)
    nm = lambda n: f"{NAMA_ARKETIPE[n]} ({n})"
    core = d["core"][str(c)]

    def relation(n, label, hal):
        g1, g2 = grp[str(c)], grp[str(n)]
        if n == c:
            return rel["sama"].format(label=label, hal=hal)
        return rel["selaras"].format(g=g1) if g1 == g2 else rel["lengkap"].format(g1=g1, g2=g2)

    u = set()
    t1 = _link(f"Inti jiwamu adalah {nm(c)}, yaitu {core}.",
               f"Titik cintamu ada pada {nm(love)}: {d['love'][str(love)]}.", "tambah", s, u)
    t1 = _link(t1, relation(love, "cinta", "caramu mencintai"), "lanjut", s, u, 1)

    u = set()
    t2 = f"Titik uangmu ada pada {nm(money)}: {d['money'][str(money)]}."
    t2 = _link(t2, relation(money, "uang", "caramu mengelola uang"), "lanjut", s, u, 2)
    t2 = _link(t2, (adv["seimbang"].format(n=love) if love == money
                    else adv["beda"].format(l=love, m=money)), "lanjut", s, u)

    u = set()
    t3 = f"Tujuan hidup utamamu mengarah ke {nm(main)}: {d['purpose'][str(main)]}."
    t3 = _link(t3, relation(main, "tujuan", "arah hidupmu"), "lanjut", s, u, 1)
    t3 = _link(t3, adv["tujuan"], "lanjut", s, u, 2)
    return [_block("Inti Jiwa × Titik Cinta", t1), _block("Inti Jiwa × Titik Uang", t2),
            _block("Tujuan Hidup Utamamu", t3)]


# ── Shio ─────────────────────────────────────────────────────────
_YANG = {"Tikus", "Macan", "Naga", "Kuda", "Monyet", "Anjing"}


def _shio(raw, d):
    shio, e = raw.get("shio"), raw.get("elemen")
    if not shio or e not in d.get("elemen", {}):
        return []
    p = "Yang" if shio in _YANG else "Yin"
    el, s = d["elemen"][e], _seed(shio, e)
    u = set()
    t1 = _link(f"Sebagai Shio {shio} dengan elemen {e} pada tahun lahirmu, kamu cenderung {el['karakter']}.",
               d["polaritas"][p], "tambah", s, u)
    t1 = _link(t1, d["advice"][f"{e}|{p}"], "lanjut", s, u, 1)
    t2 = _link(f"Elemen {e} mendukungmu di {el['karier']}.",
               f"Dalam hubungan, kamu cenderung {el['hubungan']}.", "tambah", s, set(), 1)
    return [_block(f"Elemen {e} × Polaritas {p}", t1), _block(f"Karier & Hubungan dengan Elemen {e}", t2)]


# ── Zodiak (Matahari + Bulan) ────────────────────────────────────
_ELEMEN = {"Aries": "Api", "Leo": "Api", "Sagittarius": "Api",
           "Taurus": "Tanah", "Virgo": "Tanah", "Capricorn": "Tanah",
           "Gemini": "Udara", "Libra": "Udara", "Aquarius": "Udara",
           "Cancer": "Air", "Scorpio": "Air", "Pisces": "Air"}
_HARMONIS = {frozenset(("Api", "Udara")), frozenset(("Tanah", "Air"))}


def _zodiak(raw, d):
    sun, moon = raw.get("sign"), raw.get("moon_sign")
    if sun in d.get("sun", {}) and moon is None and "tanpa_bulan" in d:  # jam lahir kosong: Matahari saja
        tb, e = d["tanpa_bulan"], _ELEMEN[sun]
        return [_block(f"Matahari di {sun} × Unsur {e}",
                       _join(f"Matahari di {sun} membuatmu tampil ke dunia dengan {d['sun'][sun]}.", tb["elemen"][e])),
                _block("Saran untuk Perpaduan Matahari dan Unsurmu", _join(tb["saran"][e], tb["catatan"]))]
    if sun not in d.get("sun", {}) or moon not in d.get("moon", {}):
        return []
    e1, e2, rel, s = _ELEMEN[sun], _ELEMEN[moon], d["relation"], _seed(sun, moon)
    if sun == moon:
        kind, r = "kembar", rel["kembar"]
    elif e1 == e2:
        kind, r = "selaras", rel["selaras"].format(e=e1)
    elif frozenset((e1, e2)) in _HARMONIS:
        kind, r = "harmonis", rel["harmonis"].format(e1=e1, e2=e2)
    else:
        kind, r = "tegangan", rel["tegangan"].format(e1=e1, e2=e2)
    u = set()
    t1 = _link(f"Matahari di {sun} membuatmu tampil ke dunia dengan {d['sun'][sun]}.",
               f"Bulan di {moon} menunjukkan bahwa secara batin kamu {d['moon'][moon]}.", "tambah", s, u)
    t1 = _link(t1, r, "kontras" if kind == "tegangan" else "lanjut", s, u, 1)
    t2 = d["advice"][kind]
    if raw.get("moon_near_edge"):
        t2 += (" Posisi Bulanmu berada dekat batas dua tanda, jadi hasil ini paling akurat "
               "bila jam lahir yang kamu isi tepat.")
    return [_block(f"Matahari di {sun} × Bulan di {moon}", t1),
            _block("Saran untuk Perpaduan Matahari dan Bulanmu", t2)]


_BUILDERS = {"Numerologi": _numerologi, "Matrix Destiny": _matrix, "Shio": _shio, "Zodiak": _zodiak}


# ── Sistem lain: teks dibaca langsung per kombinasi, kalimat disambung spasi ──
def _join(*parts):
    return " ".join(p.strip() for p in parts if p and p.strip())


def _weton(raw, d):
    hari, pas, neptu = raw.get("hari"), raw.get("pasaran"), raw.get("neptu")
    psd = (raw.get("pancasuda") or {}).get("nama")
    if not (hari and pas and neptu and psd):
        return []
    band = "rendah" if neptu <= 10 else "sedang" if neptu <= 14 else "tinggi"
    return [_block(f"Hari {hari} × Pasaran {pas}", _join(d["hari"][hari], d["pasaran"][pas], d["relasi"][f"{hari}|{pas}"])),
            _block(f"Neptu {neptu} × Pancasuda {psd}", _join(d["pancasuda"][psd], d["neptu"][band], d["advice"][psd]))]


_ZW_SLUG = {"ziwei": "zi_wei", "tianji": "tian_ji", "taiyang": "tai_yang", "wuqu": "wu_qu", "tiantong": "tian_tong",
            "lianzhen": "lian_zhen", "tianfu": "tian_fu", "taiyin": "tai_yin", "tanlang": "tan_lang",
            "jumen": "ju_men", "tianxiang": "tian_xiang", "tianliang": "tian_liang", "qisha": "qi_sha", "pojun": "po_jun"}
_ZW_NAMA = {v: v.replace("_", " ").title() for v in _ZW_SLUG.values()}


def _ziwei(raw, d):
    b = _ZW_SLUG.get(raw.get("bintang"))
    mg, el = raw.get("ming_gong"), raw.get("bureau_elemen")
    if not (b and mg and el):
        return []
    t2 = _join(d["bureau"][el], d["relasi"][f"{b}|{el}"], d["advice"][b], d["dipinjam"] if raw.get("dipinjam") else "")
    return [_block(f"{_ZW_NAMA[b]} × Ming Gong di {mg}", _join(d["bintang"][b], d["istana"][mg])),
            _block(f"{_ZW_NAMA[b]} × Biro {el}", t2)]


def _human_design(raw, d):
    tipe, oto = raw.get("tipe"), raw.get("otoritas")
    if not (tipe and oto):
        return []
    return [_block(f"{tipe} × Otoritas {oto}", _join(d["tipe"][tipe], d["otoritas"][oto], d["relasi"][f"{tipe}|{oto}"])),
            _block("Menjalankan Strategimu Sehari-hari", d["advice"][tipe])]


_MB_SUMBU = (("E", "I", "EI", "Ekstraversi / Introversi"), ("S", "N", "SN", "Sensing / Intuition"),
             ("T", "F", "TF", "Thinking / Feeling"), ("J", "P", "JP", "Judging / Perceiving"))


def _mbti(raw, d):
    tipe, c = raw.get("tipe") or "", raw.get("counts") or {}
    if len(tipe) != 4 or not c:
        return []
    temp = tipe[1:3] if tipe[1] == "N" else "S" + tipe[3]  # pola Keirsey: NT, NF, SJ, SP
    rasio = []
    for a, b, kode, label in _MB_SUMBU:
        tot = c.get(a, 0) + c.get(b, 0)
        rasio.append((max(c.get(a, 0), c.get(b, 0)) / tot if tot else 0.5, kode, label))
    kuat, tipis = max(rasio), min(rasio)
    huruf = _join(*(d["huruf"][x] for x in tipe))
    t2 = d["sumbu"][kuat[1]]["kuat"]
    if tipis[0] <= 0.7 and tipis[1] != kuat[1]:
        t2 = _join(t2, d["sumbu"][tipis[1]]["tipis"])
    return [_block(f"{tipe}: Temperamen {temp}", _join(d["temperamen"][temp], huruf)),
            _block(f"Sumbu Terjelas ({kuat[2]}) dan Terseimbang ({tipis[2]})", t2),
            _block("Saran untuk Temperamenmu", d["advice"][temp])]


_BF_PAIR = (("O", "C", "Keterbukaan × Kehati-hatian"), ("E", "A", "Ekstraversi × Keramahan"),
            ("C", "N", "Kehati-hatian × Kepekaan emosi"), ("A", "N", "Keramahan × Kepekaan emosi"))


def _big_five(raw, d):
    lv, dom = raw.get("levels") or {}, raw.get("dominant_trait")
    if len(lv) < 5:
        return []
    out = [_block("Profil Lima Sifatmu", _join(*(d["level"][t][lv[t]] for t in "OCEAN")))]
    for a, b, judul in _BF_PAIR:
        out.append(_block(judul, d["pasangan"][f"{a}|{b}"][f"{lv[a]}|{lv[b]}"]))
    if dom in d["advice"]:
        out.append(_block("Saran untuk Sifat Terkuatmu", d["advice"][dom]))
    return out


def _enneagram(raw, d):
    t, c = raw.get("tipe"), raw.get("counts") or {}
    if not t:
        return []
    kiri, kanan = (t - 2) % 9 + 1, t % 9 + 1
    sayap = kanan if c.get(kanan, 0) > c.get(kiri, 0) else kiri
    arah = d["arah"][str(t)]
    t1 = d["sayap"][str(t)][str(sayap)]
    if raw.get("tipe_tied"):
        t1 = _join(t1, d["seri"])
    return [_block(f"Tipe {t} × Sayap {sayap}", t1),
            _block(f"Tipe {t}: Saat Tumbuh dan Saat Tertekan", _join(arah["tumbuh"], arah["stres"]))]


_DISC_N = {"D": "Dominance", "I": "Influence", "S": "Steadiness", "C": "Conscientiousness"}


def _disc(raw, d):
    p, c = raw.get("tipe"), raw.get("counts") or {}
    if p not in _DISC_N or not c:
        return []
    sisa = [k for k in "DISC" if k != p]
    sec = max(sisa, key=lambda k: (c.get(k, 0), -"DISC".index(k)))
    t = d["pasangan"][p + sec]
    if c.get(sec, 0) == 0 or c.get(sec, 0) == c.get(p, 0):
        t = _join(t, d["tunggal"])
    return [_block(f"{_DISC_N[p]} × {_DISC_N[sec]}", t), _block(f"Saran untuk Gaya {_DISC_N[p]}", d["advice"][p])]


_LL_N = {"WA": "Words of Affirmation", "QT": "Quality Time", "RG": "Receiving Gifts",
         "AS": "Acts of Service", "PT": "Physical Touch"}


def _love_language(raw, d):
    p, s = raw.get("primary"), raw.get("secondary")
    if p not in _LL_N or s not in _LL_N:
        return []
    return [_block(f"{_LL_N[p]} × {_LL_N[s]}", d["pasangan"][f"{p}|{s}"]),
            _block("Cara Menyampaikan Kebutuhanmu", d["saran_pasangan"][p]),
            _block("Cara Kamu Memberi Kasih", d["cara_memberi"][p])]


_BUILDERS.update({"Weton": _weton, "Zi Wei": _ziwei, "Human Design": _human_design, "MBTI": _mbti,
                  "Big Five": _big_five, "Enneagram": _enneagram, "DISC": _disc, "Love Language": _love_language})


def build_combo(system, raw):
    """Return list [{"title","text"}] hasil penggabungan variabel, atau [] kalau tidak tersedia."""
    fn, d = _BUILDERS.get(system), _data(system)
    if not fn or not d or not isinstance(raw, dict):
        return []
    try:
        return fn(raw, d)
    except (KeyError, TypeError, ValueError):
        return []
