"""
4 modal Bantuan (UI21): FAQ & Bantuan (accordion), Hubungi Kami (form), Kebijakan Privasi, Syarat & Ketentuan.
Dibuka dari mega menu, kartu Explore & footer (class .dh-open-modal + data-modal).
DUMMY: form pesan belum ada backend (toast).
"""

import re

import streamlit as st

from components import auth
from components.feature_modals import _close_btn, _top

_UPDATED = "5 Oktober 2026"

# ─────────────── FAQ ───────────────
_FAQ = [
    ("🔮", "TENTANG DESTINY REVEAL", [
        ("Apa itu Destiny Reveal?",
         "Destiny Reveal adalah platform self-discovery yang menggabungkan 15 sistem ramalan & kepribadian — dari "
         "Zodiak, Shio, Weton, Numerologi, Matrix Destiny, MBTI, Big Five, Enneagram, DISC, Love Language, BaZi, "
         "Zi Wei, Human Design, Golongan Darah, hingga Tarot."),
        ("Apa bedanya dengan platform ramalan lain?",
         "Kami menggabungkan 15 sistem sekaligus dalam satu platform, memberikan gambaran holistik dan komprehensif "
         "tentang potensi, kepribadian, serta dinamika hidupmu."),
    ]),
    ("💎", "TENTANG STARDUST (✨)", [
        ("Apa itu Stardust (✨)?",
         "Stardust (✨) adalah mata uang digital internal di Destiny Reveal yang digunakan untuk membuka (unlock) "
         "fitur premium seperti Laporan Lengkap, Tarot Spreads, Compatibility Report, dan fitur analisis lainnya."),
        ("Bagaimana cara mendapatkan Stardust (✨)?",
         "Kamu bisa mendapatkan Stardust melalui:\n\n- Top-up saldo (mulai dari Rp 10.000)\n- Daily Check-in (Streak)\n"
         "- Program Referral & Undang Teman\n- Reward Milestone & Event Spesial"),
        ("Apakah Stardust (✨) bisa kadaluarsa?", "Tidak. Stardust berlaku selamanya dan tidak memiliki tanggal kadaluarsa."),
        ("Apakah Stardust (✨) bisa di-refund?",
         "Tidak. Stardust bersifat non-refundable dan non-transferable (tidak dapat dikembalikan atau ditransfer ke akun lain)."),
    ]),
    ("🔓", "TENTANG UNLOCK FITUR", [
        ("Apa perbedaan tingkat analisis (Free, Paid, dan Deep)?",
         "- **Free:** Preview gratis 3-5 baris (ringkasan aspek utama).\n"
         "- **Paid (A-F):** Laporan lengkap standar mencakup 6 seksi analisis utama.\n"
         "- **Deep (A-M):** Laporan mendalam mencakup 12 seksi komprehensif + panduan shadow work."),
        ("Berapa biaya Stardust (✨) untuk unlock fitur?",
         "- 1 Sistem (A-F): 50✨\n- 1 Sistem (A-M): 150✨\n- Bundle 15 Sistem (A-F): 500✨\n- Bundle 15 Sistem (A-M): 1.500✨"),
        ("Jika sudah unlock versi A-F, apakah bisa upgrade ke A-M?", "Bisa. Kamu cukup membayar selisihnya sebesar 100✨."),
    ]),
    ("💳", "TENTANG PEMBAYARAN", [
        ("Metode pembayaran apa saja yang tersedia?",
         "Kami mendukung pembayaran otomatis via:\n\n- QRIS (All Payment / E-Wallet)\n- E-Wallet: GoPay, OVO, DANA, ShopeePay\n"
         "- Virtual Account (BCA, BNI, Mandiri, BRI)\n- Kartu Debit / Kredit (via Payment Gateway resmi)"),
        ("Apakah transaksi pembayaran aman?",
         "Sangat aman. Seluruh transaksi diproses melalui Midtrans yang terlisensi resmi oleh Bank Indonesia dengan "
         "enkripsi standar industri."),
        ("Apakah transaksi pembelian bisa di-refund?",
         "Produk digital bersifat non-refundable. Refund hanya dapat diproses jika terjadi kendala teknis atau "
         "kegagalan sistem dari pihak kami."),
    ]),
    ("⭐", "TENTANG VIP MEMBERSHIP", [
        ("Apa saja keuntungan menjadi VIP Member?",
         "- Akses seluruh 15 sistem tanpa batas\n- Kuota 10 Deep Report (A-M) setiap bulan\n- Fitur Export & Download PDF Laporan\n"
         "- Bebas dari iklan (Ad-Free Experience)\n- Prioritas antrean pemrosesan data & akses fitur baru lebih awal"),
        ("Berapa tarif berlangganan VIP?",
         "- Bulanan: Rp 99.000 / bulan\n- 3 Bulan: Rp 249.000\n- 6 Bulan: Rp 449.000\n- 1 Tahun: Rp 799.000\n"
         "- Lifetime Access: Rp 1.999.000 (Bayar sekali untuk selamanya)"),
        ("Apakah VIP bisa dibayar menggunakan Stardust (✨)?",
         "Tidak. Langganan VIP hanya dapat dibayar menggunakan mata uang Rupiah (IDR)."),
    ]),
    ("🎁", "TENTANG REFERRAL & AFFILIATE", [
        ("Bagaimana cara mendapatkan link/kode referral?",
         "Kode referral otomatis dibuat setelah kamu mendaftar. Cek di Dashboard → Tab Referral."),
        ("Berapa komisi yang didapatkan dari referral?",
         "- **User Biasa (Referral):** Komisi 10–15% berupa Stardust (✨).\n"
         "- **Affiliate Partner:** Komisi 20–30% berupa Uang Tunai (Rupiah)."),
        ("Syarat untuk upgrade menjadi Affiliate Partner?",
         "1. Memiliki minimal 10 Referral Aktif\n2. Minimal 5 Referral melakukan belanja/transaksi\n"
         "3. Akumulasi Revenue transaksi referral mencapai Rp 500.000\n4. Verifikasi Email & Nomor HP aktif\n"
         "5. Verifikasi KTP & Rekening Bank atas nama pribadi"),
    ]),
    ("🛠️", "TROUBLESHOOTING & BANTUAN TEKNIS", [
        ("Laporan saya tidak muncul setelah transaksi berhasil?",
         "Cek konfirmasi email (termasuk folder Spam/Promotions). Jika belum ada, silakan hubungi tim support dengan "
         "melampirkan Bukti / ID Transaksi."),
        ("Mengapa saldo Stardust saya tidak tersimpan?",
         "Jika mengakses dalam Mode Tamu (belum login), saldo disimpan di browser lokal. Silakan Log In / Buat Akun "
         "agar saldo tersinkronisasi aman di server secara permanen."),
    ]),
]


