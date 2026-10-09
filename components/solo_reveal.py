"""
Solo Reveal (UI23): pilih 1 dari 15 sistem -> (kuesioner, khusus 5 sistem psikologi) -> bayar 200 ✨ -> hasil A-F.
Satu st.dialog, langkah ganti-ganti lewat on_click callback (dialog tetap kebuka).
State (session_state): dh_solo_step | dh_solo_sys | dh_solo_prof | dh_solo_ans | dh_solo_res
DUMMY: saldo ✨ dipotong di session saja (belum ada backend/DB).
"""

import html
import time
from datetime import date
from urllib.parse import quote as urlquote

import streamlit as st
from content import pricing as P

from components import auth
from components import form_kit
from components import close_confirm as cc
from components.dialog_bus import request_with_return
from utils.simple_pdf import make_pdf
from components import life_chart
from components.combo import build_combo
from components.modal_detail import build_detail, copy_button, render_combo_card
from content.questionnaires.big_five_soal import BIG_FIVE_QUESTIONS
from content.questionnaires.disc_soal import DISC_QUESTIONS
from content.questionnaires.enneagram_soal import ENNEAGRAM_QUESTIONS
from content.questionnaires.love_language_soal import LOVE_LANGUAGE_QUESTIONS
from content.questionnaires.mbti_soal import MBTI_QUESTIONS
from content.result_builder import build_display_data, compute_quiz_raw_result, compute_raw_result

SOLO_PRICE = P.SOLO  # Stardust

# (nama sistem di engine, ikon, jenis) — jenis "lahir" = dihitung dari data lahir, "quiz" = kuesioner
SYSTEMS = [
    ("Zodiak", "♈", "lahir"), ("Shio", "🐉", "lahir"), ("Weton", "🗓️", "lahir"),
    ("Numerologi", "🔢", "lahir"), ("Matrix Destiny", "🔷", "lahir"),
    ("MBTI", "🧠", "quiz"), ("Big Five", "📊", "quiz"), ("Enneagram", "🔺", "quiz"),
    ("DISC", "🎯", "quiz"), ("Love Language", "💖", "quiz"),
    ("BaZi", "🀄", "lahir"), ("Zi Wei", "⭐", "lahir"), ("Human Design", "🔮", "lahir"),
    ("Golongan Darah", "🩸", "lahir"), ("Tarot", "🎴", "lahir"),
]
_KIND = {n: k for n, _i, k in SYSTEMS}
_ICON = {n: i for n, i, _k in SYSTEMS}
_BANK = {"MBTI": MBTI_QUESTIONS, "Big Five": BIG_FIVE_QUESTIONS, "Enneagram": ENNEAGRAM_QUESTIONS,
         "DISC": DISC_QUESTIONS, "Love Language": LOVE_LANGUAGE_QUESTIONS}
_SCALE = {1: "Sangat Tidak Setuju", 2: "Tidak Setuju", 3: "Netral", 4: "Setuju", 5: "Sangat Setuju"}
_GOLDA = ["A", "B", "AB", "O", "Belum tahu"]
_ASPEK = ["A. ASPEK UTAMA", "B. KARIER & KEUANGAN", "C. ASMARA & HUBUNGAN",
          "D. KEKUATAN KARAKTER", "E. SHADOW WORK", "F. NASIHAT STRATEGIS"]
_ASPEK_ICON = ["📖", "💼", "💗", "💪", "🔮", "⚖️"]
_EMPTY = "Seksi ini sedang disiapkan untuk sistem ini."


def _e(t):
    return html.escape(str(t))


def _saldo():
    u = auth.current_user()
    return int(u.get("koin", 0)) if u else 0


# ─────────────── callbacks ───────────────
def _go(step):
    st.session_state.dh_solo_step = step


ACTIVE = tuple(n for n, _i, _k in SYSTEMS)  # semua 15 sistem aktif
_BIRTH5 = ("Zodiak", "Shio", "Weton", "Numerologi", "Matrix Destiny")  # punya JSON profil A-F


def _cb_pick(name):
    ss = st.session_state
    ss.dh_solo_sys = name
    ss.dh_solo_err = None


