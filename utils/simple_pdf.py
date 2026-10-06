"""
PDF sederhana TANPA dependency (font bawaan Helvetica, A4). Dipakai Solo Reveal -> Download PDF.
make_pdf(title, subtitle, sections) -> bytes ; sections = [(judul, [paragraf, ...]), ...]
Emoji / karakter non-Latin1 dibuang otomatis.
"""

_W = [278, 278, 355, 556, 556, 889, 667, 191, 333, 333, 389, 584, 278, 333, 278, 278, 556, 556, 556, 556, 556, 556, 556, 556, 556, 556, 278, 278, 584, 584, 584, 556, 1015, 667, 667, 722, 722, 667, 611, 778, 722, 278, 500, 667, 556, 833, 722, 778, 667, 778, 722, 667, 611, 722, 667, 944, 667, 667, 611, 278, 278, 278, 469, 556, 333, 556, 556, 500, 556, 556, 278, 556, 556, 222, 222, 500, 222, 833, 556, 556, 556, 556, 333, 500, 278, 556, 500, 722, 500, 500, 500, 334, 260, 334, 584]
_WB = [278, 333, 474, 556, 556, 889, 722, 238, 333, 333, 389, 584, 278, 333, 278, 278, 556, 556, 556, 556, 556, 556, 556, 556, 556, 556, 333, 333, 584, 584, 584, 611, 975, 722, 722, 722, 722, 667, 611, 778, 722, 278, 556, 722, 611, 833, 722, 778, 667, 778, 722, 667, 611, 722, 667, 944, 667, 667, 611, 333, 278, 333, 584, 556, 333, 556, 611, 556, 611, 556, 333, 611, 611, 278, 278, 556, 278, 889, 611, 611, 611, 611, 389, 556, 333, 611, 556, 778, 556, 556, 500, 389, 280, 389, 584]
_REPL = {"‘": "'", "’": "'", "“": '"', "”": '"', "–": "-", "—": "-", "…": "...",
         "•": "-", " ": " ", "→": "->", "✔": "", "✨": ""}
PW, PH, MX, MT, MB = 595, 842, 56, 64, 56


def _clean(t):
    t = str(t or "")
    for a, b in _REPL.items():
        t = t.replace(a, b)
    return "".join(c if (c == "\n" or 32 <= ord(c) < 127 or 160 <= ord(c) <= 255) else "" for c in t)


def _w(text, size, bold):
    tbl = _WB if bold else _W
    return sum((tbl[ord(c) - 32] if 32 <= ord(c) < 127 else 556) for c in text) * size / 1000.0


def _wrap(text, size, bold, width):
    lines, cur = [], ""
    for word in text.split():
        trial = f"{cur} {word}".strip()
        if _w(trial, size, bold) <= width or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines or [""]


def _esc(t):
    return t.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)").encode("latin-1", "replace").decode("latin-1")


def make_pdf(title, subtitle, sections):
    pages, ops, y = [], [], PH - MT

    def newpage():
        nonlocal ops, y
        if ops:
            pages.append(ops)
        ops, y = [], PH - MT

    def text(s, size, bold=False, color=(0.18, 0.16, 0.15), x=MX):
        ops.append(f"BT /{'F2' if bold else 'F1'} {size} Tf {color[0]} {color[1]} {color[2]} rg {x} {y:.1f} Td ({_esc(s)}) Tj ET")

    def block(s, size, bold=False, color=(0.18, 0.16, 0.15), gap=4, lead=1.45):
        nonlocal y
        for ln in _wrap(_clean(s), size, bold, PW - 2 * MX):
            if y - size < MB:
                newpage()
            text(ln, size, bold, color)
            y -= size * lead
        y -= gap

    block("DESTINY REVEAL", 9, True, (0.78, 0.35, 0.2), gap=2)
    block(title, 20, True, gap=2, lead=1.3)
    if subtitle:
        block(subtitle, 10, False, (0.42, 0.39, 0.35), gap=10)
    for head, paras in sections:
        if y - 60 < MB:
            newpage()
        ops.append(f"0.94 0.91 0.86 rg {MX} {y - 4:.1f} {PW - 2 * MX} 0.8 re f")
        y -= 14
        block(head, 12, True, (0.78, 0.35, 0.2), gap=3)
        for p in paras:
            block(p, 10.5, False, gap=5, lead=1.55)
        y -= 6
    pages.append(ops)

    objs = [b"<< /Type /Catalog /Pages 2 0 R >>", None,
            b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>",
            b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>"]
    kids = []
    for i, page in enumerate(pages):
        body = "\n".join(page + [f"BT /F1 8 Tf 0.6 0.58 0.55 rg {MX} 30 Td (destinyreveal.id  -  Halaman {i + 1}/{len(pages)}) Tj ET"])
        data = body.encode("latin-1", "replace")
        cid = len(objs) + 2
        objs.append(f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {PW} {PH}] /Contents {cid} 0 R "
                    "/Resources << /Font << /F1 3 0 R /F2 4 0 R >> >> >>".encode())
        objs.append(b"<< /Length " + str(len(data)).encode() + b" >>\nstream\n" + data + b"\nendstream")
        kids.append(f"{len(objs) - 1 + 0} 0 R")
    # nomor objek: index+1
    kid_refs = " ".join(f"{5 + 2 * i} 0 R" for i in range(len(pages)))
    objs[1] = f"<< /Type /Pages /Kids [{kid_refs}] /Count {len(pages)} >>".encode()
    out = bytearray(b"%PDF-1.4\n")
    offs = []
    for n, o in enumerate(objs, 1):
        offs.append(len(out))
        out += f"{n} 0 obj\n".encode() + o + b"\nendobj\n"
    xref = len(out)
    out += f"xref\n0 {len(objs) + 1}\n0000000000 65535 f \n".encode()
    for o in offs:
        out += f"{o:010d} 00000 n \n".encode()
    out += f"trailer\n<< /Size {len(objs) + 1} /Root 1 0 R >>\nstartxref\n{xref}\n%%EOF".encode()
    return bytes(out)
