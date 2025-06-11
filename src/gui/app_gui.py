"""
App entry point for GUI version of main.py
"""
import sys
from PyQt5.QtWidgets import QApplication
from src.gui.main_app_window import MainAppWindow

def main():
    app = QApplication(sys.argv)
    window = MainAppWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
