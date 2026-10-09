"""Watermark kecil "By Destiny Reveal" untuk semua kartu hasil (display + download)."""

import base64
import io
from functools import lru_cache
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

TEXT = "By Destiny Reveal"
_FONTS = ["DejaVuSerif-Italic.ttf", "DejaVuSans-Oblique.ttf", "DejaVuSans.ttf"]


def _font(size):
    for n in _FONTS:
        try:
            return ImageFont.truetype(n, size)
        except OSError:
            continue
    return ImageFont.load_default()


def add_watermark(img, text=TEXT, side="right", bottom=None, pad=None):
    """Return PIL RGBA: teks kecil transparan di pojok bawah (kanan/kiri)."""
    base = img.convert("RGBA")
    w, h = base.size
    size = max(11, round(w * 0.028))
    layer = Image.new("RGBA", base.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    f = _font(size)
    tw = d.textlength(text, font=f)
    pad = pad if pad is not None else round(w * 0.04)
    x = w - tw - pad if side == "right" else pad
    y = h - size - (bottom if bottom is not None else round(h * 0.022))
    reg = base.convert("L").crop((int(x), int(y), int(x + tw), int(y + size))).resize((1, 1))
    if reg.getpixel((0, 0)) > 150:  # latar terang -> teks gelap
        d.text((x, y), text, font=f, fill=(45, 42, 38, 150))
    else:
        d.text((x + 1, y + 1), text, font=f, fill=(0, 0, 0, 90))
        d.text((x, y), text, font=f, fill=(255, 255, 255, 170))
    return Image.alpha_composite(base, layer)


@lru_cache(maxsize=256)
def watermarked_png(path, side="right"):
    """path file PNG -> bytes PNG ber-watermark (cache per file)."""
    with Image.open(Path(path)) as im:
        out = add_watermark(im, side=side)
    buf = io.BytesIO()
    out.save(buf, format="PNG", optimize=True)
    return buf.getvalue()


def watermarked_data_uri(path, side="right"):
    return "data:image/png;base64," + base64.b64encode(watermarked_png(str(path), side)).decode("ascii")
