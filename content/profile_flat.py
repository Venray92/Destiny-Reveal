"""
Loader profil 10 sistem non-Mode-1 (BaZi, Zi Wei, Human Design, Golongan Darah, MBTI, Enneagram,
DISC, Love Language, Big Five, Tarot) dari JSON baru (satu-satunya sumber teks).

Bentuk entri: {"nama", "free": {siapa_kamu, atribut_1, atribut_2, quote}, "paid": {kekuatan_yang_perlu_dijaga,
pr_kecil_buat_kamu, karir, asmara, keuangan, kesehatan}}. Judul/tagline/chip dari titles.json.
"""

from pathlib import Path

from content import safe_json

_BASE = Path(__file__).resolve().parent / "interpretations"
_TITLES = "titles.json"

# Tarot: 78 kartu (22 major + 56 minor), semua bisa ditarik engine
_FILES = {
    "BaZi": ["bazi/profile.json"],
    "Zi Wei": ["ziwei/profile.json"],
    "Human Design": ["human_design/profile.json"],
    "Golongan Darah": ["golongan_darah/profile.json"],
    "MBTI": ["mbti/profile.json"],
    "Enneagram": ["enneagram/profile.json"],
    "DISC": ["disc/profile.json"],
    "Love Language": ["love_language/profile.json"],
    "Big Five": ["big_five/profile.json"],
    "Tarot": ["tarot/tarot_major.json", "tarot/tarot_cups.json", "tarot/tarot_pentacles.json",
              "tarot/tarot_swords.json", "tarot/tarot_wands.json"],
}
SYSTEMS = tuple(_FILES)

_ZIWEI = {"ziwei": "zi_wei", "tianji": "tian_ji", "taiyang": "tai_yang", "wuqu": "wu_qu", "tiantong": "tian_tong",
          "lianzhen": "lian_zhen", "tianfu": "tian_fu", "taiyin": "tai_yin", "tanlang": "tan_lang",
          "jumen": "ju_men", "tianxiang": "tian_xiang", "tianliang": "tian_liang", "qisha": "qi_sha", "pojun": "po_jun"}
_DISC = {"D": "dominance", "I": "influence", "S": "steadiness", "C": "conscientiousness"}
_LOVE = {"WA": "words_of_affirmation", "QT": "quality_time", "RG": "receiving_gifts",
         "AS": "acts_of_service", "PT": "physical_touch"}
_BF_TRAIT = {"O": "openness", "C": "conscientiousness", "E": "extraversion", "A": "agreeableness", "N": "neuroticism"}
_BF_NAMA = {"O": "keterbukaan terhadap pengalaman baru", "C": "kehati-hatian/kedisiplinan", "E": "ekstraversi",
            "A": "keramahan", "N": "kepekaan emosi"}


def _tarot_key(slug):
    from engine.tarot import TAROT_MAJOR_ARCANA, TAROT_MINOR_ARCANA  # impor lambat biar tidak melingkar
    if slug in TAROT_MAJOR_ARCANA:
        return f"major_{TAROT_MAJOR_ARCANA.index(slug):02d}"
    return slug if slug in TAROT_MINOR_ARCANA else None


def profile_key(system, raw):
    """Key entri JSON dari hasil engine (raw), atau None."""
    raw = raw or {}
    if system == "BaZi":
        return raw.get("day_master")
    if system == "Zi Wei":
        return _ZIWEI.get(raw.get("bintang"))
    if system == "Human Design":
        return raw.get("tipe_slug")
    if system == "Golongan Darah":
        g = raw.get("golongan_darah")
        return g.lower() if g else None
    if system == "MBTI":
        t = raw.get("tipe")
        return t.lower() if t else None
    if system == "Enneagram":
        t = raw.get("tipe")
        return f"tipe_{t}" if t is not None else None
    if system == "DISC":
        return _DISC.get(raw.get("tipe"))
    if system == "Love Language":
        return _LOVE.get(raw.get("primary"))
    if system == "Tarot":
        return _tarot_key(raw.get("kartu"))
    return None


def _data(system):
    out = {}
    for f in _FILES.get(system, []):
        out.update((safe_json.load(_BASE / f) or {}).get("data") or {})
    return out


def _titles(system):
    return (safe_json.load(_BASE / _TITLES) or {}).get(system) or {}


def get_profile(system, raw):
    """{"key", "nama", "free", "paid"} atau None. Big Five: pakai bf_dominan() dulu."""
    key = profile_key(system, raw)
    e = _data(system).get(key) if key else None
    if not isinstance(e, dict) or not e.get("free"):
        return None
    return {"key": key, "nama": e.get("nama", ""), "free": e["free"], "paid": e.get("paid") or {}, "entry": e}


def get_title(system, raw):
    key = profile_key(system, raw)
    t = _titles(system).get(key) if key else None
    return dict(t) if t else None


# ── Big Five ──
def bf_key(trait, level, skor=None):
    """Key JSON untuk satu trait (tinggi/sedang/rendah). Level tak dikenal -> sisi terdekat berdasarkan skor (<=21 rendah), tanpa skor -> tinggi."""
    if not trait:
        return None
    lv = (level or "").lower()
    if lv not in ("tinggi", "sedang", "rendah"):
        lv = "rendah" if (skor is not None and skor <= 21) else "tinggi"
    return f"{_BF_TRAIT[trait]}_{lv}"


def get_big_five(raw):
    """Dict siap-tampil Big Five dari JSON, atau None. Trait dominan jadi narasi utama, 4 trait lain dirangkum."""
    levels = (raw or {}).get("levels") or {}
    scores = (raw or {}).get("scores") or {}
    dom = (raw or {}).get("dominant_trait")
    if not dom or dom not in levels:
        return None
    key = bf_key(dom, levels[dom], scores.get(dom))
    e = _data("Big Five").get(key)
    tit = _titles("Big Five").get(key)
    if not e or not tit:
        return None
    ringkas = []
    for tr in ("O", "C", "E", "A", "N"):
        if tr == dom or tr not in levels:
            continue
        lv = levels[tr].lower()
        r = (_titles("Big Five").get(f"{_BF_TRAIT[tr]}_{lv}") or {}).get("ringkas")
        if r:
            ringkas.append(f"Dari sisi {_BF_NAMA[tr]} ({lv}), {r}")
    return {"key": key, "nama": e.get("nama", ""), "free": e["free"], "paid": e.get("paid") or {},
            "title": tit, "ringkas": ringkas, "entry": e}


def audit(system):
    """Cek kelengkapan: tiap entri punya free (4 field) + paid (6 field) tidak kosong dan judul di titles.json."""
    data = _data(system)
    if not data:
        return [f"{system}: file kosong / tidak terbaca"]
    tit = _titles(system)
    errs = []
    for k, e in data.items():
        errs += [f"{system}.{k}.free.{f}: kosong" for f in ("siapa_kamu", "atribut_1", "atribut_2", "quote")
                 if not str((e.get("free") or {}).get(f, "")).strip()]
        errs += [f"{system}.{k}.paid.{f}: kosong" for f in ("kekuatan_yang_perlu_dijaga", "pr_kecil_buat_kamu", "karir",
                                                           "asmara", "keuangan", "kesehatan")
                 if not str((e.get("paid") or {}).get(f, "")).strip()]
        if k not in tit:
            errs.append(f"{system}.{k}: judul tidak ada di titles.json")
    return errs
