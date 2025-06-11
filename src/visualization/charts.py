import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.gridspec import GridSpec
import matplotlib.dates as mdates
from matplotlib.patches import Rectangle

class StockVisualizer:
    def __init__(self, data):
        """
        Initialize with stock data DataFrame
        
        Parameters:
        data (DataFrame): DataFrame with columns: Close, High, Low, Open, Volume
        """
        self.data = data.copy()
        self.setup_style()
        
    @staticmethod
    def setup_style():
        """Setup the visualization style"""
        plt.style.use('default')  # Use default style instead of seaborn
        plt.rcParams['figure.figsize'] = [12, 7]
        plt.rcParams['figure.dpi'] = 100
        plt.rcParams['axes.grid'] = True
        sns.set_palette("husl")
        
    def plot_price_history(self, title=None, save_path=None):
        """Plot the stock price history"""
        fig, ax = plt.subplots(figsize=(12, 6))
        
        ax.plot(self.data.index, self.data['Close'], label='Close Price', linewidth=2)
        ax.set_title(title or 'Stock Price History')
        ax.set_xlabel('Date')
        ax.set_ylabel('Price')
        ax.legend()
        ax.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path)
            plt.close()
        return fig
        
    def plot_technical_indicators(self, title=None, save_path=None):
        """Plot price with technical indicators"""
        fig = plt.figure(figsize=(12, 10))
        gs = GridSpec(3, 1, figure=fig, height_ratios=[3, 1, 1])
        
        # Price and indicators subplot
        ax1 = fig.add_subplot(gs[0])
        ax1.plot(self.data.index, self.data['Close'], label='Close Price', linewidth=2)
        
        if 'SMA_20' in self.data.columns:
            ax1.plot(self.data.index, self.data['SMA_20'], label='SMA 20', alpha=0.7)
        if 'SMA_50' in self.data.columns:
            ax1.plot(self.data.index, self.data['SMA_50'], label='SMA 50', alpha=0.7)
        if all(x in self.data.columns for x in ['BB_H', 'BB_M', 'BB_L']):
            ax1.plot(self.data.index, self.data['BB_H'], 'r--', label='BB Upper', alpha=0.6)
            ax1.plot(self.data.index, self.data['BB_M'], 'g--', label='BB Middle', alpha=0.6)
            ax1.plot(self.data.index, self.data['BB_L'], 'r--', label='BB Lower', alpha=0.6)
            
        ax1.set_title(title or 'Technical Analysis')
        ax1.set_ylabel('Price')
        ax1.legend(loc='upper left')
        ax1.grid(True)
        
        # RSI subplot
        ax2 = fig.add_subplot(gs[1])
        if 'RSI' in self.data.columns:
            ax2.plot(self.data.index, self.data['RSI'], label='RSI', color='purple')
            ax2.axhline(y=70, color='r', linestyle='--', alpha=0.5)
            ax2.axhline(y=30, color='g', linestyle='--', alpha=0.5)
            ax2.set_ylabel('RSI')
            ax2.legend()
            ax2.grid(True)
        
        # MACD subplot
        ax3 = fig.add_subplot(gs[2])
        if all(x in self.data.columns for x in ['MACD', 'MACD_Signal']):
            ax3.plot(self.data.index, self.data['MACD'], label='MACD', color='blue')
            ax3.plot(self.data.index, self.data['MACD_Signal'], label='Signal', color='orange')
            # Plot MACD histogram
            if 'MACD_Hist' in self.data.columns:
                colors = ['red' if x < 0 else 'green' for x in self.data['MACD_Hist']]
                ax3.bar(self.data.index, self.data['MACD_Hist'], label='Histogram', 
                       color=colors, alpha=0.5)
            ax3.set_ylabel('MACD')
            ax3.legend()
            ax3.grid(True)
        
        plt.xlabel('Date')
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path)
            plt.close()
        return fig
        
    def plot_volume_profile(self, title=None, save_path=None):
        """Plot volume profile with price action"""
        fig = plt.figure(figsize=(12, 8))
        gs = GridSpec(2, 1, figure=fig, height_ratios=[3, 1])
        
        # Price subplot
        ax1 = fig.add_subplot(gs[0])
        ax1.plot(self.data.index, self.data['Close'], label='Close Price', color='blue')
        ax1.set_title(title or 'Price and Volume Analysis')
        ax1.set_ylabel('Price')
        ax1.legend()
        ax1.grid(True)
        
        # Volume subplot
        ax2 = fig.add_subplot(gs[1])
        # Color volume bars based on price movement
        colors = ['red' if close < open else 'green' 
                 for close, open in zip(self.data['Close'], self.data['Open'])]
        ax2.bar(self.data.index, self.data['Volume'], color=colors, alpha=0.7)
        ax2.set_ylabel('Volume')
        
        plt.xlabel('Date')
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path)
            plt.close()
        return fig
        
    def plot_candlestick_pattern(self, title=None, save_path=None, position_price=None):
        """Plot candlestick chart with volume and optional position marker"""
        fig = plt.figure(figsize=(12, 8))
        gs = GridSpec(2, 1, figure=fig, height_ratios=[3, 1])
        ax1 = fig.add_subplot(gs[0])
        ax2 = fig.add_subplot(gs[1])
        
        # Plot candlesticks
        width = np.timedelta64(12, 'h') # Adjust candlestick width
        up = self.data[self.data['Close'] >= self.data['Open']]
        down = self.data[self.data['Close'] < self.data['Open']]
        
        # Up candlesticks
        ax1.bar(up.index, up['Close'] - up['Open'], width, bottom=up['Open'], color='g', alpha=0.6)
        ax1.bar(up.index, up['High'] - up['Close'], width/5, bottom=up['Close'], color='g', alpha=0.6)
        ax1.bar(up.index, up['Open'] - up['Low'], width/5, bottom=up['Low'], color='g', alpha=0.6)
        
        # Down candlesticks
        ax1.bar(down.index, down['Close'] - down['Open'], width, bottom=down['Open'], color='r', alpha=0.6)
        ax1.bar(down.index, down['High'] - down['Open'], width/5, bottom=down['Open'], color='r', alpha=0.6)
        ax1.bar(down.index, down['Low'] - down['Close'], width/5, bottom=down['Close'], color='r', alpha=0.6)
        
        # Tambahkan garis posisi jika diberikan
        if position_price is not None and position_price > 0:
            ax1.axhline(y=position_price, color='orange', linestyle='--', linewidth=2, label='Posisi Saya')
            ax1.legend()
        ax1.set_title(title or 'Candlestick Chart')
        ax1.set_ylabel('Price')
        ax1.grid(True)
        
        # Volume subplot
        colors = ['red' if close < open else 'green' 
                 for close, open in zip(self.data['Close'], self.data['Open'])]
        ax2.bar(self.data.index, self.data['Volume'], color=colors, alpha=0.7)
        ax2.set_ylabel('Volume')
        
        plt.xlabel('Date')
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path)
            plt.close()
        return fig
    
    def plot_candlestick(self, title=None, save_path=None):
        """
        Plot candlestick chart (alias for plot_candlestick_pattern)
        
        Parameters:
        title (str): Chart title
        save_path (str): Path to save the chart image
        
        Returns:
        matplotlib.figure.Figure: The figure object
        """
        return self.plot_candlestick_pattern(title, save_path)
        
    def plot_returns_distribution(self, title=None, save_path=None):
        """Plot the distribution of returns"""
        returns = self.data['Close'].pct_change().dropna()
        
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
        
        # Returns over time
        ax1.plot(self.data.index[1:], returns, label='Daily Returns')
        ax1.set_title('Daily Returns Over Time')
        ax1.set_ylabel('Returns')
        ax1.grid(True)
        ax1.legend()
        
        # Returns distribution
        sns.histplot(data=returns, bins=50, kde=True, ax=ax2)
        ax2.set_title('Returns Distribution')
        ax2.set_xlabel('Returns')
        ax2.set_ylabel('Frequency')
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path)
            plt.close()
        return fig
        
    def plot_correlation_heatmap(self, title=None, save_path=None):
        """Plot correlation heatmap of numerical columns"""
        numeric_cols = self.data.select_dtypes(include=[np.number]).columns
        correlation = self.data[numeric_cols].corr()
        
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(correlation, annot=True, cmap='coolwarm', center=0, ax=ax)
        ax.set_title(title or 'Correlation Heatmap')
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path)
            plt.close()
        return fig
        
    def generate_analysis_report(self, symbol=None, save_dir=None):
        """Generate a complete set of analysis plots and save them"""
        figures = []
        
        if save_dir:
            import os
            os.makedirs(save_dir, exist_ok=True)
        
        # Price history
        title = f'Price History - {symbol}' if symbol else 'Price History'
        save_path = os.path.join(save_dir, 'price_history.png') if save_dir else None
        figures.append(self.plot_price_history(title, save_path))
        
        # Technical indicators
        title = f'Technical Analysis - {symbol}' if symbol else 'Technical Analysis'
        save_path = os.path.join(save_dir, 'technical_analysis.png') if save_dir else None
        figures.append(self.plot_technical_indicators(title, save_path))
        
        # Volume profile
        title = f'Volume Analysis - {symbol}' if symbol else 'Volume Analysis'
        save_path = os.path.join(save_dir, 'volume_analysis.png') if save_dir else None
        figures.append(self.plot_volume_profile(title, save_path))
        
        # Candlestick pattern
        title = f'Candlestick Chart - {symbol}' if symbol else 'Candlestick Chart'
        save_path = os.path.join(save_dir, 'candlestick.png') if save_dir else None
        figures.append(self.plot_candlestick_pattern(title, save_path))
        
        # Returns distribution
        title = f'Returns Analysis - {symbol}' if symbol else 'Returns Analysis'
        save_path = os.path.join(save_dir, 'returns_analysis.png') if save_dir else None
        figures.append(self.plot_returns_distribution(title, save_path))
        
        # Correlation heatmap
        title = f'Correlation Analysis - {symbol}' if symbol else 'Correlation Analysis'
        save_path = os.path.join(save_dir, 'correlation.png') if save_dir else None
        figures.append(self.plot_correlation_heatmap(title, save_path))
        
        return figures

if __name__ == "__main__":
    # Example usage
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from data.stock_data import StockData
    from analysis.technical import TechnicalAnalysis
    
    # Fetch sample data
    stock = StockData()
    data = stock.fetch_data("BBCA.JK", period="1y")
    
    # Add technical indicators
    ta = TechnicalAnalysis(data)
    ta.add_sma(20)
    ta.add_sma(50)
    ta.add_ema(20)
    ta.add_macd()
    ta.add_rsi()
    ta.add_bollinger_bands()
    
    # Create visualizer and generate plots
    viz = StockVisualizer(ta.data)
    
    # Generate and save all plots
    save_dir = "stock_analysis_plots"
    figures = viz.generate_analysis_report(symbol="BBCA.JK", save_dir=save_dir)
    
    print(f"Analysis plots have been saved to: {save_dir}")