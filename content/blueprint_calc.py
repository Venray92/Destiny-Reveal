"""
Blueprint Mendalam (REVISI06 bagian 3): rencana kuesioner (Singkat/Lengkap), scoring, dan penyusunan hasil
dari library yang SUDAH ada: profil A-M (5 sistem lahir) + profil/paid + deep.json (10 sistem lain).
Grand Synthesis = rangkaian kalimat dari lintas sistem + hitungan numerologi (personal year), bukan teks acak.
"""

import hashlib
import json
import re
from datetime import date
from functools import lru_cache
from pathlib import Path

from content import periodic
from content import profile_flat as pf
from content import profile_loader as pl
from content.questionnaires.big_five_soal import BIG_FIVE_QUESTIONS
from content.questionnaires.disc_soal import DISC_DIMENSION_NAMES, DISC_KEY, DISC_QUESTIONS
from content.questionnaires.enneagram_soal import ENNEAGRAM_QUESTIONS, ENNEAGRAM_TYPE_NAMES
from content.questionnaires.love_language_soal import (LOVE_LANGUAGE_NAMES, LOVE_LANGUAGE_QUESTIONS,
                                                       LOVE_LANGUAGE_SLUG)
from content.questionnaires.mbti_soal import MBTI_DICHOTOMIES, MBTI_QUESTIONS
from content.result_builder import compute_quiz_raw_result, compute_raw_result

_BASE = Path(__file__).resolve().parent / "interpretations"

# (nama, ikon, deskripsi singkat, jenis)
SYSTEMS = [
    ("Zodiak", "♈", "Rasi bintang barat & planet penguasa", "lahir"),
    ("Shio", "🐉", "Siklus lunar 12 hewan astrologi Tiongkok", "lahir"),
    ("Weton", "🗓️", "Neptu & panca wara kearifan tanah Jawa", "lahir"),
    ("Numerologi", "🔢", "Angka jalur hidup (Life Path Pythagoras)", "lahir"),
    ("Matrix Destiny", "🔷", "Geometri 22 arcana takdir jiwa", "lahir"),
    ("MBTI", "🧠", "16 tipe kepribadian kognitif Jungian", "quiz"),
    ("Big Five", "📊", "5 dimensi psikometri ilmiah OCEAN", "quiz"),
    ("Enneagram", "🔺", "9 arketipe bawah sadar & ketakutan inti", "quiz"),
    ("DISC", "🎯", "Pola perilaku & gaya kepemimpinan kerja", "quiz"),
    ("Love Language", "💖", "5 bahasa kasih & komunikasi emosional", "quiz"),
    ("BaZi", "🀄", "Empat pilar takdir & elemen hari lahir", "lahir"),
    ("Zi Wei", "⭐", "Peta bintang Zi Wei Dou Shu", "lahir"),
    ("Human Design", "🔮", "Tipe energi, strategi & otoritas batin", "lahir"),
    ("Golongan Darah", "🩸", "Kecenderungan sifat bawaan golongan darah", "lahir"),
    ("Tarot", "🎴", "Kartu arcana kelahiranmu", "lahir"),
]
KIND = {n: k for n, _i, _d, k in SYSTEMS}
ICON = {n: i for n, i, _d, _k in SYSTEMS}
DESC = {n: d for n, _i, d, _k in SYSTEMS}
NAMES = [n for n, *_ in SYSTEMS]
QUIZ = [n for n in NAMES if KIND[n] == "quiz"]
BANK = {"MBTI": MBTI_QUESTIONS, "Big Five": BIG_FIVE_QUESTIONS, "Enneagram": ENNEAGRAM_QUESTIONS,
        "DISC": DISC_QUESTIONS, "Love Language": LOVE_LANGUAGE_QUESTIONS}
_BIRTH5 = ("Zodiak", "Shio", "Weton", "Numerologi", "Matrix Destiny")
_DEEP_FILE = {"MBTI": "mbti", "Big Five": "big_five", "Enneagram": "enneagram", "DISC": "disc",
              "Love Language": "love_language", "BaZi": "bazi", "Zi Wei": "ziwei", "Human Design": "human_design",
              "Golongan Darah": "golongan_darah"}
