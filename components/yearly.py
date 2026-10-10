"""
Yearly Forecast (Batch 6): Shio x Shio tahun + Personal Year + kurva 12 bulan. Wajib login.
Alur: start (data diri + pilih tahun, harga di tombol) -> loading -> hasil dashboard. Hasil tersimpan per orang+tahun (buka lagi gratis).
State: dh_yr_step | dh_yr_prof | dh_yr_year | dh_yr_res | dh_yr_store | dh_yr_err.
DUMMY: saldo cuma di session.
"""

import html
import time
from datetime import date

import streamlit as st

from components import auth, form_kit
from components import close_confirm as cc
from components.dialog_bus import request_with_return
from content import pricing as P
from content import yearly_calc as YC
from engine.rotation import today_wib
from components import result_kit as RK
from utils import trait_cards
from utils.simple_pdf import make_pdf

_e = html.escape
_KEYS = ("dh_yr_step", "dh_yr_res", "dh_yr_err", "dh_yr_png")


def _ss():
    return st.session_state


def _skey(prof, year):
    return f"{prof['nama'].strip().lower()}|{prof['tgl'].isoformat()}|{year}"


def _years():
    y = today_wib().year
    return [y, y + 1]


def _reset():
    for k in _KEYS:
        _ss().pop(k, None)
    cc.cb_stay("yearly")


def _cb_dismiss():
    if _ss().get("dh_yr_step") == "result":
        cc.dismiss("yearly", True, leave=_reset)
    elif _ss().get("dh_yr_step") != "loading":
        _reset()


def _cb_go():
    ss = _ss()
    nama, tgl = (ss.get("dhyr_nama") or "").strip(), ss.get("dhyr_tgl")
    year = ss.get("dhyr_year") or _years()[-1]
    u = auth.current_user()
    if not nama or not tgl:
        ss.dh_yr_err = "Nama dan Tanggal Lahir wajib diisi."
        return
    prof = {"nama": nama, "tgl": tgl, "jam": None, "kota": "", "golda": "", "gender": None}
    ss.dh_solo_prof, ss.dh_yr_prof, ss.dh_yr_year, ss.dh_yr_err = prof, prof, year, None
    st_ = ss.get("dh_yr_store", {})
    if _skey(prof, year) in st_:
        ss.dh_yr_res, ss.dh_yr_step = st_[_skey(prof, year)], "result"
    elif u and u.get("koin", 0) >= P.YEARLY:
        ss.dh_yr_step = "loading"


def _cb_again():
    _reset()


def _cb_close():
    cc.cb_ask("yearly")


def _render_start():
    ss = _ss()
    u = auth.current_user()
    st.markdown(
        '<div class="dh-step dh-step-bp"></div>'
        '<div class="dh-bp-head"><span class="dh-bp-ico">🗓️</span><div><div class="dh-bp-h">YEARLY FORECAST</div>'
        '<div class="dh-bp-hs">Peta satu tahun: hubungan shiomu dengan shio tahun, siklus Personal Year, dan kurva energi 12 bulan.'
        '</div></div></div>', unsafe_allow_html=True)
    st.markdown('<div class="dh-bp-chips"><i>✓ Shio × Shio Tahun</i><i>✓ Personal Year</i><i>✓ Kurva 12 bulan</i>'
                '<i>✓ Bulan terbaik &amp; perlu dijaga</i></div>', unsafe_allow_html=True)
    prof = ss.get("dh_yr_prof") or ss.get("dh_solo_prof") or {}
    form_kit.data_bar("dhyr", "yearly")
    with st.container(key="dhbp_card"):
        st.markdown('<div class="dh-bp-sec">DATA DIRI &amp; TAHUN</div>', unsafe_allow_html=True)
        c1, c2 = st.columns([1.15, 1], gap="small")
        with c1:
            st.text_input("Nama Lengkap / Panggilan", value=prof.get("nama") or (u or {}).get("nama", ""), key="dhyr_nama")
        with c2:
            st.date_input("Tanggal Lahir", value=prof.get("tgl"), min_value=date(1900, 1, 1), max_value=date.today(),
                          format="DD/MM/YYYY", key="dhyr_tgl")
        ys = _years()
        st.radio("Tahun yang dibaca", ys, index=len(ys) - 1, horizontal=True, key="dhyr_year")
        st.markdown('<div class="dh-bp-note sm">Shio tahun berganti saat Imlek (Januari-Februari), bukan 1 Januari. '
                    'Kalau kamu lahir sebelum Imlek di tahun lahirmu, shiomu mengikuti tahun sebelumnya.</div>', unsafe_allow_html=True)
    saldo = int(u.get("koin", 0))
    st.markdown('<div class="dh-bp-price">'
                f'<div class="dh-bp-row"><span>Akun:</span><b class="ok">● {_e(u["email"])}</b></div>'
                f'<div class="dh-bp-row"><span>Harga:</span><b class="big">{P.coin(P.YEARLY)}</b></div>'
                f'<div class="dh-bp-row"><span>Saldo Kamu:</span><b>{P.coin(saldo)}</b></div></div>', unsafe_allow_html=True)
    if ss.get("dh_yr_err"):
        st.error(ss.dh_yr_err)
    with st.container(key="dhbp_cta"):
        if saldo < P.YEARLY:
            st.markdown(f'<div class="dh-bp-warn">Saldo belum cukup, kurang {P.coin(P.YEARLY - saldo)}.</div>', unsafe_allow_html=True)
            if st.button("Top-up Saldo →", key="dhyr_topup", type="primary", use_container_width=True):
                request_with_return("pricing_keep", "yearly", dh_pr_tab="koin")
        else:
            st.button(f"🗓️ Buka Yearly Forecast ({P.coin(P.YEARLY)})", key="dhyr_go", type="primary", on_click=_cb_go,
                      use_container_width=True)


