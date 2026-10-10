"""
Career DNA + Strength & Blind Spot (Batch 4). Wajib login.
Alur: start (data diri) -> [reuse jawaban tersimpan] -> mode (Cepat/Deep) -> kuesioner -> bayar -> loading -> hasil dashboard.
Kuesioner dipakai bersama kedua fitur: jawaban disimpan per orang (dh_sd_traits), fitur kedua tidak tanya ulang.
State: dh_sd_feat | dh_sd_step | dh_sd_mode | dh_sd_qi | dh_sd_ans | dh_sd_res | dh_sd_store | dh_sd_traits.
DUMMY: saldo & hasil cuma di session.
"""

import html
import math
import re
import time
from datetime import date

import streamlit as st

from components import auth, form_kit
from components import close_confirm as cc
from components import quiz_kit as QK
from components.dialog_bus import request_with_return
from content import blueprint_calc as BC
from content import career_calc as CC
from content import pricing as P
from utils import trait_cards
from components.modal_detail import copy_button
from utils.simple_pdf import make_pdf
from urllib.parse import quote as urlquote

_e = html.escape
_SCALE = {1: "Sangat Tidak Setuju", 2: "Tidak Setuju", 3: "Netral", 4: "Setuju", 5: "Sangat Setuju"}
SEC_PER_Q = 7
FEAT = {
    "career": {"ico": "🧬", "h": "CAREER DNA", "price": lambda: P.CAREER_DNA, "go": "Mulai Career DNA →",
               "sub": "Profil minat karier (RIASEC) dari 4 sistem kepribadian + sinyal tanggal lahir + rencana 30 hari.",
               "need": ["Kode karier 3 huruf + radar RIASEC", "10 peran & 6 industri yang cocok", "Lingkungan kerja & motivasimu",
                        "Rencana aksi 30 hari"]},
    "strength": {"ico": "💎", "h": "STRENGTH & BLIND SPOT", "price": lambda: P.STRENGTH, "go": "Mulai Strength & Blind Spot →",
                 "sub": "Kekuatan utama, titik buta, dan latihan harian dari MBTI, Big Five, DISC & Enneagram.",
                 "need": ["Grafik Big Five & DISC", "Kekuatan utama + titik buta + penawarnya", "Kekuatan yang jadi bumerang",
                          "Latihan harian"]},
}


def _ss():
    return st.session_state


def _feat():
    f = _ss().get("dh_sd_feat")
    return f if f in FEAT else "career"


def _price():
    return FEAT[_feat()]["price"]()


def _fx(t):
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", _e(t or ""))


def _pkey(prof):
    return f"{prof['nama'].strip().lower()}|{prof['tgl'].isoformat()}"


def _skey(prof):
    return f"{_feat()}|{_pkey(prof)}"


def _go(step):
    _ss().dh_sd_step = step


def _reset_view():
    ss = _ss()
    for k in ("dh_sd_res", "dh_sd_err", "dh_sd_qi", "dh_sd_ans", "dh_sd_mode", "dh_sd_modesel", "dh_sd_modeconf"):
        ss.pop(k, None)
    ss.dh_sd_step = "start"


def _cb_close():
    ss = _ss()
    cc.dismiss(_feat(), ss.get("dh_sd_step") == "result" and bool(ss.get("dh_sd_res")), leave=_reset_view)
    if not cc.asking(_feat()) and ss.get("dh_sd_step") != "result":
        _reset_view()


# ─────────────── callbacks ───────────────
def _cb_start():
    ss = _ss()
    nama, tgl = (ss.get("dhsd_nama") or "").strip(), ss.get("dhsd_tgl")
    if not nama or not tgl:
        ss.dh_sd_err = "Nama dan Tanggal Lahir wajib diisi."
        return
    prof = {"nama": nama, "tgl": tgl, "jam": ss.get("dhsd_jam"), "kota": (ss.get("dhsd_kota") or "").strip(),
            "golda": "", "gender": None}
    ss.dh_solo_prof = prof
    ss.dh_sd_prof = prof
    ss.dh_sd_err = None
    if _skey(prof) in ss.get("dh_sd_store", {}):  # sudah dibeli -> buka gratis
        ss.dh_sd_res = ss.dh_sd_store[_skey(prof)]
        _go("result")
    elif _pkey(prof) in ss.get("dh_sd_traits", {}):
        _go("reuse")
    else:
        _go("mode")


