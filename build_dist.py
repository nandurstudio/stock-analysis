# Build script for Stock Analysis & Trading Recommendation Tool
# This script creates distribution files for the application

import os
import sys
import shutil
import subprocess
from datetime import datetime

def clean_build_dirs():
    """Clean build directories"""
    print("Cleaning build directories...")
    for dir_name in ['build', 'dist', 'stock_analysis_tool.egg-info']:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
            print(f"  Cleaned {dir_name}/")

def build_wheel():
    """Build wheel distribution package"""
    print("\nBuilding wheel package...")
    subprocess.run([sys.executable, "-m", "pip", "wheel", ".", "-w", "dist/"])

def build_sdist():
    """Build source distribution package"""
    print("\nBuilding source distribution...")
    subprocess.run([sys.executable, "setup.py", "sdist"])

def build_executable():
    """Build executable distribution"""
    print("\nBuilding executable...")
    # You need PyInstaller installed: pip install pyinstaller
    try:
        subprocess.run(["pyinstaller", 
                        "--onefile",
                        "--add-data", "stock_config.json;.",
                        "--name", "stock_analysis_tool",
                        "main.py"])
        
        # Move the executable to dist folder
        exe_path = os.path.join("dist", "stock_analysis_tool.exe")
        if os.path.exists(exe_path):
            print(f"  Executable created: {exe_path}")
    except Exception as e:
        print(f"  Error building executable: {e}")
        print("  Make sure you have PyInstaller installed: pip install pyinstaller")

def create_release_notes():
    """Create release notes in the dist directory"""
    version = "1.0.0"  # You might want to read this from your package
    
    with open(os.path.join("dist", "RELEASE_NOTES.md"), "w") as f:
        f.write(f"# Stock Analysis & Trading Recommendation Tool v{version}\n\n")
        f.write(f"Release Date: {datetime.now().strftime('%d %B %Y')}\n\n")
        f.write("## What's New\n\n")
        f.write("- Initial release of Stock Analysis & Trading Recommendation Tool\n")
        f.write("- Comprehensive technical analysis features\n")
        f.write("- Transaction history tracking\n")
        f.write("- Trading recommendations based on technical indicators\n\n")
        f.write("## Installation\n\n")
        f.write("See the README.md file in this directory for installation instructions.\n\n")
        f.write("## License\n\n")
        f.write("This software is released under the MIT License.\n")

def main():
    """Main build function"""
    print("=== Stock Analysis & Trading Recommendation Tool Build Script ===")
    
    # Clean directories first
    clean_build_dirs()
    
    # Create dist directory if it doesn't exist
    if not os.path.exists("dist"):
        os.mkdir("dist")
    
    # Build distribution packages
    build_wheel()
    build_sdist()
    build_executable()
    
    # Create release notes
    create_release_notes()
    
    print("\nBuild process completed. Distribution files are in the 'dist/' directory.")

if __name__ == "__main__":
    main()
