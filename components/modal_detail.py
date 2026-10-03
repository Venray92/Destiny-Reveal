"""
Sub-modal "Detail Sistem" (UI7): kartu takdir + uraian lengkap satu sistem.
Dibuka dari tombol "Lihat & Simpan Kartu ..." di hasil Mode 1. Bukan dialog baru
(Streamlit cuma izinkan 1 dialog) — ini satu langkah di dalam _flow_dialog.

Sumber isi uraian (dibaca dinamis, urutan prioritas):
  1. key JSON versi lengkap  : aspek_utama, karier_dan_keuangan, asmara_dan_hubungan,
                               kekuatan_karakter, shadow_work, nasihat_strategis, parameter_kunci
  2. key JSON yang sudah ada : sections.free/paid/deep di content/interpretations/zodiak/zodiak_profile.json
  3. kamus konten Python (build_display_data): p1/p2/p3 + domains (semua sistem)
"""

import html
import json
from functools import lru_cache
from pathlib import Path
from urllib.parse import quote as urlquote

import streamlit as st

from components.flow_state import STEP_RESULT, set_step
from content.result_builder import build_display_data
from utils.card_images import card_filename_for_system, card_image_bytes_for_system

_ZODIAK_JSON = Path(__file__).resolve().parent.parent / "content" / "interpretations" / "zodiak" / "zodiak_profile.json"

ZODIAK_GLYPH = {
    "Aries": "♈", "Taurus": "♉", "Gemini": "♊", "Cancer": "♋", "Leo": "♌", "Virgo": "♍",
    "Libra": "♎", "Scorpio": "♏", "Sagittarius": "♐", "Capricorn": "♑", "Aquarius": "♒", "Pisces": "♓",
}

# (judul section, [key kandidat berurutan]) — semua key kandidat yang ada digabung
SECTIONS = [
    ("ASPEK UTAMA & ESENSI JIWA", ["aspek_utama", "siapa_kamu"]),
    ("KARIER, PELUANG USAHA & POTENSI FINANSIAL", ["karier_dan_keuangan", "karir", "peta_karier", "keuangan"]),
    ("ASMARA, DINAMIKA PERCINTAAN & PASANGAN JIWA", ["asmara_dan_hubungan", "asmara", "panduan_hubungan"]),
    ("KEKUATAN KARAKTER & YANG PERLU DIJAGA", ["kekuatan_karakter", "kekuatan_yang_perlu_dijaga"]),
    ("PR BAYANGAN (SHADOW WORK) & HAL YANG PERLU DIWASPADAI", ["shadow_work", "shadow_side", "blindspot"]),
    ("LANGKAH PRAKTIS JIWA & NASIHAT STRATEGIS", ["nasihat_strategis", "pr_kecil_buat_kamu"]),
]


@lru_cache(maxsize=1)
def _zodiak_json():
    try:
        return json.loads(_ZODIAK_JSON.read_text(encoding="utf-8")).get("data", {})
    except (OSError, ValueError):
        return {}


def _flatten(entry):
    """Ratakan {sections:{free,paid,deep}} + key top-level jadi satu dict datar."""
    flat = {}
    if not isinstance(entry, dict):
        return flat
    for k, v in entry.items():
        if k == "sections" and isinstance(v, dict):
            for grp in v.values():
                if isinstance(grp, dict):
                    flat.update(grp)
        else:
            flat[k] = v
    return flat


def _param_rows(system, raw):
    """Tabel 'Parameter Kunci' dari hasil engine (fallback kalau JSON gak punya parameter_kunci)."""
    r = raw or {}
    if system == "Zodiak":
        rows = [("Rasi Bintang", r.get("sign")), ("Elemen Dasar", r.get("element")),
                ("Planet Penguasa", r.get("ruling_planet")), ("Karakter Kunci", r.get("modality"))]
    elif system == "Shio":
        rows = [("Shio", r.get("shio")), ("Elemen Dasar", r.get("elemen"))]
    elif system == "Weton":
        rows = [("Hari", r.get("hari")), ("Pasaran", r.get("pasaran")), ("Neptu", r.get("neptu"))]
    elif system == "Numerologi":
        rows = [("Life Path", r.get("life_path")), ("Expression", r.get("expression")),
                ("Soul Urge", r.get("soul_urge")), ("Personality", r.get("personality"))]
    else:
        rows = [("Titik Inti", r.get("titik_inti")), ("Arketipe", r.get("nama_arketipe"))]
    return [(k, str(v)) for k, v in rows if v not in (None, "")]


