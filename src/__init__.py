"""
Stock Analysis and Trading Recommendation Tool
=============================================

This package provides tools for technical analysis of stocks,
transaction history tracking, trading recommendations, and
data visualization.

Modules:
    analysis: Technical and fundamental analysis modules
    data: Data retrieval and management modules
    utils: Utility and helper functions
    visualization: Charting and data visualization tools

Usage:
    >>> from src.data import StockData
    >>> from src.analysis import TechnicalAnalysis
    >>> stock = StockData()
    >>> data = stock.fetch_data("AAPL", period="1y")
    >>> tech = TechnicalAnalysis()
    >>> data = tech.add_all_indicators(data)
"""

__version__ = "1.1.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"
__license__ = "MIT"
