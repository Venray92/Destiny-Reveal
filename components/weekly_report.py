"""
Weekly & Monthly Report (REVISI06 bagian 2). Wajib login. Alur: beli (tab Weekly/Monthly + fokus) -> loading -> hasil 4 tab.
State: dh_wk_kind | dh_wk_step (buy/loading/result) | dh_wk_res | dh_wk_tab | dh_wk_store (laporan yang sudah dibeli).
Isi laporan dihitung di content/weekly_calc.py (library periodik + biorhythm). DUMMY: saldo cuma di session.
"""

import html
import time
from datetime import date
from urllib.parse import quote as urlquote

import streamlit as st

from components import auth
from components import close_confirm as cc
from components.dialog_bus import request_open, request_with_return
from content import pricing as P
from content import weekly_calc as W
from engine.rotation import BULAN
from components import result_kit as RK
from utils import trait_cards
from utils.simple_pdf import make_pdf

_e = html.escape
_KIND = {
    "weekly": {"tab": "📊 Weekly Report", "ico": "📊", "title": "WEEKLY REPORT", "price": P.WEEKLY,
               "sub": "Panduan timing energi 7 hari ke depan dengan sinkronisasi zodiak &amp; weton kelahiranmu."},
    "monthly": {"tab": "🗓️ Monthly Report", "ico": "🗓️", "title": "MONTHLY REPORT", "price": P.MONTHLY,
                "sub": "Navigasi komprehensif bulan ini: peta minggu, golden days, dan strategi rezeki bulanan."},
}
_TABS = [("📊", "Ringkasan & Energi"), ("🗓️", "Navigasi 7 Hari"), ("🍀", "Aspek & Hoki"), ("🧭", "Panduan Aksi")]
_FOCUS_DESC = {
    "weekly": {"harmoni": "Zodiak + Weton", "karier": "Zodiak + Weton + Shio", "asmara": "Zodiak + Weton + Tarot"},
    "monthly": {"harmoni": "Zodiak + Shio + Numerologi + BaZi + Zi Wei", "karier": "Zodiak + Shio + BaZi + Numerologi",
                "asmara": "Zodiak + Shio + Zi Wei + Tarot"},
}


def _ss():
    return st.session_state


def _kind():
    k = _ss().get("dh_wk_kind", "weekly")
    return k if k in _KIND else "weekly"


def _fmt_tgl(t):
    return f"{t.day} {BULAN[t.month - 1]} {t.year}"


# ─────────────── callbacks ───────────────
def _cb_kind(k):
    _ss().dh_wk_kind = k
    _ss().dh_wk_err = None


def _cb_tab(i):
    _ss().dh_wk_tab = i


def _go(step):
    _ss().dh_wk_step = step


def _reset_view():
    ss = _ss()
    for k in ("dh_wk_res", "dh_wk_tab", "dh_wk_err"):
        ss.pop(k, None)
    ss.dh_wk_step = "buy"


def _cb_close():
    # X di dialog: di layar hasil -> tanya dulu; di layar lain -> reset
    cc.dismiss("weekly", _ss().get("dh_wk_step") == "result" and bool(_ss().get("dh_wk_res")), leave=_reset_view)
    if not cc.asking("weekly") and _ss().get("dh_wk_step") != "result":
        _reset_view()


def _cb_save_profile():
    ss = _ss()
    nama = (ss.get("dhwk_nama") or "").strip()
    tgl = ss.get("dhwk_tgl")
    if not nama or not tgl:
        ss.dh_wk_err = "Nama dan Tanggal Lahir wajib diisi."
        return
    prof = {"nama": nama, "tgl": tgl, "jam": None, "kota": "", "golda": "", "gender": None}
    u = auth.current_user()
    if u:
        u["nama"] = nama
        u["profil"] = prof
    ss.dh_solo_prof = {k: prof[k] for k in ("nama", "jam", "kota", "golda", "gender", "tgl")}
    ss.dh_wk_err = None


