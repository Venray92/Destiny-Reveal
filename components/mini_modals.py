"""
4 modal ringkas fitur gratis (UI11): Ramalan Harian Gratis, Tarot 1 Kartu Harian,
Preview Zodiak, Streak & Reward. Dibuka dari kartu "GRATIS" di section Jelajahi
lewat jembatan JS (class .dh-open-modal + data-modal) -> tombol tersembunyi di navbar.py.

Aturan tutup: HANYA tombol X. Klik backdrop & Esc diblok (marker .dh-nodismiss,
listener-nya ada di _BRIDGE_JS navbar.py).
DUMMY: koin dan klaim streak belum ada backend. Isi ramalan harian dari content/periodic.py (JSON harian baru).
"""

import base64
import html
import random
import time
from datetime import datetime, timedelta, timezone
from functools import lru_cache
from pathlib import Path

import streamlit as st
from content import pricing as P

from components import auth
from components import form_kit
from components import close_confirm as cc
from components.modal_detail import copy_button
from components.dialog_bus import request_open

from content import periodic
from content import profile_loader
from content.profile_loader import get_profile
from content.result_builder import build_display_data
from engine.tarot import TAROT_MAJOR_ARCANA, kartu_harian
from engine.zodiak import _RENTANG_ZODIAK
from utils.card_images import card_image_data_uri

_ROOT = Path(__file__).resolve().parent.parent
_COVER = _ROOT / "assets" / "images" / "sunmoon.jpg"
_LOADCARD = _ROOT / "assets" / "images" / "loadingcard.png"  # kartu "Deck Kosmik" buat state kocok

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


def weton_list():
    """35 pilihan weton (hari + pasaran) dari key weton_profile.json (lewat profile_loader)."""
    return profile_loader.kunci_harapan("Weton")


_KIND_LABEL = {"zodiak": "Zodiak", "shio": "Shio", "weton": "Weton"}


def today_wib():
    return datetime.now(_WIB).date().isoformat()


def _e(t):
    return html.escape(str(t)).replace("\n", "<br>")


def _zodiak_info(sign):
    """Data Preview Zodiak: rentang tanggal & elemen dari engine, teks dari JSON profil baru (sections.free)."""
    rng = next((r for r in _RENTANG_ZODIAK if r[2] == sign), None)
    free = (get_profile("Zodiak", {"sign": sign}) or {}).get("free", {})
    tgl = f"{rng[0][1]} {_BLN[rng[0][0]]} - {rng[1][1]} {_BLN[rng[1][0]]}" if rng else ""

    def _val(attr, default):
        v = free.get(attr) or default
        return v.split(":", 1)[1].strip() if ":" in v else v

    return {
        "tgl": tgl, "elemen": rng[3] if rng else "",
        "siapa": free.get("siapa_kamu", ""),
        "modality": _val("atribut_1", rng[4] if rng else ""),
        "planet": _val("atribut_2", rng[5] if rng else ""),
        "quote": free.get("quote", "").strip('"“” '),
    }


def _first_sentences(text, n=2):
    parts = (text or "").split(". ")
    out = ". ".join(parts[:n]).strip()
    return out if out.endswith((".", "!", "?")) else out + "."


