# GUI entry point script for Stock Analysis Tool
import os
import sys
# Add the project root directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.gui.app_gui import main

if __name__ == '__main__':
    main()