def _store_key(kind, prof, focus):
    from engine.rotation import format_periode_minggu, today_wib
    d = today_wib()
    per = format_periode_minggu(d) if kind == "weekly" else f"{d.year}-{d.month:02d}"
    return f"{kind}|{per}|{focus}|{prof['tgl'].isoformat()}"


def _cb_buy():
    ss = _ss()
    from components.solo_reveal import _profile
    u, prof, kind = auth.current_user(), _profile(), _kind()
    focus = ss.get(f"dhwk_focus_{kind}", "harmoni")
    if not (u and prof):
        return
    key = _store_key(kind, prof, focus)
    if key in ss.get("dh_wk_store", {}):  # sudah dibeli periode ini -> buka gratis
        ss.dh_wk_res = ss.dh_wk_store[key]
        ss.dh_wk_tab = 0
        _go("result")
        return
    if u.get("koin", 0) < _KIND[kind]["price"]:
        return
    ss.dh_wk_err = None
    _go("loading")


# ─────────────── layar: beli ───────────────
def _head(kind):
    k = _KIND[kind]
    st.markdown(
        '<div class="dh-step dh-step-wr"></div>'
        f'<div class="dh-wr-badgewrap"><span class="dh-wr-ico">{k["ico"]}</span><span class="dh-wr-badge">PREMIUM REPORT</span></div>'
        f'<div class="dh-wr-h">{k["title"]}</div><div class="dh-wr-hs">{k["sub"]}</div>', unsafe_allow_html=True)


