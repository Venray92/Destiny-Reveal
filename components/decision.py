"""
Decision Reveal (Batch 5): bandingkan Pilihan A vs B dengan tebaran 7 kartu Tarot. Wajib login.
Alur: start (nama pilihan A/B + harga di tombol) -> loading kocok kartu -> hasil (7 kartu dibuka satu-satu / sekaligus,
bacaan per posisi, skor A vs B, arah saran, kartu PNG). Hasil tidak disimpan (tebar ulang = bayar lagi), seperti Tarot Spread.
State: dh_dc_step | dh_dc_a | dh_dc_b | dh_dc_cards | dh_dc_open | dh_dc_active | dh_dc_new.
DUMMY: saldo cuma di session.
"""

import html
import random
import time

import streamlit as st

from utils import resume as _resume

from components import auth
from components import close_confirm as cc
from components.dialog_bus import request_with_return
from content import decision_calc as DC
from content import pricing as P
from components import result_kit as RK
from utils import trait_cards
from utils.simple_pdf import make_pdf

_e = html.escape
MIN_CHARS = 5
_KEYS = ("dh_dc_step", "dh_dc_cards", "dh_dc_open", "dh_dc_active", "dh_dc_new", "dh_dc_err", "dh_dc_png")


def _ss():
    return st.session_state


def _reset():
    for k in _KEYS:
        _ss().pop(k, None)
    cc.cb_stay("decision")


def _cb_dismiss():
    if _ss().get("dh_dc_step") == "result":
        cc.dismiss("decision", True, leave=_reset)
    elif _ss().get("dh_dc_step") == "pay":
        _cb_back()
    elif _ss().get("dh_dc_step") != "loading":
        _reset()


def _valid(t):
    """Pilihan dianggap sah: min 5 karakter, ada cukup huruf & variasi (bukan 'aaaaa' / '12345')."""
    t = (t or "").strip()
    letters = [c for c in t if c.isalpha()]
    return len(t) >= MIN_CHARS and len(letters) >= 4 and len({c.lower() for c in letters}) >= 3


def _name(k, lab):
    return (_ss().get(k) or "").strip() or f"Pilihan {lab}"


def _cb_go():
    """Tebar 7 Kartu -> validasi -> layer konfirmasi pembayaran (belum potong saldo)."""
    ss = _ss()
    a, b = (ss.get("dhdc_a") or "").strip(), (ss.get("dhdc_b") or "").strip()
    if not _valid(a) or not _valid(b):
        ss.dh_dc_err = f"Isi kedua pilihan dengan jelas (minimal {MIN_CHARS} karakter) ya."
        return
    if a.lower() == b.lower():
        ss.dh_dc_err = "Pilihan A dan B tidak boleh sama."
        return
    ss.dh_dc_a, ss.dh_dc_b, ss.dh_dc_err = a, b, None
    ss.dh_dc_step = "pay"


def _cb_back():
    _ss().pop("dh_dc_step", None)


def _cb_pay():
    ss = _ss()
    u = auth.current_user()
    if not u or u.get("koin", 0) < P.DECISION:
        return
    from engine.tarot import TAROT_DECK
    u["koin"] -= P.DECISION
    _resume.scanned("decision")  # fitur lain yang kuesionernya tertunda di-reset
    ss.dh_dc_cards = random.sample(TAROT_DECK, 7)
    ss.dh_dc_open, ss.dh_dc_active, ss.dh_dc_new = [], None, None
    ss.dh_dc_step = "loading"


def _cb_pick(i):
    ss = _ss()
    o = ss.setdefault("dh_dc_open", [])
    if i not in o:
        o.append(i)
        ss.dh_dc_new = i
    ss.dh_dc_active = i


def _cb_all():
    ss = _ss()
    ss.dh_dc_open, ss.dh_dc_new = list(range(7)), None
    if ss.get("dh_dc_active") is None:
        ss.dh_dc_active = 0


