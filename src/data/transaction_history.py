import os
import pandas as pd
from datetime import datetime

class TransactionHistory:
    def __init__(self, filename="transaction_history.csv"):
        self.filename = filename
        self.history_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "transaction_history")
        self.filepath = os.path.join(self.history_dir, filename)
        self._init_history_file()
    
    def _init_history_file(self):
        """Initialize history file if it doesn't exist"""
        os.makedirs(self.history_dir, exist_ok=True)
        
        columns = [
            "entry_date",           # Tanggal beli sesuai input user
            "transaction_date",      # Tanggal eksekusi transaksi
            "symbol",               # Kode saham
            "transaction_type",      # BUY/SELL
            "price",                # Harga per lembar
            "lot_size",             # Jumlah lot
            "shares",               # Jumlah lembar (lot_size * 100)
            "total_value",          # Nilai total transaksi
            "running_lot_balance",  # Sisa lot setelah transaksi
            "avg_buy_price",        # Rata-rata harga beli
            "realized_pnl",         # Profit/Loss untuk transaksi SELL
            "unrealized_pnl",       # Profit/Loss paper untuk transaksi BUY
            "pnl_percentage",       # Persentase Profit/Loss
            "holding_period",       # Durasi hold dalam hari
            "status"                # Status transaksi
        ]
        
        if not os.path.exists(self.filepath):
            # Create new empty DataFrame with columns
            df = pd.DataFrame(columns=columns)
            df.to_csv(self.filepath, index=False)
        else:
            try:
                # Try to read existing file
                df = pd.read_csv(self.filepath)
                # Check if all required columns exist
                missing_columns = [col for col in columns if col not in df.columns]
                if missing_columns:
                    # Add missing columns with default values
                    for col in missing_columns:
                        df[col] = 0 if col in ["shares", "total_value", "running_lot_balance", "avg_buy_price", "realized_pnl", "unrealized_pnl", "pnl_percentage", "holding_period"] else ""
                    df.to_csv(self.filepath, index=False)
            except (pd.errors.EmptyDataError, pd.errors.ParserError):
                # If file is empty or corrupted, create new one
                df = pd.DataFrame(columns=columns)
                df.to_csv(self.filepath, index=False)

    def get_transactions(self, symbol=None):
        """Get transaction history, optionally filtered by symbol"""
        try:
            df = pd.read_csv(self.filepath)
            if symbol:
                return df[df["symbol"] == symbol]
            return df
        except pd.errors.EmptyDataError:
            # Return empty DataFrame with proper columns
            columns = [
                "entry_date", "transaction_date", "symbol", "transaction_type",
                "price", "lot_size", "shares", "total_value", "running_lot_balance",
                "avg_buy_price", "realized_pnl", "unrealized_pnl", "pnl_percentage",
                "holding_period", "status"
            ]
            return pd.DataFrame(columns=columns)

    def add_transaction(self, symbol, transaction_type, price, lot_size, input_date=None, status="EXECUTED"):
        """Add new transaction to history"""
        now = datetime.now()
        market_hour = "09:00:00"  # Default waktu buka market
        
        # entry_date selalu menggunakan current time
        entry_date = now.strftime("%Y-%m-%d %H:%M:%S")
        
        # Parse input_date for both BUY and SELL transactions if provided
        if input_date:
            try:
                # Handle DDMMYY format (6 digits)
                if len(input_date) == 6:
                    day = input_date[:2]
                    month = input_date[2:4]
                    year = "20" + input_date[4:]  # Assuming years 2000-2099
                    formatted_date = f"{year}-{month}-{day} {market_hour}"
                # Handle DD-MM-YY or DD/MM/YY formats
                elif len(input_date) == 8 and (input_date[2] in ['-', '/']):
                    day = input_date[:2]
                    month = input_date[3:5]
                    year = "20" + input_date[6:]  # Assuming years 2000-2099
                    formatted_date = f"{year}-{month}-{day} {market_hour}"
                # Handle YYYY-MM-DD format
                elif len(input_date) == 10 and input_date[4] == '-' and input_date[7] == '-':
                    formatted_date = f"{input_date} {market_hour}"
                else:
                    # Unknown format, use current date
                    raise ValueError("Unrecognized date format")
                    
                parsed_date = datetime.strptime(formatted_date, "%Y-%m-%d %H:%M:%S")
                transaction_date = parsed_date.strftime("%Y-%m-%d %H:%M:%S")
            except ValueError as e:
                print(f"Error parsing date: {e}")
                # If date parsing fails, use current date
                if transaction_type == "BUY":
                    # For BUY, use current date with market hour
                    transaction_date = now.strftime("%Y-%m-%d") + f" {market_hour}"
                else:
                    # For SELL, use current timestamp
                    transaction_date = now.strftime("%Y-%m-%d %H:%M:%S")
        else:
            # If no date provided
            if transaction_type == "BUY":
                # For BUY, use current date with market hour
                transaction_date = now.strftime("%Y-%m-%d") + f" {market_hour}"
            else:
                # For SELL, use current timestamp
                transaction_date = now.strftime("%Y-%m-%d %H:%M:%S")

        # Get existing transactions for this symbol
        df = self.get_transactions(symbol)
        
        # Calculate running lot balance and average buy price
        buy_lots = df[df["transaction_type"] == "BUY"]["lot_size"].sum()
        sell_lots = df[df["transaction_type"] == "SELL"]["lot_size"].sum()
        current_position = buy_lots - sell_lots
        
        shares = lot_size * 100
        total_value = price * shares
        
        if transaction_type == "BUY":
            running_lot_balance = current_position + lot_size
            
            # Calculate new average buy price
            total_buy_value = df[df["transaction_type"] == "BUY"]["total_value"].sum() + total_value
            total_buy_lots = buy_lots + lot_size
            avg_buy_price = total_buy_value / (total_buy_lots * 100) if total_buy_lots > 0 else price
            
            # Calculate unrealized P&L
            unrealized_pnl = 0  # Will be updated when market price is available
            realized_pnl = 0
            pnl_percentage = 0
            holding_period = 0  # New position
            
        else:  # SELL
            running_lot_balance = current_position - lot_size
            
            # Keep existing average buy price
            buy_value = df[df["transaction_type"] == "BUY"]["total_value"].sum()
            avg_buy_price = buy_value / (buy_lots * 100) if buy_lots > 0 else 0
            
            # Calculate realized P&L
            cost_basis = avg_buy_price * shares
            realized_pnl = total_value - cost_basis
            pnl_percentage = (realized_pnl / cost_basis * 100) if cost_basis > 0 else 0
            unrealized_pnl = 0
            
            # Calculate holding period from earliest remaining buy
            if df[df["transaction_type"] == "BUY"].empty:
                holding_period = 0
            else:
                try:
                    earliest_buy_str = df[df["transaction_type"] == "BUY"]["transaction_date"].min()
                    if isinstance(earliest_buy_str, str):
                        earliest_buy = pd.to_datetime(earliest_buy_str)
                        holding_period = (datetime.now() - earliest_buy).days
                    else:
                        holding_period = 0
                except Exception as e:
                    print(f"Error calculating holding period: {e}")
                    holding_period = 0

        transaction = {
            "entry_date": entry_date,
            "transaction_date": transaction_date,
            "symbol": symbol,
            "transaction_type": transaction_type,
            "price": price,
            "lot_size": lot_size,
            "shares": shares,
            "total_value": total_value,
            "running_lot_balance": running_lot_balance,
            "avg_buy_price": avg_buy_price,
            "realized_pnl": realized_pnl,
            "unrealized_pnl": unrealized_pnl,
            "pnl_percentage": pnl_percentage,
            "holding_period": holding_period,
            "status": status
        }
        
        # Try to read existing data with required columns
        try:
            all_transactions = pd.read_csv(self.filepath)
            # Convert the new transaction to DataFrame with the same columns as existing data
            new_transaction_df = pd.DataFrame([transaction])
            # Ensure both DataFrames have the same columns
            for col in all_transactions.columns:
                if col not in new_transaction_df:
                    new_transaction_df[col] = None
            # Append new transaction
            all_transactions = pd.concat([all_transactions, new_transaction_df], ignore_index=True)
        except pd.errors.EmptyDataError:
            # If file is empty, create DataFrame with proper columns
            all_transactions = pd.DataFrame([transaction])
        
        # Save back to file
        all_transactions.to_csv(self.filepath, index=False)

    def get_position_summary(self, symbol):
        """Get current position summary for a symbol"""
        df = self.get_transactions(symbol)
        if df.empty:
            return {
                "current_position": 0,
                "total_buy_lots": 0,
                "total_sell_lots": 0,
                "avg_buy_price": 0,
                "total_buy_value": 0,
                "total_sell_value": 0,
                "total_realized_pnl": 0,
                "total_unrealized_pnl": 0,
                "total_pnl": 0,
                "pnl_percentage": 0,
                "holding_period": 0
            }
        
        buy_df = df[df["transaction_type"] == "BUY"]
        sell_df = df[df["transaction_type"] == "SELL"]
        
        buy_lots = buy_df["lot_size"].sum()
        sell_lots = sell_df["lot_size"].sum()
        current_position = buy_lots - sell_lots
        
        buy_value = buy_df["total_value"].sum()
        sell_value = sell_df["total_value"].sum()
        
        total_realized_pnl = df["realized_pnl"].sum()
        total_unrealized_pnl = df["unrealized_pnl"].sum()
        total_pnl = total_realized_pnl + total_unrealized_pnl
        
        if buy_lots > 0:
            avg_buy_price = buy_value / (buy_lots * 100)
            # Calculate P&L percentage based on total investment
            pnl_percentage = (total_pnl / buy_value * 100) if buy_value > 0 else 0
            
            # Get holding period from earliest remaining buy
            if current_position > 0:
                try:
                    earliest_buy_str = buy_df["transaction_date"].min()
                    if isinstance(earliest_buy_str, str):
                        earliest_buy = pd.to_datetime(earliest_buy_str)
                        holding_period = (datetime.now() - earliest_buy).days
                    else:
                        holding_period = 0
                except Exception as e:
                    print(f"Error calculating holding period: {e}")
                    holding_period = 0
            else:
                holding_period = 0
        else:
            avg_buy_price = 0
            pnl_percentage = 0
            holding_period = 0
            
        return {
            "current_position": current_position,
            "total_buy_lots": buy_lots,
            "total_sell_lots": sell_lots,
            "avg_buy_price": avg_buy_price,
            "total_buy_value": buy_value,
            "total_sell_value": sell_value,
            "total_realized_pnl": total_realized_pnl,
            "total_unrealized_pnl": total_unrealized_pnl,
            "total_pnl": total_pnl,
            "pnl_percentage": pnl_percentage,
            "holding_period": holding_period
        }

    def get_position_detail(self, symbol):
        """Get detailed position information for a symbol"""
        summary = self.get_position_summary(symbol)
        df = self.get_transactions(symbol)
        
        if df.empty:
            return f"""
Informasi Posisi {symbol}:
Jumlah Lot       : 0 lot
Harga Rata-rata  : Rp 0
Total Investasi  : Rp 0
Status          : Tidak ada posisi
            """
        
        # Format currency values
        def format_currency(value):
            return f"Rp {value:,.0f}".replace(",", ".")
        
        # Format percentage with color indicators
        def format_percentage(value):
            if value > 0:
                return f"+{value:.2f}% 📈"
            elif value < 0:
                return f"{value:.2f}% 📉"
            else:
                return f"{value:.2f}%"
        
        # Get latest transaction price and current market price (if available)
        try:
            from src.data.stock_data import StockData
            stock_data = StockData()
            latest_market_data = stock_data.get_current_price(symbol)
            current_market_price = latest_market_data.get("price", df.iloc[-1]["price"])
            
            # Update unrealized P&L for each BUY transaction that hasn't been fully sold
            if summary["current_position"] > 0:
                # Calculate unrealized P&L based on current market price
                cost_basis = summary["current_position"] * 100 * summary["avg_buy_price"]
                market_value = summary["current_position"] * 100 * current_market_price
                summary["total_unrealized_pnl"] = market_value - cost_basis
        except Exception as e:
            print(f"Error getting current price: {e}")
            current_market_price = df.iloc[-1]["price"]

        # Get earliest buy transaction date still in position for holding period
        buy_transactions = df[df["transaction_type"] == "BUY"]
        earliest_date = None
        if not buy_transactions.empty and summary["current_position"] > 0:
            try:
                earliest_buy_str = buy_transactions["transaction_date"].min()
                if isinstance(earliest_buy_str, str):
                    earliest_date = pd.to_datetime(earliest_buy_str).strftime("%d %b %Y")
                else:
                    earliest_date = "N/A"
            except Exception as e:
                print(f"Error formatting earliest date: {e}")
                earliest_date = "N/A"
        
        # Calculate unrealized P&L if there's current position
        if summary["current_position"] > 0:
            current_value = summary["current_position"] * 100 * current_market_price
            current_cost_basis = summary["current_position"] * 100 * summary["avg_buy_price"]
            unrealized_pnl = current_value - current_cost_basis
            unrealized_pnl_pct = (unrealized_pnl / current_cost_basis * 100) if current_cost_basis > 0 else 0
        else:
            unrealized_pnl = 0
            unrealized_pnl_pct = 0
        
        # Get price movement indicators
        price_diff = current_market_price - summary['avg_buy_price']
        price_indicator = '↑' if price_diff > 0 else '↓' if price_diff < 0 else '→'
        
        # Calculate price movement percentage
        price_move_pct = (price_diff / summary['avg_buy_price'] * 100) if summary['avg_buy_price'] > 0 else 0
        
        # Format the position summary
        position_status = 'Ada posisi' if summary['current_position'] > 0 else 'Tidak ada posisi'
        status_emoji = '✅' if summary['current_position'] > 0 else '❌'
        
        # Format recent transactions table
        recent_transactions = ""
        if not df.empty:
            # Sort by transaction_date in descending order and take 5 most recent
            recent_df = df.sort_values('transaction_date', ascending=False).head(5)
            for _, row in recent_df.iterrows():
                txn_date = pd.to_datetime(row['transaction_date']).strftime("%d %b %Y")
                txn_type = "BELI" if row['transaction_type'] == "BUY" else "JUAL"
                txn_emoji = "🟢" if row['transaction_type'] == "BUY" else "🔴"
                txn_price = format_currency(row['price'])
                txn_lot = row['lot_size']
                txn_value = format_currency(row['total_value'])
                
                if row['transaction_type'] == "SELL" and row['realized_pnl'] != 0:
                    pnl_str = f" | P/L: {format_currency(row['realized_pnl'])} ({format_percentage(row['pnl_percentage'])})"
                else:
                    pnl_str = ""
                    
                recent_transactions += f"{txn_date} {txn_emoji} {txn_type} {txn_lot} lot @ {txn_price}{pnl_str}\n"
        
        return f"""
============================================================
💼 RINGKASAN POSISI TRADING {symbol}
============================================================
Status Posisi   : {position_status} {status_emoji}
Tanggal Beli    : {earliest_date or 'Tidak ada posisi'}
Harga Beli      : {format_currency(summary['avg_buy_price'])}
Harga Saat Ini  : {format_currency(current_market_price)} {price_indicator} ({format_percentage(price_move_pct)})
Jumlah Lot      : {summary['current_position']} lot
Jumlah Lembar   : {summary['current_position'] * 100} lembar
P/L per Saham   : {format_currency(price_diff)}
Total P/L       : {format_currency(unrealized_pnl)} ({format_percentage(unrealized_pnl_pct)})
Durasi Hold     : {summary['holding_period']} hari

============================================================
📊 RIWAYAT TRANSAKSI TERKINI
============================================================
{recent_transactions}
============================================================
RINGKASAN TOTAL TRANSAKSI
============================================================
Total Pembelian : {summary['total_buy_lots']} lot (Nilai: {format_currency(summary['total_buy_value'])})
Total Penjualan : {summary['total_sell_lots']} lot (Nilai: {format_currency(summary['total_sell_value'])})
P/L Realized    : {format_currency(summary['total_realized_pnl'])} ({format_percentage(summary['pnl_percentage'])})
        """
    def export_transactions_for_analysis(self, symbol=None, output_path=None):
        """
        Export transaction history to CSV in a format optimized for analysis
        
        Parameters:
        symbol (str): Symbol to filter by, if None exports all transactions
        output_path (str): Path to save the CSV file, if None returns DataFrame
        
        Returns:
        DataFrame if output_path is None, otherwise saves to CSV and returns None
        """
        df = self.get_transactions(symbol)
        
        if df.empty:
            print(f"No transactions found for {symbol or 'any symbol'}")
            return df
            
        # Add additional analysis columns
        df['transaction_date'] = pd.to_datetime(df['transaction_date'])
        df['entry_date'] = pd.to_datetime(df['entry_date'])
        
        # Add day of week, month, etc. for time-based analysis
        df['day_of_week'] = df['transaction_date'].dt.day_name()
        df['month'] = df['transaction_date'].dt.month_name()
        df['year'] = df['transaction_date'].dt.year
        df['quarter'] = df['transaction_date'].dt.quarter
        
        # Calculate delays in executing transactions
        df['execution_delay_seconds'] = (df['entry_date'] - df['transaction_date']).dt.total_seconds()
        
        # For SELL transactions, calculate holding period from the earliest BUY
        sell_df = df[df['transaction_type'] == 'SELL'].copy()
        for idx, row in sell_df.iterrows():
            # Find the earliest BUY transaction for this symbol before this SELL
            buy_txns = df[(df['symbol'] == row['symbol']) & 
                         (df['transaction_type'] == 'BUY') & 
                         (df['transaction_date'] < row['transaction_date'])]
            
            if not buy_txns.empty:
                earliest_buy = buy_txns['transaction_date'].min()
                holding_days = (row['transaction_date'] - earliest_buy).days
                df.at[idx, 'holding_period'] = holding_days
        
        # Calculate cumulative stats
        if symbol:
            # If filtering by symbol, calculate running totals
            df = df.sort_values('transaction_date')
            df['cumulative_pnl'] = df['realized_pnl'].cumsum()
            df['cumulative_investment'] = df.apply(
                lambda x: x['total_value'] if x['transaction_type'] == 'BUY' else -x['total_value'],
                axis=1
            ).cumsum()
        
        if output_path:
            # Create directory if it doesn't exist
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            
            # Save to CSV
            df.to_csv(output_path, index=False)
            print(f"Exported {len(df)} transactions to {output_path}")
            return None
        else:
            return df

    def analyze_performance(self, symbol=None):
        """
        Analyze trading performance for a symbol or the entire portfolio
        
        Parameters:
        symbol (str): Symbol to analyze, if None analyzes all transactions
        
        Returns:
        str: Formatted performance analysis report
        """
        df = self.get_transactions(symbol)
        
        if df.empty:
            return f"Tidak ada transaksi untuk {'saham ' + symbol if symbol else 'portofolio'}"
        
        # Format currency values
        def format_currency(value):
            return f"Rp {value:,.0f}".replace(",", ".")
        
        # Convert dates to datetime for analysis
        df['transaction_date'] = pd.to_datetime(df['transaction_date'])
        
        # Group by symbol if analyzing all
        performance_by_symbol = {}
        symbols = [symbol] if symbol else df['symbol'].unique()
        
        total_profit = 0
        total_loss = 0
        win_trades = 0
        loss_trades = 0
        
        for sym in symbols:
            sym_df = df[df['symbol'] == sym]
            sell_df = sym_df[sym_df['transaction_type'] == 'SELL']
            
            # Calculate profit/loss statistics for this symbol
            profit_trades = sell_df[sell_df['realized_pnl'] > 0]
            loss_trades_df = sell_df[sell_df['realized_pnl'] <= 0]
            
            win_trades += len(profit_trades)
            loss_trades += len(loss_trades_df)
            
            total_profit += profit_trades['realized_pnl'].sum()
            total_loss += abs(loss_trades_df['realized_pnl'].sum())
            
            # Calculate holding periods
            avg_holding = sell_df['holding_period'].mean() if len(sell_df) > 0 else 0
            
            performance_by_symbol[sym] = {
                'total_trades': len(sell_df),
                'win_trades': len(profit_trades),
                'loss_trades': len(loss_trades_df),
                'win_rate': len(profit_trades) / len(sell_df) * 100 if len(sell_df) > 0 else 0,
                'total_profit': profit_trades['realized_pnl'].sum(),
                'total_loss': loss_trades_df['realized_pnl'].sum(),
                'avg_profit': profit_trades['realized_pnl'].mean() if len(profit_trades) > 0 else 0,
                'avg_loss': loss_trades_df['realized_pnl'].mean() if len(loss_trades_df) > 0 else 0,
                'avg_holding_period': avg_holding,
                'largest_profit': profit_trades['realized_pnl'].max() if len(profit_trades) > 0 else 0,
                'largest_loss': loss_trades_df['realized_pnl'].min() if len(loss_trades_df) > 0 else 0
            }
        
        # Calculate overall statistics
        total_trades = win_trades + loss_trades
        win_rate = (win_trades / total_trades * 100) if total_trades > 0 else 0
        profit_factor = total_profit / total_loss if total_loss > 0 else float('inf')
        
        # Generate report
        report = []
        report.append("=" * 50)
        report.append(f"ANALISIS PERFORMA TRADING {'SAHAM ' + symbol if symbol else 'PORTOFOLIO'}")
        report.append("=" * 50)
        report.append("")
        
        # Overall statistics
        report.append("STATISTIK KESELURUHAN")
        report.append("-" * 30)
        report.append(f"Total Transaksi  : {total_trades}")
        report.append(f"Win Rate         : {win_rate:.2f}%")
        report.append(f"Profit Factor    : {profit_factor:.2f}")
        report.append(f"Total Profit     : {format_currency(total_profit)}")
        report.append(f"Total Loss       : {format_currency(total_loss)}")
        report.append(f"Net P/L          : {format_currency(total_profit - total_loss)}")
        
        # Per-symbol statistics
        if len(symbols) > 1:
            report.append("\nSTATISTIK PER SAHAM")
            report.append("-" * 30)
            
            for sym, stats in performance_by_symbol.items():
                if stats['total_trades'] > 0:
                    report.append(f"\n{sym}:")
                    report.append(f"  Win Rate: {stats['win_rate']:.2f}%")
                    report.append(f"  Profit/Loss: {format_currency(stats['total_profit'] + stats['total_loss'])}")
                    report.append(f"  Avg. Holding: {stats['avg_holding_period']:.1f} hari")
        
        # Time-based analysis
        if not df.empty:
            sell_df = df[df['transaction_type'] == 'SELL']
            if not sell_df.empty:
                report.append("\nANALISIS BERDASARKAN WAKTU")
                report.append("-" * 30)
                
                # Group by month and year
                sell_df['month_year'] = sell_df['transaction_date'].dt.strftime('%B %Y')
                monthly_pnl = sell_df.groupby('month_year')['realized_pnl'].sum()
                
                best_month = monthly_pnl.idxmax()
                worst_month = monthly_pnl.idxmin()
                
                report.append(f"Bulan Terbaik   : {best_month} ({format_currency(monthly_pnl.max())})")
                report.append(f"Bulan Terburuk  : {worst_month} ({format_currency(monthly_pnl.min())})")
                
                # Group by day of week
                sell_df['day_of_week'] = sell_df['transaction_date'].dt.day_name()
                dow_pnl = sell_df.groupby('day_of_week')['realized_pnl'].sum()
                
                # Sort by days of week
                days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
                dow_pnl = dow_pnl.reindex(days_order)
                
                best_day = dow_pnl.idxmax()
                report.append(f"Hari Terbaik    : {best_day} ({format_currency(dow_pnl.max())})")
        
        # Recommendations based on analysis
        report.append("\nREKOMENDASI")
        report.append("-" * 30)
        
        if win_rate < 50:
            report.append("⚠️ Win rate di bawah 50%. Pertimbangkan untuk meninjau strategi entry.")
        
        if profit_factor < 1:
            report.append("⚠️ Profit factor di bawah 1.0. Rata-rata kerugian lebih besar dari keuntungan.")
        
        if symbol and symbol in performance_by_symbol and performance_by_symbol[symbol]['avg_holding_period'] < 5:
            report.append("⚠️ Periode holding sangat singkat. Pertimbangkan untuk mengurangi trading jangka pendek.")
            
        return "\n".join(report)
