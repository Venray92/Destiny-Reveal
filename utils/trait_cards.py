"""Kartu share Career DNA & Strength/Blind Spot (PNG 1080x1350, Pillow) + watermark "By Destiny Reveal"."""

import io
import math
import textwrap

from PIL import Image, ImageDraw, ImageFont

from utils.watermark import add_watermark

W, H = 1080, 1350
_SERIF_B = ["DejaVuSerif-Bold.ttf", "DejaVuSerif.ttf"]
_SERIF = ["DejaVuSerif.ttf"]
_SANS_B = ["DejaVuSans-Bold.ttf", "DejaVuSans.ttf"]
_SANS = ["DejaVuSans.ttf"]
INK, ACC, MUTE = (45, 42, 38), (201, 98, 52), (139, 131, 120)


def _f(names, size):
    for n in names:
        try:
            return ImageFont.truetype(n, size)
        except OSError:
            continue
    return ImageFont.load_default()


def _base(judul):
    img = Image.new("RGB", (W, H), (255, 244, 226))
    d = ImageDraw.Draw(img)
    for y in range(H):
        t = y / (H - 1)
        d.line([(0, y), (W, y)], fill=tuple(round(a + (b - a) * t) for a, b in zip((255, 244, 226), (246, 214, 178))))
    d.rounded_rectangle((48, 48, W - 48, H - 48), radius=36, outline=ACC, width=3)
    _c(d, 100, judul, _f(_SANS_B, 30), ACC)
    return img, d


def _c(d, y, text, font, fill):
    d.text(((W - d.textlength(text, font=font)) / 2, y), text, font=font, fill=fill)


def _out(img):
    buf = io.BytesIO()
    add_watermark(img, bottom=80, pad=90).convert("RGB").save(buf, format="PNG")
    return buf.getvalue()


def kartu_karier(nama, code, arketipe, rel, peran):
    img, d = _base("CAREER DNA")
    _c(d, 150, nama, _f(_SERIF, 30), MUTE)
    _c(d, 215, code, _f(_SERIF_B, 120), INK)
    _c(d, 360, arketipe, _f(_SERIF_B, 40), ACC)
    cx, cy, R = W // 2, 700, 190
    L = list("RIASEC")
    for k in (0.33, 0.66, 1.0):
        d.polygon([(cx + R * k * math.sin(i * math.pi / 3), cy - R * k * math.cos(i * math.pi / 3)) for i in range(6)],
                  outline=(226, 205, 180), width=2)
    pts = [(cx + R * rel[l] / 100 * math.sin(i * math.pi / 3), cy - R * rel[l] / 100 * math.cos(i * math.pi / 3)) for i, l in enumerate(L)]
    d.polygon(pts, fill=(224, 140, 96), outline=ACC, width=4)
    for i, l in enumerate(L):
        x, y = cx + (R + 48) * math.sin(i * math.pi / 3), cy - (R + 48) * math.cos(i * math.pi / 3)
        d.text((x - 12, y - 18), l, font=_f(_SANS_B, 34), fill=INK)
    _c(d, 985, "PERAN YANG COCOK", _f(_SANS_B, 26), ACC)
    y = 1035
    for p in peran[:4]:
        for ln in textwrap.wrap(p, 34)[:1]:
            _c(d, y, "• " + ln, _f(_SERIF, 34), INK)
        y += 52
    return _out(img)


def kartu_kekuatan(nama, tags, blind):
    img, d = _base("STRENGTH & BLIND SPOT")
    _c(d, 150, nama, _f(_SERIF, 30), MUTE)
    _c(d, 230, "KEKUATANKU", _f(_SANS_B, 28), ACC)
    y = 290
    for t in tags[:4]:
        _c(d, y, t, _f(_SERIF_B, 44), INK)
        y += 72
    d.line([(W / 2 - 60, y + 20), (W / 2 + 60, y + 20)], fill=ACC, width=3)
    y += 70
    _c(d, y, "TITIK BUTAKU", _f(_SANS_B, 28), ACC)
    y += 60
    for b in blind[:3]:
        for ln in textwrap.wrap(b, 34)[:2]:
            _c(d, y, ln, _f(_SERIF, 38), (80, 72, 64))
            y += 54
        y += 18
    return _out(img)


def kartu_keputusan(nama_a, nama_b, skor_a, skor_b, unggul, arah):
    """Kartu share Decision Reveal. skor -6..6. unggul 'A'/'B'/None."""
    img, d = _base("DECISION REVEAL")
    _c(d, 150, "Tebaran 7 kartu", _f(_SERIF, 30), MUTE)
    top = {"A": "Condong ke A", "B": "Condong ke B", None: "Seimbang"}[unggul]
    _c(d, 230, top, _f(_SERIF_B, 70), ACC)
    y = 400
    for lab, nm, sk in (("A", nama_a, skor_a), ("B", nama_b, skor_b)):
        on = unggul == lab
        d.rounded_rectangle((120, y, W - 120, y + 190), radius=28, fill=(255, 255, 255) if on else (250, 236, 218),
                            outline=ACC if on else (226, 205, 180), width=4 if on else 2)
        d.text((160, y + 28), f"PILIHAN {lab}", font=_f(_SANS_B, 26), fill=ACC)
        d.text((160, y + 72), textwrap.shorten(nm or f"Pilihan {lab}", 24, placeholder="…"), font=_f(_SERIF_B, 44), fill=INK)
        frac = (sk + 6) / 12
        d.rounded_rectangle((160, y + 142, W - 160, y + 158), radius=8, fill=(240, 226, 208))
        d.rounded_rectangle((160, y + 142, 160 + (W - 320) * frac, y + 158), radius=8, fill=ACC)
        y += 230
    _c(d, 900, "ARAH SARAN 7 HARI", _f(_SANS_B, 26), ACC)
    yy = 950
    for ln in textwrap.wrap(arah, 38)[:4]:
        _c(d, yy, ln, _f(_SERIF, 34), INK)
        yy += 50
    return _out(img)


def kartu_tahunan(nama, year, shio_kamu, shio_tahun, rel_label, skor, tier, terbaik, terjaga, kurva):
    """Kartu share Yearly Forecast. kurva = 12 skor."""
    img, d = _base(f"YEARLY FORECAST {year}")
    _c(d, 150, nama, _f(_SERIF, 30), MUTE)
    _c(d, 220, f"{shio_kamu} × {shio_tahun}", _f(_SERIF_B, 64), INK)
    _c(d, 310, rel_label, _f(_SANS_B, 32), ACC)
    _c(d, 380, f"Skor tahun {skor} · {tier}", _f(_SERIF_B, 44), INK)
    x0, base, bw, gap = 120, 820, 52, 20
    for i, v in enumerate(kurva):
        h = round(v / 100 * 330)
        col = (110, 143, 94) if v >= 65 else (232, 166, 127) if v >= 50 else (192, 86, 75)
        x = x0 + i * (bw + gap)
        d.rounded_rectangle((x, base - h, x + bw, base), radius=10, fill=col)
        d.text((x + 8, base + 10), "JFMAMJJASOND"[i], font=_f(_SANS_B, 28), fill=MUTE)
    _c(d, 910, "BULAN TERBAIK: " + ", ".join(terbaik), _f(_SANS_B, 28), (79, 122, 60))
    _c(d, 960, "PERLU DIJAGA: " + ", ".join(terjaga), _f(_SANS_B, 28), (178, 85, 44))
    return _out(img)