def _head(block=False):
    email = st.session_state.get("dh_email")
    badge = (f'✓ Akun Terhubung ({_e(email)})' if email else "Belum masuk akun")
    st.markdown(
        '<div class="dh-step dh-step-mini"></div>' + ('<div class="dh-nodismiss"></div>' if block else '') +
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


def request_solo(system):
    """Buka Solo Reveal dengan sistem terpilih (mulai dari pilih sistem, hasil lama dibuang)."""
    ss = st.session_state
    for k in ("dh_solo_res", "dh_solo_ans"):
        ss.pop(k, None)
    request_open("solo", dh_solo_step="select", dh_solo_sys=system, dh_solo_err=None)


_COIN_MSG = "Fitur ini belum tersedia, masih tahap pengembangan 🚧"


def _soon(msg):
    st.toast(msg)


# ═══════════ 1. RAMALAN HARIAN GRATIS ═══════════
_WARNA = ["Merah Bata (Terracotta)", "Biru Laut", "Hijau Sage", "Kuning Madu", "Ungu Lavender", "Putih Gading", "Emas", "Hitam Pekat"]


def _fmt_angka(v):
    """[7, 19, 23] -> '7, 19 & 23'."""
    if isinstance(v, (list, tuple)):
        v = [str(x) for x in v]
        return v[0] if len(v) == 1 else ", ".join(v[:-1]) + " & " + v[-1]
    return str(v or "")


def get_daily_reading(kind, name, day):
    """Return {pesan, angka, warna}: pesan harian (maks 2 kalimat) dari JSON harian baru (content/periodic.py).
    Kunci record dihitung dari kalender (Zodiak: rumah Bulan, Shio: elemen hari), bukan acak.
    Cadangan (file tidak terbaca): pesan = quote profil, angka/warna deterministik dari nama+tanggal."""
    sistem = _KIND_LABEL[kind]
    e = periodic.get_daily(sistem, name, now=datetime.fromisoformat(day))
    if e and e.get("pesan"):
        return {"pesan": _first_sentences(e["pesan"], 2), "angka": _fmt_angka(e.get("angka_hoki")),
                "warna": str(e.get("warna_hoki") or "")}
    raw = {"zodiak": {"sign": name}, "shio": {"shio": name}, "weton": dict(zip(("hari", "pasaran"), name.split()))}[kind]
    free = (get_profile(sistem, raw) or {}).get("free", {})
    seed = random.Random(f"{kind}{name}{day}")
    n1 = seed.randint(1, 9)
    return {"pesan": free.get("quote", ""), "angka": f"{n1} & {n1 * 3}", "warna": seed.choice(_WARNA)}


def _cb_daily_tab(tab):
    st.session_state.dh_daily_tab = tab
    st.session_state.dh_daily_pick = None


def _cb_daily_pick(name):
    st.session_state.dh_daily_pick = name


def _cb_daily_open():
    """Klik 'Buka Ramalan' -> tampilkan popup konfirmasi kuota dulu (belum kepotong)."""
    st.session_state.dh_daily_confirm = True


SWAP_PRICE = P.SWAP  # Stardust


def _cb_swap_open():
    st.session_state.dh_daily_swap = True


def _cb_swap_cancel():
    st.session_state.dh_daily_swap = False


def _cb_swap_pay():
    """Bayar 50 ✨ -> buang kunci harian, user bisa pilih Zodiak/Shio lain lagi."""
    ss = st.session_state
    u = auth.current_user()
    if not u or u.get("koin", 0) < SWAP_PRICE:
        return
    u["koin"] -= SWAP_PRICE
    ss.dh_daily_paid = today_wib()  # konten berbayar -> tombol salin & konfirmasi tutup aktif
    ss.dh_daily_swap = False
    ss.dh_daily_confirm = False
    ss.pop("dh_daily_lock", None)


def _render_swap(u):
    saldo = u["koin"] if u else 0
    st.markdown(
        '<div class="dh-dr-confirm"><div class="dh-dr-cico">🔄</div><div class="dh-dr-ctitle">Buka Sistem Lain Hari Ini</div>'
        '<p>Kuota gratis hari ini sudah terpakai. Mau intip Zodiak, Shio, atau Weton lain? Biayanya '
        f'<b>{SWAP_PRICE} ✨</b>, lalu kamu bisa pilih ulang.</p>'
        f'<div class="dh-dr-bal">Saldo kamu: <b>{saldo} ✨</b> · Sisa setelah bayar: <b>{max(saldo - SWAP_PRICE, 0) if u else 0} ✨</b></div></div>',
        unsafe_allow_html=True)
    if not u:
        st.markdown('<div class="dh-dr-warn">🔒 Masuk akun dulu supaya saldo ✨ bisa dipakai.</div>', unsafe_allow_html=True)
    elif saldo < SWAP_PRICE:
        st.markdown(f'<div class="dh-dr-warn">Saldo belum cukup, kurang {SWAP_PRICE - saldo} ✨.</div>', unsafe_allow_html=True)
    with st.container(key="dhdy_confirm"):
        c1, c2 = st.columns(2, gap="small")
        with c1:
            st.button("Batal", key="dhdy_swap_no", on_click=_cb_swap_cancel, use_container_width=True)
        with c2:
            if not u:
                if st.button("Masuk / Daftar →", key="dhdy_swap_login", type="primary", use_container_width=True):
                    request_open("auth")
            elif saldo < SWAP_PRICE:
                if st.button("Top-up Saldo →", key="dhdy_swap_topup", type="primary", use_container_width=True):
                    request_open("pricing_keep", dh_pr_tab="koin")
            else:
                st.button(f"Bayar {SWAP_PRICE} ✨ & Pilih Ulang", key="dhdy_swap_yes", type="primary",
                          on_click=_cb_swap_pay, use_container_width=True)


def _cb_daily_cancel():
    st.session_state.dh_daily_confirm = False


def _cb_daily_confirm():
    ss = st.session_state
    ss.dh_daily_confirm = False
    ss.dh_daily_loading = {"kind": ss.dh_daily_tab, "name": ss.dh_daily_pick}


_LOAD_SUB = {
    "zodiak": "Membuka peta takdir harianmu...",
    "shio": "Membaca energi shio dan keberuntungan harianmu...",
    "weton": "Menghitung neptu dan ritme pasaran harianmu...",
}


def _render_daily_loading(ld):
    """Modal loading compact (3 detik, tema krem) lalu kunci kuota harian & tampilkan hasil."""
    label = _KIND_LABEL[ld["kind"]]
    st.markdown(
        '<div class="dh-step dh-step-mini"></div><div class="dh-nodismiss"></div>'
        '<div class="dh-dl-load"><div class="dh-dl-orb"><i></i><span>✦</span></div>'
        f'<div class="dh-dl-t">Menyelaraskan Ramalan {label} {_e(ld["name"])}...</div>'
        f'<div class="dh-dl-s">{_LOAD_SUB[ld["kind"]]}</div></div>', unsafe_allow_html=True)
    time.sleep(3)
    ss = st.session_state
    ss.dh_daily_lock = {"date": today_wib(), "kind": ld["kind"], "name": ld["name"]}
    ss.pop("dh_daily_loading", None)
    st.rerun(scope="fragment")


def _cb_daily_dismiss():
    """X: kalau lagi di layar hasil ramalan -> tanya konfirmasi dulu."""
    ss = st.session_state
    lock = ss.get("dh_daily_lock")
    at_result = bool(lock and lock.get("date") == today_wib() and ss.get("dh_daily_paid") == today_wib()
                     and not ss.get("dh_daily_swap") and not ss.get("dh_daily_loading"))
    cc.dismiss("daily", at_result)


@st.dialog("Ramalan Kartu Harian", width="small", on_dismiss=_cb_daily_dismiss)
def daily_dialog():
    ss = st.session_state
    paid = ss.get("dh_daily_paid") == today_wib()
    if not form_kit.login_gate("daily"):
        return
    if ss.get("dh_daily_loading"):
        _render_daily_loading(ss.dh_daily_loading)
        return
    if cc.asking("daily"):
        cc.render("daily", leave=None, icon="🌅", title="Yakin Mau Tutup Halaman Ini?",
                  text="Apakah kamu yakin ingin menutup halaman ini? Pastikan teks hasil sudah disalin.",
                  tip=None, stay="Batal", go="Ya, Tutup")
        return
    _head(block=paid)
    _title("🌅", "Ramalan Kartu Harian", "1x per hari · Pilih Zodiak, Shio, atau Weton kelahiranmu")
    lock = ss.get("dh_daily_lock")
    if lock and lock.get("date") == today_wib():  # sudah dipilih hari ini -> terkunci sampai 00:00 WIB
        if ss.get("dh_daily_swap"):
            _render_swap(auth.current_user())
            return
        kind, name = lock["kind"], lock["name"]
        r = get_daily_reading(kind, name, lock["date"])
        label = _KIND_LABEL[kind]
        sym = GLYPH.get(name, "") + "\ufe0e" if kind == "zodiak" else SHIO_EMOJI.get(name, "🗓️")
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
            if st.button("🔒 Buka Analisis Lengkap Per Sistem", key="dhdy_unlock", type="primary"):
                request_solo(label)
            st.markdown('<div class="dh-dr-sub">Buka analisis mendalam 6 aspek: Aspek Utama, Karier, Asmara, Karakter, '
                        'Shadow Work, &amp; Nasihat Strategis.</div>', unsafe_allow_html=True)
        with st.container(key="dhdy_swap"):
            st.markdown('<div class="dh-dr-swaptxt">Mau intip ramalan zodiak, shio, atau weton lain hari ini?</div>',
                        unsafe_allow_html=True)
            st.button(f"Ganti Pilihan / Buka Sistem Lain ({P.SWAP} ✨) →", key="dhdy_swapbtn", on_click=_cb_swap_open)
        if paid:  # sudah bayar (ganti sistem 50 ✨): salin + selesai (dengan konfirmasi)
            c1, c2 = st.columns(2, gap="small")
            with c1:
                copy_button(f"{label} {name} · Pesan Hari Ini\n{r['pesan']}\nAngka Hoki: {r['angka']}\nWarna Hoki: {r['warna']}\n#DestinyReveal",
                            "📋 Salin Teks", "dhdy_copy", fs=13, h=46)
            with c2:
                st.button("Selesai & Tutup", key="dhdy_done_btn", type="primary", use_container_width=True,
                          on_click=cc.cb_ask, args=("daily",))
        return

    tab = ss.setdefault("dh_daily_tab", "zodiak")
    if ss.get("dh_daily_confirm") and ss.get("dh_daily_pick"):
        kind_label = _KIND_LABEL[tab]
        st.markdown('<div class="dh-dr-confirm"><div class="dh-dr-cico">⚠️</div><div class="dh-dr-ctitle">Konfirmasi Kuota Harian Gratis</div>'
                    f'<p>Apakah kamu yakin ingin melihat ramalan untuk <b>{kind_label} {_e(ss.dh_daily_pick)}</b>? '
                    'Jatah gratis ini hanya bisa digunakan <b>1x per hari</b> dan tidak dapat diganti setelah dibuka hari ini.</p></div>',
                    unsafe_allow_html=True)
        with st.container(key="dhdy_confirm"):
            c1, c2 = st.columns(2, gap="small")
            with c1:
                st.button("Batal", key="dhdy_cancel", on_click=_cb_daily_cancel, use_container_width=True)
            with c2:
                st.button("Ya, Buka Ramalan", key="dhdy_yes", type="primary", on_click=_cb_daily_confirm,
                          use_container_width=True)
        return
    items = {"zodiak": ZODIAK_LIST, "shio": SHIO_LIST, "weton": weton_list()}[tab]
    if ss.get("dh_daily_pick") not in items:
        ss.dh_daily_pick = items[0]
    with st.container(key="dhdy_tabs"):
        c1, c2, c3 = st.columns(3, gap="small")
        with c1:
            st.button("♈︎ Zodiak Barat", key="dhdy_tab_zodiak", on_click=_cb_daily_tab, args=("zodiak",),
                      type="primary" if tab == "zodiak" else "secondary", use_container_width=True)
        with c2:
            st.button("🐍 Shio Timur", key="dhdy_tab_shio", on_click=_cb_daily_tab, args=("shio",),
                      type="primary" if tab == "shio" else "secondary", use_container_width=True)
        with c3:
            st.button("🗓️ Weton Jawa", key="dhdy_tab_weton", on_click=_cb_daily_tab, args=("weton",),
                      type="primary" if tab == "weton" else "secondary", use_container_width=True)
    lab = {"zodiak": "Rasi Zodiak", "shio": "Shio", "weton": "Weton (Hari + Pasaran)"}[tab]
    st.markdown(f'<div class="dh-mn-lab2">Pilih 1 {lab} Kelahiranmu:</div>', unsafe_allow_html=True)
    if tab == "weton":  # 35 opsi -> dropdown, bukan grid
        with st.container(key="dhdy_wsel"):
            ss.dh_daily_pick = st.selectbox("Weton", items, index=items.index(ss.dh_daily_pick), key="dhdy_weton_sel",
                                            label_visibility="collapsed")
    else:
        with st.container(key="dhdy_grid"):
            for row in range(3):
                cols = st.columns(4, gap="small")
                for col, name in zip(cols, items[row * 4:(row + 1) * 4]):
                    with col:
                        st.button(name, key=f"dhdy_pick_{tab}_{name}", on_click=_cb_daily_pick, args=(name,),
                                  type="primary" if ss.dh_daily_pick == name else "secondary", use_container_width=True)
    st.markdown('<div class="dh-mn-notice"><b>ⓘ Ketentuan Kuota Ramalan Gratis:</b>'
                'Kamu hanya dapat memilih 1 tanda (Zodiak / Shio / Weton) per hari. Hasil tersimpan otomatis dan sistem '
                'terkunci hingga pergantian hari (00:00 WIB).</div>', unsafe_allow_html=True)
    label = _KIND_LABEL[tab]
    st.button(f"✨ Buka Ramalan {label} {ss.dh_daily_pick} Hari Ini", key="dhdy_cta", type="primary",
              use_container_width=True, on_click=_cb_daily_open)


# ═══════════ 2. TAROT 1 KARTU HARIAN ═══════════
_ROMAN = ["0", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII", "XIII", "XIV", "XV", "XVI",
          "XVII", "XVIII", "XIX", "XX", "XXI"]
_SUIT_SYM = {"cups": "🏺", "pentacles": "🪙", "swords": "⚔️", "wands": "🔥"}


def _tarot_face(kartu, idx, nama):
    """Muka kartu bawaan (CSS) — tampil kalau gambar kartu belum ada / gagal dimuat; gambar asli menimpa di atasnya."""
    if idx is not None:
        top, mid = _ROMAN[idx], "✦"
    else:
        suit, _, rank = kartu.partition("_")
        top = rank.upper() if not rank.isdigit() else str(int(rank))
        mid = _SUIT_SYM.get(suit, "✦")
    return (f'<span class="dh-trf-n">{_e(top)}</span><span class="dh-trf-s">{mid}</span>'
            f'<span class="dh-trf-t">{_e(nama)}</span>')


@lru_cache(maxsize=1)
def _cover_uri():
    if not _COVER.is_file():
        return None
    return "data:image/jpeg;base64," + base64.b64encode(_COVER.read_bytes()).decode("ascii")


@lru_cache(maxsize=1)
def _loadcard_uri():
    if not _LOADCARD.is_file():
        return None
    return "data:image/png;base64," + base64.b64encode(_LOADCARD.read_bytes()).decode("ascii")


def _pilih_kartu():
    """Login + profil punya tanggal lahir -> rumus numerologi; selain itu seed tanggal + email/id sesi."""
    import uuid
    ss = st.session_state
    u = auth.current_user()
    tgl = ((u or {}).get("profil") or {}).get("tgl")
    if tgl is not None and not hasattr(tgl, "day"):  # jaga-jaga kalau tersimpan sebagai teks ISO
        try:
            tgl = datetime.fromisoformat(str(tgl)).date()
        except ValueError:
            tgl = None
    if u:
        key = u["email"]
    else:
        key = ss.setdefault("dh_anon_key", uuid.uuid4().hex)
    return kartu_harian(tgl, key)


def _cb_tarot_draw():
    # kartu tetap sepanjang hari: kalau sudah ada tarikan hari ini, pakai yang sama.
    # Tarikan baru -> layar "kocok deck" 3 detik dulu (lihat tarot_dialog)
    cur = st.session_state.get("dh_tarot_draw")
    if not cur or cur.get("date") != today_wib():
        st.session_state.dh_tarot_loading = True


_TAROT_CAP = '<div class="dh-tr-cap">Dihitung otomatis dari sinkronisitas tanggal hari ini!</div>'


@st.dialog("Gacha Kartu Tarot", width="small")
def tarot_dialog():
    ss = st.session_state
    if not form_kit.login_gate("tarot"):
        return
    _head()
    _title("🃏", "Gacha Kartu Tarot", "Tarik 1 kartu sinkronisitas kosmik murni untuk memandu energimu hari ini.")
    draw = ss.get("dh_tarot_draw")
    if ss.get("dh_tarot_loading") and (not draw or draw.get("date") != today_wib()):
        _lc = _loadcard_uri()
        st.markdown((f'<div class="dh-tr-shuf"><img src="{_lc}" alt="Deck kosmik"></div>' if _lc else
                     '<div class="dh-tr-shuf"><i></i></div>') +
                    '<div class="dh-tr-shuft">Mengocok Deck Kosmik...</div>'
                    '<div class="dh-tr-shufs">Menghubungkan frekuensi batinmu dengan arketipe hari ini</div>',
                    unsafe_allow_html=True)
        time.sleep(3)
        ss.dh_tarot_draw = {"date": today_wib(), "kartu": _pilih_kartu()}
        ss.pop("dh_tarot_loading", None)
        st.rerun(scope="fragment")
    if not draw or draw.get("date") != today_wib():
        uri = _cover_uri()
        with st.container(key="dhtr_cover"):
            st.markdown(f'<div class="dh-tr-crop"><img class="dh-tr-cimg" src="{uri}" alt="Kartu tarot"></div>' if uri else
                        '<div class="dh-tr-img dh-tr-ph">🂠</div>', unsafe_allow_html=True)
            st.button("Tarik kartu", key="dhtr_draw", on_click=_cb_tarot_draw)
        st.markdown('<div class="dh-tr-hint">👆 Klik dan tarik kartu hari ini</div>' + _TAROT_CAP,
                    unsafe_allow_html=True)
        return

    kartu = draw["kartu"]
    mayor = kartu in TAROT_MAJOR_ARCANA
    idx = TAROT_MAJOR_ARCANA.index(kartu) if mayor else None
    c = build_display_data("Tarot", {"kartu": kartu}) or {}
    nama, _, arti = (c.get("title") or kartu).partition(", ")
    uri = card_image_data_uri(f"tarot/{idx:02d}_{kartu}.png") if mayor else None  # Minor: gambar belum ada -> kartu ilustrasi bawaan
    face = _tarot_face(kartu, idx, nama)
    img = (f'<div class="dh-tr-img dh-tr-face">{face}</div>' +
           (f'<img class="dh-tr-img dh-tr-art" src="{uri}" alt="{_e(nama)}" onerror="this.remove()">' if uri else ""))
    label = f"ARCANA #{idx}" if mayor else "ARCANA MINOR"
    st.markdown(
        f'<div class="dh-tr-wrap">{img}<div class="dh-tr-over"><b>{label}</b>'
        f'<div>{_e(nama)}{f" ({_e(arti)})" if arti else ""}</div></div></div>'
        + _TAROT_CAP +
        f'<div class="dh-mn-msg"><div class="dh-mn-msghead"><span>PESAN INTI HARI INI:</span><b>{_e(arti or nama)}</b></div>'
        f'<p>{_e(_first_sentences(c.get("p1", ""), 3))}</p></div>',
        unsafe_allow_html=True)
    with st.container(key="dhtr_pay"):
        st.markdown('<div class="dh-mn-paywall"><b>Mau Tau Lebih Dalam?</b>'
                    '<span>Bongkar dimensi karier, dinamika asmara, dan peringatan energi tersembunyi kartu ini.</span></div>',
                    unsafe_allow_html=True)
        if st.button("🔒 Mau Tau Lebih Dalam?", key="dhtr_unlock", type="primary", use_container_width=True):
            request_solo("Tarot")  # langsung ke One-System Blueprint dengan Tarot terpilih


# ═══════════ 3. PREVIEW ZODIAK ═══════════
def _cb_pv_pick(name):
    st.session_state.dh_pv_pick = name


@st.dialog("Preview Zodiak", width="small")
def preview_dialog():
    ss = st.session_state
    if not form_kit.login_gate("preview"):
        return
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
        f'<div class="dh-mn-quote2"><b>QUOTE:</b> &ldquo;{_e(d["quote"])}&rdquo;</div></div>',
        unsafe_allow_html=True)
    if st.button("🔒 Buka Analisis Lengkap Per Sistem", key="dhpv_unlock", type="primary",
                 use_container_width=True):
        request_solo("Zodiak")


