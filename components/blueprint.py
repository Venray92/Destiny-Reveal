"""
Deep Blueprint (REVISI06 bagian 3). Wajib login.
Alur: start (tab Deep Dive / Complete Blueprint + verifikasi profil) -> mode kuesioner -> kuesioner auto-slide
      -> bayar -> loading 15 dimensi -> hasil (Grand Synthesis + 15 sistem).
State: dh_bp_tab | dh_bp_sys | dh_bp_step | dh_bp_mode | dh_bp_qi | dh_bp_ans | dh_bp_res | dh_bp_rtab | dh_bp_store.
Isi dihitung di content/blueprint_calc.py (profil A-M + deep.json). DUMMY: saldo cuma di session.
"""

import html
import re
import time
from datetime import date
from urllib.parse import quote as urlquote

import streamlit as st

from components import auth
from components import close_confirm as cc
from components import life_chart
from components.dialog_bus import request_with_return
from content import blueprint_calc as BC
from content import pricing as P
from utils.simple_pdf import make_pdf

_e = html.escape
_GOLDA = ["A", "B", "AB", "O", "Belum tahu"]
_SCALE = {1: "Sangat Tidak Setuju", 2: "Tidak Setuju", 3: "Netral", 4: "Setuju", 5: "Sangat Setuju"}
_RTABS = [("🧬", "Grand Synthesis & Arsitektur Hidup"), ("🌌", "15 Dimensi Sistem Lengkap")]
_BLOCKS = [("utama", "🔹 Aspek Utama"), ("karier", "💼 Karier & Rezeki"), ("asmara", "💗 Asmara & Percintaan"),
           ("nasihat", "🧭 Nasihat Strategis")]


def _ss():
    return st.session_state


def _tab():
    return "complete" if _ss().get("dh_bp_tab") == "complete" else "dive"


def _scope():
    if _tab() == "complete":
        return list(BC.NAMES)
    s = _ss().get("dh_bp_sys")
    return [s if s in BC.NAMES else BC.NAMES[0]]


def _price():
    return P.BLUEPRINT_ALL if _tab() == "complete" else P.BLUEPRINT


def _fx(t):
    """escape + **tebal** -> <b>"""
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", _e(t or ""))


def _plain(t):
    return re.sub(r"\*\*(.+?)\*\*", r"\1", t or "")


def _paras(xs):
    return "".join(f"<p>{_fx(x)}</p>" for x in xs if x)


def _store_key(prof):
    sc = "complete" if _tab() == "complete" else _scope()[0]
    return f"{sc}|{prof['nama']}|{prof['tgl'].isoformat()}"


# ─────────────── callbacks ───────────────
def _go(step):
    _ss().dh_bp_step = step


def _cb_tab(t):
    _ss().dh_bp_tab = t
    _ss().dh_bp_err = None


def _cb_sys():
    _ss().dh_bp_sys = _ss().get("dhbp_sysel")


def _cb_rtab(i):
    _ss().dh_bp_rtab = i


def _reset_view():
    ss = _ss()
    for k in ("dh_bp_res", "dh_bp_rtab", "dh_bp_err", "dh_bp_qi", "dh_bp_ans", "dh_bp_mode"):
        ss.pop(k, None)
    ss.dh_bp_step = "start"


def _cb_close():
    cc.dismiss("blueprint", _ss().get("dh_bp_step") == "result" and bool(_ss().get("dh_bp_res")), leave=_reset_view)
    if not cc.asking("blueprint") and _ss().get("dh_bp_step") != "result":
        _reset_view()


