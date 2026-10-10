"""Kit kartu share PNG (format IG Story 1080x1920, dirender 2x = 2160x3840) - tema cream & coklat Destiny Reveal."""

import io
import math
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H, S = 1080, 1920, 2
CREAM_T, CREAM_B = (253, 251, 247), (246, 221, 192)
INK, ACC, ACC_D, MUTE = (45, 42, 38), (200, 109, 59), (168, 82, 38), (139, 131, 120)
LINE, SOFT = (232, 224, 213), (250, 240, 226)
GOOD, WARN = (122, 155, 118), (192, 86, 75)
_FD = Path(__file__).resolve().parent.parent / "assets" / "fonts"
_cache = {}


def font(kind, size):
    """kind: serif | serif_i | sans | sans_m | sans_b"""
    k = (kind, size)
    if k in _cache:
        return _cache[k]
    spec = {"serif": ("Lora-Variable.ttf", "Bold"), "serif_r": ("Lora-Variable.ttf", "Regular"),
            "serif_i": ("Lora-Italic-Variable.ttf", "Italic"), "sans": ("Poppins-Regular.ttf", None),
            "sans_m": ("Poppins-Medium.ttf", None), "sans_b": ("Poppins-Bold.ttf", None)}[kind]
    try:
        f = ImageFont.truetype(str(_FD / spec[0]), size * S)
        if spec[1]:
            try:
                f.set_variation_by_name(spec[1])
            except Exception:
                pass
    except OSError:
        try:
            f = ImageFont.truetype("DejaVuSans.ttf", size * S)
        except OSError:
            f = ImageFont.load_default(size * S)
    _cache[k] = f
    return f