def _as_rows(value):
    """parameter_kunci dari JSON: dict {label: nilai} atau list [{label,nilai}] / [[l,v]]."""
    rows = []
    if isinstance(value, dict):
        rows = [(str(k), str(v)) for k, v in value.items()]
    elif isinstance(value, list):
        for it in value:
            if isinstance(it, dict) and len(it) >= 2:
                vals = list(it.values())
                lab = it.get("label") or it.get("nama") or vals[0]
                val = it.get("nilai") or it.get("value") or vals[1]
                rows.append((str(lab), str(val)))
            elif isinstance(it, (list, tuple)) and len(it) >= 2:
                rows.append((str(it[0]), str(it[1])))
    return rows


def build_detail(system, raw):
    """Susun data detail satu sistem. Return dict {title, sections:[(judul, [teks...])], params:[(k,v)]} atau None."""
    disp = build_display_data(system, raw)
    if not disp:
        return None
    flat = {"siapa_kamu": disp.get("p1"), "kekuatan_yang_perlu_dijaga": disp.get("p2"),
            "pr_kecil_buat_kamu": disp.get("p3")}
    flat.update({k: v for k, v in (disp.get("domains") or {}).items() if v})
    if system == "Zodiak":
        flat.update(_flatten(_zodiak_json().get((raw or {}).get("sign"))))

    sections = []
    for title, keys in SECTIONS:
        texts = []
        for k in keys:
            v = flat.get(k)
            if isinstance(v, str) and v.strip():
                texts.append(v.strip())
            elif isinstance(v, list):
                texts.extend(str(x).strip() for x in v if str(x).strip())
        sections.append((title, texts))

    params = _as_rows(flat.get("parameter_kunci")) or _param_rows(system, raw)
    return {"title": disp["title"], "quote": disp.get("quote", ""), "tagline": disp.get("tagline", ""),
            "sections": sections, "params": params}


def _plain_text(system_label, detail):
    out = [f"Analisis Lengkap: {system_label}", detail["title"], ""]
    for title, texts in detail["sections"]:
        if texts:
            out += [title, *texts, ""]
    if detail["params"]:
        out += ["PARAMETER KUNCI SISTEM INI", *[f"{k}: {v}" for k, v in detail["params"]]]
    return "\n".join(out).strip()


# ── callback ─────────────────────────────────────────────────────
def cb_open_detail(system):
    st.session_state.dh_detail_system = system
    st.session_state.pop("dh_show_quote", None)
    st.session_state.pop("dh_show_fulltext", None)
    set_step("detail")


def _cb_back():
    set_step(STEP_RESULT)


def _cb_toggle(key):
    st.session_state[key] = not st.session_state.get(key)


def _e(text):
    return html.escape(str(text)).replace("\n", "<br>")


