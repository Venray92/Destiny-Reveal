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

from utils import resume as _resume
from content import pricing as P

from components import auth
from components import form_kit
from components import close_confirm as cc
from components import quiz_kit as QK
from components import result_kit as RK
from components.aspek_info import heading_with_info
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


def _okey(name, prof, ans=None):
    """Kunci hasil yang sudah dibeli: sistem + orang (+ jawaban kuesioner, supaya tes ulang dengan jawaban beda = hasil baru)."""
    k = f"{name}|{prof.get('nama', '')}|{prof['tgl'].isoformat()}"
    if ans:
        k += "|" + ",".join(f"{a}={ans[a]}" for a in sorted(ans))
    return k


def _open_owned(name, prof, ans=None):
    """Kalau sudah dibeli: buka hasilnya gratis. Return True kalau dibuka."""
    ss = st.session_state
    res = (ss.get("dh_solo_store") or {}).get(_okey(name, prof, ans))
    if not res:
        return False
    ss.dh_solo_res = res
    ss.dh_solo_free = True
    _go("result")
    return True


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
    nama = (ss.get("dhso_nama") or "").strip()
    tgl = ss.get("dhso_tgl")
    if not nama or not tgl:
        ss.dh_solo_err = "Isi Nama Lengkap dan Tanggal Lahir dulu ya (bertanda Wajib)."
        return
    prof = {"nama": nama, "tgl": tgl, "jam": ss.get("dhso_jam"), "kota": (ss.get("dhso_kota") or "").strip(),
            "golda": ss.get("dhso_golda") or ""}
    if name in ("Zi Wei", "Human Design") and not prof.get("jam"):
        ss.dh_solo_err = f"{name} butuh Jam Lahir. Isi Jam Lahir dulu ya."
        return
    if name == "Golongan Darah" and prof.get("golda") in ("", "Belum tahu"):
        ss.dh_solo_err = "Golongan Darah butuh pilihan golongan darahmu (A/B/AB/O)."
        return
    ss.dh_solo_prof = prof  # selalu simpan, juga kalau profil dari data Reveal
    ss.dh_solo_err = None
    if _KIND[name] != "quiz" and _open_owned(name, prof):
        return
    if _KIND[name] == "quiz":
        ss.dh_solo_qi = 0
        for q in _BANK[name]:
            ss.pop(f"dhsoq_{q['id']}", None)
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
    if ss.get("dh_solo_prof") and _open_owned(name, ss.dh_solo_prof, ans):
        return
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
        f'<div class="dh-dl-t">Menyelaraskan One-System Blueprint {_e(name)}...</div>'
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
    _resume.scanned("solo")  # fitur lain yang kuesionernya tertunda di-reset
    ss.dh_solo_res = {"system": name, "detail": detail, "nama": prof["nama"], "raw": raw}
    ss.dh_solo_free = False
    ss.setdefault("dh_solo_store", {})[_okey(name, prof, ss.get("dh_solo_ans") if _KIND[name] == "quiz" else None)] = ss.dh_solo_res
    time.sleep(max(0.0, 3.0 - (time.time() - t0)))
    _go("result")
    st.rerun(scope="fragment")


def _cb_again():
    ss = st.session_state
    for k in ("dh_solo_res", "dh_solo_ans", "dh_solo_sys", "dh_solo_free"):
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


def _prefill_form(prof):
    """Isi field form dari profil (akun / data scan) sekali, selama field belum ada di state."""
    ss = st.session_state
    p = prof or form_kit.my_data() or {}
    if not p or "dhso_nama" in ss:
        return
    tgl = p.get("tgl")
    if isinstance(tgl, str):
        try:
            tgl = date.fromisoformat(tgl[:10])
        except ValueError:
            tgl = None
    ss.dhso_nama = p.get("nama") or ""
    ss.dhso_tgl = tgl
    ss.dhso_jam = p.get("jam") or None
    ss.dhso_kota = p.get("kota") or ""
    ss.dhso_golda = p.get("golda") if p.get("golda") in _GOLDA else None


