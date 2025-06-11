@echo off
REM Jalankan GUI Stock Analysis Tool
REM Pastikan virtual environment sudah aktif jika ada

REM Aktifkan virtual environment jika ada
IF EXIST .venv\Scripts\activate (
    call .venv\Scripts\activate
)

REM Jalankan aplikasi GUI
python -m src.gui.app_gui
