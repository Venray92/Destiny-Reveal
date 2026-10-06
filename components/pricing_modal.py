"""
Modal "Daftar Harga & Benefit VIP" (UI14). 5 tab: Semua | Stardust | Fitur Stardust | VIP | Referral.
Tab = tombol segmented + session_state (dh_pr_tab), pindah tab lewat on_click (dialog tetap kebuka).
Tampilan light (ngikutin mockup), bukan dark theme.
DUMMY: pembelian Stardust / langganan VIP / tombol "Buka" fitur belum terhubung payment (toast / buka modal fitur).
"""

import html

import streamlit as st

from components import auth
from components.dialog_bus import request_open
from components.feature_modals import _top
from components.modal_detail import copy_button

_PAY_TOAST = "Pembayaran belum tersedia, masih tahap pengembangan 🚧"
TABS = [("semua", "Semua"), ("koin", "✨ Stardust"), ("fitur", "🔒 Fitur Stardust"), ("vip", "⭐ VIP"), ("ref", "🎁 Referral")]

# (nama, badge, harga, per SD, jumlah SD, bonus, deskripsi)
COIN_PACKS = [
    ("Starter", "Coba Dulu", "Rp 10.000", "Rp 83/SD", 120, "+20%", "Cocok untuk dicoba, bisa unlock 2 sistem atau Tarot 3 Kartu."),
    ("Basic", "Populer", "Rp 25.000", "Rp 71/SD", 350, "+40%", "Pilihan pas untuk eksplorasi beberapa sistem dan Tarot."),
    ("Value", "Hemat", "Rp 50.000", "Rp 67/SD", 750, "+50%", "Cukup untuk Complete Bundle (15 sistem) atau Deep Blueprint."),
    ("Pro", "Best Value", "Rp 100.000", "Rp 63/SD", 1600, "+60%", "Ideal untuk eksplorasi mendalam, report bulanan, dan kompatibilitas."),
    ("Sultan", "Top Up / Hemat 75%", "Rp 200.000", "Rp 57/SD", 3500, "+75%", "Akses tak terbatas untuk semua analisis, report, dan Tarot."),
    ("Kaisar", "Top Up / Bonus 100%", "Rp 500.000", "Rp 50/SD", 10000, "+100%", "Paket ultimate dengan bonus maksimal untuk penggunaan jangka panjang tanpa batas."),
]


def _fmt(n):
    return f"{n:,}".replace(",", ".")


# (kategori, [(nama, SD, keterangan, dialog tujuan, state)])
FEATURES = [
    ("ANALISIS SISTEM LAHIR & PSIKOLOGI", [
        ("Buka 1 Sistem (Daily) Lengkap", 50, "Buka lengkap ramalan harian", "daily", {}),
        ("Buka 1 Sistem (Single)", 150, "Analisis A-F lengkap untuk 1 sistem pilihan", "reveal", {}),
        ("Bundle 5 Sistem Kelahiran", 200, "A-F lengkap untuk Zodiak, Shio, Weton, Numerologi, Matrix Destiny (Hemat 20%)", "reveal", {"dh_modal_mode": "instan"}),
        ("Bundle 5 Tes Psikologi", 200, "A-F lengkap untuk MBTI, Big Five, Enneagram, DISC, Love Language (Hemat 20%)", "reveal", {"dh_modal_mode": "mendalam"}),
        ("Complete Bundle (15 Sistem)", 500, "A-F lengkap untuk SELURUH 15 sistem (Hemat 67% 🔥)", "reveal", {"dh_modal_mode": "lengkap"}),
    ]),
    ("TAROT MULTI KARTU", [
        ("Tarot 3 Kartu", 50, "Past, Present, Future + Interpretasi Detail", "tarot_spread", {"dh_ts_tab": 3}),
        ("Tarot 5 Kartu", 100, "Cross Spread (Situasi, Rintangan, Bawah Sadar, Saran, Hasil)", "tarot_spread", {"dh_ts_tab": 5}),
        ("Tarot Celtic Cross", 150, "10 Posisi Legendaris Celtic Cross Komprehensif", "tarot_spread", {"dh_ts_tab": 10}),
        ("Tarot Bundle", 250, "3 Spread Sekaligus (Hemat 50 SD)", "tarot_spread", {"dh_ts_tab": 3}),
    ]),
    ("LAPORAN & KECOCOKAN (REPORT & COMPATIBILITY)", [
        ("Weekly Report", 100, "Panduan timing & prediksi mingguan (4-5 minggu)", "weekly", {}),
        ("Monthly Report", 200, "Prediksi bulanan komprehensif + saran strategis & risiko (12 bulan)", "weekly", {}),
        ("Deep Blueprint Report", 300, "Analisis A-M (13 Section) super mendalam", "blueprint", {}),
        ("Compatibility (1 Sistem)", 100, "Analisis kecocokan 2 orang (Nama + Tanggal Lahir)", "compat", {}),
        ("Compatibility (2 Sistem)", 180, "Kecocokan 2 orang pada 2 sistem", "compat", {}),
        ("Compatibility (3 Sistem)", 250, "Kecocokan 2 orang pada 3 sistem", "compat", {}),
    ]),
]
VIP_BENEFITS = ["Semua 15 sistem kebuka tanpa batas", "10 Deep Report / bulan",
                "Download booklet PDF personal", "Bebas iklan (No Ads) & antrean cepat",
                "Akses fitur baru duluan"]