def _cb_to_next():
    """Dari pilih sistem: validasi data diri -> kuesioner (sistem psikologi) atau bayar."""
    ss = st.session_state
    name = ss.get("dh_solo_sys")
    prof = _profile()
    if not name:
        ss.dh_solo_err = "Pilih salah satu sistem dulu ya."
        return
    if not prof:
        nama = (ss.get("dhso_nama") or "").strip()
        tgl = ss.get("dhso_tgl")
        if not nama or not tgl:
            ss.dh_solo_err = "Isi Nama Lengkap dan Tanggal Lahir dulu ya (bertanda Wajib)."
            return
        jam = ss.get("dhso_jam")
        prof = {"nama": nama, "tgl": tgl, "jam": jam, "kota": (ss.get("dhso_kota") or "").strip(),
                "golda": ss.get("dhso_golda") or ""}
        ss.dh_solo_prof = prof
    else:  # profil sudah ada: lengkapi jam / golda dari field tambahan kalau sistemnya butuh
        prof = dict(prof)
        if ss.get("dhso_jam2") and not prof.get("jam"):
            prof["jam"] = ss.dhso_jam2
        if ss.get("dhso_golda2") and prof.get("golda") in ("", "Belum tahu", None):
            prof["golda"] = ss.dhso_golda2
    if name in ("Zi Wei", "Human Design") and not prof.get("jam"):
        ss.dh_solo_err = f"{name} butuh Jam Lahir. Isi Jam Lahir dulu ya."
        return
    if name == "Golongan Darah" and prof.get("golda") in ("", "Belum tahu"):
        ss.dh_solo_err = "Golongan Darah butuh pilihan golongan darahmu (A/B/AB/O)."
        return
    ss.dh_solo_prof = prof  # selalu simpan, juga kalau profil dari data Reveal
    ss.dh_solo_err = None
    _go("quiz" if _KIND[name] == "quiz" else "pay")


def _cb_quiz_done():
    ss = st.session_state
    name = ss.dh_solo_sys
    ans = {}
    for q in _BANK[name]:
        v = ss.get(f"dhsoq_{q['id']}")
        if v is None:
            ss.dh_solo_err = "Masih ada soal yang belum dijawab. Lengkapi semuanya dulu ya."
            return
        ans[q["id"]] = v
    ss.dh_solo_ans = ans
    ss.dh_solo_err = None
    _go("pay")


# alias key JSON per aspek (dibaca langsung dari JSON; urutan = prioritas)
_ALIAS = {
    "A": ("aspek_utama", "siapa_kamu"),
    "B": ("karier_dan_keuangan", "karir", "keuangan"),
    "C": ("asmara_dan_hubungan", "asmara"),
    "D": ("kekuatan_karakter", "kekuatan_yang_perlu_dijaga"),
    "E": ("shadow_work", "shadow", "sisi_gelap", "shadow_side", "blindspot"),
    "F": ("nasihat_strategis", "nasihat", "rekomendasi"),
}


def _entry_aspek(entry):
    """Teks aspek A-F dari satu entri JSON. Prioritas: sections.A-F (format A-M) -> key bernama
    (paid/free/sections/entri) sesuai _ALIAS -> cadangan lama (E = pr_kecil_buat_kamu, F = kesehatan)."""
    sec = entry.get("sections") if isinstance(entry.get("sections"), dict) else {}
    pools = [sec, entry.get("paid") or {}, entry.get("free") or {}, entry]

    def one(key):
        for pool in pools:
            v = pool.get(key)
            if isinstance(v, str) and v.strip():
                return v.strip()
            if isinstance(v, list):
                t = [str(x).strip() for x in v if str(x).strip()]
                if t:
                    return "\n".join(t)
        return ""

    out = {}
    for h, keys in _ALIAS.items():
        texts = [one(h)] if one(h) else []
        if not texts:
            texts = [t for t in (one(k) for k in keys) if t]
            if h in "AEF" and texts:
                texts = texts[:1]
        out[h] = texts
    if not out["E"]:
        out["E"] = [t for t in [one("pr_kecil_buat_kamu")] if t]
    if not out["F"]:
        out["F"] = [t for t in [one("kesehatan")] if t]
    return [out[h] for h in "ABCDEF"]