def _render_buy():
    from components.solo_reveal import _profile
    ss = _ss()
    u = auth.current_user()
    kind = _kind()
    k = _KIND[kind]
    prof = _profile()
    _head(kind)
    with st.container(key="dhwk_tabs"):
        c1, c2 = st.columns(2, gap="small")
        for col, kk in zip((c1, c2), ("weekly", "monthly")):
            with col:
                st.button(f'{_KIND[kk]["tab"]}  ·  {P.coin(_KIND[kk]["price"])}', key=f"dhwk_tab_{kk}", on_click=_cb_kind,
                          args=(kk,), type="primary" if kk == kind else "secondary", use_container_width=True)

    with st.container(key="dhwk_card"):
        st.markdown(f'<div class="dh-wr-row"><span>Status Akun:</span><b class="ok">● Akun Terhubung ({_e(u["email"])})</b></div>',
                    unsafe_allow_html=True)
        if not prof:
            st.markdown('<div class="dh-wr-lbl">Lengkapi Profil</div>'
                        '<div class="dh-wr-note">Kami butuh nama &amp; tanggal lahir untuk menghitung Zodiak dan Weton-mu.</div>',
                        unsafe_allow_html=True)
            st.text_input("Nama Lengkap / Panggilan", key="dhwk_nama", value=u.get("nama", "") if u else "")
            st.date_input("Tanggal Lahir", value=None, min_value=date(1930, 1, 1), max_value=date.today(),
                          format="DD/MM/YYYY", key="dhwk_tgl")
            if ss.get("dh_wk_err"):
                st.error(ss.dh_wk_err)
            st.button("Simpan Profil →", key="dhwk_saveprof", type="primary", on_click=_cb_save_profile, use_container_width=True)
            return
        det = W.profil_terdeteksi(prof["tgl"])
        z, w = det["zodiak"], det["weton"]
        kota = f' ({_e(prof["kota"])})' if prof.get("kota") else ""
        st.markdown(
            f'<div class="dh-wr-row"><span class="dh-wr-lbl0">Profil Terdeteksi:</span>'
            f'<em class="dh-wr-tag">{_e(z["sign"])} • {_e(w["hari"])} {_e(w["pasaran"])}</em></div>'
            f'<div class="dh-wr-prof"><div><b>{_e(prof["nama"])}</b><small>Lahir: {_fmt_tgl(prof["tgl"])}{kota}</small></div>'
            '<span class="dh-wr-ver">✓ Terverifikasi</span></div>'
            '<div class="dh-wr-note">Laporan berkala siap digenerate dengan saldo Stardust kamu.</div>'
            '<div class="dh-wr-lbl">Pilih Fokus Analisis:</div>', unsafe_allow_html=True)
        focus = st.selectbox("Pilih Fokus Analisis", list(W.FOCUS), key=f"dhwk_focus_{kind}", label_visibility="collapsed",
                             format_func=lambda f: f"{W.FOCUS[f][1]} {W.FOCUS[f][0]}")
        desc = W.FOCUS[focus][2].replace("minggu ini", "bulan ini") if kind == "monthly" else W.FOCUS[focus][2]
        st.markdown(f'<div class="dh-wr-focus"><b>{_e(W.FOCUS[focus][0])}</b><span>{_FOCUS_DESC[kind][focus]}</span>'
                    f'<small>{_e(desc)}</small></div>', unsafe_allow_html=True)

    price, saldo = k["price"], u.get("koin", 0)
    key = _store_key(kind, prof, focus)
    owned = key in ss.get("dh_wk_store", {})
    sisa = saldo - price
    if owned:
        st.markdown('<div class="dh-wr-price own"><div class="dh-wr-row"><span>Laporan periode ini sudah kamu buka.</span>'
                    '<b class="ok">Gratis dibuka lagi ✓</b></div></div>', unsafe_allow_html=True)
    else:
        st.markdown(
            '<div class="dh-wr-price">'
            f'<div class="dh-wr-row"><span>Harga Pembacaan:</span><b class="big">{P.coin(price)}</b></div>'
            f'<div class="dh-wr-row"><span>Saldo Stardust Kamu:</span><b>{P.coin(saldo)}</b></div><div class="dh-wr-line"></div>'
            f'<div class="dh-wr-row"><span>Sisa Saldo Setelah Transaksi:</span><b class="{"ok" if sisa >= 0 else "bad"}">{P.coin(sisa)}</b></div></div>',
            unsafe_allow_html=True)
    with st.container(key="dhwk_cta"):
        if not owned and sisa < 0:
            st.markdown(f'<div class="dh-wr-warn">Saldo belum cukup, kurang {P.coin(-sisa)}.</div>', unsafe_allow_html=True)
            if st.button("Top-up Saldo →", key="dhwk_topup", type="primary", use_container_width=True):
                request_with_return("pricing_keep", "weekly", dh_pr_tab="koin")
        else:
            label = "✨ Buka Laporan Tersimpan" if owned else f"✨ Buka Laporan Sekarang ({P.coin(price)})"
            st.button(label, key="dhwk_buy", type="primary", on_click=_cb_buy, use_container_width=True)
    st.markdown('<div class="dh-wr-foot">Laporan akan tersimpan otomatis dan bisa diakses kapan saja.</div>', unsafe_allow_html=True)


# ─────────────── layar: loading ───────────────
def _render_loading():
    from components.solo_reveal import _profile
    ss = _ss()
    u, prof, kind = auth.current_user(), _profile(), _kind()
    price = _KIND[kind]["price"]
    if not (u and prof) or u.get("koin", 0) < price:
        _go("buy")
        st.rerun(scope="fragment")
    focus = ss.get(f"dhwk_focus_{kind}", "harmoni")
    nama_k = "Mingguan" if kind == "weekly" else "Bulanan"
    st.markdown(
        '<div class="dh-step dh-step-wr"></div><div class="dh-nodismiss"></div>'
        '<div class="dh-dl-load"><div class="dh-dl-orb"><i></i><span>✦</span></div>'
        f'<div class="dh-dl-t">Membaca Frekuensi {nama_k}-mu...</div>'
        '<div class="dh-dl-s">Menyelaraskan siklus bioritme, zodiak, dan weton ke dalam peta energimu.</div></div>',
        unsafe_allow_html=True)
    t0 = time.time()
    try:
        rep = W.build_report(kind, prof, focus)
    except Exception:
        rep = None
    if not rep or not rep.get("prio"):
        ss.dh_wk_err = "Laporan belum bisa disusun untuk datamu. Saldo tidak dipotong."
        _go("buy")
        st.rerun(scope="fragment")
    u["koin"] -= price
    rep["price"] = price
    ss.setdefault("dh_wk_store", {})[_store_key(kind, prof, focus)] = rep
    ss.dh_wk_res, ss.dh_wk_tab = rep, 0
    time.sleep(max(0, 3 - (time.time() - t0)))
    _go("result")
    st.rerun(scope="fragment")


