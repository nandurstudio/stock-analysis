# main_v2.py - Enhanced Stock Analyzer with Transaction History Tracking
import os
import time
from datetime import datetime, timedelta
import keyboard
import traceback
import msvcrt
import pytz
import pandas as pd
import numpy as np

from src.data.stock_data import StockData
from src.analysis.technical import TechnicalAnalysis
from src.analysis.prediction import StockPredictor
from src.visualization.charts import StockVisualizer
from src.utils.config import stock_config
from src.data.transaction_history import TransactionHistory
from src.analysis.trade_advisor import TradeAdvisor

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def format_number(num):
    """Format number with thousand separator and 2 decimal places"""
    return f"{num:,.2f}"

def get_trend_arrow(change):
    """Return trend arrow based on price change"""
    if change > 0:
        return "↑"
    elif change < 0:
        return "↓"
    return "→"

def analyze_stock_with_history(symbol, period="1y", output_dir="analysis_results"):
    """
    Analyze stock with enhanced recommendations based on transaction history
    
    Parameters:
    symbol (str): Stock symbol (e.g., 'BBCA.JK')
    period (str): Time period for analysis (default 1y)
    output_dir (str): Directory to save results
    
    Returns:
    dict: Analysis results
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # 1. Fetch Stock Data
    print(f"\nMengambil data {symbol}...")
    stock = StockData()
    data = stock.fetch_data(symbol, period=period)
    
    # Get current price and changes
    current_price = data['Close'].iloc[-1]
    prev_price = data['Close'].iloc[-2]
    price_change = current_price - prev_price
    price_change_pct = (price_change / prev_price) * 100
    
    # 2. Technical Analysis
    print("Melakukan analisis teknikal...")
    ta = TechnicalAnalysis(data)
    ta.add_sma(20)
    ta.add_sma(50)
    ta.add_ema(20)
    ta.add_macd()
    ta.add_rsi()
    ta.add_bollinger_bands()
    ta.add_obv()
    
    # Get technical signals
    technical_signals = ta.get_signals()
    
    # 3. Get transaction history
    print("Menganalisis riwayat transaksi...")
    th = TransactionHistory()
    position_summary = th.get_position_summary(symbol)
    
    # 4. Create advisor and get enhanced recommendations
    advisor = TradeAdvisor(th)
    
    # Basic recommendation score based on technical indicators
    points = 0
    signal_strength = 0
    
    # RSI Analysis (Weight: 25%)
    rsi_value = ta.data['RSI'].iloc[-1]
    if rsi_value > 70:
        points -= 3
        signal_strength += 25
    elif rsi_value < 30:
        points += 3
        signal_strength += 25
    elif 30 <= rsi_value <= 70:
        if rsi_value > 50:
            points += 1
        else:
            points -= 1
    
    # MACD Analysis (Weight: 20%)
    macd_hist = ta.data['MACD_Hist'].iloc[-1]
    if macd_hist > 0:
        points += 2
        signal_strength += 20
    else:
        points -= 2
        signal_strength += 20
    
    # Bollinger Bands Analysis (Weight: 15%)
    close_price = data['Close'].iloc[-1]
    bb_high = ta.data['BB_H'].iloc[-1]
    bb_low = ta.data['BB_L'].iloc[-1]
    
    bb_position = "ATAS" if close_price > bb_high else \
                 "BAWAH" if close_price < bb_low else "TENGAH"
    
    if bb_position == "ATAS":
        points -= 2
        signal_strength += 15
    elif bb_position == "BAWAH":
        points += 2
        signal_strength += 15
    
    # Volume Analysis (Weight: 15%)
    volume = data['Volume'].iloc[-1]
    avg_volume = data['Volume'].rolling(window=20).mean().iloc[-1]
    
    if volume > avg_volume * 1.5:
        if close_price > data['Close'].iloc[-2]:
            points += 2
        else:
            points -= 2
        signal_strength += 15
    
    # Trend Analysis (Weight: 25%)
    if close_price > ta.data['SMA_50'].iloc[-1]:
        points += 2
        signal_strength += 25
    else:
        points -= 2
        signal_strength += 25
    
    # Determine base recommendation
    if points >= 3:
        action = "BELI/TAMBAH POSISI 🟢"
    elif points <= -3:
        action = "JUAL 🔴"
    else:
        action = "TAHAN ⚪"
    
    # Get enhanced recommendation
    technical_data = {
        "strength": signal_strength,
        "rsi": rsi_value,
        "macd_hist": macd_hist,
        "bb_position": bb_position,
        "price": current_price,
        "volume_ratio": volume / avg_volume if avg_volume > 0 else 1
    }
    
    enhanced_recommendation = advisor.get_enhanced_recommendation(
        symbol, 
        technical_data, 
        position_summary, 
        data,
        action
    )
    
    # 5. Create visualization
    print("Membuat visualisasi...")
    viz = StockVisualizer(data)
    charts_dir = os.path.join(output_dir, f"{symbol}_charts")
    os.makedirs(charts_dir, exist_ok=True)
      # Save charts
    viz.plot_price_history(title=f"{symbol} Price History", 
                         save_path=os.path.join(charts_dir, "price_history.png"))
    
    viz.plot_technical_indicators(title=f"{symbol} Technical Analysis", 
                                save_path=os.path.join(charts_dir, "technical_analysis.png"))
    
    viz.plot_candlestick_pattern(title=f"{symbol} Candlestick Chart", 
                       save_path=os.path.join(charts_dir, "candlestick.png"))
    
    # Optional prediction
    try:
        print("Membuat prediksi harga...")
        predictor = StockPredictor(data)
        prediction_data = predictor.predict_next_days(days=5)
    except Exception as e:
        prediction_data = None
        print(f"Error during prediction: {e}")
    
    # Format results
    results = {
        'symbol': symbol,
        'data': data,
        'current_price': current_price,
        'price_change': price_change,
        'price_change_pct': price_change_pct,
        'technical_signals': technical_signals,
        'position_summary': position_summary,
        'recommendation': enhanced_recommendation,
        'charts_dir': charts_dir,
        'prediction': prediction_data,
        'ta_data': ta.data
    }
    
    # Save data to CSV
    data.to_csv(os.path.join(output_dir, f"{symbol}_data.csv"))
    
    # Display results
    display_analysis_results(results)
    
    return results

def display_analysis_results(results):
    """
    Display analysis results in an enhanced, professional format
    
    Parameters:
    results (dict): Analysis results from analyze_stock_with_history
    """
    symbol = results['symbol']
    data = results['data']
    current_price = results['current_price']
    price_change = results['price_change']
    price_change_pct = results['price_change_pct']
    technical_signals = results['technical_signals']
    position_summary = results['position_summary']
    recommendation = results['recommendation']
    ta_data = results['ta_data']
    
    # Get day's high and low
    day_high = data['High'].iloc[-1]
    day_low = data['Low'].iloc[-1]
    
    # Get volume
    volume = data['Volume'].iloc[-1]
    avg_volume = data['Volume'].rolling(window=5).mean().iloc[-1]
    volume_change_pct = ((volume - avg_volume) / avg_volume) * 100
    
    clear_screen()
    
    # === HEADER SECTION ===
    print(f"\n{'='*80}")
    print(f"ANALISIS SAHAM: {symbol} - {datetime.now().strftime('%d %b %Y %H:%M')}")
    print(f"{'='*80}")
    
    # === PRICE & VOLUME SECTION ===
    print(f"\n📊 HARGA & VOLUME")
    print(f"{'─'*80}")
    print(f"Harga Saat Ini  : Rp {format_number(current_price)} {get_trend_arrow(price_change)}")
    print(f"Perubahan       : {price_change:+,.2f} ({price_change_pct:+.2f}%)")
    print(f"Range Hari Ini  : Rp {format_number(day_low)} - Rp {format_number(day_high)}")
    print(f"Volume          : {volume:,.0f} lot ({volume_change_pct:+.1f}% dari rata-rata)")
    
    # === TECHNICAL ANALYSIS SECTION ===
    print(f"\n📈 ANALISIS TEKNIKAL")
    print(f"{'─'*80}")
    
    # RSI Analysis
    rsi_value = ta_data['RSI'].iloc[-1]
    rsi_status = "OVERBOUGHT 🔴" if rsi_value > 70 else "OVERSOLD 🟢" if rsi_value < 30 else "NETRAL ⚪"
    print(f"RSI ({format_number(rsi_value)})      : {rsi_status}")
    
    # MACD Analysis
    macd = ta_data['MACD'].iloc[-1]
    macd_signal = ta_data['MACD_Signal'].iloc[-1]
    macd_hist = ta_data['MACD_Hist'].iloc[-1]
    macd_direction = "BULLISH 🟢" if macd_hist > 0 else "BEARISH 🔴"
    print(f"MACD             : {format_number(macd_hist)} ({macd_direction})")
    
    # Moving Averages
    sma_20 = ta_data['SMA_20'].iloc[-1]
    sma_50 = ta_data['SMA_50'].iloc[-1]
    ma_trend = "BULLISH 🟢" if sma_20 > sma_50 else "BEARISH 🔴"
    print(f"MA Trend        : {ma_trend} (SMA20: {format_number(sma_20)}, SMA50: {format_number(sma_50)})")
    
    # Bollinger Bands
    bb_upper = ta_data['BB_H'].iloc[-1]
    bb_mid = ta_data['BB_M'].iloc[-1]
    bb_lower = ta_data['BB_L'].iloc[-1]
    
    if current_price > bb_upper:
        bb_position = "DI ATAS BAND (Potential Overbought) 🔴"
    elif current_price < bb_lower:
        bb_position = "DI BAWAH BAND (Potential Oversold) 🟢"
    else:
        bb_position = "DI DALAM BAND (Normal Range) ⚪"
    
    print(f"Bollinger Bands : {bb_position}")
    
    # === POSITION DETAILS SECTION ===
    if position_summary['current_position'] > 0:
        print(f"\n💼 POSISI SAHAM SAAT INI")
        print(f"{'─'*80}")
        print(f"Jumlah Lot      : {position_summary['current_position']:,d} lot ({position_summary['current_position']*100:,d} lembar)")
        print(f"Harga Rata-rata : Rp {format_number(position_summary['avg_buy_price'])}")
        print(f"Nilai Investasi : Rp {format_number(position_summary['total_buy_value'])}")
        print(f"Nilai Saat Ini  : Rp {format_number(position_summary['current_position']*100*current_price)}")
        
        # Calculate unrealized P/L
        unrealized_pnl = position_summary['current_position']*100*(current_price - position_summary['avg_buy_price'])
        unrealized_pnl_pct = (current_price/position_summary['avg_buy_price'] - 1) * 100
        print(f"Unrealized P/L  : Rp {format_number(unrealized_pnl)} ({unrealized_pnl_pct:+.2f}%)")
        print(f"Durasi Hold     : {position_summary['holding_period']} hari")
    else:
        print(f"\n💼 POSISI SAHAM SAAT INI")
        print(f"{'─'*80}")
        print(f"Status: Tidak memiliki posisi untuk {symbol}")
    
    # === RECOMMENDATION SECTION ===
    print(f"\n🎯 REKOMENDASI TRADING")
    print(f"{'─'*80}")
    
    action = recommendation['action']
    confidence = recommendation['confidence']
    reasons = recommendation['reasons']
    
    if action == "BELI/TAMBAH POSISI 🟢":
        print("REKOMENDASI KUAT: BELI/TAMBAH POSISI 🟢")
        print(f"\nStop Loss       : Rp {format_number(recommendation['stop_loss'])}")
        print(f"Target Price    : Rp {format_number(recommendation['target_price'])}")
        print(f"Risk-Reward     : {recommendation['risk_reward_ratio']:.2f}:1")
        print(f"Posisi Sizing   : {recommendation['position_sizing']}% dari modal tersedia")
        print(f"Time Horizon    : {recommendation['time_horizon']}")
    elif action == "JUAL 🔴":
        print("REKOMENDASI KUAT: JUAL 🔴")
        if 'trailing_stop' in recommendation:
            print(f"\nTrailing Stop   : Rp {format_number(recommendation['trailing_stop'])} ({recommendation['trailing_stop_pct']:.1f}%)")
        if 'stop_price' in recommendation:
            print(f"Target Harga    : Rp {format_number(recommendation['stop_price'])}")
        if 'current_pnl_pct' in recommendation:
            print(f"Persentase P/L  : {recommendation['current_pnl_pct']:+.2f}%")
    else:
        print("REKOMENDASI: TAHAN POSISI ⚪")
        print(f"\nLevel Support   : Rp {format_number(bb_lower)}")
        print(f"Level Resistance: Rp {format_number(bb_upper)}")
    
    print(f"\nTingkat Keyakinan: {confidence:.1f}%")
    print(f"Tingkat Risiko   : {recommendation['risk_level']}")
    
    print("\nAlasan Utama:")
    for reason in reasons[:3]:
        print(f"● {reason}")
    
    # === CONCLUSION SECTION ===
    print(f"\n{'='*80}")
    print("💡 KESIMPULAN AKHIR")
    print(f"{'='*80}")
    
    conclusion = ""
    if action == "BELI/TAMBAH POSISI 🟢":
        conclusion = f"Berdasarkan analisis teknikal dan riwayat transaksi dengan keyakinan {confidence:.1f}%, "
        conclusion += "sangat disarankan untuk MENAMBAH POSISI saat ini. "
        if position_summary['current_position'] > 0:
            conclusion += f"Gunakan stop loss di level Rp {format_number(recommendation['stop_loss'])} "
            conclusion += f"dan target profit di Rp {format_number(recommendation['target_price'])}. "
        else:
            conclusion += f"Mulai dengan {recommendation['position_sizing']}% dari modal tersedia "
            conclusion += f"dengan target profit Rp {format_number(recommendation['target_price'])} "
            conclusion += f"dan stop loss Rp {format_number(recommendation['stop_loss'])}. "
    elif action == "JUAL 🔴":
        conclusion = f"Berdasarkan analisis teknikal dan riwayat transaksi dengan keyakinan {confidence:.1f}%, "
        if position_summary['current_position'] > 0:
            if 'current_pnl_pct' in recommendation and recommendation['current_pnl_pct'] > 0:
                conclusion += "sangat disarankan untuk MENJUAL dan mengamankan profit. "
                conclusion += "Berdasarkan analisis, harga berpotensi mengalami koreksi. "
            else:
                conclusion += "sangat disarankan untuk MENJUAL dan membatasi kerugian. "
                conclusion += "Indikator teknikal menunjukkan potensi penurunan lebih lanjut. "
        else:
            conclusion += "kondisi pasar mendukung untuk melakukan SHORT SELLING "
            conclusion += "karena indikator teknikal menunjukkan tren bearish yang kuat. "
    else:
        conclusion = f"Berdasarkan analisis teknikal dan riwayat transaksi dengan keyakinan {confidence:.1f}%, "
        conclusion += "disarankan untuk MENAHAN posisi saat ini. "
        conclusion += "Pantau pergerakan harga di sekitar level support dan resistance "
        conclusion += "sebelum mengambil keputusan lebih lanjut. "
    
    print(conclusion)
    
    # === TRADE EXPLANATION SECTION ===
    print(f"\n{'='*80}")
    print("🧠 PENJELASAN SEDERHANA & TERMINOLOGI TRADING")
    print(f"{'='*80}")
    
    # Generate trade explanation
    explanation = generate_trade_explanation(
        action=action,
        technical_data={
            'rsi': rsi_value,
            'macd_hist': macd_hist,
            'price': current_price,
            'bb_position': bb_position,
            'volume_ratio': volume / avg_volume if avg_volume > 0 else 1
        },
        position_data=position_summary,
        recommendation=recommendation
    )
    
    print(explanation)

def generate_trade_explanation(action, technical_data, position_data, recommendation):
    """
    Generate detailed trade explanation with trading terminology
    
    Parameters:
    action (str): Recommended action (BUY/SELL/HOLD)
    technical_data (dict): Technical indicators data
    position_data (dict): Current position data
    recommendation (dict): Enhanced recommendation
    
    Returns:
    str: Detailed trade explanation
    """
    explanation = ""
    
    # Profit/Loss explanation
    if position_data['current_position'] > 0:
        price_diff = technical_data['price'] - position_data['avg_buy_price']
        profit_loss_pct = (price_diff / position_data['avg_buy_price']) * 100
        
        if profit_loss_pct <= -10:
            explanation += "💸 DRAWDOWN: Anda telah mengalami kerugian lebih dari 10%. "
            if action == "JUAL 🔴":
                explanation += "Menjual sekarang akan mengamankan sisa modal Anda dari potensi penurunan lebih lanjut. "
                explanation += "Prinsip 'cut loss' (batasi kerugian) sering digunakan untuk menghindari kerugian yang lebih besar. "
                explanation += "Dalam trading, istilah 'stop loss' digunakan untuk titik keluar otomatis saat kerugian mencapai batas tertentu.\n\n"
            else:
                explanation += "Namun indikator teknikal menunjukkan potensi pembalikan arah (reversal pattern), "
                explanation += "sehingga mungkin lebih baik menunggu pemulihan harga atau 'averaging down' "
                explanation += "dengan menambah posisi pada harga lebih rendah untuk menurunkan rata-rata harga beli.\n\n"
        elif profit_loss_pct >= 15:
            explanation += "💰 PROFITABLE POSITION: Anda telah mendapatkan keuntungan lebih dari 15%. "
            explanation += "Mengambil keuntungan (profit taking) adalah strategi yang baik untuk "
            explanation += "mengamankan keuntungan (lock in profit). Beberapa strategi yang umum: \n"
            explanation += "  - TRAILING STOP: Mengunci keuntungan sambil memberi ruang untuk kenaikan lebih lanjut\n"
            explanation += "  - SCALING OUT: Menjual sebagian posisi untuk mengambil profit parsial\n"
            explanation += "  - TAKE PROFIT: Menjual seluruh posisi ketika target harga tercapai\n\n"
    
    # Market momentum explanation
    if technical_data['macd_hist'] < 0:
        explanation += "📉 BEARISH MOMENTUM: Harga saham sedang dalam tren menurun (bearish), "
        explanation += "yang terlihat dari indikator MACD negatif (bearish crossover). "
        if action == "JUAL 🔴":
            explanation += "Menjual sekarang dapat menghindari kerugian lebih besar jika harga terus turun. "
            explanation += "Strategi 'Sell on Rally' - menjual saat ada kenaikan kecil dalam tren turun - "
            explanation += "sering digunakan dalam kondisi bearish market.\n\n"
        else:
            explanation += "Perhatikan level support (batas bawah) sebagai titik masuk potensial. "
            explanation += "Dalam kondisi downtrend, strategi yang umum adalah menunggu konfirmasi pembalikan (reversal confirmation).\n\n"
    elif technical_data['macd_hist'] > 0:
        explanation += "📈 BULLISH MOMENTUM: MACD menunjukkan momentum bullish (naik), "
        explanation += "yang berarti ada potensi kenaikan harga dalam waktu dekat (uptrend). "
        explanation += "MACD positif menandakan bullish crossover, dimana rata-rata harga jangka pendek "
        explanation += "melampaui rata-rata jangka panjang, tanda klasik untuk entry point. "
        if action == "BELI/TAMBAH POSISI 🟢":
            explanation += "Menambah posisi dapat meningkatkan potensi keuntungan dari tren naik ini "
            explanation += "dengan strategi 'Buy on Dips' - membeli saat ada koreksi kecil dalam tren naik.\n\n"
    
    # Volume analysis
    if technical_data['volume_ratio'] > 1.3:
        explanation += "📊 VOLUME SURGE: Volume perdagangan saat ini tinggi, "
        explanation += "yang menunjukkan adanya minat kuat dari pasar dan likuiditas yang baik. "
        if technical_data['price'] > position_data.get('avg_buy_price', 0) or position_data['current_position'] == 0:
            explanation += "Volume tinggi bersamaan dengan harga naik adalah konfirmasi tren bullish yang kuat, "
            explanation += "sering disebut sebagai 'accumulation phase' dimana investor institusional memasuki pasar. "
            explanation += "Perhatikan 'breakout volume' yang biasanya 50% lebih tinggi dari rata-rata sebagai konfirmasi tren.\n\n"
        else:
            explanation += "Volume tinggi bersamaan dengan harga turun dapat menandakan tekanan jual yang kuat ('distribution phase'), "
            explanation += "dimana pelaku pasar besar sedang melepas saham mereka. Ini bisa menjadi tanda 'capitulation' "
            explanation += "jika volume sangat tinggi dan harga turun drastis.\n\n"
    
    # RSI explanation
    rsi = technical_data['rsi']
    if rsi > 70:
        explanation += "⚠️ OVERBOUGHT CONDITION: RSI di atas 70 menunjukkan saham dalam kondisi jenuh beli, "
        explanation += "yang berarti harga mungkin akan mengalami koreksi dalam waktu dekat. "
        explanation += "Trader sering menggunakan RSI sebagai indikator 'contrarian' - membuat keputusan "
        explanation += "berlawanan dengan arah pasar saat ini ketika mencapai ekstrim. Strategi 'overbought fade' "
        explanation += "melibatkan pengambilan posisi jual (short) ketika RSI menunjukkan jenuh beli.\n\n"
    elif rsi < 30:
        explanation += "💡 OVERSOLD CONDITION: RSI di bawah 30 menunjukkan saham dalam kondisi jenuh jual, "
        explanation += "yang berarti ada potensi pembalikan ke atas (rebound/reversal). "
        explanation += "Kondisi ini sering menjadi sinyal 'dip buying opportunity', terutama jika ditemukan "
        explanation += "pola 'bullish divergence' di mana harga membuat level terendah baru tetapi RSI tidak. "
        explanation += "Pada saham dengan fundamental kuat, ini sering menjadi entry point yang baik.\n\n"
    elif 40 <= rsi <= 60:
        explanation += "⚖️ NEUTRAL MOMENTUM: RSI berada pada zona netral (40-60), "
        explanation += "menunjukkan keseimbangan antara tekanan beli dan jual. Dalam kondisi ini, "
        explanation += "trader biasanya menunggu 'breakout confirmation' dari level support atau resistance.\n\n"
    
    # Final recommendation with professional terminology
    if action == "BELI/TAMBAH POSISI 🟢":
        explanation += "✅ TRADE RECOMMENDATION:\n"
        explanation += "LONG ENTRY SIGNAL - Beli/tambah posisi karena indikator menunjukkan bullish momentum dan potensi kenaikan harga dalam waktu dekat. "
        explanation += f"Target profit dapat ditetapkan pada level resistance terdekat (Rp {format_number(recommendation['target_price'])}), "
        explanation += f"dengan stop loss di level Rp {format_number(recommendation['stop_loss'])} untuk manajemen risiko yang baik. "
        explanation += f"Risk-to-reward ratio {recommendation['risk_reward_ratio']:.2f}:1 disarankan untuk trade ini."
    elif action == "JUAL 🔴":
        explanation += "✅ TRADE RECOMMENDATION:\n"
        explanation += "EXIT POSITION/SHORT ENTRY - Jual untuk mengamankan modal (capital preservation) dari potensi penurunan lebih lanjut "
        explanation += "berdasarkan bearish confirmation. "
        if 'trailing_stop' in recommendation:
            explanation += f"Gunakan trailing stop {recommendation['trailing_stop_pct']:.1f}% (Rp {format_number(recommendation['trailing_stop'])}) "
            explanation += "untuk mengamankan sebagian keuntungan sambil memberi ruang untuk potensi kenaikan lanjutan. "
        explanation += "Untuk trader agresif, sinyal ini juga bisa menjadi entry point untuk posisi short "
        explanation += "dengan target pada level support terdekat dan stop loss yang ketat di atas resistance terakhir."
    else:
        explanation += "✅ TRADE RECOMMENDATION:\n"
        explanation += "NEUTRAL STANCE - Tahan posisi (hold) dan pantau perkembangan chart pattern dan volume, "
        explanation += "karena belum ada sinyal yang cukup kuat untuk mengambil tindakan agresif. "
        explanation += "Perhatikan level support dan resistance terdekat untuk kemungkinan breakout. "
        explanation += "Strategi cash conservation dan wait-and-see direkomendasikan sampai ada konfirmasi tren yang lebih jelas."
    
    return explanation

def main():
    """Main function to run enhanced stock analysis"""
    clear_screen()
    print("\n===== Stock Analysis & Trading Recommendation Tool v1.0 =====")
    print("\nAlat untuk menganalisis saham dan memberikan rekomendasi trading")
    print("berdasarkan analisis teknikal dan riwayat transaksi")
    print("\nLoading...")
    time.sleep(1)
    
    try:
        while True:
            clear_screen()
            print("\n===== Stock Analysis & Trading Recommendation Tool v1.0 =====")
            print("\n1. Analisis Saham Baru")
            print("2. Lihat Riwayat Transaksi")
            print("3. Tambah Transaksi Baru")
            print("4. Kelola Daftar Saham")
            print("5. Keluar")
            
            choice = input("\nPilih menu (1-5): ").strip()
            
            if choice == "1":
                # Get stock symbol from user
                print("\nDaftar saham tersedia:")
                stocks = stock_config.get_stocks_without_suffix()
                for i, stock in enumerate(stocks, 1):
                    print(f"{i}. {stock}")
                    
                try:
                    idx = int(input("\nMasukkan nomor saham (atau 0 untuk input manual): ").strip())
                    if idx == 0:
                        symbol = input("Masukkan kode saham (contoh: BBCA): ").strip().upper()
                        symbol = stock_config.get_stock_with_suffix(symbol)
                    else:
                        if 1 <= idx <= len(stocks):
                            symbol = stock_config.get_stock_with_suffix(stocks[idx-1])
                        else:
                            print("Nomor tidak valid!")
                            time.sleep(2)
                            continue
                except ValueError:
                    print("Input tidak valid!")
                    time.sleep(2)
                    continue
                
                # Run analysis
                try:
                    analyze_stock_with_history(symbol)
                    input("\nTekan Enter untuk kembali ke menu utama...")
                except Exception as e:
                    print(f"Error: {str(e)}")
                    input("\nTekan Enter untuk kembali ke menu utama...")
            
            elif choice == "2":
                # View Transaction History
                clear_screen()
                print("\n===== Riwayat Transaksi =====")
                
                # Initialize transaction history
                th = TransactionHistory()
                
                # Get all transactions
                transactions = th.get_transactions()
                
                if transactions.empty:
                    print("\nBelum ada transaksi tercatat.")
                else:
                    # Group by symbol
                    symbols = transactions['symbol'].unique()
                    
                    for symbol in symbols:
                        symbol_txns = transactions[transactions['symbol'] == symbol]
                        buy_txns = symbol_txns[symbol_txns['transaction_type'] == 'BUY']
                        sell_txns = symbol_txns[symbol_txns['transaction_type'] == 'SELL']
                        
                        print(f"\n{'-'*50}")
                        print(f"SAHAM: {symbol}")
                        print(f"{'-'*50}")
                        
                        # Get position summary
                        pos = th.get_position_summary(symbol)
                        
                        print(f"Posisi Saat Ini : {pos['current_position']} lot")
                        if pos['avg_buy_price'] > 0:
                            print(f"Harga Rata-rata : Rp {format_number(pos['avg_buy_price'])}")
                        
                        print("\nTransaksi:")
                        print(f"{'Tanggal':<12} {'Tipe':<8} {'Harga':<10} {'Lot':<8} {'Total':<15} {'P/L':<15}")
                        print(f"{'-'*65}")
                        
                        for _, txn in symbol_txns.iterrows():
                            txn_date = pd.to_datetime(txn['transaction_date']).strftime('%Y-%m-%d')
                            txn_type = txn['transaction_type']
                            price = txn['price']
                            lots = txn['lot_size']
                            total = txn['total_value']
                            pnl = txn['realized_pnl']
                            
                            pnl_str = f"Rp {format_number(pnl)}" if pnl != 0 else "-"
                            
                            print(f"{txn_date:<12} {txn_type:<8} {format_number(price):<10} {lots:<8} {'Rp ' + format_number(total):<15} {pnl_str:<15}")
                            
                        print(f"{'-'*65}")
                        if pos['total_realized_pnl'] != 0:
                            print(f"Total Realized P/L: Rp {format_number(pos['total_realized_pnl'])}")
                
                input("\nTekan Enter untuk kembali ke menu utama...")
            
            elif choice == "3":
                # Add new transaction
                clear_screen()
                print("\n===== Tambah Transaksi Baru =====")
                
                # Initialize transaction history
                th = TransactionHistory()
                
                # Get stock symbol
                print("\nDaftar saham tersedia:")
                stocks = stock_config.get_stocks_without_suffix()
                for i, stock in enumerate(stocks, 1):
                    print(f"{i}. {stock}")
                    
                try:
                    idx = int(input("\nMasukkan nomor saham (atau 0 untuk input manual): ").strip())
                    if idx == 0:
                        symbol = input("Masukkan kode saham (contoh: BBCA): ").strip().upper()
                        symbol = stock_config.get_stock_with_suffix(symbol)
                    else:
                        if 1 <= idx <= len(stocks):
                            symbol = stock_config.get_stock_with_suffix(stocks[idx-1])
                        else:
                            print("Nomor tidak valid!")
                            time.sleep(2)
                            continue
                except ValueError:
                    print("Input tidak valid!")
                    time.sleep(2)
                    continue
                
                # Get transaction type
                print("\nJenis transaksi:")
                print("1. BELI (BUY)")
                print("2. JUAL (SELL)")
                
                try:
                    tx_type_choice = int(input("\nPilih jenis transaksi (1-2): ").strip())
                    if tx_type_choice == 1:
                        tx_type = "BUY"
                    elif tx_type_choice == 2:
                        tx_type = "SELL"
                    else:
                        print("Pilihan tidak valid!")
                        time.sleep(2)
                        continue
                except ValueError:
                    print("Input tidak valid!")
                    time.sleep(2)
                    continue
                
                # Get date
                print("\nFormat tanggal yang didukung:")
                print("- DDMMYY (contoh: 110625 untuk 11 Jun 2025)")
                print("- DD-MM-YY atau DD/MM/YY (contoh: 11-06-25)")
                print("- YYYY-MM-DD (contoh: 2025-06-11)")
                
                date_str = input("\nMasukkan tanggal transaksi: ").strip()
                
                # Get price
                try:
                    price = float(input("\nMasukkan harga per lembar: Rp ").strip())
                    if price <= 0:
                        print("Harga harus lebih dari 0!")
                        time.sleep(2)
                        continue
                except ValueError:
                    print("Harga tidak valid!")
                    time.sleep(2)
                    continue
                
                # Get lot size
                try:
                    lot_size = int(input("\nMasukkan jumlah lot: ").strip())
                    if lot_size <= 0:
                        print("Jumlah lot harus lebih dari 0!")
                        time.sleep(2)
                        continue
                except ValueError:
                    print("Jumlah lot tidak valid!")
                    time.sleep(2)
                    continue
                
                # Get position summary before adding transaction
                pos_before = th.get_position_summary(symbol)
                
                # Validate sell transaction
                if tx_type == "SELL" and lot_size > pos_before['current_position']:
                    print(f"\nError: Posisi saat ini hanya {pos_before['current_position']} lot!")
                    print("Tidak bisa menjual lebih dari jumlah yang dimiliki.")
                    time.sleep(2)
                    continue
                
                # Add transaction
                try:
                    th.add_transaction(symbol, tx_type, price, lot_size, input_date=date_str)
                    
                    # Get position summary after adding transaction
                    pos_after = th.get_position_summary(symbol)
                    
                    print("\nTransaksi berhasil ditambahkan!")
                    print(f"\nPosisi {symbol} saat ini: {pos_after['current_position']} lot")
                    if pos_after['avg_buy_price'] > 0:
                        print(f"Harga rata-rata: Rp {format_number(pos_after['avg_buy_price'])}")
                    
                    # If it's a sell transaction, show realized P&L
                    if tx_type == "SELL":
                        realized_pnl = pos_after['total_realized_pnl'] - pos_before['total_realized_pnl']
                        print(f"\nRealized P/L dari transaksi ini: Rp {format_number(realized_pnl)}")
                    
                    time.sleep(2)
                except ValueError as e:
                    print(f"\nError: {str(e)}")
                    time.sleep(2)
                except Exception as e:
                    print(f"\nTerjadi kesalahan: {str(e)}")
                    time.sleep(2)
            
            elif choice == "4":
                # Manage stock list
                clear_screen()
                print("\n===== Kelola Daftar Saham =====")
                
                while True:
                    print("\nDaftar saham:")
                    stocks = stock_config.get_stocks_without_suffix()
                    for i, stock in enumerate(stocks, 1):
                        print(f"{i}. {stock}")
                    
                    print("\n1. Tambah saham baru")
                    print("2. Hapus saham")
                    print("3. Kembali ke menu utama")
                    
                    sub_choice = input("\nPilih menu (1-3): ").strip()
                    
                    if sub_choice == "1":
                        symbol = input("Masukkan kode saham (tanpa .JK): ").strip().upper()
                        stock_config.add_stock(symbol)
                        print(f"\nBerhasil menambahkan {symbol}")
                        time.sleep(1)
                    
                    elif sub_choice == "2":
                        try:
                            idx = int(input("Masukkan nomor saham yang akan dihapus: ").strip()) - 1
                            if 0 <= idx < len(stocks):
                                symbol = stocks[idx]
                                stock_config.remove_stock(symbol)
                                print(f"\nBerhasil menghapus {symbol}")
                                time.sleep(1)
                            else:
                                print("\nNomor tidak valid!")
                                time.sleep(1)
                        except ValueError:
                            print("\nInput tidak valid!")
                            time.sleep(1)
                    
                    elif sub_choice == "3":
                        break
                    
                    clear_screen()
                    print("\n===== Kelola Daftar Saham =====")
            
            elif choice == "5":
                # Exit
                print("\nTerima kasih telah menggunakan Stock Analysis & Trading Recommendation Tool!")
                break
                
    except KeyboardInterrupt:
        print("\nProgram dihentikan oleh user")
    except Exception as e:
        print(f"\nTerjadi kesalahan: {str(e)}")
        print("Stack trace:")
        print(traceback.format_exc())

if __name__ == "__main__":
    main()
