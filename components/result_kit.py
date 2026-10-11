"""
Komponen hasil bersama (REVISI03 Batch 4): hero, radar (HANYA dari skor asli), kartu insight expand,
kartu visual + Save PNG + WhatsApp. Tidak ada angka karangan: sistem tanpa skor numerik tidak dapat radar.
"""

import html
import math
import re
from urllib.parse import quote as urlquote

import streamlit as st

from utils.card_images import (card_filename_for_system, card_image_bytes_for_system,
                               card_image_data_uri_small, _resolve_relative_path)

_E = html.escape
_BF_NAMA = {"O": "Keterbukaan", "C": "Kedisiplinan", "E": "Ekstraversi", "A": "Keramahan", "N": "Sensitivitas"}
_DISC_NAMA = {"D": "Dominance", "I": "Influence", "S": "Steadiness", "C": "Conscientious"}
_LL_NAMA = {"WA": "Kata Afirmasi", "QT": "Waktu Bersama", "RG": "Hadiah", "AS": "Pelayanan", "PT": "Sentuhan"}
_MBTI_PAIR = (("E", "I", "Ekstraversi", "Introversi"), ("S", "N", "Sensing", "Intuisi"),
              ("T", "F", "Thinking", "Feeling"), ("J", "P", "Judging", "Perceiving"))


def quiz_axes(system, raw):
    """[(label, persen 0-100)] dari skor kuesioner ASLI, atau None kalau sistem ini tidak punya skor."""
    if not raw or raw.get("placeholder"):
        return None
    try:
        if system == "Big Five" and raw.get("scores"):
            return [(_BF_NAMA[k], round((v - 7) / 28 * 100)) for k, v in raw["scores"].items() if k in _BF_NAMA]
        if system == "Enneagram" and raw.get("counts"):
            return [(f"Tipe {k}", round(min(v, 4) / 4 * 100)) for k, v in sorted(raw["counts"].items())]
        if system == "DISC" and raw.get("counts"):
            tot = sum(raw["counts"].values()) or 1
            return [(_DISC_NAMA.get(k, k), round(v / tot * 100)) for k, v in raw["counts"].items()]
        if system == "Love Language" and raw.get("counts"):
            tot = sum(raw["counts"].values()) or 1
            return [(_LL_NAMA.get(k, k), round(v / tot * 100)) for k, v in raw["counts"].items()]
    except Exception:
        return None
    return None


def mbti_pairs(raw):
    """[(kiri, kanan, nama kiri, nama kanan, persen kiri)] dari counts MBTI asli, atau None."""
    c = (raw or {}).get("counts")
    if not c:
        return None
    out = []
    for a, b, na, nb in _MBTI_PAIR:
        t = (c.get(a, 0) + c.get(b, 0)) or 1
        out.append((a, b, na, nb, round(c.get(a, 0) / t * 100)))
    return out


def radar_svg(axes, w=440, h=300):
    """Radar polygon coklat transparan. axes = [(label, 0-100)], minimal 3 sumbu."""
    n = len(axes)
    if n < 3:
        return ""
    cx, cy, r = w / 2, h / 2 + 4, min(w, h) / 2 - 52
    def pt(i, v):
        a = -math.pi / 2 + i * 2 * math.pi / n
        return cx + r * v / 100 * math.cos(a), cy + r * v / 100 * math.sin(a)
    g = ""
    for ring in (25, 50, 75, 100):
        g += '<polygon class="rk-ring" points="' + " ".join("%.1f,%.1f" % pt(i, ring) for i in range(n)) + '"/>'
    for i in range(n):
        x, y = pt(i, 100)
        g += f'<line class="rk-ax" x1="{cx:.1f}" y1="{cy:.1f}" x2="{x:.1f}" y2="{y:.1f}"/>'
    poly = " ".join("%.1f,%.1f" % pt(i, v) for i, (_l, v) in enumerate(axes))
    g += f'<polygon class="rk-poly" points="{poly}"/>'
    for i, (lb, v) in enumerate(axes):
        x, y = pt(i, v)
        g += f'<circle class="rk-dot" cx="{x:.1f}" cy="{y:.1f}" r="4"/>'
        lx, ly = pt(i, 100 + 2600 / r)
        anchor = "middle" if abs(lx - cx) < 8 else ("start" if lx > cx else "end")
        g += (f'<text class="rk-lb" x="{lx:.1f}" y="{ly:.1f}" text-anchor="{anchor}">{_E(lb)}</text>'
              f'<text class="rk-v" x="{lx:.1f}" y="{ly + 12:.1f}" text-anchor="{anchor}">{v}%</text>')
    return f'<svg class="rk-radar" viewBox="0 0 {w} {h}" role="img" aria-label="Radar skor">{g}</svg>'


