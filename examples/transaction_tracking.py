"""
Example of transaction tracking using Stock Analysis Tool.

This example demonstrates:
1. Recording buy/sell transactions
2. Calculating profit/loss
3. Analyzing trading performance
4. Exporting transaction history
"""
import sys
import os
import pandas as pd
from datetime import datetime, timedelta

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data.stock_data import StockData
from src.data.transaction_history import TransactionHistory


def main():
    # Initialize components
    stock_data = StockData()
    transactions = TransactionHistory("example_transactions.csv")
    
    # Choose stock to track
    symbol = "TLKM.JK"  # Telkom Indonesia
    print(f"Transaction tracking example for: {symbol}")
    
    # Fetch stock data to get realistic prices
    data = stock_data.fetch_data(symbol, period="6mo")
    if data.empty:
        print("Failed to fetch data. Using mock data instead.")
        # Use mock data
        start_price = 3800
        prices = [start_price + i*10 for i in range(10)]
    else:
        # Get some sample prices from real data
        prices = data['Close'].iloc[-10:].tolist()
        
    print(f"Successfully fetched price data for demonstration")
    
    # Simulate a series of transactions
    # First transaction - BUY
    print("\nRecording transactions...")
    
    # Buy transaction
    buy_date = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
    transactions.add_transaction(
        entry_date=buy_date,
        symbol=symbol,
        transaction_type="BUY",
        price=prices[0],
        quantity=100,
        total_amount=prices[0] * 100,
        notes="Initial position"
    )
    print(f"Recorded BUY transaction: {prices[0]} x 100 shares on {buy_date}")
    
    # Additional buy transaction
    buy_date_2 = (datetime.now() - timedelta(days=20)).strftime("%Y-%m-%d")
    transactions.add_transaction(
        entry_date=buy_date_2,
        symbol=symbol,
        transaction_type="BUY",
        price=prices[2],
        quantity=50,
        total_amount=prices[2] * 50,
        notes="Increased position"
    )
    print(f"Recorded BUY transaction: {prices[2]} x 50 shares on {buy_date_2}")
    
    # Sell transaction
    sell_date = (datetime.now() - timedelta(days=10)).strftime("%Y-%m-%d")
    sell_price = prices[-1]
    transactions.add_transaction(
        entry_date=sell_date,
        symbol=symbol,
        transaction_type="SELL",
        price=sell_price,
        quantity=75,
        total_amount=sell_price * 75,
        notes="Partial profit taking"
    )
    print(f"Recorded SELL transaction: {sell_price} x 75 shares on {sell_date}")
    
    # Display all transactions
    print("\nTransaction History:")
    all_transactions = transactions.get_transactions()
    print(all_transactions[['entry_date', 'symbol', 'transaction_type', 'price', 'quantity', 'total_amount']])
    
    # Analyze performance
    print("\nPerformance Analysis:")
    performance = transactions.analyze_performance(symbol)
    if performance:
        print(f"Total Buy Value: {performance['total_buy_value']:,.2f}")
        print(f"Total Sell Value: {performance['total_sell_value']:,.2f}")
        print(f"Realized Profit/Loss: {performance['realized_pl']:,.2f}")
        print(f"Unrealized Profit/Loss: {performance['unrealized_pl']:,.2f}")
        print(f"Current Holdings: {performance['current_holdings']} shares")
        print(f"Average Buy Price: {performance['avg_buy_price']:,.2f}")
    
    # Export to CSV
    output_dir = "example_output"
    os.makedirs(output_dir, exist_ok=True)
    export_path = os.path.join(output_dir, "transaction_analysis.csv")
    transactions.export_analysis_to_csv(export_path)
    print(f"\nTransaction analysis exported to: {export_path}")


if __name__ == "__main__":
    main()
