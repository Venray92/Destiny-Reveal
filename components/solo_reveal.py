"""
Solo Reveal (UI23): pilih 1 dari 15 sistem -> (kuesioner, khusus 5 sistem psikologi) -> bayar 150 SD -> hasil A-F.
Satu st.dialog, langkah ganti-ganti lewat on_click callback (dialog tetap kebuka).
State (session_state): dh_solo_step | dh_solo_sys | dh_solo_prof | dh_solo_ans | dh_solo_res
DUMMY: Stardust dipotong di session saja (belum ada backend/DB).
"""

import html
from datetime import date
from urllib.parse import quote as urlquote

import streamlit as st

from components import auth
from components.dialog_bus import request_open, request_with_return
from utils.simple_pdf import make_pdf
from components.modal_detail import build_detail, copy_button
from content.questionnaires.big_five_soal import BIG_FIVE_QUESTIONS
from content.questionnaires.disc_soal import DISC_QUESTIONS
from content.questionnaires.enneagram_soal import ENNEAGRAM_QUESTIONS
from content.questionnaires.love_language_soal import LOVE_LANGUAGE_QUESTIONS
from content.questionnaires.mbti_soal import MBTI_QUESTIONS
from content.result_builder import compute_quiz_raw_result, compute_raw_result

SOLO_PRICE = 150  # Stardust

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


ACTIVE = ("Zodiak", "Shio", "Weton", "Numerologi", "Matrix Destiny")  # sistem yang sudah jalan


def _cb_pick(name):
    ss = st.session_state
    ss.dh_solo_sys = name
    if name not in ACTIVE:  # 10 sistem lain masih dikembangkan -> info, tanpa potong Stardust
        ss.dh_solo_err = None
        _go("dev")


def _cb_dev_ok():
    ss = st.session_state
    ss.pop("dh_solo_sys", None)
    _go("select")


def _cb_to_next():
    """Dari pilih sistem: validasi data diri -> kuesioner (sistem psikologi) atau bayar."""
    ss = st.session_state
    name = ss.get("dh_solo_sys")
    if name and name not in ACTIVE:
        _go("dev")
        return
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
    if name in ("Zi Wei", "Human Design") and not prof.get("jam"):
        ss.dh_solo_err = f"{name} butuh Jam Lahir. Isi Jam Lahir dulu ya."
        return
    if name == "Golongan Darah" and prof.get("golda") in ("", "Belum tahu"):
        ss.dh_solo_err = "Golongan Darah butuh pilihan golongan darahmu (A/B/AB/O)."
        return
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


def _cb_pay():
    ss = st.session_state
    u = auth.current_user()
    if not u or u.get("koin", 0) < SOLO_PRICE:
        return
    name, prof = ss.dh_solo_sys, ss.dh_solo_prof
    if _KIND[name] == "quiz":
        raw = compute_quiz_raw_result(name, ss.get("dh_solo_ans") or {})
    else:
        raw = compute_raw_result(name, {
            "tanggal_lahir": prof["tgl"], "jam_lahir": prof.get("jam"), "kota_lahir": prof.get("kota"),
            "golongan_darah": prof.get("golda"), "nama_lengkap": prof["nama"]})
    detail = build_detail(name, raw)
    if not detail:
        ss.dh_solo_err = "Hasil sistem ini belum bisa dihitung untuk datamu (mis. tahun lahir di luar jangkauan). Saldo tidak dipotong."
        return
    u["koin"] -= SOLO_PRICE
    ss.dh_solo_res = {"system": name, "detail": detail, "nama": prof["nama"]}
    ss.dh_solo_err = None
    _go("result")


def _cb_again():
    ss = st.session_state
    for k in ("dh_solo_res", "dh_solo_ans", "dh_solo_sys"):
        ss.pop(k, None)
    _go("select")