def _cb_again():
    _reset()


def _cb_close():
    cc.cb_ask("decision")


# ─────────────── layar ───────────────
def _render_start():
    ss = _ss()
    u = auth.current_user()
    st.markdown(
        '<div class="dh-step dh-step-bp"></div>'
        '<div class="dh-bp-head"><span class="dh-bp-ico">⚖️</span><div><div class="dh-bp-h">DECISION REVEAL</div>'
        '<div class="dh-bp-hs">Bimbang antara dua pilihan? Tebaran 7 kartu membandingkan energi dan risiko masing-masing, '
        'plus faktor tersembunyi dan arah saran.</div></div></div>', unsafe_allow_html=True)
    st.markdown('<div class="dh-bp-chips"><i>✓ Skor Pilihan A vs B</i><i>✓ 7 posisi kartu</i><i>✓ Faktor tersembunyi</i>'
                '<i>✓ Langkah 7 hari</i></div>', unsafe_allow_html=True)
    with st.container(key="dhbp_card"):
        st.markdown('<div class="dh-bp-sec">DUA PILIHANMU</div>', unsafe_allow_html=True)
        st.text_input("Pilihan A", value=ss.get("dh_dc_a") or "", placeholder="Tulis pilihan lengkap, contoh: Terima tawaran kerja baru di Jakarta", key="dhdc_a",
                      max_chars=60)
        st.text_input("Pilihan B", value=ss.get("dh_dc_b") or "", placeholder="Tulis pilihan lengkap, contoh: Bertahan di kantor sekarang dan minta naik gaji", key="dhdc_b",
                      max_chars=60)
        st.markdown(f'<div class="dh-dc-tip">✍️ Tulis konteks yang jelas (minimal {MIN_CHARS} karakter per pilihan). '
                    'Isi asal-asalan atau kata acak tetap diproses, jadi jawabannya juga ikut tidak bermakna.</div>', unsafe_allow_html=True)
        st.markdown('<div class="dh-bp-note sm">Pikirkan kedua pilihan itu dengan tenang sebelum menebar kartu. '
                    'Hasilnya kecenderungan energi, bukan kepastian atau pengganti pertimbangan fakta.</div>', unsafe_allow_html=True)
    saldo = int(u.get("koin", 0))
    st.markdown('<div class="dh-bp-price">'
                f'<div class="dh-bp-row"><span>Akun:</span><b class="ok">● {_e(u["email"])}</b></div>'
                f'<div class="dh-bp-row"><span>Harga:</span><b class="big">{P.coin(P.DECISION)}</b></div>'
                f'<div class="dh-bp-row"><span>Saldo Kamu:</span><b>{P.coin(saldo)}</b></div></div>', unsafe_allow_html=True)
    if ss.get("dh_dc_err"):
        st.error(ss.dh_dc_err)
    with st.container(key="dhbp_cta"):
        if saldo < P.DECISION:
            st.markdown(f'<div class="dh-bp-warn">Saldo belum cukup, kurang {P.coin(P.DECISION - saldo)}.</div>', unsafe_allow_html=True)
            if st.button("Top-up Saldo →", key="dhdc_topup", type="primary", use_container_width=True):
                request_with_return("pricing_keep", "decision", dh_pr_tab="koin")
        else:
            ok = _valid(ss.get("dhdc_a")) and _valid(ss.get("dhdc_b"))
            st.button(f"🔮 Tebar 7 Kartu ({P.coin(P.DECISION)})", key="dhdc_go", type="primary", on_click=_cb_go,
                      use_container_width=True, disabled=not ok)