def _cb_generate():
    ss = _ss()
    nama = (ss.get("dhbp_nama") or "").strip()
    tgl = ss.get("dhbp_tgl")
    golda = ss.get("dhbp_golda") or ""
    jam = ss.get("dhbp_jam")
    sc = _scope()
    if not nama or not tgl:
        ss.dh_bp_err = "Nama dan Tanggal Lahir wajib diisi."
        return
    if ("Zi Wei" in sc or "Human Design" in sc) and len(sc) == 1 and not jam:
        ss.dh_bp_err = f"Jam lahir wajib diisi untuk {sc[0]}."
        return
    if sc == ["Golongan Darah"] and golda not in ("A", "B", "AB", "O"):
        ss.dh_bp_err = "Pilih golongan darahmu dulu."
        return
    prof = {"nama": nama, "tgl": tgl, "jam": jam, "kota": (ss.get("dhbp_kota") or "").strip(),
            "golda": "" if golda == "Belum tahu" else golda, "gender": None}
    ss.dh_solo_prof = prof
    u = auth.current_user()
    if u:
        u["nama"] = nama
    ss.dh_bp_err = None
    if _store_key(prof) in ss.get("dh_bp_store", {}):  # sudah dibeli -> buka gratis
        ss.dh_bp_res = ss.dh_bp_store[_store_key(prof)]
        ss.dh_bp_rtab = 0
        _go("result")
    elif [s for s in sc if s in BC.QUIZ]:
        _go("mode")
    else:
        ss.dh_bp_mode = "lengkap"
        _go("pay")


def _cb_mode(m):
    ss = _ss()
    ss.dh_bp_mode, ss.dh_bp_qi, ss.dh_bp_ans = m, 0, {}
    _go("quiz")


def _cb_ans(sys_, qid, val):
    ss = _ss()
    ss.setdefault("dh_bp_ans", {}).setdefault(sys_, {})[qid] = val
    ss.dh_bp_qi = ss.get("dh_bp_qi", 0) + 1
    if ss.dh_bp_qi >= len(BC.plan(ss.dh_bp_mode, _scope())):
        _go("pay")


def _cb_qback():
    ss = _ss()
    if ss.get("dh_bp_qi", 0) > 0:
        ss.dh_bp_qi -= 1
    else:
        _go("mode")


def _cb_pay_back():
    _go("quiz" if [s for s in _scope() if s in BC.QUIZ] else "start")
    if _ss().dh_bp_step == "quiz":
        _ss().dh_bp_qi = max(0, len(BC.plan(_ss().get("dh_bp_mode"), _scope())) - 1)


def _cb_pay():
    u = auth.current_user()
    if not u or u.get("koin", 0) < _price():
        return
    _ss().dh_bp_err = None
    _go("loading")


# ─────────────── layar: start ───────────────
def _head(sub):
    st.markdown(
        '<div class="dh-step dh-step-bp"></div>'
        '<div class="dh-bp-head"><span class="dh-bp-ico">🔷</span><div><div class="dh-bp-h">DEEP BLUEPRINT</div>'
        f'<div class="dh-bp-hs">{sub}</div></div></div>', unsafe_allow_html=True)


