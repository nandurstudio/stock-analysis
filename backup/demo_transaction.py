#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Demo script for showing the enhanced transaction history features.
This script demonstrates how to use the transaction history system
to manage and analyze trading positions.
"""

import sys
import os

# Add the current directory to the path to ensure we can import modules
sys.path.insert(0, os.getcwd())

from src.data.transaction_history import TransactionHistory

def main():
    """Main entry point for the script."""
    print("Stock Transaction History Demo")
    print("=" * 50)
    
    # Use a separate transaction history file for the demo
    history = TransactionHistory(filename="demo_transaction_history.csv")
    
    # Add some sample transactions with different date formats
    print("\nAdding sample transactions...")
    
    # Add BUY transactions for multiple stocks with different date formats
    history.add_transaction(
        symbol="BBCA.JK",
        transaction_type="BUY",
        price=8500,
        lot_size=10,
        input_date="010525"  # DDMMYY format - May 1, 2025
    )
    
    history.add_transaction(
        symbol="BBCA.JK",
        transaction_type="BUY",
        price=8600,
        lot_size=5,
        input_date="15-05-25"  # DD-MM-YY format - May 15, 2025
    )
    
    history.add_transaction(
        symbol="TLKM.JK",
        transaction_type="BUY",
        price=4200,
        lot_size=20,
        input_date="2025-05-20"  # YYYY-MM-DD format - May 20, 2025
    )
    
    # Add some SELL transactions
    history.add_transaction(
        symbol="BBCA.JK",
        transaction_type="SELL",
        price=9000,
        lot_size=8
    )
    
    history.add_transaction(
        symbol="TLKM.JK",
        transaction_type="SELL",
        price=4100,
        lot_size=10
    )
    
    # Display the position summary for each symbol
    symbols = ["BBCA.JK", "TLKM.JK"]
    
    for symbol in symbols:
        print("\n" + "=" * 50)
        print(f"Position Details for {symbol}")
        print(history.get_position_detail(symbol))
    
    # Export transactions for analysis
    export_path = os.path.join("analysis_results", "demo_transaction_analysis.csv")
    history.export_transactions_for_analysis(output_path=export_path)
    print(f"\nExported transaction data to {export_path}")
    
    # Show performance analysis
    print("\n" + "=" * 50)
    print("Portfolio Performance Analysis")
    print(history.analyze_performance())

if __name__ == "__main__":
    # Create the analysis_results directory if it doesn't exist
    os.makedirs("analysis_results", exist_ok=True)
    main()
