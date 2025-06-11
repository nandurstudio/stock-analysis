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