def _render_form(u):
    with st.container(key="dhso_data"):  # satu kartu krem untuk seluruh Data Diri
        st.markdown('<div class="dh-modal-section"><span>📅 DATA DIRI</span><em>Wajib</em></div>', unsafe_allow_html=True)
        form_kit.data_bar("dhso", "solo")
        c1, c2 = st.columns([1.15, 1], gap="small")
        with c1:
            st.text_input("Nama Lengkap / Panggilan", placeholder="Contoh: Rina Anggraini", key="dhso_nama")
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
        '<div class="dh-so-head"><span class="dh-so-ico">🧭</span><div><div class="dh-so-brand">ONE-SYSTEM BLUEPRINT</div>'
        f'<div class="dh-so-hsub">{sub}</div></div></div><div class="dh-so-line"></div>',
        unsafe_allow_html=True)


def _render_select():
    ss = st.session_state
    u = auth.current_user()
    prof = _profile()
    _head()
    heading_with_info('<div class="dh-so-h2">Pilih Sistem</div>', "solo", "AF")
    if u:
        _prefill_form(prof)
        st.markdown(f'<div class="dh-so-prof"><span><i></i><b>{_e(u.get("nama") or "Kamu")}</b></span>'
                    f'<span class="dh-so-bal">Saldo: {_saldo()} ✨</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="dh-so-sub">Pilih 1 sistem untuk dianalisis mendalam (6 aspek A-F). '
                + ('Cek data dirimu di bawah, ubah kalau perlu.' if u else
                   'Isi data dirimu (atau masuk akun supaya terisi otomatis).') + '</div>', unsafe_allow_html=True)
    _render_form(u)
    picked = ss.get("dh_solo_sys")
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
def _qget(sys_, qid):
    return st.session_state.get(f"dhsoq_{qid}")


def _qput(sys_, qid, val):
    st.session_state[f"dhsoq_{qid}"] = val