def _solo_detail(name, raw):
    """Detail A-F. 5 sistem lahir = JSON A-F. 10 sistem lain = dibaca dari entri JSON-nya (lihat _entry_aspek)."""
    d = build_detail(name, raw)
    if not d or name in _BIRTH5:
        return d
    from content import profile_flat
    prof = profile_flat.get_big_five(raw) if name == "Big Five" else profile_flat.get_profile(name, raw)
    entry = (prof or {}).get("entry")
    if not entry:
        return d
    secs = _entry_aspek(entry)
    if name == "Big Five":  # narasi utama + ringkasan 4 trait lain
        disp = build_display_data(name, raw) or {}
        if disp.get("p1"):
            secs[0] = [disp["p1"]]
    d["sections"] = [(ic, t, texts, tone) for (ic, t, _old, tone), texts in zip(d["sections"], secs)]
    return d


def _cb_pay():
    """Validasi saldo & data, lalu masuk layar loading (hitung + potong saldo ada di _render_loading)."""
    ss = st.session_state
    u = auth.current_user()
    if not u or u.get("koin", 0) < SOLO_PRICE:
        return
    if not (ss.get("dh_solo_prof") or _profile()):
        ss.dh_solo_err = "Data diri belum lengkap. Kembali & isi dulu ya."
        return
    ss.dh_solo_err = None
    _go("loading")


def _render_loading():
    """Layar loading (tiru Reveal Dirimu): hitung hasil, potong saldo kalau berhasil, tampil minimal ~3 detik."""
    ss = st.session_state
    u = auth.current_user()
    name = ss.get("dh_solo_sys")
    prof = ss.get("dh_solo_prof") or _profile()
    if not (u and name and prof) or u.get("koin", 0) < SOLO_PRICE:
        _go("pay")
        st.rerun(scope="fragment")
    t0 = time.time()
    st.markdown(
        '<div class="dh-step dh-step-loading"></div><div class="dh-nodismiss"></div>'
        '<div class="dh-dl-load"><div class="dh-dl-orb"><i></i><span>✦</span></div>'
        f'<div class="dh-dl-t">Menyelaraskan Solo Reveal {_e(name)}...</div>'
        '<div class="dh-dl-s">Menghitung peta takdirmu dan menyusun 6 aspek analisis personal.</div></div>',
        unsafe_allow_html=True)
    if _KIND[name] == "quiz":
        raw = compute_quiz_raw_result(name, ss.get("dh_solo_ans") or {})
    else:
        raw = compute_raw_result(name, {
            "tanggal_lahir": prof["tgl"], "jam_lahir": prof.get("jam"), "kota_lahir": prof.get("kota"),
            "golongan_darah": prof.get("golda"), "nama_lengkap": prof["nama"]})
    detail = _solo_detail(name, raw)
    if not detail:
        ss.dh_solo_err = "Hasil sistem ini belum bisa dihitung untuk datamu (mis. tahun lahir di luar jangkauan). Saldo tidak dipotong."
        _go("pay")
        st.rerun(scope="fragment")
    u["koin"] -= SOLO_PRICE
    ss.dh_solo_res = {"system": name, "detail": detail, "nama": prof["nama"], "raw": raw}
    time.sleep(max(0.0, 3.0 - (time.time() - t0)))
    _go("result")
    st.rerun(scope="fragment")


def _cb_again():
    ss = st.session_state
    for k in ("dh_solo_res", "dh_solo_ans", "dh_solo_sys"):
        ss.pop(k, None)
    _go("select")


def _cb_close():
    """X di dialog. Loading -> balik ke bayar (saldo belum dipotong). Hasil -> tanya konfirmasi dulu."""
    ss = st.session_state
    step = ss.get("dh_solo_step")
    if step == "loading":
        _go("pay")
        return
    cc.dismiss("solo", step == "result" and bool(ss.get("dh_solo_res")), leave=_cb_again)


# ─────────────── data diri ───────────────
def _profile():
    """Profil siap pakai: akun login + data scan terakhir (tgl lahir) / data Solo sebelumnya."""
    ss = st.session_state
    u = auth.current_user()
    if not u:
        return None
    p = ss.get("dh_solo_prof")
    if p:
        return p
    md = ss.get("dh_modal_data") or {}
    if md.get("tgl_lahir"):
        jam = md.get("jam_lahir") or ""
        from datetime import time as _t
        jam_t = _t(int(jam[:2]), int(jam[3:5])) if len(jam) >= 5 and jam[2] == ":" else None
        return {"nama": u.get("nama") or md.get("nama") or "Kamu", "tgl": md["tgl_lahir"], "jam": jam_t,
                "kota": md.get("kota_lahir", ""), "golda": md.get("golongan_darah", "")}
    return None


