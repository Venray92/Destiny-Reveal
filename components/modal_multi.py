"""
Multi-System Blueprint (Reveal) - langkah baru semua mode (REVISI03 Batch 5):
form -> [Mode 2/3: pilih Singkat/Lengkap -> kuesioner] -> bayar Stardust -> loading -> hasil.
Mode 1 = 5 kelahiran (tanpa kuesioner), Mode 2 = 5 psikologi, Mode 3 = 15 sistem.
"""

import html
import time
from datetime import datetime

import streamlit as st

from utils import resume as _resume

from components import auth
from components import close_confirm as cc
from components import quiz_reuse as QR
from utils import quiz_store as QS
from components import quiz_kit as QK
from components.dialog_bus import request_with_return
from components.flow_state import STEP_FORM, STEP_LOADING, STEP_PAY, STEP_RESULT, set_step
from components.modal_detail import build_detail
from content import blueprint_calc as BC
from content import pricing as P
from content.result_builder import compute_raw_result

STEP_MODE, STEP_QUIZ, STEP_REUSE = "mode", "quiz", "reuse"
_E = html.escape
_SCALE = {1: "Sangat Tidak Setuju", 2: "Tidak Setuju", 3: "Netral", 4: "Setuju", 5: "Sangat Setuju"}
BIRTH5 = ["Zodiak", "Shio", "Weton", "Numerologi", "Matrix Destiny"]
PSY5 = ["MBTI", "Big Five", "Enneagram", "DISC", "Love Language"]
# mode -> (judul, sub, harga, sistem)
MODES = {
    "instan": ("Mode 1: 5 Kelahiran", "Zodiak, Shio, Weton, Numerologi, Matrix Destiny", P.BUNDLE_BIRTH, BIRTH5),
    "mendalam": ("Mode 2: 5 Psikologi", "MBTI, Big Five, Enneagram, DISC, Love Language", P.BUNDLE_PSY, PSY5),
    "lengkap": ("Mode 3: 15 Sistem", "Seluruh 15 sistem kosmik dalam satu laporan", P.BUNDLE_ALL, list(BC.NAMES)),
}


def mode_key():
    m = st.session_state.get("dh_modal_mode", "instan")
    return m if m in MODES else "instan"


def info():
    return MODES[mode_key()]


def needs_quiz(mode=None):
    return (mode or mode_key()) != "instan"


def price(mode=None):
    return MODES[mode or mode_key()][2]


def title(mode=None):
    return MODES[mode or mode_key()][0]


def _ans():
    return st.session_state.setdefault("dh_mx_ans", {})


def _who():
    d = st.session_state.get("dh_modal_data") or {}
    tgl = d.get("tgl_lahir")
    meta = " · ".join(str(x) for x in (tgl, d.get("kota_lahir")) if x)
    return d.get("nama"), meta


# ─────────────── navigasi ───────────────
def go_after_form():
    """Dipanggil setelah form valid: Mode 1 langsung bayar, Mode 2/3 pilih kedalaman kuesioner."""
    if needs_quiz():
        st.session_state.pop("dh_mx_qi", None)
        st.session_state.pop("dh_mx_reused", None)
        set_step(STEP_REUSE if _offer() else STEP_MODE)
    else:
        set_step(STEP_PAY)


def _cb_qmode(m):
    ss = st.session_state
    ss.dh_mx_qmode, ss.dh_mx_qi, ss.dh_mx_ans = m, 0, {}
    ss.pop("dh_mx_reused", None)
    set_step(STEP_QUIZ)


def _pk():
    d = st.session_state.get("dh_modal_data") or {}
    return QS.pkey(d.get("nama"), d.get("tgl_lahir")) if d.get("tgl_lahir") else None


def _offer():
    pk = _pk()
    return QS.offer("mx", pk, lambda m: BC.plan(m, info()[3])) if pk else None


def _cb_reuse():
    ss = st.session_state
    o = _offer()
    if not o:
        set_step(STEP_MODE)
        return
    ss.dh_mx_qmode = o["mode"]
    ss.dh_mx_ans, ss.dh_mx_qi = QS.fill(o, BC.plan(o["mode"], info()[3]))
    if o["full"]:
        ss.dh_mx_reused = True
        set_step(STEP_PAY)
    else:
        ss.pop("dh_mx_reused", None)
        set_step(STEP_QUIZ)


def _cb_redo():
    set_step(STEP_MODE)


