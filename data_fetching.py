import yfinance as yf
import pandas as pd
from datetime import datetime

def fetch_data(tickers, start_date, end_date, save_path):
    """Fetch data from Yahoo Finance and save raw files"""
    for ticker in tickers:
        df = yf.download(ticker, start=start_date, end=end_date)
        df.to_csv(f"{save_path}/{ticker}_raw.csv")
    print("Raw data saved successfully")

if __name__ == "__main__":
    tickers = ['TSLA', 'BND', 'SPY']
    fetch_data(tickers, '2015-07-01', '2025-07-31', 'data/raw')