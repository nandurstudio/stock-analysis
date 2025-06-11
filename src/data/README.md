# Data Module

This module handles data acquisition, processing, and storage for the Stock Analysis Tool.

## Components

### stock_data.py
Provides `StockData` class for:
- Fetching historical stock data from Yahoo Finance
- Processing and cleaning data
- Calculating returns and other basic metrics

### transaction_history.py
Provides `TransactionHistory` class for:
- Recording buy/sell transactions
- Calculating profit/loss
- Generating transaction reports
- Analyzing trading performance

## Usage Example

```python
from src.data.stock_data import StockData
from src.data.transaction_history import TransactionHistory

# Initialize stock data component
stock_data = StockData()

# Fetch data for a stock symbol
data = stock_data.fetch_historical_data("AAPL", period="1y")

# Initialize transaction history
transactions = TransactionHistory()

# Record a buy transaction
transactions.add_transaction(
    entry_date="2023-01-15",
    symbol="AAPL",
    transaction_type="BUY",
    price=150.25,
    quantity=10,
    total_amount=1502.50,
    notes="Initial position"
)

# Get all transactions
history = transactions.get_transactions()
```
