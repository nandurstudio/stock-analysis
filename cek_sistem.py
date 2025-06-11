"""
Script untuk memeriksa kesiapan sistem untuk menjalankan
Stock Analysis and Trading Recommendation Tool
"""

import sys
import os
import importlib
import platform

def check_python_version():
    """Check if Python version meets requirements"""
    print("\nMemeriksa versi Python...")
    major = sys.version_info.major
    minor = sys.version_info.minor
    micro = sys.version_info.micro
    is_valid = major >= 3 and minor >= 8
    version_str = f"{major}.{minor}.{micro}"
    
    if is_valid:
        print(f"✅ Versi Python {version_str} kompatibel")
    else:
        print(f"❌ Versi Python {version_str} TIDAK kompatibel. Dibutuhkan Python 3.8+")
    
    return is_valid

def check_required_modules():
    """Check if required modules are installed"""
    print("\nMemeriksa modul yang diperlukan...")
    
    required_modules = [
        'pandas', 'numpy', 'matplotlib', 'seaborn', 'ta', 
        'yfinance', 'sklearn', 'keyboard', 'pytz'
    ]
    
    missing_modules = []
    for module in required_modules:
        try:
            importlib.import_module(module)
            print(f"✅ Modul {module} terinstal")
        except ImportError:
            print(f"❌ Modul {module} TIDAK terinstal")
            missing_modules.append(module)
    
    if missing_modules:
        print("\n❗ Modul yang hilang. Harap instal dengan perintah:")
        print(f"pip install {' '.join(missing_modules)}")
        return False
    
    return True

def check_file_structure():
    """Check if necessary files exist"""
    print("\nMemeriksa struktur file...")
    required_files = [
        'main.py',
        'src/data/stock_data.py',
        'src/analysis/technical.py',
        'src/visualization/charts.py',
        'src/data/transaction_history.py',
        'src/analysis/trade_advisor.py'
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            print(f"❌ File {file} tidak ditemukan")
            missing_files.append(file)
        else:
            print(f"✅ File {file} ditemukan")
    
    if missing_files:
        print("\n❗ File yang diperlukan tidak ditemukan")
        return False
    
    return True

def check_transaction_dir():
    """Check if transaction directory exists and create if needed"""
    print("\nMemeriksa direktori transaksi...")
    
    transaction_dir = "transaction_history"
    if not os.path.exists(transaction_dir):
        print(f"❌ Direktori {transaction_dir} tidak ditemukan, membuat direktori...")
        try:
            os.makedirs(transaction_dir)
            print(f"✅ Direktori {transaction_dir} berhasil dibuat")
        except Exception as e:
            print(f"❌ Gagal membuat direktori {transaction_dir}: {str(e)}")
            return False
    else:
        print(f"✅ Direktori {transaction_dir} ditemukan")
    
    return True

def check_internet_connection():
    """Check internet connection by trying to connect to Yahoo Finance"""
    print("\nMemeriksa koneksi internet untuk mengambil data saham...")
    
    try:
        import yfinance as yf
        ticker = yf.Ticker("MSFT")
        ticker.info
        print("✅ Koneksi internet aktif, dapat mengakses Yahoo Finance")
        return True
    except Exception as e:
        print("❌ Tidak dapat terhubung ke Yahoo Finance. Periksa koneksi internet")
        print(f"Error: {str(e)}")
        return False

def print_system_info():
    """Print system information"""
    print("\n" + "="*50)
    print("INFORMASI SISTEM")
    print("="*50)
    print(f"Sistem Operasi: {platform.system()} {platform.version()}")
    print(f"Python: {sys.version}")
    print(f"Path Python: {sys.executable}")
    print(f"Direktori Kerja: {os.getcwd()}")
    print("="*50)

def main():
    """Main function to check system readiness"""
    print("\n" + "="*50)
    print("PEMERIKSAAN SISTEM STOCK ANALYSIS TOOL")
    print("="*50)
    
    # Print system info
    print_system_info()
    
    # Run checks
    python_ok = check_python_version()
    modules_ok = check_required_modules()
    files_ok = check_file_structure()
    transaction_dir_ok = check_transaction_dir()
    internet_ok = check_internet_connection()
      # Summary
    print("\n" + "="*50)
    print("HASIL PEMERIKSAAN SISTEM")
    print("="*50)
    if all([python_ok, modules_ok, files_ok, transaction_dir_ok, internet_ok]):
        print("✅ SISTEM SIAP!")
        print("Anda dapat menjalankan Stock Analysis Tool dengan perintah:")
        print("   python main.py")
        print("   atau dengan batch file: run_stock_analyzer.bat")
    else:
        print("❌ SISTEM BELUM SIAP!")
        print("Harap perbaiki masalah yang ditemukan sebelum menjalankan aplikasi")
        print("\nUntuk informasi lebih lanjut, baca panduan_penggunaan.md")
    print("="*50)

if __name__ == "__main__":
    main()
