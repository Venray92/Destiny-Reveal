"""
Langkah 2-5 alur modal Reveal Mode 1 (lihat components/flow_state.py):
verify (email + referral) -> pay (paket & pembayaran) -> loading -> result.
Semua transisi lewat on_click callback (dialog tetap kebuka).
DUMMY: magic link, validasi kode referral, dan pembayaran belum ada backend.
"""

import time

import streamlit as st

from components import auth
from components.flow_state import (
    MODE1_PRICE_BASE, REFERRAL_BONUS_COIN, REFERRAL_DISCOUNT, STEP_LOADING, STEP_PAY,
    STEP_RESULT, STEP_VERIFY, price_now, reset_for_new_scan, rp, set_step, valid_email,
)
from content.profile_loader import ALLOW_LEGACY_FALLBACK, get_profile
from content.result_builder import build_display_data, compute_raw_result
from components.modal_detail import cb_open_detail
from utils.date_format import format_tanggal_lengkap


# ── Header + tab langkah (dipakai step verify & pay) ─────────────
def _head(active):
    done = active == 2
    t1 = f'<div class="dh-vtab {"done" if done else "on"}">{"✓" if done else "1."} Verifikasi Email &amp; Referral</div>'
    t2 = f'<div class="dh-vtab {"on" if done else ""}">2. Paket &amp; Pembayaran</div>'
    st.markdown(
        f'<div class="dh-step dh-step-{"pay" if done else "verify"}"></div>'
        '<div class="dh-modal-head">'
        '<div class="dh-modal-eyebrow">LANGKAH TERAKHIR · VERIFIKASI &amp; AKTIVASI</div>'
        '<div class="dh-modal-title">Buka Cetak Biru Takdirmu</div>'
        '<div class="dh-modal-sub">Hasil jawaban akan terbuka setelah verifikasi email dan konfirmasi '
        'pembayaran. Akunmu otomatis terbuat.</div></div>'
        f'<div class="dh-vtabs">{t1}{t2}</div>',
        unsafe_allow_html=True,
    )


# ══════════════════ LANGKAH 1: VERIFIKASI EMAIL & REFERRAL ══════════════════
def _cb_send_link():
    email = (st.session_state.get("dhv_email") or "").strip()
    if not valid_email(email):
        st.session_state.dh_verify_error = "Format email belum valid, contoh: nama@email.com"
        st.session_state.dh_email_sent = False
        return
    st.session_state.dh_verify_error = None
    st.session_state.dh_email = email
    st.session_state.dh_email_sent = True  # DUMMY: belum ada pengiriman email beneran


def _cb_verify():
    auth.ensure_user(st.session_state.get("dh_email", ""))  # akun otomatis dibuat (250 SD bonus)
    st.session_state.dh_email_verified = True
    set_step(STEP_PAY)


def _cb_apply_ref():
    code = (st.session_state.get("dhv_ref") or "").strip().upper()
    if not code:
        st.session_state.dh_ref_error = "Masukkan kode referral dulu ya."
        return
    st.session_state.dh_ref_error = None
    st.session_state.dh_ref_code = code  # DUMMY: semua kode dianggap valid
    st.session_state.dh_ref_applied = True


