"""
Basic example of stock analysis using Stock Analysis Tool.

This example demonstrates:
1. Fetching stock data
2. Performing technical analysis
3. Getting trading recommendations
4. Visualizing results
"""
import sys
import os
import pandas as pd
from datetime import datetime

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data.stock_data import StockData
from src.analysis.technical import TechnicalAnalysis
from src.analysis.trade_advisor import TradeAdvisor
from src.analysis.prediction import StockPredictor
from src.visualization.charts import StockVisualizer

def main():
    # Initialize components
    stock_data = StockData()
    advisor = TradeAdvisor()
    predictor = StockPredictor()
    
    # Choose stock to analyze
    symbol = "BBCA.JK"  # Bank Central Asia (Indonesia)
    print(f"Analyzing stock: {symbol}")
    
    # Fetch stock data
    data = stock_data.fetch_data(symbol, period="1y")
    print(f"Successfully fetched {len(data)} days of data")
    
    # Perform technical analysis
    technical = TechnicalAnalysis()
    data = technical.add_all_indicators(data)
      # Display recent technical indicators
    print("\nRecent Technical Indicators:")
    latest = data.iloc[-1]
    print(f"RSI: {latest.get('RSI', 0):.2f}")
    print(f"MACD: {latest.get('MACD', 0):.2f}")
    print(f"Signal: {latest.get('MACD_Signal', 0):.2f}")
    print(f"Bollinger Upper: {latest.get('Upper_Band', 0):.2f}")
    print(f"Bollinger Lower: {latest.get('Lower_Band', 0):.2f}")
    
    # Get trading recommendation
    recommendation = advisor.get_recommendation(data.iloc[-1], data)
    print(f"\nTrading Recommendation: {recommendation['action']}")
    print(f"Confidence: {recommendation['confidence']:.2f}%")
    print(f"Reason: {recommendation['reason']}")
    
    # Make predictions
    prediction = predictor.predict_next_day_simple(data)
    print(f"\nPrice Prediction for Next Day: {prediction['predicted_close']:.2f}")
    print(f"Predicted Direction: {prediction['predicted_direction']}")
    
    # Visualization
    output_dir = "example_output"
    os.makedirs(output_dir, exist_ok=True)
    
    visualizer = StockVisualizer()
    visualizer.plot_price_history(data, symbol=symbol, 
                                 save_path=os.path.join(output_dir, "price_history.png"),
                                 show=False)
    visualizer.plot_technical_indicators(data, symbol=symbol, 
                                        save_path=os.path.join(output_dir, "technical_analysis.png"),
                                        show=False)
    
    print(f"\nAnalysis completed! Charts saved to {output_dir} directory")

if __name__ == "__main__":
    main()