def _render_start():
    ss = _ss()
    u = auth.current_user()
    tab = _tab()
    _head("Peta takdir mendalam: profil lengkap A-M yang dipadukan dengan analisis personal.")
    with st.container(key="dhbp_tabs"):
        c1, c2 = st.columns(2, gap="small")
        for col, t, lb in ((c1, "dive", "🔬 Deep Dive"), (c2, "complete", "🌌 Complete Blueprint")):
            with col:
                st.button(lb, key=f"dhbp_tab_{t}", on_click=_cb_tab, args=(t,), type="primary" if t == tab else "secondary",
                          use_container_width=True)
    if tab == "dive":
        st.markdown('<div class="dh-bp-note">Pilih 1 sistem, dapat analisis lengkap A-M.</div>', unsafe_allow_html=True)
        cur = _scope()[0]
        st.selectbox("Pilih Sistem", BC.NAMES, index=BC.NAMES.index(cur), key="dhbp_sysel", label_visibility="collapsed",
                     format_func=lambda n: f"{BC.ICON[n]}  {n}", on_change=_cb_sys)
        s = _scope()[0]
        st.markdown(f'<div class="dh-bp-sysdesc"><b>{BC.ICON[s]} {_e(s)}</b><span>{_e(BC.DESC[s])}</span></div>',
                    unsafe_allow_html=True)
    else:
        st.markdown('<div class="dh-bp-note">Analisis A-M untuk seluruh <b>15 sistem</b> + Grand Synthesis, roadmap 10 tahun, '
                    'dan PDF lengkap.</div>', unsafe_allow_html=True)
        st.markdown('<div class="dh-bp-chips">' + "".join(f'<i>{BC.ICON[n]} {_e(n)}</i>' for n in BC.NAMES) + '</div>',
                    unsafe_allow_html=True)

    from components.solo_reveal import _profile
    prof = _profile() or {}
    with st.container(key="dhbp_card"):
        st.markdown('<div class="dh-bp-sec">VERIFIKASI PARAMETER PROFIL</div>', unsafe_allow_html=True)
        c1, c2 = st.columns([1.15, 1], gap="small")
        with c1:
            st.text_input("Nama Lengkap / Panggilan", value=prof.get("nama") or (u or {}).get("nama", ""), key="dhbp_nama")
        with c2:
            st.date_input("Tanggal Lahir", value=prof.get("tgl"), min_value=date(1900, 1, 1), max_value=date.today(),
                          format="DD/MM/YYYY", key="dhbp_tgl")
        c3, c4, c5 = st.columns(3, gap="small")
        with c3:
            st.time_input("Jam Lahir (Opsional)", value=prof.get("jam") or None, key="dhbp_jam")
        with c4:
            st.text_input("Kota Lahir (Opsional)", value=prof.get("kota") or "", placeholder="Contoh: Jakarta", key="dhbp_kota")
        with c5:
            g = prof.get("golda")
            st.selectbox("Golongan Darah", _GOLDA, index=_GOLDA.index(g) if g in _GOLDA else None, placeholder="Pilih",
                         key="dhbp_golda")
        if tab == "complete":
            st.markdown('<div class="dh-bp-note sm">Jam lahir dibutuhkan untuk Zi Wei &amp; Human Design, golongan darah untuk '
                        'sistem Golongan Darah. Kalau kosong, sistem itu dilewati.</div>', unsafe_allow_html=True)

    price, saldo = _price(), int(u.get("koin", 0))
    sisa = saldo - price
    st.markdown(
        '<div class="dh-bp-price">'
        f'<div class="dh-bp-row"><span>Akun:</span><b class="ok">● {_e(u["email"])}</b></div>'
        f'<div class="dh-bp-row"><span>Harga Blueprint:</span><b class="big">{P.coin(price)}</b></div>'
        f'<div class="dh-bp-row"><span>Saldo Kamu:</span><b>{P.coin(saldo)}</b></div></div>', unsafe_allow_html=True)
    if ss.get("dh_bp_err"):
        st.error(ss.dh_bp_err)
    if sisa < 0:
        st.markdown(f'<div class="dh-bp-warn">Saldo belum cukup, kurang {P.coin(-sisa)}. Top-up dulu ya.</div>', unsafe_allow_html=True)
    with st.container(key="dhbp_cta"):
        st.button("Generate Deep Blueprint →", key="dhbp_go", type="primary", on_click=_cb_generate, use_container_width=True)


# ─────────────── layar: mode kuesioner ───────────────
def _render_mode():
    sc = _scope()
    _head("Satu langkah lagi: pilih kedalaman kuesioner kepribadianmu.")
    n_s, n_l = len(BC.plan("singkat", sc)), len(BC.plan("lengkap", sc))
    full = _tab() == "complete"
    t_s = "~2-3 menit" if full else f"~{max(1, round(n_s * 7 / 60))} menit"
    t_l = "~5-7 menit" if full else f"~{max(1, round(n_l * 7 / 60))} menit"
    qs = ", ".join(s for s in BC.QUIZ if s in sc)
    st.markdown(f'<div class="dh-bp-note">Kuesioner untuk: <b>{_e(qs)}</b>. Satu pertanyaan per layar, langsung lanjut tiap kamu menjawab.</div>',
                unsafe_allow_html=True)
    cards = [("singkat", "⚡ Kuesioner Singkat", t_s, n_s, "Estimasi cepat dari soal pilihan. Akurasi cukup untuk gambaran awal."),
             ("lengkap", "🎯 Kuesioner Lengkap", t_l, n_l, "Seluruh bank soal. Hasil kepribadian paling akurat.")]
    c1, c2 = st.columns(2, gap="small")
    for col, (m, ttl, tm, n, ds) in zip((c1, c2), cards):
        with col:
            st.markdown(f'<div class="dh-bp-mcard"><b>{ttl}</b><em>{tm} · {n} soal</em><p>{ds}</p></div>', unsafe_allow_html=True)
            with st.container(key=f"dhbp_mode_{m}"):
                st.button("Pilih", key=f"dhbp_pick_{m}", on_click=_cb_mode, args=(m,), type="primary" if m == "lengkap" else "secondary",
                          use_container_width=True)
    st.button("← Kembali", key="dhbp_mode_back", on_click=_go, args=("start",), type="tertiary")


