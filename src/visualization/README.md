# Visualization Module

This module handles the creation of charts and visual representations of stock data and analysis.

## Components

### charts.py
Provides `StockVisualizer` class for:
- Creating price history charts
- Visualizing technical indicators
- Generating candlestick charts
- Creating correlation plots
- Creating interactive charts with Plotly

## Usage Example

```python
from src.visualization.charts import StockVisualizer

# Initialize visualizer with stock data
visualizer = StockVisualizer(stock_data)

# Generate price history chart
visualizer.plot_price_history(
    title="AAPL Price History",
    save_path="charts/price_history.png",
    show=True
)

# Plot technical indicators
visualizer.plot_technical_indicators(
    title="AAPL Technical Analysis",
    save_path="charts/technical_analysis.png"
)

# Create candlestick chart
visualizer.plot_candlestick(
    title="AAPL Candlestick",
    save_path="charts/candlestick.png"
)

# Generate all charts at once
visualizer.generate_analysis_charts(
    symbol="AAPL",
    save_dir="charts/AAPL_charts"
)
```
