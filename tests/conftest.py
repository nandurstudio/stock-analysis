"""
Pytest configuration file for Stock Analysis Tool tests.
"""
import os
import sys
import pytest
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Add src to the Python path for all tests
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


@pytest.fixture
def mock_stock_data():
    """
    Fixture that creates mock stock data suitable for testing.
    Returns a pandas DataFrame with OHLCV data.
    """
    dates = pd.date_range(start='1/1/2023', periods=100)
    data = pd.DataFrame({
        'Open': np.random.normal(100, 5, 100),
        'High': np.random.normal(105, 5, 100),
        'Low': np.random.normal(95, 5, 100),
        'Close': np.random.normal(100, 5, 100),
        'Volume': np.random.normal(1000000, 200000, 100)
    }, index=dates)
    return data


@pytest.fixture
def mock_stock_data_with_trend():
    """
    Fixture that creates mock stock data with a clear trend for testing.
    Returns a pandas DataFrame with OHLCV data showing an upward trend.
    """
    dates = pd.date_range(start='1/1/2023', periods=100)
    data = pd.DataFrame({
        'Open': np.linspace(90, 110, 100) + np.random.normal(0, 2, 100),
        'High': np.linspace(95, 115, 100) + np.random.normal(0, 2, 100),
        'Low': np.linspace(85, 105, 100) + np.random.normal(0, 2, 100),
        'Close': np.linspace(90, 110, 100) + np.random.normal(0, 2, 100),
        'Volume': np.random.normal(1000000, 200000, 100)
    }, index=dates)
    return data


@pytest.fixture
def mock_technical_data():
    """
    Fixture that creates mock stock data with technical indicators.
    Returns a pandas DataFrame with OHLCV data and indicators.
    """
    dates = pd.date_range(start='1/1/2023', periods=100)
    data = pd.DataFrame({
        'Open': np.random.normal(100, 5, 100),
        'High': np.random.normal(105, 5, 100),
        'Low': np.random.normal(95, 5, 100),
        'Close': np.random.normal(100, 5, 100),
        'Volume': np.random.normal(1000000, 200000, 100),
        'SMA_20': np.random.normal(100, 3, 100),
        'SMA_50': np.random.normal(100, 2, 100),
        'EMA_20': np.random.normal(100, 3, 100),
        'RSI': np.random.normal(50, 15, 100),
        'MACD': np.random.normal(0, 1, 100),
        'MACD_Signal': np.random.normal(0, 1, 100),
        'Upper_Band': np.random.normal(105, 3, 100),
        'Lower_Band': np.random.normal(95, 3, 100)
    }, index=dates)
    return data


@pytest.fixture
def temp_dir(tmp_path):
    """
    Fixture that provides a temporary directory path.
    """
    return tmp_path


@pytest.fixture
def mock_transaction_history(temp_dir):
    """
    Fixture that creates a mock transaction history file.
    """
    history_file = temp_dir / "test_transactions.csv"
    
    # Create sample transactions data
    dates = pd.date_range(start='1/1/2023', periods=10)
    data = pd.DataFrame({
        'entry_date': dates.strftime('%Y-%m-%d'),
        'transaction_date': dates.strftime('%Y-%m-%d %H:%M:%S'),
        'symbol': ['MOCK.JK'] * 5 + ['TEST.JK'] * 5,
        'transaction_type': ['BUY', 'SELL'] * 5,
        'price': np.random.normal(1000, 100, 10),
        'quantity': np.random.randint(1, 100, 10),
        'total_amount': np.random.normal(100000, 10000, 10),
        'profit_loss': np.random.normal(5000, 2000, 10),
        'notes': ['Test transaction'] * 10
    })
    
    # Save to CSV
    data.to_csv(history_file, index=False)
    
    return str(history_file)
