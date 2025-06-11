def format_date(date_str):
    """Convert a date string to a standardized format."""
    from datetime import datetime
    return datetime.strptime(date_str, '%Y-%m-%d').date()

def preprocess_data(data):
    """Clean and preprocess stock data."""
    # Example preprocessing steps
    data = data.dropna()  # Remove missing values
    data['date'] = data['date'].apply(format_date)  # Format date
    return data

def calculate_percentage_change(current_price, previous_price):
    """Calculate the percentage change between two prices."""
    if previous_price == 0:
        return 0
    return ((current_price - previous_price) / previous_price) * 100

def get_stock_symbol(ticker):
    """Return the stock symbol for a given ticker."""
    return ticker.upper()  # Ensure the ticker is in uppercase

# Additional utility functions can be added here as needed.