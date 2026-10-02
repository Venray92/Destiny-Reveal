"""Konten Zodiak (12 kategori) — tiap sign di file terpisah. Lihat docs/formula-notes.md."""

from .aries import ARIES_CONTENT
from .taurus import TAURUS_CONTENT
from .gemini import GEMINI_CONTENT
from .cancer import CANCER_CONTENT
from .leo import LEO_CONTENT
from .virgo import VIRGO_CONTENT
from .libra import LIBRA_CONTENT
from .scorpio import SCORPIO_CONTENT
from .sagittarius import SAGITTARIUS_CONTENT
from .capricorn import CAPRICORN_CONTENT
from .aquarius import AQUARIUS_CONTENT
from .pisces import PISCES_CONTENT

ZODIAK_CONTENT = {
    "Aries": ARIES_CONTENT,
    "Taurus": TAURUS_CONTENT,
    "Gemini": GEMINI_CONTENT,
    "Cancer": CANCER_CONTENT,
    "Leo": LEO_CONTENT,
    "Virgo": VIRGO_CONTENT,
    "Libra": LIBRA_CONTENT,
    "Scorpio": SCORPIO_CONTENT,
    "Sagittarius": SAGITTARIUS_CONTENT,
    "Capricorn": CAPRICORN_CONTENT,
    "Aquarius": AQUARIUS_CONTENT,
    "Pisces": PISCES_CONTENT,
}