def _render_loading():
    from components.mini_modals import _loadcard_uri
    lc = _loadcard_uri()
    st.markdown(
        '<div class="dh-step dh-step-fm dh-step-tsload"></div><div class="dh-nodismiss"></div>'
        '<div class="dh-ts-badgewrap"><span class="dh-fm-badge dh-ts-badge">Decision Reveal</span></div>'
        + (f'<div class="dh-tr-shuf"><img src="{lc}" alt="Deck kosmik"></div>' if lc else '<div class="dh-tr-shuf"><i></i></div>')
        + '<div class="dh-tr-shuft">Mengocok 78 Arcana Kosmik...</div>'
        '<div class="dh-tr-shufs">Menimbang dua jalan di depanmu</div>', unsafe_allow_html=True)
    time.sleep(3)
    _ss().dh_dc_step = "result"
    st.rerun(scope="fragment")


def _tile_html(slug, i, is_open, is_active, is_new):
    from components.feature_modals import _ts_tile
    return _ts_tile(slug, i, is_open, is_active, is_new)


def _reading(p):
    from components.feature_modals import _ts_info
    _c, nama, arti, idx = _ts_info(p["slug"])
    judul = f"Arcana #{idx}: {nama}" if idx is not None else nama
    kk = "".join(f"<span class=\"dh-ts-chip\">{_e(k)}</span>" for k in p["kunci"])
    pol = f'<span class="dh-dc-pol {p["polarity"]}">{_e(p["label"])}</span>'
    return (f'<div class="dh-ts-read"><div class="dh-ts-rpos">{_e(p["judul"].upper())}</div>'
            f'<div class="dh-ts-rhead"><div class="dh-ts-rname">{_e(judul)}</div>{pol}{kk}</div>'
            f'<div class="dh-ts-rl dh-ts-rmean"><b>Makna Posisi Ini:</b> {_e(p["makna"])}</div>'
            f'<div class="dh-ts-rl"><p>{_e(p["teks"])}</p></div></div>')


def _verdict(r, a, b):
    def bar(lab, nm, sk):
        pct = round((sk + 6) / 12 * 100)
        on = " on" if r["unggul"] == lab else ""
        return (f'<div class="dh-dc-opt{on}"><div class="dh-dc-on"><b>{lab}</b><span>{_e(nm)}</span><em>{sk:+d}</em></div>'
                f'<div class="dh-dc-bar"><i style="width:{pct}%"></i></div></div>')
    note = ('<div class="dh-bp-note sm">Teks kartu masih sementara (data Gemini belum dipasang).</div>' if r["placeholder"] else "")
    return (f'<div class="dh-bp-card dh-dc-verdict"><div class="dh-bp-ct">⚖️ SKOR PILIHAN</div>{bar("A", a, r["skor"]["A"])}'
            f'{bar("B", b, r["skor"]["B"])}<p>{_e(r["verdict"])}</p>{note}</div>')


