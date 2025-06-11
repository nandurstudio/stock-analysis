# Stock Analysis and Trading Recommendation Tool v1.0

## Deskripsi
Stock Analysis and Trading Recommendation Tool adalah aplikasi command-line berbasis Python yang membantu investor dan trader menganalisis saham, melacak transaksi trading, dan mendapatkan rekomendasi berdasarkan analisis teknikal dan fundamental.

## Fitur Utama
1. **Analisis Teknikal Komprehensif**
   - Menghitung indikator teknikal seperti RSI, MACD, Bollinger Bands, SMA, EMA
   - Visualisasi data saham dan indikator teknikal
   - Mengidentifikasi trend dan sinyal trading

2. **Pelacakan Transaksi**
   - Mencatat transaksi BUY/SELL di file CSV
   - Menghitung profit/loss untuk setiap transaksi
   - Menyimpan detail seperti harga, jumlah lot, tanggal, dan status transaksi

3. **Rekomendasi Trading Profesional**
   - Memberikan rekomendasi BUY/HOLD/SELL berdasarkan analisis teknikal
   - Menghitung tingkat kepercayaan rekomendasi
   - Menyertakan alasan dan penjelasan sederhana untuk rekomendasi

4. **Analisis Histori Transaksi**
   - Menganalisis pola trading berdasarkan transaksi sebelumnya
   - Menghitung win rate dan metrik kinerja trading
   - Menyesuaikan rekomendasi berdasarkan gaya dan preferensi trading pengguna

5. **Manajemen Risiko**
   - Merekomendasikan level stop loss dan target profit
   - Menghitung rasio risk-to-reward untuk setiap trade
   - Menyarankan posisi sizing berdasarkan profil risiko

## Cara Penggunaan

### Instalasi
1. Clone repository ini:
   ```
   git clone https://github.com/username/stock-analysis.git
   cd stock-analysis
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

### Menjalankan Aplikasi
Untuk menjalankan versi terbaru (v1.0):
```
python main_v2.py
```

Untuk menjalankan versi lama:
```
python main.py
```

### Menu Utama
Aplikasi memiliki 5 menu utama:
1. **Analisis Saham Baru**
   - Menganalisis saham dan memberikan rekomendasi
   - Menampilkan visualisasi data teknikal
   - Memberikan rekomendasi trading dengan penjelasan detail

2. **Lihat Riwayat Transaksi**
   - Menampilkan semua transaksi yang telah dilakukan
   - Menghitung profit/loss dari setiap transaksi
   - Menampilkan ringkasan posisi untuk setiap saham

3. **Tambah Transaksi Baru**
   - Mencatat transaksi beli/jual baru
   - Memvalidasi transaksi (misal: tidak bisa jual lebih dari yang dimiliki)
   - Menghitung realized profit/loss untuk transaksi jual

4. **Kelola Daftar Saham**
   - Menambahkan saham baru ke watchlist
   - Menghapus saham dari watchlist
   - Mengatur daftar saham default

5. **Keluar**
   - Keluar dari aplikasi

### Format File Transaksi
File transaksi disimpan di `transaction_history/transaction_history.csv` dengan format:
- `entry_date`: Tanggal input transaksi
- `transaction_date`: Tanggal eksekusi transaksi 
- `symbol`: Kode saham (contoh: BBCA.JK)
- `transaction_type`: Jenis transaksi (BUY/SELL)
- `price`: Harga per lembar saham
- `lot_size`: Jumlah lot (1 lot = 100 lembar)
- `shares`: Jumlah lembar saham (lot_size * 100)
- `total_value`: Nilai total transaksi (price * shares)
- `running_lot_balance`: Sisa lot setelah transaksi
- `avg_buy_price`: Harga rata-rata pembelian
- `realized_pnl`: Profit/Loss yang direalisasi (untuk transaksi SELL)
- `unrealized_pnl`: Profit/Loss paper (untuk transaksi BUY)
- `pnl_percentage`: Persentase Profit/Loss
- `holding_period`: Durasi hold dalam hari
- `status`: Status transaksi (EXECUTED, PENDING, CANCELLED)

## Terminologi Trading yang Digunakan

### Indikator Teknikal
- **RSI (Relative Strength Index)**: Indikator momentum yang mengukur kecepatan dan perubahan pergerakan harga.
  - **Overbought**: RSI > 70, menandakan potensi koreksi turun
  - **Oversold**: RSI < 30, menandakan potensi pembalikan naik

- **MACD (Moving Average Convergence Divergence)**: Indikator trend-following yang menunjukkan hubungan antara dua moving averages.
  - **Bullish Crossover**: MACD line memotong signal line dari bawah ke atas
  - **Bearish Crossover**: MACD line memotong signal line dari atas ke bawah

- **Bollinger Bands**: Indikator volatilitas yang terdiri dari tiga garis.
  - **Upper Band**: Garis atas, biasanya 2 standar deviasi di atas SMA
  - **Middle Band**: Simple Moving Average (SMA)
  - **Lower Band**: Garis bawah, biasanya 2 standar deviasi di bawah SMA

### Strategi Trading
- **Scaling Out**: Menjual sebagian posisi untuk mengamankan profit
- **Averaging Down**: Menambah posisi pada harga yang lebih rendah untuk menurunkan harga rata-rata
- **Trailing Stop**: Stop loss yang bergerak mengikuti pergerakan harga untuk memaksimalkan profit
- **Stop Loss**: Batas harga untuk membatasi kerugian
- **Take Profit**: Batas harga untuk mengambil keuntungan
- **Buy on Dips**: Membeli saat terjadi koreksi kecil dalam uptrend
- **Sell on Rally**: Menjual saat terjadi kenaikan kecil dalam downtrend

### Kondisi Market
- **Accumulation Phase**: Fase dimana investor institusional mulai mengakumulasi saham
- **Distribution Phase**: Fase dimana investor besar mulai melepas (menjual) saham mereka
- **Bullish Momentum**: Tren kenaikan harga yang kuat
- **Bearish Momentum**: Tren penurunan harga yang kuat
- **Breakout**: Harga yang bergerak keluar dari rentang konsolidasi
- **Drawdown**: Penurunan dari titik tertinggi ke titik terendah dalam suatu periode

## Kontribusi
Jika Anda ingin berkontribusi pada proyek ini, silakan fork repository, buat branch untuk fitur atau bug fix yang Anda kerjakan, dan ajukan pull request.

## Lisensi
MIT License
