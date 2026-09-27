"""
Bank soal Kuesioner Love Language (30 pasangan pernyataan A/B, pilih 1
yang paling menggambarkan diri).

Sumber: draft soal dari Stev (chip.docx, 27 Sep 2026) — teks 30 pasangan
soalnya TIDAK diubah. TAPI bagian "kunci jawaban" di draft asli RUSAK/gak
lengkap (ada baris literal "Tergantung pasangannya" yang gak jelas, dan
gak ada pemetaan per-nomor yang bisa langsung dipakai buat scoring).
Kunci di bawah ini (field "category" tiap opsi) DIBANGUN ULANG dari awal
dengan cara baca isi tiap pernyataan satu-satu dan cocokkan ke 5 kategori
Love Language aslinya (Gary Chapman) — bukan salin dari draft asli.

Kategori: WA=Words of Affirmation, QT=Quality Time, RG=Receiving Gifts,
AS=Acts of Service, PT=Physical Touch.

KETERBATASAN (jujur, biar jelas bukan disembunyikan): distribusi
kategori di 30 soal ini TIDAK 100% simetris — WA & AS masing2 muncul
13-14x dari 60 slot, sedangkan RG & PT cuma 10x. Idealnya tiap kategori
persis 12x (60/5) biar skor maksimal tiap kategori sama rata. Masih layak
pakai buat nentuin Primary/Secondary Love Language, tapi bukan instrumen
yang matematis sempurna seimbang.

Tiap soal: {"id": nomor (1-30), "A": {"text":..., "category":...},
"B": {"text":..., "category":...}}.
"""

