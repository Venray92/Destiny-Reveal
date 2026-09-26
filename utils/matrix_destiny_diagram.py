"""
Bikin SVG octagram (bintang 8 titik) buat Matrix Destiny — dua kotak yang
saling tumpang tindih (Personal Square A/B/C/D + Ancestral Square F/G/H/I)
ditambah Titik Pusat (E), persis strukturnya kayak matrix-destiny.com, TAPI
warna & palet beda (dipakai warna coklat/krem khas app ini, bukan biru-emas
mistis) — sesuai permintaan Stev biar nggak dianggap menjiplak.

8 titik ditaruh di lingkaran (urutan searah jarum jam mulai dari atas,
sesuai usia): A(0) - F(10) - B(20) - G(30) - C(40) - I(50) - D(60) - H(70).
Personal Square (A-B-C-D, tiap 90°) dan Ancestral Square (F-G-H-I, tiap
90°, digeser 45° dari Personal Square) digambar sebagai 2 kotak terpisah
biar kelihatan strukturnya, baru dua-duanya nyambung ke titik tengah (E)
lewat garis tipis putus-putus.

Label diposisikan lewat sudut (theta) yang sama kayak titiknya, BUKAN cuma
nge-scale koordinat x/y titik — biar jaraknya ke tiap titik konsisten &
nggak ketiban/kepotong viewBox di titik kiri-kanan (0°/180°), yang sempat
kejadian di revisi pertama.
"""

import math

_WARNA_PERSONAL = "#b8562f"   # coklat utama app — kotak Personal Square (A,B,C,D)
_WARNA_ANCESTRAL = "#c9a227"  # emas app (senada gradient kartu) — Ancestral Square (F,G,H,I)
_WARNA_SPOKE = "#e4ddd0"      # garis tipis ke titik tengah
_WARNA_TEKS = "#1c1a17"
_WARNA_LABEL = "#8a7f6d"

# (kode, usia, label singkat -- sengaja pendek biar muat di samping titik)
_TITIK_URUTAN = [
    ("a", 0, "Karakter"),
    ("f", 10, "Kakek (Ibu)"),
    ("b", 20, "Spiritual"),
    ("g", 30, "Kakek (Ayah)"),
    ("c", 40, "Material"),
    ("i", 50, "Nenek (Ayah)"),
    ("d", 60, "Karma"),
    ("h", 70, "Nenek (Ibu)"),
]


def _theta(idx, total):
    # idx=0 di jam 12 (atas), searah jarum jam.
    return -math.pi / 2 + idx * (2 * math.pi / total)


def _anchor_untuk(theta):
    cos_t = math.cos(theta)
    if cos_t > 0.35:
        return "start"
    if cos_t < -0.35:
        return "end"
    return "middle"