def _cb_mode(m):
    ss = _ss()
    ss.dh_sd_mode, ss.dh_sd_qi, ss.dh_sd_ans = m, 0, {}
    ss.pop("dh_sd_modeconf", None)
    _go("quiz")


def _cb_modesel(m):
    _ss().dh_sd_modesel = m  # state pilihan Cepat / Deep (belum lanjut)


def _cb_modeask():
    if _ss().get("dh_sd_modesel"):
        _ss().dh_sd_modeconf = True


def _cb_modestay():
    _ss().pop("dh_sd_modeconf", None)


def _cb_ans(sys_, qid, val):
    ss = _ss()
    ss.setdefault("dh_sd_ans", {}).setdefault(sys_, {})[qid] = val
    ss.dh_sd_qi = ss.get("dh_sd_qi", 0) + 1
    if ss.dh_sd_qi >= len(BC.plan(ss.dh_sd_mode, CC.QUIZ_SYSTEMS)):
        ss.setdefault("dh_sd_traits", {})[_pkey(ss.dh_sd_prof)] = {"mode": ss.dh_sd_mode, "ans": ss.dh_sd_ans}
        _go("pay")


def _cb_qback():
    ss = _ss()
    if ss.get("dh_sd_qi", 0) > 0:
        ss.dh_sd_qi -= 1
    else:
        _go("mode")


def _cb_reuse():
    t = _ss()["dh_sd_traits"][_pkey(_ss().dh_sd_prof)]
    _ss().dh_sd_mode, _ss().dh_sd_ans = t["mode"], t["ans"]
    _go("pay")


def _cb_pay():
    u = auth.current_user()
    if u and u.get("koin", 0) >= _price():
        _ss().dh_sd_err = None
        _go("loading")


def _cb_pay_back():
    ss = _ss()
    _go("reuse" if _pkey(ss.dh_sd_prof) in ss.get("dh_sd_traits", {}) and not ss.get("dh_sd_qi") else "mode")


# ─────────────── layar ───────────────
def _head(sub=None):
    f = FEAT[_feat()]
    st.markdown('<div class="dh-step dh-step-bp"></div>'
                f'<div class="dh-bp-head"><span class="dh-bp-ico">{f["ico"]}</span><div><div class="dh-bp-h">{f["h"]}</div>'
                f'<div class="dh-bp-hs">{sub or f["sub"]}</div></div></div>', unsafe_allow_html=True)