def _render_form(u):
    with st.container(key="dhso_data"):  # satu kartu krem untuk seluruh Data Diri
        st.markdown('<div class="dh-modal-section"><span>📅 DATA DIRI</span><em>Wajib</em></div>', unsafe_allow_html=True)
        form_kit.data_bar("dhso", "solo")
        c1, c2 = st.columns([1.15, 1], gap="small")
        with c1:
            st.text_input("Nama Lengkap / Panggilan", value=(u or {}).get("nama", ""),
                          placeholder="Contoh: Rina Anggraini", key="dhso_nama")
        with c2:
            st.date_input("Tanggal Lahir", value=None, min_value=date(1900, 1, 1), max_value=date.today(),
                          format="DD/MM/YYYY", key="dhso_tgl")
        c3, c4, c5 = st.columns(3, gap="small")
        with c3:
            st.time_input("Jam Lahir (Opsional)", value=None, key="dhso_jam")
        with c4:
            st.text_input("Tempat Lahir (Opsional)", placeholder="Contoh: Jakarta", key="dhso_kota")
        with c5:
            st.selectbox("Golongan Darah", _GOLDA, index=None, placeholder="Pilih", key="dhso_golda")


# ─────────────── langkah 1: pilih sistem ───────────────
def _head(sub="Pilih 1 sistem, dapat analisis lengkap A-F"):
    st.markdown(
        '<div class="dh-step dh-step-solo"></div><div class="dh-nodismiss"></div>'
        '<div class="dh-so-head"><span class="dh-so-ico">🧭</span><div><div class="dh-so-brand">SOLO REVEAL</div>'
        f'<div class="dh-so-hsub">{sub} · {SOLO_PRICE} ✨</div></div></div><div class="dh-so-line"></div>',
        unsafe_allow_html=True)


def _render_select():
    ss = st.session_state
    u = auth.current_user()
    prof = _profile()
    _head()
    st.markdown(f'<div class="dh-so-h2">Pilih Sistem<span class="dh-so-pill">Biaya: {SOLO_PRICE} ✨</span></div>',
                unsafe_allow_html=True)
    if prof:
        tgl = prof["tgl"].strftime("%Y-%m-%d") if hasattr(prof["tgl"], "strftime") else str(prof["tgl"])
        st.markdown(
            f'<div class="dh-so-sub">Pilih 1 sistem yang mau kamu analisis secara mendalam (6 aspek A-F) untuk '
            f'{_e(prof["nama"])}.</div>'
            f'<div class="dh-so-prof"><span><i></i><b>{_e(prof["nama"])}</b> · {tgl}</span>'
            f'<span class="dh-so-bal">Saldo: {_saldo()} ✨</span></div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="dh-so-sub">Pilih 1 sistem yang mau kamu analisis secara mendalam (6 aspek A-F). '
                    + ('Lengkapi data dirimu dulu.' if u else 'Isi data dirimu (atau masuk akun supaya data terisi otomatis).')
                    + '</div>', unsafe_allow_html=True)
        _render_form(u)
    picked = ss.get("dh_solo_sys")
    if prof and picked in ("Zi Wei", "Human Design") and not prof.get("jam"):
        st.time_input(f"Jam Lahir (wajib untuk {picked})", value=None, key="dhso_jam2")
    if prof and picked == "Golongan Darah" and prof.get("golda") in ("", "Belum tahu", None):
        st.selectbox("Golongan Darah", _GOLDA[:4], index=None, placeholder="Pilih", key="dhso_golda2")
    st.markdown('<div class="dh-so-label">Pilih 1 dari 15 Sistem Kosmik:</div>', unsafe_allow_html=True)
    with st.container(key="dhso_grid"):
        for r in range(3):
            cols = st.columns(5, gap="small")
            for col, (name, icon, _k) in zip(cols, SYSTEMS[r * 5:(r + 1) * 5]):
                with col:
                    st.button(f"{icon}  \n**{name}**", key=f"dhso_pick_{name}", on_click=_cb_pick, args=(name,),
                              type="primary" if picked == name else "secondary", use_container_width=True)
    if ss.get("dh_solo_err"):
        st.error(ss.dh_solo_err)
    label = f"Lanjutkan ke Pembayaran ({SOLO_PRICE} ✨) →" if picked and _KIND[picked] != "quiz" else (
        f"Lanjut: Isi Kuesioner {picked} →" if picked else f"Lanjutkan ke Pembayaran ({SOLO_PRICE} ✨) →")
    with st.container(key="dhso_cta"):
        st.button(label, key="dhso_next", type="primary", use_container_width=True, on_click=_cb_to_next)



