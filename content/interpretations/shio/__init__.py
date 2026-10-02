"""Konten Shio (12 kategori) — tiap shio di file terpisah. Lihat docs/formula-notes.md."""

from .tikus import TIKUS_CONTENT
from .kerbau import KERBAU_CONTENT
from .macan import MACAN_CONTENT
from .kelinci import KELINCI_CONTENT
from .naga import NAGA_CONTENT
from .ular import ULAR_CONTENT
from .kuda import KUDA_CONTENT
from .kambing import KAMBING_CONTENT
from .monyet import MONYET_CONTENT
from .ayam import AYAM_CONTENT
from .anjing import ANJING_CONTENT
from .babi import BABI_CONTENT

SHIO_CONTENT = {
    "Tikus": TIKUS_CONTENT,
    "Kerbau": KERBAU_CONTENT,
    "Macan": MACAN_CONTENT,
    "Kelinci": KELINCI_CONTENT,
    "Naga": NAGA_CONTENT,
    "Ular": ULAR_CONTENT,
    "Kuda": KUDA_CONTENT,
    "Kambing": KAMBING_CONTENT,
    "Monyet": MONYET_CONTENT,
    "Ayam": AYAM_CONTENT,
    "Anjing": ANJING_CONTENT,
    "Babi": BABI_CONTENT,
}