def _render_start():
    ss = _ss()
    u = auth.current_user()
    f = FEAT[_feat()]
    _head()
    st.markdown('<div class="dh-bp-chips">' + "".join(f"<i>✓ {_e(x)}</i>" for x in f["need"]) + "</div>", unsafe_allow_html=True)
    prof = ss.get("dh_sd_prof") or ss.get("dh_solo_prof") or {}
    form_kit.data_bar("dhsd", _feat())
    with st.container(key="dhbp_card"):
        st.markdown('<div class="dh-bp-sec">DATA DIRI</div>', unsafe_allow_html=True)
        c1, c2 = st.columns([1.15, 1], gap="small")
        with c1:
            st.text_input("Nama Lengkap / Panggilan", value=prof.get("nama") or (u or {}).get("nama", ""), key="dhsd_nama")
        with c2:
            st.date_input("Tanggal Lahir", value=prof.get("tgl"), min_value=date(1900, 1, 1), max_value=date.today(),
                          format="DD/MM/YYYY", key="dhsd_tgl")
        st.markdown('<div class="dh-bp-note sm">Setelah ini kamu menjawab kuesioner kepribadian (pilih Cepat atau Deep). '
                    'Jawabannya dipakai bersama Career DNA &amp; Strength &amp; Blind Spot, jadi cuma sekali.</div>', unsafe_allow_html=True)
    price, saldo = _price(), int(u.get("koin", 0))
    st.markdown('<div class="dh-bp-price">'
                f'<div class="dh-bp-row"><span>Akun:</span><b class="ok">● {_e(u["email"])}</b></div>'
                f'<div class="dh-bp-row"><span>Harga:</span><b class="big">{P.coin(price)}</b></div>'
                f'<div class="dh-bp-row"><span>Saldo Kamu:</span><b>{P.coin(saldo)}</b></div></div>', unsafe_allow_html=True)
    if ss.get("dh_sd_err"):
        st.error(ss.dh_sd_err)
    if saldo < price:
        st.markdown(f'<div class="dh-bp-warn">Saldo belum cukup, kurang {P.coin(price - saldo)}. Top-up dulu ya.</div>', unsafe_allow_html=True)
    with st.container(key="dhbp_cta"):
        st.button(f["go"], key="dhsd_go", type="primary", on_click=_cb_start, use_container_width=True)


def _menit(n):
    return max(1, round(n * SEC_PER_Q / 60))


def _render_mode():
    ss = _ss()
    sel = ss.get("dh_sd_modesel")
    if ss.get("dh_sd_modeconf") and sel:
        nm = "Cepat" if sel == "singkat" else "Deep"
        cc.layer("sdmode", _mode_screen, on_go=lambda: _cb_mode(sel), on_stay=_cb_modestay, icon="📝",
                 title="Mulai Kuesioner?", text=f"Apakah kamu yakin ingin melanjutkan dengan kuesioner mode <b>{nm}</b>?",
                 stay="Batal / Beralih", go="Ya, Lanjutkan")
    else:
        _mode_screen()


def _mode_screen():
    ss = _ss()
    sel = ss.get("dh_sd_modesel")
    _head("Pilih kedalaman kuesioner kepribadianmu.")
    n_s, n_l = len(BC.plan("singkat", CC.QUIZ_SYSTEMS)), len(BC.plan("lengkap", CC.QUIZ_SYSTEMS))
    st.markdown('<div class="dh-bp-note">Kuesioner: <b>MBTI, Big Five, Enneagram, DISC</b>. Satu pertanyaan per layar, '
                'semua wajib dijawab.</div>', unsafe_allow_html=True)
    cards = [("singkat", "⚡ Cepat", n_s, "Gambaran awal yang cukup baik.",
              "Tiap dimensi dinilai dari sedikit soal (MBTI 4 soal per dimensi, Big Five 3 per sifat, Enneagram 2 per tipe). "
              "Hasil bisa bergeser kalau kamu menjawab ulang."),
             ("lengkap", "🎯 Deep", n_l, "Paling akurat &amp; stabil.",
              "Seluruh bank soal (MBTI 8 per dimensi, Big Five 7 per sifat, Enneagram 4 per tipe). "
              "Lebih sedikit tertukar akibat satu jawaban yang meleset.")]
    c1, c2 = st.columns(2, gap="small")
    for col, (m, ttl, n, tag, ds) in zip((c1, c2), cards):
        with col:
            st.markdown(f'<div class="dh-bp-mcard{" is-sel" if sel == m else ""}"><b>{ttl}</b><em>~{_menit(n)} menit · {n} soal</em>'
                        f'<p><b style="display:inline;font-size:12.5px">{tag}</b> {ds}</p></div>', unsafe_allow_html=True)
            with st.container(key=f"dhbp_mode_{m}"):
                st.button("Dipilih ✓" if sel == m else "Pilih", key=f"dhsd_pick_{m}", on_click=_cb_modesel, args=(m,),
                          type="primary" if sel == m else "secondary", use_container_width=True)
    with st.container(key="dhbp_cta"):
        st.button("Mulai Kuesioner →", key="dhsd_mode_go", type="primary", on_click=_cb_modeask,
                  disabled=not sel, use_container_width=True)
    st.button("← Kembali", key="dhsd_mode_back", on_click=_go, args=("start",), type="tertiary")


