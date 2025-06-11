from enum import Enum

class AnalysisPeriod(Enum):
    MINGGU_INI = "5d"      # Pergerakan minggu ini
    BULAN_INI = "1mo"      # Tren bulan berjalan
    KUARTAL = "3mo"        # Performa 3 bulan terakhir
    SEMESTER = "6mo"       # Performa 6 bulan terakhir
    TAHUN_INI = "1y"       # Performa tahun berjalan
    DUA_TAHUN = "2y"       # Perbandingan 2 tahun terakhir
    JANGKA_PANJANG = "5y"  # Historis jangka panjang

    @staticmethod
    def get_description(period):
        descriptions = {
            "5d": """
Analisis Minggu Ini (5 hari terakhir)
- Cocok untuk: Melihat momentum harga terkini
- Berguna untuk: Menentukan waktu yang tepat untuk beli/jual
- Disarankan untuk: Trading harian atau mingguan
            """,
            "1mo": """
Analisis Bulan Ini
- Cocok untuk: Melihat tren bulanan
- Berguna untuk: Menentukan arah pergerakan harga jangka pendek
- Disarankan untuk: Keputusan beli/jual dalam sebulan
            """,
            "3mo": """
Analisis Kuartal (3 bulan)
- Cocok untuk: Melihat tren per kuartal
- Berguna untuk: Evaluasi kinerja saham per triwulan
- Disarankan untuk: Perencanaan investasi 3 bulanan
            """,
            "6mo": """
Analisis Semester (6 bulan)
- Cocok untuk: Evaluasi tengah tahun
- Berguna untuk: Melihat performa setengah tahun
- Disarankan untuk: Penyesuaian portofolio tengah tahun
            """,
            "1y": """
Analisis Tahun Ini
- Cocok untuk: Evaluasi tahunan
- Berguna untuk: Melihat kinerja saham selama setahun
- Disarankan untuk: Perencanaan investasi tahunan
            """,
            "2y": """
Analisis Dua Tahun Terakhir
- Cocok untuk: Perbandingan antar tahun
- Berguna untuk: Melihat konsistensi kinerja
- Disarankan untuk: Investasi jangka menengah
            """,
            "5y": """
Analisis Jangka Panjang (5 tahun)
- Cocok untuk: Melihat rekam jejak panjang
- Berguna untuk: Menilai stabilitas perusahaan
- Disarankan untuk: Investasi jangka panjang
            """
        }
        return descriptions.get(period.value, "Periode tidak valid")

    @staticmethod
    def list_periods():
        """Menampilkan daftar periode analisis yang tersedia dengan penjelasan"""
        print("Pilihan Periode Analisis Yang Tersedia:")
        print("-" * 50)
        for period in AnalysisPeriod:
            print(f"\n{period.name}:")
            print(AnalysisPeriod.get_description(period))