def pair_bars(pairs):
    rows = ""
    for a, b, na, nb, p in pairs:
        win_l = p >= 50
        rows += (f'<div class="rk-pr"><span class="{"on" if win_l else ""}">{a} · {_E(na)}</span>'
                 f'<div class="rk-pb"><i style="width:{p}%"></i></div>'
                 f'<span class="r {"" if win_l else "on"}">{_E(nb)} · {b}</span></div>')
    return f'<div class="rk-pairs">{rows}</div>'


def dashboard(system, raw):
    """HTML panel skor (radar / bar MBTI) atau '' kalau tidak ada skor asli."""
    pairs = mbti_pairs(raw) if system == "MBTI" else None
    if pairs:
        return ('<div class="rk-panel"><div class="rk-ph">📊 PROFIL SKORMU</div>' + pair_bars(pairs) +
                '<div class="rk-note">Persentase dihitung dari jawabanmu di kuesioner.</div></div>')
    axes = quiz_axes(system, raw)
    if not axes:
        return ""
    top = sorted(axes, key=lambda x: -x[1])[:2]
    badges = "".join(f'<span class="rk-bd">{_E(l)} <b>{v}%</b></span>' for l, v in top)
    return ('<div class="rk-panel"><div class="rk-ph">🕸️ RADAR SKORMU</div>' + radar_svg(axes) +
            f'<div class="rk-bds">Paling menonjol: {badges}</div>'
            '<div class="rk-note">Skor dihitung dari jawabanmu di kuesioner, bukan perkiraan.</div></div>')


def _first_sentence(t, n=150):
    t = re.sub(r"\s+", " ", (t or "").strip())
    m = re.match(r"(.+?[.!?])(\s|$)", t)
    s = m.group(1) if m else t
    return s if len(s) <= n else s[:n].rsplit(" ", 1)[0] + "…"


_ICON_RULES = [("blind", "👁️"), ("titik buta", "👁️"), ("shadow", "🌙"), ("sisi gelap", "🌙"), ("pr kecil", "🎯"),
               ("latihan", "🎯"), ("nasihat", "🧭"), ("kompas", "🧭"), ("karier", "💼"), ("karir", "💼"),
               ("keuangan", "💰"), ("rezeki", "💼"), ("asmara", "💖"), ("hubungan", "💖"), ("utama", "🔷"), ("siapa", "🔷")]


def icon_for(title, default="🧩"):
    """Ikon seragam per jenis kartu aspek (dipakai kalau ikon bawaan kosong / generik 🧩)."""
    t = (title or "").lower()
    for k, ic in _ICON_RULES:
        if k in t:
            return ic
    return default


def insight_cards(items):
    """items = [(ikon, judul, [teks...])]. Kartu grid: sorotan 1 kalimat + 'Baca selengkapnya' (expand)."""
    out = ""
    for ic, title, texts in items:
        if not ic or ic == "🧩":
            ic = icon_for(title, ic or "🧩")
        texts = [t for t in texts if t]
        if not texts:
            continue
        rest = "".join(f"<p>{_E(t)}</p>" for t in texts)
        out += (f'<details class="rk-ic"><summary><span class="rk-ico">{ic}</span><div><b>{_E(title)}</b>'
                f'<em>{_E(_first_sentence(texts[0]))}</em></div><i>Baca ▾</i></summary><div class="rk-body">{rest}</div></details>')
    return f'<div class="rk-grid">{out}</div>' if out else ""


def has_card(system, raw):
    if not raw or raw.get("placeholder"):
        return False  # hasil belum valid -> jangan pinjam kartu generik
    try:
        return bool(_resolve_relative_path(system, raw))
    except Exception:
        return False


