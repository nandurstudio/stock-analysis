# Panduan Kontribusi

Terima kasih telah mempertimbangkan untuk berkontribusi pada Stock Analysis and Trading Recommendation Tool! Panduan ini berisi informasi tentang cara kontribusi ke proyek ini.

## Cara Berkontribusi

### Melaporkan Bug
Jika Anda menemukan bug, silahkan buat issue baru dengan label `bug`. Harap sertakan:

- Langkah-langkah untuk mereproduksi bug
- Output yang diharapkan vs output sebenarnya
- Screenshot jika memungkinkan
- Versi Python dan sistem operasi Anda

### Mengusulkan Fitur Baru
Untuk mengusulkan fitur baru:

1. Buat issue dengan label `enhancement`
2. Jelaskan fitur yang diusulkan secara detail
3. Jelaskan manfaat dari fitur tersebut untuk pengguna

### Pull Request
Untuk membuat pull request:

1. Fork repository ini
2. Buat branch baru (`git checkout -b feature/amazing-feature`)
3. Commit perubahan Anda (`git commit -m 'Add some amazing feature'`)
4. Push ke branch (`git push origin feature/amazing-feature`)
5. Buka Pull Request

## Standar Kode

### Gaya Kode
- Ikuti [PEP 8](https://peps.python.org/pep-0008/) untuk Python
- Gunakan docstring untuk fungsi dan kelas
- Tulis komentar untuk kode yang kompleks

### Pengujian
- Pastikan fitur baru disertai dengan unit test yang sesuai
- Jalankan semua test sebelum membuat pull request

## Struktur Proyek
```
stock-analysis/
│
├── docs/                # Dokumentasi
│   ├── images/          # Gambar untuk dokumentasi
│   │   └── ...
│   └── ...
│
├── src/                 # Kode sumber
│   ├── analysis/        # Modul analisis
│   ├── data/            # Modul pengelolaan data
│   ├── utils/           # Fungsi utilitas
│   └── visualization/   # Modul visualisasi
│
├── tests/               # Unit test
│
├── transaction_history/ # Data transaksi
│
└── analysis_results/    # Hasil analisis
```

## Proses Rilis
1. Versi baru akan dirilis setelah melalui pengujian
2. Perubahan akan didokumentasikan di CHANGELOG.md

## Kode Etik
Proyek ini mengikuti [Contributor Covenant](https://www.contributor-covenant.org/version/2/0/code_of_conduct/).

Terima kasih atas kontribusi Anda!
