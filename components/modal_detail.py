"""
Sub-modal "Detail Sistem" (UI7): kartu takdir + uraian lengkap satu sistem.
Dibuka dari tombol "Lihat & Simpan Kartu ..." di hasil Mode 1. Bukan dialog baru
(Streamlit cuma izinkan 1 dialog) — ini satu langkah di dalam _flow_dialog.

Sumber isi uraian (5 sistem Mode 1):
  1. JSON profil baru lewat content/profile_loader.py: sections A-F (G-M = Deep Blueprint, tidak dirender di sini)
  2. Cadangan: kamus konten Python (build_display_data) HANYA kalau entri belum ada di JSON baru
     (mati kalau profile_loader.ALLOW_LEGACY_FALLBACK = False). Judul/tagline tetap dari kamus.
"""

import html
import json
from urllib.parse import quote as urlquote

import streamlit as st
import streamlit.components.v1 as components

from components.combo import build_combo
from components.flow_state import STEP_RESULT, set_step
from content.profile_loader import ALLOW_LEGACY_FALLBACK, MODE1, get_profile
from content.result_builder import build_display_data
from utils.card_images import card_filename_for_system, card_image_bytes_for_system, card_image_for_system

ZODIAK_GLYPH = {
    "Aries": "♈", "Taurus": "♉", "Gemini": "♊", "Cancer": "♋", "Leo": "♌", "Virgo": "♍",
    "Libra": "♎", "Scorpio": "♏", "Sagittarius": "♐", "Capricorn": "♑", "Aquarius": "♒", "Pisces": "♓",
}

# (judul section, [key kandidat berurutan]) — semua key kandidat yang ada digabung
SECTIONS = [
    ("🪐", "ASPEK UTAMA & ESENSI JIWA", ["aspek_utama", "siapa_kamu"], "ivory"),
    ("💼", "KARIER, PELUANG USAHA & POTENSI FINANSIAL", ["karier_dan_keuangan", "karir", "peta_karier", "keuangan"], "white"),
    ("🤍", "ASMARA, DINAMIKA PERCINTAAN & PASANGAN JIWA", ["asmara_dan_hubungan", "asmara", "panduan_hubungan"], "sand"),
    ("🛡️", "KEKUATAN KARAKTER & YANG PERLU DIJAGA", ["kekuatan_karakter", "kekuatan_yang_perlu_dijaga"], "sage"),
    ("⚠️", "PR BAYANGAN (SHADOW WORK) & HAL YANG PERLU DIWASPADAI", ["shadow_work", "shadow_side", "blindspot"], "soft"),
    ("💡", "LANGKAH PRAKTIS JIWA & NASIHAT STRATEGIS", ["nasihat_strategis", "pr_kecil_buat_kamu"], "dark"),
]


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
    """Susun data detail satu sistem. Return dict {title, sections:[(icon, judul, [teks...], tone)], params:[(k,v)]} atau None.
    Mode 1 = seksi A-F dari JSON baru. Entri yang belum ada di JSON baru jatuh ke kamus lama (lihat ALLOW_LEGACY_FALLBACK)."""
    disp = build_display_data(system, raw)  # judul/tagline + cadangan
    prof = get_profile(system, raw)
    if prof and all(h in prof["sections"] for h in MODE1):
        sections = [(icon, title, [prof["sections"][h]], tone) for (icon, title, _k, tone), h in zip(SECTIONS, MODE1)]
        return {"title": (disp or {}).get("title") or prof["key"],
                "quote": prof["free"].get("quote") or (disp or {}).get("quote", ""),
                "tagline": (disp or {}).get("tagline", ""), "sections": sections,
                "params": _as_rows(prof["meta"].get("parameter_kunci")) or _param_rows(system, raw)}
    if not disp or not ALLOW_LEGACY_FALLBACK:
        return None

    flat = {"siapa_kamu": disp.get("p1"), "kekuatan_yang_perlu_dijaga": disp.get("p2"),
            "pr_kecil_buat_kamu": disp.get("p3")}
    flat.update({k: v for k, v in (disp.get("domains") or {}).items() if v})
    sections = []
    for icon, title, keys, tone in SECTIONS:
        texts = []
        for k in keys:
            v = flat.get(k)
            if isinstance(v, str) and v.strip():
                texts.append(v.strip())
            elif isinstance(v, list):
                texts.extend(str(x).strip() for x in v if str(x).strip())
        sections.append((icon, title, texts, tone))
    return {"title": disp["title"], "quote": disp.get("quote", ""), "tagline": disp.get("tagline", ""),
            "sections": sections, "params": _param_rows(system, raw)}