# (label, nama, harga, satuan, deskripsi, tombol, gaya, badge)
VIP_PLANS = [
    ("1 BULAN", "VIP 1 Bulan", "Rp 99.000", "per bulan", "Eksplorasi intensif selama 30 hari.", "Pilih Bulanan", "out", ""),
    ("3 BULAN", "VIP 3 Bulan", "Rp 249.000", "(~Rp 83.000/bln)", "Hemat Rp 48.000 dibanding bulanan.", "Pilih 3 Bulan", "out", "HEMAT 16%"),
    ("6 BULAN", "VIP 6 Bulan", "Rp 449.000", "(~Rp 74.833/bln)", "Hemat Rp 145.000 untuk setengah tahun.", "Pilih 6 Bulan", "out", "HEMAT 24%"),
    ("1 TAHUN", "VIP 1 Tahun", "Rp 799.000", "(~Rp 66.583/bln)", "Pilihan paling hemat untuk setahun penuh.", "Pilih Tahunan", "out", "PALING POPULER · HEMAT 33%"),
    ("SEKALI BAYAR", "VIP Lifetime", "Rp 1.999.000", "(Sekali Bayar)", "Akses seumur hidup tanpa biaya langganan bulanan selamanya.", "Pilih Lifetime", "out", "ALL ACCESS"),
]
COMMISSION = [
    ("USER BIASA (REFERRAL)", "Referral Stardust", "10 - 15%",
     "Dapatkan komisi Stardust dari setiap teman yang top up Stardust (10%) atau buka Report (15%)."),
    ("AFFILIATE PARTNER", "Affiliate (Cuan Cash)", "20 - 30%",
     "Komisi berupa uang tunai (dapat dicairkan) untuk kreator &amp; komunitas yang memenuhi syarat."),
    ("INCOME PASIF", "VIP Recurring", "10 - 15%",
     "Komisi pasif berkala setiap bulan selama teman yang kamu undang tetap aktif berlangganan VIP."),
]
# (omset referral, extra bonus)
AFF_SYARAT = ["10 Referral Aktif (Daftar pakai kode kamu)", "5 Referral Belanja (Melakukan transaksi)",
              "Total Revenue Rp 500.000 dari transaksi referral", "Verifikasi Email & Nomor HP",
              "Verifikasi KTP (Khusus pencairan komisi)", "Rekening Bank (Tujuan transfer komisi)"]
MILESTONES = [("Rp 500rb", "Extra Rp 50.000"), ("Rp 2,5jt", "Extra Rp 250.000"),
              ("Rp 10jt", "Extra Rp 1.000.000"), ("Rp 25jt", "Extra Rp 2.500.000")]
# (ikon, nama, komisi, syarat) - tier pertama = tier aktif user baru
TIERS = [("✨", "Stardust", "10%", ""), ("⭐️", "Star", "15%", "10 Referral"), ("🌟", "Constell.", "20%", "25 Referral"),
         ("💫", "Galaxy", "25%", "50 Referral"), ("🌌", "Universe", "30%", "100 Referral")]
