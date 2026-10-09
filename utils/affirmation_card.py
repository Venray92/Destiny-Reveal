"""Kartu Afirmasi Harian (PNG 1080x1350) dibuat dengan Pillow + watermark "By Destiny Reveal"."""

import io
import textwrap

from PIL import Image, ImageDraw, ImageFont

from utils.watermark import add_watermark

W, H = 1080, 1350
_SERIF = ["Lora-Italic-Variable.ttf", "DejaVuSerif-Italic.ttf", "DejaVuSerif.ttf"]
_SERIF_B = ["DejaVuSerif-Bold.ttf", "DejaVuSerif.ttf"]
_SANS = ["DejaVuSans-Bold.ttf", "DejaVuSans.ttf"]


def _font(names, size):
    for n in names:
        try:
            return ImageFont.truetype(n, size)
        except OSError:
            continue
    return ImageFont.load_default()


def _gradient():
    top, bot = (255, 244, 226), (246, 214, 178)
    img = Image.new("RGB", (W, H), top)
    px = ImageDraw.Draw(img)
    for y in range(H):
        t = y / (H - 1)
        px.line([(0, y), (W, y)], fill=tuple(round(top[i] + (bot[i] - top[i]) * t) for i in range(3)))
    return img


def _center(d, y, text, font, fill):
    w = d.textlength(text, font=font)
    d.text(((W - w) / 2, y), text, font=font, fill=fill)


def buat_kartu(nama, tanggal_txt, kalimat, langkah):
    """Return bytes PNG. kalimat = list 4 kalimat afirmasi; langkah = 1 kalimat aksi."""
    img = _gradient()
    d = ImageDraw.Draw(img)
    ink, accent = (45, 42, 38), (201, 98, 52)
    d.rounded_rectangle((48, 48, W - 48, H - 48), radius=36, outline=(201, 98, 52), width=3)
    _center(d, 110, "AFIRMASI HARI INI", _font(_SANS, 30), accent)
    _center(d, 160, tanggal_txt, _font(_SERIF, 30), (139, 131, 120))
    d.line([(W / 2 - 60, 215), (W / 2 + 60, 215)], fill=accent, width=3)

    y = 270
    f_main = _font(_SERIF_B, 46)
    for ln in textwrap.wrap(f"“{kalimat[0]}”", 28):
        _center(d, y, ln, f_main, ink)
        y += 66
    y += 36
    f_s = _font(_SERIF, 34)
    for k in kalimat[1:]:
        for ln in textwrap.wrap(k, 40):
            _center(d, y, ln, f_s, (80, 72, 64))
            y += 48
        y += 22

    by = max(y + 20, 1010)
    d.rounded_rectangle((120, by, W - 120, by + 180), radius=24, fill=(255, 255, 255), outline=(232, 224, 213), width=2)
    _center(d, by + 22, "LANGKAH KECIL HARI INI", _font(_SANS, 24), accent)
    yy = by + 70
    for ln in textwrap.wrap(langkah, 46)[:3]:
        _center(d, yy, ln, _font(_SERIF, 30), ink)
        yy += 42
    _center(d, H - 150, f"Untuk: {nama}", _font(_SANS, 26), (139, 131, 120))
    out = add_watermark(img, side="right", bottom=78, pad=92)
    buf = io.BytesIO()
    out.convert("RGB").save(buf, format="PNG", optimize=True)
    return buf.getvalue()