@st.dialog("FAQ & Bantuan", width="large")
def faq_dialog():
    _top(login_link=False, key="fq")
    st.markdown('<div class="dh-hp-h1">FAQ &amp; BANTUAN</div>', unsafe_allow_html=True)
    for ico, title, qas in _FAQ:
        st.markdown(f'<div class="dh-hp-h2">{ico} {title}</div>', unsafe_allow_html=True)
        for q, a in qas:
            with st.expander(q):
                st.markdown(a)
    _close_btn("Tutup", "fq", outline=True)


# ─────────────── Hubungi Kami ───────────────
_KATEGORI = ["Support", "Pembayaran", "Affiliate", "Kendala Teknis", "Lainnya"]
_EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def _contact_card(ico, title, rows, note=""):
    li = "".join(f"<li><span>{k}</span><b>{v}</b></li>" for k, v in rows)
    n = f'<div class="dh-hp-note">{note}</div>' if note else ""
    return f'<div class="dh-hp-card"><div class="dh-hp-ct">{ico} {title}</div><ul>{li}</ul>{n}</div>'


@st.dialog("Hubungi Kami", width="large")
def contact_dialog():
    _top(login_link=False, key="ct")
    u = auth.current_user() or {}
    st.markdown(
        '<div class="dh-hp-h1">HUBUNGI KAMI</div>'
        '<p class="dh-hp-lead">Kami siap membantu kamu! Pilih saluran komunikasi yang paling nyaman bagi kamu:</p>'
        + _contact_card("📧", "EMAIL &amp; SUPPORT", [
            ("Customer Support", "support@destinyreveal.com"), ("Kerjasama / Business", "hello@destinyreveal.com"),
            ("Program Affiliate", "affiliate@destinyreveal.com")], "Respon balasan max 1x24 jam pada hari kerja")
        + _contact_card("💬", "WHATSAPP &amp; SOCIAL MEDIA", [
            ("WhatsApp Support", "+62 812-3456-7890"), ("Jam Operasional", "09:00 - 18:00 WIB"),
            ("Instagram", "@destinyreveal"), ("TikTok", "@destinyreveal"), ("Twitter / X", "@destinyreveal")])
        + _contact_card("🏢", "DOMISILI OPERASIONAL", [("Destiny Reveal HQ", "Operasional Digital / Jakarta, Indonesia")]),
        unsafe_allow_html=True)
    st.markdown('<div class="dh-hp-h2">📝 FORM PESAN / BANTUAN</div>', unsafe_allow_html=True)
    with st.form("dhct_form", clear_on_submit=True, border=False):
        nama = st.text_input("Nama Lengkap", value=u.get("nama", ""), placeholder="Nama kamu")
        email = st.text_input("Email Terdaftar", value=u.get("email", ""), placeholder="nama@email.com")
        kat = st.selectbox("Kategori Pertanyaan", _KATEGORI)
        pesan = st.text_area("Pesan / Kendala", placeholder="Ceritakan kendala atau pertanyaanmu...", height=110)
        sent = st.form_submit_button("Kirim Pesan", type="primary", use_container_width=True)
    if sent:
        if not nama.strip() or not pesan.strip() or not _EMAIL_RE.match(email.strip()):
            st.error("Lengkapi nama, email yang valid, dan pesan dulu ya.")
        else:
            st.toast(f"✅ Pesan ({kat}) terkirim! Kami balas max 1x24 jam hari kerja.")  # DUMMY: belum ada backend
    _close_btn("Tutup", "ct", outline=True)