class Card:
    def __init__(self):
        g = Image.new("RGB", (1, H))
        for y in range(H):
            t = y / (H - 1)
            g.putpixel((0, y), tuple(round(a + (b - a) * t) for a, b in zip(CREAM_T, CREAM_B)))
        self.img = g.resize((W * S, H * S)).convert("RGBA")
        self._glow()
        self.d = ImageDraw.Draw(self.img)

    def _glow(self):
        lay = Image.new("RGBA", self.img.size, (0, 0, 0, 0))
        ld = ImageDraw.Draw(lay)
        for cx, cy, r, a in ((W * 0.9, 80, 300, 34), (W * 0.05, H * 0.7, 260, 22), (W * 0.95, H * 0.93, 300, 30)):
            ld.ellipse(((cx - r) * S, (cy - r) * S, (cx + r) * S, (cy + r) * S), fill=ACC + (a,))
        lay = lay.filter(ImageFilter.GaussianBlur(150 * S))
        self.img = Image.alpha_composite(self.img, lay)

    # ---------- primitif ----------
    def tw(self, text, f, spacing=0):
        return (self.d.textlength(text, font=f) + spacing * S * max(len(text) - 1, 0)) / S

    def text(self, x, y, text, f, fill, spacing=0, anchor="l"):
        w = self.tw(text, f, spacing)
        if anchor == "c":
            x -= w / 2
        elif anchor == "r":
            x -= w
        if not spacing:
            self.d.text((x * S, y * S), text, font=f, fill=fill)
            return w
        for ch in text:
            self.d.text((x * S, y * S), ch, font=f, fill=fill)
            x += self.d.textlength(ch, font=f) / S + spacing
        return w

    def ctext(self, y, text, f, fill, spacing=0):
        return self.text(W / 2, y, text, f, fill, spacing, "c")

    def wrap(self, text, f, maxw):
        words, lines, cur = str(text).split(), [], ""
        for w in words:
            t = (cur + " " + w).strip()
            if self.tw(t, f) <= maxw or not cur:
                cur = t
            else:
                lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
        return lines

    def para(self, y, text, f, fill, maxw, lh, maxl=None, x=None, anchor="c"):
        ls = self.wrap(text, f, maxw)
        if maxl and len(ls) > maxl:
            ls = ls[:maxl]
            ls[-1] = ls[-1].rstrip(".,; ") + "…"
        for ln in ls:
            self.text(W / 2 if x is None else x, y, ln, f, fill, anchor=anchor if x is None else "l")
            y += lh
        return y

    def rrect(self, box, r, fill=None, outline=None, width=2, shadow=False):
        x0, y0, x1, y1 = box
        if shadow:
            lay = Image.new("RGBA", self.img.size, (0, 0, 0, 0))
            ImageDraw.Draw(lay).rounded_rectangle(((x0) * S, (y0 + 10) * S, (x1) * S, (y1 + 10) * S), r * S, fill=(120, 70, 30, 55))
            lay = lay.filter(ImageFilter.GaussianBlur(14 * S))
            self.img = Image.alpha_composite(self.img, lay)
            self.d = ImageDraw.Draw(self.img)
        self.d.rounded_rectangle((x0 * S, y0 * S, x1 * S, y1 * S), r * S, fill=fill, outline=outline, width=width * S)

    def star(self, cx, cy, r, fill):
        pts = []
        for i in range(8):
            rr = r if i % 2 == 0 else r * 0.28
            a = i * math.pi / 4 - math.pi / 2
            pts.append(((cx + rr * math.cos(a)) * S, (cy + rr * math.sin(a)) * S))
        self.d.polygon(pts, fill=fill)

    def line(self, x0, y0, x1, y1, fill, width=2):
        self.d.line([(x0 * S, y0 * S), (x1 * S, y1 * S)], fill=fill, width=width * S)

    def poly(self, pts, fill=None, outline=None, width=2):
        self.d.polygon([(x * S, y * S) for x, y in pts], fill=fill)
        if outline:
            q = [(x * S, y * S) for x, y in pts]
            self.d.line(q + [q[0]], fill=outline, width=width * S, joint="curve")

    # ---------- kerangka ----------
    def frame(self, judul, sub=None):
        self.rrect((60, 150, W - 60, H - 150), 56, outline=ACC, width=3)
        # pill brand
        f = font("sans_b", 22)
        label = "DESTINY REVEAL"
        w = self.tw(label, f, 4) + 70
        x0 = (W - w) / 2
        self.rrect((x0, 190, x0 + w, 244), 27, fill=(255, 255, 255), outline=LINE, width=2)
        self.star(x0 + 28, 217, 9, ACC)
        self.text(x0 + 48, 202, label, f, ACC_D, spacing=4)
        self.ctext(284, judul, font("sans_b", 30), ACC, spacing=6)
        if sub:
            self.ctext(334, sub, font("serif_i", 32), MUTE)

    def footer(self):
        self.text(W - 110, 1680, "By Destiny Reveal", font("serif_i", 30), MUTE, anchor="r")

    def png(self):
        self.footer()
        buf = io.BytesIO()
        self.img.convert("RGB").save(buf, format="PNG", optimize=True)
        return buf.getvalue()


def radar(c, cx, cy, R, labels, vals, lab_font=None, show_val=True):
    n = len(labels)
    ang = lambda i: i * 2 * math.pi / n
    for k in (0.33, 0.66, 1.0):
        c.poly([(cx + R * k * math.sin(ang(i)), cy - R * k * math.cos(ang(i))) for i in range(n)], outline=(226, 205, 180), width=2)
    for i in range(n):
        c.line(cx, cy, cx + R * math.sin(ang(i)), cy - R * math.cos(ang(i)), (236, 220, 198), 2)
    pts = [(cx + R * max(v, 4) / 100 * math.sin(ang(i)), cy - R * max(v, 4) / 100 * math.cos(ang(i))) for i, v in enumerate(vals)]
    c.poly(pts, fill=(224, 140, 96, 190), outline=ACC, width=4)
    for x, y in pts:
        c.d.ellipse(((x - 7) * S, (y - 7) * S, (x + 7) * S, (y + 7) * S), fill=ACC_D)
    lf = lab_font or font("sans_b", 36)
    for i, l in enumerate(labels):
        x, y = cx + (R + 62) * math.sin(ang(i)), cy - (R + 62) * math.cos(ang(i))
        c.text(x, y - 30, l, lf, INK, anchor="c")
        if show_val:
            c.text(x, y + 8, f"{round(vals[i])}", font("sans", 22), MUTE, anchor="c")