# ─────────────── layar: hasil ───────────────
def _bar(b):
    t = b["tier"]
    tag = {"puncak": f'<span class="dh-wr-pk">{b["pct"]}% ⭐<br>PUNCAK</span>',
           "hindari": f'<span class="dh-wr-tg bad">{b["pct"]}% Hindari</span>'}.get(
        t, f'<span class="dh-wr-tg">{b["pct"]}% {_e(b["tag"])}</span>')
    return (f'<div class="dh-wr-er"><i>{_e(b["label"])}</i><div class="dh-wr-trk"><div class="dh-wr-fill {t}" '
            f'style="width:{b["pct"]}%"></div></div>{tag}</div>')


def _tab_ringkasan(r):
    h = r["harmoni"]
    hero = (
        '<div class="dh-wr-hero"><div class="dh-wr-hero-top">'
        f'<span class="dh-wr-pill">🎯 {r["judul"]}</span><span class="dh-wr-per">Periode: {_e(r["periode"])}</span></div>'
        f'<div class="dh-wr-name">{_e(r["nama"])}</div><div class="dh-wr-sub">{_e(r["sub"])}</div><div class="dh-wr-hline"></div>'
        f'<div class="dh-wr-hero-bot"><div><small>Indeks Harmoni Siklus:</small><b class="acc">{h["idx"]}% — {_e(h["label"])}</b></div>'
        f'<div class="r"><small>Elemen Dominan:</small><b>{_e(r["elemen"])} ✨</b></div></div></div>')
    pr = "".join(
        f'<div class="dh-wr-pr {p["cls"]}"><div class="dh-wr-pr-t"><b>{i}. {_e(p["title"])}</b><span>Best day: {_e(p["best"])}</span></div>'
        f'<div class="dh-wr-pr-m"><small>Progres Keberhasilan Kosmik</small><em>Priority: {_e(p["level"])} ({p["pct"]}%)</em></div>'
        f'<div class="dh-wr-trk"><div class="dh-wr-fill pr-{p["cls"]}" style="width:{p["pct"]}%"></div></div></div>'
        for i, p in enumerate(r["prio"], 1))
    st.markdown(hero + f'<div class="dh-wr-card"><div class="dh-wr-ct">🎯 TOP 3 PRIORITAS {"MINGGU" if r["kind"] == "weekly" else "BULAN"} INI'
                '<span class="dh-wr-key">Aksi Kunci</span></div>' + pr + '</div>', unsafe_allow_html=True)
    bars = "".join(_bar(b) for b in r["bars"])
    st.markdown(f'<div class="dh-wr-card"><div class="dh-wr-ct">⚡ {r["bars_judul"]}<span class="dh-wr-mut">Skala Bioritme Kosmik</span></div>{bars}'
                f'<div class="dh-wr-ins"><b>💡 Insight Energi:</b> &ldquo;{_e(r["insight"])}&rdquo;</div></div>', unsafe_allow_html=True)
    tema = "".join(f"<p>{_e(t)}</p>" for t in r["tema"])
    st.markdown(f'<div class="dh-wr-card"><div class="dh-wr-ct acc">⚡ TEMA &amp; ARUS ENERGI {"PEKAN" if r["kind"] == "weekly" else "BULAN"} INI</div>{tema}</div>',
                unsafe_allow_html=True)