def _render_reuse():
    ss = _ss()
    t = ss["dh_sd_traits"][_pkey(ss.dh_sd_prof)]
    n = len(BC.plan(t["mode"], CC.QUIZ_SYSTEMS))
    _head("Jawaban kuesionermu sudah tersimpan.")
    nm = "Deep" if t["mode"] == "lengkap" else "Cepat"
    st.markdown(f'<div class="dh-bp-mcard"><b>✓ Kuesioner {nm} · {n} soal</b><em>Dipakai ulang, tanpa isi lagi</em>'
                '<p>Kamu pernah mengisinya di fitur lain. Pakai lagi, atau ulangi kalau ingin hasil yang lebih akurat.</p></div>',
                unsafe_allow_html=True)
    with st.container(key="dhbp_cta"):
        st.button("Pakai Jawaban Ini →", key="dhsd_reuse", type="primary", on_click=_cb_reuse, use_container_width=True)
    lbl = "Ulangi dengan Deep (lebih akurat)" if t["mode"] == "singkat" else "Ulangi Kuesioner"
    st.button(lbl, key="dhsd_redo", on_click=_go, args=("mode",), use_container_width=True)
    st.button("← Kembali", key="dhsd_reuse_back", on_click=_go, args=("start",), type="tertiary")


def _qget(sys_, qid):
    return (_ss().get("dh_sd_ans") or {}).get(sys_, {}).get(qid)


def _qput(sys_, qid, val):
    _ss().setdefault("dh_sd_ans", {}).setdefault(sys_, {})[qid] = val


def _qdone():
    ss = _ss()
    ss.setdefault("dh_sd_traits", {})[_pkey(ss.dh_sd_prof)] = {"mode": ss.dh_sd_mode, "ans": ss.dh_sd_ans}
    _go("pay")


def _render_quiz():
    ss = _ss()
    items = BC.plan(ss.get("dh_sd_mode") or "singkat", CC.QUIZ_SYSTEMS)
    prof = ss.get("dh_sd_prof") or {}
    meta = " · ".join(str(x) for x in (prof.get("tgl"), prof.get("kota")) if x)
    QK.render("dhsd", items, _qget, _qput, "dh_sd_qi", "Kuesioner " + ("Career DNA" if _feat() == "career" else "Strength & Blind Spot"),
              (prof.get("nama"), meta), lambda: _go("mode"), _qdone, _SCALE)


def _render_pay():
    ss = _ss()
    u, prof = auth.current_user(), ss.dh_sd_prof
    price, saldo = _price(), int(u.get("koin", 0))
    sisa = saldo - price
    _head("Konfirmasi pembayaran")
    nm = "Deep" if ss.get("dh_sd_mode") == "lengkap" else "Cepat"
    st.markdown('<div class="dh-bp-price">'
                f'<div class="dh-bp-row"><span>Untuk:</span><b>{_e(prof["nama"])}</b></div>'
                f'<div class="dh-bp-row"><span>Laporan:</span><b>{FEAT[_feat()]["h"].title()}</b></div>'
                f'<div class="dh-bp-row"><span>Kuesioner:</span><b>{nm} ✓ selesai</b></div><div class="dh-bp-line"></div>'
                f'<div class="dh-bp-row"><span>Harga:</span><b class="big">{P.coin(price)}</b></div>'
                f'<div class="dh-bp-row"><span>Saldo Kamu:</span><b>{P.coin(saldo)}</b></div>'
                f'<div class="dh-bp-row"><span>Sisa Setelah Transaksi:</span><b class="{"ok" if sisa >= 0 else "bad"}">{P.coin(sisa)}</b></div></div>',
                unsafe_allow_html=True)
    if ss.get("dh_sd_err"):
        st.error(ss.dh_sd_err)
    with st.container(key="dhbp_cta"):
        if sisa < 0:
            st.markdown(f'<div class="dh-bp-warn">Saldo belum cukup, kurang {P.coin(-sisa)}.</div>', unsafe_allow_html=True)
            if st.button("Top-up Saldo →", key="dhsd_topup", type="primary", use_container_width=True):
                request_with_return("pricing_keep", _feat(), dh_pr_tab="koin")
        else:
            st.button(f"✨ Bayar & Lihat Hasil ({P.coin(price)})", key="dhsd_pay", type="primary", on_click=_cb_pay,
                      use_container_width=True)
    st.button("← Kembali", key="dhsd_pay_back", on_click=_cb_pay_back, type="tertiary")