def _render_loading():
    ss = _ss()
    u, prof, year = auth.current_user(), ss.get("dh_yr_prof"), ss.get("dh_yr_year")
    if not (u and prof and year) or u.get("koin", 0) < P.YEARLY:
        ss.dh_yr_step = "start"
        st.rerun(scope="fragment")
    steps = [("🐉", "Membaca shio lahirmu"), ("🔄", "Menghubungkan dengan shio tahun"), ("🔢", "Menghitung Personal Year"),
             ("📈", "Menyusun kurva 12 bulan")]
    st.markdown('<div class="dh-step dh-step-bp"></div><div class="dh-nodismiss"></div>'
                f'<div class="dh-bp-lt">Menyusun peta tahun {year}…</div>'
                '<div class="dh-bp-ls">Memadukan Shio, Numerologi, dan siklus bulan.</div>', unsafe_allow_html=True)
    box, n = st.empty(), len(steps)
    for k in range(n + 1):
        tiles = "".join(f'<span class="{"on" if i < k else ""}"><b>{ic}</b><small>{_e(tx)}</small></span>' for i, (ic, tx) in enumerate(steps))
        box.markdown(f'<div class="dh-bp-tiles" style="grid-template-columns:repeat(4,1fr)">{tiles}</div>'
                     f'<div class="dh-bp-prog big"><i style="width:{round(k / n * 100)}%"></i></div>'
                     f'<div class="dh-bp-pct">{round(k / n * 100)}%</div>', unsafe_allow_html=True)
        time.sleep(3.0 / n)
    try:
        res = YC.baca(prof["tgl"], year)
    except Exception:
        res = None
    if not res:
        ss.dh_yr_err = "Forecast belum bisa disusun dari datamu. Saldo tidak dipotong."
        ss.dh_yr_step = "start"
        st.rerun(scope="fragment")
    u["koin"] -= P.YEARLY
    res["nama"] = prof["nama"]
    ss.setdefault("dh_yr_store", {})[_skey(prof, year)] = res
    ss.dh_yr_res, ss.dh_yr_step = res, "result"
    st.rerun(scope="fragment")


def _chart(kv, best, worst):
    bs, ws = {x["m"] for x in best}, {x["m"] for x in worst}
    out, w = "", 30
    for i, x in enumerate(kv):
        v = x["skor"]
        h = round(v / 100 * 110)
        cls = "hi" if v >= 65 else "mid" if v >= 50 else "lo"
        xx = 6 + i * w
        mark = "★" if x["m"] in bs else "▼" if x["m"] in ws else ""
        out += (f'<rect x="{xx}" y="{130 - h}" width="22" height="{h}" rx="5" class="b {cls}"/>'
                f'<text x="{xx + 11}" y="{124 - h}" class="v">{v}</text>'
                f'<text x="{xx + 11}" y="148" class="m">{x["bulan"][:3]}</text>'
                + (f'<text x="{xx + 11}" y="12" class="s {"g" if mark == "★" else "r"}">{mark}</text>' if mark else ""))
    return f'<svg viewBox="0 0 372 156" class="dh-yr-chart">{out}</svg>'