def _cb_quiz_done():
    ss = st.session_state
    pk = _pk()
    if pk:
        m = ss.get("dh_mx_qmode") or "singkat"
        QS.save("mx", pk, m, BC.plan(m, info()[3]), ss.get("dh_mx_ans") or {}, title())
    set_step(STEP_PAY)


def render_reuse():
    o = _offer()
    if not o:
        set_step(STEP_MODE)
        st.rerun(scope="fragment")
    ttl = info()[0]
    st.markdown(
        '<div class="dh-step dh-step-bp"></div><div class="dh-nodismiss"></div>'
        f'<div class="dh-bp-head"><span class="dh-bp-ico">🔮</span><div><div class="dh-bp-h">{_E(ttl.upper())}</div>'
        '<div class="dh-bp-hs">Jawaban kuesionermu sudah tersimpan.</div></div></div>', unsafe_allow_html=True)
    QR.screen("dhmx", o, _cb_reuse, _cb_redo, _cb_back_form)


def _cb_back_form():
    set_step(STEP_FORM)


def _cb_pay_back():
    if needs_quiz() and st.session_state.get("dh_mx_reused"):
        set_step(STEP_REUSE)
    elif needs_quiz():
        st.session_state.dh_mx_qi = max(0, len(_items()) - 1)
        set_step(STEP_QUIZ)
    else:
        set_step(STEP_FORM)


def _cb_pay():
    u = auth.current_user()
    if not u or u.get("koin", 0) < price():
        return
    st.session_state.dh_mx_err = None
    st.session_state.pop("dh_flow_result", None)
    set_step(STEP_LOADING)


def _resume_and(name, **state):
    st.session_state.dh_mx_resume = True
    request_with_return(name, "reveal", **state)


def _items():
    return BC.plan(st.session_state.get("dh_mx_qmode") or "singkat", info()[3])


# ─────────────── layar: pilih kedalaman kuesioner (pola sama dengan Career DNA) ───────────────
def _cb_modesel(m):
    st.session_state.dh_mx_modesel = m


def _cb_modeask():
    if st.session_state.get("dh_mx_modesel"):
        st.session_state.dh_mx_modeconf = True


def _cb_modestay():
    st.session_state.pop("dh_mx_modeconf", None)


def _cb_modego(m):
    st.session_state.pop("dh_mx_modeconf", None)
    _cb_qmode(m)


def render_mode():
    ss = st.session_state
    sel = ss.get("dh_mx_modesel")
    if ss.get("dh_mx_modeconf") and sel:
        nm = "Cepat" if sel == "singkat" else "Deep"
        cc.layer("mxmode", _mode_screen, on_go=lambda: _cb_modego(sel), on_stay=_cb_modestay, icon="📝",
                 title="Mulai Kuesioner?", text=f"Apakah kamu yakin ingin melanjutkan dengan kuesioner mode <b>{nm}</b>?",
                 stay="Batal / Beralih", go="Ya, Lanjutkan")
    else:
        with cc.bg("mxmode"):
            _mode_screen()


def _mode_screen():
    sel = st.session_state.get("dh_mx_modesel")
    ttl, sub, _p, sc = info()
    n_s, n_l = len(BC.plan("singkat", sc)), len(BC.plan("lengkap", sc))
    st.markdown(
        '<div class="dh-step dh-step-bp"></div><div class="dh-nodismiss"></div>'
        f'<div class="dh-bp-head"><span class="dh-bp-ico">🔮</span><div><div class="dh-bp-h">{_E(ttl.upper())}</div>'
        '<div class="dh-bp-hs">Pilih kedalaman kuesioner kepribadianmu.</div></div></div>'
        f'<div class="dh-bp-note">Kuesioner: <b>{_E(", ".join(s for s in BC.QUIZ if s in sc))}</b>. '
        'Satu pertanyaan per layar, semua wajib dijawab.</div>', unsafe_allow_html=True)
    cards = [("singkat", "⚡ Cepat", n_s, "Gambaran awal yang cukup baik.",
              "Tiap dimensi dinilai dari sedikit soal. Hasil bisa bergeser kalau kamu menjawab ulang."),
             ("lengkap", "🎯 Deep", n_l, "Paling akurat &amp; stabil.",
              "Seluruh bank soal. Lebih sedikit tertukar akibat satu jawaban yang meleset.")]
    c1, c2 = st.columns(2, gap="small")
    for col, (m, t, n, tag, ds) in zip((c1, c2), cards):
        with col:
            st.markdown(f'<div class="dh-bp-mcard{" is-sel" if sel == m else ""}"><b>{t}</b>'
                        f'<em>~{max(1, round(n * 7 / 60))} menit · {n} soal</em>'
                        f'<p><b style="display:inline;font-size:12.5px">{tag}</b> {ds}</p></div>', unsafe_allow_html=True)
            with st.container(key=f"dhbp_mode_{m}"):
                st.button("Dipilih ✓" if sel == m else "Pilih", key=f"dhmx_pick_{m}", on_click=_cb_modesel, args=(m,),
                          type="primary" if sel == m else "secondary", use_container_width=True)
    with st.container(key="dhbp_cta"):
        st.button("Mulai Kuesioner →", key="dhmx_mode_go", type="primary", on_click=_cb_modeask,
                  disabled=not sel, use_container_width=True)
    st.button("← Kembali", key="dhmx_mode_back", on_click=_cb_back_form, type="tertiary")


