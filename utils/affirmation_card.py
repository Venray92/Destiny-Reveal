"""Kartu Afirmasi Harian (PNG story 1080x1920 @2x) - kit di utils/share_card.py."""

from utils.share_card import ACC, ACC_D, INK, LINE, MUTE, W, Card, font


def buat_kartu(nama, tanggal_txt, kalimat, langkah):
    """Return bytes PNG. kalimat = list 4 kalimat afirmasi; langkah = 1 kalimat aksi."""
    c = Card()
    c.frame("AFIRMASI HARI INI", tanggal_txt)
    c.ctext(390, "“", font("serif", 150), (232, 190, 160))
    y = c.para(500, kalimat[0], font("serif", 56), INK, 820, 80, maxl=5) + 30
    f = font("serif_r", 34)
    for k in kalimat[1:]:
        y = c.para(y, k, f, (80, 72, 64), 800, 48, maxl=3) + 16
    by = max(y + 60, 1180)
    c.rrect((110, by, W - 110, by + 300), 36, fill=(255, 255, 255), outline=LINE, shadow=True)
    c.ctext(by + 32, "LANGKAH KECIL HARI INI", font("sans_b", 24), ACC_D, spacing=4)
    c.para(by + 90, langkah, font("serif_r", 34), INK, 780, 48, maxl=4)
    c.ctext(by + 322, f"Untuk: {nama}", font("sans_m", 26), MUTE)
    return c.png()
