import pandas as pd
import numpy as np
from datetime import datetime, timedelta

class TradeAdvisor:
    """
    Trade Advisor class for providing enhanced trading recommendations
    by analyzing market data and transaction history
    """
    
    def __init__(self, transaction_history):
        """
        Initialize with transaction history
        
        Parameters:
        transaction_history: TransactionHistory object
        """
        self.transaction_history = transaction_history
        
    def analyze_past_trades(self, symbol, current_data):
        """
        Analyze past trades for a given symbol to find patterns and improve recommendations
        
        Parameters:
        symbol (str): Stock symbol
        current_data (DataFrame): Current market data
        
        Returns:
        dict: Analysis results with patterns and insights
        """
        # Get all transactions for this symbol
        transactions = self.transaction_history.get_transactions(symbol)
        
        if transactions.empty:
            return {
                "has_history": False,
                "avg_holding_period": 0,
                "avg_profit_trades": 0,
                "avg_loss_trades": 0,
                "win_rate": 0,
                "risk_profile": "UNKNOWN",
                "trade_frequency": "FIRST_TRADE",
                "common_errors": [],
                "success_patterns": []
            }
        
        # Extract buy and sell transactions
        buy_txns = transactions[transactions["transaction_type"] == "BUY"]
        sell_txns = transactions[transactions["transaction_type"] == "SELL"]
        
        # Calculate key metrics
        total_trades = len(sell_txns)
        
        # Initialize analysis results
        analysis = {
            "has_history": True,
            "total_trades": total_trades,
            "win_rate": 0,
            "avg_holding_period": 0,
            "avg_profit_trades": 0,
            "avg_loss_trades": 0,
            "risk_profile": "MODERATE",
            "trade_frequency": "LOW",
            "common_errors": [],
            "success_patterns": []
        }
        
        # If no completed trades yet, return basic analysis
        if total_trades == 0:
            analysis["trade_frequency"] = "FIRST_POSITION" if len(buy_txns) > 0 else "NO_TRADES"
            return analysis
        
        # Calculate win rate
        profitable_trades = sell_txns[sell_txns["realized_pnl"] > 0]
        loss_trades = sell_txns[sell_txns["realized_pnl"] <= 0]
        
        win_rate = len(profitable_trades) / total_trades * 100 if total_trades > 0 else 0
        analysis["win_rate"] = win_rate
          # Calculate average holding periods
        holding_periods = []
        for _, sell_row in sell_txns.iterrows():
            try:
                sell_date_str = sell_row["transaction_date"]
                sell_date = pd.to_datetime(sell_date_str) if isinstance(sell_date_str, str) else sell_date_str
                
                # Ensure entry_date is datetime
                buy_txns_copy = buy_txns.copy()
                buy_txns_copy["entry_date"] = buy_txns_copy["entry_date"].apply(
                    lambda x: pd.to_datetime(x) if isinstance(x, str) else x)
                
                matched_buys = buy_txns_copy[buy_txns_copy["entry_date"] < sell_date]
                
                if not matched_buys.empty:
                    buy_date_str = matched_buys["entry_date"].iloc[0]
                    buy_date = pd.to_datetime(buy_date_str) if isinstance(buy_date_str, str) else buy_date_str
                    holding_period = (sell_date - buy_date).days
                    holding_periods.append(holding_period)
            except Exception as e:
                print(f"Error calculating holding period in trade analysis: {e}")
        
        analysis["avg_holding_period"] = np.mean(holding_periods) if holding_periods else 0
        
        # Calculate average profit and loss percentages
        profit_percentages = profitable_trades["pnl_percentage"].tolist()
        loss_percentages = loss_trades["pnl_percentage"].tolist()
        
        analysis["avg_profit_trades"] = np.mean(profit_percentages) if profit_percentages else 0
        analysis["avg_loss_trades"] = np.mean(loss_percentages) if loss_percentages else 0
        
        # Determine risk profile based on trading history
        if win_rate >= 70:
            analysis["risk_profile"] = "CONSERVATIVE"
        elif win_rate >= 50:
            analysis["risk_profile"] = "MODERATE"
        else:
            analysis["risk_profile"] = "AGGRESSIVE"
            
        # Determine trading frequency
        days_since_first_trade = (datetime.now() - pd.to_datetime(transactions["entry_date"].min())).days
        if days_since_first_trade > 0:
            trades_per_month = total_trades / (days_since_first_trade / 30)
            if trades_per_month >= 5:
                analysis["trade_frequency"] = "HIGH"
            elif trades_per_month >= 2:
                analysis["trade_frequency"] = "MODERATE"
            else:
                analysis["trade_frequency"] = "LOW"
            
        # Identify common trading errors
        if win_rate < 40:
            analysis["common_errors"].append("LOW_WIN_RATE: Perlu evaluasi strategi masuk/keluar pasar")
            
        if analysis["avg_loss_trades"] < -15:
            analysis["common_errors"].append("LARGE_LOSSES: Stop loss tidak diterapkan dengan baik")
            
        if len(profitable_trades) > 0 and analysis["avg_profit_trades"] < 10:
            analysis["common_errors"].append("SMALL_PROFITS: Target profit terlalu rendah")
            
        # Identify successful trading patterns
        if win_rate > 60:
            analysis["success_patterns"].append("HIGH_ACCURACY: Strategi entry yang baik")
            
        if len(profitable_trades) > 0 and analysis["avg_profit_trades"] > 20:
            analysis["success_patterns"].append("LETTING_PROFITS_RUN: Menahan posisi profit dengan baik")
            
        if len(loss_trades) > 0 and abs(analysis["avg_loss_trades"]) < 10:
            analysis["success_patterns"].append("GOOD_RISK_MANAGEMENT: Kerugian terkontrol dengan baik")
            
        return analysis
        
    def get_enhanced_recommendation(self, symbol, technical_signals, position_data, price_data, trade_action):
        """
        Generate enhanced trading recommendations based on technical signals and transaction history
        
        Parameters:
        symbol (str): Stock symbol
        technical_signals (dict): Technical analysis signals
        position_data (dict): Current position data
        price_data (DataFrame): Price data
        trade_action (str): Base recommendation (BUY/SELL/HOLD)
        
        Returns:
        dict: Enhanced trading recommendation
        """
        # Get trade history analysis
        trade_history = self.analyze_past_trades(symbol, price_data)
          # Check if we have positions for sell recommendations
        has_position = position_data.get("current_position", 0) > 0
        
        # If the base action is SELL but we don't have a position, change to SHORT or NEUTRAL
        if trade_action == "JUAL 🔴" and not has_position:
            # Determine if conditions are strong enough for a short position
            rsi = technical_signals.get("rsi", 50)
            macd_hist = technical_signals.get("macd_hist", 0)
            
            if rsi > 70 or macd_hist < -0.5:  # Strong overbought or strong downtrend
                trade_action = "SHORT SELL 🔴"  # Recommend short selling
            else:
                trade_action = "TAHAN ⚪"  # Neutral recommendation
        
        # Start with the base recommendation
        recommendation = {
            "action": trade_action,
            "confidence": 0,
            "reasons": [],
            "risk_level": "MODERATE",
            "stop_loss": 0,
            "target_price": 0,
            "time_horizon": "MEDIUM",
            "position_sizing": 0,
            "risk_reward_ratio": 0,
        }
        
        # Current price
        current_price = price_data['Close'].iloc[-1]
        
        # Calculate volatility for stop loss and target calculation
        volatility = price_data['Close'].pct_change().std() * 100
        
        # Set confidence level based on technical signals and history
        signals_strength = technical_signals.get("strength", 50)
        history_confidence = 0
        
        if trade_history["has_history"]:
            # Adjust confidence based on past performance
            if trade_action == "BELI/TAMBAH POSISI 🟢" and trade_history["win_rate"] > 60:
                history_confidence = 20
            elif trade_action == "JUAL 🔴" and trade_history["win_rate"] < 40:
                history_confidence = 20
            else:
                history_confidence = 10
            
        recommendation["confidence"] = min(signals_strength + history_confidence, 100)
        
        # Determine risk level based on price volatility and past trades
        if volatility > 3:
            recommendation["risk_level"] = "HIGH"
        elif volatility > 1.5:
            recommendation["risk_level"] = "MODERATE"
        else:
            recommendation["risk_level"] = "LOW"
            
        if trade_history["has_history"]:
            # Adjust risk based on trading history
            if trade_history["risk_profile"] == "AGGRESSIVE":
                recommendation["risk_level"] = "HIGH"
            elif trade_history["risk_profile"] == "CONSERVATIVE":
                if recommendation["risk_level"] == "HIGH":
                    recommendation["risk_level"] = "MODERATE"
        
        # Calculate stop loss and target price
        if trade_action == "BELI/TAMBAH POSISI 🟢":
            # For buy recommendations
            stop_loss_pct = max(2, min(volatility * 1.5, 7))  # Between 2% and 7%
            target_pct = max(5, min(volatility * 3, 20))  # Between 5% and 20%
            
            recommendation["stop_loss"] = current_price * (1 - stop_loss_pct/100)
            recommendation["target_price"] = current_price * (1 + target_pct/100)
            recommendation["risk_reward_ratio"] = target_pct / stop_loss_pct
            
            # Adjust time horizon based on volatility and historical holding periods
            if trade_history["has_history"] and trade_history["avg_holding_period"] > 0:
                if trade_history["avg_holding_period"] > 90:
                    recommendation["time_horizon"] = "LONG"
                elif trade_history["avg_holding_period"] > 30:
                    recommendation["time_horizon"] = "MEDIUM"
                else:
                    recommendation["time_horizon"] = "SHORT"
            else:
                # Default based on volatility
                if volatility < 1.5:
                    recommendation["time_horizon"] = "LONG"
                elif volatility < 2.5:
                    recommendation["time_horizon"] = "MEDIUM"
                else:
                    recommendation["time_horizon"] = "SHORT"
              # Position sizing recommendation based on risk profile
            if recommendation["risk_level"] == "LOW":
                recommendation["position_sizing"] = 10  # Percentage of available capital
            elif recommendation["risk_level"] == "MODERATE":
                recommendation["position_sizing"] = 7
            else:
                recommendation["position_sizing"] = 5
                
        elif trade_action == "JUAL 🔴" or trade_action == "SHORT SELL 🔴":
            # Handles both regular sell and short sell recommendations
            if position_data.get("avg_buy_price", 0) > 0:
                # Regular sell - we have a position
                entry_price = position_data["avg_buy_price"]
                pnl_pct = (current_price - entry_price) / entry_price * 100
                
                recommendation["entry_price"] = entry_price
                recommendation["current_pnl_pct"] = pnl_pct
                
                # Check if we're in profit or loss
                if pnl_pct > 0:
                    # In profit, recommend trailing stop
                    trail_pct = max(2, min(volatility, 5))
                    recommendation["trailing_stop_pct"] = trail_pct
                    recommendation["trailing_stop"] = current_price * (1 - trail_pct/100)
                else:
                    # In loss, recommend stop if further decline expected
                    lower_target = current_price * (1 - volatility/100)
                    recommendation["stop_price"] = lower_target
            else:
                # Short sell recommendation - no current position
                trail_pct = max(2, min(volatility, 5))
                recommendation["trailing_stop_pct"] = trail_pct
                recommendation["trailing_stop"] = current_price * (1 + trail_pct/100)  # For short, stop is above current price
                
                # Calculate potential target based on technical indicators
                target_pct = max(5, min(volatility * 2, 15))
                recommendation["target_price"] = current_price * (1 - target_pct/100)
                recommendation["risk_reward_ratio"] = target_pct / trail_pct
        
        # Generate reasons based on technical signals and history
        if trade_history["has_history"]:
            for error in trade_history["common_errors"]:
                recommendation["reasons"].append(f"TRADE HISTORY: {error}")
                
            for pattern in trade_history["success_patterns"]:
                recommendation["reasons"].append(f"SUCCESSFUL PATTERN: {pattern}")
                
        # Add risk-reward explanation if buying
        if trade_action == "BELI/TAMBAH POSISI 🟢":
            recommendation["reasons"].append(
                f"RISK-REWARD: Rasio {recommendation['risk_reward_ratio']:.2f}:1 " +
                f"(Target: +{(recommendation['target_price']/current_price - 1)*100:.2f}%, " +
                f"Stop: -{(1 - recommendation['stop_loss']/current_price)*100:.2f}%)"
            )
            
        return recommendation