# ─────────────── layar: kuesioner ───────────────
def _qget(sys_, qid):
    return _ans().get(sys_, {}).get(qid)


def _qput(sys_, qid, val):
    _ans().setdefault(sys_, {})[qid] = val


def render_quiz():
    QK.render("dhmx", _items(), _qget, _qput, "dh_mx_qi", "Kuesioner " + title().split(": ")[0], _who(),
              lambda: set_step(STEP_MODE), _cb_quiz_done, _SCALE)


# ─────────────── layar: pembayaran Stardust ───────────────
def pay_layer(form_fn):
    """Mode 1: konfirmasi bayar tampil sebagai layer di atas Modal Isi Data (tetap ada, di-blur)."""
    with cc.bg("mxpay"):
        form_fn()
    with st.container(key="dhcc_layer_mxpay"):
        with st.container(key="dhcc_card_mxpay"):
            render_pay(marker=False)


def render_pay(marker=True):
    ss = st.session_state
    u = auth.current_user()
    ttl, sub, pr, sc = info()
    d = ss.get("dh_modal_data") or {}
    st.markdown(
        ('<div class="dh-step dh-step-bp"></div>' if marker else "") + '<div class="dh-nodismiss"></div>'
        '<div class="dh-bp-head"><span class="dh-bp-ico">🔮</span><div><div class="dh-bp-h">MULTI-SYSTEM BLUEPRINT</div>'
        '<div class="dh-bp-hs">Konfirmasi pembayaran</div></div></div>', unsafe_allow_html=True)
    if not u:
        st.markdown('<div class="dh-bp-warn">Masuk dulu supaya hasilnya tersimpan di akunmu dan bisa dibayar pakai Stardust.</div>',
                    unsafe_allow_html=True)
        if st.button("Masuk / Daftar →", key="dhmx_login", type="primary", use_container_width=True):
            _resume_and("auth")
        st.button("← Kembali", key="dhmx_pay_back0", on_click=_cb_pay_back, type="tertiary")
        return
    saldo = int(u.get("koin", 0))
    sisa = saldo - pr
    mode = ""
    if needs_quiz():
        mode = f'<div class="dh-bp-row"><span>Kuesioner:</span><b>{"Lengkap" if ss.get("dh_mx_qmode") == "lengkap" else "Singkat"} ✓ selesai</b></div>'
    st.markdown(
        '<div class="dh-bp-price">'
        f'<div class="dh-bp-row"><span>Untuk:</span><b>{_E(d.get("nama", "-"))}</b></div>'
        f'<div class="dh-bp-row"><span>Paket:</span><b>{_E(ttl)}</b></div>'
        f'<div class="dh-bp-row"><span>Isi:</span><b>{_E(sub)}</b></div>{mode}<div class="dh-bp-line"></div>'
        f'<div class="dh-bp-row"><span>Harga:</span><b class="big">{P.coin(pr)}</b></div>'
        f'<div class="dh-bp-row"><span>Saldo Kamu:</span><b>{P.coin(saldo)}</b></div>'
        f'<div class="dh-bp-row"><span>Sisa Setelah Transaksi:</span><b class="{"ok" if sisa >= 0 else "bad"}">{P.coin(sisa)}</b></div></div>',
        unsafe_allow_html=True)
    if ss.get("dh_mx_err"):
        st.error(ss.dh_mx_err)
    with st.container(key="dhbp_cta"):
        if sisa < 0:
            st.markdown(f'<div class="dh-bp-warn">Saldo belum cukup, kurang {P.coin(-sisa)}.</div>', unsafe_allow_html=True)
            if st.button("Top-up Saldo →", key="dhmx_topup", type="primary", use_container_width=True):
                _resume_and("pricing_keep", dh_pr_tab="koin")
        else:
            st.button(f"Bayar & Buka Hasil {pr:,}✨".replace(",", "."), key="dhmx_pay", type="primary", on_click=_cb_pay,
                      use_container_width=True)
    st.button("← Kembali", key="dhmx_pay_back", on_click=_cb_pay_back, type="tertiary")