_AM = {"A": "Aspek Utama", "B": "Karier & Keuangan", "C": "Asmara & Hubungan", "D": "Kekuatan Karakter",
       "E": "Shadow Work", "F": "Nasihat Strategis", "G": "Siapa Kamu", "H": "Karier", "I": "Asmara",
       "J": "Keuangan", "K": "Shadow Side", "L": "Blindspot", "M": "PR Kecil"}
_FLAT_EXTRA = [("kekuatan_yang_perlu_dijaga", "Kekuatan Karakter"), ("shadow_work", "Shadow Work"),
               ("kesehatan", "Kesehatan"), ("emosi_trigger", "Pemicu Emosi"), ("blindspot", "Blindspot"),
               ("pr_kecil_buat_kamu", "PR Kecil Buat Kamu")]


# ═════════════ kuesioner ═════════════
def _short_ids(system):
    bank = BANK[system]
    if system == "MBTI":
        pick, seen = [], {}
        for q in bank:
            if seen.get(q["letter"], 0) < 2:
                seen[q["letter"]] = seen.get(q["letter"], 0) + 1
                pick.append(q)
        return pick
    if system == "Big Five":
        pick, seen = [], {}
        for q in bank:
            if seen.get(q["trait"], 0) < 3:
                seen[q["trait"]] = seen.get(q["trait"], 0) + 1
                pick.append(q)
        return pick
    if system == "Enneagram":
        pick, seen = [], {}
        for q in bank:
            if seen.get(q["type"], 0) < 2:
                seen[q["type"]] = seen.get(q["type"], 0) + 1
                pick.append(q)
        return pick
    return bank[:12]  # DISC & Love Language


def plan(mode, systems):
    """Daftar soal berurutan [{sys, q}] untuk mode 'singkat'/'lengkap' pada sistem kuesioner yang dipilih."""
    out = []
    for s in QUIZ:
        if s in systems:
            for q in (BANK[s] if mode == "lengkap" else _short_ids(s)):
                out.append({"sys": s, "q": q})
    return out


def _short_raw(system, ans):
    """Scoring versi singkat (subset soal), bentuk hasilnya sama dengan engine/*_scoring.py."""
    qs = _short_ids(system)
    if system == "MBTI":
        counts = {l: 0 for pair in MBTI_DICHOTOMIES for l in pair}
        for q in qs:
            if ans.get(q["id"]):
                counts[q["letter"]] += 1
        tipe = "".join(a if counts[a] >= counts[b] else b for a, b in MBTI_DICHOTOMIES)
        return {"tipe": tipe, "counts": counts}
    if system == "Big Five":
        from engine.big_five_scoring import BIG_FIVE_TRAIT_SLUG, _level
        raw_sum, n = {}, {}
        for q in qs:
            v = ans.get(q["id"], 3)
            raw_sum[q["trait"]] = raw_sum.get(q["trait"], 0) + (6 - v if q["reverse"] else v)
            n[q["trait"]] = n.get(q["trait"], 0) + 1
        scores = {t: int(round(raw_sum[t] * 7 / n[t])) for t in raw_sum}  # skala 7 soal/trait seperti versi lengkap
        dom = max(scores, key=scores.get)
        return {"scores": scores, "levels": {t: _level(s) for t, s in scores.items()}, "dominant_trait": dom,
                "dominant_slug": BIG_FIVE_TRAIT_SLUG[dom]}
    if system == "Enneagram":
        counts = {t: 0 for t in range(1, 10)}
        for q in qs:
            if ans.get(q["id"]):
                counts[q["type"]] += 1
        top = max(counts.values())
        tied = sorted(t for t, c in counts.items() if c == top)
        return {"tipe": tied[0], "tipe_nama": ENNEAGRAM_TYPE_NAMES[tied[0]], "tipe_tied": tied if len(tied) > 1 else None,
                "counts": counts}
    if system == "DISC":
        counts = {"D": 0, "I": 0, "S": 0, "C": 0}
        for q in qs:
            d = DISC_KEY.get(ans.get(q["id"]))
            if d:
                counts[d] += 1
        top = max(counts.values())
        tied = sorted(k for k, v in counts.items() if v == top)
        return {"tipe": tied[0], "tipe_nama": DISC_DIMENSION_NAMES[tied[0]], "tipe_tied": tied if len(tied) > 1 else None,
                "counts": counts}
    counts = {k: 0 for k in LOVE_LANGUAGE_NAMES}  # Love Language
    for q in qs:
        p = ans.get(q["id"])
        if p in ("A", "B"):
            counts[q[p]["category"]] += 1
    ranked = sorted(counts, key=lambda k: counts[k], reverse=True)
    return {"primary": ranked[0], "secondary": ranked[1], "primary_nama": LOVE_LANGUAGE_NAMES[ranked[0]],
            "secondary_nama": LOVE_LANGUAGE_NAMES[ranked[1]], "primary_slug": LOVE_LANGUAGE_SLUG[ranked[0]], "counts": counts}


