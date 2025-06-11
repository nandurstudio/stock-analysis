import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.ensemble import RandomForestRegressor

class StockPredictor:
    def __init__(self, data):
        """
        Initialize with stock data DataFrame
        
        Parameters:
        data (DataFrame): DataFrame with columns: Close, High, Low, Open, Volume
        """
        self.data = data.copy()
        self.model = None
        self.scaler = MinMaxScaler()
        
    def prepare_data(self, target_column='Close', lookback=30):
        """
        Prepare data for prediction by creating features from historical data
        
        Parameters:
        target_column (str): Column to predict (default: 'Close')
        lookback (int): Number of previous days to use as features
        """
        df = self.data.copy()
        
        # Create features from historical prices
        for i in range(1, lookback + 1):
            df[f'Close_lag_{i}'] = df[target_column].shift(i)
            df[f'Volume_lag_{i}'] = df['Volume'].shift(i)
        
        # Add technical indicators as features
        df['SMA_5'] = df[target_column].rolling(window=5).mean()
        df['SMA_20'] = df[target_column].rolling(window=20).mean()
        df['Price_Change'] = df[target_column].pct_change()
        df['Volume_Change'] = df['Volume'].pct_change()
        
        # Drop rows with NaN values
        df = df.dropna()
        
        # Prepare features and target
        features = [col for col in df.columns if col.startswith(('Close_lag', 'Volume_lag', 'SMA', 'Price_Change', 'Volume_Change'))]
        X = df[features]
        y = df[target_column]
        
        # Scale features
        self.scaler = MinMaxScaler()
        X_scaled = self.scaler.fit_transform(X)
        
        return X_scaled, y
        
    def train_model(self, test_size=0.2, lookback=30):
        """
        Train the prediction model
        
        Parameters:
        test_size (float): Proportion of dataset to include in the test split
        lookback (int): Number of previous days to use as features
        """
        X, y = self.prepare_data(lookback=lookback)
        
        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, shuffle=False)
        
        # Initialize and train the model
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.model.fit(X_train, y_train)
        
        # Make predictions on test set
        y_pred = self.model.predict(X_test)
          # Calculate metrics
        metrics = {
            'MSE': mean_squared_error(y_test, y_pred),
            'RMSE': np.sqrt(mean_squared_error(y_test, y_pred)),
            'MAE': mean_absolute_error(y_test, y_pred)
        }
        
        # Add R2 only if it's well-defined (avoid warning for constant targets)
        if len(set(y_test)) > 1:  # Check if target has more than one unique value
            metrics['R2'] = r2_score(y_test, y_pred)
        else:
            metrics['R2'] = np.nan
        
        return metrics, y_test, y_pred
        
    def predict_next_day(self):
        """
        Predict the next day's price
        """
        if self.model is None:
            raise ValueError("Model not trained. Call train_model() first.")
        
        # Prepare the most recent data
        X, _ = self.prepare_data()
        latest_features = X[-1].reshape(1, -1)
          # Make prediction
        prediction = self.model.predict(latest_features)[0]
        return prediction
        
    def predict_next_days(self, days=5):
        """
        Predict stock prices for the next specified number of days
        
        Parameters:
        days (int): Number of days to predict ahead
        
        Returns:
        dict: Prediction results with dates and prices
        """
        try:
            # Check if we have enough data for prediction
            if len(self.data) < 30:  # Minimal data requirement
                raise ValueError(f"Insufficient data for prediction: {len(self.data)} rows. Need at least 30 rows.")
            
            # First train the model if it hasn't been trained yet
            if self.model is None:
                self.train_model()
                
            # Get the latest data to use as a starting point
            latest_data = self.data.copy().iloc[-30:] # Use last 30 days
              # Prepare data for prediction
            try:
                features, _ = self.prepare_data()
                
                # Make sure features data is not empty
                if len(features) == 0:
                    raise ValueError("No feature data available for prediction")
            except Exception as e:
                raise ValueError(f"Error preparing data for prediction: {str(e)}")
            
            # Store predictions
            dates = []
            predicted_prices = []
            confidence_intervals = []
            
            # Start with the latest date in the data
            current_date = self.data.index[-1]
            
            # Make copy of latest data for predictions
            prediction_data = self.data.copy()
            
            for i in range(days):
                # Move to next business day
                current_date = self._next_business_day(current_date)
                dates.append(current_date)
                
                # Get features for prediction
                X_pred = self._prepare_prediction_features(prediction_data)
                
                # Make prediction
                predicted_price = self.model.predict(X_pred)[0]
                predicted_prices.append(predicted_price)
                
                # Calculate confidence interval (simple estimation)
                std_dev = prediction_data['Close'].std() * 0.5  # Simplified
                lower_bound = predicted_price - 1.96 * std_dev
                upper_bound = predicted_price + 1.96 * std_dev
                confidence_intervals.append((lower_bound, upper_bound))
                
                # Add prediction to the data for next iteration
                new_row = prediction_data.iloc[-1:].copy()
                new_row.index = [current_date]
                new_row['Close'] = predicted_price
                # Estimate other values (simplified)
                new_row['Open'] = predicted_price * 0.99
                new_row['High'] = predicted_price * 1.01
                new_row['Low'] = predicted_price * 0.98
                new_row['Volume'] = prediction_data['Volume'].mean()
                
                prediction_data = pd.concat([prediction_data, new_row])
            
            # Format results
            return {
                'dates': dates,
                'predicted_prices': predicted_prices,
                'confidence_intervals': confidence_intervals,
                'current_price': self.data['Close'].iloc[-1],
                'price_change': predicted_prices[-1] - self.data['Close'].iloc[-1],
                'price_change_pct': (predicted_prices[-1] / self.data['Close'].iloc[-1] - 1) * 100
            }
        except Exception as e:
            print(f"Error in prediction: {str(e)}")
            return {
                'dates': [],
                'predicted_prices': [],
                'confidence_intervals': [],
                'current_price': self.data['Close'].iloc[-1] if not self.data.empty else 0,
                'price_change': 0,
                'price_change_pct': 0,
                'error': str(e)
            }
    
    def _next_business_day(self, date):
        """Helper method to get the next business day"""
        next_day = date + pd.Timedelta(days=1)
        # Skip weekends (simplified)
        if next_day.weekday() >= 5:  # 5 is Saturday, 6 is Sunday
            next_day = next_day + pd.Timedelta(days=7 - next_day.weekday())
        return next_day
    
    def _prepare_prediction_features(self, data):
        """Prepare features for a single prediction"""
        # Get the latest available data
        df = data.copy()
        
        # Create features from historical prices (similar to prepare_data)
        lookback = 30
        for i in range(1, lookback + 1):
            df[f'Close_lag_{i}'] = df['Close'].shift(i)
            df[f'Volume_lag_{i}'] = df['Volume'].shift(i)
        
        # Add technical indicators as features
        df['SMA_5'] = df['Close'].rolling(window=5).mean()
        df['SMA_20'] = df['Close'].rolling(window=20).mean()
        df['Price_Change'] = df['Close'].pct_change()
        df['Volume_Change'] = df['Volume'].pct_change()
        
        # Get last row for prediction (latest complete feature set)
        features = [col for col in df.columns if col.startswith(('Close_lag', 'Volume_lag', 'SMA', 'Price_Change', 'Volume_Change'))]
        X = df[features].iloc[-1:].values
        
        # Scale features if scaler exists
        if hasattr(self, 'scaler') and self.scaler is not None:
            X = self.scaler.transform(X)
        
        return X
        
    def generate_forecast_summary(self):
        """
        Generate a summary of the forecast including metrics and predictions
        """
        # Train model and get metrics
        metrics, y_test, y_pred = self.train_model()
        next_day_pred = self.predict_next_day()
        
        summary = []
        summary.append("Stock Price Forecast Summary")
        summary.append("=" * 50)
        
        # Add model performance metrics
        summary.append("\nModel Performance Metrics:")
        summary.append("-" * 30)
        for metric, value in metrics.items():
            summary.append(f"{metric}: {value:.4f}")
        
        # Add next day prediction
        current_price = self.data['Close'].iloc[-1]
        price_change = next_day_pred - current_price
        pct_change = (price_change / current_price) * 100
        
        summary.append("\nPrice Predictions:")
        summary.append("-" * 30)
        summary.append(f"Current Price: {current_price:.2f}")
        summary.append(f"Next Day Prediction: {next_day_pred:.2f}")
        summary.append(f"Expected Change: {price_change:.2f} ({pct_change:.2f}%)")
        
        # Add prediction confidence
        if abs(pct_change) > 5:
            summary.append("\nNote: Large predicted price change, interpret with caution")
        
        return "\n".join(summary)

if __name__ == "__main__":
    # Example usage
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from data.stock_data import StockData
    
    # Fetch some sample data
    stock = StockData()
    data = stock.fetch_data("BBCA.JK", period="1y")
    
    # Create predictor and generate forecast
    predictor = StockPredictor(data)
    print(predictor.generate_forecast_summary())
