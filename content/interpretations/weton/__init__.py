"""Konten Weton — tiap entri di file terpisah. Lihat docs/formula-notes.md."""

from .legi import LEGI_CONTENT
from .pahing import PAHING_CONTENT
from .pon import PON_CONTENT
from .wage import WAGE_CONTENT
from .kliwon import KLIWON_CONTENT

WETON_CONTENT = {
    "Legi": LEGI_CONTENT,
    "Pahing": PAHING_CONTENT,
    "Pon": PON_CONTENT,
    "Wage": WAGE_CONTENT,
    "Kliwon": KLIWON_CONTENT,
}