def _plain_text(system_label, detail, combo=()):
    out = [f"Analisis Lengkap: {system_label}", detail["title"], ""]
    for _i, title, texts, _t in detail["sections"]:
        if texts:
            out += [title, *texts, ""]
    if combo:
        out += ["COMBO: KETIKA VARIABEL-VARIABELMU BERTEMU", ""]
        for b in combo:
            out += [b["title"], b["text"], ""]
    if detail["params"]:
        out += ["PARAMETER KUNCI SISTEM INI", *[f"{k}: {v}" for k, v in detail["params"]]]
    return "\n".join(out).strip()


def render_combo_card(sys_title, blocks):
    """Kartu Combo border pelangi (dipakai Analisis Lengkap Mode 1 dan hasil Solo Reveal)."""
    if not blocks:
        return
    body = "".join(f'<span class="dh-dt-cb-h">{_e(b["title"])}</span><p>{_e(b["text"])}</p>' for b in blocks)
    st.markdown('<div class="dh-dt-combo"><div class="dh-dt-sec-t"><span class="dh-dt-ico">🌈</span>'
                'COMBO: KETIKA VARIABEL-VARIABELMU BERTEMU</div>'
                f'<div class="dh-dt-cb-sub">Perpaduan beberapa unsur dalam hasil {_e(sys_title)} milikmu.</div>{body}</div>',
                unsafe_allow_html=True)


# ── callback ─────────────────────────────────────────────────────
def cb_open_detail(system):
    st.session_state.dh_detail_system = system
    set_step("detail")


def _cb_back():
    set_step(STEP_RESULT)


def _e(text):
    return html.escape(str(text)).replace("\n", "<br>")