BLUEPRINT_AM = [
    ("A", "aspek_utama", "Aspek utama kepribadian"), ("B", "karier_dan_keuangan", "Karier & keuangan"),
    ("C", "asmara_dan_hubungan", "Asmara & hubungan"), ("D", "kekuatan_karakter", "Kekuatan karakter"),
    ("E", "shadow_work", "Shadow work / sisi gelap"), ("F", "nasihat_strategis", "Nasihat strategis"),
    ("G", "siapa_kamu", "Siapa kamu"), ("H", "karir", "Karier"), ("I", "asmara", "Asmara"),
    ("J", "keuangan", "Keuangan"), ("K", "shadow_side", "Shadow side"), ("L", "blindspot", "Blindspot"),
    ("M", "pr_kecil_buat_kamu", "PR kecil"),
]


def _buy(_what=""):
    st.toast(_PAY_TOAST)


def _cb_tab(t):
    st.session_state.dh_pr_tab = t


# ─────────────── bagian-bagian ───────────────
def _sec_head(icon, title, right):
    st.markdown(f'<div class="dh-pr-sec"><b>{icon} {title}</b><span>{right}</span></div>', unsafe_allow_html=True)


def _sec_coin():
    _sec_head("✨", "Paket Stardust", "Stardust tidak pernah kedaluwarsa &amp; non-refundable")
    for row in range(0, len(COIN_PACKS), 2):
        chunk = COIN_PACKS[row:row + 2]
        cols = st.columns(len(chunk) if len(chunk) == 2 else 1, gap="small")
        for col, (nama, badge, harga, per, sd, bonus, desc) in zip(cols, chunk):
            with col:
                with st.container(key=f"dhpr_coin_{sd}"):
                    st.markdown(
                        f'<div class="dh-pr-chead"><b>{nama}</b><em>{badge}</em></div>'
                        f'<div class="dh-pr-sd">{_fmt(sd)} ✨ Stardust <i>Bonus {bonus}</i></div>'
                        f'<div class="dh-pr-price">{harga}</div>'
                        f'<div class="dh-pr-cdesc">{desc}</div>', unsafe_allow_html=True)
                    st.button(f"Beli {_fmt(sd)} Stardust", key=f"dhpr_buy_{sd}", on_click=_buy, use_container_width=True)


def _blueprint_info():
    """Tombol ℹ️ + popup struktur A-M Deep Blueprint."""
    with st.popover("ℹ️"):
        st.markdown('<div class="dh-pr-tiphead">Struktur Deep Blueprint (A-M)</div>', unsafe_allow_html=True)
        st.markdown('<div class="dh-pr-tip">' + "".join(
            f'<div><b>{k}</b><span><code>{key}</code> {html.escape(ket)}</span></div>' for k, key, ket in BLUEPRINT_AM)
            + '</div>', unsafe_allow_html=True)


_COLS = [1.7, 0.95, 2.4, 0.85]


def _sec_fitur():
    _sec_head("🔒", "Harga Fitur (Pakai Stardust)", "Bayar sesuai kebutuhan")
    with st.container(key="dhpr_table"):
        with st.container(key="dhpr_head"):
            h = st.columns(_COLS, gap="small", vertical_alignment="center")
            for col, t in zip(h, ["FITUR", "HARGA", "KETERANGAN", "AKSI"]):
                with col:
                    if t == "KETERANGAN":
                        with st.container(key="dhpr_bp_ket"):
                            k1, k2 = st.columns([1, 1], gap="small", vertical_alignment="center")
                            with k1:
                                st.markdown(f'<div class="dh-pr-hd">{t}</div>', unsafe_allow_html=True)
                            with k2:
                                with st.container(key="dhpr_info"):
                                    _blueprint_info()
                    else:
                        st.markdown(f'<div class="dh-pr-hd">{t}</div>', unsafe_allow_html=True)
        i = 0
        for kat, rows in FEATURES:
            st.markdown(f'<div class="dh-pr-cat">{html.escape(kat)}</div>', unsafe_allow_html=True)
            for nama, sd, ket, dlg, state in rows:
                with st.container(key=f"dhpr_row_{i}"):
                    c1, c2, c3, c4 = st.columns(_COLS, gap="small", vertical_alignment="center")
                    with c1:
                        st.markdown(f'<div class="dh-pr-fn">{nama}</div>', unsafe_allow_html=True)
                    with c2:
                        st.markdown(f'<span class="dh-pr-pill">{sd} ✨ SD</span>', unsafe_allow_html=True)
                    with c3:
                        st.markdown(f'<div class="dh-pr-fk">{html.escape(ket)}</div>', unsafe_allow_html=True)
                    with c4:
                        if st.button("Buka →", key=f"dhpr_open_{i}"):
                            request_open(dlg, **state)
                i += 1


