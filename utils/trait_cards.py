"""Kartu share Career DNA, Strength, Decision, Yearly (PNG story 1080x1920 @2x) - kit di utils/share_card.py."""

from utils.share_card import ACC, ACC_D, GOOD, H, INK, LINE, MUTE, SOFT, W, WARN, Card, font, radar


def _trim(c, text, f, maxw):
    t = str(text)
    while c.tw(t, f) > maxw and len(t) > 2:
        t = t[:-2].rstrip() + "…"
    return t


def kartu_karier(nama, code, arketipe, rel, peran):
    c = Card()
    c.frame("CAREER DNA", nama)
    c.ctext(395, code, font("serif", 190), INK, spacing=6)
    c.ctext(640, _trim(c, arketipe, font("serif", 52), 840), font("serif", 52), ACC)
    c.rrect((110, 720, W - 110, 1250), 40, fill=(255, 255, 255), outline=LINE, shadow=True)
    L = list("RIASEC")
    radar(c, W / 2, 985, 135, L, [rel[l] for l in L])
    c.ctext(1290, "PERAN YANG COCOK", font("sans_b", 26), ACC_D, spacing=4)
    y = 1345
    f = font("serif_r", 36)
    for p in peran[:4]:
        c.d.ellipse((150 * 2, (y + 17) * 2, 164 * 2, (y + 31) * 2), fill=ACC)
        c.text(190, y, _trim(c, p, f, 760), f, INK)
        y += 70
    return c.png()


def kartu_kekuatan(nama, tags, blind):
    c = Card()
    c.frame("STRENGTH & BLIND SPOT", nama)
    c.ctext(400, "KEKUATANKU", font("sans_b", 28), ACC_D, spacing=5)
    y, f = 460, font("serif", 46)
    for t in tags[:4]:
        t = _trim(c, t, f, 700)
        w = c.tw(t, f) + 90
        c.rrect(((W - w) / 2, y, (W + w) / 2, y + 86), 43, fill=(255, 255, 255), outline=ACC, width=3, shadow=True)
        c.ctext(y + 14, t, f, INK)
        y += 112
    y += 30
    fb = font("serif_r", 34)
    hh = 100 + sum(len(c.wrap(b, fb, 720)[:2]) * 48 + 22 for b in blind[:3]) + 20
    c.rrect((110, y, W - 110, y + hh), 40, fill=(255, 255, 255), outline=LINE, shadow=True)
    c.ctext(y + 36, "TITIK BUTAKU", font("sans_b", 28), ACC_D, spacing=5)
    yy = y + 100
    for b in blind[:3]:
        c.d.ellipse((150 * 2, (yy + 15) * 2, 164 * 2, (yy + 29) * 2), fill=ACC)
        yy = c.para(yy, b, fb, (80, 72, 64), 720, 48, maxl=2, x=190) + 22
    return c.png()


def kartu_keputusan(nama_a, nama_b, skor_a, skor_b, unggul, arah):
    """Kartu share Decision Reveal. skor -6..6. unggul 'A'/'B'/None."""
    c = Card()
    c.frame("DECISION REVEAL", "Tebaran 7 kartu")
    top = {"A": "Condong ke A", "B": "Condong ke B", None: "Seimbang"}[unggul]
    c.ctext(420, top, font("serif", 84), ACC)
    y = 590
    for lab, nm, sk in (("A", nama_a, skor_a), ("B", nama_b, skor_b)):
        on = unggul == lab
        c.rrect((110, y, W - 110, y + 220), 36, fill=(255, 255, 255) if on else SOFT, outline=ACC if on else LINE,
                width=4 if on else 2, shadow=on)
        c.text(160, y + 28, f"PILIHAN {lab}", font("sans_b", 24), ACC_D, spacing=3)
        c.text(160, y + 70, _trim(c, nm or f"Pilihan {lab}", font("serif", 46), 760), font("serif", 46), INK)
        frac = (sk + 6) / 12
        c.rrect((160, y + 160, W - 160, y + 180), 10, fill=(240, 226, 208))
        c.rrect((160, y + 160, max(160 + 24, 160 + (W - 320) * frac), y + 180), 10, fill=ACC)
        y += 260
    c.ctext(1160, "ARAH SARAN 7 HARI", font("sans_b", 26), ACC_D, spacing=4)
    c.para(1225, arah, font("serif_r", 38), INK, 800, 56, maxl=6)
    return c.png()