def render_octagram_svg(personal_square: dict, ancestral_square: dict, width: int = 520) -> str:
    """
    Args:
        personal_square: {"a","b","c","d","e"} dari hitung_matrix_destiny()
        ancestral_square: {"f","g","h","i"} dari hitung_matrix_destiny()

    Returns:
        str: markup <svg> siap ditaruh di st.markdown(unsafe_allow_html=True)
    """
    size = width
    cx = cy = size / 2
    r = size * 0.27
    r_point = size * 0.045
    r_label = r + r_point + size * 0.035

    titik_nilai = dict(personal_square)
    titik_nilai.update(ancestral_square)

    total = len(_TITIK_URUTAN)
    posisi = {}
    theta_map = {}
    for idx, (kode, _usia, _label) in enumerate(_TITIK_URUTAN):
        th = _theta(idx, total)
        theta_map[kode] = th
        posisi[kode] = (cx + r * math.cos(th), cy + r * math.sin(th))

    parts = [
        f'<svg viewBox="0 0 {size} {size}" width="100%" height="auto" '
        f'style="max-width:{size}px;display:block;margin:0 auto;">'
    ]

    # Spokes ke titik tengah (digambar dulu biar ketutup sama kotak & titik)
    for kode in titik_nilai:
        if kode == "e":
            continue
        x, y = posisi[kode]
        parts.append(
            f'<line x1="{cx:.1f}" y1="{cy:.1f}" x2="{x:.1f}" y2="{y:.1f}" '
            f'stroke="{_WARNA_SPOKE}" stroke-width="1.2" stroke-dasharray="3,4" />'
        )

    # Personal Square (A-B-C-D)
    pa, pb, pc, pd = posisi["a"], posisi["b"], posisi["c"], posisi["d"]
    parts.append(
        f'<polygon points="{pa[0]:.1f},{pa[1]:.1f} {pb[0]:.1f},{pb[1]:.1f} '
        f'{pc[0]:.1f},{pc[1]:.1f} {pd[0]:.1f},{pd[1]:.1f}" '
        f'fill="none" stroke="{_WARNA_PERSONAL}" stroke-width="2.4" />'
    )
    # Ancestral Square (F-G-I-H) — urutan diagonal sesuai posisi di lingkaran
    pf, pg, pi_, ph = posisi["f"], posisi["g"], posisi["i"], posisi["h"]
    parts.append(
        f'<polygon points="{pf[0]:.1f},{pf[1]:.1f} {pg[0]:.1f},{pg[1]:.1f} '
        f'{pi_[0]:.1f},{pi_[1]:.1f} {ph[0]:.1f},{ph[1]:.1f}" '
        f'fill="none" stroke="{_WARNA_ANCESTRAL}" stroke-width="2.4" />'
    )

    # Titik tengah (E)
    parts.append(
        f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r_point + 6:.1f}" '
        f'fill="#fff8ef" stroke="{_WARNA_PERSONAL}" stroke-width="2.4" />'
    )
    parts.append(
        f'<text x="{cx:.1f}" y="{cy + 5:.1f}" text-anchor="middle" '
        f'font-family="Fraunces, serif" font-weight="700" font-size="15" '
        f'fill="{_WARNA_TEKS}">{titik_nilai["e"]}</text>'
    )

    # 8 titik keliling + nilai
    for kode, usia, label in _TITIK_URUTAN:
        x, y = posisi[kode]
        warna = _WARNA_PERSONAL if kode in ("a", "b", "c", "d") else _WARNA_ANCESTRAL
        parts.append(
            f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r_point:.1f}" '
            f'fill="#ffffff" stroke="{warna}" stroke-width="2.2" />'
        )
        parts.append(
            f'<text x="{x:.1f}" y="{y + 4.5:.1f}" text-anchor="middle" '
            f'font-family="Fraunces, serif" font-weight="700" font-size="13" '
            f'fill="{_WARNA_TEKS}">{titik_nilai[kode]}</text>'
        )

    # Label (usia + keterangan) DIPISAH dari loop titik, dihitung dari
    # theta yang sama tapi radius lebih jauh (r_label) -- jaraknya ke tiap
    # titik jadi konsisten, dan anchor teks disesuaikan arah (kiri/kanan/
    # tengah) biar nggak kepotong tepi SVG atau numpuk sama lingkaran titik.
    for idx, (kode, usia, label) in enumerate(_TITIK_URUTAN):
        th = theta_map[kode]
        lx = cx + r_label * math.cos(th)
        ly = cy + r_label * math.sin(th)
        anchor = _anchor_untuk(th)
        parts.append(
            f'<text x="{lx:.1f}" y="{ly:.1f}" text-anchor="{anchor}" '
            f'font-family="Inter, sans-serif" font-size="10.5" font-weight="700" '
            f'fill="{_WARNA_LABEL}">USIA {usia}</text>'
        )
        parts.append(
            f'<text x="{lx:.1f}" y="{ly + 13:.1f}" text-anchor="{anchor}" '
            f'font-family="Inter, sans-serif" font-size="9.5" '
            f'fill="{_WARNA_LABEL}">{label}</text>'
        )

    parts.append("</svg>")
    return "".join(parts)


