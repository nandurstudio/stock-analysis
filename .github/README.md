# GitHub Configuration for Stock Analysis Tool

Folder ini berisi konfigurasi GitHub untuk Stock Analysis and Trading Recommendation Tool.

## Struktur Folder

### ISSUE_TEMPLATE
Berisi template untuk GitHub Issues:
- `bug_report.md`: Template untuk melaporkan bug
- `feature_request.md`: Template untuk mengusulkan fitur baru

### workflows
Berisi GitHub Action workflows:
- `python-tests.yml`: Workflow untuk menjalankan otomatisasi testing

## Menggunakan Issue Templates

1. Buka tab Issues di GitHub repository
2. Klik "New Issue"
3. Pilih template yang sesuai (Bug Report atau Feature Request)
4. Isi template dengan informasi yang diminta
5. Submit issue

## GitHub Actions Workflows

Workflow `python-tests.yml` secara otomatis menjalankan test pada:
- Setiap push ke branch main
- Setiap pull request ke branch main

Workflow ini menguji kode dengan Python versi 3.9, 3.10, dan 3.11 untuk memastikan kompatibilitas.
