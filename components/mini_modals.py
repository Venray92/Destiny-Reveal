"""
4 modal ringkas fitur gratis (UI11): Ramalan Harian Gratis, Tarot 1 Kartu Harian,
Preview Zodiak, Streak & Reward. Dibuka dari kartu "GRATIS" di section Jelajahi
lewat jembatan JS (class .dh-open-modal + data-modal) -> tombol tersembunyi di navbar.py.

Aturan tutup: HANYA tombol X. Klik backdrop & Esc diblok (marker .dh-nodismiss,
listener-nya ada di _BRIDGE_JS navbar.py).
DUMMY: koin, klaim streak, dan isi ramalan harian (daily.json) belum ada backend.
"""

import base64
import html
import json
import random
from datetime import datetime, timedelta, timezone
from functools import lru_cache
from pathlib import Path

import streamlit as st

from content.result_builder import SHIO_CONTENT, TAROT_CONTENT, ZODIAK_CONTENT
from engine.tarot import TAROT_MAJOR_ARCANA
from engine.zodiak import _RENTANG_ZODIAK
from utils.card_images import card_image_data_uri

_ROOT = Path(__file__).resolve().parent.parent
_ZODIAK_JSON = _ROOT / "content" / "interpretations" / "zodiak" / "zodiak_profile.json"
_COVER = _ROOT / "assets" / "images" / "sunmoon.jpg"

GLYPH = {
    "Aries": "♈", "Taurus": "♉", "Gemini": "♊", "Cancer": "♋", "Leo": "♌", "Virgo": "♍",
    "Libra": "♎", "Scorpio": "♏", "Sagittarius": "♐", "Capricorn": "♑", "Aquarius": "♒", "Pisces": "♓",
}
ZODIAK_LIST = list(GLYPH)
SHIO_LIST = ["Tikus", "Kerbau", "Macan", "Kelinci", "Naga", "Ular", "Kuda", "Kambing", "Monyet", "Ayam", "Anjing", "Babi"]
SHIO_EMOJI = {"Tikus": "🐭", "Kerbau": "🐂", "Macan": "🐯", "Kelinci": "🐰", "Naga": "🐲", "Ular": "🐍",
              "Kuda": "🐴", "Kambing": "🐐", "Monyet": "🐵", "Ayam": "🐔", "Anjing": "🐶", "Babi": "🐷"}
_BLN = ["", "Jan", "Feb", "Mar", "Apr", "Mei", "Jun", "Jul", "Agu", "Sep", "Okt", "Nov", "Des"]
_WIB = timezone(timedelta(hours=7))


def today_wib():
    return datetime.now(_WIB).date().isoformat()


def _e(t):
    return html.escape(str(t)).replace("\n", "<br>")


@lru_cache(maxsize=1)
def _zodiak_json():
    try:
        return json.loads(_ZODIAK_JSON.read_text(encoding="utf-8")).get("data", {})
    except (OSError, ValueError):
        return {}


def _zodiak_info(sign):
    """Data Preview Zodiak: rentang tanggal & elemen dari engine, teks dari JSON (sections.free)."""
    rng = next((r for r in _RENTANG_ZODIAK if r[2] == sign), None)
    free = (_zodiak_json().get(sign, {}).get("sections", {}) or {}).get("free", {}) or {}
    fallback = ZODIAK_CONTENT.get(sign, {})
    tgl = f"{rng[0][1]} {_BLN[rng[0][0]]} - {rng[1][1]} {_BLN[rng[1][0]]}" if rng else ""

    def _val(attr, default):
        v = free.get(attr) or default
        return v.split(":", 1)[1].strip() if ":" in v else v

    return {
        "tgl": tgl, "elemen": rng[3] if rng else "",
        "siapa": free.get("siapa_kamu") or fallback.get("p1", ""),
        "modality": _val("atribut_1", rng[4] if rng else ""),
        "planet": _val("atribut_2", rng[5] if rng else ""),
        "quote": (free.get("quote") or fallback.get("quote", "")).strip('"“” '),
    }


def _first_sentences(text, n=2):
    parts = (text or "").split(". ")
    out = ". ".join(parts[:n]).strip()
    return out if out.endswith((".", "!", "?")) else out + "."