# ── render ───────────────────────────────────────────────────────
def render_detail():
    ss = st.session_state
    system = ss.get("dh_detail_system")
    item = next((r for r in (ss.get("dh_flow_result") or []) if r["system"] == system), None)
    detail = build_detail(system, item["raw"]) if item else None
    nama = (ss.get("dh_modal_data") or {}).get("nama", "")
    if not item or not detail:
        st.markdown('<div class="dh-step dh-step-detail"></div>', unsafe_allow_html=True)
        st.warning("Detail sistem ini belum tersedia.")
        st.button("← Tutup & Kembali ke Cetak Biru Takdir", key="dhd_back", on_click=_cb_back,
                  use_container_width=True)
        return

    raw, label = item["raw"], item["label"]
    num, _, nm = label.partition(". ")
    sys_title = nm.title().replace("Pythagoras", "Pythagoras")
    symbol = (ZODIAK_GLYPH.get(raw.get("sign"), "✦") + "\ufe0e") if system == "Zodiak" else \
        (detail["tagline"].split(" ")[0] if detail["tagline"] else "✦")
    elemen = raw.get("element") or raw.get("elemen")
    subline = f"Elemen {elemen}" if elemen else item["tag"]
    pills = "".join(f'<span class="dh-dt-pill">{_e(k)}: {_e(v)}</span>' for k, v in detail["params"][:3])
    quote = detail["quote"]
    quote_html = f'<div class="dh-dt-quote">&ldquo;{_e(quote)}&rdquo;</div>' if quote else ""

    st.markdown('<div style="height:14px;"></div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="dh-step dh-step-detail"></div>'
        '<div class="dh-dt-eyebrow">DETAIL SISTEM · KARTU TAKDIR</div>'
        '<div class="dh-dt-card">'
        '<div class="dh-dt-brand">✦ DESTINY REVEAL ✦</div>'
        f'<div class="dh-dt-sys">{_e(num)} · {_e(sys_title)}</div>'
        f'<div class="dh-dt-symbol">{_e(symbol)}</div>'
        f'<div class="dh-dt-name">{_e(item["short"])}</div>'
        f'<div class="dh-dt-sub">{_e(subline)}</div>'
        f'{quote_html}<div class="dh-dt-pills">{pills}</div>'
        f'<div class="dh-dt-foot"><span>Milik: <b>{_e(nama)}</b></span><span>destinyreveal.id</span></div>'
        '</div>', unsafe_allow_html=True)

    caption = (f'"{quote}"\n\n— {nama} · {item["short"]}\nCek takdirmu di destinyreveal.id #DestinyReveal'
               if quote else f'{nama} · {item["short"]}\nCek takdirmu di destinyreveal.id #DestinyReveal')
    img = card_image_bytes_for_system(system, raw)
    b1, b2 = st.columns(2, gap="small")
    with b1:
        if img:
            st.download_button("Simpan Gambar PNG", data=img, file_name=card_filename_for_system(system, raw),
                               mime="image/png", key="dhd_png", on_click="ignore", use_container_width=True,
                               icon=":material/download:")
        else:
            st.button("Simpan Gambar PNG", key="dhd_png", disabled=True, use_container_width=True)
    with b2:
        st.link_button("Share ke WhatsApp", f"https://wa.me/?text={urlquote(caption)}",
                       key="dhd_wa", use_container_width=True, icon=":material/send:")
    st.button("Salin Teks Kutipan untuk Caption", key="dhd_copyq", on_click=_cb_toggle,
              args=("dh_show_quote",), use_container_width=True, icon=":material/content_copy:")
    if ss.get("dh_show_quote"):
        st.code(caption, language=None)

    st.markdown('<div class="dh-dt-sep"></div>'
                '<div class="dh-dt-eyebrow">URAIAN KOMPREHENSIF VERSI LENGKAP</div>', unsafe_allow_html=True)
    h1, h2 = st.columns([2.4, 1.4], gap="small", vertical_alignment="center")
    with h1:
        st.markdown(f'<div class="dh-dt-h">Analisis Lengkap: {_e(sys_title)}</div>', unsafe_allow_html=True)
    with h2:
        st.button("Salin Seluruh Analisis Lengkap", key="dhd_copyall", on_click=_cb_toggle,
                  args=("dh_show_fulltext",), use_container_width=True, icon=":material/content_copy:")
    if ss.get("dh_show_fulltext"):
        st.code(_plain_text(sys_title, detail), language=None)

    for title, texts in detail["sections"]:
        if not texts:
            continue
        body = "".join(f"<p>{_e(t)}</p>" for t in texts)
        dark = " dh-dt-dark" if title.startswith("LANGKAH PRAKTIS") else ""
        st.markdown(f'<div class="dh-dt-sec{dark}"><div class="dh-dt-sec-t">{title}</div>{body}</div>',
                    unsafe_allow_html=True)

    if detail["params"]:
        rows = "".join(f"<tr><td>{_e(k)}</td><td>{_e(v)}</td></tr>" for k, v in detail["params"])
        st.markdown('<div class="dh-dt-sec"><div class="dh-dt-sec-t">PARAMETER KUNCI SISTEM INI</div>'
                    f'<table class="dh-dt-table">{rows}</table></div>', unsafe_allow_html=True)

    st.button("← Tutup & Kembali ke Cetak Biru Takdir", key="dhd_back", on_click=_cb_back,
              use_container_width=True)
