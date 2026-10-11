"""
Layar kuesioner bersama (Solo, Career DNA, Strength, Blueprint).
1 soal per layar, pilih jawaban = otomatis lanjut. Footer: Kembali / Selanjutnya (untuk cek ulang) / Selesaikan.
Selesaikan dengan soal kosong -> popup "Pengisian Belum Lengkap" (layer di atas modal).
"""

import html

import streamlit as st

from components import close_confirm as cc

_ICON = {"MBTI": "🧠", "Enneagram": "🔢", "Big Five": "🌊", "DISC": "🎯", "Love Language": "💞"}
_Q_DEFAULT = "Mana yang lebih sesuai buat kamu?"
INC_TITLE = "Pengisian Belum Lengkap"
INC_TEXT = "Mohon jawab seluruh pertanyaan sebelum melanjutkan untuk mendapatkan hasil analisis yang akurat."


def options(s, q, scale):
    """Daftar (nilai, label) per tipe soal."""
    if s in ("MBTI", "Enneagram"):
        return [(True, "👍 Setuju"), (False, "👎 Tidak Setuju")]
    if s == "Big Five":
        return [(v, f"{v}  ·  {scale[v]}") for v in (5, 4, 3, 2, 1)]
    if s == "DISC":
        return [(L, q["options"][L]) for L in "ABCD"]
    return [(L, f"**{L}.** {q[L]['text']}") for L in "AB"]


def _qtext(s, q):
    if s in ("MBTI", "Enneagram", "Big Five"):
        return html.escape(q["text"])
    if s == "DISC":
        return "Pilih kata yang <b>paling</b> menggambarkan dirimu:"
    return _Q_DEFAULT


def _cb_pick(put, s, qid, val, qi_key=None, last=True):
    """Pilih jawaban -> langsung lanjut ke soal berikutnya (soal terakhir tetap menunggu Selesaikan)."""
    put(s, qid, val)
    if qi_key and not last:
        st.session_state[qi_key] = st.session_state.get(qi_key, 0) + 1


def _cb_move(qi_key, d):
    st.session_state[qi_key] = max(0, st.session_state.get(qi_key, 0) + d)


def _cb_back(qi_key, on_exit):
    if st.session_state.get(qi_key, 0) > 0:
        st.session_state[qi_key] -= 1
    else:
        on_exit()


def _first_missing(items, get):
    for i, it in enumerate(items):
        if get(it["sys"], it["q"]["id"]) is None:
            return i
    return None


def _cb_finish(prefix, qi_key, items, get, on_done):
    ss = st.session_state
    miss = _first_missing(items, get)
    if miss is not None:
        ss[f"{prefix}_inc"] = True
        return
    ss.pop(f"{prefix}_inc", None)
    on_done()


def _cb_fix(prefix, qi_key, items, get):
    ss = st.session_state
    ss.pop(f"{prefix}_inc", None)
    miss = _first_missing(items, get)
    if miss is not None:
        ss[qi_key] = miss


def _screen(prefix, items, get, put, qi_key, title, who, on_exit, on_done, scale):
    ss = st.session_state
    e = html.escape
    n = len(items)
    qi = min(max(ss.get(qi_key, 0), 0), n - 1)
    ss[qi_key] = qi
    s, q = items[qi]["sys"], items[qi]["q"]
    name, meta = who
    ini = e((name or "?").strip()[:1].upper() or "?")
    done = sum(1 for it in items if get(it["sys"], it["q"]["id"]) is not None)
    st.markdown(
        '<div class="dh-step dh-step-quiz"></div><div class="dh-nodismiss"></div>'
        f'<div class="dh-qz-who"><span class="dh-qz-av">{ini}</span>'
        f'<div><b>{e(name or "Kamu")}</b><small>{e(meta or "")}</small></div></div>'
        f'<div class="dh-qz-scr"><span>{e(title)} - {n} Soal</span><em>{done}/{n} terjawab</em></div>'
        f'<div class="dh-qz-pt"><b>Pertanyaan {qi + 1} dari {n}</b><span>{_ICON.get(s, "✨")} {e(s)}</span></div>'
        f'<div class="dh-bp-prog"><i style="width:{round((qi + 1) / n * 100)}%"></i></div>',
        unsafe_allow_html=True)
    cur = get(s, q["id"])
    last = qi >= n - 1
    with st.container(key=f"dhbp_slide_{prefix}{qi}"):
        st.markdown(f'<div class="dh-qz-q">{_qtext(s, q)}</div>', unsafe_allow_html=True)
        with st.container(key="dhbp_opts"):
            ops = options(s, q, scale)
            if s in ("MBTI", "Enneagram"):
                cols = st.columns(2, gap="small")
                for col, (v, lb) in zip(cols, ops):
                    with col:
                        st.button(lb, key=f"{prefix}_a_{qi}_{int(v)}", on_click=_cb_pick, args=(put, s, q["id"], v, qi_key, last),
                                  type="primary" if cur is not None and cur == v else "secondary", use_container_width=True)
            else:
                for v, lb in ops:
                    st.button(lb, key=f"{prefix}_a_{qi}_{v}", on_click=_cb_pick, args=(put, s, q["id"], v, qi_key, last),
                              type="primary" if cur is not None and cur == v else "secondary", use_container_width=True)
    with st.container(key=f"{prefix}_qfoot"):
        c1, c2 = st.columns(2, gap="small")
        with c1:
            st.button("Kembali", key=f"{prefix}_qback", on_click=_cb_back, args=(qi_key, on_exit), use_container_width=True)
        with c2:
            if last:
                st.button("Selesaikan", key=f"{prefix}_qfin", type="primary", on_click=_cb_finish,
                          args=(prefix, qi_key, items, get, on_done), use_container_width=True)
            else:
                st.button("Selanjutnya", key=f"{prefix}_qnext", type="primary", on_click=_cb_move,
                          args=(qi_key, 1), use_container_width=True, disabled=cur is None)


def render(prefix, items, get, put, qi_key, title, who, on_exit, on_done, scale=None):
    """items = [{"sys","q"}]; get(sys, qid) -> nilai/None; put(sys, qid, val).
    title = 'Kuesioner Enneagram'; who = (nama, meta). on_exit = Kembali di soal 1; on_done = semua terjawab."""
    scale = scale or {}
    args = (prefix, items, get, put, qi_key, title, who, on_exit, on_done, scale)
    if st.session_state.get(f"{prefix}_inc"):
        cc.layer(f"{prefix}inc", lambda: _screen(*args), on_go=_cb_fix, icon="📝", title=INC_TITLE, text=INC_TEXT,
                 stay=None, go="Lengkapi Sekarang", go_args=(prefix, qi_key, items, get))
    else:
        with cc.bg(f"{prefix}inc"):
            _screen(*args)