# ─────────────── Privasi & Terms ───────────────
def _sec(title, body):
    return f'<div class="dh-hp-sec"><div class="dh-hp-h3">{title}</div>{body}</div>'


def _ul(items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


@st.dialog("Kebijakan Privasi", width="large")
def privacy_dialog():
    _top(login_link=False, key="pv")
    st.markdown(
        '<div class="dh-hp-h1">KEBIJAKAN PRIVASI</div>'
        f'<div class="dh-hp-upd">Terakhir Diperbarui: {_UPDATED}</div>'
        + _sec("1. PENDAHULUAN",
               "<p>Destiny Reveal (&quot;Kami&quot;) berkomitmen untuk melindungi dan menghormati privasi data pribadi "
               "pengguna. Kebijakan Privasi ini menjelaskan bagaimana kami mengumpulkan, menggunakan, menyimpan, dan "
               "melindungi informasi pribadi kamu sesuai dengan ketentuan regulasi Perlindungan Data Pribadi (PDP) yang berlaku.</p>")
        + _sec("2. DATA YANG KAMI KUMPULKAN",
               "<p>Kami mengumpulkan informasi yang kamu berikan secara langsung saat registrasi dan penggunaan layanan:</p>"
               + _ul(["<b>Data Profil:</b> Nama, alamat email, tanggal lahir, jam lahir (opsional), kota kelahiran (opsional), dan golongan darah (opsional).",
                      "<b>Data Transaksi:</b> Informasi pembayaran yang diproses secara aman melalui payment gateway mitra kami (Midtrans). Kami tidak pernah menyimpan data kartu kredit/debit di server kami.",
                      "<b>Data Teknis:</b> Alamat IP, jenis perangkat, jenis browser, data log, dan aktivitas penggunaan layanan."]))
        + _sec("3. PENGGUNAAN DATA",
               "<p>Data pribadi kamu digunakan khusus untuk:</p>"
               + _ul(["Menggenerasi hasil analisis ramalan &amp; profil self-discovery secara akurat.",
                      "Memproses transaksi pembayaran dan pengelolaan saldo Stardust / VIP.",
                      "Mengirimkan konfirmasi akun, notifikasi transaksi, dan informasi layanan.",
                      "Mengamankan akun dari potensi fraud dan penyalahgunaan."])
               + "<p><b>Kami menjamin TIDAK AKAN PERNAH menjual atau menyewakan data pribadi kamu kepada pihak ketiga mana pun.</b></p>")
        + _sec("4. KEAMANAN DATA",
               "<p>Kami menerapkan standar keamanan enkripsi SSL/TLS untuk seluruh lalu lintas data, enkripsi kata sandi, "
               "dan pembatasan akses server yang ketat guna melindungi data kamu dari akses yang tidak sah.</p>")
        + _sec("5. HAK PENGGUNA",
               "<p>Kamu berhak untuk mengakses, memperbarui, meminta salinan, atau mengajukan penghapusan data pribadi kamu "
               "dari sistem kami kapan saja dengan menghubungi kami melalui <b>support@destinyreveal.com</b>.</p>"),
        unsafe_allow_html=True)
    _close_btn("Mengerti & Kembali", "pv")


@st.dialog("Syarat & Ketentuan", width="large")
def terms_dialog():
    _top(login_link=False, key="tm")
    st.markdown(
        '<div class="dh-hp-h1">SYARAT &amp; KETENTUAN</div>'
        f'<div class="dh-hp-upd">Terakhir Diperbarui: {_UPDATED}</div>'
        + _sec("1. PENERIMAAN SYARAT",
               "<p>Dengan mendaftar, mengakses, atau menggunakan platform Destiny Reveal, kamu menyatakan telah membaca, "
               "memahami, dan menyetujui seluruh Syarat &amp; Ketentuan ini.</p>")
        + _sec("2. PENAFIAN LAYANAN (DISCLAIMER)",
               _ul(["Destiny Reveal adalah platform self-discovery dan hiburan berbasis analisis kompilasi 15 sistem astrologi, numerologi, dan psikologi.",
                    "Seluruh informasi dan hasil laporan yang disajikan bertujuan sebagai sarana refleksi diri dan <b>HIBURAN</b> semata, bukan merupakan nasihat finansial, medis, hukum, atau profesional.",
                    "Setiap keputusan atau tindakan yang kamu ambil berdasarkan hasil analisis platform adalah tanggung jawab pribadi pengguna sepenuhnya."]))
        + _sec("3. KETENTUAN AKUN &amp; PENGGUNAAN",
               _ul(["Pengguna wajib memberikan data registrasi yang akurat dan menjaga kerahasiaan akun masing-masing.",
                    "Dilarang keras melakukan manipulasi sistem, penggunaan bot, penyebaran spam referral, atau pembuatan akun palsu. Pelanggaran dapat mengakibatkan penghentian akun (suspend/ban) secara permanen tanpa pengembalian dana."]))
        + _sec("4. PEMBAYARAN, STARDUST &amp; NON-REFUNDABLE",
               _ul(["Seluruh transaksi dilakukan dalam mata uang Rupiah (IDR).",
                    "Stardust (✨) adalah poin internal platform yang tidak dapat diuangkan kembali (non-refundable) dan tidak dapat ditransfer antar akun.",
                    "Seluruh pembelian produk digital bersifat final dan tidak dapat dibatalkan atau dikembalikan dana, kecuali disebabkan oleh kegagalan sistem dari pihak kami."]))
        + _sec("5. HUKUM YANG BERLAKU",
               "<p>Syarat &amp; Ketentuan ini diatur dan ditafsirkan sesuai dengan hukum yang berlaku di Republik Indonesia.</p>"),
        unsafe_allow_html=True)
    _close_btn("Mengerti & Kembali", "tm")


DIALOGS = {"faq": faq_dialog, "contact": contact_dialog, "privacy": privacy_dialog, "terms": terms_dialog}
