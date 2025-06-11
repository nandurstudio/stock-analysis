# Panduan Penggunaan Stock Analysis and Trading Tool v1.0.1

## TL;DR - Ringkasan Cepat

### Menggunakan Aplikasi
- **Instalasi**: Pastikan Python 3.8+ terinstal, lalu jalankan `pip install -r requirements.txt`
- **Cara Menjalankan**: Double-click pada `run_stock_analyzer.bat` atau ketik `python main.py` di terminal
- **Menu Utama**: 1) Analisis Saham, 2) Lihat Riwayat Transaksi, 3) Tambah Transaksi, 4) Kelola Daftar Saham, 5) Keluar
- **Navigasi**: Tekan Enter tanpa input untuk kembali ke menu utama dari submenu manapun

### Analisis & Rekomendasi
- **Cara Analisis**: Pilih menu "1", pilih saham dari daftar atau ketik "0" untuk input manual
- **Jenis Rekomendasi**: 
  - 🟢 **BELI/TAMBAH POSISI**: Beli saham baru atau tambah posisi yang sudah ada
  - ⚪ **TAHAN**: Pertahankan posisi yang sudah ada, tunggu konfirmasi sinyal selanjutnya
  - 🔴 **JUAL**: Jual saham yang sudah Anda miliki (untuk mengamankan profit atau batasi rugi)
  - 🔴 **SHORT SELL**: Strategi saat harga berpotensi turun (untuk trader berpengalaman)
- **Parameter Penting**: Perhatikan Stop Loss, Target Price, Risk-Reward, dan Time Horizon

### Integrasi dengan IPOT
- **Mengambil Data**: 
  1. Login ke aplikasi IPOT → Menu "Portfolio" atau "Order" → Tab "History"/"Done"
  2. Catat detail transaksi: tanggal, kode saham, tipe BUY/SELL, harga, jumlah lot
- **Input Transaksi**: 
  1. Di Stock Analysis Tool, pilih menu "3", pilih saham, dan jenis transaksi
  2. Format tanggal: DD-MM-YY (misalnya 26-03-25) atau DDMMYY (260325)
  3. Format harga: tanpa pemisah ribuan (misalnya "8550" bukan "8.550")
  4. Format jumlah: dalam lot (1 lot = 100 lembar saham)

### Tips Penting
- Input transaksi secara kronologis (dari terlama ke terbaru)
- Pilih menu "2" untuk memeriksa posisi saham dan riwayat transaksi
- Cek posisi Anda sebelum mengambil keputusan berdasarkan rekomendasi
- SHORT SELL hanya muncul jika Anda tidak memiliki saham tersebut
- Tekan Enter tanpa mengetik apapun untuk kembali ke menu utama dari semua submenu

### Troubleshooting Cepat
- Jika aplikasi tidak berjalan: pastikan Python terinstal dan ada di PATH sistem
- Error saat mengambil data: periksa koneksi internet dan kebenaran kode saham
- Kesalahan input transaksi: gunakan menu "3" untuk menambahkan transaksi koreksi

---

## Persyaratan Sistem
- Python 3.8 atau lebih baru
- Paket Python yang diperlukan (lihat requirements.txt)
- Koneksi internet untuk mengambil data saham real-time

## Cara Instalasi

1. Pastikan Python sudah terinstal:
   ```
   python --version
   ```

2. Instal dependencies yang diperlukan:
   ```
   pip install -r requirements.txt
   ```

## Cara Menjalankan Program

Program dapat dijalankan dengan cara berikut:

```
python main.py
```

Atau dengan menggunakan file batch:

```
run_stock_analyzer.bat
```

3. **Memeriksa Sistem:**
   ```
   python cek_sistem.py
   ```

## Panduan Langkah-demi-Langkah

### Menjalankan Program dengan Click and Run

1. Buka Windows Explorer dan navigasikan ke folder `stock-analysis` Anda
2. Cari file `run_stock_analyzer.bat` di dalam folder tersebut
3. Double-click pada file tersebut untuk menjalankan program
4. Sebuah jendela terminal akan terbuka dengan menu utama aplikasi
5. Program akan memuat data dan menampilkan 5 menu pilihan (1-5)
6. Gunakan keyboard untuk memasukkan nomor menu yang ingin Anda pilih

Contoh tampilan menu:
```
====================================
STOCK ANALYSIS & TRADING TOOL v1.0.1
====================================

1. Analisis Saham Baru
2. Lihat Riwayat Transaksi
3. Tambah Transaksi Baru
4. Kelola Daftar Saham
5. Keluar

Pilihan Anda (1-5): _
```

> **Catatan Penting**: Di semua submenu, Anda dapat menekan Enter tanpa memasukkan input apapun untuk kembali ke menu utama. Ini membuat navigasi lebih mudah dan intuitif.

