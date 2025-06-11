"""
Complete example of Stock Analysis Tool usage.

This example demonstrates a complete workflow:
1. Fetching data for multiple stocks
2. Performing technical analysis
3. Getting trading recommendations
4. Recording transactions
5. Generating visualizations
6. Analyzing portfolio performance
"""
import sys
import os
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data.stock_data import StockData
from src.data.transaction_history import TransactionHistory
from src.analysis.technical import TechnicalAnalysis
from src.analysis.trade_advisor import TradeAdvisor
from src.analysis.prediction import StockPredictor
from src.visualization.charts import StockVisualizer


def analyze_portfolio(symbols, period="6mo"):
    """Analyze multiple stocks and compile results."""
    stock_data = StockData()
    technical = TechnicalAnalysis()
    advisor = TradeAdvisor()
    predictor = StockPredictor()
    visualizer = StockVisualizer()
    
    results = {}
    
    for symbol in symbols:
        print(f"\nAnalyzing {symbol}...")
        
        # Fetch data
        data = stock_data.fetch_data(symbol, period=period)
        if data.empty:
            print(f"Failed to fetch data for {symbol}. Skipping.")
            continue
            
        # Add technical indicators
        data = technical.add_all_indicators(data)
        
        # Get recommendation
        latest = data.iloc[-1]
        recommendation = advisor.get_recommendation(latest, data)
        
        # Predict next day price
        prediction = predictor.predict_next_day_simple(data)
        
        # Store results
        results[symbol] = {
            'data': data,
            'current_price': latest['Close'],
            'change_pct': data['Close'].pct_change().iloc[-1] * 100,
            'recommendation': recommendation,
            'prediction': prediction
        }
        
        # Generate charts
        output_dir = os.path.join("example_output", f"{symbol}_analysis")
        os.makedirs(output_dir, exist_ok=True)
        
        visualizer.plot_price_history(data, symbol=symbol, 
                                     save_path=os.path.join(output_dir, "price_history.png"),
                                     show=False)
        visualizer.plot_technical_indicators(data, symbol=symbol, 
                                            save_path=os.path.join(output_dir, "technical_analysis.png"),
                                            show=False)
        
    return results


def record_demo_transactions(symbols):
    """Record demo transactions for given symbols."""
    stock_data = StockData()
    transactions = TransactionHistory("demo_portfolio.csv")
    
    for symbol in symbols:
        # Fetch data to get real prices
        data = stock_data.fetch_data(symbol, period="6mo")
        if data.empty:
            continue
            
        prices = data['Close'].iloc[-30:].values
        
        # Record a BUY transaction
        buy_date = data.index[-30].strftime("%Y-%m-%d")
        buy_price = prices[0]
        quantity = 100
        
        transactions.add_transaction(
            entry_date=buy_date,
            symbol=symbol,
            transaction_type="BUY",
            price=buy_price,
            quantity=quantity,
            total_amount=buy_price * quantity,
            notes=f"Initial {symbol} position"
        )
        
        # Record a SELL transaction for half the position
        if len(prices) > 20:
            sell_date = data.index[-10].strftime("%Y-%m-%d")
            sell_price = prices[20]
            sell_quantity = quantity // 2
            
            transactions.add_transaction(
                entry_date=sell_date,
                symbol=symbol,
                transaction_type="SELL",
                price=sell_price,
                quantity=sell_quantity,
                total_amount=sell_price * sell_quantity,
                notes=f"Partial profit taking"
            )
    
    return transactions


def analyze_transaction_performance(transactions, symbols):
    """Analyze performance of transactions."""
    performance_results = {}
    
    for symbol in symbols:
        performance = transactions.analyze_performance(symbol)
        if performance:
            performance_results[symbol] = performance
    
    return performance_results


def display_portfolio_summary(analysis_results, performance_results):
    """Display a summary of portfolio analysis."""
    # Create a summary table
    summary_data = []
    
    for symbol in analysis_results:
        result = analysis_results[symbol]
        performance = performance_results.get(symbol, {})
        
        summary_data.append({
            'Symbol': symbol,
            'Price': result['current_price'],
            'Change': f"{result['change_pct']:.2f}%",
            'RSI': result['data'].iloc[-1].get('RSI', 0),
            'Recommendation': result['recommendation']['action'],
            'Next Day': f"{result['prediction']['predicted_close']:.2f}",
            'Holdings': performance.get('current_holdings', 0),
            'Realized P/L': performance.get('realized_pl', 0)
        })
    
    # Convert to DataFrame and display
    summary_df = pd.DataFrame(summary_data)
    print("\nPortfolio Summary:")
    print(summary_df.to_string(index=False))
    
    # Save summary to CSV
    os.makedirs("example_output", exist_ok=True)
    summary_df.to_csv("example_output/portfolio_summary.csv", index=False)
    print("Summary saved to example_output/portfolio_summary.csv")


def main():
    # Define portfolio
    symbols = ["BBCA.JK", "TLKM.JK", "GOTO.JK"]
    print(f"Analyzing portfolio with {len(symbols)} stocks: {', '.join(symbols)}")
    
    # Analyze stocks
    analysis_results = analyze_portfolio(symbols)
    
    # Record demo transactions
    transactions = record_demo_transactions(symbols)
    
    # Analyze performance
    performance_results = analyze_transaction_performance(transactions, symbols)
    
    # Display summary
    display_portfolio_summary(analysis_results, performance_results)
    
    # Export transaction analysis
    transactions.export_analysis_to_csv("example_output/portfolio_analysis.csv")
    print("Transaction analysis exported to example_output/portfolio_analysis.csv")
    

if __name__ == "__main__":
    os.makedirs("example_output", exist_ok=True)
    main()