def _tab_navigasi(r):
    cards = "".join(
        f'<div class="dh-wr-day {c["tier"]}"><div class="dh-wr-day-t"><b>{_e(c["label"])}</b>'
        + (f'<em class="bd">⭐ {"Best Day" if r["kind"] == "weekly" else "Puncak"}</em>' if c["tier"] == "puncak" else '<em class="wn">⚠️ Hati-hati</em>' if c["tier"] == "hindari"
           else '<em class="bd">🔑 Fase Kunci</em>' if c.get("kunci") else "")
        + f'</div><p>{_e(c["text"])}</p></div>' for c in r["cards"])
    st.markdown(f'<div class="dh-wr-card"><div class="dh-wr-ct acc">🗓️ {r["nav_judul"]}</div>'
                f'<div class="dh-wr-best"><b>☀️ {r["best_head"]}</b><span>{_e(r["best_txt"])} ✨</span></div>'
                f'<div class="dh-wr-days">{cards}</div></div>', unsafe_allow_html=True)


def _tab_aspek(r):
    ac = "".join(f'<div><b>{ic} {_e(t)}</b><p>{_e(x)}</p></div>' for ic, t, x in r["aspek"])
    note = f'<div class="dh-wr-mut2">Uraian aspek diambil dari kartu Tarot periode ini: {_e(r["tarot_judul"])}.</div>' if r.get("tarot_judul") else ""
    h = r["hoki"]
    st.markdown(f'<div class="dh-wr-aspek">{ac}</div>{note}'
                f'<div class="dh-wr-card"><div class="dh-wr-ct">🍀 HOKI {"MINGGU" if r["kind"] == "weekly" else "BULAN"} INI'
                '<span class="dh-wr-mut">Resonansi Frekuensi Keberuntungan</span></div><div class="dh-wr-hoki">'
                f'<div><span>🔢</span><small>ANGKA</small><b class="acc">{_e(h["angka"])}</b></div>'
                f'<div><span>🎨</span><small>WARNA</small><b>{_e(h["warna"])}</b></div>'
                f'<div><span>🧭</span><small>ARAH</small><b>{_e(h["arah"])}</b></div></div></div>'
                f'<div class="dh-wr-quote"><small>💬 QUOTE {"MINGGU" if r["kind"] == "weekly" else "BULAN"} INI</small>'
                f'<p>&ldquo;{_e(r["quote"])}&rdquo;</p><em>— Destiny Reveal</em></div>', unsafe_allow_html=True)


def _secs(r):
    return [("INDEKS HARMONI", [f'{r["harmoni"]["idx"]}% - {r["harmoni"]["label"]} · Elemen dominan: {r["elemen"]}', r["sub"]]),
           ("TOP 3 PRIORITAS", [f'{p["title"]} - Best day: {p["best"]} - Priority: {p["level"]} ({p["pct"]}%)' for p in r["prio"]]),
           (r["bars_judul"], [f'{b["label"]}: {b["pct"]}% {b["tag"]}' for b in r["bars"]] + [r["insight"]]),
           ("TEMA & ARUS ENERGI", r["tema"]),
           (r["nav_judul"], [r["best_head"] + " " + r["best_txt"]] + [f'{c["label"]}: {c["text"]}' for c in r["cards"]]),
           ("ASPEK", [f"{t}: {x}" for _i, t, x in r["aspek"]]),
           ("HOKI", [f'Angka: {r["hoki"]["angka"]} · Warna: {r["hoki"]["warna"]} · Arah: {r["hoki"]["arah"]}', r["quote"]]),
           ("SANGAT DIANJURKAN (DO'S)", r["dos"]), ("HINDARI (DON'TS)", r["donts"])]