def _render_result():
    ss = _ss()
    cards = ss.get("dh_dc_cards") or []
    if len(cards) != 7:
        _reset()
        st.rerun(scope="fragment")
    r = DC.baca(cards)
    a, b = _name("dh_dc_a", "A"), _name("dh_dc_b", "B")
    opened = ss.setdefault("dh_dc_open", [])
    active, new = ss.get("dh_dc_active"), ss.get("dh_dc_new")
    st.markdown('<div class="dh-step dh-step-detail dh-step-tsres"></div><div class="dh-nodismiss"></div>', unsafe_allow_html=True)
    h1, h2 = st.columns([2.6, 1.3], gap="small", vertical_alignment="center")
    with h1:
        st.markdown('<div class="dh-ts-eyebrow">DECISION REVEAL</div>'
                    f'<div class="dh-ts-hint">A: {_e(a)} · B: {_e(b)}<br>Ketuk kartu untuk membukanya, atau buka sekaligus.</div>',
                    unsafe_allow_html=True)
    with h2:
        if len(opened) < 7:
            with st.container(key="dhts_openall"):
                st.button("Buka Semua Kartu", key="dhdc_all", on_click=_cb_all, use_container_width=True)
    st.markdown('<div class="dh-ts-sep"></div>', unsafe_allow_html=True)
    with st.container(key="dhts_grid"):
        for r0, n in ((0, 4), (4, 3)):
            cols = st.columns(4, gap="small")
            for j, col in enumerate(cols):
                i = r0 + j
                if j >= n:
                    continue
                with col:
                    with st.container(key=f"dhtsk_{i}"):
                        st.markdown(_tile_html(cards[i], i, i in opened, active == i, new == i), unsafe_allow_html=True)
                        st.button("Pilih", key=f"dhtso_{i}", on_click=_cb_pick, args=(i,))
    if active is not None and active in opened:
        st.markdown(_reading(r["pos"][active]), unsafe_allow_html=True)
    else:
        st.markdown('<div class="dh-ts-empty">Pilih satu kartu untuk membaca penjelasannya.</div>', unsafe_allow_html=True)
    if len(opened) >= 7:
        st.markdown(_verdict(r, a, b), unsafe_allow_html=True)
        arah = r["pos"][6]["teks"]
        st.markdown(f'<div class="dh-bp-card"><div class="dh-bp-ct">🧭 ARAH SARAN 7 HARI</div><p>{_e(arah)}</p></div>',
                    unsafe_allow_html=True)
        if not ss.get("dh_dc_png"):
            ss.dh_dc_png = trait_cards.kartu_keputusan(a, b, r["skor"]["A"], r["skor"]["B"], r["unggul"], arah)
        secs = [("Hasil", [f'A ({a}): {r["skor"]["A"]:+d}', f'B ({b}): {r["skor"]["B"]:+d}', r["verdict"]]), ("Arah Saran 7 Hari", [arah])]
        wa = f'Decision Reveal: {r["verdict"]} Cek takdirmu di destinyreveal.id #DestinyReveal'
        st.markdown('<div style="height:6px"></div>', unsafe_allow_html=True)
        RK.actions("dhdc", (_cb_close, ()), pdf=make_pdf("Decision Reveal", f"A: {a} - B: {b}", secs),
                   text=RK.sections_text("Decision Reveal", f"A: {a} - B: {b}", secs), png=ss.dh_dc_png, wa=wa,
                   name="decision-reveal",
                   extra=lambda: st.button("← Tebar Ulang dengan Pilihan Lain", key="dhdc_again", use_container_width=True, on_click=_cb_again))
        return
    with st.container(key="dhts_acts"):
        st.button("← Tebar Ulang dengan Pilihan Lain", key="dhdc_again", use_container_width=True, on_click=_cb_again)
        st.button("Selesai & Tutup", key="dhdc_done", type="primary", use_container_width=True, on_click=_cb_close)


@st.dialog("Decision Reveal", width="large", on_dismiss=_cb_dismiss)
def decision_dialog():
    ss = _ss()
    if not auth.current_user():
        request_with_return("auth", "decision")
    step = ss.get("dh_dc_step", "start")
    if step == "result":
        cc.wrap("decision", _render_result, leave=_reset, icon="⚖️", title="Yakin Mau Tutup Hasil Ini?",
                      text="Tebaran ini tidak bisa dibuka lagi setelah ditutup. Menebar ulang butuh Stardust baru.",
                      tip="Simpan kartu PNG dulu kalau mau dibagikan.", stay="✨ Lanjut Baca", go="Ya, Tutup")
    elif step == "loading":
        _render_loading()
    elif step == "pay":
        from components import pay_layer
        pay_layer.render("mxpay_dc", _render_start, icon="⚖️", brand="DECISION REVEAL", price=P.DECISION,
                         rows=[("Pilihan A", _name("dh_dc_a", "A")), ("Pilihan B", _name("dh_dc_b", "B")), ("Isi", "Tebaran 7 kartu")],
                         on_pay=_cb_pay, on_back=_cb_back, return_to="decision", pay_label="Bayar & Tebar Kartu")
    else:
        with cc.bg("mxpay_dc"):
            _render_start()


DIALOGS = {"decision": decision_dialog}