# ─────────────── langkah 1b: kuesioner (5 sistem psikologi) ───────────────
def _render_quiz():
    ss = st.session_state
    name = ss.dh_solo_sys
    bank = _BANK[name]
    _head(f"Kuesioner {name}")
    st.markdown(f'<div class="dh-so-h2">Kuesioner {_e(name)}<span class="dh-so-pill">{len(bank)} soal</span></div>'
                '<div class="dh-so-sub">Jawab jujur sesuai dirimu sehari-hari. Hasil dihitung dari jawabanmu.</div>',
                unsafe_allow_html=True)
    for n, q in enumerate(bank, 1):
        k = f"dhsoq_{q['id']}"
        if name in ("MBTI", "Enneagram"):
            st.markdown(f'<div class="dh-so-q">{n}. {_e(q["text"])}</div>', unsafe_allow_html=True)
            v = st.radio(k, ["Setuju", "Tidak Setuju"], index=None, key=k + "_r", horizontal=True,
                         label_visibility="collapsed")
            ss[k] = None if v is None else (v == "Setuju")
        elif name == "Big Five":
            st.markdown(f'<div class="dh-so-q">{n}. {_e(q["text"])}</div>', unsafe_allow_html=True)
            v = st.radio(k, [1, 2, 3, 4, 5], format_func=lambda i: f"{i}: {_SCALE[i]}", index=None, key=k + "_r",
                         horizontal=True, label_visibility="collapsed")
            ss[k] = v
        elif name == "DISC":
            st.markdown(f'<div class="dh-so-q">{n}. Pilih SATU kata yang PALING menggambarkan dirimu:</div>',
                        unsafe_allow_html=True)
            v = st.radio(k, ["A", "B", "C", "D"], format_func=lambda L, q=q: q["options"][L], index=None,
                         key=k + "_r", horizontal=True, label_visibility="collapsed")
            ss[k] = v
        else:  # Love Language
            st.markdown(f'<div class="dh-so-q">{n}. Pilih pernyataan yang paling menggambarkan dirimu:</div>',
                        unsafe_allow_html=True)
            v = st.radio(k, ["A", "B"], format_func=lambda L, q=q: f"{L}. {q[L]['text']}", index=None,
                         key=k + "_r", label_visibility="collapsed")
            ss[k] = v
    if ss.get("dh_solo_err"):
        st.error(ss.dh_solo_err)
    c1, c2 = st.columns([1, 2.2], gap="small")
    with c1:
        with st.container(key="dhso_back"):
            st.button("← Kembali", key="dhso_q_back", on_click=_go, args=("select",), use_container_width=True)
    with c2:
        with st.container(key="dhso_cta"):
            st.button(f"Lanjutkan ke Pembayaran ({SOLO_PRICE} ✨) →", key="dhso_q_next", type="primary",
                      use_container_width=True, on_click=_cb_quiz_done)


