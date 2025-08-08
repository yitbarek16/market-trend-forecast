import pandas as pd
import numpy as np

def calculate_volatility_metrics(df, ticker, window=30):
    """Calculate volatility metrics for a single ticker"""
    close_col = f'Close_{ticker}'
    
    # Daily returns
    df[f'Return_{ticker}'] = df[close_col].pct_change()
    df[f'LogReturn_{ticker}'] = np.log(df[close_col]/df[close_col].shift(1))
    
    # Volatility metrics
    df[f'RollingMean_{ticker}'] = df[close_col].rolling(window).mean()
    df[f'RollingStd_{ticker}'] = df[close_col].rolling(window).std()
    df[f'Volatility_{ticker}'] = df[f'LogReturn_{ticker}'].rolling(window).std() * np.sqrt(252)
    
    return df

def clean_and_merge(data_path, output_path, window=30):
    """Enhanced cleaning with volatility pre-calculation"""
    tickers = ['TSLA', 'BND', 'SPY']
    dfs = []
    
    # Load and preprocess each ticker
    for ticker in tickers:
        df = pd.read_csv(f"{data_path}/{ticker}_raw.csv", 
                        parse_dates=['Date'],
                        usecols=['Date', 'Open', 'High', 'Low', 'Close', 'Volume'])
        
        # Standardize column names
        df.columns = ['Date', f'Open_{ticker}', f'High_{ticker}', 
                     f'Low_{ticker}', f'Close_{ticker}', f'Volume_{ticker}']
        dfs.append(df.set_index('Date'))
    
    # Outer merge to preserve all dates
    merged = pd.concat(dfs, axis=1).sort_index()
    
    # Calculate volatility metrics for each ticker
    for ticker in tickers:
        merged = calculate_volatility_metrics(merged, ticker, window)
    
    # Forward fill missing values (markets closed on different days)
    merged = merged.ffill().dropna()
    
    # Save processed data
    merged.to_csv(f"{output_path}/processed_data.csv")
    
    print(f"Processed data saved with {len(merged.columns)} columns")
    return merged

if __name__ == "__main__":
    final_data = clean_and_merge(
        data_path='data/raw',
        output_path='data/processed',
        window=30  # 30-day rolling window
    )