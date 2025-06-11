"""
Entry point for the Stock Analysis Tool.
This file allows the package to be run as a module: python -m src
"""
import os
import sys
import argparse
from datetime import datetime
import importlib.util

# Check if main.py exists at the project root
main_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "main.py")
if os.path.exists(main_path):
    # Import main.py from the root directory
    spec = importlib.util.spec_from_file_location("main", main_path)
    main_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(main_module)
    main_func = main_module.main
else:
    # Define a simple main function if the original main.py is not found
    def main_func():
        print("Stock Analysis Tool - Main function")
        print("Original main.py not found. Please run one of the examples:")
        print("  python examples/basic_analysis.py")
        print("  python examples/transaction_tracking.py")
        print("  python examples/portfolio_analysis.py")


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Stock Analysis and Trading Recommendation Tool')
    
    parser.add_argument('--symbol', '-s', type=str, help='Stock symbol to analyze (e.g. BBCA.JK)')
    parser.add_argument('--period', '-p', type=str, default='1y', 
                        help='Period to analyze (1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y)')
    parser.add_argument('--output', '-o', type=str, default='analysis_results',
                        help='Directory to save analysis results')
    
    return parser.parse_args()


def run():
    """Run the stock analyzer with command line arguments."""
    args = parse_arguments()
    
    if args.symbol:
        # If a specific stock is requested, analyze it
        from src.data.stock_data import StockData
        from src.analysis.technical import TechnicalAnalysis
        from src.analysis.trade_advisor import TradeAdvisor
        from src.visualization.charts import StockVisualizer
        
        print(f"Analyzing {args.symbol} for period {args.period}")
        
        stock_data = StockData()
        data = stock_data.fetch_data(args.symbol, period=args.period)
        
        if data.empty:
            print(f"Error: Could not fetch data for {args.symbol}")
            return
        
        technical = TechnicalAnalysis()
        data = technical.add_all_indicators(data)
        
        advisor = TradeAdvisor()
        recommendation = advisor.get_recommendation(data.iloc[-1], data)
        
        print("\nAnalysis Results:")
        print(f"Current Price: {data['Close'].iloc[-1]:.2f}")
        print(f"RSI: {data.iloc[-1].get('RSI', 0):.2f}")
        print(f"Recommendation: {recommendation['action']} (Confidence: {recommendation['confidence']:.2f}%)")
        print(f"Reason: {recommendation['reason']}")
        
        # Save charts
        output_dir = os.path.join(args.output, f"{args.symbol}_charts")
        os.makedirs(output_dir, exist_ok=True)
        
        visualizer = StockVisualizer()
        visualizer.plot_price_history(data, symbol=args.symbol, 
                                     save_path=os.path.join(output_dir, "price_history.png"),
                                     show=False)
        visualizer.plot_technical_indicators(data, symbol=args.symbol, 
                                            save_path=os.path.join(output_dir, "technical_analysis.png"),
                                            show=False)
        
        print(f"\nCharts saved to {output_dir}")
    else:
        # Otherwise run the main application
        main_func()


if __name__ == "__main__":
    run()