def _render_loading():
    ss = _ss()
    u, prof = auth.current_user(), ss.get("dh_sd_prof")
    price = _price()
    if not (u and prof) or u.get("koin", 0) < price:
        _go("pay")
        st.rerun(scope="fragment")
    st.markdown('<div class="dh-step dh-step-bp"></div><div class="dh-nodismiss"></div>', unsafe_allow_html=True)
    sc = CC.QUIZ_SYSTEMS
    st.markdown('<div class="dh-bp-lt">Menyusun profilmu…</div>'
                '<div class="dh-bp-ls">Menggabungkan 4 sistem kepribadian dan data tanggal lahirmu.</div>', unsafe_allow_html=True)
    box, n, t0 = st.empty(), len(sc), time.time()
    for k in range(n + 1):
        tiles = "".join(f'<span class="{"on" if i < k else ""}"><b>{BC.ICON[x]}</b><small>{_e(x)}</small></span>' for i, x in enumerate(sc))
        box.markdown(f'<div class="dh-bp-tiles">{tiles}</div><div class="dh-bp-prog big"><i style="width:{round(k / n * 100)}%"></i></div>'
                     f'<div class="dh-bp-pct">{round(k / n * 100)}%</div>', unsafe_allow_html=True)
        time.sleep(3.2 / n)
    try:
        mode = ss.get("dh_sd_mode") or "lengkap"
        raws = CC.trait_raws(ss.get("dh_sd_ans") or {}, mode)
        res = (CC.build_career if _feat() == "career" else CC.build_strength)(prof, raws, mode)
    except Exception:
        res = None
    if not res:
        ss.dh_sd_err = "Hasil belum bisa disusun dari jawabanmu. Saldo tidak dipotong."
        _go("pay")
        st.rerun(scope="fragment")
    u["koin"] -= price
    res["price"] = price
    ss.setdefault("dh_sd_store", {})[_skey(prof)] = res
    ss.dh_sd_res = res
    time.sleep(max(0, 0.3 - (time.time() - t0)))
    _go("result")
    st.rerun(scope="fragment")


# ─────────────── hasil ───────────────
def _radar(rel, order):
    cx = cy = 130
    R = 92
    pt = lambda i, k: (cx + R * k * math.sin(i * math.pi / 3), cy - R * k * math.cos(i * math.pi / 3))
    g = "".join('<polygon points="' + " ".join("%.1f,%.1f" % pt(i, k) for i in range(6)) + '" class="g"/>' for k in (.33, .66, 1))
    ax = "".join('<line x1="130" y1="130" x2="%.1f" y2="%.1f" class="g"/>' % pt(i, 1) for i in range(6))
    poly = " ".join("%.1f,%.1f" % pt(i, rel[l] / 100) for i, l in enumerate(CC.LETTERS))
    lab = "".join('<text x="%.1f" y="%.1f" class="%s">%s</text>' % (*[v + d for v, d in zip(pt(i, 1.27), (0, 5))],
                  "top" if l in order[:3] else "", l) for i, l in enumerate(CC.LETTERS))
    return f'<svg viewBox="0 0 260 260" class="dh-sd-radar">{g}{ax}<polygon points="{poly}" class="v"/>{lab}</svg>'


