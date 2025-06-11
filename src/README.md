# Source Code Stock Analysis Tool

Folder ini berisi kode sumber untuk Stock Analysis and Trading Recommendation Tool. Kode diorganisir menggunakan pendekatan modular untuk memudahkan pemeliharaan dan pengembangan.

## Struktur Folder

### analysis
Berisi modul dan kelas yang bertanggung jawab untuk analisis teknikal, prediksi, dan rekomendasi trading.
- Technical Analysis (indikator RSI, MACD, Bollinger Bands, dll.)
- Trade Advisor yang menghasilkan rekomendasi
- Algoritma prediksi (jika tersedia)

### data
Berisi modul untuk mengambil, memproses, dan mengelola data.
- Stock Data untuk mengambil data dari Yahoo Finance
- Transaction History untuk mengelola riwayat transaksi 
- Data cleaning dan preprocessing

### utils
Berisi fungsi dan kelas utilitas yang digunakan di seluruh aplikasi.
- Konfigurasi (stock_config)
- Helper functions
- Constants dan defines

### visualization
Berisi kode untuk visualisasi data dan chart.
- Chart generation (candlestick, technical analysis, dll.)
- Data plotting dan styling
- Formatter untuk output konsol

## Pola Desain

Aplikasi menggunakan pendekatan modular dengan prinsip-prinsip berikut:
- Separation of concerns (pemisahan tanggung jawab)
- Encapsulation (enkapsulasi)
- DRY (Don't Repeat Yourself)

## Kontribusi

Jika Anda ingin berkontribusi pada kode sumber:
1. Pastikan kode mengikuti gaya koding yang konsisten
2. Tambahkan docstrings dan komentar yang jelas
3. Tulis unit tests untuk fitur baru
4. Ikuti panduan kontribusi di file CONTRIBUTING.md