def _render_quiz():
    ss = st.session_state
    name = ss.dh_solo_sys
    items = [{"sys": name, "q": q} for q in _BANK[name]]
    prof = ss.get("dh_solo_prof") or {}
    meta = " · ".join(str(x) for x in (prof.get("tgl"), prof.get("kota")) if x)
    QK.render("dhsoqz", items, _qget, _qput, "dh_solo_qi", f"Kuesioner {name}", (prof.get("nama"), meta),
              lambda: _go("select"), _cb_quiz_done, _SCALE)


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
        f'<div class="dh-so-row"><span>Fitur One-System Blueprint:</span><b>Analisis 6 Aspek ({_e(name)})</b></div>'
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
                '<div class="dh-so-head"><span class="dh-so-ico">🧭</span><div><div class="dh-so-brand">ONE-SYSTEM BLUEPRINT</div>'
                f'<div class="dh-so-hsub">Pilih 1 sistem, dapat analisis lengkap A-F</div></div></div>'
                '<div class="dh-so-line"></div>', unsafe_allow_html=True)
    quote = d.get("quote") or ""
    chips = "".join(f'<span class="dh-so-chip">{_e(k)}: <b>{_e(v)}</b></span>' for k, v in (d.get("params") or []))
    st.markdown(
        '<div class="dh-so-banner"><div class="dh-so-eyebrow">HASIL RESMI ONE-SYSTEM BLUEPRINT</div>'
        f'<div class="dh-so-title">{_ICON[name]} ONE-SYSTEM BLUEPRINT: {_e(name.upper())}</div>'
        f'<div class="dh-so-bsub"><b>{_e(d.get("title", ""))}</b> · Untuk: {_e(nama)}</div>'
        + (f'<div class="dh-so-quote">&ldquo;{_e(quote)}&rdquo;</div>' if quote else "") + '</div>'
        + (f'<div class="dh-so-chips">{chips}</div>' if chips else ""), unsafe_allow_html=True)
    _tg = (st.session_state.get("dh_solo_prof") or {}).get("tgl")
    if st.session_state.get("dh_solo_free"):
        st.markdown('<div class="dh-so-note ok">✓ Hasil ini sudah kamu beli sebelumnya, jadi dibuka gratis.</div>', unsafe_allow_html=True)
    if _tg:
        life_chart.strip(nama, _tg)
    raw = res.get("raw")
    secs = {i: (texts or []) for i, (_ic, _t, texts, _tone) in enumerate(d["sections"])}
    cap = f"One-System Blueprint {name}: {nama}\nCek takdirmu di destinyreveal.id #DestinyReveal"
    if quote:
        cap = f'"{quote}"\n\n' + cap
    # dashboard atas: kartu visual (assets/cards) + radar/bar skor ASLI (hanya sistem kuesioner)
    panel = RK.dashboard(name, raw)
    has_card = RK.has_card(name, raw)
    if has_card and panel:
        c1, c2 = st.columns([1, 1.15], gap="medium")
        with c1:
            RK.card_visual(name, raw, nama, cap, "dhsorc")
        with c2:
            st.markdown(panel, unsafe_allow_html=True)
    elif has_card:
        RK.card_visual(name, raw, nama, cap, "dhsorc")
    elif panel:
        st.markdown(panel, unsafe_allow_html=True)
    if name in life_chart.SYSTEMS and _tg:  # dashboard visual: Roda Takdir / grafik usia 20-60
        st.markdown('<div class="rk-ph" style="margin:14px 0 8px">🧭 PETA SIKLUS HIDUPMU</div>', unsafe_allow_html=True)
        life_chart.render(name, _tg, height=700 if name == "Matrix Destiny" else 560)
    pdf_secs = [(_ASPEK[i], [t for t in secs.get(i, []) if t] or [_EMPTY]) for i in range(len(_ASPEK))]
    combo = build_combo(name, raw) if raw else []
    if combo:
        pdf_secs.append(("COMBO: KETIKA VARIABEL-VARIABELMU BERTEMU", [f'{b["title"]}: {b["text"]}' for b in combo]))
    heading_with_info('<div class="dh-so-h3">Analisis 6 Aspek</div>', "solo_res", "AF")
    plain = [f"ONE-SYSTEM BLUEPRINT: {name} · {nama}", d.get("title", ""), ""]
    items = []
    for i, title in enumerate(_ASPEK):
        texts = [t for t in secs.get(i, []) if t]
        items.append((_ASPEK_ICON[i], title, texts or [_EMPTY]))
        plain += [title, *texts, ""]
    st.markdown(RK.insight_cards(items), unsafe_allow_html=True)
    render_combo_card(name, combo)  # kartu combo di paling bawah analisis, sebelum tombol aksi
    if combo:
        plain += ["COMBO: KETIKA VARIABEL-VARIABELMU BERTEMU", ""]
        for b in combo:
            plain += [b["title"], b["text"], ""]
    with st.container(key="dhso_acts"):
        a1, a2 = st.columns(2, gap="small")
        with a1:
            st.download_button("Download PDF", make_pdf(f"One-System Blueprint - {name}", f'{d.get("title", "")} - Untuk: {nama}', pdf_secs),
                               file_name=f"solo-reveal-{name.lower().replace(' ', '-')}.pdf", mime="application/pdf",
                               key="dhso_pdf", use_container_width=True, on_click="ignore", icon=":material/download:")
        with a2:
            copy_button("\n".join(plain).strip(), "📋 Salin Teks", "dhso_copy", fs=13, h=44)
        b1, b2 = st.columns(2, gap="small")
        with b1:
            st.button(f"🔄 Sistem Lain ({SOLO_PRICE}✨)", key="dhso_again", on_click=_cb_again, use_container_width=True)
        with b2:
            st.button("Tutup", key="dhso_done", type="primary", use_container_width=True,
                      on_click=cc.cb_ask, args=("solo",))


@st.dialog("One-System Blueprint", width="large", on_dismiss=_cb_close)
def solo_dialog():
    ss = st.session_state
    step = ss.get("dh_solo_step", "select")
    if step == "result" and ss.get("dh_solo_res"):
        cc.wrap("solo", _render_result, leave=_cb_again, icon="🧭", title="Yakin Mau Tutup Hasil One-System Blueprint?",
                      text="Analisis 6 aspekmu aman tersimpan. Kamu bisa membukanya lagi GRATIS kapan saja: pilih sistem yang sama "
                           "dengan data diri yang sama.",
                      tip="Download PDF atau salin analisis kalau mau dibaca tanpa membuka aplikasi.",
                      stay="✨ Lanjut Baca", go="Ya, Tutup Hasil")
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


def _reset_resume():
    st.session_state.pop("dh_solo_qi", None)
    _cb_again()


_resume.register("solo", _reset_resume)
DIALOGS = {"solo": open_solo}