def _bars(rows):
    return "".join(f'<div class="dh-sd-bar"><span>{_e(a)}</span><div><i style="width:{max(4, v)}%"></i></div><b>{v}</b></div>' for a, v in rows)


def _sys_cards(items):
    return "".join(f'<div class="dh-sd-sys"><b>{x["icon"]} {_e(x["name"])}{" · " + _e(x["title"]) if x.get("title") else ""}</b>'
                   f'<p>{_fx(x["teks"])}</p></div>' for x in items)


def _res_career(r):
    L = CC.LETTER
    o = r["order"]
    lb = "".join(f'<div class="dh-sd-lv{" top" if l in o[:3] else ""}"><b>{l}</b><span>{_e(L[l]["nama"])}</span><em>{r["rel"][l]}</em></div>'
                 for l in o)
    out = (f'<div class="dh-bp-id"><div class="dh-bp-id-top"><span class="dh-bp-badge">CAREER DNA</span><em>ID: {_e(r["id"])}</em></div>'
           f'<div class="dh-bp-id-n">{_e(r["nama"])}</div><div class="dh-sd-code">{r["code"]}</div>'
           f'<div class="dh-bp-id-l">{_e(r["arketipe"])}</div></div>'
           f'<div class="dh-bp-card"><div class="dh-bp-ct">📡 RADAR MINAT KARIER (RIASEC)</div>'
           f'<div class="dh-sd-rwrap">{_radar(r["rel"], o)}<div class="dh-sd-lvs">{lb}</div></div>'
           + ('<div class="dh-bp-note sm">Huruf ke-3 dan ke-4 skornya sangat tipis; urutan tiga besar bisa bergeser.</div>' if r["tipis"] else "")
           + f'</div><div class="dh-bp-card"><div class="dh-bp-ct">🔹 INTI KARIERMU</div><p>{_e(r["inti"])}</p>'
           f'<div class="dh-bp-blk"><b>🏢 Lingkungan kerja ideal</b><p>{_e(r["lingkungan"])}</p></div>'
           f'<div class="dh-bp-blk"><b>🔥 Yang menggerakkanmu</b><p>{_e(r["motivasi"])}</p></div>'
           f'<div class="dh-bp-blk"><b>🧩 Pendamping: {_e(r["kedua"])}</b><p>Huruf kedua menentukan gaya kerjamu; peran terbaik biasanya memadukan keduanya.</p></div></div>'
           f'<div class="dh-bp-card"><div class="dh-bp-ct">💼 PERAN YANG COCOK</div><div class="dh-bp-chips">'
           + "".join(f"<i>{_e(x)}</i>" for x in r["peran"]) + '</div>'
           '<div class="dh-bp-ct2">Industri yang cocok</div><div class="dh-bp-chips">'
           + "".join(f"<i>{_e(x)}</i>" for x in r["industri"]) + '</div></div>')
    if r["sistem"]:
        out += f'<div class="dh-bp-card"><div class="dh-bp-ct">🧠 KARIER MENURUT KEPRIBADIANMU</div>{_sys_cards(r["sistem"])}</div>'
    if r["sinyal"]:
        out += (f'<div class="dh-bp-card"><div class="dh-bp-ct">🌙 SINYAL DARI TANGGAL LAHIRMU</div>{_sys_cards(r["sinyal"])}</div>')
    out += ('<div class="dh-bp-card"><div class="dh-bp-ct">🗓️ RENCANA AKSI 30 HARI</div>'
            + "".join(f'<div class="dh-bp-rm"><b>{_e(a)}</b><p>{_e(b)}</p></div>' for a, b in r["plan"]) + '</div>')
    return out