def quiz_raw(system, ans, mode):
    return compute_quiz_raw_result(system, ans) if mode == "lengkap" else _short_raw(system, ans)


# ═════════════ data per sistem ═════════════
@lru_cache(maxsize=None)
def _deep(system):
    if system == "Tarot":
        out = {}
        for f in ("major", "wands", "cups", "swords", "pentacles"):
            try:
                out.update(json.loads((_BASE / "tarot" / f"deep_{f}.json").read_text(encoding="utf-8")))
            except Exception:
                pass
        return out
    f = _DEEP_FILE.get(system)
    if not f:
        return {}
    try:
        return json.loads((_BASE / f / "deep.json").read_text(encoding="utf-8"))
    except Exception:
        return {}


def _t(x):
    return x.strip() if isinstance(x, str) and x.strip() else ""


def _blocks(system, raw):
    """{title, utama, karier, asmara, nasihat (list paragraf), extra [(label, teks)]} atau None."""
    if not raw or raw.get("placeholder"):
        return None
    if system in _BIRTH5:
        p = pl.get_profile(system, raw)
        if not p:
            return None
        s = p.get("sections") or {}
        g = lambda k: [_t(s.get(k))] if _t(s.get(k)) else []
        extra = [(_AM[k], _t(s.get(k))) for k in "DEGHIJKLM" if _t(s.get(k))]
        ttl = (pl.get_title(system, raw) or {}).get("title", "")
        return {"title": ttl, "utama": g("A"), "karier": g("B"), "asmara": g("C"), "nasihat": g("F"),
                "extra": extra, "shadow": g("E"), "kuat": g("D"), "key": p["key"]}
    p = pf.get_big_five(raw) if system == "Big Five" else pf.get_profile(system, raw)
    if not p:
        return None
    e = p.get("entry") or {}
    free, paid = e.get("free") or {}, e.get("paid") or {}
    deep = _deep(system).get(p["key"]) or {}
    lst = lambda *xs: [t for t in (_t(x) for x in xs) if t]
    ttl = ((p.get("title") if system == "Big Five" else pf.get_title(system, raw)) or {}).get("title", "") or e.get("nama", "")
    extra = [(lbl, _t(paid.get(k)) or _t(deep.get(k))) for k, lbl in _FLAT_EXTRA]
    return {"title": ttl, "utama": lst(deep.get("ringkasan"), free.get("siapa_kamu")),
            "karier": lst(paid.get("karir"), paid.get("keuangan"), deep.get("karir_deep"), deep.get("rezeki_deep")),
            "asmara": lst(paid.get("asmara"), deep.get("asmara_deep")),
            "nasihat": lst(paid.get("nasihat_strategis"), deep.get("latihan_harian")),
            "extra": [(a, b) for a, b in extra if b], "key": p["key"],
            "shadow": lst(paid.get("shadow_work"), deep.get("blindspot")), "kuat": lst(paid.get("kekuatan_yang_perlu_dijaga"))}


# ═════════════ sintesis ═════════════
def _kal(text, n=1, maks=230):
    parts = re.split(r"(?<=[.!?])\s+", (text or "").strip())
    out = " ".join(parts[:n]).strip()
    if len(out) > maks:
        out = out[:maks].rsplit(" ", 1)[0].rstrip(",;:") + "…"
    return out


_TEMA_PY = {1: "Inisiasi & Awal Baru", 2: "Kemitraan & Kesabaran", 3: "Ekspresi & Kreativitas", 4: "Fondasi & Disiplin",
            5: "Perubahan & Kebebasan", 6: "Tanggung Jawab & Keluarga", 7: "Refleksi & Pendalaman Batin",
            8: "Panen, Otoritas & Keuangan", 9: "Penyelesaian & Pelepasan"}


