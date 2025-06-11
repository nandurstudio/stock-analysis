@echo off
REM Install Stock Analysis Tool
echo Installing Stock Analysis and Trading Recommendation Tool...

REM Check if Python is installed
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Python tidak ditemukan. Mohon install Python 3.9 atau lebih baru.
    echo Download Python dari https://www.python.org/downloads/
    pause
    exit /b 1
)

REM Create virtual environment (optional)
echo.
echo Checking for virtual environment...
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
    echo Virtual environment created.
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate

REM Install package in development mode
echo.
echo Menginstall package dan dependencies...
python -m pip install --upgrade pip
python -m pip install -e .

REM Install test dependencies
echo.
echo Menginstall dependencies untuk testing...
python -m pip install pytest pytest-cov

echo.
echo Instalasi selesai!
echo.
echo Anda dapat menjalankan aplikasi dengan:
echo.
echo     1. Mengaktifkan virtual environment: venv\Scripts\activate
echo     2. Menjalankan aplikasi: stock-analyzer
echo.
echo atau dengan menjalankan:
echo.
echo     run_stock_analyzer.bat
echo.
echo Untuk menjalankan tests:
echo.
echo     pytest
echo.
pause