def _render_result():
    ss = _ss()
    r = ss.get("dh_yr_res")
    if not r:
        ss.dh_yr_step = "start"
        st.rerun(scope="fragment")
    st.markdown('<div class="dh-step dh-step-bp"></div>', unsafe_allow_html=True)
    nm = lambda xs: ", ".join(x["bulan"] for x in xs)
    pd = r["py_data"]
    out = (f'<div class="dh-bp-id"><div class="dh-bp-id-top"><span class="dh-bp-badge">YEARLY FORECAST {r["year"]}</span>'
           f'<em>{_e(r["nama"])}</em></div><div class="dh-bp-id-n">{_e(r["judul"])}</div>'
           f'<div class="dh-bp-id-c"><span><small>Shio × Shio Tahun</small><b>{r["shio_kamu"]} × {r["shio_tahun"]}</b></span>'
           f'<span><small>Hubungan</small><b>{_e(r["rel_label"])}</b></span>'
           f'<span><small>Personal Year</small><b>{r["py"]} · {_e(YC.TEMA_PY[r["py"]])}</b></span>'
           f'<span><small>Skor Tahun</small><b>{r["skor"]} · {_e(r["tier"])}</b></span></div></div>'
           f'<div class="dh-bp-card"><div class="dh-bp-ct">📈 KURVA ENERGI 12 BULAN</div>{_chart(r["kurva"], r["terbaik"], r["terjaga"])}'
           f'<div class="dh-yr-legend"><span class="g">★ Terbaik: {_e(nm(r["terbaik"]))}</span>'
           f'<span class="r">▼ Perlu dijaga: {_e(nm(r["terjaga"]))}</span></div>'
           '<div class="dh-bp-note sm">Skor bulanan = hubungan bulan dengan shiomu, Personal Month, dan hubungan shio tahunmu. '
           'Ini kecenderungan energi, bukan kepastian.</div></div>'
           f'<div class="dh-bp-card"><div class="dh-bp-ct">🔹 RINGKASAN TAHUN</div><p>{_e(r["ringkasan"])}</p>'
           f'<div class="dh-bp-blk"><b>🔄 Hubungan shio</b><p>{_e(r["rel_info"])}</p></div>'
           f'<div class="dh-bp-blk"><b>🔢 Personal Year {r["py"]}{" · " + _e(pd.get("judul") or "") if pd.get("judul") else ""}</b>'
           f'<p>{_e(pd.get("ringkasan") or "")}</p></div>'
           + (f'<div class="dh-bp-blk"><b>🌗 Paruh tahun</b><p>{_e(r["paruh"])}</p></div>' if r.get("paruh") else "") + "</div>")
    for lb, tx in r["sections"]:
        out += f'<div class="dh-bp-card"><div class="dh-bp-ct">{_e(lb.upper())}</div><p>{_e(tx)}</p></div>'
    out += ('<div class="dh-bp-card"><div class="dh-bp-ct">🧭 3 LANGKAH UNTUK TAHUN INI</div>'
            + "".join(f'<div class="dh-bp-rm"><b>{i}</b><p>{_e(t)}</p></div>' for i, t in enumerate(r["tips"], 1)) + "</div>")
    if r["placeholder"]:
        out += '<div class="dh-bp-note sm">Sebagian teks masih sementara (data Gemini belum dipasang). Skor, hubungan, dan kurva sudah dihitung asli.</div>'
    st.markdown(out, unsafe_allow_html=True)
    if not ss.get("dh_yr_png"):
        ss.dh_yr_png = trait_cards.kartu_tahunan(r["nama"], r["year"], r["shio_kamu"], r["shio_tahun"], r["rel_label"], r["skor"],
                                                 r["tier"], [x["bulan"][:3] for x in r["terbaik"]],
                                                 [x["bulan"][:3] for x in r["terjaga"]], [x["skor"] for x in r["kurva"]])
    secs = [("Ringkasan Tahun", [r["ringkas"] if "ringkas" in r else r["ringkasan"], f'Hubungan shio: {r["rel_info"]}']),
            ("Bulan Terbaik", [nm(r["terbaik"])]), ("Perlu Dijaga", [nm(r["terjaga"])])] + \
           [(lb, [tx]) for lb, tx in r["sections"]] + [("3 Langkah Tahun Ini", list(r["tips"]))]
    sub = f'{r["shio_kamu"]} x {r["shio_tahun"]} - Skor {r["skor"]} ({r["tier"]})'
    ttl = f'Yearly Forecast {r["year"]}'
    wa = f'{ttl} {r["nama"]}: skor {r["skor"]} ({r["tier"]}). Cek takdirmu di destinyreveal.id #DestinyReveal'
    RK.actions("dhyr", (_cb_close, ()), pdf=make_pdf(ttl, f'Untuk: {r["nama"]} - {sub}', secs),
               text=RK.sections_text(ttl, f'{r["nama"]} - {sub}', secs), png=ss.dh_yr_png, wa=wa, name=f"yearly-{r['year']}")


@st.dialog("Yearly Forecast", width="large", on_dismiss=_cb_dismiss)
def yearly_dialog():
    ss = _ss()
    if not auth.current_user():
        request_with_return("auth", "yearly")
    step = ss.get("dh_yr_step", "start")
    if step == "result" and ss.get("dh_yr_res"):
        cc.wrap("yearly", _render_result, leave=_reset, icon="🗓️", title="Yakin Mau Tutup Forecast Ini?",
                      text="Forecast ini sudah tersimpan. Buka lagi dari menu ini tanpa bayar ulang (isi data dan tahun yang sama).",
                      tip="Simpan kartu PNG dulu kalau mau dibagikan.", stay="✨ Lanjut Baca", go="Ya, Tutup")
    elif step == "loading":
        _render_loading()
    else:
        _render_start()


DIALOGS = {"yearly": yearly_dialog}
