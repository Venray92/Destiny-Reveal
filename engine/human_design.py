"""
Engine Human Design — simplifikasi: cuma nentuin TYPE (5 kemungkinan:
Generator, Manifesting Generator, Manifestor, Projector, Reflector), bukan
bodygraph penuh (gate/line/profile/incarnation cross dll).

Sumber rumus:
- Gate Wheel (64 gate -> 360 derajat, mulai dari Gate 41 di ~2 derajat
  Aquarius, searah jarum jam) + logic Type/Strategy/Authority: dari
  dokumen referensi yang dikasih Stev (27 Sep 2026).
- Tabel "gate masuk center yang mana" (9 pusat/center) + daftar 36
  channel (pasangan gate yang menghubungkan 2 center): TIDAK ada di
  dokumen Stev -- dicari & diverifikasi sendiri (cross-check: total 64
  gate tersebar rapi ke 9 center tanpa tumpang tindih; 36 channel selalu
  menghubungkan 2 center yang beda; titik awal wheel 302 derajat
  dikonfirmasi cocok sama fakta yang banyak dikutip "Gate 25 mulai
  persis sebelum 0 derajat Aries").

Posisi planet dihitung pakai `pyswisseph` (Swiss Ephemeris Python
binding) dengan flag Moshier (SEFLG_MOSEPH) -- ephemeris semi-analitik
bawaan library, TIDAK butuh file data ephemeris eksternal (JPL dll),
presisinya jauh lebih dari cukup buat keperluan gate-level (lebar 1
gate = 5.625 derajat).

TIMEZONE: presisi HD sensitif ke waktu UTC yang tepat (terutama Bulan,
yang gerak ~13 derajat/hari -> bisa ganti gate tiap ~10 jam). Karena kita
cuma punya nama kota (bukan koordinat), dipakai pendekatan SEMENTARA:
lookup kasar zona waktu Indonesia dari nama kota (WIB/WITA/WIT),
fallback ke WIB kalau kota gak dikenali/di luar Indonesia (keputusan
Stev 27 Sep 2026, opsi 1 dari 2 yang ditawarkan -- lihat progress-notes
buat detail diskusinya). Ini kompromi yang disengaja demi kesederhanaan,
BUKAN keakuratan penuh untuk kota luar Indonesia.
"""

from datetime import date, time

import swisseph as swe

# ── Timezone lookup kasar (Indonesia) ───────────────────────────────
# WIB = UTC+7, WITA = UTC+8, WIT = UTC+9. Dicocokkan dari SUBSTRING nama
# kota (lowercase) -- daftar kota WITA & WIT provinsi Kalimantan
# Timur/Utara/Selatan, Bali, NTB, NTT, Sulawesi, Maluku, Papua. Kota yang
# gak ketemu / bukan Indonesia -> fallback WIB (+7).
_WITA_HINTS = [
    "bali", "denpasar", "mataram", "lombok", "kupang", "ntt", "ntb",
    "makassar", "manado", "palu", "kendari", "gorontalo", "balikpapan",
    "samarinda", "banjarmasin", "tarakan", "sulawesi", "toraja",
    # NOTE: Pontianak & Kalimantan Barat SENGAJA gak dimasukin sini --
    # meski geografis di Kalimantan, itu tetap pakai WIB (+7), bukan WITA.
]
_WIT_HINTS = [
    "jayapura", "papua", "ambon", "maluku", "sorong", "manokwari",
    "ternate", "merauke", "fakfak", "biak",
]


def _tebak_utc_offset(kota_lahir: str | None) -> int:
    """Tebak offset UTC (jam) dari nama kota. Default WIB (+7) kalau gak
    ketemu/kosong -- lihat docstring modul buat alasan simplifikasi ini."""
    if not kota_lahir:
        return 7
    k = kota_lahir.strip().lower()
    if any(hint and hint in k for hint in _WIT_HINTS):
        return 9
    if any(hint and hint in k for hint in _WITA_HINTS):
        return 8
    return 7


# ── Gate Wheel (dari dokumen Stev, sudah divalidasi 64 gate lengkap
# tanpa duplikat) -- mulai index 0 = Gate 41, di 302 derajat ekliptika
# (~2 derajat Aquarius), searah jarum jam (index makin besar = derajat
# makin besar).
GATE_WHEEL_START_DEGREE = 302.0
GATE_WIDTH = 360.0 / 64  # 5.625 derajat
GATE_WHEEL_SEQUENCE = [
    41, 19, 13, 49, 30, 55, 37, 63, 22, 36, 25, 17, 21, 51, 42, 3,
    27, 24, 2, 23, 8, 20, 16, 35, 45, 12, 15, 52, 39, 53, 62, 56,
    31, 33, 7, 4, 29, 59, 40, 64, 47, 6, 46, 18, 48, 57, 32, 50,
    28, 44, 1, 43, 14, 34, 9, 5, 26, 11, 10, 58, 38, 54, 61, 60,
]


