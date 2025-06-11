import json
import os

# Get absolute path to config file in the root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CONFIG_FILE = os.path.join(BASE_DIR, "stock_config.json")

class StockConfig:
    def __init__(self):
        self.default_stocks = ["BBCA", "BBRI", "ASII", "TLKM", "GOTO"]  # Default IDX stocks
        self.timeframe = "1d"
        self.user_stocks = []
        self.load_config()

    def load_config(self):
        """Load configuration from file"""
        if os.path.exists(CONFIG_FILE):
            try:
                with open(CONFIG_FILE, 'r') as f:
                    config = json.load(f)
                    self.user_stocks = config.get('stocks', self.default_stocks)
                    self.timeframe = config.get('timeframe', self.timeframe)
            except Exception as e:
                print(f"Error loading config: {e}")
                self.user_stocks = self.default_stocks
        else:
            self.user_stocks = self.default_stocks
            self.save_config()

    def save_config(self):
        """Save configuration to file"""
        config = {
            'stocks': self.user_stocks,
            'timeframe': self.timeframe
        }
        try:
            with open(CONFIG_FILE, 'w') as f:
                json.dump(config, f, indent=2)
        except Exception as e:
            print(f"Error saving config: {e}")

    def add_stock(self, symbol: str):
        """Add a stock to the user's list"""
        # Remove .JK suffix if present
        symbol = symbol.upper().replace('.JK', '')
        if symbol not in self.user_stocks:
            self.user_stocks.append(symbol)
            self.save_config()

    def remove_stock(self, symbol: str):
        """Remove a stock from the user's list"""
        symbol = symbol.upper().replace('.JK', '')
        if symbol in self.user_stocks:
            self.user_stocks.remove(symbol)
            self.save_config()

    def get_stock_with_suffix(self, symbol: str) -> str:
        """Get stock symbol with .JK suffix"""
        return f"{symbol.upper()}.JK"

    def get_stocks(self) -> list:
        """Get list of user's stocks with .JK suffix"""
        return [self.get_stock_with_suffix(s) for s in self.user_stocks]

    def get_stocks_without_suffix(self) -> list:
        """Get list of user's stocks without suffix"""
        return self.user_stocks.copy()

    def set_timeframe(self, timeframe: str):
        """Set the timeframe for analysis"""
        self.timeframe = timeframe
        self.save_config()

# Create global config instance
stock_config = StockConfig()