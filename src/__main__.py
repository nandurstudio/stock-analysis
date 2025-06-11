"""
Main entry point for the Stock Analysis Tool package.
This module is executed when the package is run with 'python -m src'.
"""
import sys
import os

# Add the parent directory to sys.path to allow imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.main import run

if __name__ == "__main__":
    run()