![Menu Utama](https://via.placeholder.com/500x300?text=Menu+Utama+Stock+Analysis+Tool)

### Menu-menu dalam Aplikasi

Program memiliki 5 menu utama:

#### 1. Analisis Saham Baru

Menu ini adalah fitur utama aplikasi untuk menganalisis saham dan mendapatkan rekomendasi trading berdasarkan analisis teknikal.

- **Langkah Penggunaan Lengkap**:
  1. **Pilih Menu**: Ketik "1" kemudian tekan Enter  2. **Pilih Saham**:
     - Lihat daftar saham yang ditampilkan dengan nomor urut
     - Ketik nomor saham yang ingin dianalisis (misal: "4" untuk BBCA)
     - ATAU ketik "-1" untuk input manual (kemudian masukkan kode saham tanpa .JK)
     - Atau tekan Enter tanpa input untuk kembali ke menu utama
  3. **Proses Analisis**:
     - Sistem akan menampilkan "Mengambil data [Kode Saham]..."
     - Tunggu beberapa saat selama data diambil dari server
     - Selanjutnya sistem akan menampilkan "Melakukan analisis teknikal..."
     - Sistem juga akan menganalisis riwayat transaksi Anda jika ada
  4. **Membaca Hasil Analisis**:
     - Hasil analisis akan ditampilkan dalam beberapa bagian terformat
     - Mulai dari informasi harga terakhir dan perubahan
     - Diikuti rekomendasi dalam kotak berbingkai
     - Kemudian detail teknikal dan penjelasan rekomendasi

- **Contoh Output dan Cara Membacanya**:
  ```
  ================================================================================
  HASIL ANALISIS UNTUK BBCA.JK (Bank Central Asia Tbk)
  ================================================================================
  Tanggal: 10 Juni 2025, 16:30:15
  Harga Terakhir: Rp 9,250.00
  Perubahan: +1.65% ↑
  --------------------------------------------------------------------------------

  **************************************************************************
  *                                                                        *
  *                 REKOMENDASI KUAT: BELI/TAMBAH POSISI 🟢                 *
  *                                                                        *
  **************************************************************************

  Stop Loss      : Rp 8,787.50
  Target Price   : Rp 9,712.50
  Risk-Reward    : 1:2.5
  Posisi Sizing  : 7% dari modal tersedia
  Time Horizon   : MEDIUM
  ```

- **Penjelasan Bagian-bagian Hasil Analisis**:
  1. **Header**: Menampilkan nama saham, tanggal dan waktu analisis
  2. **Informasi Harga**: Harga terakhir dan persentase perubahan dengan arah (↑/↓)
  3. **Kotak Rekomendasi**: Saran tindakan dengan indikator warna (🟢/⚪/🔴)
  4. **Parameter Trading**:
     - **Stop Loss**: Harga untuk keluar jika saham bergerak melawan prediksi
     - **Target Price**: Harga target untuk mengambil keuntungan
     - **Risk-Reward**: Rasio antara risiko dan potensi keuntungan (1:2.5 berarti potensi keuntungan 2.5x risiko)
     - **Posisi Sizing**: Saran persentase alokasi dana
     - **Time Horizon**: Perkiraan jangka waktu (SHORT/MEDIUM/LONG)

- **Tips untuk Pemula**:
  - **Perhatikan warna indikator**: 🟢 (beli), ⚪ (tahan), 🔴 (jual/short)
  - **Selalu perhatikan Risk-Reward**: Idealnya minimal 1:2 (potensi untung dua kali lipat dari risiko)
  - **Gunakan Stop Loss**: Tetapkan harga jual otomatis di broker Anda sesuai saran stop loss
  - **Posisi Sizing**: Jangan gunakan lebih dari persentase yang disarankan untuk satu saham

#### 2. Lihat Riwayat Transaksi

Menu ini memungkinkan Anda melihat semua transaksi yang telah Anda catat sebelumnya dan mengetahui posisi kepemilikan saham saat ini.

- **Langkah Penggunaan Menu Riwayat**:
  1. **Pilih Menu**: Ketik "2" kemudian tekan Enter
  2. **Lihat Ringkasan Portofolio**:
     - Program akan menampilkan ringkasan semua saham yang dimiliki
     - Untuk setiap saham, Anda bisa melihat:
       * Jumlah lot yang dimiliki saat ini
       * Harga rata-rata pembelian
       * Total nilai investasi
       * Unrealized P/L (keuntungan/kerugian sementara)
  3. **Detail Per Saham**:
     - Setelah ringkasan, program menampilkan detail untuk setiap saham
     - Data diurutkan berdasarkan tanggal transaksi (terlama ke terbaru)
  4. **Kembali ke Menu Utama**:
     - Setelah selesai melihat data, tekan Enter untuk kembali ke menu utama

- **Contoh Output dan Penjelasannya**:
  ```
  ==================================================
  RINGKASAN PORTOFOLIO (10 Juni 2025)
  ==================================================
  Total Saham        : 2 jenis
  Total Lot Aktif    : 14 lot
  Total Nilai        : Rp 3,847,000.00
  Unrealized P/L     : Rp 435,200.00 (+11.31%)
  Realized P/L       : Rp 447,000.00
  
  --------------------------------------------------
  SAHAM: BBCA.JK
  --------------------------------------------------
  Posisi Saat Ini    : 1 lot
  Harga Rata-rata    : Rp 8,550.00
  Total Investasi    : Rp 855,000.00
  Unrealized P/L     : Rp 395,500.00 (+46.26%)

  Transaksi:
  Tanggal      Tipe     Harga      Lot    Total          P/L
  ---------------------------------------------------------------------
  2025-03-26   BUY      8,550.00   1      Rp 855,000.00  -
  ```

- **Penjelasan Komponen Tampilan**:
  1. **Ringkasan Portofolio**:
     - **Total Saham**: Jumlah jenis saham dalam portofolio
     - **Total Lot Aktif**: Jumlah keseluruhan lot yang dimiliki
     - **Total Nilai**: Nilai investasi keseluruhan berdasarkan harga beli
     - **Unrealized P/L**: Keuntungan/kerugian yang belum direalisasi (paper profit/loss)
     - **Realized P/L**: Keuntungan/kerugian yang sudah direalisasi dari saham yang dijual

  2. **Detail Per Saham**:
     - **Posisi Saat Ini**: Jumlah lot yang masih dimiliki
     - **Harga Rata-rata**: Rata-rata harga beli per lembar
     - **Total Investasi**: Nilai total investasi pada saham ini
     - **Unrealized P/L**: Keuntungan/kerugian sementara berdasarkan harga pasar terakhir
     
  3. **Tabel Transaksi**:
     - **Tanggal**: Waktu transaksi dilakukan
     - **Tipe**: BUY (beli) atau SELL (jual)
     - **Harga**: Harga per lembar saat transaksi
     - **Lot**: Jumlah lot yang ditransaksikan
     - **Total**: Nilai total transaksi
     - **P/L**: Profit/Loss untuk transaksi jual

- **Tips untuk Pemula**:
  - Perhatikan "Unrealized P/L" untuk melihat performa investasi Anda saat ini
  - Bandingkan "Harga Rata-rata" beli dengan harga pasar saat ini
  - Gunakan informasi ini sebagai dasar keputusan untuk menambah posisi atau menjual

#### 3. Tambah Transaksi Baru

Menu ini digunakan untuk mencatat transaksi saham yang Anda lakukan, baik itu pembelian (BUY) maupun penjualan (SELL). Transaksi yang akurat sangat mempengaruhi akurasi rekomendasi saham yang diberikan sistem.

- **Langkah Penggunaan Terperinci**:  1. **Pilih Menu**: Ketik "3" kemudian tekan Enter
  
  2. **Pilih Saham**:
     - Sistem menampilkan daftar saham dengan nomor urut
     - Ketik nomor saham yang sesuai (misal: "4" untuk BBCA)
     - ATAU ketik "-1" untuk input manual (kemudian masukkan kode saham)
     - Atau cukup tekan Enter tanpa input untuk kembali ke menu utama
  
  3. **Pilih Jenis Transaksi**:
     - Sistem menampilkan dua pilihan:
       ```
       Jenis transaksi:
       1. BELI (BUY)
       2. JUAL (SELL)
       ```
     - Ketik "1" untuk transaksi pembelian atau "2" untuk penjualan
     - Tekan Enter untuk melanjutkan
  
  4. **Input Tanggal Transaksi**:
     - Sistem akan menampilkan format yang didukung:
       ```
       Format tanggal yang didukung:
       - DDMMYY (contoh: 110625 untuk 11 Jun 2025)
       - DD-MM-YY atau DD/MM/YY (contoh: 11-06-25)
       - YYYY-MM-DD (contoh: 2025-06-11)
       ```
     - Masukkan tanggal sesuai salah satu format yang didukung
     - Tekan Enter untuk melanjutkan
  
  5. **Input Harga Per Lembar**:
     - Sistem akan meminta: "Masukkan harga per lembar: Rp "
     - Masukkan harga per lembar tanpa pemisah ribuan (misal: "9250" bukan "9,250")
     - Tekan Enter untuk melanjutkan
  
  6. **Input Jumlah Lot**:
     - Sistem akan meminta: "Masukkan jumlah lot: "
     - Masukkan jumlah lot yang ditransaksikan (1 lot = 100 lembar)
     - Tekan Enter untuk melanjutkan
  
  7. **Verifikasi Hasil**:
     - Sistem akan memvalidasi input Anda
     - Untuk transaksi SELL, sistem akan memeriksa apakah Anda memiliki cukup lot
     - Jika valid, sistem menampilkan konfirmasi dan posisi terkini:
       ```
       Transaksi berhasil ditambahkan!
       
       Posisi BBCA.JK saat ini: 2 lot
       Harga rata-rata: Rp 8,750.00
       ```

- **Panduan Input yang Benar**:
  | Data yang Diinput | Format Benar | Format Salah |
  |-------------------|--------------|--------------|
  | Kode Saham        | BBCA         | BBCA.JK      |
  | Tanggal           | 26-03-25     | 26/03/2025   |
  | Harga             | 8550         | 8.550        |
  | Lot               | 1            | 1 lot        |

- **Validasi yang Dilakukan Sistem**:
  - **Untuk Transaksi JUAL**: memastikan jumlah lot yang dijual tidak lebih dari yang dimiliki
  - **Untuk Harga**: memastikan input berupa angka positif
  - **Untuk Jumlah Lot**: memastikan input berupa angka bulat positif

- **Tips Penting**:
  - Selalu masukkan transaksi sesuai urutan kronologis (dari terlama ke terbaru)
  - Gunakan tanggal sesuai dengan tanggal eksekusi di pasar (bukan tanggal order)
  - Perhatikan harga beli rata-rata setelah menambahkan transaksi untuk memantau performa investasi

#### 4. Kelola Daftar Saham

Menu ini digunakan untuk mengelola daftar saham yang ingin Anda pantau. Anda bisa menambahkan saham-saham favorit atau menghapus saham yang tidak ingin dipantau lagi.

- **Langkah Penggunaan Menu Kelola Daftar Saham**:
  1. **Pilih Menu**: Ketik "4" kemudian tekan Enter
  
  2. **Melihat Submenu Pengelolaan**:     - Sistem akan menampilkan daftar saham yang saat ini terdaftar
     - Kemudian sistem menampilkan dua opsi submenu dan instruksi untuk kembali:
       ```
       1. Tambah saham baru
       2. Hapus saham
       
       Tekan Enter tanpa input untuk kembali ke menu utama
       ```
    3. **Untuk Menambah Saham Baru**:
     - Ketik "1" kemudian tekan Enter
     - Masukkan kode saham tanpa suffix .JK (misal: "ANTM" untuk Aneka Tambang)
     - Tekan Enter untuk menyimpan
     - Sistem akan menampilkan konfirmasi: "Berhasil menambahkan ANTM"
  
  4. **Untuk Menghapus Saham**:
     - Ketik "2" kemudian tekan Enter
     - Masukkan nomor urut saham yang ingin dihapus (misal: "5")
     - Tekan Enter untuk menghapus
     - Sistem akan menampilkan konfirmasi: "Berhasil menghapus [KODE]"
  
  5. **Kembali ke Menu Utama**:
     - Cukup tekan Enter tanpa mengetik apapun di prompt pilihan menu

- **Tips Mengelola Daftar Saham**:
  - Tambahkan saham-saham yang aktif Anda perdagangkan
  - Tambahkan saham-saham bluechip untuk memantau pergerakan pasar secara umum
  - Hapus saham yang sudah tidak aktif atau tidak relevan
  - Jangan menambahkan terlalu banyak saham agar menu tetap rapi dan mudah dibaca

- **Kode Saham yang Didukung**:
  - Kode saham Indonesia di Bursa Efek Indonesia (BEI)
  - Format penulisan tanpa .JK (contoh: BBCA, TLKM, GOTO)
  - Sistem otomatis menambahkan suffix .JK saat mengakses data

#### 5. Keluar

Menu ini digunakan untuk keluar dari program Stock Analysis Tool.

- **Langkah Penggunaan**:
  - Ketik "5" kemudian tekan Enter
  - Program akan menampilkan pesan penutup
  - Program akan ditutup dan kembali ke Command Prompt Windows
  
- **Catatan Penting**:
  - Semua data transaksi yang telah diinput otomatis tersimpan
  - Tidak perlu menyimpan secara manual sebelum keluar
  - Disarankan untuk selalu keluar melalui menu ini daripada menutup jendela terminal secara langsung

## Tips Penggunaan

1. **Analisis Saham & Rekomendasi:**
   - Perhatikan rekomendasi dan tingkat keyakinan (confidence)
   - Baca penjelasan teknikal untuk memahami alasan rekomendasi
   - Gunakan level stop loss dan target profit yang disarankan
   - Pahami jenis rekomendasi:
     * **BELI/TAMBAH POSISI 🟢**: Saatnya membeli saham atau menambah posisi yang sudah ada
     * **TAHAN ⚪**: Tunggu dulu, belum ada sinyal kuat untuk beli maupun jual
     * **JUAL 🔴**: Jual saham yang Anda miliki untuk mengamankan keuntungan atau membatasi kerugian
     * **SHORT SELL 🔴**: Strategi untuk mengambil keuntungan dari penurunan harga saham (khusus untuk trader berpengalaman)

2. **Pencatatan Transaksi:**
   - Catat semua transaksi untuk mendapatkan rekomendasi yang lebih akurat
   - Format tanggal yang didukung: DDMMYY, DD-MM-YY, YYYY-MM-DD
   - Pastikan jumlah lot dan harga dimasukkan dengan benar

3. **Terminologi Trading:**
   - Pelajari terminologi trading di file `trading_terminology_guide.md` 
   - Pahami indikator-indikator teknikal yang digunakan
   - Pelajari strategi manajemen risiko yang direkomendasikan

## Panduan Troubleshooting Lengkap

Berikut adalah panduan untuk mengatasi masalah umum yang mungkin Anda temui saat menggunakan Stock Analysis Tool:

### 1. Masalah Instalasi dan Menjalankan Program

**Masalah**: "Python not recognized" atau "python is not recognized as an internal or external command"
- **Solusi 1**: Pastikan Python sudah terinstal dengan benar
  1. Buka Command Prompt dan ketik: `py --version` atau `python3 --version` 
  2. Jika tidak berfungsi, kemungkinan Python belum terinstal atau belum ada di PATH
  3. Download dan instal Python dari python.org, pastikan centang "Add Python to PATH"

- **Solusi 2**: Verifikasi PATH sistem
  1. Tekan Win+R, ketik "sysdm.cpl", lalu klik OK
  2. Pilih tab "Advanced", klik "Environment Variables"
  3. Di bagian "System variables", cari dan edit "Path"
  4. Pastikan lokasi instalasi Python (misalnya C:\Python312) ada dalam daftar
  5. Restart Command Prompt setelah mengedit PATH

**Masalah**: "ModuleNotFoundError: No module named 'X'"
- **Solusi**:
  1. Buka Command Prompt
  2. Navigasikan ke folder stock-analysis: `cd path\to\stock-analysis`
  3. Jalankan: `pip install -r requirements.txt`
  4. Jika masalah spesifik untuk modul tertentu, instal modul tersebut: `pip install [nama_modul]`

### 2. Masalah Koneksi dan Data

**Masalah**: "Error saat mengambil data saham" atau "Failed to download..."
- **Solusi 1**: Periksa koneksi internet
  1. Buka browser dan coba akses situs lain untuk memverifikasi koneksi internet
  2. Jika menggunakan proxy, pastikan pengaturan proxy sudah benar

- **Solusi 2**: Verifikasi kode saham
  1. Pastikan kode saham yang dimasukkan benar (format: KODE tanpa .JK)
  2. Periksa apakah saham tersebut masih aktif diperdagangkan

- **Solusi 3**: Coba lagi nanti
  1. Server data mungkin sedang sibuk atau maintenance
  2. Tunggu beberapa menit dan coba lagi

**Masalah**: "Data tidak akurat" atau "Harga tidak sesuai market"
- **Solusi 1**: Refresh data
  1. Keluar dari program (pilih menu 5)
  2. Jalankan kembali program
  3. Lakukan analisis saham yang sama lagi

- **Solusi 2**: Periksa tanggal sistem komputer
  1. Pastikan tanggal dan waktu sistem Anda sesuai dengan zona waktu Indonesia
  2. Tanggal yang tidak tepat dapat menyebabkan pengambilan data yang salah

### 3. Masalah dengan Transaksi

**Masalah**: "Error: Posisi saat ini hanya X lot!" saat mencoba menjual
- **Solusi**:
  1. Periksa posisi Anda di menu "2. Lihat Riwayat Transaksi"
  2. Pastikan jumlah lot yang ingin dijual tidak melebihi yang dimiliki
  3. Jika Anda yakin data transaksi salah, tambahkan transaksi pembelian yang hilang

**Masalah**: "Input tidak valid!" saat memasukkan data transaksi
- **Solusi**:
  1. Pastikan format tanggal sesuai dengan yang didukung (DDMMYY, DD-MM-YY, YYYY-MM-DD)
  2. Untuk harga dan jumlah lot, gunakan angka tanpa simbol khusus
  3. Contoh benar: "8550" (bukan "8.550" atau "Rp 8550")

**Masalah**: "Transaction history file corrupted" atau tidak bisa membaca file transaksi
- **Solusi**:
  1. Cek apakah file `transaction_history.csv` ada di folder `transaction_history`
  2. Jika rusak, cari backup di folder `backup/transaction_history_backup`
  3. Salin file backup terbaru ke folder `transaction_history` dan ganti namanya menjadi `transaction_history.csv`

### 4. Masalah dengan Format Tampilan

**Masalah**: Tampilan menu atau hasil analisis berantakan
- **Solusi 1**: Atur ukuran window terminal
  1. Klik kanan pada title bar terminal
  2. Pilih "Properties"
  3. Di tab "Layout", atur "Window Size" dengan Width minimal 120
  4. Klik OK untuk menyimpan pengaturan

- **Solusi 2**: Gunakan font monospace
  1. Klik kanan pada title bar terminal
  2. Pilih "Properties"
  3. Di tab "Font", pilih font monospace seperti "Consolas" atau "Courier New"
  4. Klik OK untuk menyimpan pengaturan

### 5. Bantuan Lebih Lanjut

Jika Anda mengalami masalah yang tidak tercantum di atas:
1. Periksa file `bug_fix_log.md` untuk solusi masalah umum terbaru
2. Jalankan `python cek_sistem.py` untuk diagnosis otomatis
3. Kontak pengembang dengan menyertakan:
   - Deskripsi masalah
   - Langkah-langkah untuk mereproduksi masalah
   - Screenshot pesan error (jika ada)
   - Hasil dari menjalankan `python cek_sistem.py`

## Panduan Memahami Indikator Teknikal

Program ini menggunakan berbagai indikator teknikal untuk memberikan rekomendasi trading yang akurat. Berikut adalah penjelasan sederhana dari setiap indikator:

### 1. RSI (Relative Strength Index)

RSI adalah indikator yang mengukur kecepatan dan perubahan pergerakan harga pada skala 0-100.

- **Cara Membaca RSI**:
  - **Nilai di atas 70**: Kondisi overbought (jenuh beli) - harga kemungkinan akan turun
  - **Nilai di bawah 30**: Kondisi oversold (jenuh jual) - harga kemungkinan akan naik
  - **Nilai antara 40-60**: Kondisi netral/normal

- **Contoh Penggunaan**:
  - RSI = 78 → Terlalu tinggi (overbought) → Sinyal untuk berhati-hati atau jual
  - RSI = 25 → Terlalu rendah (oversold) → Sinyal untuk mulai membeli

- **Ilustrasi Visual**:
  ```
  0 ----- 30 -------- 50 -------- 70 ----- 100
  [OVERSOLD] [NORMAL RANGE] [OVERBOUGHT]
       ↑                          ↑
   Sinyal Beli               Sinyal Jual
  ```

### 2. MACD (Moving Average Convergence Divergence)

MACD menunjukkan hubungan antara dua moving average dari harga saham dan membantu mengidentifikasi perubahan momentum.

- **Komponen MACD**:
  - **MACD Line**: Selisih antara EMA 12 dan EMA 26
  - **Signal Line**: EMA 9 dari MACD Line
  - **Histogram**: Perbedaan antara MACD Line dan Signal Line

- **Cara Membaca MACD**:
  - **MACD Line memotong Signal Line dari bawah ke atas**: Sinyal bullish (beli)
  - **MACD Line memotong Signal Line dari atas ke bawah**: Sinyal bearish (jual)
  - **Histogram positif dan membesar**: Momentum naik menguat
  - **Histogram negatif dan membesar**: Momentum turun menguat

- **Tips untuk Pemula**:
  - MACD lebih efektif pada pasar trending (yang bergerak dengan trend jelas)
  - Kombinasikan dengan indikator lain untuk konfirmasi

### 3. Bollinger Bands

Bollinger Bands terdiri dari 3 garis yang menunjukkan volatilitas dan area harga "normal" saham.

- **Komponen Bollinger Bands**:
  - **Middle Band**: SMA 20 dari harga (garis tengah)
  - **Upper Band**: SMA 20 + (2 × standar deviasi)
  - **Lower Band**: SMA 20 - (2 × standar deviasi)

- **Cara Membaca Bollinger Bands**:
  - **Harga menyentuh Upper Band**: Potensi overbought (jenuh beli)
  - **Harga menyentuh Lower Band**: Potensi oversold (jenuh jual)
  - **Bands menyempit**: Volatilitas rendah, ekspektasi pergerakan besar segera
  - **Bands melebar**: Volatilitas tinggi, trend kuat sedang berlangsung

- **Strategi Sederhana**:
  - "Bollinger Bounce": Beli saat harga mendekati lower band, jual saat mendekati upper band
  - "Bollinger Squeeze": Perhatikan saat bands menyempit untuk antisipasi breakout

### 4. Moving Averages (SMA/EMA)

Moving Average menghitung rata-rata harga selama periode tertentu untuk mengidentifikasi trend.

- **Jenis Moving Average**:
  - **SMA (Simple Moving Average)**: Rata-rata sederhana, semua harga memiliki bobot sama
  - **EMA (Exponential Moving Average)**: Memberikan bobot lebih pada data terbaru

- **Moving Average yang Digunakan**:
  - **SMA 20**: Trend jangka pendek (short-term)
  - **SMA 50**: Trend jangka menengah (medium-term)
  - **EMA 20**: Trend jangka pendek dengan respons lebih cepat

- **Sinyal Trading Penting**:
  - **Golden Cross**: SMA 20 memotong SMA 50 dari bawah ke atas (sinyal bullish)
  - **Death Cross**: SMA 20 memotong SMA 50 dari atas ke bawah (sinyal bearish)
  - **Harga di atas MA**: Trend naik (uptrend)
  - **Harga di bawah MA**: Trend turun (downtrend)
  - **Harga memantul dari MA**: Potensi support/resistance

### 5. Volume Analysis

Volume menunjukkan minat pasar dan kekuatan trend yang sedang berlangsung.

- **Cara Membaca Volume**:
  - **Volume tinggi + Harga naik**: Trend bullish kuat
  - **Volume tinggi + Harga turun**: Trend bearish kuat
  - **Volume rendah + Pergerakan harga**: Trend lemah, potensi pembalikan
  - **Volume meningkat secara signifikan**: Validasi breakout atau breakdown

- **OBV (On-Balance Volume)**:
  - Menambahkan volume saat harga naik
  - Mengurangi volume saat harga turun
  - OBV naik mendahului kenaikan harga: Akumulasi (bullish)
  - OBV turun mendahului penurunan harga: Distribusi (bearish)

### Kombinasi Indikator untuk Hasil Terbaik

Aplikasi ini mengkombinasikan semua indikator di atas dengan bobot yang sesuai:
- RSI (25%)
- MACD (20%)
- Bollinger Bands (15%)
- Moving Averages (25%)
- Volume (15%)

Bobot ini dijumlahkan untuk menentukan kekuatan sinyal yang menghasilkan rekomendasi akurat.

## Memahami Rekomendasi SHORT SELL

Sejak update Juni 2025, aplikasi ini dapat memberikan rekomendasi "SHORT SELL 🔴" yang perlu dipahami dengan baik:

### Apa itu Short Sell?
Short sell adalah strategi trading di mana investor meminjam saham dan menjualnya dengan harapan harga akan turun, kemudian membelinya kembali di harga yang lebih rendah untuk mendapatkan keuntungan dari selisihnya.

### Kapan Muncul Rekomendasi SHORT SELL?
Rekomendasi ini muncul ketika:
- Indikator teknikal menunjukkan kemungkinan harga akan turun
- Anda TIDAK memiliki saham tersebut dalam portofolio Anda

### Beda dengan Rekomendasi JUAL
- **JUAL 🔴**: Untuk melepas saham yang sudah Anda miliki
- **SHORT SELL 🔴**: Untuk mendapatkan keuntungan dari penurunan harga saham yang tidak Anda miliki

### Perhatian untuk Pemula
Short selling memiliki risiko lebih tinggi dibandingkan trading biasa karena:
1. Potensi kerugian tidak terbatas jika harga naik terus
2. Memerlukan margin/jaminan dari broker
3. Dikenakan biaya pinjam saham

Jika Anda pemula, sebaiknya pelajari terlebih dahulu atau konsultasikan dengan broker Anda sebelum melakukan short selling.

## Panduan Evaluasi Strategi dengan Fitur Backtesting

Stock Analysis Tool menyediakan fitur backtesting untuk membantu Anda mengevaluasi dan menyempurnakan strategi trading Anda berdasarkan data historis.

### Apa itu Backtesting?

Backtesting adalah proses mengevaluasi strategi trading menggunakan data historis untuk menentukan seberapa efektif strategi tersebut di masa lalu. Ini membantu mengidentifikasi kekuatan dan kelemahan strategi sebelum menggunakannya dengan uang sungguhan.

### Cara Menggunakan Fitur Backtesting

1. **Akses Menu Backtesting** (dari menu utama):
   - Jalankan program dengan `run_stock_analyzer.bat`
   - Pilih "1. Analisis Saham Baru"
   - Pilih saham yang ingin dianalisis
   - Setelah hasil analisis muncul, program akan menampilkan opsi "Lakukan backtesting?"

2. **Pilih Parameter Backtesting**:
   - **Periode**: Pilih rentang waktu untuk backtesting (3 bulan, 6 bulan, 1 tahun, atau 2 tahun)
   - **Strategi**: Pilih strategi yang ingin diuji:
     * "Rekomendasi Sistem" - Menggunakan rekomendasi yang dihasilkan oleh aplikasi
     * "RSI Basic" - Strategi berdasarkan indikator RSI saja
     * "MACD Crossover" - Strategi berdasarkan sinyal MACD crossover
     * "Moving Average" - Strategi berdasarkan perpotongan moving average
     * "Custom" - Menggunakan kombinasi parameter yang Anda tentukan

3. **Interpretasi Hasil Backtesting**:
   - Sistem akan menampilkan simulasi trading menggunakan strategi pilihan Anda
   - Hasil ditampilkan dalam format tabel dengan detail setiap transaksi
   - Di bagian bawah, Anda akan melihat ringkasan kinerja:
     ```
     =================== RINGKASAN KINERJA STRATEGI ===================
     Total Transaksi       : 14
     Win Rate              : 64.3% (9 profit, 5 loss)
     Profit Factor         : 2.3
     Rata-rata Profit      : 8.5%
     Rata-rata Loss        : -3.2%
     Drawdown Maksimum     : -7.5%
     Return Total          : +43.2%
     Return Annualized     : +28.7%
     Sharpe Ratio          : 1.8
     ================================================================
     ```

4. **Optimasi Strategi**:
   - Setelah melihat hasil, Anda bisa mengoptimasi strategi dengan mengubah parameter
   - Pilih "Uji dengan parameter berbeda" untuk mencoba variasi strategi
   - Bandingkan hasil dari berbagai strategi untuk menemukan yang paling sesuai

### Contoh Penggunaan Praktis

1. **Menguji Efektivitas Stop Loss**:
   - Pilih "Custom Strategy"
   - Tetapkan stop loss pada 5%, 7%, dan 10%
   - Bandingkan hasil untuk menemukan nilai optimal

2. **Membandingkan Strategi untuk Saham Berbeda**:
   - Lakukan backtesting untuk beberapa saham dengan strategi yang sama
   - Identifikasi saham mana yang paling sesuai dengan strategi tersebut

3. **Optimasi Time Horizon**:
   - Uji strategi yang sama dengan periode holding berbeda
   - Temukan periode optimal untuk jenis saham tertentu

### Tips Menggunakan Backtesting untuk Pemula

1. **Hindari Overfitting**: Strategi yang terlalu dioptimasi untuk data historis mungkin tidak bekerja dengan baik di masa depan
2. **Uji di Berbagai Kondisi Pasar**: Pastikan strategi Anda diuji baik di pasar bullish maupun bearish
3. **Mulai Sederhana**: Awali dengan strategi sederhana sebelum menambahkan kompleksitas
4. **Kombinasikan dengan Analisis Fundamental**: Backtesting hanya menggunakan data teknikal, pertimbangkan juga faktor fundamental

## Panduan Memahami Format Penjelasan Trading

Sejak update Juni 2025, format penjelasan trading telah ditingkatkan untuk menjadi lebih terstruktur, visual, dan mudah dipahami. Berikut panduan lengkap cara membaca format baru:

### 1. Format Penjelasan Indikator Teknikal

Setiap indikator teknikal disajikan dalam format yang konsisten dengan ikon yang menunjukkan arah sinyal:

```
📈 BULLISH MOMENTUM:
MACD menunjukkan momentum bullish (naik), yang berarti ada potensi kenaikan harga dalam waktu dekat
(uptrend). MACD positif menandakan bullish crossover, dimana rata-rata harga jangka pendek
melampaui rata-rata jangka panjang, tanda klasik untuk entry point.
```

```
📉 BEARISH SIGNAL:
RSI berada pada level 75.3 yang menunjukkan kondisi overbought (jenuh beli). Secara historis,
saham ini cenderung mengalami koreksi setelah RSI mencapai level di atas 70.
```

**Ikon yang Digunakan**:
- 📈 = Sinyal bullish (mendukung kenaikan harga)
- 📉 = Sinyal bearish (mendukung penurunan harga)
- ⚖️ = Sinyal netral atau mixed (campuran)
- ⚠️ = Peringatan atau kondisi yang perlu perhatian khusus

### 2. Format Kotak Rekomendasi

Rekomendasi utama ditampilkan dalam kotak berbingkai untuk menarik perhatian:

```
**************************************************************************
*                                                                        *
*                 REKOMENDASI KUAT: BELI/TAMBAH POSISI 🟢                 *
*                                                                        *
**************************************************************************
```

```
**************************************************************************
*                                                                        *
*                    REKOMENDASI KUAT: SHORT SELL 🔴                      *
*                                                                        *
**************************************************************************
```

**Jenis Rekomendasi**:
- **BELI/TAMBAH POSISI 🟢** - Saatnya membeli atau menambah saham yang sudah ada
- **TAHAN ⚪** - Tetap pegang saham yang sudah dimiliki, tapi jangan beli lagi
- **JUAL 🔴** - Jual saham yang Anda miliki untuk mengamankan profit/batasi rugi
- **SHORT SELL 🔴** - Untuk trader berpengalaman, sinyal bahwa harga kemungkinan turun

### 3. Format Detail Rekomendasi Trading

Detail rekomendasi disajikan dengan format bullet point yang mudah dibaca:

```
✅ TRADE RECOMMENDATION:
JUAL 🔴 (SELL)
- Meskipun ada momentum bullish dari MACD, kondisi overbought dari RSI menandakan waktu untuk JUAL
- Gunakan trailing stop 5% (Rp 8,550) untuk mengamankan keuntungan saat ini
- Pertimbangkan untuk menjual secara bertahap (scaling out) jika Anda memiliki posisi besar
```

### 4. Format Analisis Riwayat Trading

Aplikasi juga menganalisis riwayat trading Anda untuk memberikan insight personal:

```
💼 ANALISIS RIWAYAT TRADING:
- Win rate Anda untuk saham ini: 67% (2/3 transaksi profit)
- Rata-rata holding period: 35 hari
- Peringatan: Anda cenderung menjual terlalu cepat (rata-rata +15% profit)
```

### 5. Contoh Lengkap Format Rekomendasi

Berikut adalah contoh lengkap bagaimana rekomendasi ditampilkan:

```
================================================================================
HASIL ANALISIS UNTUK BBCA.JK (Bank Central Asia Tbk)
================================================================================
Tanggal: 10 Juni 2025, 16:30:15
Harga Terakhir: Rp 9,250.00
Perubahan: +1.65% ↑
--------------------------------------------------------------------------------

**************************************************************************
*                                                                        *
*                 REKOMENDASI KUAT: BELI/TAMBAH POSISI 🟢                 *
*                                                                        *
**************************************************************************

Stop Loss      : Rp 8,787.50
Target Price   : Rp 9,712.50
Risk-Reward    : 1:2.5
Posisi Sizing  : 7% dari modal tersedia
Time Horizon   : MEDIUM

--------------------------------------------------------------------------------
PENJELASAN SEDERHANA & TERMINOLOGI TRADING:
--------------------------------------------------------------------------------

📈 MOMENTUM KUAT:
MACD menunjukkan momentum bullish yang kuat. Histogram MACD positif dan terus 
meningkat, yang menandakan kekuatan pembeli (buyers) masih dominan.

📊 TREND ANALYSIS:
SMA 20 (Rp 8,950) berada di atas SMA 50 (Rp 8,750) membentuk Golden Cross sejak
15 hari yang lalu. Ini menandakan trend utama masih bullish (naik).

⚖️ VOLATILITAS:
Bollinger Bands saat ini cukup lebar (3.2%) menandakan volatilitas moderat.
Harga bergerak di area tengah bands, masih memiliki ruang untuk naik.

⚠️ PERINGATAN:
RSI saat ini di level 65, mendekati kondisi overbought (70+). Meskipun masih
bullish, mulai waspadai potensi koreksi jangka pendek.

✅ TRADE RECOMMENDATION:
BELI/TAMBAH POSISI 🟢 (BUY)
- Rekomendasi entry di harga saat ini (Rp 9,250) atau di support terdekat (Rp 9,100)
- Tetapkan stop loss di Rp 8,787.50 (5% di bawah harga masuk)
- Target profit di Rp 9,712.50 (5% di atas harga masuk)
- Time horizon: Medium term (1-3 bulan)

💼 ANALISIS RIWAYAT TRADING:
- Anda memiliki 1 lot BBCA.JK dengan harga rata-rata Rp 8,550
- Posisi saat ini profit +Rp 70,000 (+8.2%)
- Berdasarkan pola trading Anda, sebaiknya tahan posisi ini untuk potensi kenaikan lebih lanjut
```

### 6. Cara Membaca Konflik Sinyal

Terkadang indikator berbeda dapat memberikan sinyal yang bertentangan. Aplikasi akan menjelaskan seperti ini:

```
⚠️ KONFLIK SINYAL:
Terdapat konflik sinyal di mana RSI menunjukkan kondisi oversold (bullish), tetapi
MACD masih dalam trend bearish. Dalam kasus konflik seperti ini, rekomendasi lebih
condong ke TAHAN ⚪ sampai konfirmasi lebih jelas muncul.
```

Untuk melihat contoh lengkap format baru, buka file `backup/FORMAT_UPDATE_JUNI2025.md`.

## Panduan Lengkap Mengisi Data Transaksi dari IPOT

Aplikasi Stock Analysis Tool dirancang khusus untuk berintegrasi dengan data dari aplikasi trading IPOT, membantu menghasilkan rekomendasi yang akurat dan personal. Mengisi riwayat transaksi yang akurat sangat penting agar rekomendasi SHORT SELL dan JUAL bisa dibedakan dengan tepat berdasarkan posisi riil saham Anda.

### Langkah-Langkah Detail Mengakses Data IPOT

#### 1. Login dan Akses IPOT

1. **Membuka Aplikasi IPOT**:
   - **Desktop**: Buka website ipot.co.id di browser Anda
   - **Mobile**: Buka aplikasi IPOT di smartphone
   - Masukkan username dan password akun trading Anda
   - Klik tombol "Login" atau "Masuk" untuk melanjutkan
   - Tunggu hingga dashboard utama muncul

   ![Contoh Login IPOT](https://via.placeholder.com/400x200?text=Login+IPOT)

2. **Navigasi ke Halaman Portfolio/Transaksi**:

   **📱 Di Aplikasi Mobile IPOT**:
   - Tap ikon "Portfolio" atau "Portofolio" di menu bawah
   - Pilih tab "History" atau "Riwayat"
   - Untuk detail lebih lanjut, tap pada transaksi spesifik
   - Akan muncul layar dengan detail lengkap transaksi

   **💻 Di Website IPOT**:
   - Klik menu "Portfolio" atau "Portofolio" di navigasi atas
   - Pilih submenu "History Transaksi" atau "Riwayat Transaksi"
   - Untuk melihat transaksi lama, gunakan filter tanggal
   - Klik pada nomor transaksi untuk melihat detail lengkap

#### 2. Memahami Data Transaksi IPOT

**Format Standar Data di IPOT**:

| Kolom Data | Contoh di IPOT | Catatan untuk Stock Analysis Tool |
|------------|----------------|-----------------------------------|
| Order ID | 123456789 | Tidak perlu diinput ke aplikasi |
| Tanggal | 26 Mar 2025 14:35:22 | Perlu dikonversi ke format DD-MM-YY |
| Kode Saham | BBCA | Gunakan tanpa .JK |
| Board | Regular / RG | Tidak perlu diinput |
| Jenis | Buy (Beli) / Sell (Jual) | Pilih 1 untuk Buy, 2 untuk Sell |
| Harga | Rp 8.550 | Input angka saja tanpa pemisah ribuan: 8550 |
| Volume | 100 (1 lot) | Input dalam jumlah lot: 1 |
| Nilai Total | Rp 855.000 | Tidak perlu diinput, dihitung otomatis |
| Status | Done (Matched) | Hanya input transaksi dengan status "Done" |

**Contoh Screenshot Data IPOT**:

```
+-------------------+------------------------+----------+-----------+
| Order ID: 123456789                        | Status: Done        |
+-------------------+------------------------+----------+-----------+
| Date: 26 Mar 2025 14:35:22                 | Board: Regular      |
+-------------------+------------------------+----------+-----------+
| Stock: BBCA                                | Type: Buy           |
+-------------------+------------------------+----------+-----------+
| Price: Rp 8.550                            | Volume: 100 (1 lot) |
+-------------------+------------------------+----------+-----------+
| Value: Rp 855.000                          | Fee: Rp 1.710       |
+-------------------+------------------------+----------+-----------+
```

#### 3. Mengumpulkan Data Secara Sistematis

Untuk memastikan semua data penting terekam, ikuti langkah-langkah ini:

1. **Buat Template Pencatatan**:
   - Gunakan spreadsheet Excel/Google Sheets atau bahkan catatan kertas
   - Buat kolom untuk: Tanggal, Kode Saham, Jenis, Harga, Lot
   - Contoh format:

   | Tanggal | Kode | Jenis | Harga | Lot |
   |---------|------|-------|-------|-----|
   | 26-03-25 | BBCA | BUY | 8550 | 1 |
   | 15-05-25 | TLKM | SELL | 4350 | 2 |

2. **Filter Transaksi Penting**:
   - Di IPOT, gunakan filter untuk periode 6-12 bulan terakhir
   - Catat semua transaksi "BUY" dan "SELL" dengan status "Done/Matched"
   - Abaikan transaksi dengan status "Withdrawn" atau "Rejected"
   - Untuk saham yang masih Anda pegang, pastikan semua transaksi BUY tercatat

3. **Atur Secara Kronologis**:
   - Urutkan transaksi dari yang paling lama ke yang terbaru
   - Ini sangat penting untuk perhitungan rata-rata harga yang akurat

#### 4. Contoh Tampilan Detail Transaksi di Berbagai Versi IPOT

**IPOT Desktop (Web):**
```
Order Details:
Order ID: 123456789
Stock: BBCA
Exchange: IDX
Board: Regular
Order Date: 26 Mar 2025
Order Time: 14:35:22
Type: Buy
Price: Rp 8,550
Volume: 100
Value: Rp 855,000
Status: Matched
```

**IPOT Mobile:**
```
BBCA - Buy
26/03/2025 14:35
Price: 8550
Vol: 100
Status: Done
```

**IPOT NextG:**
```
Transaction Details
-----------------
Code: BBCA
Date: 26/03/2025
Time: 14:35:22
Side: Buy
Type: Day
Price: 8,550
Executed: 100 shares
Total: 855,000
```

### Cara Memasukkan Data IPOT ke Stock Analysis Tool

Setelah Anda mengumpulkan data transaksi dari IPOT, langkah selanjutnya adalah memasukkannya ke dalam Stock Analysis Tool dengan langkah-langkah berikut:

#### 1. Proses Input Data Langkah-demi-Langkah

1. **Menjalankan Program**:
   - Buka folder instalasi Stock Analysis Tool di komputer Anda
   - Double-click pada file `run_stock_analyzer.bat`
   - Tunggu hingga menu utama muncul dengan 5 pilihan opsi

2. **Akses Menu Transaksi**:
   - Ketik `3` untuk memilih "Tambah Transaksi Baru"
   - Tekan tombol Enter
   - Sistem akan menampilkan daftar saham yang tersedia

3. **Pilih Saham yang Sesuai**:
   - Lihat nomor urut saham yang ingin Anda tambahkan transaksinya
   - Ketik nomor tersebut dan tekan Enter
   - ATAU ketik `0` jika saham tidak ada dalam daftar, lalu masukkan kode saham manual

4. **Input Jenis Transaksi**:
   ```
   Jenis transaksi:
   1. BELI (BUY)
   2. JUAL (SELL)
   
   Pilih jenis transaksi (1-2): _
   ```
   - Ketik `1` untuk transaksi BUY (beli) dari IPOT
   - Ketik `2` untuk transaksi SELL (jual) dari IPOT
   - Tekan Enter untuk melanjutkan

5. **Input Tanggal**:
   ```
   Format tanggal yang didukung:
   - DDMMYY (contoh: 110625 untuk 11 Jun 2025)
   - DD-MM-YY atau DD/MM/YY (contoh: 11-06-25)
   - YYYY-MM-DD (contoh: 2025-06-11)
   
   Masukkan tanggal transaksi: _
   ```
   
   **Konversi Format Tanggal dari IPOT ke Stock Analysis Tool**:
   
   | Format IPOT | Konversi ke Format Stock Analysis |
   |-------------|----------------------------------|
   | 26 Mar 2025 | 26-03-25 atau 260325 |
   | 26/03/2025 | 26-03-25 atau 260325 |
   | 2025-03-26 | 2025-03-26 (tidak perlu diubah) |

   - Ketik tanggal dalam format yang didukung
   - Tekan Enter untuk melanjutkan

6. **Input Harga**:
   ```
   Masukkan harga per lembar: Rp _
   ```
   
   **Konversi Format Harga dari IPOT**:
   - Hapus pemisah ribuan dan desimal dari harga di IPOT
   - Misalnya, "Rp 8.550,00" diinput sebagai "8550"
   - Jangan memasukkan simbol mata uang (Rp) atau pemisah ribuan (.)
   - Tekan Enter untuk melanjutkan

7. **Input Jumlah Lot**:
   ```
   Masukkan jumlah lot: _
   ```
   
   **Konversi Jumlah Saham ke Lot**:
   - 1 lot = 100 lembar saham
   - Jika IPOT menampilkan "100 shares", maka input "1" (lot)
   - Jika IPOT menampilkan "500 shares", maka input "5" (lot)
   - Jika IPOT menampilkan volume dalam lot, langsung input jumlah yang sama
   - Tekan Enter untuk melanjutkan

8. **Verifikasi Hasil**:
   - Sistem akan memproses data dan menampilkan konfirmasi:
   ```
   Transaksi berhasil ditambahkan!
   
   Posisi BBCA.JK saat ini: 1 lot
   Harga rata-rata: Rp 8,550.00
   ```
   - Periksa informasi yang ditampilkan untuk memastikan data sudah benar
   - Program akan kembali ke menu utama setelah beberapa detik

#### 2. Menangani Kasus Khusus dalam Transaksi IPOT

1. **Transaksi Partial (Sebagian)**:
   - Di IPOT, terkadang order besar dieksekusi secara bertahap dengan harga berbeda
   - Untuk kasus ini, input setiap eksekusi sebagai transaksi terpisah
   - Gunakan tanggal dan waktu eksekusi tersebut untuk setiap transaksi

2. **Corporate Action (Aksi Korporasi)**:
   - **Stock Split**: Input sebagai transaksi beli tambahan dengan harga baru
   - Contoh: Split 1:2 dari 100 lembar @ Rp 10.000 menjadi 200 lembar @ Rp 5.000
   - Input: BUY 1 lot @ 5000 dengan tanggal aksi korporasi

3. **Transaksi Histori Lama**:
   - Jika memiliki saham yang dibeli lama sebelum menggunakan aplikasi ini
   - Input dengan harga beli rata-rata dan tanggal perkiraan pembelian
   - Ini penting untuk memastikan rekomendasi akurat berdasarkan posisi aktual

#### 3. Contoh Komprehensif Mengisi Data IPOT

**Skenario**: Berikut adalah riwayat transaksi seorang investor di IPOT

**Data dari IPOT**:
```
1. Order ID: 123456789
   Date: 26 Mar 2025 09:30:15
   Stock: BBCA
   Type: Buy
   Price: Rp 8,550
   Volume: 100 (1 lot)
   Status: Done (Matched)

2. Order ID: 234567890
   Date: 10 Apr 2025 10:15:22
   Stock: TLKM
   Type: Buy
   Price: Rp 4,250
   Volume: 500 (5 lot)
   Status: Done (Matched)

3. Order ID: 345678901
   Date: 15 May 2025 13:45:30
   Stock: BBCA
   Type: Sell
   Price: Rp 9,200
   Volume: 100 (1 lot)
   Status: Done (Matched)
```

**Proses Input ke Stock Analysis Tool**:

**Transaksi 1 - BBCA Buy**:
1. Pilih menu "3. Tambah Transaksi Baru"
2. Pilih saham BBCA dari daftar (misal nomor 4)
3. Pilih jenis transaksi: ketik "1" (BELI/BUY)
4. Input tanggal: "26-03-25"
5. Input harga: "8550"
6. Input jumlah lot: "1"
7. Verifikasi konfirmasi: "Posisi BBCA.JK saat ini: 1 lot"

**Transaksi 2 - TLKM Buy**:
1. Pilih menu "3. Tambah Transaksi Baru"
2. Pilih saham TLKM dari daftar (misal nomor 7)
3. Pilih jenis transaksi: ketik "1" (BELI/BUY)
4. Input tanggal: "10-04-25"
5. Input harga: "4250"
6. Input jumlah lot: "5"
7. Verifikasi konfirmasi: "Posisi TLKM.JK saat ini: 5 lot"

**Transaksi 3 - BBCA Sell**:
1. Pilih menu "3. Tambah Transaksi Baru"
2. Pilih saham BBCA dari daftar (misal nomor 4)
3. Pilih jenis transaksi: ketik "2" (JUAL/SELL)
4. Input tanggal: "15-05-25"
5. Input harga: "9200"
6. Input jumlah lot: "1"
7. Verifikasi konfirmasi: "Posisi BBCA.JK saat ini: 0 lot" dan "Realized P/L dari transaksi ini: Rp 65,000"

#### 4. Validasi dan Verifikasi Data

Setelah memasukkan semua data transaksi dari IPOT, sangat penting untuk memverifikasi bahwa data tersebut telah tercatat dengan benar di Stock Analysis Tool:

1. **Periksa Posisi Saat Ini**:
   - Pilih menu "2. Lihat Riwayat Transaksi"
   - Bandingkan posisi saham yang ditampilkan dengan portofolio aktual di IPOT
   - Pastikan jumlah lot dan harga rata-rata beli sesuai

2. **Verifikasi Riwayat Transaksi**:
   - Periksa bahwa semua transaksi tercatat dengan benar
   - Perhatikan urutan kronologis transaksi
   - Pastikan nilai Realized P/L untuk transaksi jual sudah benar

3. **Koreksi Jika Diperlukan**:
   - Jika ada kesalahan input, tidak ada fitur edit langsung
   - Untuk memperbaiki, tambahkan transaksi "koreksi":
     * Jika salah input BUY 2 lot (seharusnya 1 lot), tambahkan SELL 1 lot dengan tanggal dan harga yang sama
     * Jika salah input SELL 2 lot (seharusnya 1 lot), tambahkan BUY 1 lot dengan tanggal dan harga yang sama

#### 5. Tips Menjaga Akurasi Data IPOT dan Stock Analysis Tool

1. **Update Rutin**:
   - Segera input transaksi baru setelah eksekusi di IPOT
   - Lebih baik update transaksi harian daripada menunggu minggu/bulan

2. **Pengelompokan Transaksi**:
   - Untuk banyak transaksi kecil dengan saham dan harga sama pada hari yang sama
   - Bisa digabung menjadi satu transaksi dengan jumlah total lot

3. **Backup Rutin**:
   - Secara berkala salin file `transaction_history.csv` ke lokasi aman
   - Ini mencegah kehilangan data jika terjadi masalah dengan sistem

4. **Abaikan Transaksi Gagal**:
   - Jangan input transaksi dengan status "Withdrawn" atau "Rejected" di IPOT
   - Hanya input transaksi dengan status "Done" atau "Matched"

5. **Verifikasi Berkala**:
   - Setiap bulan, bandingkan posisi di Stock Analysis Tool dengan IPOT
   - Pastikan jumlah lot dan harga rata-rata sesuai

Dengan mengikuti panduan di atas, Anda akan memiliki data transaksi yang akurat yang memastikan rekomendasi SHORT SELL dan JUAL yang diberikan oleh Stock Analysis Tool sesuai dengan posisi riil portofolio Anda di IPOT.
Price: Rp 8,550
Volume: 100
Value: Rp 855,000
Status: Matched
```

**IPOT Mobile:**
```
BBCA - Buy
26/03/2025 14:35
Price: 8550
Vol: 100
Status: Done
```

**IPOT NextG:**
```
Transaction Details
-----------------
Code: BBCA
Date: 26/03/2025
Time: 14:35:22
Side: Buy
Type: Day
Price: 8,550
Executed: 100 shares
Total: 855,000
```

2. **Masuk ke Aplikasi Stock Analysis Tool**:
   - Jalankan program dengan double-click pada `run_stock_analyzer.bat`
   - Pilih menu "3. Tambah Transaksi Baru" dengan mengetik "3" lalu Enter

3. **Mengisi Data Transaksi Step-by-Step**:
   a. **Pilih Saham**:
      - Lihat daftar saham yang ditampilkan
      - Ketik nomor saham (contoh: 4 untuk BBCA) atau ketik "0" lalu Enter untuk input manual
      - Jika input manual, ketik kode saham (contoh: "BBCA") dan tekan Enter
   
   b. **Pilih Jenis Transaksi**:
      - Ketik "1" untuk BELI (BUY) atau "2" untuk JUAL (SELL) sesuai transaksi di IPOT
      - Tekan Enter
   
   c. **Masukkan Tanggal**:
      - Format tanggal yang diterima: "DDMMYY", "DD-MM-YY", atau "YYYY-MM-DD"
      - Contoh untuk 26 Maret 2025: "260325", "26-03-25", atau "2025-03-26"
      - Ketik format yang Anda pilih dan tekan Enter
   
   d. **Masukkan Harga**:
      - Ketik harga per lembar tanpa format ribuan (contoh: "8550" bukan "8.550")
      - Tekan Enter
   
   e. **Masukkan Jumlah Lot**:
      - Ketik jumlah lot (contoh: "1" untuk 100 lembar saham)
      - Tekan Enter

4. **Verifikasi Data**:
   - Sistem akan menampilkan ringkasan transaksi yang baru ditambahkan
   - Cek apakah semua data sudah benar
   - Jika ada kesalahan, Anda bisa menambahkan transaksi koreksi nanti

### Contoh Lengkap Pengisian Data dari IPOT

**Data di IPOT**:
```
Order ID: 123456789
Date: 26 Mar 2025
Stock: BBCA
Board: Regular
Type: Buy
Price: Rp 8.550
Volume: 100 (1 lot)
Status: Done (Matched)
```

**Langkah Input di Stock Analysis Tool**:

1. Pilih "3" untuk menu "Tambah Transaksi Baru"
2. Tampilan daftar saham muncul
3. Ketik "4" untuk memilih BBCA (atau "0" lalu "BBCA" jika input manual)
4. Pilih jenis transaksi dengan mengetik "1" untuk BELI (BUY)
5. Untuk tanggal, ketik "26-03-25" (atau format lain yang didukung)
6. Untuk harga, ketik "8550"
7. Untuk jumlah lot, ketik "1"
8. Sistem akan menampilkan pesan:
   ```
   Transaksi berhasil ditambahkan!
   
   Posisi BBCA.JK saat ini: 1 lot
   Harga rata-rata: Rp 8,550.00
   ```

### Tips Penting untuk Mengisi Data IPOT

1. **Mengisi Transaksi Secara Kronologis**:
   - Sebaiknya isi transaksi dari yang paling lama ke yang terbaru
   - Ini memastikan perhitungan posisi dan rata-rata harga yang akurat

2. **Memeriksa Posisi Sebelum Transaksi Jual**:
   - Pastikan Anda memiliki cukup lot sebelum menginput transaksi jual
   - Sistem akan memvalidasi dan menolak jika mencoba menjual lebih dari yang dimiliki

3. **Filter Data Transaksi IPOT**:
   - Di aplikasi IPOT, gunakan filter tanggal untuk menemukan transaksi lama
   - Biasanya bisa difilter hingga 3-6 bulan ke belakang tergantung paket IPOT Anda

4. **Menangani Special Order**:
   - Untuk transaksi Cash Dividend, Stock Split, Bonus, atau Right Issue
   - Saat ini belum didukung otomatis, hubungi pengembang untuk petunjuk lebih lanjut

Aplikasi akan mencatat transaksi dan menggunakan data ini untuk menghasilkan rekomendasi yang lebih akurat berdasarkan posisi dan riwayat trading Anda.

## Tanggung Jawab

Program ini hanya memberikan rekomendasi berdasarkan analisis teknikal dan tidak menjamin keuntungan investasi. Pengguna tetap bertanggung jawab penuh atas keputusan investasi yang diambil. Untuk memahami lebih jauh mengenai terminologi dan strategi trading, silakan baca file `trading_terminology_guide.md`.