def _head():
    email = st.session_state.get("dh_email")
    badge = (f'✓ Akun Terhubung ({_e(email)})' if email else "Belum masuk akun")
    st.markdown(
        '<div class="dh-step dh-step-mini"></div><div class="dh-nodismiss"></div>'
        f'<div class="dh-mn-status"><span>Status:</span><b class="{"" if email else "off"}">{badge}</b></div>'
        '<div class="dh-mn-div"></div>', unsafe_allow_html=True)


def _title(icon_html, title, sub):
    st.markdown(f'<div class="dh-mn-title"><div class="dh-mn-ico">{icon_html}</div>'
                f'<div><div class="dh-mn-h">{title}</div><div class="dh-mn-sub">{sub}</div></div></div>',
                unsafe_allow_html=True)


def _open_reveal():
    """Tutup modal ini lalu buka modal Reveal (lihat modal.reopen_if_pending)."""
    st.session_state.dh_open_reveal = True
    st.rerun()


_COIN_MSG = "Fitur Stardust belum tersedia — masih tahap pengembangan 🚧"


def _soon(msg):
    st.toast(msg)


# ═══════════ 1. RAMALAN HARIAN GRATIS ═══════════
_DAILY_JSON = _ROOT / "content" / "interpretations" / "daily" / "daily.json"
_WARNA = ["Merah Bata (Terracotta)", "Biru Laut", "Hijau Sage", "Kuning Madu", "Ungu Lavender", "Putih Gading", "Emas", "Hitam Pekat"]