def card_visual(system, raw, nama, caption, key):
    """Kartu visual sistem (assets/cards) + Simpan PNG + Share WhatsApp. Return True kalau kartunya ada."""
    uri = card_image_data_uri_small(_resolve_relative_path(system, raw) or "x/none") if has_card(system, raw) else None
    if not uri:
        return False
    st.markdown(f'<div class="dh-dt-imgwrap"><img class="dh-dt-img" src="{uri}" alt="Kartu {_E(system)} {_E(nama)}"></div>',
                unsafe_allow_html=True)
    png = card_image_bytes_for_system(system, raw)
    with st.container(key=f"{key}_cardacts"):
        c1, c2 = st.columns(2, gap="small")
        with c1:
            if png:
                st.download_button("Simpan PNG", data=png, file_name=card_filename_for_system(system, raw),
                                   mime="image/png", key=f"{key}_png", on_click="ignore", use_container_width=True,
                                   icon=":material/download:")
        with c2:
            st.link_button("WhatsApp", f"https://wa.me/?text={urlquote(caption)}", key=f"{key}_wa",
                           use_container_width=True, icon=":material/share:")
    return True


def score_panels(pairs, heading="📊 PROFIL SKOR KEPRIBADIAN", cls="rk-ph"):
    """pairs = [(sistem, raw)]. Panel skor asli: bar MBTI satu baris penuh, radar lain 2 per baris."""
    ph = [(s, dashboard(s, r)) for s, r in pairs if r]
    ph = [(s, h) for s, h in ph if h]
    if not ph:
        return
    st.markdown(f'<div class="{cls}" style="margin:8px 2px 8px">{heading}</div>', unsafe_allow_html=True)
    full = [h for s, h in ph if s == "MBTI"]
    rest = [h for s, h in ph if s != "MBTI"]
    for h in full:
        st.markdown(h, unsafe_allow_html=True)
    for i in range(0, len(rest), 2):
        cols = st.columns(2, gap="small")
        for col, h in zip(cols, rest[i:i + 2]):
            with col:
                st.markdown(h, unsafe_allow_html=True)


def sections_text(title, sub, sections):
    """[(judul, [baris])] -> teks polos untuk Salin."""
    out = [title.upper(), sub, ""]
    for t, xs in sections:
        out += [t.upper(), *[f"- {x}" for x in (xs or ["-"])], ""]
    out.append("By Destiny Reveal")
    return "\n".join(out)


def actions(prefix, close, pdf=None, text=None, png=None, wa=None, name="hasil", extra=None, clean=True, close_label="Tutup", side=None):
    """Footer hasil seragam (REVISI03): PDF | Salin, PNG | WhatsApp, [extra], Tutup coklat.
    close = (callback, args). pdf/png = bytes. text = str. wa = caption WhatsApp. extra = fungsi opsional (tombol tambahan)."""
    from components.modal_detail import copy_button
    cells = []
    if pdf:
        cells.append(lambda: st.download_button("Download PDF", pdf, file_name=f"{name}.pdf", mime="application/pdf",
                                                key=f"{prefix}_pdf", use_container_width=True, on_click="ignore",
                                                icon=":material/download:"))
    if text:
        cells.append(lambda: copy_button(text, "📋 Salin Teks", f"{prefix}_copy", fs=13, h=44) if clean else copy_button(text, "📋 Salin Teks", f"{prefix}_copy", fs=12.5, h=48, brown=True))
    if png:
        cells.append(lambda: st.download_button("Save Image", png, file_name=f"{name}.png", mime="image/png",
                                                key=f"{prefix}_png", use_container_width=True, on_click="ignore",
                                                icon=":material/image:"))
    if wa:
        cells.append(lambda: st.link_button("Share WhatsApp", f"https://wa.me/?text={urlquote(wa)}",
                                            use_container_width=True, icon=":material/share:"))
    if side:  # tombol tambahan sejajar dengan baris atas (mis. "Scan Mode Lain")
        s_label, s_key, s_cb = side
        cells.append(lambda: st.button(s_label, key=s_key, on_click=s_cb, use_container_width=True))
    with st.container(key="dhcl_acts" if clean else "dhbp_actions"):
        for i in range(0, len(cells), 2):
            row = cells[i:i + 2]
            cols = st.columns(len(row), gap="small")
            for col, fn in zip(cols, row):
                with col:
                    fn()
        if extra:
            extra()
        cb, args = close
        st.button(close_label, key=f"{prefix}_done", on_click=cb, args=args, use_container_width=True)