def _sec_vip():
    _sec_head("⭐", "VIP (Langganan)", '<i class="dh-pr-allacc">All Access</i>')
    items = "".join(f'<div>✓ {b}</div>' for b in VIP_BENEFITS)
    st.markdown(f'<div class="dh-pr-vipbox"><b>✦ BENEFIT VIP MEMBERSHIP ✦</b><div class="dh-pr-vipgrid">{items}</div></div>',
                unsafe_allow_html=True)
    for r0 in range(0, len(VIP_PLANS), 3):
        chunk = list(enumerate(VIP_PLANS))[r0:r0 + 3]
        cols = st.columns(3, gap="small")
        for col, (i, (lab, nama, harga, unit, desc, btn, style, badge)) in zip(cols, chunk):
            with col:
                with st.container(key=f"dhpr_plan_{style}_{i}"):
                    ribbon = (f'<span class="dh-pr-ribbon">{badge}</span>'
                              if badge else '<div style="height:16px"></div>')
                    st.markdown(f'{ribbon}<div class="dh-pr-plab">{lab}</div><div class="dh-pr-pname">{nama}</div>'
                                f'<div class="dh-pr-price">{harga}</div><div class="dh-pr-unit">{unit}</div>'
                                f'<div class="dh-pr-cdesc dh-pr-cd3">{desc}</div>',
                                unsafe_allow_html=True)
                    st.button(btn, key=f"dhpr_plan_btn_{i}", type="secondary",
                              on_click=_buy, use_container_width=True)


def _sec_ref():
    _sec_head("🎁", "Program Referral & Affiliate", '<i class="dh-pr-comm">Komisi Menarik</i>')
    syarat = ('<i class="dh-pr-ti" tabindex="0">ℹ️ Lihat Syarat Upgrade<i class="dh-pr-pop"><i class="dh-pr-pophead">📌 SYARAT NAIK TIER AFFILIATE (Pencairan Uang Tunai):</i>'
              + "".join(f'<i class="dh-pr-popi"><i>{n}</i>{html.escape(t)}</i>' for n, t in enumerate(AFF_SYARAT, 1)) + '</i></i>')
    cards = "".join(f'<div><span>{a}</span><u>{t}</u><b>{b}</b><p>{c}</p>{syarat if i == 1 else ""}</div>'
                    for i, (a, t, b, c) in enumerate(COMMISSION))
    ms = "".join(f'<div><span>{a}</span><i>➡️</i><b>{b}</b></div>' for a, b in MILESTONES)
    tiers = "".join(
        f'<div class="dh-pr-tier{" on" if i == 0 else ""}"><i>{ic}</i><b>{nm}</b><em>({pc})</em>'
        + ('<s>← Kamu</s>' if i == 0 else f'<small>{req}</small>') + '</div>'
        for i, (ic, nm, pc, req) in enumerate(TIERS))
    steps = '<i>➔</i>'.join(f'<span>{x}</span>' for x in ["Buat akun / Login", "Dapatkan Kode Unik", "Bagikan Link", "Dapat Komisi Stardust (10-15%)!"])
    st.markdown(
        f'<div class="dh-pr-refwrap"><div class="dh-pr-refcards">{cards}</div>'
        f'<div class="dh-pr-ms"><div class="dh-pr-mshead">🏆 Extra Bonus Milestone (10% Revenue)</div>'
        f'<div class="dh-pr-mssub">Dapatkan bonus tambahan 10% tunai setiap kali mencapai total transaksi referral berikut:</div>'
        f'<div class="dh-pr-msgrid">{ms}</div></div></div>'
        f'<div class="dh-pr-tierhead">TIER JOURNEY KOSMIK</div><div class="dh-pr-tiers">{tiers}</div>'
        f'<div class="dh-pr-tierhead">CARA KERJA PROGRAM</div><div class="dh-pr-how">'
        f'<div><b>🔁 Referral Biasa (Otomatis)</b><div class="dh-pr-steps">{steps}</div></div>'
        f'<div><b>🚀 Upgrade ke Affiliate (Komisi Cair Tunai)</b>'
        f'<p>Capai <u>10 Referral</u> (5 Belanja &amp; Revenue Rp 500rb) + lengkapi <u>Verifikasi KTP &amp; Rekening Bank</u> '
        f'untuk mulai cairkan uang tunai setiap <u>tanggal 1-5</u> awal bulan.</p></div></div>',
        unsafe_allow_html=True)
    u = auth.current_user()
    with st.container(key="dhpr_refcode"):
        if u:
            link = f"https://destiny-reveal.streamlit.app/?ref={u['ref']}"
            c1, c2, c3 = st.columns([1.5, 1, 1], gap="small", vertical_alignment="center")
            with c1:
                st.markdown(f'<div class="dh-pr-rcl">ID &amp; LINK REFERRAL KHUSUS KAMU</div><div class="dh-pr-rc">{u["ref"]}</div>',
                            unsafe_allow_html=True)
            with c2:
                copy_button(u["ref"], "📋 Salin Kode", "dhpr_cp", fs=12)
            with c3:
                copy_button(link, "🔗 Salin Link", "dhpr_cp2", fs=12)
        else:
            c1, c2 = st.columns([1.5, 1.2], gap="small", vertical_alignment="center")
            with c1:
                st.markdown('<div class="dh-pr-rcl">ID &amp; LINK REFERRAL KHUSUS KAMU</div>'
                            '<div class="dh-pr-rc dh-pr-rcoff">Masuk atau buat akun dulu untuk mendapatkan kode referral unik kamu.</div>',
                            unsafe_allow_html=True)
            with c2:
                if st.button("Masuk / Daftar Sekarang", key="dhpr_login", type="primary", use_container_width=True):
                    request_open("auth")