@lru_cache(maxsize=1)
def _daily_json():
    try:
        return json.loads(_DAILY_JSON.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def _daily_entry(kind, name, day):
    """Ambil entri harian dari daily.json. Format yang didukung (data.<kind>.<nama>):
    - dict per tanggal: {"2026-10-03": {...}}  ATAU  - list yang diputar per hari (urut tanggal)
    Field entri: pesan, angka_hoki, warna_hoki."""
    d = _daily_json()
    d = d.get("data", d)
    node = (d.get(kind, {}) or {}).get(name)
    if isinstance(node, dict):
        node = node.get(day) or node.get("harian")
    if isinstance(node, list) and node:
        node = node[datetime.fromisoformat(day).toordinal() % len(node)]
    return node if isinstance(node, dict) else None


def get_daily_reading(kind, name, day):
    """Return {pesan, angka, warna}: PESAN SINGKAT harian (1-2 kalimat), bukan profil statis.
    Sumber: daily.json. DUMMY kalau file belum ada: pesan = 2 kalimat 'Untuk Hari Ini' kamus konten,
    angka/warna hoki dibuat deterministik dari nama+tanggal."""
    e = _daily_entry(kind, name, day)
    if e and e.get("pesan"):
        return {"pesan": _first_sentences(e["pesan"], 2), "angka": str(e.get("angka_hoki", "")),
                "warna": str(e.get("warna_hoki", ""))}
    c = (ZODIAK_CONTENT if kind == "zodiak" else SHIO_CONTENT).get(name, {})
    seed = random.Random(f"{kind}{name}{day}")
    n1 = seed.randint(1, 9)
    return {"pesan": _first_sentences(c.get("p3", ""), 1), "angka": f"{n1} & {n1 * 3}", "warna": seed.choice(_WARNA)}


def _cb_daily_tab(tab):
    st.session_state.dh_daily_tab = tab
    st.session_state.dh_daily_pick = None


def _cb_daily_pick(name):
    st.session_state.dh_daily_pick = name


def _cb_daily_open():
    ss = st.session_state
    ss.dh_daily_lock = {"date": today_wib(), "kind": ss.dh_daily_tab, "name": ss.dh_daily_pick}


@st.dialog("Ramalan Harian Gratis", width="small")
def daily_dialog():
    ss = st.session_state
    _head()
    _title("🌅", "Ramalan Harian Gratis", "1x per hari · Pilih Zodiak atau Shio kelahiranmu")
    lock = ss.get("dh_daily_lock")
    if lock and lock.get("date") == today_wib():  # sudah dipilih hari ini -> terkunci sampai 00:00 WIB
        kind, name = lock["kind"], lock["name"]
        r = get_daily_reading(kind, name, lock["date"])
        label = "Zodiak" if kind == "zodiak" else "Shio"
        sym = GLYPH.get(name, "") + "\ufe0e" if kind == "zodiak" else SHIO_EMOJI.get(name, "")
        st.markdown(
            '<div class="dh-dr-quota"><span class="dh-dr-ck">✓</span><div>'
            '<b>Kuota Gratis Hari Ini Sudah Digunakan</b>'
            f'<span>Membaca: {sym} {label} {_e(name)} (Reset besok 00:00)</span></div>'
            '<em>Terkunci</em></div>'
            f'<div class="dh-dr-msg"><div class="dh-dr-msghead"><b>{label} {_e(name)}</b><span>Pesan Hari Ini</span></div>'
            f'<p>{_e(r["pesan"])}</p>'
            f'<div class="dh-dr-foot"><div>Angka Hoki: <b>{_e(r["angka"])}</b></div>'
            f'<div>Warna Hoki: <b>{_e(r["warna"])}</b></div></div></div>',
            unsafe_allow_html=True)
        with st.container(key="dhdy_lock"):
            st.markdown('<div class="dh-dr-blur"><p>💼 Karier: Peluang kerja sama baru terbuka lewat obrolan yang kamu mulai hari ini…</p>'
                        '<p>💗 Asmara: Percakapan jujur dengan orang terdekat membawa suasana yang lebih hangat…</p>'
                        '<p>💡 Nasihat: Tuntaskan satu hal kecil sebelum memulai hal baru supaya energimu tidak pecah…</p></div>',
                        unsafe_allow_html=True)
            st.button("🔒 Buka Analisis Lengkap — 50 SD", key="dhdy_unlock", type="primary",
                      on_click=_soon, args=(_COIN_MSG,))
            st.markdown('<div class="dh-dr-sub">Membongkar detail karier, dinamika asmara, dan nasihat langkah konkret hari ini.</div>',
                        unsafe_allow_html=True)
        with st.container(key="dhdy_swap"):
            st.markdown('<div class="dh-dr-swaptxt">Mau intip ramalan zodiak atau shio lain hari ini?</div>',
                        unsafe_allow_html=True)
            st.button("Ganti Pilihan / Buka Sistem Lain (50 SD) →", key="dhdy_swapbtn", on_click=_soon, args=(_COIN_MSG,))
        if st.button("Sinkronkan dengan Weton & Numerologi Lengkap →", key="dhdy_sync", use_container_width=True):
            _open_reveal()
        return

    tab = ss.setdefault("dh_daily_tab", "zodiak")
    items = ZODIAK_LIST if tab == "zodiak" else SHIO_LIST
    if ss.get("dh_daily_pick") not in items:
        ss.dh_daily_pick = items[0]
    with st.container(key="dhdy_tabs"):
        c1, c2 = st.columns(2, gap="small")
        with c1:
            st.button("♈︎ Zodiak Barat", key="dhdy_tab_zodiak", on_click=_cb_daily_tab, args=("zodiak",),
                      type="primary" if tab == "zodiak" else "secondary", use_container_width=True)
        with c2:
            st.button("🐍 Shio Timur", key="dhdy_tab_shio", on_click=_cb_daily_tab, args=("shio",),
                      type="primary" if tab == "shio" else "secondary", use_container_width=True)
    st.markdown(f'<div class="dh-mn-lab2">Pilih 1 {"Rasi Zodiak" if tab == "zodiak" else "Shio"} Kelahiranmu:</div>',
                unsafe_allow_html=True)
    with st.container(key="dhdy_grid"):
        for row in range(3):
            cols = st.columns(4, gap="small")
            for col, name in zip(cols, items[row * 4:(row + 1) * 4]):
                with col:
                    st.button(name, key=f"dhdy_pick_{tab}_{name}", on_click=_cb_daily_pick, args=(name,),
                              type="primary" if ss.dh_daily_pick == name else "secondary", use_container_width=True)
    st.markdown('<div class="dh-mn-notice"><b>ⓘ Ketentuan Kuota Ramalan Gratis:</b>'
                'Kamu hanya dapat memilih 1 tanda (Zodiak / Shio) per hari. Hasil tersimpan otomatis dan sistem '
                'terkunci hingga pergantian hari (00:00 WIB).</div>', unsafe_allow_html=True)
    label = "Zodiak" if tab == "zodiak" else "Shio"
    st.button(f"✨ Buka Ramalan {label} {ss.dh_daily_pick} Hari Ini", key="dhdy_cta", type="primary",
              use_container_width=True, on_click=_cb_daily_open)


# ═══════════ 2. TAROT 1 KARTU HARIAN ═══════════
@lru_cache(maxsize=1)
def _cover_uri():
    if not _COVER.is_file():
        return None
    return "data:image/jpeg;base64," + base64.b64encode(_COVER.read_bytes()).decode("ascii")


def _cb_tarot_draw():
    # kartu tetap sepanjang hari: kalau sudah ada tarikan hari ini, pakai yang sama
    cur = st.session_state.get("dh_tarot_draw")
    if not cur or cur.get("date") != today_wib():
        st.session_state.dh_tarot_draw = {"date": today_wib(), "kartu": random.choice(TAROT_MAJOR_ARCANA)}


@st.dialog("Tarot 1 Kartu Harian", width="small")
def tarot_dialog():
    ss = st.session_state
    _head()
    _title("🃏", "Tarot 1 Kartu Harian", "Tarik 1 kartu sinkronisitas kosmik murni untuk memandu energimu hari ini.")
    draw = ss.get("dh_tarot_draw")
    if not draw or draw.get("date") != today_wib():
        uri = _cover_uri()
        with st.container(key="dhtr_cover"):
            st.markdown(f'<img class="dh-tr-img" src="{uri}" alt="Kartu tarot">' if uri else
                        '<div class="dh-tr-img dh-tr-ph">🂠</div>', unsafe_allow_html=True)
            st.button("Tarik kartu", key="dhtr_draw", on_click=_cb_tarot_draw)
        st.markdown('<div class="dh-tr-hint">👆 Klik kartu untuk membuka kartumu hari ini</div>'
                    '<div class="dh-tr-cap">Kartu sinkronisitas tetap sepanjang hari ini (tanpa kocok ulang)</div>',
                    unsafe_allow_html=True)
        return

    kartu = draw["kartu"]
    idx = TAROT_MAJOR_ARCANA.index(kartu)
    c = TAROT_CONTENT.get(kartu, {})
    nama, _, arti = (c.get("title") or kartu).partition(" — ")
    uri = next((u for u in [card_image_data_uri(f"tarot/{idx:02d}_{kartu}.png")] if u), None)
    img = f'<img class="dh-tr-img" src="{uri}" alt="{_e(nama)}">' if uri else '<div class="dh-tr-img dh-tr-ph">🂠</div>'
    st.markdown(
        f'<div class="dh-tr-wrap">{img}<div class="dh-tr-over"><b>ARCANA #{idx}</b>'
        f'<div>{_e(nama)}{f" ({_e(arti)})" if arti else ""}</div></div></div>'
        '<div class="dh-tr-cap">Kartu sinkronisitas tetap sepanjang hari ini (tanpa kocok ulang)</div>'
        f'<div class="dh-mn-msg"><div class="dh-mn-msghead"><span>PESAN INTI HARI INI:</span><b>{_e(arti or nama)}</b></div>'
        f'<p>{_e(_first_sentences(c.get("p1", ""), 3))}</p></div>',
        unsafe_allow_html=True)
    with st.container(key="dhtr_pay"):
        st.markdown('<div class="dh-mn-paywall"><b>Mau Tau Lebih Dalam?</b>'
                    '<span>Bongkar dimensi karier, dinamika asmara, dan peringatan energi tersembunyi kartu ini.</span></div>',
                    unsafe_allow_html=True)
        st.button("🔒 Mau Tau Lebih Dalam? (50 SD)", key="dhtr_unlock", type="primary", use_container_width=True,
                  on_click=_soon, args=(_COIN_MSG,))
    if st.button("Sinkronkan Kartu Ini dengan Zodiak & Wetonmu di Scan →", key="dhtr_sync", use_container_width=True):
        _open_reveal()


# ═══════════ 3. PREVIEW ZODIAK ═══════════
def _cb_pv_pick(name):
    st.session_state.dh_pv_pick = name


@st.dialog("Preview Zodiak", width="small")
def preview_dialog():
    ss = st.session_state
    _head()
    pick = ss.setdefault("dh_pv_pick", "Aries")
    _title(f'<span class="dh-mn-glyph">{GLYPH[pick]}&#xFE0E;</span>', "Preview Zodiak",
           "Pilih 1 dari 12 rasi bintang untuk melihat esensi jiwamu")
    with st.container(key="dhpv_grid"):
        for row in range(2):
            cols = st.columns(6, gap="small")
            for col, name in zip(cols, ZODIAK_LIST[row * 6:(row + 1) * 6]):
                with col:
                    st.button(f"{GLYPH[name]}\ufe0e  \n{name}", key=f"dhpv_pick_{name}", on_click=_cb_pv_pick,
                              args=(name,), type="primary" if pick == name else "secondary", use_container_width=True)
    d = _zodiak_info(pick)
    st.markdown(
        f'<div class="dh-mn-card"><div class="dh-mn-cardhead"><span class="dh-mn-sym dh-mn-glyph">{GLYPH[pick]}&#xFE0E;</span>'
        f'<div><div class="dh-mn-name">{pick}</div><div class="dh-mn-meta">{_e(d["tgl"])} · Elemen {_e(d["elemen"])}</div></div>'
        '<span class="dh-mn-free">Gratis</span></div>'
        f'<div class="dh-mn-lab">SIAPA KAMU:</div><p>{_e(_first_sentences(d["siapa"], 3))}</p>'
        f'<div class="dh-mn-micro"><div><span>MODALITY:</span><b>{_e(d["modality"])}</b></div>'
        f'<div><span>PLANET PENGUASA:</span><b>{_e(d["planet"])}</b></div></div>'
        f'<div class="dh-mn-quote2"><b>QUOTE:</b> &ldquo;{_e(d["quote"])}&rdquo;</div></div>'
        '<div class="dh-mn-lock"><div class="dh-mn-blur"><i></i><i></i><i></i></div><div class="dh-mn-lockbody">'
        f'<span class="dh-mn-lockico">🔒</span><b>Buka Analisis Lengkap {pick}</b>'
        '<span>Membongkar kekuatan sejati, PR batin (shadow work), serta insight karier, asmara &amp; keuangan.</span></div></div>',
        unsafe_allow_html=True)
    st.button("🔒 Buka Analisis Lengkap — 50 SD", key="dhpv_unlock", type="primary", use_container_width=True,
              on_click=_soon, args=(_COIN_MSG,))
    if st.button("Sinkronkan dengan Weton & Shio Milikmu →", key="dhpv_sync", use_container_width=True):
        _open_reveal()


# ═══════════ 4. STREAK & REWARD (UI statis) ═══════════
@st.dialog("Streak & Reward", width="small")
def streak_dialog():
    email = st.session_state.get("dh_email")
    _head()
    ms = [("5 Hari", "🎁 50 SD", True), ("7 Hari", "💎 100 SD", False), ("30 Hari", "👑 1 Bln VIP", False),
          ("100 Hari", "🏆 Lifetime", False)]
    cards = "".join(f'<div class="dh-sk-ms{" on" if on else ""}"><b>{a}</b><span>{b}</span></div>' for a, b, on in ms)
    st.markdown(
        '<div class="dh-sk-flame">🔥</div><div class="dh-sk-title">Streak &amp; Reward</div>'
        '<div class="dh-mn-notice dh-sk-info"><b>📌 Cara Menaikkan Streak:</b>'
        'Buka website tiap hari buat naikin streak (+1 setiap kali kamu membuka fitur gratis harian).</div>'
        '<div class="dh-sk-prog"><div class="dh-sk-proghead"><b>5 / 7 Hari menuju 50 SD Gratis</b><span>71%</span></div>'
        '<div class="dh-sk-bar"><i style="width:71%"></i></div></div>'
        f'<div class="dh-sk-grid">{cards}</div>', unsafe_allow_html=True)
    st.button("Klaim Hadiah Hari Ini (+50 SD)", key="dhsk_claim", type="primary", use_container_width=True)
    st.markdown('<div class="dh-sk-foot">✓ Stardust dan streak tersinkronisasi aman ke akun '
                f'({_e(email or "belum masuk akun")}).</div>', unsafe_allow_html=True)


DIALOGS = {"daily": daily_dialog, "tarot": tarot_dialog, "preview": preview_dialog, "streak": streak_dialog}
