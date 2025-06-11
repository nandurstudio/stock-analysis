# Changelog

Semua perubahan penting pada proyek ini akan didokumentasikan dalam file ini.

Format berdasarkan [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
dan proyek ini mengikuti [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [v1.1.0] - 2025-06-11

### Added
- Antarmuka GUI (PyQt5) dengan tab Analisis Saham, Riwayat Transaksi, Tambah Transaksi, Kelola Saham, dan Tentang
- Fitur analisis saham via GUI dengan indikator loading/spinner dan output analisis lengkap
- Visualisasi chart candlestick interaktif di GUI, termasuk penanda posisi harga beli pengguna
- Tab Tentang yang dinamis, memuat info dari `developer_info.txt` via modul `developer_info.py`
- Batch file `run_gui_app.bat` untuk menjalankan aplikasi GUI secara instan

### Changed
- Integrasi logika analisis CLI ke dalam GUI
- Penyempurnaan tampilan dan navigasi pada GUI
- Penambahan chart candlestick dengan garis posisi user pada visualisasi

### Fixed
- Perbaikan bug minor pada proses analisis dan visualisasi
- Validasi input pada form transaksi di GUI

## [v1.0.0] - 2025-06-11

### Added
- Sistem analisis teknikal komprehensif
- Manajemen portofolio dan pencatatan transaksi
- Visualisasi data interaktif
- Rekomendasi trading otomatis
- Dokumentasi lengkap dalam Bahasa Indonesia
- Contoh penggunaan dan test cases
- Branding PyIDX Community dengan logo baru

### Changed
- Restrukturisasi kode untuk modularitas lebih baik
- Optimasi performa untuk analisis data besar
- Peningkatan akurasi prediksi

### Fixed
- Validasi input data yang lebih baik
- Penanganan error yang lebih robust
- Masalah kompatibilitas Python versi 3.9+