# ─────────────── dialog ───────────────
@st.dialog("Daftar Harga & Benefit VIP", width="large", on_dismiss="rerun")
def pricing_dialog():
    ss = st.session_state
    _top(login_link=False, key="pr")
    st.markdown('<div class="dh-step dh-step-price"></div><div class="dh-pr-eyebrow">✦ TRANSPARANSI BIAYA DESTINY REVEAL ✦</div>'
                '<div class="dh-pr-title">Daftar Harga &amp; Benefit VIP</div>'
                '<div class="dh-pr-sub">Mulai dari eksplorasi gratis, fleksibilitas paket Stardust tanpa kedaluwarsa, '
                'hingga membership VIP tak terbatas.</div><div class="dh-fm-div"></div>', unsafe_allow_html=True)
    tab = ss.setdefault("dh_pr_tab", "semua")
    with st.container(key="dhpr_tabs"):
        cols = st.columns(len(TABS), gap="small")
        for col, (k, lab) in zip(cols, TABS):
            with col:
                st.button(lab, key=f"dhpr_tab_{k}", on_click=_cb_tab, args=(k,),
                          type="primary" if tab == k else "secondary", use_container_width=True)
    if tab in ("semua", "koin"):
        _sec_coin()
    if tab in ("semua", "fitur"):
        _sec_fitur()
    if tab in ("semua", "vip"):
        _sec_vip()
    if tab in ("semua", "ref"):
        _sec_ref()
    with st.container(key="dhfm_outline_pr"):
        if st.button("Tutup & Kembali", key="dhpr_close", use_container_width=True):
            st.rerun()


def open_pricing(tab="semua"):
    """Dipanggil dari tombol biasa di halaman (bukan dari dalam dialog)."""
    st.session_state.dh_pr_tab = tab
    pricing_dialog()


def _open_all():
    open_pricing("semua")


DIALOGS = {
    "pricing": _open_all,
    "pricing_koin": lambda: open_pricing("koin"),
    "pricing_fitur": lambda: open_pricing("fitur"),
    "pricing_vip": lambda: open_pricing("vip"),
    "pricing_ref": lambda: open_pricing("ref"),
}