def _res_strength(r):
    out = (f'<div class="dh-bp-id"><div class="dh-bp-id-top"><span class="dh-bp-badge">STRENGTH &amp; BLIND SPOT</span><em>ID: {_e(r["id"])}</em></div>'
           f'<div class="dh-bp-id-n">{_e(r["nama"])}</div><div class="dh-bp-id-c">'
           + "".join(f"<span><small>{a}</small><b>{_e(str(b))}</b></span>" for a, b in (("MBTI", r["mbti"]), ("DISC", r["disc"]), ("Enneagram", r["enn"])) if b)
           + '</div></div>')
    if r["bars"]:
        out += '<div class="dh-bp-card"><div class="dh-bp-ct">📊 PETA KARAKTERMU</div>'
        if r["bars"].get("ocean"):
            out += '<div class="dh-bp-ct2">Big Five</div>' + _bars(r["bars"]["ocean"])
        if r["bars"].get("disc"):
            out += '<div class="dh-bp-ct2">DISC</div>' + _bars(r["bars"]["disc"])
        out += "</div>"
    out += ('<div class="dh-bp-card"><div class="dh-bp-ct">💪 KEKUATAN UTAMA</div><div class="dh-bp-chips">'
            + "".join(f"<i>{_e(t)}</i>" for t in r["tags"]) + "</div>" + _sys_cards(r["kuat"]) + "</div>")
    bl = "".join(f'<div class="bl"><small>{_e(s)}</small><b>{_e(lab)}</b><p>{_e(gej)}</p>'
                 + (f'<p class="tw">🛠️ {_e(pen)}</p>' if pen else "") + "</div>" for s, _t, lab, gej, pen in r["blind"])
    out += f'<div class="dh-bp-ct2">🌑 {len(r["blind"])} TITIK BUTA</div><div class="dh-bp-grid">{bl}</div>'
    if r["overuse"]:
        out += f'<div class="dh-bp-card"><div class="dh-bp-ct">⚖️ KEKUATAN YANG JADI BUMERANG</div><p>{_e(r["overuse"])}</p></div>'
    if r["practice"]:
        out += f'<div class="dh-bp-card"><div class="dh-bp-ct">🧭 LATIHAN HARIAN</div>{_sys_cards(r["practice"])}</div>'
    return out


def _pl(t):
    return re.sub(r"\*\*(.+?)\*\*", r"\1", str(t or ""))


def _sections(r):
    """Isi hasil sebagai [(judul, [baris])] untuk PDF + Salin Teks (data sama dengan layar)."""
    sc = lambda items: [f'{x["name"]}' + (f' · {x["title"]}' if x.get("title") else "") + f': {_pl(x["teks"])}' for x in items]
    if "plan" in r:
        out = [("KODE & ARKETIPE", [f'{r["code"]} · {r["arketipe"]}']),
               ("INTI KARIERMU", [r["inti"], f'Lingkungan kerja ideal: {r["lingkungan"]}', f'Yang menggerakkanmu: {r["motivasi"]}']),
               ("PERAN YANG COCOK", list(r["peran"])), ("INDUSTRI YANG COCOK", list(r["industri"]))]
        if r["sistem"]:
            out.append(("KARIER MENURUT KEPRIBADIANMU", sc(r["sistem"])))
        if r["sinyal"]:
            out.append(("SINYAL DARI TANGGAL LAHIRMU", sc(r["sinyal"])))
        out.append(("RENCANA AKSI 30 HARI", [f"{a}: {b}" for a, b in r["plan"]]))
        return out
    out = [("KEKUATAN UTAMA", list(r["tags"]) + sc(r["kuat"])),
           ("TITIK BUTA", [f"{s}: {lab}. {gej}" + (f" Cara menyiasati: {pen}" if pen else "") for s, _t, lab, gej, pen in r["blind"]])]
    if r["overuse"]:
        out.append(("KEKUATAN YANG JADI BUMERANG", [r["overuse"]]))
    if r["practice"]:
        out.append(("LATIHAN HARIAN", sc(r["practice"])))
    return out


def _plain_result(r):
    ttl = "CAREER DNA" if "plan" in r else "STRENGTH & BLIND SPOT"
    lines = [f'{ttl} · {r["nama"]} ({r["id"]})', ""]
    for t, xs in _sections(r):
        lines += [t, *xs, ""]
    lines.append("Cek takdirmu di destinyreveal.id #DestinyReveal")
    return "\n".join(lines)