def _tip_align(theta):
    """
    Nentuin arah bukaan tooltip (bukan text-anchor label) -- KEBALIKAN
    dari _anchor_untuk, soalnya tujuannya beda: label boleh nyembur keluar
    kotak (menjauhi tengah), tapi tooltip harus tetep di DALAM lebar
    kontainer, jadi titik yang deket tepi kanan tooltip-nya harus mekar
    ke KIRI (bukan ke kanan), begitu juga sebaliknya.
    """
    cos_t = math.cos(theta)
    if cos_t > 0.35:
        return "md-align-left"   # titik di sisi kanan -> tooltip mekar ke kiri
    if cos_t < -0.35:
        return "md-align-right"  # titik di sisi kiri -> tooltip mekar ke kanan
    return "md-align-mid"


def _hover_zone_html(x_pct, y_pct, zone_px, align_class, info):
    label = info.get("label", "")
    nilai = info.get("nilai", "")
    arti = info.get("arti", "")
    judul = f"{label} &middot; Angka {nilai}" if label else f"Angka {nilai}"
    return (
        f'<div class="md-hz {align_class}" '
        f'style="left:{x_pct:.2f}%;top:{y_pct:.2f}%;width:{zone_px:.0f}px;height:{zone_px:.0f}px;">'
        '<div class="md-tip">'
        f'<span class="md-tip-title">{judul}</span>'
        f'<span class="md-tip-body">{arti}</span>'
        '</div></div>'
    )


def render_octagram_svg_with_tooltips(personal_square: dict, ancestral_square: dict,
                                       tooltip_info: dict, width: int = 520) -> str:
    """
    Sama kayak render_octagram_svg(), TAPI ditambah layer "hover zone"
    transparan tepat di atas tiap titik (posisinya dihitung ulang pakai
    theta yang SAMA biar presisi nempel), isinya tooltip custom (bukan
    tooltip bawaan browser) yang muncul lewat CSS :hover.

    Args:
        tooltip_info: dict {kode_titik: {"label": str, "nilai": int, "arti": str}}
                      buat 9 kode (a,b,c,d,e,f,g,h,i). Kalau salah satu kode
                      nggak ada di dict, hover zone-nya tetap dibikin tapi
                      isi tooltip-nya cuma nampilin nilai angkanya doang.

    Returns:
        str: markup gabungan (div wrapper + svg + hover zones), siap ditaruh
        di st.markdown(unsafe_allow_html=True). CSS-nya (.md-diagram-wrap,
        .md-hz, .md-tip, dst) ditaruh terpisah di _inject_style() halaman
        yang makai, BUKAN di sini, biar palet warnanya gampang disesuaikan
        per-halaman tanpa ubah file ini.
    """
    svg = render_octagram_svg(personal_square, ancestral_square, width=width)

    size = width
    cx = cy = size / 2
    r = size * 0.27
    r_point = size * 0.045
    zone_px = max(r_point * 2 + 16, 30)

    titik_nilai = dict(personal_square)
    titik_nilai.update(ancestral_square)

    total = len(_TITIK_URUTAN)
    zones_html = []
    for idx, (kode, _usia, label) in enumerate(_TITIK_URUTAN):
        th = _theta(idx, total)
        x_pct = (cx + r * math.cos(th)) / size * 100
        y_pct = (cy + r * math.sin(th)) / size * 100
        info = dict(tooltip_info.get(kode, {}))
        info.setdefault("label", label)
        info.setdefault("nilai", titik_nilai.get(kode, "-"))
        zones_html.append(_hover_zone_html(x_pct, y_pct, zone_px, _tip_align(th), info))

    # Titik pusat (E) -- selalu di tengah persis (50%, 50%), tooltip dibuka
    # ke BAWAH (bukan ngikut aturan atas/bawah default) biar nggak numpuk
    # sama titik-titik lain yang posisinya di atas dia.
    info_e = dict(tooltip_info.get("e", {}))
    info_e.setdefault("label", "Titik Pusat (Inti Jiwa)")
    info_e.setdefault("nilai", titik_nilai.get("e", "-"))
    zones_html.append(_hover_zone_html(50.0, 50.0, r_point * 2 + 18, "md-align-mid md-center", info_e))

    return (
        '<div class="md-diagram-wrap">'
        f'{svg}'
        f'{"".join(zones_html)}'
        '</div>'
    )