# ─────────────── layar: kuesioner (auto-slide) ───────────────
def _render_quiz():
    ss = _ss()
    items = BC.plan(ss.get("dh_bp_mode") or "singkat", _scope())
    n = len(items)
    qi = min(max(ss.get("dh_bp_qi", 0), 0), n - 1)
    it = items[qi]
    s, q = it["sys"], it["q"]
    st.markdown(
        '<div class="dh-step dh-step-bp"></div><div class="dh-nodismiss"></div>'
        f'<div class="dh-bp-qtop"><span>{BC.ICON[s]} {_e(s)}</span><b>Soal {qi + 1} / {n}</b></div>'
        f'<div class="dh-bp-prog"><i style="width:{round(qi / n * 100)}%"></i></div>', unsafe_allow_html=True)
    with st.container(key=f"dhbp_slide_{qi}"):  # key beda tiap soal -> animasi slide-in
        if s in ("MBTI", "Enneagram", "Big Five"):
            st.markdown(f'<div class="dh-bp-q">{_e(q["text"])}</div>', unsafe_allow_html=True)
        elif s == "DISC":
            st.markdown('<div class="dh-bp-q">Pilih kata yang <b>paling</b> menggambarkan dirimu:</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="dh-bp-q">Mana yang lebih sesuai buat kamu?</div>', unsafe_allow_html=True)
        with st.container(key="dhbp_opts"):
            if s in ("MBTI", "Enneagram"):
                c1, c2 = st.columns(2, gap="small")
                for col, lb, v in ((c1, "👍 Setuju", True), (c2, "👎 Tidak Setuju", False)):
                    with col:
                        st.button(lb, key=f"dhbp_a_{qi}_{int(v)}", on_click=_cb_ans, args=(s, q["id"], v), use_container_width=True)
            elif s == "Big Five":
                for v in (5, 4, 3, 2, 1):
                    st.button(f"{v}  ·  {_SCALE[v]}", key=f"dhbp_a_{qi}_{v}", on_click=_cb_ans, args=(s, q["id"], v),
                              use_container_width=True)
            elif s == "DISC":
                for L in "ABCD":
                    st.button(q["options"][L], key=f"dhbp_a_{qi}_{L}", on_click=_cb_ans, args=(s, q["id"], L), use_container_width=True)
            else:
                for L in "AB":
                    st.button(f"{L}.  {q[L]['text']}", key=f"dhbp_a_{qi}_{L}", on_click=_cb_ans, args=(s, q["id"], L),
                              use_container_width=True)
    st.button("← Kembali", key="dhbp_qback", on_click=_cb_qback, type="tertiary")


# ─────────────── layar: bayar ───────────────
def _render_pay():
    ss = _ss()
    u = auth.current_user()
    prof = ss.get("dh_solo_prof") or {}
    sc = _scope()
    price, saldo = _price(), int(u.get("koin", 0))
    sisa = saldo - price
    _head("Konfirmasi pembayaran")
    lbl = "Complete Blueprint · 15 Sistem" if len(sc) > 1 else f"Deep Dive · {sc[0]}"
    mode = ""
    if [s for s in sc if s in BC.QUIZ]:
        mode = f'<div class="dh-bp-row"><span>Kuesioner:</span><b>{"Lengkap" if ss.get("dh_bp_mode") == "lengkap" else "Singkat"} ✓ selesai</b></div>'
    st.markdown(
        '<div class="dh-bp-price">'
        f'<div class="dh-bp-row"><span>Untuk:</span><b>{_e(prof.get("nama", "-"))}</b></div>'
        f'<div class="dh-bp-row"><span>Paket:</span><b>{_e(lbl)}</b></div>{mode}<div class="dh-bp-line"></div>'
        f'<div class="dh-bp-row"><span>Harga:</span><b class="big">{P.coin(price)}</b></div>'
        f'<div class="dh-bp-row"><span>Saldo Kamu:</span><b>{P.coin(saldo)}</b></div>'
        f'<div class="dh-bp-row"><span>Sisa Setelah Transaksi:</span><b class="{"ok" if sisa >= 0 else "bad"}">{P.coin(sisa)}</b></div></div>',
        unsafe_allow_html=True)
    if ss.get("dh_bp_err"):
        st.error(ss.dh_bp_err)
    with st.container(key="dhbp_cta"):
        if sisa < 0:
            st.markdown(f'<div class="dh-bp-warn">Saldo belum cukup, kurang {P.coin(-sisa)}.</div>', unsafe_allow_html=True)
            if st.button("Top-up Saldo →", key="dhbp_topup", type="primary", use_container_width=True):
                request_with_return("pricing_keep", "blueprint", dh_pr_tab="koin")
        else:
            st.button(f"✨ Bayar & Generate ({P.coin(price)})", key="dhbp_pay", type="primary", on_click=_cb_pay,
                      use_container_width=True)
    st.button("← Kembali", key="dhbp_pay_back", on_click=_cb_pay_back, type="tertiary")


