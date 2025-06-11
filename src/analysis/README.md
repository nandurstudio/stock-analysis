# Analysis Module

This module contains components for performing technical analysis and generating trading recommendations.

## Components

### technical.py
Provides `TechnicalAnalysis` class that implements various technical indicators:
- Simple Moving Average (SMA)
- Exponential Moving Average (EMA)
- Relative Strength Index (RSI)
- Moving Average Convergence Divergence (MACD)
- Bollinger Bands
- And more

### prediction.py
Provides `StockPredictor` class with methods for:
- Simple next-day predictions
- LSTM model training and prediction
- Linear regression models

### trade_advisor.py
Provides `TradeAdvisor` class that:
- Analyzes technical indicators
- Evaluates patterns
- Considers market trends
- Generates buy/sell/hold recommendations with confidence scores

## Usage Example

```python
from src.analysis.technical import TechnicalAnalysis
from src.analysis.prediction import StockPredictor
from src.analysis.trade_advisor import TradeAdvisor

# Initialize components
tech_analyzer = TechnicalAnalysis()
predictor = StockPredictor()
advisor = TradeAdvisor()

# Analyze stock data
data_with_indicators = tech_analyzer.add_all_indicators(stock_data)

# Make prediction
prediction = predictor.predict_next_day_simple(data_with_indicators)

# Get trading recommendation
recommendation = advisor.get_recommendation(data_with_indicators.iloc[-1], data_with_indicators)
```