# ─────────────── langkah 2: pembayaran ───────────────
def _render_pay():
    ss = st.session_state
    u = auth.current_user()
    name = ss.dh_solo_sys
    saldo = _saldo()
    sisa = saldo - SOLO_PRICE
    _head()
    st.markdown(
        '<div class="dh-so-h2">Konfirmasi Pembayaran</div>'
        f'<div class="dh-so-sub">Sistem terpilih: <b class="dh-so-acc">{_e(name)}</b> {_ICON[name]}</div>'
        '<div class="dh-so-box">'
        f'<div class="dh-so-row"><span>Fitur Solo Reveal:</span><b>Analisis 6 Aspek ({_e(name)})</b></div>'
        f'<div class="dh-so-row"><span>Harga Fitur:</span><b class="dh-so-acc">{SOLO_PRICE} ✨</b></div>'
        f'<div class="dh-so-row"><span>Saldo Kamu:</span><b>{saldo} ✨</b></div>'
        f'<div class="dh-so-row dh-so-last"><span>Sisa Saldo Setelah Bayar:</span><b class="dh-so-big">{max(sisa, 0) if u else 0} ✨</b></div>'
        '</div>', unsafe_allow_html=True)
    if not u:
        st.markdown('<div class="dh-so-note bad">🔒 Kamu belum masuk akun. Masuk dulu supaya saldo ✨ bisa dipakai '
                    '(akun baru dapat bonus ✨).</div>', unsafe_allow_html=True)
    elif sisa < 0:
        st.markdown(f'<div class="dh-so-note bad">Saldo belum cukup, kurang {-sisa} ✨. Top-up dulu ya.</div>',
                    unsafe_allow_html=True)
    else:
        st.markdown('<div class="dh-so-note ok">✓ Saldo mencukupi! Klik bayar untuk memulai kalkulasi seketika.</div>',
                    unsafe_allow_html=True)
    if ss.get("dh_solo_err"):
        st.error(ss.dh_solo_err)
    back = "quiz" if _KIND[name] == "quiz" else "select"
    c1, c2 = st.columns([1, 2.2], gap="small")
    with c1:
        with st.container(key="dhso_back"):
            st.button("Batal / Kembali", key="dhso_p_back", on_click=_go, args=(back,), use_container_width=True)
    with c2:
        with st.container(key="dhso_cta"):
            if not u:
                if st.button("Masuk / Daftar untuk Bayar →", key="dhso_p_login", type="primary",
                             use_container_width=True):
                    request_with_return("auth", "solo")
            elif sisa < 0:
                if st.button("Top-up Saldo →", key="dhso_p_topup", type="primary", use_container_width=True):
                    request_with_return("pricing_keep", "solo", dh_pr_tab="koin")
            else:
                st.button(f"Bayar {SOLO_PRICE} ✨ →", key="dhso_p_pay", type="primary",
                          use_container_width=True, on_click=_cb_pay)