# ─────────────── hitung hasil (Mode 2 & 3) ───────────────
def _first_sentence(text, limit=170):
    text = (text or "").strip()
    cut = text.find(". ")
    out = text if cut == -1 else text[: cut + 1]
    return out if len(out) <= limit else out[: limit - 1].rstrip() + "…"


def _jam(s):
    try:
        return datetime.strptime(s, "%H:%M").time() if s else None
    except Exception:
        return None


def compute_systems(mode, data, qmode, ans):
    """Hasil per sistem untuk kartu hasil. Format item sama dengan compute_mode1 (modal_steps)."""
    ld = {"tanggal_lahir": data["tgl_lahir"], "jam_lahir": _jam(data.get("jam_lahir")), "kota_lahir": data.get("kota_lahir") or None,
          "golongan_darah": data.get("golongan_darah") if data.get("golongan_darah") in ("A", "B", "AB", "O") else None,
          "nama_lengkap": data["nama"]}
    out = []
    for s in MODES[mode][3]:
        try:
            raw = BC.quiz_raw(s, ans.get(s) or {}, qmode) if BC.KIND[s] == "quiz" else compute_raw_result(s, ld)
        except Exception:
            raw = {}
        det = build_detail(s, raw) if raw and not raw.get("placeholder") else None
        n = BC.NAMES.index(s) + 1
        sec0 = (det["sections"][0][2] or [""])[0] if det and det.get("sections") else ""
        params = (det or {}).get("params") or []
        out.append({
            "system": s, "label": f"{n:02d}. {s.upper()}", "raw": raw, "short": s,
            "tag": str(params[0][1]) if params else "",
            "title": det["title"] if det else "Belum bisa dihitung",
            "desc": _first_sentence(sec0) if det else "Sistem ini butuh data tambahan (jam lahir / golongan darah) atau tahun lahir di luar jangkauan data.",
            "quote": (det or {}).get("quote", ""),
        })
    return out


def render_loading(form_fn=None):
    """Loading seragam semua mode: hitung -> potong Stardust -> hasil. Gagal hitung = saldo tidak dipotong."""
    from components import modal_steps
    ss = st.session_state
    u = auth.current_user()
    mode = mode_key()
    if not u or u.get("koin", 0) < price():
        set_step(STEP_PAY)
        st.rerun(scope="fragment")
    data = ss.get("dh_modal_data") or {}
    t0 = time.time()
    _html = (('' if form_fn else '<div class="dh-step dh-step-loading"></div>') + '<div class="dh-nodismiss"></div>'
             '<div class="dh-dl-load"><div class="dh-dl-orb"><i></i><span>✦</span></div>'
             f'<div class="dh-dl-t">Menyelaraskan {_E(title(mode))}...</div>'
             '<div class="dh-dl-s">Memproses peta takdirmu dan menyimpannya ke akun.</div></div>')
    if form_fn:  # Mode 1: loading jadi layer di atas Modal Isi Data yang di-blur
        with cc.bg("mxpay"):
            form_fn()
        with st.container(key="dhcc_layer_mxpay"):
            with st.container(key="dhcc_card_mxpay"):
                st.markdown(_html, unsafe_allow_html=True)
    else:
        st.markdown(_html, unsafe_allow_html=True)
    try:
        if mode == "instan":
            res = modal_steps.compute_mode1(data.get("nama", ""), data.get("tgl_lahir"),
                                            data.get("jam_lahir") or None, data.get("kota_lahir") or None)
        else:
            res = compute_systems(mode, data, ss.get("dh_mx_qmode") or "singkat", ss.get("dh_mx_ans") or {})
    except Exception:
        res = None
    if not res or not any(r["raw"] and not r["raw"].get("placeholder") for r in res):
        ss.dh_mx_err = "Hasil belum bisa disusun dari datamu. Saldo tidak dipotong."
        set_step(STEP_PAY)
        st.rerun(scope="fragment")
    u["koin"] -= price(mode)
    _resume.scanned("reveal")  # fitur lain yang kuesionernya tertunda di-reset
    ss.dh_flow_result = res
    auth.add_history(data.get("nama", ""), data.get("tgl_lahir"), res)
    time.sleep(max(0.0, 3.0 - (time.time() - t0)))
    set_step(STEP_RESULT)
    st.rerun(scope="fragment")