def _pdf(r):
    if not r.get("_pdf"):
        r["_pdf"] = make_pdf(r["judul"].title(), f'Untuk: {r["nama"]} · Periode: {r["periode"]}', _secs(r))
    return r["_pdf"]


def _tab_aksi(r):
    li = lambda xs: "".join(f"<li>{_e(x)}</li>" for x in xs)
    st.markdown(f'<div class="dh-wr-dd"><div class="do"><b>✅ SANGAT DIANJURKAN (DO\'S)</b><ul>{li(r["dos"])}</ul></div>'
                f'<div class="dont"><b>⛔ HINDARI (DON\'TS)</b><ul>{li(r["donts"])}</ul></div></div>', unsafe_allow_html=True)
    cap = (f'{r["judul"].title()} {r["periode"]} · Indeks Harmoni {r["harmoni"]["idx"]}% ({r["harmoni"]["label"]}). '
           f'Hari terbaik: {r["best_txt"]}. Cek laporanmu di Destiny Reveal.')
    if not r.get("_png"):
        r["_png"] = trait_cards.kartu_laporan(r["judul"].upper(), f'{r["nama"]} · {r["periode"]}', f'{r["harmoni"]["idx"]}%',
                                              f'Indeks Harmoni · {r["harmoni"]["label"]}', [(b["label"], b["pct"]) for b in r["bars"]],
                                              "TOP 3 PRIORITAS", [p["title"] for p in r["prio"]])
    sec = _secs(r)
    RK.actions("dhwk", (cc.cb_ask, ("weekly",)), pdf=_pdf(r), png=r["_png"], wa=cap, name=f'{r["kind"]}-report',
               text=RK.sections_text(r["judul"].title(), f'Untuk: {r["nama"]} - Periode: {r["periode"]}', sec))


def _render_result():
    ss = _ss()
    r = ss.get("dh_wk_res")
    if not r:
        _go("buy")
        st.rerun(scope="fragment")
    st.markdown('<div class="dh-step dh-step-wr"></div><div class="dh-wr-resbar"><span class="dh-wr-badge">PREMIUM REPORT</span></div>',
                unsafe_allow_html=True)
    tab = ss.get("dh_wk_tab", 0)
    labels = list(_TABS)
    labels[1] = ("🗓️", "Navigasi 7 Hari" if r["kind"] == "weekly" else "Navigasi 4 Minggu")
    with st.container(key="dhwk_rtabs"):
        cols = st.columns(4, gap="small")
        for i, (col, (ic, lb)) in enumerate(zip(cols, labels)):
            with col:
                st.button(f"{ic}  \n{lb}", key=f"dhwk_rt_{i}", on_click=_cb_tab, args=(i,),
                          type="primary" if i == tab else "secondary", use_container_width=True)
    [_tab_ringkasan, _tab_navigasi, _tab_aspek, _tab_aksi][tab](r)


@st.dialog("Weekly & Monthly Report", width="large", on_dismiss=_cb_close)
def weekly_dialog():
    ss = _ss()
    if not auth.current_user():  # wajib login: langsung ke modal masuk, habis login balik ke sini
        request_with_return("auth", "weekly")
    step = ss.get("dh_wk_step", "buy")
    if step == "result" and ss.get("dh_wk_res"):
        cc.wrap("weekly", _render_result, leave=_reset_view, icon="📊", title="Yakin Mau Tutup Laporan Ini?",
                      text="Laporan periode ini sudah tersimpan. Kamu bisa membukanya lagi dari menu ini tanpa bayar ulang, "
                           "selama periodenya masih sama.",
                      tip="Download PDF dulu kalau mau dibaca offline.", stay="✨ Lanjut Baca", go="Ya, Tutup Laporan")
    elif step == "loading":
        _render_loading()
    else:
        _render_buy()


DIALOGS = {"weekly": weekly_dialog}