# ─────────────── layar: loading ───────────────
def _tiles(sc, k):
    return "".join(f'<span class="{"on" if i < k else ""}"><b>{BC.ICON[n]}</b><small>{_e(n)}</small></span>' for i, n in enumerate(sc))


def _render_loading():
    ss = _ss()
    u, prof, sc = auth.current_user(), ss.get("dh_solo_prof"), _scope()
    price = _price()
    if not (u and prof) or u.get("koin", 0) < price:
        _go("pay")
        st.rerun(scope="fragment")
    st.markdown('<div class="dh-step dh-step-bp"></div><div class="dh-nodismiss"></div>', unsafe_allow_html=True)
    ttl = f"Mensintesis {len(sc)} Dimensi Takdir…" if len(sc) > 1 else f"Mensintesis {sc[0]}…"
    st.markdown(f'<div class="dh-bp-lt">{ttl}</div><div class="dh-bp-ls">Memadukan profil A-M dengan pola kepribadianmu.</div>',
                unsafe_allow_html=True)
    box = st.empty()
    n = len(sc)
    t0 = time.time()
    for k in range(n + 1):
        box.markdown(f'<div class="dh-bp-tiles">{_tiles(sc, k)}</div>'
                     f'<div class="dh-bp-prog big"><i style="width:{round(k / n * 100)}%"></i></div>'
                     f'<div class="dh-bp-pct">{round(k / n * 100)}%</div>', unsafe_allow_html=True)
        time.sleep(3.6 / n)
    try:
        res = BC.build_blueprint(prof, sc, ss.get("dh_bp_ans") or {}, ss.get("dh_bp_mode") or "lengkap")
    except Exception:
        res = None
    if not res:
        ss.dh_bp_err = "Blueprint belum bisa disusun dari datamu. Saldo tidak dipotong."
        _go("pay")
        st.rerun(scope="fragment")
    u["koin"] -= price
    res["price"] = price
    ss.setdefault("dh_bp_store", {})[_store_key(prof)] = res
    ss.dh_bp_res, ss.dh_bp_rtab = res, 0
    time.sleep(max(0, 0.3 - (time.time() - t0)))
    _go("result")
    st.rerun(scope="fragment")


# ─────────────── layar: hasil ───────────────
def _idcard(r):
    h = r["head"]
    chips = "".join(f"<span><small>{a}</small><b>{_e(b)}</b></span>" for a, b in
                    (("Zodiak", h["zodiak"]), ("Weton", h["weton"]), ("Matrix Destiny", h["matrix"]), ("Human Design", h["hd"])))
    st.markdown(
        '<div class="dh-bp-id"><div class="dh-bp-id-top"><span class="dh-bp-badge">DEEP BLUEPRINT</span>'
        f'<em>ID: {_e(r["id"])}</em></div><div class="dh-bp-id-n">{_e(r["nama"])}</div>'
        f'<div class="dh-bp-id-l">Lahir: {_e(r["lahir"])}</div><div class="dh-bp-id-c">{chips}</div></div>', unsafe_allow_html=True)