def _roadmap(tgl, y0):
    years = [(y0 + i, periodic.personal_year(tgl, y0 + i)) for i in range(10)]
    fase = [years[0:3], years[3:6], years[6:10]]
    out = []
    best = max(range(3), key=lambda i: sum(1 for _y, p in fase[i] if p in (8, 1)))
    for i, f in enumerate(fase):
        temas = []
        for _y, p in f:
            t = _TEMA_PY.get(p, "")
            if t and t not in temas:
                temas.append(t)
        rinci = " → ".join(f"{y} (Tahun {p}: {_TEMA_PY.get(p, '').split(' &')[0]})" for y, p in f)
        out.append({"label": f"Tahun ke-{1 + sum(len(x) for x in fase[:i])} s/d {sum(len(x) for x in fase[:i + 1])}: Fase " + " & ".join(
            t.split(" &")[0] for t in temas[:2]), "text": f"{rinci}.", "star": i == best})
    return out


def _siklus_panen(tgl, y0):
    age = y0 - tgl.year
    next7 = (age // 7 + 1) * 7
    y8 = next((y0 + i for i in range(0, 12) if periodic.personal_year(tgl, y0 + i) == 8), None)
    y1 = next((y0 + i for i in range(0, 12) if periodic.personal_year(tgl, y0 + i) == 1), None)
    bits = []
    if y8:
        bits.append(f"Tahun pribadi 8 (panen, otoritas & keuangan) berikutnya jatuh pada {y8}")
    if y1:
        bits.append(f"tahun pribadi 1 (peluncuran baru) pada {y1}")
    bits.append(f"siklus usia kelipatan 7 berikutnya di usia {next7} ({tgl.year + next7})")
    return "; ".join(bits) + ". Pada titik-titik ini, ekspansi bisnis atau peluncuran portofolio baru paling selaras dengan ritme hidupmu."


def _synthesis(prof, raws, B, now_year):
    tgl = prof["tgl"]
    n = sum(1 for s in NAMES if B.get(s))
    ti = lambda s: ((pl.get_title(s, raws.get(s)) if s in _BIRTH5 else (pf.get_title(s, raws.get(s)) if s != "Big Five" else
                                                                         (pf.get_big_five(raws.get(s)) or {}).get("title"))) or {}).get("title", "")
    g = lambda s, k, i=1, m=230: _kal((B.get(s) or {}).get(k, [""])[0] if (B.get(s) or {}).get(k) else "", i, m)
    main = ti("MBTI") or ti("Zodiak")
    lp = (raws.get("Numerologi") or {}).get("life_path", "")
    p1 = (f"Sintesis dari {n} sistem menunjukkan kamu adalah sosok **{main}**, dengan jiwa bertema "
          f"**{ti('Matrix Destiny') or '-'}** dan angka hidup **{lp}**. " + g("Zodiak", "utama", 1, 260))
    p2 = ("Di sisi lain, " + (ti("Weton") + ". " if ti("Weton") else "") + g("Weton", "utama", 1, 200) + " " + g("Shio", "utama", 1, 200)).strip()
    sup = []
    for s in ("MBTI", "Zodiak", "Enneagram", "Weton", "Big Five"):
        t = g(s, "kuat", 1, 170)
        if t and len(sup) < 3:
            sup.append((s, t))
    blind = []
    for s in ("Enneagram", "DISC", "Big Five", "MBTI", "Weton"):
        t = g(s, "shadow", 1, 170)
        if t and len(blind) < 2:
            blind.append((s, t))
    prof_txt = [g("Matrix Destiny", "karier", 2, 330), g("BaZi", "karier", 1, 230) or g("Zodiak", "karier", 1, 230)]
    ll = raws.get("Love Language") or {}
    asm1 = (f"Dalam relasi cinta, bahasa kasih utamamu adalah **{ll.get('primary_nama', '-')}**"
            + (f" (kedua: {ll.get('secondary_nama')})" if ll.get("secondary_nama") else "") + ". "
            + g("Love Language", "asmara", 1, 230) + " " + g("Zodiak", "asmara", 1, 230)).strip()
    asm2 = (g("Weton", "asmara", 1, 230) + " " + g("Enneagram", "asmara", 1, 230)).strip()
    enn = raws.get("Enneagram") or {}
    sh1 = (f"Berdasarkan Enneagram **{enn.get('tipe_nama', '-')}** dan arketipe Weton-mu, " + g("Enneagram", "shadow", 2, 330)).strip()
    sh2 = ("Latihan integrasi jiwamu: " + g("Enneagram", "nasihat", 1, 260)).strip() if g("Enneagram", "nasihat") else ""
    return {
        "arketipe": [p1, p2], "super": sup, "blind": blind, "profesi": [t for t in prof_txt if t],
        "panen": _siklus_panen(tgl, now_year), "asmara": [t for t in (asm1, asm2) if t],
        "shadow": [t for t in (sh1, sh2) if t], "roadmap": _roadmap(tgl, now_year),
    }


# ═════════════ build ═════════════
def build_blueprint(prof, systems, quiz_answers, mode, now_year=None):
    """prof {nama,tgl,jam,kota,golda}; systems list nama; quiz_answers {sistem: {id: val}}. Return dict hasil atau None."""
    from engine.rotation import today_wib
    now_year = now_year or today_wib().year
    ld = {"tanggal_lahir": prof["tgl"], "jam_lahir": prof.get("jam"), "kota_lahir": prof.get("kota"),
          "golongan_darah": prof.get("golda") if prof.get("golda") in ("A", "B", "AB", "O") else None,
          "nama_lengkap": prof["nama"]}
    raws, B = {}, {}
    for s in systems:
        try:
            raws[s] = quiz_raw(s, quiz_answers.get(s) or {}, mode) if KIND[s] == "quiz" else compute_raw_result(s, ld)
            B[s] = _blocks(s, raws[s])
        except Exception:
            raws[s], B[s] = {}, None
    if not any(B.values()):
        return None
    z, w, m, hd = raws.get("Zodiak") or {}, raws.get("Weton") or {}, raws.get("Matrix Destiny") or {}, raws.get("Human Design") or {}
    def _extra(name):  # kepala identitas selalu terisi, walau sistemnya tidak ada di scope (Deep Dive 1 sistem)
        try:
            return raws.get(name) or compute_raw_result(name, ld) or {}
        except Exception:
            return {}
    z, w, m = _extra("Zodiak"), _extra("Weton"), _extra("Matrix Destiny")
    hd = hd or _extra("Human Design")
    head = {
        "zodiak": f"{z['sign']} ({z['element']})" if z.get("sign") else "-",
        "weton": f"{w['hari']} {w['pasaran']} ({w['neptu']})" if w.get("hari") else "-",
        "matrix": f"Arcana {m['titik_inti']}" if m.get("titik_inti") else "-",
        "hd": hd.get("tipe") or hd.get("tipe_nama") or "-",
    }
    jam = prof.get("jam")
    lahir = f"{prof['tgl'].day} {_BULAN[prof['tgl'].month - 1]} {prof['tgl'].year}"
    if jam is not None and hasattr(jam, "strftime"):
        lahir += f" ({jam.strftime('%H:%M')})"
    if prof.get("kota"):
        lahir += f" di {prof['kota']}"
    if prof.get("golda") in ("A", "B", "AB", "O"):
        lahir += f" · Gol. Darah {prof['golda']}"
    sid = hashlib.md5(f"{prof['nama']}{prof['tgl']}".encode()).hexdigest()[:5].upper()
    systems_out = []
    for i, s in enumerate(NAMES, 1):
        if s in systems:
            b = B.get(s)
            systems_out.append({"n": i, "name": s, "icon": ICON[s], "desc": DESC[s], "ok": bool(b), **(b or {})})
    res = {"nama": prof["nama"], "lahir": lahir, "head": head, "id": f"BP-{now_year}-{sid}", "systems": systems_out,
           "complete": len(systems) > 1, "mode": mode, "n_ok": sum(1 for x in systems_out if x["ok"])}
    if res["complete"]:
        res["synth"] = _synthesis(prof, raws, B, now_year)
    return res


_BULAN = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November",
          "Desember"]