def render_verify():
    _head(1)
    ss = st.session_state
    with st.container(key="dhv_card_email"):
        st.markdown('<div class="dh-modal-section"><span>✉️ 1. MASUKKAN &amp; VERIFIKASI EMAIL</span>'
                    '<em>Wajib</em></div>'
                    '<div class="dh-flabel">Alamat Email (Untuk Pengiriman Magic Link &amp; Pembuatan Akun Otomatis)</div>',
                    unsafe_allow_html=True)
        c1, c2 = st.columns([4, 1.3], gap="small", vertical_alignment="center")
        with c1:
            st.text_input("Alamat Email", placeholder="contoh: nama@email.com", key="dhv_email",
                          label_visibility="collapsed")
        with c2:
            st.button("Kirim Ulang" if ss.get("dh_email_sent") else "Kirim Magic Link",
                      key="dhv_send", on_click=_cb_send_link, use_container_width=True)
        st.markdown('<div class="dh-fhint">Bebas repot: Tidak perlu mengingat password. '
                    'Link masuk instan akan dikirim ke emailmu.</div>', unsafe_allow_html=True)
        if ss.get("dh_verify_error"):
            st.error(ss.dh_verify_error)
        if ss.get("dh_email_sent"):
            with st.container(key="dhv_sentbox"):
                st.markdown(
                    f'<div class="dh-sent-top"><span>Magic link terkirim ke <b>{ss.dh_email}</b>!</span>'
                    '<em>Siap Diverifikasi</em></div>'
                    '<div class="dh-fhint">Klik tombol di bawah ini untuk mengonfirmasi verifikasi email '
                    'dan melanjutkan ke pemilihan paket &amp; pembayaran:</div>',
                    unsafe_allow_html=True,
                )
                st.button("✓ Verifikasi Email & Lanjut ke Pembayaran →", key="dhv_go_pay",
                          on_click=_cb_verify, use_container_width=True)

    with st.container(key="dhv_card_ref"):
        st.markdown('<div class="dh-modal-section"><span>🎁 PUNYA KODE REFERRAL / KUPON?</span>'
                    '<i class="dh-opt">Opsional</i></div>'
                    '<div class="dh-fhint">Masukkan kode referral teman atau kode promosi untuk mendapatkan '
                    'diskon biaya dan bonus Stardust.</div>', unsafe_allow_html=True)
        r1, r2 = st.columns([4, 1.3], gap="small", vertical_alignment="center")
        with r1:
            st.text_input("Kode Referral", placeholder="MASUKKAN KODE REFERRAL (CTH: DESTINY2026)",
                          key="dhv_ref", label_visibility="collapsed")
        with r2:
            st.button("Terapkan", key="dhv_apply", on_click=_cb_apply_ref, use_container_width=True)
        if ss.get("dh_ref_error"):
            st.error(ss.dh_ref_error)
        if ss.get("dh_ref_applied"):
            st.markdown(
                f'<div class="dh-okbox">✓ Kode referral "{ss.dh_ref_code}" aktif! '
                f'Diskon {int(REFERRAL_DISCOUNT * 100)}% &amp; bonus {REFERRAL_BONUS_COIN} SD diterapkan.</div>',
                unsafe_allow_html=True,
            )
    st.markdown('<div class="dh-lockbox">🔒 Paket terpilih (Mode 1: 5 Kelahiran) dan metode pembayaran '
                'akan otomatis ditampilkan segera setelah kamu memverifikasi email di atas.</div>',
                unsafe_allow_html=True)


# ══════════════════ LANGKAH 2: PAKET & PEMBAYARAN ══════════════════
PAY_METHODS = [
    ("koin", "✨", "Saldo Stardust", "200 SD"),
    ("gopay", "📱", "GoPay", "Instan"),
    ("qris", "⬛", "QRIS", "Semua Bank"),
    ("ovo", "💜", "OVO / DANA", "E-Wallet"),
]


def _cb_pick_pay(key):
    st.session_state.dh_pay_method = key


def _cb_change_email():
    st.session_state.dhv_email = st.session_state.get("dh_email", "")
    st.session_state.dh_email_verified = False
    set_step(STEP_VERIFY)


def _cb_pay():
    # DUMMY: belum ada payment gateway -> langsung dianggap sukses
    st.session_state.pop("dh_flow_result", None)
    set_step(STEP_LOADING)


def render_pay():
    _head(2)
    ss = st.session_state
    data = ss.get("dh_modal_data") or {}
    method = ss.get("dh_pay_method", "gopay")
    price = price_now()
    ref_line = (f'<div class="dh-vref">🎁 Referral Aktif: {ss.dh_ref_code} '
                f'(Diskon {int(REFERRAL_DISCOUNT * 100)}% &amp; +{REFERRAL_BONUS_COIN} SD)</div>'
                if ss.get("dh_ref_applied") else "")
    strike = f'<s>{rp(MODE1_PRICE_BASE)}</s>' if ss.get("dh_ref_applied") else ""

    with st.container(key="dhp_verified"):
        a, b = st.columns([5, 1], vertical_alignment="center")
        with a:
            st.markdown(f'<div class="dh-vtitle">✓ Email Terverifikasi</div>'
                        f'<div class="dh-vmail">{ss.get("dh_email", "")}</div>{ref_line}', unsafe_allow_html=True)
        with b:
            st.button("Ubah Email", key="dhp_change", on_click=_cb_change_email)

    st.markdown(
        '<div class="dh-pkg"><div class="dh-pkg-row"><div>'
        '<div class="dh-pkg-label">PAKET TERPILIH:</div>'
        '<div class="dh-pkg-title">Mode 1: 5 Kelahiran</div>'
        '<div class="dh-pkg-sub">Zodiak, Shio, Weton, Numerologi, Matrix Destiny</div></div>'
        f'<div class="dh-pkg-price">{strike}<b>{rp(price)}</b><span>atau 200 SD</span></div></div>'
        f'<div class="dh-pkg-foot"><span>Profil: <b>{(data.get("nama") or "").upper()}</b></span>'
        '<span>Format: Cetak Biru Interaktif + Akun</span></div></div>',
        unsafe_allow_html=True,
    )

    with st.container(key="dhp_methods"):
        st.markdown('<div class="dh-modal-section"><span>💳 PILIH METODE PEMBAYARAN</span></div>',
                    unsafe_allow_html=True)
        cols = st.columns(4, gap="small")
        for col, (key, icon, name, sub) in zip(cols, PAY_METHODS):
            with col:
                with st.container(key=f"dhpay_m_{key}"):
                    st.markdown(f'<div class="dh-pm{" dh-pm-sel" if key == method else ""}">'
                                f'<div class="dh-pm-ico">{icon}</div><div class="dh-pm-name">{name}</div>'
                                f'<div class="dh-pm-sub">{sub}</div></div>', unsafe_allow_html=True)
                    st.button(f"Bayar pakai {name}", key=f"dhpay_pick_{key}", on_click=_cb_pick_pay, args=(key,))
        st.markdown(f'<div class="dh-pay-total"><span>Total Pembayaran: <b>{rp(price)}</b></span>'
                    '<span class="dh-safe">🛡️ Garansi Privasi Aman</span></div>', unsafe_allow_html=True)

    st.button(f"Bayar {rp(price)} & Buka Hasil Sekarang →", key="dhp_pay", type="primary",
              use_container_width=True, on_click=_cb_pay)
    st.markdown('<div class="dh-fhint" style="text-align:center;">Setelah pembayaran berhasil, halaman '
                'Cetak Biru Takdir Berhasil Terungkap akan terbuka dan otomatis tersimpan di akunmu.</div>',
                unsafe_allow_html=True)