def _cb_close():
    """X / Selesai & Tutup di layar hasil -> reset, klik Solo Reveal berikutnya mulai dari pilih sistem."""
    ss = st.session_state
    if ss.get("dh_solo_step") == "result":
        _cb_again()


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
    st.markdown('<div class="dh-so-sec2"><span>📅 DATA DIRI</span><em>Wajib</em></div>', unsafe_allow_html=True)
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
        '<div class="dh-so-head"><span class="dh-so-ico">🎯</span><div><div class="dh-so-brand">SOLO REVEAL</div>'
        f'<div class="dh-so-hsub">{sub} · 💰 {SOLO_PRICE} Stardust</div></div></div><div class="dh-so-line"></div>',
        unsafe_allow_html=True)


def _render_select():
    ss = st.session_state
    u = auth.current_user()
    prof = _profile()
    _head()
    st.markdown(f'<div class="dh-so-h2">Pilih Sistem<span class="dh-so-pill">Biaya: {SOLO_PRICE} Stardust</span></div>',
                unsafe_allow_html=True)
    if prof:
        tgl = prof["tgl"].strftime("%Y-%m-%d") if hasattr(prof["tgl"], "strftime") else str(prof["tgl"])
        st.markdown(
            f'<div class="dh-so-sub">Pilih 1 sistem yang mau kamu analisis secara mendalam (6 aspek A-F) untuk '
            f'{_e(prof["nama"])}.</div>'
            f'<div class="dh-so-prof"><span><i></i><b>{_e(prof["nama"])}</b> · {tgl}</span>'
            f'<span class="dh-so-bal">Saldo: ✨ {_saldo()} SD</span></div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="dh-so-sub">Pilih 1 sistem yang mau kamu analisis secara mendalam (6 aspek A-F). '
                    + ('Lengkapi data dirimu dulu.' if u else 'Isi data dirimu (atau masuk akun supaya data terisi otomatis).')
                    + '</div>', unsafe_allow_html=True)
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
    label = f"Lanjutkan ke Pembayaran ({SOLO_PRICE}✨) →" if picked and _KIND[picked] != "quiz" else (
        f"Lanjut: Isi Kuesioner {picked} →" if picked else f"Lanjutkan ke Pembayaran ({SOLO_PRICE}✨) →")
    with st.container(key="dhso_cta"):
        st.button(label, key="dhso_next", type="primary", use_container_width=True, on_click=_cb_to_next)


