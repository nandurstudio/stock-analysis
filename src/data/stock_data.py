import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

class StockData:
    def __init__(self):
        self.data = None
        self.symbol = None
        
    def fetch_data(self, symbol, period="1y"):
        """
        Fetch stock data from Yahoo Finance
        
        Parameters:
        symbol (str): Stock symbol (e.g., 'BBCA.JK' for BCA)
        period (str): Time period ('1d','5d','1mo','3mo','6mo','1y','2y','5y','10y','ytd','max')
        """
        self.symbol = symbol
        stock = yf.Ticker(symbol)
        self.data = stock.history(period=period)
        return self.data
    
    def get_latest_price(self):
        """Get the latest closing price"""
        if self.data is not None and not self.data.empty:
            return self.data['Close'].iloc[-1]
        return None
    
    def get_price_change(self):
        """Calculate price change and percentage change"""
        if self.data is not None and not self.data.empty:
            latest_price = self.data['Close'].iloc[-1]
            prev_price = self.data['Close'].iloc[-2]
            change = latest_price - prev_price
            pct_change = (change / prev_price) * 100
            return change, pct_change
        return None, None

    def get_historical_data(self, start_date, end_date=None):
        """
        Get historical data for a specific date range
        
        Parameters:
        start_date (str): Start date in 'YYYY-MM-DD' format
        end_date (str): End date in 'YYYY-MM-DD' format (optional, defaults to today)
        """
        if self.symbol is None:
            raise ValueError("Symbol not set. Call fetch_data() first.")
            
        if end_date is None:
            end_date = datetime.today().strftime('%Y-%m-%d')
            
        stock = yf.Ticker(self.symbol)
        self.data = stock.history(start=start_date, end=end_date)
        return self.data

    def save_to_csv(self, filename):
        """Save data to CSV file"""
        if self.data is not None:
            self.data.to_csv(filename)
            
    def load_from_csv(self, filename):
        """Load data from CSV file"""
        self.data = pd.read_csv(filename, index_col=0, parse_dates=True)
        return self.data
            
if __name__ == "__main__":
    # Example usage
    stock = StockData()
    data = stock.fetch_data("BBCA.JK")  # BCA stock
    print(f"Latest price: {stock.get_latest_price()}")
    change, pct_change = stock.get_price_change()
    print(f"Price change: {change:.2f} ({pct_change:.2f}%)")