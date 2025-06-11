# Utilities Module

This module contains utility functions and helper classes used throughout the Stock Analysis Tool.

## Components

### config.py
Provides configuration management with `StockConfig` class:
- Loading and saving user preferences
- Managing default stock symbols
- Configuring application settings

### helpers.py
Contains various helper functions:
- Date formatting utilities
- Number formatting
- Error handling
- Text processing

## Usage Example

```python
from src.utils.config import StockConfig
import src.utils.helpers as helpers

# Load configuration
config = StockConfig()

# Get user stocks
stocks = config.user_stocks

# Add a new stock
config.user_stocks.append("MSFT.JK")
config.save_config()

# Format currency
formatted = helpers.format_currency(1500000, "IDR")
```