# ══════════════════ LANGKAH 3: LOADING ══════════════════
MODE1_SYSTEMS = [
    ("Zodiak", "01. ZODIAK BARAT"), ("Shio", "02. SHIO LUNAR"), ("Weton", "03. WETON JAWA"),
    ("Numerologi", "04. NUMEROLOGI PYTHAGORAS"), ("Matrix Destiny", "05. MATRIX DESTINY"),
]


def _first_sentence(text, limit=170):
    text = (text or "").strip()
    cut = text.find(". ")
    out = text if cut == -1 else text[: cut + 1]
    return out if len(out) <= limit else out[: limit - 1].rstrip() + "…"


def _tag_and_short(system, raw):
    """(tag kecil di kanan atas kartu, nama pendek buat tombol kartu)."""
    if system == "Zodiak":
        return raw.get("ruling_planet", ""), raw.get("sign", "Zodiak")
    if system == "Shio":
        return f'Elemen {raw.get("elemen", "")}', f'Shio {raw.get("shio", "")}'
    if system == "Weton":
        return f'Neptu {raw.get("neptu", "")}', f'Weton {raw.get("hari", "")} {raw.get("pasaran", "")}'
    if system == "Numerologi":
        return f'Life Path #{raw.get("life_path", "")}', f'Life Path {raw.get("life_path", "")}'
    return f'Arcana #{raw.get("titik_inti", "")}', raw.get("nama_arketipe", "Matrix Destiny")


def compute_mode1(nama, tgl):
    """Hitung 5 sistem Mode 1 dari engine + kamus konten (content/result_builder.py)."""
    ld = {"tanggal_lahir": tgl, "nama_lengkap": nama}
    out = []
    for system, label in MODE1_SYSTEMS:
        raw = compute_raw_result(system, ld)
        disp = build_display_data(system, raw)
        prof = get_profile(system, raw)  # teks dari JSON baru; kamus lama cuma cadangan (judul + entri yang belum ada)
        tag, short = _tag_and_short(system, raw) if disp else ("", system)
        free = (prof or {}).get("free", {})
        lama = disp if (disp and ALLOW_LEGACY_FALLBACK) else {}
        out.append({
            "system": system, "label": label, "raw": raw, "tag": tag, "short": short,
            "title": disp["title"] if disp else "Belum bisa dihitung",
            "desc": _first_sentence(free.get("siapa_kamu") or lama.get("p1", "")) if disp
            else "Tahun lahir ini di luar jangkauan data sistem ini.",
            "quote": (free.get("quote") or lama.get("quote", "")) if disp else "",
        })
    return out