def _longitude_to_gate(longitude_deg: float) -> int:
    offset = (longitude_deg - GATE_WHEEL_START_DEGREE) % 360
    idx = int(offset // GATE_WIDTH)
    idx = min(idx, 63)  # jaga2 pembulatan float pas di batas 360
    return GATE_WHEEL_SEQUENCE[idx]


# ── 9 Center -> daftar gate ─────────────────────────────────────────
CENTER_GATES = {
    "Head": [61, 63, 64],
    "Ajna": [4, 11, 17, 24, 43, 47],
    "Throat": [8, 12, 16, 20, 23, 31, 33, 35, 45, 56, 62],
    "G": [1, 2, 7, 10, 13, 15, 25, 46],
    "Heart": [21, 26, 40, 51],
    "Sacral": [3, 5, 9, 14, 27, 29, 34, 42, 59],
    "SolarPlexus": [6, 22, 30, 36, 37, 49, 55],
    "Spleen": [18, 28, 32, 44, 48, 50, 57],
    "Root": [19, 38, 39, 41, 52, 53, 54, 58, 60],
}
_GATE_TO_CENTER = {g: c for c, gates in CENTER_GATES.items() for g in gates}

MOTOR_CENTERS = {"Sacral", "SolarPlexus", "Heart", "Root"}

# ── 36 Channel (pasangan gate) ──────────────────────────────────────
CHANNELS = [
    (61, 24), (64, 47), (63, 4), (17, 62), (11, 56), (43, 23), (16, 48), (57, 20),
    (20, 10), (20, 34), (34, 10), (57, 10), (57, 34), (26, 44), (7, 31), (1, 8),
    (13, 33), (15, 5), (2, 14), (46, 29), (25, 51), (21, 45), (37, 40), (12, 22),
    (35, 36), (27, 50), (32, 54), (28, 38), (18, 58), (42, 53), (3, 60), (9, 52),
    (59, 6), (19, 49), (39, 55), (41, 30),
]

# ── Badan langit yang dihitung: (nama, kode_swisseph) ───────────────
_PLANETS = [
    ("Sun", swe.SUN), ("Moon", swe.MOON), ("Mercury", swe.MERCURY),
    ("Venus", swe.VENUS), ("Mars", swe.MARS), ("Jupiter", swe.JUPITER),
    ("Saturn", swe.SATURN), ("Uranus", swe.URANUS), ("Neptune", swe.NEPTUNE),
    ("Pluto", swe.PLUTO), ("NNode", swe.MEAN_NODE),
]


def _jd_ut(tanggal: date, jam_desimal: float) -> float:
    return swe.julday(tanggal.year, tanggal.month, tanggal.day, jam_desimal)


def _longitude(body_code: int, jd: float) -> float:
    result, _flag = swe.calc_ut(jd, body_code, swe.FLG_MOSEPH)
    return result[0] % 360


def _semua_gate_aktif(jd: float) -> set:
    """Hitung gate yang aktif dari 11 badan langit + Earth (=Sun+180) +
    South Node (=NNode+180) pada satu titik waktu (jd) -- 13 titik total."""
    gates = set()
    lons = {}
    for name, code in _PLANETS:
        lons[name] = _longitude(code, jd)
    lons["Earth"] = (lons["Sun"] + 180) % 360
    lons["SNode"] = (lons["NNode"] + 180) % 360
    for lon in lons.values():
        gates.add(_longitude_to_gate(lon))
    return gates


def _cari_jd_design(jd_lahir: float, sun_lon_lahir: float) -> float:
    """Cari titik waktu (jd) di masa lalu saat Sun berada persis 88 derajat
    busur ekliptika sebelum posisi Sun saat lahir -- ini "Design" dalam HD
    (sering disebut informal "~88 hari sebelum lahir", tapi yang presisi
    adalah 88 DERAJAT busur matahari, bukan 88 hari kalender pas -- lama
    harinya sedikit bervariasi tergantung kecepatan orbit bumi).
    Dicari lewat iterasi sederhana (fixed-point), konvergen cepat karena
    kecepatan matahari relatif stabil (~0.9856 derajat/hari)."""
    target = (sun_lon_lahir - 88.0) % 360
    jd = jd_lahir - 88.0
    for _ in range(8):
        current = _longitude(swe.SUN, jd)
        diff = (current - target + 180) % 360 - 180  # selisih bertanda, -180..180
        jd -= diff / 0.9856
    return jd


def _pusat_terdefinisi(gate_aktif: set) -> set:
    """Center dianggap Defined kalau MINIMAL 1 channel yang nyambung ke
    center itu punya KEDUA gate-nya aktif."""
    defined = set()
    for g1, g2 in CHANNELS:
        if g1 in gate_aktif and g2 in gate_aktif:
            defined.add(_GATE_TO_CENTER[g1])
            defined.add(_GATE_TO_CENTER[g2])
    return defined


def _channel_terdefinisi(gate_aktif: set):
    """List channel (pasangan CENTER, bukan gate) yang aktif -- dipakai
    buat cek konektivitas graf antar center."""
    edges = []
    for g1, g2 in CHANNELS:
        if g1 in gate_aktif and g2 in gate_aktif:
            edges.append((_GATE_TO_CENTER[g1], _GATE_TO_CENTER[g2]))
    return edges


def _terhubung(a: str, b: str, edges: list) -> bool:
    """BFS sederhana: apa center `a` bisa mencapai center `b` lewat
    channel yang aktif (langsung ATAU lewat center lain di antaranya)."""
    if a == b:
        return True
    adj = {}
    for x, y in edges:
        adj.setdefault(x, set()).add(y)
        adj.setdefault(y, set()).add(x)
    visited = {a}
    queue = [a]
    while queue:
        cur = queue.pop()
        if cur == b:
            return True
        for nxt in adj.get(cur, ()):
            if nxt not in visited:
                visited.add(nxt)
                queue.append(nxt)
    return b in visited


def _tentukan_type_authority(defined: set, edges: list) -> dict:
    sacral_defined = "Sacral" in defined
    motor_to_throat = any(
        m in defined and _terhubung(m, "Throat", edges)
        for m in MOTOR_CENTERS
    )

    if not defined:
        tipe, strategi = "Reflector", "Wait a Lunar Cycle (28.5 hari)"
    elif sacral_defined and motor_to_throat:
        tipe, strategi = "Manifesting Generator", "To Respond, then Inform"
    elif sacral_defined:
        tipe, strategi = "Generator", "To Respond"
    elif motor_to_throat:
        tipe, strategi = "Manifestor", "To Inform"
    else:
        tipe, strategi = "Projector", "Wait for the Invitation"

    # Authority (hierarki prioritas)
    if "SolarPlexus" in defined:
        otoritas = "Emotional / Solar Plexus"
    elif "Sacral" in defined:
        otoritas = "Sacral"
    elif "Spleen" in defined:
        otoritas = "Splenic"
    elif "Heart" in defined:
        otoritas = "Ego / Heart"
    elif "G" in defined and _terhubung("G", "Throat", edges):
        otoritas = "G-Center / Self-Projected"
    elif tipe == "Reflector":
        otoritas = "Lunar / Environmental"
    else:
        otoritas = "Mental Projector / Outer Authority"

    return {"tipe": tipe, "strategi": strategi, "otoritas": otoritas}


# Slug dipakai buat lookup kartu/konten (5 tipe).
_TIPE_SLUG = {
    "Generator": "generator",
    "Manifesting Generator": "manifesting_generator",
    "Manifestor": "manifestor",
    "Projector": "projector",
    "Reflector": "reflector",
}


def hitung_human_design(tanggal_lahir: date, jam_lahir: time, kota_lahir: str | None) -> dict:
    """
    Hitung Type/Strategy/Authority Human Design.

    Args:
        tanggal_lahir: tanggal lahir Gregorian (waktu LOKAL).
        jam_lahir: jam lahir (waktu LOKAL, objek datetime.time).
        kota_lahir: nama kota lahir (dipakai buat nebak offset UTC kasar
            -- lihat docstring modul soal keterbatasannya).

    Returns:
        dict: {"tipe_slug": "generator", "tipe": "Generator",
               "strategi": "To Respond", "otoritas": "Sacral"}
    """
    offset = _tebak_utc_offset(kota_lahir)
    jam_desimal_lokal = jam_lahir.hour + jam_lahir.minute / 60 + jam_lahir.second / 3600
    jam_desimal_utc = jam_desimal_lokal - offset

    jd_lahir = _jd_ut(tanggal_lahir, jam_desimal_utc)
    sun_lon_lahir = _longitude(swe.SUN, jd_lahir)
    jd_design = _cari_jd_design(jd_lahir, sun_lon_lahir)

    gate_personality = _semua_gate_aktif(jd_lahir)
    gate_design = _semua_gate_aktif(jd_design)
    gate_aktif = gate_personality | gate_design

    defined = _pusat_terdefinisi(gate_aktif)
    edges = _channel_terdefinisi(gate_aktif)
    hasil = _tentukan_type_authority(defined, edges)

    return {
        "tipe_slug": _TIPE_SLUG[hasil["tipe"]],
        "tipe": hasil["tipe"],
        "strategi": hasil["strategi"],
        "otoritas": hasil["otoritas"],
    }
