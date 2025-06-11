"""
Main GUI for Enhanced Stock Analyzer with Transaction History Tracking
"""
from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QComboBox, QTableWidget,
    QTableWidgetItem, QTabWidget, QLineEdit, QMessageBox, QTextEdit, QHeaderView
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QMovie
from src.data.stock_data import StockData
from src.analysis.technical import TechnicalAnalysis
from src.analysis.prediction import StockPredictor
from src.visualization.charts import StockVisualizer
from src.utils.config import stock_config
from src.data.transaction_history import TransactionHistory
from src.analysis.trade_advisor import TradeAdvisor
import pandas as pd
import os
import datetime

class MainAppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stock Analysis & Trading Recommendation Tool")
        self.setMinimumSize(1200, 800)
        self.transaction_history = TransactionHistory()
        self.init_ui()

    def init_ui(self):
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)

        header = QLabel("Stock Analysis & Trading Recommendation Tool v1.1.0")
        header.setFont(QFont("Arial", 16, QFont.Bold))
        header.setAlignment(Qt.AlignCenter)
        layout.addWidget(header)

        self.tabs = QTabWidget()
        layout.addWidget(self.tabs)

        self.analysis_tab = self.create_analysis_tab()
        self.tabs.addTab(self.analysis_tab, "Analisis Saham")

        self.history_tab = self.create_history_tab()
        self.tabs.addTab(self.history_tab, "Riwayat Transaksi")

        self.add_tab = self.create_add_transaction_tab()
        self.tabs.addTab(self.add_tab, "Tambah Transaksi")

        self.manage_tab = self.create_manage_stock_tab()
        self.tabs.addTab(self.manage_tab, "Kelola Saham")

        self.about_tab = self.create_about_tab()
        self.tabs.addTab(self.about_tab, "Tentang")

    def create_analysis_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        stock_selection = QHBoxLayout()
        stock_label = QLabel("Pilih Saham:")
        self.stock_combo = QComboBox()
        self.stock_combo.addItems(stock_config.get_stocks_without_suffix())
        stock_selection.addWidget(stock_label)
        stock_selection.addWidget(self.stock_combo)
        stock_selection.addStretch()
        layout.addLayout(stock_selection)
        self.analyze_btn = QPushButton("Analisis")
        self.analyze_btn.clicked.connect(self.run_analysis)
        layout.addWidget(self.analyze_btn)
        # Spinner
        self.spinner_label = QLabel()
        self.spinner_label.setAlignment(Qt.AlignCenter)
        self.spinner_movie = QMovie(os.path.join(os.path.dirname(__file__), "spinner.gif"))
        self.spinner_label.setMovie(self.spinner_movie)
        self.spinner_label.hide()
        layout.addWidget(self.spinner_label)
        self.analysis_result = QTextEdit()
        self.analysis_result.setReadOnly(True)
        layout.addWidget(self.analysis_result)
        # Chart label
        self.chart_label = QLabel()
        self.chart_label.setAlignment(Qt.AlignCenter)
        self.chart_label.hide()
        layout.addWidget(self.chart_label)
        return tab

    def run_analysis(self):
        import io
        import sys
        from PyQt5.QtGui import QPixmap
        symbol = self.stock_combo.currentText()
        if not symbol:
            QMessageBox.warning(self, "Input Error", "Pilih saham terlebih dahulu.")
            return
        symbol = stock_config.get_stock_with_suffix(symbol)
        self.analysis_result.hide()
        self.chart_label.hide()
        self.spinner_label.show()
        self.spinner_movie.start()
        self.analyze_btn.setEnabled(False)
        self.repaint()  # Force UI update
        old_stdout = sys.stdout
        try:
            from main import analyze_stock_with_history
            sys.stdout = mystdout = io.StringIO()
            analyze_stock_with_history(symbol)
            sys.stdout = old_stdout
            output = mystdout.getvalue()
            self.spinner_movie.stop()
            self.spinner_label.hide()
            self.analysis_result.setPlainText(output)
            self.analysis_result.show()
            # Show chart
            symbol_filename = symbol.replace('.JK', '') + '.JK'
            chart_path = os.path.join('analysis_results', f'{symbol_filename}_charts', 'candlestick.png')
            if os.path.exists(chart_path):
                pixmap = QPixmap(chart_path)
                self.chart_label.setPixmap(pixmap.scaledToWidth(600, Qt.SmoothTransformation))
                self.chart_label.show()
            else:
                self.chart_label.hide()
        except Exception as e:
            sys.stdout = old_stdout
            self.spinner_movie.stop()
            self.spinner_label.hide()
            self.analysis_result.setPlainText(f"Error: {str(e)}")
            self.analysis_result.show()
            self.chart_label.hide()
        self.analyze_btn.setEnabled(True)

    def create_history_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        self.history_table = QTableWidget()
        self.history_table.setColumnCount(8)
        self.history_table.setHorizontalHeaderLabels([
            "Tanggal", "Saham", "Tipe", "Harga", "Lot", "Total", "P/L", "Status"
        ])
        self.history_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(self.history_table)
        refresh_btn = QPushButton("Refresh")
        refresh_btn.clicked.connect(self.load_history)
        layout.addWidget(refresh_btn)
        self.load_history()
        return tab

    def load_history(self):
        tx = self.transaction_history.get_transactions()
        self.history_table.setRowCount(len(tx))
        for i, (_, row) in enumerate(tx.iterrows()):
            self.history_table.setItem(i, 0, QTableWidgetItem(str(row['transaction_date'])))
            self.history_table.setItem(i, 1, QTableWidgetItem(str(row['symbol'])))
            self.history_table.setItem(i, 2, QTableWidgetItem(str(row['transaction_type'])))
            self.history_table.setItem(i, 3, QTableWidgetItem(f"{row['price']:,.2f}"))
            self.history_table.setItem(i, 4, QTableWidgetItem(str(row['lot_size'])))
            self.history_table.setItem(i, 5, QTableWidgetItem(f"{row['total_value']:,.2f}"))
            self.history_table.setItem(i, 6, QTableWidgetItem(f"{row['realized_pnl']:,.2f}"))
            self.history_table.setItem(i, 7, QTableWidgetItem(str(row.get('status', 'EXECUTED'))))

    def create_add_transaction_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        form = QHBoxLayout()
        self.add_stock_input = QLineEdit()
        self.add_stock_input.setPlaceholderText("Stock Symbol")
        form.addWidget(self.add_stock_input)
        self.add_type_combo = QComboBox()
        self.add_type_combo.addItems(["BUY", "SELL"])
        form.addWidget(self.add_type_combo)
        self.add_price_input = QLineEdit()
        self.add_price_input.setPlaceholderText("Price")
        form.addWidget(self.add_price_input)
        self.add_lot_input = QLineEdit()
        self.add_lot_input.setPlaceholderText("Lot Size")
        form.addWidget(self.add_lot_input)
        add_btn = QPushButton("Tambah Transaksi")
        add_btn.clicked.connect(self.add_transaction)
        form.addWidget(add_btn)
        layout.addLayout(form)
        self.add_tx_status = QLabel("")
        layout.addWidget(self.add_tx_status)
        return tab

    def add_transaction(self):
        symbol = self.add_stock_input.text().strip().upper()
        if not symbol:
            self.add_tx_status.setText("Stock symbol required.")
            return
        if not symbol.endswith('.JK'):
            symbol += '.JK'
        try:
            price = float(self.add_price_input.text())
            lot_size = int(self.add_lot_input.text())
            tx_type = self.add_type_combo.currentText()
            self.transaction_history.add_transaction(symbol, tx_type, price, lot_size)
            self.add_tx_status.setText("Transaksi berhasil ditambahkan!")
            self.load_history()
        except Exception as e:
            self.add_tx_status.setText(f"Error: {str(e)}")

    def create_manage_stock_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        self.stock_list_label = QLabel(self.get_stock_list_text())
        layout.addWidget(self.stock_list_label)
        form = QHBoxLayout()
        self.manage_stock_input = QLineEdit()
        self.manage_stock_input.setPlaceholderText("Kode Saham")
        form.addWidget(self.manage_stock_input)
        add_btn = QPushButton("Tambah")
        add_btn.clicked.connect(self.add_stock)
        form.addWidget(add_btn)
        del_btn = QPushButton("Hapus")
        del_btn.clicked.connect(self.remove_stock)
        form.addWidget(del_btn)
        layout.addLayout(form)
        return tab

    def get_stock_list_text(self):
        stocks = stock_config.get_stocks_without_suffix()
        return "Daftar Saham: " + ", ".join(stocks)

    def add_stock(self):
        symbol = self.manage_stock_input.text().strip().upper()
        if symbol:
            stock_config.add_stock(symbol)
            self.stock_list_label.setText(self.get_stock_list_text())
            self.stock_combo.clear()
            self.stock_combo.addItems(stock_config.get_stocks_without_suffix())

    def remove_stock(self):
        symbol = self.manage_stock_input.text().strip().upper()
        if symbol:
            stock_config.remove_stock(symbol)
            self.stock_list_label.setText(self.get_stock_list_text())
            self.stock_combo.clear()
            self.stock_combo.addItems(stock_config.get_stocks_without_suffix())

    def create_about_tab(self):
        from src.utils.developer_info import DeveloperInfo
        tab = QWidget()
        layout = QVBoxLayout(tab)
        info = DeveloperInfo()
        about_text = info.generate_about_text()
        # Social media
        social = info.get_social_media()
        if social:
            about_text += "\nMedia Sosial:\n"
            for k, v in social.items():
                about_text += f"- {k.title()}: {v}\n"
        # Funding
        funding = info.get_funding_links()
        if funding:
            about_text += "\nDukungan/Donasi:\n"
            for k, v in funding.items():
                about_text += f"- {k.title()}: {v}\n"
        # Contributors
        contributors = info.get_contributors()
        if contributors:
            about_text += "\nKontributor:\n"
            for c in contributors:
                about_text += f"- {c['name']} ({c['role']}) <{c['email']}>\n"
        about = QTextEdit()
        about.setReadOnly(True)
        about.setPlainText(about_text)
        layout.addWidget(about)
        return tab
