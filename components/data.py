"""Data statis Home v2: urutan/warna node diagram 15 sistem + kategori filter."""

NODE_ORDER = [
    ("Zodiak", "star"),
    ("Shio", "pets"),
    ("Weton", "calendar_today"),
    ("Numerologi", "tag"),
    ("Matrix Destiny", "grid_view"),
    ("MBTI", "psychology"),
    ("Big Five", "insights"),
    ("DISC", "groups"),
    ("Enneagram", "category"),
    ("Love Language", "favorite"),
    ("BaZi", "account_tree"),
    ("Zi Wei", "auto_awesome"),
    ("Human Design", "hub"),
    ("Golongan Darah", "bloodtype"),
    ("Tarot", "style"),
]

# Warna khas per sistem (background ikon node di diagram radial) — biar
# ga monoton krem semua, sesuai acuan mockup.
NODE_COLOR = {
    "Zodiak": "#8B5CF6",
    "Shio": "#10B981",
    "Weton": "#3B82F6",
    "Numerologi": "#6366F1",
    "Matrix Destiny": "#0EA5E9",
    "MBTI": "#EC4899",
    "Big Five": "#14B8A6",
    "DISC": "#F97316",
    "Enneagram": "#EF4444",
    "Love Language": "#F43F5E",
    "BaZi": "#D97706",
    "Zi Wei": "#CA8A04",
    "Human Design": "#7C3AED",
    "Golongan Darah": "#DC2626",
    "Tarot": "#991B1B",
}

# Mapping kategori filter -> sistem yang tetap menyala (sisanya diredupkan).
# None = semua menyala.
CATEGORY_SYSTEMS = {
    "Semua 15 Sistem": None,
    "Astrologi & Kosmik": {"Zodiak", "Numerologi"},
    "Kearifan Nusantara & Timur": {"Golongan Darah", "Shio", "Weton", "Zi Wei", "BaZi"},
    "Psikologi Modern": {"Love Language", "DISC", "Enneagram", "Big Five", "MBTI"},
    "Energi & Intuisi": {"Human Design", "Tarot", "Matrix Destiny"},
}