LOVE_LANGUAGE_QUESTIONS = [
    {"id": 1, "A": {"text": "Saya merasa sangat dicintai ketika pasangan saya memberikan pelukan hangat atau genggaman tangan secara spontan.", "category": "PT"},
               "B": {"text": "Saya merasa sangat dicintai ketika pasangan saya memberikan hadiah kecil sebagai tanda bahwa ia mengingat saya.", "category": "RG"}},
    {"id": 2, "A": {"text": "Saya sangat menghargai ketika pasangan saya meluangkan waktu penuh tanpa gangguan gadget untuk mengobrol dengan saya.", "category": "QT"},
               "B": {"text": "Saya merasa sangat dihargai ketika pasangan saya secara rutin membantu meringankan pekerjaan rumah tangga saya.", "category": "AS"}},
    {"id": 3, "A": {"text": "Ungkapan \"Aku bangga sama kamu\" atau \"Terima kasih ya\" dari pasangan memiliki makna yang sangat dalam bagi saya.", "category": "WA"},
               "B": {"text": "Saya merasa paling disayang ketika pasangan saya menemani saya berjalan-jalan atau melakukan aktivitas berdua.", "category": "QT"}},
    {"id": 4, "A": {"text": "Sentuhan fisik seperti menepuk pundak atau merangkul saat menonton film adalah cara utama saya merasakan kehangatan cinta.", "category": "PT"},
               "B": {"text": "Saya merasa sangat diperhatikan ketika pasangan saya tiba-tiba membawakan makanan kesukaan saya sepulang kerja.", "category": "AS"}},
    {"id": 5, "A": {"text": "Pujian verbal atas penampilan atau pencapaian saya membuat hati saya berbunga-bunga.", "category": "WA"},
               "B": {"text": "Saya merasa dicintai secara nyata ketika pasangan saya rela turun tangan memperbaiki barang yang rusak di rumah saya tanpa diminta.", "category": "AS"}},
    {"id": 6, "A": {"text": "Menghabiskan waktu berkualitas dengan liburan berdua adalah bentuk cinta terhebat bagi saya.", "category": "QT"},
               "B": {"text": "Menerima hadiah yang dibungkus rapi di hari spesial menunjukkan betapa pasangan benar-benar memikirkan saya.", "category": "RG"}},
    {"id": 7, "A": {"text": "Saya merasa dicintai saat pasangan dengan sigap membantu menyelesaikan urusan saya yang sedang repot.", "category": "AS"},
               "B": {"text": "Kata-kata penyemangat saat saya sedang stres adalah hal yang paling saya butuhkan dari pasangan.", "category": "WA"}},
    {"id": 8, "A": {"text": "Duduk berdampingan di sofa sambil bersandar jauh lebih bermakna daripada diberi hadiah mahal.", "category": "PT"},
               "B": {"text": "Saya sangat senang diberi hadiah kejutan, sekecil apa bentuknya, asalkan diberikan dengan tulus.", "category": "RG"}},
    {"id": 9, "A": {"text": "Saya merasa dihargai ketika pasangan memuji sifat atau kepribadian saya di depan orang lain.", "category": "WA"},
               "B": {"text": "Perhatian kecil berupa tindakan nyata dalam melayani kebutuhan sehari-hari adalah bahasa cinta sejati bagi saya.", "category": "AS"}},
    {"id": 10, "A": {"text": "Berbagi hobi atau mencoba pengalaman baru bersama pasangan adalah cara terbaik untuk merasa dekat.", "category": "QT"},
                "B": {"text": "Sentuhan fisik yang lembut dan konsisten membuat saya merasa aman dan dicintai dalam hubungan.", "category": "PT"}},
    {"id": 11, "A": {"text": "Mendengar pasangan mengatakan \"Aku mencintaimu\" secara tulus setiap hari adalah kebutuhan mutlak bagi saya.", "category": "WA"},
                "B": {"text": "Saya merasa sangat disayang saat pasangan rela mengorbankan waktunya demi menemani saya pergi ke suatu tempat.", "category": "QT"}},
    {"id": 12, "A": {"text": "Hadiah fisik menunjukkan bukti nyata bahwa pasangan mengingat saya bahkan saat kami sedang terpisah jarak.", "category": "RG"},
                "B": {"text": "Tindakan pelayanan seperti dibuatkan secangkir kopi hangat saat saya lelah adalah bukti cinta yang paling nyata.", "category": "AS"}},
    {"id": 13, "A": {"text": "Saya merasa paling dicintai ketika kami menghabiskan malam berdua hanya untuk saling bertukar cerita mendalam.", "category": "QT"},
                "B": {"text": "Sentuhan fisik yang spontan selalu berhasil meredakan hari yang berat bagi saya.", "category": "PT"}},
    {"id": 14, "A": {"text": "Pujian yang tulus atas kerja keras saya jauh lebih berharga daripada kado material apa pun.", "category": "WA"},
                "B": {"text": "Pasangan yang inisiatif membantu tugas-tugas saya adalah pasangan yang paling romantis.", "category": "AS"}},
    {"id": 15, "A": {"text": "Saya sangat menghargai kejutan berupa hadiah kecil yang diberikan di hari biasa (bukan hari ulang tahun/anniversary).", "category": "RG"},
                "B": {"text": "Menghabiskan waktu bersama tanpa gangguan layar ponsel adalah momen paling berharga bagi saya.", "category": "QT"}},
    {"id": 16, "A": {"text": "Sentuhan fisik seperti pijatan lembut di pundak setelah seharian lelah bekerja sangat berarti bagi saya.", "category": "PT"},
                "B": {"text": "Kata-kata apresiasi atas hal-hal kecil yang saya lakukan membuat saya merasa dihargai.", "category": "WA"}},
    {"id": 17, "A": {"text": "Saya merasa dicintai ketika pasangan membantu saya merapikan atau membereskan sesuatu.", "category": "AS"},
                "B": {"text": "Menerima suvenir atau oleh-oleh dari perjalanan pasangan membuat saya merasa selalu ada di dalam pikirannya.", "category": "RG"}},
    {"id": 18, "A": {"text": "Mengobrol berdua di dalam mobil dalam perjalanan jauh adalah momen kedekatan favorit saya.", "category": "QT"},
                "B": {"text": "Ungkapan cinta tertulis seperti surat atau pesan teks manis sangat menyentuh hati saya.", "category": "WA"}},
    {"id": 19, "A": {"text": "Saya merasa diutamakan ketika pasangan rela melakukan pekerjaan berat menggantikan saya.", "category": "AS"},
                "B": {"text": "Duduk berdekatan atau bersentuhan fisik saat menonton TV memberikan kenyamanan luar biasa bagi saya.", "category": "PT"}},
    {"id": 20, "A": {"text": "Hadiah dari pasangan memiliki nilai sentimental yang sangat tinggi di mata saya.", "category": "RG"},
                "B": {"text": "Mendengar pasangan menceritakan hal-hal baik tentang saya kepada orang lain membuat saya merasa sangat dicintai.", "category": "WA"}},
    {"id": 21, "A": {"text": "Saya merasa paling diperhatikan ketika pasangan meluangkan waktu khusus untuk mendengarkan keluh kesah saya.", "category": "QT"},
                "B": {"text": "Tindakan nyata pasangan yang meringankan beban saya adalah bukti cinta yang paling valid.", "category": "AS"}},
    {"id": 22, "A": {"text": "Sentuhan fisik adalah cara tercepat untuk mengembalikan kedekatan setelah bertengkar.", "category": "PT"},
                "B": {"text": "Kata-kata maaf yang tulus dan pujian penyemangat jauh lebih berharga daripada bentuk permintaan maaf lainnya.", "category": "WA"}},
    {"id": 23, "A": {"text": "Saya merasa sangat senang ketika pasangan memberikan hadiah yang sudah lama saya idamkan.", "category": "RG"},
                "B": {"text": "Menghabiskan akhir pekan bersama untuk melakukan kegiatan santai berdua adalah impian saya.", "category": "QT"}},
    {"id": 24, "A": {"text": "Bantuan praktis dalam bentuk tindakan melayani membuat saya merasa tidak berjuang sendirian.", "category": "AS"},
                "B": {"text": "Pujian verbal atas penampilan fisik atau gaya busana saya selalu berhasil menceriakan hari saya.", "category": "WA"}},
    {"id": 25, "A": {"text": "Saya merasa dicintai saat pasangan menggenggam tangan saya di tempat umum.", "category": "PT"},
                "B": {"text": "Saya sangat menghargai waktu khusus yang sengaja disediakan pasangan untuk bersama saya.", "category": "QT"}},
    {"id": 26, "A": {"text": "Menerima hadiah kejutan menunjukkan bahwa pasangan selalu memikirkan saya di mana pun ia berada.", "category": "RG"},
                "B": {"text": "Kata-kata dorongan semangat saat saya ragu pada diri sendiri adalah hal terpenting bagi saya.", "category": "WA"}},
    {"id": 27, "A": {"text": "Saya merasa disayang ketika pasangan inisiatif menyiapkan keperluan saya sebelum bepergian.", "category": "AS"},
                "B": {"text": "Berbagi pandangan dan mengobrol secara mendalam dengan pasangan adalah momen paling intim bagi saya.", "category": "QT"}},
    {"id": 28, "A": {"text": "Sentuhan kehangatan fisik jauh lebih meyakinkan daripada seribu kata-kata cinta.", "category": "PT"},
                "B": {"text": "Barang pemberian pasangan yang saya simpan rapi menjadi pengingat cinta yang kuat bagi saya.", "category": "RG"}},
    {"id": 29, "A": {"text": "Saya merasa sangat dihargai ketika pasangan memuji kecerdasan atau ide-ide saya.", "category": "WA"},
                "B": {"text": "Pasangan yang membawakan makanan saat saya sibuk bekerja adalah definisi cinta yang nyata.", "category": "AS"}},
    {"id": 30, "A": {"text": "Menghabiskan momen liburan berdua tanpa gangguan pekerjaan adalah hal terbaik dalam hubungan.", "category": "QT"},
                "B": {"text": "Tindakan nyata berupa bantuan kecil sehari-hari membuat saya jatuh cinta setiap hari.", "category": "AS"}},
]

LOVE_LANGUAGE_NAMES = {
    "WA": "Words of Affirmation",
    "QT": "Quality Time",
    "RG": "Receiving Gifts",
    "AS": "Acts of Service",
    "PT": "Physical Touch",
}
# Slug dipakai buat cari gambar kartu (assets/cards/love_language/<slug>.png).
LOVE_LANGUAGE_SLUG = {
    "WA": "words_of_affirmation",
    "QT": "quality_time",
    "RG": "receiving_gifts",
    "AS": "acts_of_service",
    "PT": "physical_touch",
}
