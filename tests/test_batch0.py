"""Batch 0: harga tidak tampil di home, watermark kartu, form_kit, register step."""
import io
import re

from PIL import Image


def test_home_tanpa_harga():
    from components import sections, navbar
    html = "".join(c[6] for c in sections._categories()) + navbar._mega_menu_html()
    assert not re.search(r"\d+\s*✨", html)
    assert "dh-ov-price" not in html


def test_watermark_ada_di_pojok_bawah():
    from utils.card_images import card_image_bytes
    from utils.watermark import add_watermark
    raw = card_image_bytes("zodiak/leo.png")
    im = Image.open(io.BytesIO(raw))
    base = Image.open("assets/cards/zodiak/leo.png").convert("RGBA")
    assert im.size == base.size
    w, h = im.size
    box = (int(w * 0.55), int(h * 0.93), w, h)
    assert list(im.convert("RGBA").crop(box).getdata()) != list(base.crop(box).getdata())
    top = (0, 0, w, int(h * 0.9))
    assert list(im.convert("RGBA").crop(top).getdata()) == list(base.crop(top).getdata())
    assert add_watermark(base, side="left").size == base.size


def test_form_kit_dan_register_ada():
    from components import form_kit, auth, mini_modals
    for f in ("data_bar", "login_gate", "loading_view", "render_register", "save_profile"):
        assert hasattr(form_kit, f)
    import inspect
    for fn in (mini_modals.daily_dialog, mini_modals.tarot_dialog, mini_modals.preview_dialog, mini_modals.streak_dialog):
        assert "login_gate" in inspect.getsource(fn)
    assert "register" in inspect.getsource(auth._login)