# ─────────────── info: sistem belum tersedia ───────────────
def _render_dev():
    name = st.session_state.dh_solo_sys
    _head()
    st.markdown(
        '<div class="dh-so-dev"><div class="dh-so-devico">🚧</div><div class="dh-so-devh">Fitur Dalam Tahap Pengembangan</div>'
        f'<p>Sistem <b>{_e(name)}</b> saat ini masih dalam tahap pengembangan dan akan segera hadir. Silakan pilih sistem '
        'lain yang sudah tersedia (Zodiak, Shio, Weton, Numerologi, atau Matrix Destiny) untuk melanjutkan analisis.</p>'
        '<div class="dh-so-devnote">Stardust kamu tidak dipotong.</div></div>', unsafe_allow_html=True)
    with st.container(key="dhso_cta"):
        st.button("Pilih Sistem Lain", key="dhso_dev_ok", type="primary", use_container_width=True, on_click=_cb_dev_ok)


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
            st.button(f"Lanjutkan ke Pembayaran ({SOLO_PRICE}✨) →", key="dhso_q_next", type="primary",
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
        f'<div class="dh-so-row"><span>Harga Fitur:</span><b class="dh-so-acc">💰 {SOLO_PRICE} Stardust</b></div>'
        f'<div class="dh-so-row"><span>Saldo Stardust Kamu:</span><b>⭐ {saldo} Stardust</b></div>'
        f'<div class="dh-so-row dh-so-last"><span>Sisa Saldo Setelah Bayar:</span><b class="dh-so-big">⭐ {max(sisa, 0) if u else 0} Stardust</b></div>'
        '</div>', unsafe_allow_html=True)
    if not u:
        st.markdown('<div class="dh-so-note bad">🔒 Kamu belum masuk akun. Masuk dulu supaya Saldo Stardust bisa dipakai '
                    '(akun baru dapat bonus Stardust).</div>', unsafe_allow_html=True)
    elif sisa < 0:
        st.markdown(f'<div class="dh-so-note bad">Saldo belum cukup, kurang {-sisa} Stardust. Top-up dulu ya.</div>',
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
                if st.button("Top-up Stardust →", key="dhso_p_topup", type="primary", use_container_width=True):
                    request_with_return("pricing_keep", "solo", dh_pr_tab="koin")
            else:
                st.button(f"Bayar {SOLO_PRICE} Stardust →", key="dhso_p_pay", type="primary",
                          use_container_width=True, on_click=_cb_pay)


# ─────────────── langkah 3: hasil A-F ───────────────
def _render_result():
    res = st.session_state.get("dh_solo_res")
    if not res:
        _go("select")
        return _render_select()
    d, name, nama = res["detail"], res["system"], res["nama"]
    st.markdown('<div class="dh-step dh-step-solo"></div><div class="dh-nodismiss"></div>'
                '<div class="dh-so-head"><span class="dh-so-ico">🎯</span><div><div class="dh-so-brand">SOLO REVEAL</div>'
                f'<div class="dh-so-hsub">Pilih 1 sistem, dapat analisis lengkap A-F · 💰 {SOLO_PRICE} Stardust</div></div></div>'
                '<div class="dh-so-line"></div>', unsafe_allow_html=True)
    quote = d.get("quote") or ""
    chips = "".join(f'<span class="dh-so-chip">{_e(k)}: <b>{_e(v)}</b></span>' for k, v in (d.get("params") or []))
    st.markdown(
        '<div class="dh-so-banner"><div class="dh-so-eyebrow">HASIL RESMI SOLO REVEAL</div>'
        f'<div class="dh-so-title">{_ICON[name]} SOLO REVEAL: {_e(name.upper())}</div>'
        f'<div class="dh-so-bsub"><b>{_e(d.get("title", ""))}</b> · Untuk: {_e(nama)}</div>'
        + (f'<div class="dh-so-quote">&ldquo;{_e(quote)}&rdquo;</div>' if quote else "") + '</div>'
        + (f'<div class="dh-so-chips">{chips}</div>' if chips else ""), unsafe_allow_html=True)
    secs = {i: (texts or []) for i, (_ic, _t, texts, _tone) in enumerate(d["sections"])}
    pdf_secs = [(_ASPEK[i], [t for t in secs.get(i, []) if t] or [_EMPTY]) for i in range(len(_ASPEK))]
    st.download_button("📥 Download PDF", make_pdf(f"Solo Reveal - {name}", f'{d.get("title", "")} - Untuk: {nama}', pdf_secs),
                       file_name=f"solo-reveal-{name.lower().replace(' ', '-')}.pdf", mime="application/pdf",
                       key="dhso_pdf", use_container_width=True, on_click="ignore")
    plain = [f"SOLO REVEAL: {name} · {nama}", d.get("title", ""), ""]
    for i, title in enumerate(_ASPEK):
        texts = [t for t in secs.get(i, []) if t]
        body = "".join(f"<p>{_e(t)}</p>" for t in texts) or f'<p class="dh-so-empty">{_EMPTY}</p>'
        st.markdown(f'<div class="dh-so-card"><div class="dh-so-ct"><span>{_ASPEK_ICON[i]}</span>{_e(title)}</div>{body}</div>',
                    unsafe_allow_html=True)
        plain += [title, *texts, ""]
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
            if st.button("Selesai & Tutup", key="dhso_done", type="primary", use_container_width=True):
                _cb_again()
                st.rerun()  # rerun penuh = dialog nutup


@st.dialog("Solo Reveal", width="large", on_dismiss=_cb_close)
def solo_dialog():
    ss = st.session_state
    step = ss.get("dh_solo_step", "select")
    if step == "result" and ss.get("dh_solo_res"):
        _render_result()
    elif step == "dev" and ss.get("dh_solo_sys"):
        _render_dev()
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
