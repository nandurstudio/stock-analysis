"""
Stock Analysis and Trading Recommendation Tool Demo
-------------------------------------------------

This file demonstrates how to use the new stock analysis and trading recommendation
system programmatically by importing and calling the analyze_stock_with_history function.

This can help users automate their analysis for multiple stocks or integrate with
their own custom trading systems.
"""

import os
import pandas as pd
from datetime import datetime
from src.data.transaction_history import TransactionHistory
from main_v2 import analyze_stock_with_history

def demo_stock_analysis():
    """
    Demonstrate the stock analysis system with transaction history integration
    """
    print("=" * 80)
    print("STOCK ANALYSIS AND TRADING RECOMMENDATION TOOL DEMO")
    print("=" * 80)
    
    # Initialize transaction history
    th = TransactionHistory()
    
    # Add sample transactions if none exist
    if th.get_transactions().empty:
        print("\nAdding sample transactions...\n")
        
        # Sample transactions for BBCA.JK
        th.add_transaction("BBCA.JK", "BUY", 9000, 10, input_date="2025-01-10")
        th.add_transaction("BBCA.JK", "BUY", 8800, 5, input_date="2025-02-15")
        th.add_transaction("BBCA.JK", "SELL", 9500, 7, input_date="2025-03-20")
        
        # Sample transactions for TLKM.JK
        th.add_transaction("TLKM.JK", "BUY", 4200, 15, input_date="2025-02-05")
        th.add_transaction("TLKM.JK", "SELL", 4000, 5, input_date="2025-04-10")
        
        print("Sample transactions added successfully!\n")
    
    # List of stocks to analyze
    stocks = ["BBCA.JK", "TLKM.JK", "GOTO.JK"]
    
    for symbol in stocks:
        print(f"\nAnalyzing {symbol}...\n")
        
        # Run analysis with transaction history integration
        try:
            results = analyze_stock_with_history(symbol)
            
            # You can access various properties from the results
            current_price = results['current_price']
            recommendation = results['recommendation']
            position = results['position_summary']
            
            print("\nSUMMARY OF ANALYSIS:")
            print(f"Current Price: Rp {current_price:,.2f}")
            print(f"Recommendation: {recommendation['action']}")
            print(f"Confidence: {recommendation['confidence']:.1f}%")
            
            if position['current_position'] > 0:
                print(f"Current Position: {position['current_position']} lots")
                print(f"Average Buy Price: Rp {position['avg_buy_price']:,.2f}")
                
                # Calculate unrealized P/L
                unreal_pnl = position['current_position'] * 100 * (current_price - position['avg_buy_price'])
                unreal_pnl_pct = (current_price / position['avg_buy_price'] - 1) * 100
                
                print(f"Unrealized P/L: Rp {unreal_pnl:,.2f} ({unreal_pnl_pct:+.2f}%)")
            else:
                print("No current position in this stock")
            
            print("\n" + "-" * 50)
            
        except Exception as e:
            print(f"Error analyzing {symbol}: {str(e)}")
    
    print("\nDemo completed successfully!")

if __name__ == "__main__":
    demo_stock_analysis()