def _tab_synth(r):
    y = r["synth"]
    out = f'<div class="dh-bp-card"><div class="dh-bp-ct">🧬 ARKETIPE INTI</div>{_paras(y["arketipe"])}</div>'
    if r.get("tgl"):  # dashboard visual: Roda Takdir + grafik usia 20-60 (Matrix Destiny)
        st.markdown(out, unsafe_allow_html=True)
        st.markdown('<div class="dh-bp-ct" style="margin:6px 2px 8px">🧭 PETA SIKLUS HIDUP</div>', unsafe_allow_html=True)
        life_chart.render("Matrix Destiny", r["tgl"], height=700)
        out = ""
    out += ''
    box = lambda items, cls: "".join(f'<div class="{cls}"><small>{_e(s)}</small><p>{_fx(t)}</p></div>' for s, t in items)
    if y["super"]:
        out += f'<div class="dh-bp-ct2">💪 {len(y["super"])} SUPERPOWER UTAMA</div><div class="dh-bp-grid">{box(y["super"], "sp")}</div>'
    if y["blind"]:
        out += f'<div class="dh-bp-ct2">🌑 {len(y["blind"])} TITIK BUTA</div><div class="dh-bp-grid">{box(y["blind"], "bl")}</div>'
    out += (f'<div class="dh-bp-card"><div class="dh-bp-ct">💼 JALUR PROFESI &amp; MONEY MAGNET</div>{_paras(y["profesi"])}'
            f'<div class="dh-bp-gold"><b>🌾 Siklus Panen Finansial Terbaik</b><p>{_fx(y["panen"])}</p></div></div>')
    if y["asmara"]:
        out += f'<div class="dh-bp-card"><div class="dh-bp-ct">💗 DINAMIKA ASMARA</div>{_paras(y["asmara"])}</div>'
    if y["shadow"]:
        out += f'<div class="dh-bp-card"><div class="dh-bp-ct">🌗 SHADOW WORK</div>{_paras(y["shadow"])}</div>'
    rm = "".join(f'<div class="dh-bp-rm{" best" if x["star"] else ""}"><b>{"⭐ " if x["star"] else ""}{_e(x["label"])}</b>'
                 f'<p>{_e(x["text"])}</p></div>' for x in y["roadmap"])
    out += f'<div class="dh-bp-card"><div class="dh-bp-ct">🗺️ ROADMAP TAKDIR 10 TAHUN</div>{rm}</div>'
    st.markdown(out, unsafe_allow_html=True)


def _sys_body(s):
    if not s["ok"]:
        return ('<div class="dh-bp-miss">Sistem ini belum bisa dihitung dari datamu (biasanya butuh jam lahir atau golongan darah). '
                'Isi datanya lalu generate ulang.</div>')
    out = ""
    for k, lb in _BLOCKS:
        if s.get(k):
            out += f'<div class="dh-bp-blk"><b>{lb}</b>{_paras(s[k])}</div>'
    if s.get("extra"):
        ex = "".join(f'<div class="dh-bp-blk"><b>{_e(a)}</b><p>{_fx(b)}</p></div>' for a, b in s["extra"])
        out += f'<details class="dh-bp-more"><summary>Analisis A-M lengkap</summary>{ex}</details>'
    return out


def _tab_systems(r):
    out = ""
    for s in r["systems"]:
        t = f'<small>{_e(s["title"])}</small>' if s.get("title") else ""
        out += (f'<details class="dh-bp-ac"><summary><span>SISTEM {s["n"]:02d}</span><b>{s["icon"]} {_e(s["name"])}</b>{t}</summary>'
                f'<div class="dh-bp-acb">{_sys_body(s)}</div></details>')
    st.markdown(f'<div class="dh-bp-acs">{out}</div>', unsafe_allow_html=True)


def _pdf(r):
    sec = []
    if r.get("synth"):
        y = r["synth"]
        sec += [("ARKETIPE INTI", [_plain(t) for t in y["arketipe"]]),
                ("SUPERPOWER UTAMA", [f"{s}: {_plain(t)}" for s, t in y["super"]]),
                ("TITIK BUTA", [f"{s}: {_plain(t)}" for s, t in y["blind"]]),
                ("JALUR PROFESI & MONEY MAGNET", [_plain(t) for t in y["profesi"]] + ["Siklus Panen Finansial: " + _plain(y["panen"])]),
                ("DINAMIKA ASMARA", [_plain(t) for t in y["asmara"]]), ("SHADOW WORK", [_plain(t) for t in y["shadow"]]),
                ("ROADMAP TAKDIR 10 TAHUN", [f'{x["label"]}: {x["text"]}' for x in y["roadmap"]])]
    for s in r["systems"]:
        lines = []
        if not s["ok"]:
            lines = ["Data sistem ini belum bisa dihitung."]
        for k, lb in _BLOCKS:
            lines += [f'{lb[2:]}: {_plain(t)}' for t in s.get(k) or []]
        lines += [f"{a}: {_plain(b)}" for a, b in s.get("extra") or []]
        sec.append((f'SISTEM {s["n"]:02d} {s["name"].upper()}' + (f' - {s["title"]}' if s.get("title") else ""), lines))
    return make_pdf("Deep Blueprint", f'Untuk: {r["nama"]} · {r["id"]}', sec)