def copy_button(text, label, key, fs=13, h=40):
    """Tombol salin MURNI ke clipboard (JS). Layar gak berubah, cuma teks tombol
    jadi '✓ Tersalin!' 2 detik."""
    payload = json.dumps(text).replace("</", "<\\/")
    components.html(
        '<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@700&display=swap" rel="stylesheet">'
        "<style>html,body{margin:0;background:transparent}"
        "button{width:100%;height:{H}px;border-radius:100px;border:1px solid #E9C9A8;background:#FFFFFF;"
        "color:#C25E00;font:700 {FS}px 'Plus Jakarta Sans',system-ui,sans-serif;cursor:pointer;transition:background .15s}"
        "button:hover{background:#FFF6EA}button.ok{background:#EAF3EC;border-color:#BBD4C0;color:#4A6B53}</style>"
        .replace("{FS}", str(fs)).replace("{H}", str(h)) +
        f'<button id="b" type="button">{html.escape(label)}</button>'
        f"<script>var T={payload},L={json.dumps(label)},b=document.getElementById('b');"
        "function ok(){b.textContent='✓ Tersalin!';b.className='ok';setTimeout(function(){b.textContent=L;b.className='';},2000)}"
        "function fb(){var t=document.createElement('textarea');t.value=T;t.style.position='fixed';t.style.opacity=0;"
        "document.body.appendChild(t);t.select();try{document.execCommand('copy');ok()}catch(e){}document.body.removeChild(t)}"
        "b.onclick=function(){if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(T).then(ok,fb)}else{fb()}};"
        "</script>",
        height=h + 4,
    )


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
    sys_title = nm.title()
    quote = detail["quote"]
    img_uri = card_image_for_system(system, raw)
    img = card_image_bytes_for_system(system, raw)

    st.markdown('<div style="height:30px;"></div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="dh-step dh-step-detail"></div>'
        '<div class="dh-dt-eyebrow">KARTU TAKDIR &amp; ANALISIS LENGKAP</div>'
        f'<div class="dh-dt-title">{_e(num)}. {_e(sys_title)} · {_e(nama)}</div>'
        '<div class="dh-dt-subtitle">Simpan gambar kartu untuk story sosial mediamu, dan scroll ke bawah '
        'untuk membaca versi analisis lengkapnya.</div>', unsafe_allow_html=True)

    if img_uri:  # kartu = file gambar dari assets/cards/, ditampilkan utuh (portrait)
        st.markdown(f'<div class="dh-dt-imgwrap"><img class="dh-dt-img" src="{img_uri}" alt="Kartu {_e(item["short"])}"></div>',
                    unsafe_allow_html=True)
    else:  # fallback kalau file kartu belum ada
        st.markdown(
            '<div class="dh-dt-card"><div class="dh-dt-brand">✦ DESTINY REVEAL ✦</div>'
            f'<div class="dh-dt-sys">{_e(num)} · {_e(sys_title)}</div>'
            f'<div class="dh-dt-name">{_e(item["short"])}</div><div class="dh-dt-sub">{_e(item["tag"])}</div>'
            f'<div class="dh-dt-foot"><span>Milik: <b>{_e(nama)}</b></span><span>destinyreveal.id</span></div></div>',
            unsafe_allow_html=True)

    if quote:  # kutipan di antara kartu dan tombol aksi
        st.markdown(f'<div class="dh-dt-quotebox">&ldquo;{_e(quote)}&rdquo;</div>', unsafe_allow_html=True)

    caption = (f'"{quote}"\n\n{nama} · {item["short"]}\nCek takdirmu di destinyreveal.id #DestinyReveal'
               if quote else f'{nama} · {item["short"]}\nCek takdirmu di destinyreveal.id #DestinyReveal')
    with st.container(key="dhd_actions"):
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
                           key="dhd_wa", use_container_width=True, icon=":material/share:")
        copy_button(caption, "📋 Salin Teks Kutipan untuk Caption", "dhd_copyq")

    st.markdown('<div class="dh-dt-sep"></div>'
                '<div class="dh-dt-eyebrow">URAIAN KOMPREHENSIF VERSI LENGKAP</div>', unsafe_allow_html=True)
    h1, h2 = st.columns([1.5, 1], gap="small", vertical_alignment="center")
    with h1:
        st.markdown(f'<div class="dh-dt-h">Analisis Lengkap: {_e(sys_title)}</div>', unsafe_allow_html=True)
    with h2:
        copy_button(_plain_text(sys_title, detail, build_combo(system, raw)), "📋 Salin Seluruh Analisis Lengkap", "dhd_copyall")

    for icon, title, texts, tone in detail["sections"]:
        if not texts:
            continue
        body = "".join(f"<p>{_e(t)}</p>" for t in texts)
        st.markdown(f'<div class="dh-dt-sec dh-dt-{tone}"><div class="dh-dt-sec-t"><span class="dh-dt-ico">{icon}</span>'
                    f'{title}</div>{body}</div>', unsafe_allow_html=True)

    render_combo_card(sys_title, build_combo(system, raw))  # kartu terakhir setelah seksi hasil: border pelangi

    if detail["params"]:
        cells = "".join(f'<div class="dh-dt-pm"><span>{_e(k)}</span><b>{_e(v)}</b></div>' for k, v in detail["params"])
        st.markdown('<div class="dh-dt-sec dh-dt-params"><div class="dh-dt-sec-t"><span class="dh-dt-ico">🧭</span>'
                    f'PARAMETER KUNCI SISTEM INI</div><div class="dh-dt-pgrid">{cells}</div></div>',
                    unsafe_allow_html=True)

    st.button("← Tutup & Kembali ke Cetak Biru Takdir", key="dhd_back", on_click=_cb_back,
              use_container_width=True)