# ─────────────── langkah 3: hasil A-F ───────────────
def _render_result():
    res = st.session_state.get("dh_solo_res")
    if not res:
        _go("select")
        return _render_select()
    d, name, nama = res["detail"], res["system"], res["nama"]
    st.markdown('<div class="dh-step dh-step-solo dh-step-solo-lg"></div><div class="dh-nodismiss"></div>'
                '<div class="dh-so-head"><span class="dh-so-ico">🧭</span><div><div class="dh-so-brand">SOLO REVEAL</div>'
                f'<div class="dh-so-hsub">Pilih 1 sistem, dapat analisis lengkap A-F · {SOLO_PRICE} ✨</div></div></div>'
                '<div class="dh-so-line"></div>', unsafe_allow_html=True)
    quote = d.get("quote") or ""
    chips = "".join(f'<span class="dh-so-chip">{_e(k)}: <b>{_e(v)}</b></span>' for k, v in (d.get("params") or []))
    st.markdown(
        '<div class="dh-so-banner"><div class="dh-so-eyebrow">HASIL RESMI SOLO REVEAL</div>'
        f'<div class="dh-so-title">{_ICON[name]} SOLO REVEAL: {_e(name.upper())}</div>'
        f'<div class="dh-so-bsub"><b>{_e(d.get("title", ""))}</b> · Untuk: {_e(nama)}</div>'
        + (f'<div class="dh-so-quote">&ldquo;{_e(quote)}&rdquo;</div>' if quote else "") + '</div>'
        + (f'<div class="dh-so-chips">{chips}</div>' if chips else ""), unsafe_allow_html=True)
    _tg = (st.session_state.get("dh_solo_prof") or {}).get("tgl")
    if name in life_chart.SYSTEMS and _tg:  # dashboard visual: Roda Takdir / grafik usia 20-60
        st.markdown('<div style="font-weight:800;letter-spacing:.8px;font-size:12px;color:#B2552C;margin:14px 0 8px">🧭 PETA SIKLUS HIDUPMU</div>', unsafe_allow_html=True)
        life_chart.render(name, _tg, height=700 if name == "Matrix Destiny" else 560)
    secs = {i: (texts or []) for i, (_ic, _t, texts, _tone) in enumerate(d["sections"])}
    pdf_secs = [(_ASPEK[i], [t for t in secs.get(i, []) if t] or [_EMPTY]) for i in range(len(_ASPEK))]
    combo = build_combo(name, res.get("raw")) if res.get("raw") else []
    if combo:
        pdf_secs.append(("COMBO: KETIKA VARIABEL-VARIABELMU BERTEMU", [f'{b["title"]}: {b["text"]}' for b in combo]))
    st.download_button("📥 Download PDF", make_pdf(f"Solo Reveal - {name}", f'{d.get("title", "")} - Untuk: {nama}', pdf_secs),
                       file_name=f"solo-reveal-{name.lower().replace(' ', '-')}.pdf", mime="application/pdf",
                       key="dhso_pdf", use_container_width=True, on_click="ignore")
    plain = [f"SOLO REVEAL: {name} · {nama}", d.get("title", ""), ""]
    for i, title in enumerate(_ASPEK):
        texts = [t for t in secs.get(i, []) if t]
        body = "".join(f"<p>{_e(t)}</p>" for t in texts) or f'<p class="dh-so-empty">{_EMPTY}</p>'
        acc = " dh-so-amber" if i == len(_ASPEK) - 1 else ""
        st.markdown(f'<div class="dh-so-card{acc}"><div class="dh-so-ct"><span>{_ASPEK_ICON[i]}</span>{_e(title)}</div>{body}</div>',
                    unsafe_allow_html=True)
        plain += [title, *texts, ""]
    render_combo_card(name, combo)  # kartu combo di paling bawah analisis, sebelum tombol aksi
    if combo:
        plain += ["COMBO: KETIKA VARIABEL-VARIABELMU BERTEMU", ""]
        for b in combo:
            plain += [b["title"], b["text"], ""]
    cap = f"Solo Reveal {name}: {nama}\nCek takdirmu di destinyreveal.id #DestinyReveal"
    with st.container(key="dhso_acts"):
        a1, a2 = st.columns(2, gap="small")
        with a1:
            copy_button("\n".join(plain).strip(), "📋 Salin Seluruh Analisis", "dhso_copy", fs=12.5, h=46)
        with a2:
            st.link_button("Share ke WhatsApp", f"https://wa.me/?text={urlquote(cap)}", use_container_width=True,
                           key="dhso_wa", icon=":material/share:")
        b1, b2 = st.columns(2, gap="small")
        with b1:
            st.button(f"🔄 Pilih Sistem Kosmik Lain ({SOLO_PRICE}✨)", key="dhso_again", on_click=_cb_again,
                      use_container_width=True)
        with b2:
            st.button("Selesai & Tutup", key="dhso_done", type="primary", use_container_width=True,
                      on_click=cc.cb_ask, args=("solo",))


@st.dialog("Solo Reveal", width="large", on_dismiss=_cb_close)
def solo_dialog():
    ss = st.session_state
    step = ss.get("dh_solo_step", "select")
    if step == "result" and ss.get("dh_solo_res"):
        if cc.asking("solo"):
            cc.render("solo", leave=_cb_again, icon="🧭", title="Yakin Mau Tutup Hasil Solo Reveal?",
                      text="Analisis 6 aspekmu baru saja terbuka. Kalau ditutup, hasil ini tidak bisa dilihat lagi tanpa "
                           f"membuka ulang ({SOLO_PRICE} ✨).",
                      tip="Download PDF atau salin analisis dulu, biar bisa dibaca kapan saja.",
                      stay="✨ Lanjut Baca", go="Ya, Tutup Hasil")
        else:
            _render_result()
    elif step == "loading" and ss.get("dh_solo_sys"):
        _render_loading()
    elif step == "quiz" and ss.get("dh_solo_sys"):
        _render_quiz()
    elif step == "pay" and ss.get("dh_solo_sys"):
        _render_pay()
    else:
        _render_select()


def open_solo():
    """Dari kartu Premium: lanjut dari langkah terakhir (mis. balik dari login) / tampilkan hasil yang sudah dibayar."""
    ss = st.session_state
    ss.dh_solo_err = None
    solo_dialog()


DIALOGS = {"solo": open_solo}