def _pdf_result(r):
    if not r.get("_pdf"):
        ttl = "Career DNA" if "plan" in r else "Strength & Blind Spot"
        r["_pdf"] = make_pdf(ttl, f'Untuk: {r["nama"]} · {r["id"]}', [(t, xs or ["-"]) for t, xs in _sections(r)])
    return r["_pdf"]


def _card_png(r):
    if r.get("_png"):
        return r["_png"]
    if "plan" in r:
        r["_png"] = trait_cards.kartu_karier(r["nama"], r["code"], r["arketipe"], r["rel"], r["peran"])
    else:
        r["_png"] = trait_cards.kartu_kekuatan(r["nama"], r["tags"], [b[2] for b in r["blind"]])
    return r["_png"]


def _render_result():
    ss = _ss()
    r = ss.get("dh_sd_res")
    if not r:
        _go("start")
        st.rerun(scope="fragment")
    st.markdown('<div class="dh-step dh-step-bp"></div>', unsafe_allow_html=True)
    st.markdown(_res_career(r) if "plan" in r else _res_strength(r), unsafe_allow_html=True)
    cap = f'{FEAT[_feat()]["h"].title()} {r["nama"]}\nCek takdirmu di destinyreveal.id #DestinyReveal'
    with st.container(key="dhbp_actions"):
        c1, c2 = st.columns(2, gap="small")
        with c1:
            st.download_button("Download PDF", _pdf_result(r), file_name=f"{_feat()}-{r['id']}.pdf", mime="application/pdf",
                               key="dhsd_pdf", use_container_width=True, on_click="ignore", icon=":material/download:")
        with c2:
            copy_button(_plain_result(r), "📋 Salin Teks", "dhsd_copy", fs=12.5, h=48, brown=True)
        c3, c4 = st.columns(2, gap="small")
        with c3:
            st.download_button("Save Image", _card_png(r), file_name=f"{_feat()}-{r['id']}.png", mime="image/png",
                               key="dhsd_png", use_container_width=True, on_click="ignore", icon=":material/image:")
        with c4:
            st.link_button("Share WhatsApp", f"https://wa.me/?text={urlquote(cap)}", use_container_width=True,
                           icon=":material/share:")
        st.button("Tutup", key="dhsd_done", on_click=cc.cb_ask, args=(_feat(),), use_container_width=True)


def _dialog_body(feat):
    ss = _ss()
    if ss.get("dh_sd_feat") != feat:  # ganti fitur -> mulai dari awal (hasil tersimpan tetap)
        ss.dh_sd_feat = feat
        _reset_view()
    if not auth.current_user():
        request_with_return("auth", feat)
    step = ss.get("dh_sd_step", "start")
    if step == "result" and ss.get("dh_sd_res"):
        cc.wrap(_feat(), _render_result, leave=_reset_view, icon=FEAT[feat]["ico"], title="Yakin Mau Tutup Hasil Ini?",
                      text="Hasil ini sudah tersimpan. Buka lagi dari menu ini tanpa bayar ulang (isi data yang sama).",
                      tip="Simpan kartu PNG dulu kalau mau dibagikan.", stay="✨ Lanjut Baca", go="Ya, Tutup")
    elif step == "reuse" and ss.get("dh_sd_prof"):
        _render_reuse()
    elif step == "mode":
        _render_mode()
    elif step == "quiz":
        _render_quiz()
    elif step == "pay" and ss.get("dh_sd_prof"):
        _render_pay()
    elif step == "loading":
        _render_loading()
    else:
        _render_start()


@st.dialog("Career DNA", width="large", on_dismiss=_cb_close)
def career_dialog():
    _dialog_body("career")


@st.dialog("Strength & Blind Spot", width="large", on_dismiss=_cb_close)
def strength_dialog():
    _dialog_body("strength")


DIALOGS = {"career": career_dialog, "strength": strength_dialog}
