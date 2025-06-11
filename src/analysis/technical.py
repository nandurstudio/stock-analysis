import pandas as pd
import numpy as np
from ta.trend import SMAIndicator, EMAIndicator, MACD
from ta.momentum import RSIIndicator
from ta.volatility import BollingerBands
from ta.volume import OnBalanceVolumeIndicator

class TechnicalAnalysis:
    def __init__(self, data):
        """
        Initialize with stock data DataFrame
        
        Parameters:
        data (DataFrame): DataFrame with columns: Close, High, Low, Open, Volume
        """
        self.data = data.copy()
        
    def add_sma(self, window=20):
        """Add Simple Moving Average"""
        sma = SMAIndicator(close=self.data["Close"], window=window)
        self.data[f'SMA_{window}'] = sma.sma_indicator()
        
    def add_ema(self, window=20):
        """Add Exponential Moving Average"""
        ema = EMAIndicator(close=self.data["Close"], window=window)
        self.data[f'EMA_{window}'] = ema.ema_indicator()
        
    def add_macd(self, window_slow=26, window_fast=12, window_sign=9):
        """Add MACD indicator"""
        macd = MACD(
            close=self.data["Close"],
            window_slow=window_slow,
            window_fast=window_fast,
            window_sign=window_sign
        )
        self.data['MACD'] = macd.macd()
        self.data['MACD_Signal'] = macd.macd_signal()
        self.data['MACD_Hist'] = macd.macd_diff()
        
    def add_rsi(self, window=14):
        """Add Relative Strength Index"""
        rsi = RSIIndicator(close=self.data["Close"], window=window)
        self.data['RSI'] = rsi.rsi()
        
    def add_bollinger_bands(self, window=20, window_dev=2):
        """Add Bollinger Bands"""
        bb = BollingerBands(close=self.data["Close"], window=window, window_dev=window_dev)
        self.data['BB_H'] = bb.bollinger_hband()
        self.data['BB_M'] = bb.bollinger_mavg()
        self.data['BB_L'] = bb.bollinger_lband()
        
    def add_obv(self):
        """Add On Balance Volume"""
        obv = OnBalanceVolumeIndicator(close=self.data["Close"], volume=self.data["Volume"])
        self.data['OBV'] = obv.on_balance_volume()
        
    def get_signals(self):
        """
        Generate trading signals based on technical indicators
        Returns: Dictionary with trading signals
        """
        signals = {}
        latest = self.data.iloc[-1]
        
        # RSI signals
        if 'RSI' in self.data.columns:
            rsi = latest['RSI']
            if rsi > 70:
                signals['RSI'] = {'signal': 'SELL', 'reason': 'Overbought', 'value': rsi}
            elif rsi < 30:
                signals['RSI'] = {'signal': 'BUY', 'reason': 'Oversold', 'value': rsi}
            else:
                signals['RSI'] = {'signal': 'NEUTRAL', 'reason': 'Normal range', 'value': rsi}
        
        # MACD signals
        if all(x in self.data.columns for x in ['MACD', 'MACD_Signal']):
            macd = latest['MACD']
            signal = latest['MACD_Signal']
            hist = latest['MACD_Hist']
            
            if hist > 0 and self.data['MACD_Hist'].iloc[-2] <= 0:
                signals['MACD'] = {'signal': 'BUY', 'reason': 'Bullish crossover', 'value': hist}
            elif hist < 0 and self.data['MACD_Hist'].iloc[-2] >= 0:
                signals['MACD'] = {'signal': 'SELL', 'reason': 'Bearish crossover', 'value': hist}
            else:
                signals['MACD'] = {'signal': 'NEUTRAL', 'reason': 'No crossover', 'value': hist}
        
        # Bollinger Bands signals
        if all(x in self.data.columns for x in ['BB_H', 'BB_M', 'BB_L']):
            close = latest['Close']
            bb_high = latest['BB_H']
            bb_low = latest['BB_L']
            
            if close > bb_high:
                signals['BB'] = {'signal': 'SELL', 'reason': 'Above upper band', 'value': close}
            elif close < bb_low:
                signals['BB'] = {'signal': 'BUY', 'reason': 'Below lower band', 'value': close}
            else:
                signals['BB'] = {'signal': 'NEUTRAL', 'reason': 'Between bands', 'value': close}
                
        return signals
        
    def generate_summary(self):
        """
        Generate a comprehensive technical analysis summary
        Returns: String with analysis summary
        """
        # Calculate all indicators
        self.add_sma(20)
        self.add_sma(50)
        self.add_ema(20)
        self.add_macd()
        self.add_rsi()
        self.add_bollinger_bands()
        self.add_obv()
        
        signals = self.get_signals()
        latest = self.data.iloc[-1]
        
        summary = []
        summary.append("Technical Analysis Summary:")
        summary.append("=" * 50)
        summary.append(f"Current Price: {latest['Close']:.2f}")
        summary.append("-" * 50)
        
        # Add signals to summary
        for indicator, data in signals.items():
            summary.append(f"{indicator}:")
            summary.append(f"Signal: {data['signal']}")
            summary.append(f"Reason: {data['reason']}")
            summary.append(f"Value: {data['value']:.2f}")
            summary.append("-" * 30)
        
        # Overall recommendation - with weighted scoring
        # Assign weights to different indicators based on their reliability
        weights = {
            'RSI': 0.35,     # RSI is a strong indicator
            'MACD': 0.35,    # MACD is also strong
            'BB': 0.3,       # Bollinger Bands
        }
        
        score = 0
        available_indicators = 0
        
        for indicator, data in signals.items():
            if indicator in weights:
                available_indicators += weights[indicator]
                if data['signal'] == 'BUY':
                    score += weights[indicator]
                elif data['signal'] == 'SELL':
                    score -= weights[indicator]
                # NEUTRAL signals don't affect the score
        
        buy_signals = sum(1 for s in signals.values() if s['signal'] == 'BUY')
        sell_signals = sum(1 for s in signals.values() if s['signal'] == 'SELL')
        neutral_signals = sum(1 for s in signals.values() if s['signal'] == 'NEUTRAL')
        
        # Calculate strength as a percentage
        if available_indicators > 0:
            strength_pct = abs(score / available_indicators) * 100
        else:
            strength_pct = 0
            
        # Determine signal based on weighted score
        if score > 0:
            signal = "BUY"
            summary.append(f"\nOverall Recommendation: {signal} (Strength: {strength_pct:.1f}%)")
        elif score < 0:
            signal = "SELL"
            summary.append(f"\nOverall Recommendation: {signal} (Strength: {strength_pct:.1f}%)")
        else:
            signal = "NEUTRAL"
            summary.append(f"\nOverall Recommendation: {signal}")
            
        summary.append(f"Buy Signals: {buy_signals}")
        summary.append(f"Sell Signals: {sell_signals}")
        summary.append(f"Neutral Signals: {neutral_signals}")
            
        return "\n".join(summary)

if __name__ == "__main__":
    # Example usage with sample data
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from data.stock_data import StockData
    
    stock = StockData()
    data = stock.fetch_data("BBCA.JK", period="1y")
    
    ta = TechnicalAnalysis(data)
    print(ta.generate_summary())