# ═══════════ 4. STREAK & REWARD ═══════════
# DUMMY: state di session (belum ada backend). Awal 6 hari supaya klaim Week 1 bisa dicoba setelah 1x check-in.
STREAK_DEMO_START = 6
_WEEKS = [("Week 1", "Hari 1-7", 30), ("Week 2", "Hari 8-14", 40), ("Week 3", "Hari 15-21", 50), ("Week 4", "Hari 22-28", 60)]


def _streak_state(u):
    """State streak per akun; reset otomatis tiap awal bulan (WIB)."""
    ym = today_wib()[:7]
    st_ = u.get("streak")
    if not st_ or st_.get("month") != ym:
        st_ = u["streak"] = {"month": ym, "days": STREAK_DEMO_START if not st_ else 0, "last": None, "claimed": []}
    return st_


def _cb_checkin():
    u = auth.current_user()
    if not u:
        return
    s_ = _streak_state(u)
    if s_["last"] == today_wib():
        return
    s_["last"] = today_wib()
    s_["days"] = min(s_["days"] + 1, 28)
    st.session_state.dh_sk_pop = {"icon": "✅", "title": "Check-in Berhasil!",
                                  "text": f"Streak kamu sekarang {s_['days']} hari. Lanjutkan besok biar apinya tetap menyala!"}