def render_loading():
    data = st.session_state.get("dh_modal_data") or {}
    st.markdown(
        '<div class="dh-step dh-step-loading"></div><div class="dh-loading">'
        '<div class="dh-spin"><span>✦</span></div>'
        '<div class="dh-loading-title">Menyelaraskan Mode 1: 5 Kelahiran...</div>'
        '<div class="dh-loading-sub">Memproses peta takdir dan membuat akun personalmu.</div></div>',
        unsafe_allow_html=True,
    )
    st.session_state.dh_flow_result = compute_mode1(data.get("nama", ""), data.get("tgl_lahir"))
    auth.add_history(data.get("nama", ""), data.get("tgl_lahir"), st.session_state.dh_flow_result)
    time.sleep(2.5)
    set_step(STEP_RESULT)
    st.rerun(scope="fragment")


# ══════════════════ LANGKAH 4: HASIL ══════════════════
def _cb_toggle_summary():
    st.session_state.dh_show_summary = not st.session_state.get("dh_show_summary")


def _cb_soon(msg):
    st.toast(msg)


def _summary_text(nama, tgl, results):
    lines = [f"Peta Jiwa: {nama}", f"Mode 1: 5 Kelahiran · Lahir {format_tanggal_lengkap(tgl)}", ""]
    for r in results:
        lines.append(f'{r["label"]}: {r["title"]}')
    return "\n".join(lines)


def render_result():
    ss = st.session_state
    data = ss.get("dh_modal_data") or {}
    results = ss.get("dh_flow_result") or []
    nama, tgl = data.get("nama", ""), data.get("tgl_lahir")
    jam = f' · {data["jam_lahir"]} WIB' if data.get("jam_lahir") else ""
    email = ss.get("dh_email", "")

    # kolom ke-4 kosong = ruang buat tombol X dialog (X di kanan tombol Salin Ringkasan)
    h1, h2, h3, _x = st.columns([3.1, 1, 1.4, 0.32], gap="small", vertical_alignment="top")
    with h1:
        st.markdown(
            '<div class="dh-step dh-step-result"></div>'
            '<div class="dh-res-badge">✓ CETAK BIRU TAKDIR BERHASIL TERUNGKAP</div>'
            f'<div class="dh-res-title">Peta Jiwa: {nama}</div>'
            f'<div class="dh-res-info"><b>Mode 1: 5 Kelahiran</b> · Lahir: {format_tanggal_lengkap(tgl)}{jam}'
            f' · Tersimpan di Akun ({email})</div>', unsafe_allow_html=True)
    with h2:
        if st.button("Buka Akunku", key="dhr_account", use_container_width=True):
            ss.dh_open_profile = True
            st.rerun()  # rerun penuh: modal hasil nutup, profil kebuka
    with h3:
        st.button("Salin Ringkasan", key="dhr_copy", type="primary", on_click=_cb_toggle_summary,
                  use_container_width=True, icon=":material/share:")
    if ss.get("dh_show_summary"):
        st.code(_summary_text(nama, tgl, results), language=None)

    st.markdown('<div class="dh-res-hint">✨ Ketuk tombol <b>"Lihat &amp; Simpan Kartu Takdir"</b> di setiap '
                'sistem untuk mengunduh gambar kartu estetik dan membagikannya ke Story sosmed!</div>',
                unsafe_allow_html=True)

    for row in (results[0:2], results[2:4], results[4:5]):
        cols = st.columns(2, gap="small")
        for col, r in zip(cols, row):
            with col:
                with st.container(key=f'dhres_card_{r["system"].replace(" ", "")}'):
                    tag = f'<span class="dh-rc-tag">{r["tag"]}</span>' if r["tag"] else ""
                    quote = f'<div class="dh-rc-quote">"{r["quote"]}"</div>' if r["quote"] else ""
                    st.markdown(f'<div class="dh-rc-top"><span>{r["label"]}</span>{tag}</div>'
                                f'<div class="dh-rc-title">{r["title"]}</div>'
                                f'<div class="dh-rc-desc">{r["desc"]}</div>{quote}', unsafe_allow_html=True)
                    st.button(f'📷 Lihat & Simpan Kartu {r["short"]}', key=f'dhres_dl_{r["system"]}',
                              on_click=cb_open_detail, args=(r["system"],), use_container_width=True)

    st.markdown('<div class="dh-res-sep"></div>', unsafe_allow_html=True)
    f1, f2, f3 = st.columns([2.2, 1.4, 1.1], gap="small", vertical_alignment="center")
    with f1:
        st.markdown(f'<div class="dh-res-saved">Tersimpan di akun: <b>{email}</b></div>', unsafe_allow_html=True)
    with f2:
        st.button("Buka Profil & Riwayat", key="dhr_profile", on_click=_cb_soon,
                  args=("Profil & riwayat belum tersedia, masih tahap pengembangan 🚧",), use_container_width=True)
    with f3:
        st.button("Scan Orang Lain", key="dhr_again", type="primary", on_click=reset_for_new_scan,
                  use_container_width=True)
