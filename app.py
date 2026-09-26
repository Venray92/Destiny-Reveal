"""
Destiny Reveal — entry point Streamlit app.
Homepage + preview layout form. Isi/logic ditambahin pelan-pelan dari sini.
"""

import streamlit as st

from views.reveal_yourself import render as render_reveal_yourself
from views.loadingpage import render as render_loading
from views.revealpage import render as render_result

st.set_page_config(
    page_title="Destiny Reveal",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Custom CSS ──────────────────────────────────────────────
st.markdown(
    '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />'
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,wght@0,500;0,600;0,700;1,500&family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Lora:ital,wght@0,400;0,500;1,400&display=swap">',
    unsafe_allow_html=True,
)
st.markdown(
    """
    <style>
    #MainMenu, footer, header {visibility: hidden;}

    .material-symbols-outlined {
        font-family: 'Material Symbols Outlined';
        font-weight: normal; font-style: normal; font-size: 24px; line-height: 1;
        letter-spacing: normal; text-transform: none; display: inline-block;
        white-space: nowrap; word-wrap: normal; direction: ltr;
        -webkit-font-smoothing: antialiased;
    }

    .dr-font-display { font-family: 'Fraunces', serif !important; }
    .dr-font-reading { font-family: 'Lora', serif !important; }

    /* Sembunyikan panah dropdown (expand_more) di tombol popover chip sistem.
       Dicek langsung dari DOM: panah dibungkus div aria-hidden="true" terpisah
       dari ikon+label, jadi bisa ditarget spesifik tanpa ikut menghapus ikon. */
    button[data-testid="stPopoverButton"] div[aria-hidden="true"] { display: none !important; }

    /* Paksa panel popover selalu terang, apapun tema browser/sistemnya —
       sebelumnya panel ini ikut dark-mode sehingga teks gelap jadi tak kebaca.
       Sekarang juga dikasih border + shadow biar nggak nyaru ke background putih halaman. */
    div[data-testid="stPopoverBody"] {
        background-color: #ffffff !important;
        color: #1c1a17 !important;
        border: 1.5px solid #ecddc9 !important;
        border-radius: 14px !important;
        box-shadow: 0 16px 36px -14px rgba(28,26,23,0.22) !important;
    }
    div[data-testid="stPopoverBody"] * {
        color: inherit;
    }

    /* Kolom Streamlit auto-stretch tinggi sesuai isi paling tinggi.
       Testid kolom aslinya "stColumn". stColumn sendiri sudah stretch otomatis
       dari flexbox parent (stHorizontalBlock, align-items:stretch), tapi
       beberapa div pembungkus DI DALAMNYA (stVerticalBlock, stLayoutWrapper,
       stElementContainer, dst) masih perlu diregangkan manual lewat flex-grow,
       khusus untuk kartu yang dibungkus st.container(key="drfillheight_...").
       Pakai :has() supaya ancestor-nya ikut kebawa tanpa menyentuh kolom lain
       di halaman yang tidak perlu tinggi seragam. */
    [data-testid="stHorizontalBlock"] { align-items: stretch !important; }

    [data-testid="stColumn"]:has([class*="drfillheight"]) {
        display: flex !important; flex-direction: column !important;
    }
    [data-testid="stVerticalBlock"]:has([class*="drfillheight"]),
    [data-testid="stLayoutWrapper"]:has([class*="drfillheight"]) {
        display: flex !important; flex-direction: column !important;
        flex: 1 !important; min-height: 0 !important;
    }
    [class*="drfillheight"] {
        display: flex !important; flex-direction: column !important;
        flex: 1 !important; min-height: 0 !important;
    }
    [class*="drfillheight"] [data-testid="stElementContainer"],
    [class*="drfillheight"] .stMarkdown,
    [class*="drfillheight"] .stMarkdown > div,
    [class*="drfillheight"] [data-testid="stMarkdownContainer"] {
        display: flex !important; flex-direction: column !important;
        flex: 1 !important; min-height: 0 !important;
    }
    [class*="drfillheight"] .dr-card,
    [class*="drfillheight"] .dr-bulk-card {
        flex: 1 !important;
    }

    .stApp { background-color: #ffffff; }
    .block-container { padding-top: 1.5rem; padding-bottom: 2rem; max-width: 1360px; }
    div[data-testid="stVerticalBlock"] { gap: 1rem !important; }

    .stApp, .stApp p, .stApp span, .stApp div, .stApp b, .stApp li,
    .stApp label, .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5,
    .stMarkdown, .stMarkdown p {
        color: #1c1a17;
    }
    .stApp { font-family: 'Plus Jakarta Sans', -apple-system, sans-serif; }

    .dr-center { text-align: center; }
    /* Footer copyright + byline — dipakai lewat class, bukan inline style,
       karena sanitizer HTML Streamlit ternyata membuang deklarasi CSS yang
       pakai !important di dalam atribut style="" (terbukti lewat inspeksi
       DOM langsung: propertinya lenyap total dari outerHTML). */
    .dr-footer-copyright { text-align: center; color: #9a948a !important; font-size: 12.5px; }
    .dr-footer-byline { color: #d9cdb6 !important; }

    .dr-badge {
        display: inline-flex; align-items: center; gap: 6px;
        padding: 7px 16px; border: 1px solid #ecddc9; border-radius: 100px;
        font-size: 13px; color: #8a5a2f !important; background: #fdf3e7;
        margin-bottom: 22px;
    }
    .dr-hero-title {
        font-family: 'Fraunces', serif;
        font-size: 38px; font-weight: 700; line-height: 1.25;
        margin: 0 0 22px 0; letter-spacing: -0.01em; color: #1c1a17 !important;
        text-align: left;
    }
    .dr-hero-sub {
        font-size: 18px; line-height: 1.75; color: #5c564d !important;
        max-width: 680px; margin: 0 0 30px 0; text-align: left;
    }
    .dr-hero-sub em { color: #b8562f !important; font-style: normal; font-weight: 600; }
    .dr-section-title-wrap { margin-bottom: 18px; }
    .dr-section-title {
        font-family: 'Fraunces', serif; font-size: 28px; font-weight: 700;
        color: #1c1a17 !important; margin: 0; text-align: left; display: inline-block;
        position: relative; padding-bottom: 12px;
    }
    .dr-section-title::after {
        content: ""; position: absolute; left: 0; bottom: 0;
        width: 48px; height: 3px; border-radius: 3px; background: #b8562f;
    }
    .dr-card {
        padding: 24px; border-radius: 16px; background: #ffffff;
        height: 100%; box-sizing: border-box;
        border: 2px solid #ece6dc;
        text-align: center;
    }
    .dr-card b { color: #1c1a17 !important; font-size: 15.5px; }
    .dr-card p { color: #6b6459 !important; }

    /* Stepper cara kerja */
    .dr-stepper-row { display: flex; align-items: center; margin-bottom: 18px; max-width: 640px; margin-left: auto; margin-right: auto; }
    .dr-step-circle {
        width: 46px; height: 46px; border-radius: 50%; background: #b8562f;
        color: #ffffff !important; display: flex; align-items: center; justify-content: center;
        font-weight: 800; font-size: 17px; flex-shrink: 0;
    }
    .dr-step-line { flex: 1; height: 3px; background: #ecddc9; margin: 0 10px; border-radius: 3px; }
    .dr-step-card-1, .dr-step-card-2, .dr-step-card-3 { border-color: #e4ddd0 !important; }

    /* Chip popover (sistem kecil di hero) */
    div[data-testid="stPopover"] button {
        border-radius: 100px !important; background: #f6f1e9 !important;
        border: 1px solid #ecddc9 !important; font-size: 12.5px !important; font-weight: 600 !important;
        color: #5c564d !important; padding: 5px 14px !important; min-height: 0 !important;
    }
    div[data-testid="stPopover"] button:hover {
        background: #ecddc9 !important; color: #8a5a2f !important;
    }

    /* Kartu bulk kategori */
    .dr-bulk-card {
        padding: 22px 24px; border-radius: 16px; background: #fbf8f3;
        border: 2px solid #ece6dc; height: 100%; box-sizing: border-box;
        display: flex; flex-direction: column; align-items: center; text-align: center;
    }
    .dr-bulk-icon {
        width: 44px; height: 44px; border-radius: 12px; background: #fdf3e7;
        display: flex; align-items: center; justify-content: center; margin-bottom: 12px;
        color: #b8562f !important; flex-shrink: 0;
    }
    .dr-bulk-tags-wrap { display: flex; flex-wrap: wrap; justify-content: center; gap: 6px; }
    .dr-bulk-tag {
        display: inline-block; padding: 6px 13px; border-radius: 100px;
        background: #ffffff; border: 1px solid #e4ddd0; color: #1c1a17 !important;
        font-size: 12.5px; font-weight: 600;
    }

    .dr-result-card {
        border: 2px solid #ecddc9; border-radius: 18px; overflow: hidden;
        box-shadow: 0 20px 50px -22px rgba(139,90,47,0.25);
    }
    .dr-result-header {
        padding: 20px 26px; background: #fdf3e7; border-bottom: 2px solid #ecddc9;
        color: #8a5a2f !important; font-family: 'Fraunces', serif;
        font-size: 17px; font-weight: 700;
    }
    .dr-result-header * { color: #8a5a2f !important; }
    .dr-mini-card {
        padding: 16px 18px; border: 1px solid #ecddc9; border-radius: 12px;
        margin-bottom: 12px; background: #fffdf9;
    }
    .dr-mini-card b { color: #1c1a17 !important; }
    .dr-mini-tag {
        display: inline-block; padding: 5px 13px; border-radius: 100px;
        background: #fdf3e7; color: #8a5a2f !important; font-size: 12.5px; font-weight: 700;
        margin-bottom: 8px;
    }
    .dr-mini-label {
        font-size: 12px; font-weight: 700; color: #b8562f !important; text-transform: uppercase;
        letter-spacing: 0.04em; margin-top: 8px; display: block; width: fit-content;
        border-bottom: 2px solid #e4a56e; padding-bottom: 2px;
    }
    .dr-mini-text { font-family: 'Lora', serif; font-size: 13.5px; color: #3a362f !important; line-height: 1.6; margin: 2px 0 0 0; }

    div.stButton > button[kind="primary"] {
        background: #c9683a; color: #ffffff !important; border: 2px solid #c9683a;
        padding: 14px 32px; border-radius: 10px; font-weight: 700; font-size: 18px;
    }
    div.stButton > button[kind="secondary"] {
        background: #ffffff; color: #1c1a17 !important; border: 2px solid #e4ddd0;
        padding: 14px 32px; border-radius: 10px; font-weight: 700; font-size: 18px;
    }
    /* Teks label tombol Streamlit dibungkus <p>, dan aturan global ".stApp p"
       di atas lebih spesifik ke elemen <p> itu sendiri dibanding warna yang
       diset di <button>-nya, jadi warnanya harus dipaksa lagi di sini juga
       (bug yang sama kayak kasus tombol "Mulai Reveal" sebelumnya). */
    div.stButton > button[kind="primary"] p,
    div.stButton > button[kind="primary"] span,
    div.stButton > button[kind="primary"] div {
        color: #ffffff !important;
    }
    div.stButton > button[kind="primary"]:hover { background: #b8562f; border-color: #b8562f; }
    div.stButton > button[kind="secondary"]:hover { border-color: #b8562f; color: #b8562f !important; }

    hr { border-color: #ece6dc !important; }

    /* Streamlit versi ini pakai komponen react-aria-ComboBox untuk selectbox,
       bukan lagi data-baseweb="select" — dua-duanya dipasang biar tahan
       terhadap versi Streamlit yang beda. */
    /* Sama kayak kasus popover/dropdown sebelumnya: tanpa background-color
       dipaksa eksplisit, input-input ini ikut tema dark-mode browser/OS
       (jadi item hitam) alih-alih tema cream/putih situsnya. */
    .stTextInput input, .stDateInput input, .stTimeInput input,
    .stSelectbox div[data-baseweb="select"] > div,
    .stSelectbox [class*="react-aria-ComboBox"] > div {
        border-radius: 8px !important; border-color: #e4ddd0 !important;
        background-color: #ffffff !important; color: #1c1a17 !important;
    }
    .stDateInput input::placeholder, .stTimeInput input::placeholder,
    .stTextInput input::placeholder { color: #9a948a !important; }

    /* Popover pilihan dropdown (listbox-nya sendiri) dirender lewat portal
       terpisah, dibungkus stSelectboxVirtualDropdown — wrapper ini juga
       punya background gelap sendiri yang beda dari listbox di dalamnya,
       jadi kelihatan kayak "bingkai hitam" ngelilingin pilihan. */
    [data-testid="stSelectboxVirtualDropdown"] { background-color: #ffffff !important; }

    /* Teks yang tampil di selectbox sebenarnya dirender oleh <input> di dalam
       react-aria-ComboBox, BUKAN oleh div pembungkusnya. Rule di atas cuma
       ngasih warna ke div pembungkus, jadi teks <input>-nya sendiri masih
       ikut warna default tema (putih di dark-mode) dan nyaru sama background
       putih situs. Dipaksa eksplisit di sini. */
    .stSelectbox input { color: #1c1a17 !important; }

    /* Kolom teks biasa (Email, Nama Lengkap, Kota Lahir) juga sama kasusnya
       kayak Tanggal/Jam Lahir: border yang KELIHATAN itu bukan di <input>,
       tapi di div pembungkus langsung di dalam react-aria-TextField. Tanpa
       dipaksa, border div ini ikut warna gelap tema browser/OS (garis
       hitam/navy). */
    .stTextInput [class*="react-aria-TextField"] > div {
        border-color: #e4ddd0 !important;
        background-color: #ffffff !important;
    }

    /* Tanggal & Jam Lahir sebenarnya bukan <input> polos — nilai yang kelihatan
       dirender lewat span-span react-aria-DateField (per-segmen tahun/bulan/hari
       dan jam/menit). Wrapper aslinya adalah stDateInputField / stTimeInputTimeDisplay,
       bukan .stDateInput input, jadi rule di atas tidak kena ke situ dan wrapper ini
       ikut warna gelap tema browser/OS. Dipaksa eksplisit di sini. */
    [data-testid="stDateInputField"], [data-testid="stTimeInputTimeDisplay"] {
        background-color: #ffffff !important;
        border: 1px solid #e4ddd0 !important;
        border-radius: 8px !important;
    }
    [data-testid="stDateInputField"] span[role="spinbutton"],
    [data-testid="stTimeInputTimeDisplay"] span[role="spinbutton"] {
        color: #1c1a17 !important;
    }
    [data-testid="stDateInputField"] span[data-type="literal"],
    [data-testid="stTimeInputTimeDisplay"] span[data-type="literal"] {
        color: #9a948a !important;
    }

    /* Dropdown bahasa di nav: kecil, cream, border lebih jelas, sejajar tengah dgn logo.
       Bintang kiri-kanan dipasang lewat ::before/::after (dekorasi, dipindah dari
       badge hero yang sudah dihapus) supaya tidak perlu elemen HTML tambahan. */
    .st-key-lang_switch {
        max-width: 100%; width: 100%; margin-left: auto; margin-right: 0;
        position: relative; padding: 0 18px;
    }
    .st-key-lang_switch::before,
    .st-key-lang_switch::after {
        content: "✧"; color: #b8562f; font-size: 13px;
        position: absolute; top: 50%; transform: translateY(-50%);
        line-height: 1;
    }
    .st-key-lang_switch::before { left: 0px; }
    .st-key-lang_switch::after { right: 0px; }
    .st-key-lang_switch [class*="react-aria-ComboBox"] input {
        font-size: 12.5px !important;
        white-space: nowrap !important;
        overflow: visible !important;
        text-overflow: unset !important;
    }
    .st-key-lang_switch div[data-baseweb="select"] > div,
    .st-key-lang_switch [class*="react-aria-ComboBox"] > div {
        background: #fdf3e7 !important; border: 1.5px solid #e4a56e !important;
        border-radius: 100px !important; color: #8a5a2f !important;
        min-height: 40px !important; font-weight: 700 !important;
        box-shadow: 0 1px 3px rgba(184,86,47,0.08) !important;
        min-width: 0 !important;
    }
    .st-key-lang_switch [class*="react-aria-ComboBox"] input {
        color: #8a5a2f !important; font-weight: 700 !important; background: transparent !important;
        min-width: 0 !important;
    }
    .st-key-lang_switch div[data-baseweb="select"] > div:hover,
    .st-key-lang_switch [class*="react-aria-ComboBox"] > div:hover {
        border-color: #b8562f !important;
    }
    .st-key-lang_switch svg { fill: #8a5a2f !important; }

    /* Daftar opsi dropdown (portal terpisah) — paksa terang, ikut dark-mode
       kalau tidak dipaksa, sama seperti kasus panel popover */
    div[role="listbox"] {
        background-color: #ffffff !important;
        border: 1.5px solid #ecddc9 !important;
        border-radius: 12px !important;
        overflow: hidden !important;
        box-shadow: 0 12px 30px -10px rgba(28,26,23,0.18) !important;
    }
    div[role="listbox"] * { color: #1c1a17 !important; }
    div[role="listbox"] [role="option"] { background-color: #ffffff !important; }
    div[role="listbox"] [role="option"]:hover,
    div[role="listbox"] [aria-selected="true"] { background-color: #fdf3e7 !important; }

    /* Nav: sejajarkan logo & dropdown bahasa secara vertikal */
    .st-key-nav_row [data-testid="stHorizontalBlock"] { align-items: center !important; }

    /* Kontainer Contoh Laporan lebih compact */
    .dr-report-grid { display: grid; grid-template-columns: repeat(2, minmax(0,1fr)); gap: 12px; }
    .dr-report-item { padding: 4px 0; border-bottom: 1px solid #f2ecdf; }
    .dr-report-item:nth-last-child(-n+2) { border-bottom: none; }

    /* Tab (Beranda / Preview Form + Global / Mingguan) jadi pill nav modern */
    [data-testid="stTabs"] [data-baseweb="tab-list"] {
        gap: 10px !important; background: #fbf8f3; padding: 8px; border-radius: 100px;
        border: 1px solid #ece6dc; display: inline-flex !important; width: auto !important;
    }
    [data-testid="stTabs"] button[role="tab"] {
        border: 1.5px solid transparent !important;
        border-radius: 100px !important;
        padding: 10px 24px !important;
        font-size: 14.5px !important;
        font-weight: 700 !important;
        color: #6b6459 !important;
        background: transparent !important;
        transition: all 0.15s ease;
    }
    [data-testid="stTabs"] button[role="tab"] p { font-weight: 700 !important; }
    [data-testid="stTabs"] button[role="tab"]:hover {
        border-color: #ecddc9 !important; color: #b8562f !important;
    }
    [data-testid="stTabs"] button[role="tab"][aria-selected="true"] {
        border-color: #b8562f !important;
        background: #ffffff !important;
        color: #b8562f !important;
        box-shadow: 0 0 0 3px rgba(184,86,47,0.12), 0 4px 14px -4px rgba(184,86,47,0.35);
    }
    [data-testid="stTabs"] [data-baseweb="tab-highlight"] { display: none; }
    [data-testid="stTabs"] [data-baseweb="tab-border"] { display: none; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ── Data sistem lengkap (buat popover chip) — urut abjad ────
# format: (nama, icon_material, apa_ini, [topik yang bisa diketahui], kalimat_ajakan, aktif)
SEMUA_SISTEM = [
    ("BaZi", "account_tree",
     "Sistem astrologi Tiongkok kuno yang membaca empat pilar waktu lahir, yaitu tahun, bulan, tanggal, dan jam, untuk memetakan struktur nasib seseorang secara mendalam.",
     ["Elemen dominan dalam diri", "Potensi rezeki dan karier", "Periode hidup yang perlu diperhatikan"],
     "Banyak yang baru sadar polanya justru dari sisi yang paling sering diabaikan, yaitu jam lahir.", False),
    ("Big Five", "insights",
     "Model kepribadian yang paling banyak divalidasi dalam riset psikologi modern, mengukur lima dimensi utama karakter seseorang secara terukur.",
     ["Tingkat keterbukaan terhadap hal baru", "Cara mengelola emosi", "Gaya bekerja sama dengan orang lain"],
     "Cocok buat kamu yang ingin memahami diri lewat data, bukan sekadar label kepribadian.", False),
    ("DISC", "groups",
     "Model perilaku kerja yang memetakan bagaimana seseorang berkomunikasi, mengambil keputusan, dan merespons tekanan di lingkungan profesional.",
     ["Gaya komunikasi di tempat kerja", "Cara mengambil keputusan", "Reaksi terhadap tekanan"],
     "Sering dipakai perusahaan untuk proses rekrutmen, sekarang kamu bisa coba versi personalnya sendiri.", False),
    ("Enneagram", "category",
     "Sistem sembilan tipe kepribadian yang menelusuri motivasi inti dan ketakutan terdalam di balik setiap perilaku seseorang.",
     ["Motivasi tersembunyi di balik tindakan", "Ketakutan yang memengaruhi pilihan", "Arah berkembang jadi versi terbaik diri"],
     "Kalau kamu sering bertanya kenapa selalu bereaksi dengan cara yang sama, jawabannya mungkin ada di sini.", False),
    ("Golongan Darah", "bloodtype",
     "Pembacaan sifat berdasarkan golongan darah, populer di budaya Jepang dan Korea sebagai cara memahami kecenderungan dasar seseorang.",
     ["Kecenderungan sifat bawaan", "Cara menghadapi masalah", "Kecocokan dengan golongan darah lain"],
     "Terdengar sederhana, tapi banyak orang justru merasa gambarannya paling mengena.", False),
    ("Human Design", "hub",
     "Sistem yang memetakan tipe energi bawaan dan cara alami seseorang dalam mengambil keputusan yang selaras dengan dirinya.",
     ["Tipe energi alami", "Cara terbaik mengambil keputusan", "Peran dalam kelompok atau tim"],
     "Cocok buat kamu yang lelah memaksakan cara kerja orang lain ke dalam ritme hidupmu sendiri.", False),
    ("Love Language", "favorite",
     "Konsep lima bahasa kasih yang menjelaskan cara seseorang paling nyaman menerima dan menyampaikan perhatian dalam suatu hubungan.",
     ["Cara paling nyaman menerima kasih sayang", "Cara menyampaikan perhatian ke orang lain", "Potensi kesalahpahaman dalam hubungan"],
     "Pahami ini, dan komunikasi dengan orang terdekatmu bisa terasa jauh lebih lancar.", False),
    ("Matrix Destiny", "grid_view",
     "Peta numerologi menyeluruh dari tanggal lahir yang menggambarkan kepribadian, arah rezeki, hubungan, dan pelajaran hidup sekaligus dalam satu diagram.",
     ["Peta kepribadian menyeluruh", "Arah rezeki dan keuangan", "Pelajaran hidup yang dibawa sejak lahir"],
     "Satu peta yang merangkum hampir semua sisi hidupmu hanya dari satu tanggal lahir.", False),
    ("MBTI", "psychology",
     "Salah satu tes kepribadian paling dikenal secara global, membagi cara berpikir dan bekerja seseorang ke dalam enam belas tipe.",
     ["Gaya berpikir dan memproses informasi", "Cara bekerja yang paling efektif", "Kecocokan dengan tipe kepribadian lain"],
     "Tes yang paling sering jadi bahan obrolan, sekarang saatnya lihat versi yang lebih lengkap.", False),
    ("Numerologi", "tag",
     "Ilmu penafsiran angka dari tanggal lahir dan nama untuk membaca arah hidup dan pola yang berulang pada diri seseorang.",
     ["Jalan hidup utama", "Angka keberuntungan pribadi", "Tantangan yang cenderung berulang"],
     "Angka lahir dan namamu ternyata menyimpan pola yang jarang disadari sebelumnya.", False),
    ("Shio", "pets",
     "Astrologi Tiongkok berdasarkan siklus dua belas hewan yang menggambarkan sifat, elemen bawaan, dan peruntungan tahunan seseorang.",
     ["Sifat dan elemen bawaan lahir", "Peruntungan tahun berjalan", "Kecocokan dengan shio lain"],
     "Dipercaya turun-temurun, tapi jarang dibaca sampai ke elemen dan peruntungan tahunannya.", False),
    ("Tarot", "style",
     "Pembacaan simbolis melalui kartu yang merepresentasikan arketipe jiwa dan pelajaran hidup yang sedang dijalani seseorang saat ini.",
     ["Arketipe jiwa yang mewakili dirimu", "Pelajaran hidup yang sedang dijalani", "Energi yang sedang berlangsung"],
     "Bukan soal menebak masa depan, tapi mengenali energi yang sedang kamu jalani sekarang.", False),
    ("Weton", "calendar_today",
     "Perhitungan tradisi Jawa yang menggabungkan hari kelahiran dan siklus pasaran untuk membaca watak bawaan dan hari baik.",
     ["Watak bawaan lahir menurut tradisi Jawa", "Hari baik untuk momen penting", "Neptu dan maknanya"],
     "Sistem asli Indonesia yang masih dipakai untuk menentukan hari baik sampai sekarang.", False),
    ("Zi Wei", "auto_awesome",
     "Astrologi bintang ungu dari Tiongkok yang memetakan dua belas istana kehidupan berdasarkan posisi bintang saat lahir.",
     ["Peta dua belas istana kehidupan", "Potensi karier dan jodoh", "Periode baik dalam siklus hidup"],
     "Lebih detail dibanding astrologi Barat, karena memetakan dua belas sisi kehidupan sekaligus.", False),
    ("Zodiak", "star",
     "Astrologi Barat yang membaca karakter dasar seseorang dari posisi matahari terhadap salah satu dari dua belas rasi bintang saat lahir.",
     ["Karakter dasar dan elemen", "Gaya emosi dan cara merespons", "Kecocokan dengan zodiak lain"],
     "Sistem yang paling familiar, tapi baru terasa lengkap kalau digabung dengan sistem lain.", True),
]

# ── NAVIGASI HALAMAN ────────────────────────────────────────
# Bukan st.tabs — st.tabs nggak bisa dipindah programatis lewat klik tombol
# lain (misal tombol "Mulai Reveal" di hero). Jadi navigasi antar
# "halaman" (Beranda / Reveal Yourself) dipegang manual lewat
# st.session_state, dan konten dirender bergantian pakai if/else biasa.
if "dr_page" not in st.session_state:
    st.session_state.dr_page = "home"

# ── NAV BAR ──────────────────────────────────────────────────
with st.container(key="nav_row"):
    nav_l, nav_home_btn, nav_reveal_btn, nav_r = st.columns([2.7, 1.3, 1.7, 1.9])
    with nav_l:
        st.markdown(
            '<div style="font-family:\'Fraunces\',serif;font-size:28px;font-weight:700;'
            'color:#1c1a17;letter-spacing:-0.01em;">✨ Destiny Reveal</div>',
            unsafe_allow_html=True,
        )
    with nav_home_btn:
        if st.button(
            "Home", key="nav_btn_home", icon=":material/home:",
            type="primary" if st.session_state.dr_page == "home" else "secondary",
            use_container_width=True,
        ):
            st.session_state.dr_page = "home"
            st.rerun()
    with nav_reveal_btn:
        if st.button(
            "Reveal Yourself", key="nav_btn_reveal", icon=":material/auto_awesome:",
            type="primary" if st.session_state.dr_page == "reveal" else "secondary",
            use_container_width=True,
        ):
            st.session_state.dr_page = "reveal"
            st.rerun()
    with nav_r:
        with st.container(key="lang_switch"):
            st.selectbox("Bahasa", ["🇮🇩 Indonesian", "🇬🇧 English"], label_visibility="collapsed")

st.markdown("<hr style='margin-top:14px;'>", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# HALAMAN — BERANDA
# ══════════════════════════════════════════════════════════════
if st.session_state.dr_page == "home":

    # ── HERO ─────────────────────────────────────────────────
    st.markdown('<div class="dr-hero-title">Ada Banyak Versi Dirimu yang Belum Kamu Kenal.</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="dr-hero-sub">'
        'Masa lalu sudah menjadi pelajaran, saatnya kenali dirimu sepenuhnya sebelum melangkah ke depan.<br>'
        '<em>Satu pembacaan lengkap</em> dari 15 sistem ini akan menunjukkan potensi, kelebihan, kelemahan, '
        'dan langkah yang sebaiknya kamu ambil.'
        '</div>',
        unsafe_allow_html=True,
    )

    col_a, col_b, col_r = st.columns([1.3, 1.3, 2.4])
    with col_a:
        if st.button("Mulai Reveal", key="cta_hero", type="primary", icon=":material/bolt:", use_container_width=True):
            st.session_state.dr_page = "reveal"
            st.rerun()

    st.write("")
    st.markdown('<p style="font-size:12.5px;color:#9a948a !important;margin-bottom:6px;">Klik tiap sistem untuk melihat penjelasannya:</p>', unsafe_allow_html=True)

    n_per_row = 5
    for i in range(0, len(SEMUA_SISTEM), n_per_row):
        chunk = SEMUA_SISTEM[i:i + n_per_row]
        cols = st.columns(n_per_row)
        for col, (nama, icon, apa_ini, topik_list, ajakan, aktif) in zip(cols, chunk):
            with col:
                with st.popover(nama, use_container_width=True, icon=f":material/{icon}:"):
                    status_badge = "Sudah aktif" if aktif else "Segera hadir"
                    status_color = "#8a5a2f" if aktif else "#9a948a"
                    st.markdown(
                        f'<p style="font-size:11px;font-weight:700;letter-spacing:0.06em;'
                        f'text-transform:uppercase;color:{status_color} !important;margin-bottom:6px;">{status_badge}</p>',
                        unsafe_allow_html=True,
                    )
                    st.markdown(f"**{nama}**")
                    st.write(apa_ini)
                    st.markdown(
                        '<p style="font-size:12.5px;font-weight:700;color:#3a362f !important;margin:14px 0 4px 0;">Bisa bantu kamu tahu:</p>',
                        unsafe_allow_html=True,
                    )
                    for topik in topik_list:
                        st.markdown(
                            f'<p style="font-size:13px;color:#3a362f !important;margin:2px 0;">'
                            f'<span style="color:#b8562f !important;">•</span> {topik}</p>',
                            unsafe_allow_html=True,
                        )
                    st.markdown(
                        f'<p style="font-size:12.5px;color:#8a5a2f !important;font-style:italic;'
                        f'margin:14px 0 0 0;padding-top:10px;border-top:1px solid #ecddc9;">{ajakan}</p>',
                        unsafe_allow_html=True,
                    )

    st.write("")

    # ── CARA KERJA ───────────────────────────────────────────
    st.markdown('<div class="dr-section-title-wrap"><span class="dr-section-title">Tiga Langkah, Tanpa Ribet</span></div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="dr-stepper-row">
            <div class="dr-step-circle">1</div>
            <div class="dr-step-line"></div>
            <div class="dr-step-circle">2</div>
            <div class="dr-step-line"></div>
            <div class="dr-step-circle">3</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns(3, gap="medium")
    steps = [
        (":material/mail:", "Verifikasi Email", "Masukkan email, dapat kode verifikasi. Tanpa akun atau password.", "dr-step-card-1"),
        (":material/auto_awesome:", "Pilih Mode & Diproses", "Pilih fokus eksplorasimu, data lain ditanya pelan-pelan sambil diproses.", "dr-step-card-2"),
        (":material/visibility:", "Buka Hasil Lengkap", "Laporan lengkap langsung terbuka & dikirim ke email kamu.", "dr-step-card-3"),
    ]
    for idx, (col, (icon, title, desc, cls)) in enumerate(zip([c1, c2, c3], steps)):
        with col:
            with st.container(key=f"drfillheight_step{idx}"):
                st.markdown(
                    f"""<div class="dr-card {cls}">
                        <b>{title}</b>
                        <p style="font-size:13.5px;margin-top:8px;line-height:1.6;">{desc}</p>
                    </div>""",
                    unsafe_allow_html=True,
                )

    st.write("")

    # ── SATU DATA, BANYAK CARA PANDANG ────────────────────────
    st.markdown('<div class="dr-section-title-wrap"><span class="dr-section-title">Satu Data, Banyak Cara Pandang</span></div>', unsafe_allow_html=True)

    bulk_groups = [
        ("calendar_month", "Cuma dari Tanggal Lahir", ["Zodiak", "Shio", "Weton", "Numerologi", "Matrix Destiny"]),
        ("schedule", "+ Tambah Jam Lahir", ["BaZi (4 Pilar)", "Zi Wei Dou Shu", "Human Design", "Ascendant Zodiak"]),
        ("location_on", "+ Tambah Kota Lahir", ["BaZi Akurat Penuh", "Human Design Akurat Penuh"]),
        ("quiz", "Kuesioner Terpisah", ["MBTI", "Big Five", "Enneagram", "DISC", "Golongan Darah", "Love Language"]),
    ]
    bcols = st.columns(4, gap="medium")
    for idx, (col, (icon, title, items)) in enumerate(zip(bcols, bulk_groups)):
        with col:
            with st.container(key=f"drfillheight_bulk{idx}"):
                tags_html = "".join(f'<span class="dr-bulk-tag">{x}</span>' for x in items)
                st.markdown(
                    f"""<div class="dr-bulk-card">
                        <div class="dr-bulk-icon"><span class="material-symbols-outlined">{icon}</span></div>
                        <b style="font-size:14.5px;">{title}</b>
                        <div class="dr-bulk-tags-wrap" style="margin-top:10px;">{tags_html}</div>
                    </div>""",
                    unsafe_allow_html=True,
                )

    st.write("")

    # ── CTA PENUTUP ──────────────────────────────────────────
    # Sengaja tanpa st.write("") kosong di sini — tiap st.write("") nambah
    # elemen container-nya sendiri, dan gap antar stVerticalBlock (1rem) ikut
    # kekali tiap ada elemen kosong tambahan, jadi jaraknya membengkak jauh
    # lebih besar dari yang kelihatan di kode. Jarak sekarang cuma diatur
    # lewat margin di <hr>-nya sendiri.
    st.markdown("<hr style='margin-top:4px;margin-bottom:20px;'>", unsafe_allow_html=True)
    st.markdown('<div class="dr-center"><span class="dr-section-title">Penasaran Sama Dirimu Sendiri?</span></div>', unsafe_allow_html=True)
    st.markdown(
        '<p class="dr-center" style="color:#6b6459 !important;font-size:15px;margin-bottom:22px;">Mulai sekarang, hasil pertama muncul dalam hitungan menit.</p>',
        unsafe_allow_html=True,
    )
    cta_l, cta_mid, cta_r = st.columns([1.5, 1.4, 1.5])
    with cta_mid:
        if st.button("Mulai Reveal Gratis", key="cta_footer", type="primary", icon=":material/arrow_forward:", use_container_width=True):
            st.session_state.dr_page = "reveal"
            st.rerun()

    st.write("")
    st.markdown(
        '<p class="dr-footer-copyright">© 2026 Destiny Reveal '
        '<span class="dr-footer-byline">· By Zio</span></p>',
        unsafe_allow_html=True,
    )

# ══════════════════════════════════════════════════════════════
# HALAMAN — REVEAL YOURSELF (Verifikasi Email + Pilih Mode)
# ══════════════════════════════════════════════════════════════
elif st.session_state.dr_page == "reveal":
    render_reveal_yourself()

# ══════════════════════════════════════════════════════════════
# HALAMAN — LOADING (proses per-titik, floating window minta data)
# ══════════════════════════════════════════════════════════════
elif st.session_state.dr_page == "loading":
    render_loading()

# ══════════════════════════════════════════════════════════════
# HALAMAN — HASIL AKHIR (stub, belum dibuat penuh)
# ══════════════════════════════════════════════════════════════
else:
    render_result()