def _cb_claim_week(i):
    u = auth.current_user()
    if not u:
        return
    s_ = _streak_state(u)
    if i in s_["claimed"] or s_["days"] < 7 * (i + 1):
        return
    s_["claimed"].append(i)
    u["koin"] = u.get("koin", 0) + _WEEKS[i][2]
    st.session_state.dh_sk_pop = {"icon": "🎉", "title": "Selamat!",
                                  "text": f"+{_WEEKS[i][2]} ✨ telah berhasil masuk ke saldo kamu."}


def _cb_streak_login():
    request_open("auth")


@st.dialog("Daily Checkin", width="small")
def streak_dialog():
    if not form_kit.login_gate("streak"):
        return
    u = auth.current_user()
    if pop := st.session_state.pop("dh_sk_pop", None):  # popup sukses bertema, nutup sendiri ~2,5 detik
        st.markdown(
            '<div class="dh-step dh-step-mini"></div><div class="dh-nodismiss"></div>'
            f'<div class="dh-sk-pop2"><div class="dh-sk-popico"><i></i><span>{pop["icon"]}</span></div>'
            f'<div class="dh-sk-poptitle">{_e(pop["title"])}</div><div class="dh-sk-poptext">{_e(pop["text"])}</div>'
            '<div class="dh-sk-popbar"><i></i></div></div>', unsafe_allow_html=True)
        time.sleep(2.5)
        st.rerun(scope="fragment")
    _head()
    s_ = _streak_state(u) if u else {"days": 0, "last": None, "claimed": []}
    days, claimed = s_["days"], s_["claimed"]
    nxt = next((i for i in range(4) if i not in claimed), None)
    if nxt is None:
        ptxt, pct = "Semua reward bulan ini sudah diklaim 🎉", 100
    else:
        done = max(0, min(days - 7 * nxt, 7))
        ptxt, pct = f"{done} / 7 Hari menuju +{_WEEKS[nxt][2]}✨ Gratis", round(done / 7 * 100)
    tip = ('<i class="dh-sk-ti" tabindex="0">ℹ️ Apa yang bisa didapat dengan 180✨?<i class="dh-sk-pop">'
           '<i class="dh-sk-pophead">💡 Dengan mengumpulkan 180✨ per bulan, kamu bisa unlock:</i>'
           '<i>✅ 1 Tarot Celtic Cross (150✨)</i><i>✅ 1 Tarot 5 Kartu + 1 Tarot 3 Kartu (150✨)</i>'
           '<i>✅ 3 Ramalan Kartu Harian Lengkap (150✨)</i></i></i>')
    st.markdown(
        '<div class="dh-sk-flame">🔥</div><div class="dh-sk-title">Daily Checkin</div>'
        '<div class="dh-mn-notice dh-sk-info"><b>📌 Cara Menaikkan Streak:</b>'
        'Buka website tiap hari buat naikin streak (+1 setiap kali kamu membuka fitur gratis harian).'
        f'{tip}</div>'
        f'<div class="dh-sk-prog"><div class="dh-sk-proghead"><b>{ptxt}</b><span>{pct}%</span></div>'
        f'<div class="dh-sk-bar"><i style="width:{pct}%"></i></div></div>', unsafe_allow_html=True)
    with st.container(key="dhsk_weeks"):
        cols = st.columns(4, gap="small")
        for i, (name, rng, sd) in enumerate(_WEEKS):
            ready = bool(u) and i not in claimed and days >= 7 * (i + 1)
            done_ = i in claimed
            tag = "Diklaim" if done_ else f"+{sd}✨"
            with cols[i]:
                st.button(f"**{name}**  \n{rng}  \n**{'✓ ' if done_ else ''}{tag}**", key=f"dhsk_wk_{i}",
                          type="primary" if ready else "secondary", disabled=not ready,
                          on_click=_cb_claim_week, args=(i,), use_container_width=True)
    with st.container(key="dhsk_cta"):
        if not u:
            st.button("Masuk / Log In untuk Check-in", key="dhsk_login", type="primary", on_click=_cb_streak_login)
        elif s_["last"] == today_wib():
            st.button("✓ Sudah Check-in Hari Ini", key="dhsk_checkin", type="primary", disabled=True)
        else:
            st.button("Check-in Hari Ini", key="dhsk_checkin", type="primary", on_click=_cb_checkin)


DIALOGS = {"daily": daily_dialog, "tarot": tarot_dialog, "preview": preview_dialog, "streak": streak_dialog}