def _pdf_cached(r):
    ss = _ss()
    key = f'{r["id"]}|{len(r["systems"])}|{r["systems"][0]["name"]}|{r["mode"]}'
    c = ss.get("dh_bp_pdfc")
    if not c or c[0] != key:
        data = _pdf(r)
        pages = len(re.findall(rb"/Type\s*/Page(?![s\w])", data)) or 1
        c = ss.dh_bp_pdfc = (key, data, pages)
    return c[1], c[2]


def _render_result():
    ss = _ss()
    r = ss.get("dh_bp_res")
    if not r:
        _go("start")
        st.rerun(scope="fragment")
    st.markdown('<div class="dh-step dh-step-bp"></div>', unsafe_allow_html=True)
    _idcard(r)
    tab = ss.get("dh_bp_rtab", 0)
    if r["complete"]:
        with st.container(key="dhbp_rtabs"):
            cols = st.columns(2, gap="small")
            for i, (col, (ic, lb)) in enumerate(zip(cols, _RTABS)):
                with col:
                    st.button(f"{ic}  {lb}", key=f"dhbp_rt_{i}", on_click=_cb_rtab, args=(i,),
                              type="primary" if i == tab else "secondary", use_container_width=True)
        (_tab_synth if tab == 0 else _tab_systems)(r)
    else:
        s = r["systems"][0]
        if s["name"] in life_chart.SYSTEMS and r.get("tgl"):
            life_chart.render(s["name"], r["tgl"], height=700 if s["name"] == "Matrix Destiny" else 560)
        st.markdown(f'<div class="dh-bp-card"><div class="dh-bp-ct">{s["icon"]} {_e(s["name"].upper())}'
                    f'{" · " + _e(s["title"]) if s.get("title") else ""}</div>{_sys_body(s)}</div>', unsafe_allow_html=True)
    data, pages = _pdf_cached(r)
    cap = f'Deep Blueprint {r["nama"]} ({r["id"]}) sudah jadi di Destiny Reveal.'
    with st.container(key="dhbp_actions"):
        c1, c2, c3 = st.columns([1.9, 1.2, 0.8], gap="small")
        with c1:
            st.download_button(f"⬇️ Download Full PDF {pages} Halaman", data, file_name="deep-blueprint.pdf", mime="application/pdf",
                               key="dhbp_pdf", type="primary", use_container_width=True, on_click="ignore")
        with c2:
            st.link_button("Share Blueprint", f"https://wa.me/?text={urlquote(cap)}", use_container_width=True, icon=":material/share:")
        with c3:
            st.button("Tutup", key="dhbp_done", on_click=cc.cb_ask, args=("blueprint",), use_container_width=True)


@st.dialog("Deep Blueprint", width="large", on_dismiss=_cb_close)
def blueprint_dialog():
    ss = _ss()
    if not auth.current_user():  # wajib login, habis login balik ke sini
        request_with_return("auth", "blueprint")
    step = ss.get("dh_bp_step", "start")
    if step == "result" and ss.get("dh_bp_res"):
        if cc.asking("blueprint"):
            cc.render("blueprint", leave=_reset_view, icon="🔷", title="Yakin Mau Tutup Blueprint Ini?",
                      text="Blueprint ini sudah tersimpan. Kamu bisa membukanya lagi dari menu ini tanpa bayar ulang "
                           "(isi data yang sama).",
                      tip="Download PDF dulu kalau mau dibaca offline.", stay="✨ Lanjut Baca", go="Ya, Tutup Blueprint")
        else:
            _render_result()
    elif step == "mode":
        _render_mode()
    elif step == "quiz":
        _render_quiz()
    elif step == "pay":
        _render_pay()
    elif step == "loading":
        _render_loading()
    else:
        _render_start()


DIALOGS = {"blueprint": blueprint_dialog}