def kartu_tahunan(nama, year, shio_kamu, shio_tahun, rel_label, skor, tier, terbaik, terjaga, kurva):
    """Kartu share Yearly Forecast. kurva = 12 skor."""
    c = Card()
    c.frame(f"YEARLY FORECAST {year}", nama)
    c.ctext(395, f"{shio_kamu} × {shio_tahun}", font("serif", 78), INK)
    c.ctext(515, rel_label, font("sans_b", 32), ACC_D)
    c.ctext(580, f"Skor tahun {skor} · {tier}", font("serif", 46), INK)
    c.rrect((90, 690, W - 90, 1230), 40, fill=(255, 255, 255), outline=LINE, shadow=True)
    bw, gap = 52, 16
    x0, base = (W - (12 * bw + 11 * gap)) / 2, 1130
    for g in (0.5, 1.0):
        c.line(110, base - 330 * g, W - 110, base - 330 * g, (240, 230, 216), 2)
    for i, v in enumerate(kurva):
        h = max(round(v / 100 * 330), 8)
        col = GOOD if v >= 65 else (232, 166, 127) if v >= 50 else WARN
        x = x0 + i * (bw + gap)
        c.rrect((x, base - h, x + bw, base), 12, fill=col)
        c.text(x + bw / 2, base + 14, "JFMAMJJASOND"[i], font("sans_b", 26), MUTE, anchor="c")
    for y, lab, vals, col in ((1280, "BULAN TERBAIK", terbaik, (79, 122, 60)), (1430, "PERLU DIJAGA", terjaga, (178, 85, 44))):
        c.rrect((110, y, W - 110, y + 120), 30, fill=SOFT, outline=LINE)
        c.text(W / 2, y + 22, lab, font("sans_b", 22), col, spacing=3, anchor="c")
        c.text(W / 2, y + 60, _trim(c, ", ".join(vals) or "-", font("serif", 38), 760), font("serif", 38), INK, anchor="c")
    return c.png()


def kartu_laporan(judul, nama, hero, sub=None, bars=None, bullets_title=None, bullets=None):
    """Kartu share generik (Weekly/Monthly, Soul Match, Tarot Spread, dll). bars = [(label, 0-100)]."""
    def draw(c, y):
        fh = font("serif", 84 if len(hero) <= 14 else 60)
        y = c.para(y, hero, fh, INK, 860, 100 if len(hero) <= 14 else 76, maxl=2)
        if sub:
            c.ctext(y + 14, _trim(c, sub, font("sans_b", 32), 860), font("sans_b", 32), ACC_D)
            y += 14 + 70
        y += 30
        if bars:
            bs = bars[:6]
            hh = 40 + len(bs) * 78
            c.rrect((110, y, W - 110, y + hh), 40, fill=(255, 255, 255), outline=LINE, shadow=True)
            yy = y + 34
            for lab, pct in bs:
                c.text(160, yy, _trim(c, lab, font("sans_m", 26), 560), font("sans_m", 26), INK)
                c.text(W - 160, yy, f"{round(pct)}%", font("sans_b", 26), ACC_D, anchor="r")
                c.rrect((160, yy + 40, W - 160, yy + 54), 7, fill=(240, 226, 208))
                c.rrect((160, yy + 40, max(160 + 14, 160 + (W - 320) * max(0, min(pct, 100)) / 100), yy + 54), 7, fill=ACC)
                yy += 78
            y += hh + 40
        if bullets:
            if bullets_title:
                c.ctext(y, bullets_title, font("sans_b", 26), ACC_D, spacing=4)
                y += 56
            fb = font("serif_r", 34)
            for b in bullets[:5]:
                c.d.ellipse((150 * 2, (y + 15) * 2, 164 * 2, (y + 29) * 2), fill=ACC)
                y = c.para(y, b, fb, INK, 760, 46, maxl=2, x=190) + 14
        return y

    end = draw(Card(), 400)  # ukur tinggi isi, lalu taruh di tengah area aman
    y0 = 400 + max(0, min(220, (1640 - end) // 2 - 40))
    c = Card()
    c.frame(judul, nama)
    draw(c, y0)
    return c.png()
