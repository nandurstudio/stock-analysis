# Panduan GitHub Release untuk Stock Analysis & Trading Recommendation Tool

## Persiapan Release

1. **Pastikan versi terbaru**:
   - Update nomor versi di `setup.py`
   - Update CHANGELOG.md dengan fitur terbaru

2. **Build distribusi**:
   ```bash
   python build_dist.py
   ```
   
   Ini akan membuat file distribusi di folder `dist/`:
   - `stock_analysis_tool-X.Y.Z.tar.gz` (Source distribution)
   - `stock_analysis_tool-X.Y.Z-py3-none-any.whl` (Wheel distribution)
   - `stock_analysis_tool.exe` (Executable untuk Windows)

3. **Test distribusi**:
   - Pastikan executable berjalan dengan baik
   - Pastikan wheel package dapat diinstal dan berjalan

## Membuat GitHub Release

1. **Login ke GitHub**:
   - Buka repositori proyek Anda

2. **Buat release baru**:
   - Klik tab "Releases"
   - Klik "Draft a new release"
   - Masukkan tag versi (contoh: `v1.1.0`)
   - Masukkan judul release (contoh: "Stock Analysis & Trading Recommendation Tool v1.1.0")
   - Salin isi file `dist/RELEASE_NOTES.md` ke deskripsi release

3. **Upload file distribusi**:
   - Drag & drop atau pilih semua file dari folder `dist/`
   - Tambahkan file `README.md` dan `LICENSE` jika perlu

4. **Publikasikan release**:
   - Klik "Publish release" jika langsung ingin mempublikasikan
   - Atau klik "Save draft" untuk menyimpan sebagai draft terlebih dahulu

## Setelah Release

1. **Pemberitahuan**:
   - Informasikan pengguna tentang release baru melalui media sosial, forum, atau email

2. **Dokumentasi**:
   - Pastikan dokumentasi di `docs/` sudah diperbarui untuk versi terbaru

3. **Feedback**:
   - Monitor isu yang mungkin muncul setelah release
   - Siapkan hotfix jika diperlukan

## Checklist Release

- [ ] Update nomor versi di kode
- [ ] Update CHANGELOG.md
- [ ] Build distribusi berhasil
- [ ] Test semua file distribusi
- [ ] Create tag di Git
- [ ] Upload file distribusi ke GitHub
- [ ] Publikasikan release di GitHub
- [ ] Informasikan pengguna tentang release baru
