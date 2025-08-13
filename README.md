# Market Trend Forecast: Time Series Forecasting & Portfolio Optimization

## Overview
**Guide Me in Finance (GMF) Investments** utilizes advanced time series modeling and modern portfolio theory to optimize investment strategies. This project analyzes and forecasts three key assets:
- **TSLA**: High-growth technology stock
- **SPY**: S&P 500 ETF (U.S. equity benchmark)
- **BND**: Vanguard Total Bond Market ETF (low-volatility, income asset)

The workflow covers **data acquisition, exploratory analysis, time series modeling, forecasting, portfolio optimization, and backtesting**.

---

## Project Structure

```
market-trend-forecast/
├── data/
│   ├── raw/             # Original YFinance downloads
│   └── processed/       # Cleaned, merged datasets with features
├── notebooks/
│   ├── 1_EDA.ipynb     # Exploratory Data Analysis
│   ├── 2_Develop_forcasting_models.ipynb # LSTM Model Training
│   ├── 3_Future_market_trends.ipynb # 12-Month Forecast
│   ├── 4_Portfolio_optimization.ipynb # MPT Optimization
│   └── 5_Strategy_backtesting.ipynb # Strategy Simulation
|
├── data_fetching.py    # Historical price data fetch
├── data_cleaning.py    # Preprocessing & feature engineering
│           
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── outputs/                # Charts, forecasts, and CSVs
    ├── EDA/ 
    ├── Forcasting models/
    ├── Future market trends/
    ├── Portfolio optimization/
    └── Strategy backtesting/

```

---

## Methodology & Key Results

### 1. Data Acquisition & EDA
- Downloaded daily OHLCV data for TSLA, SPY, BND via `yfinance`
- Engineered features: daily/log returns, rolling mean/std, annualized volatility
- Statistical and correlation analysis

**Summary (2015–2025):**

| Metric         | TSLA    | SPY    | BND   |
|----------------|---------|--------|-------|
| Annual Return  | 30.42%  | 13.00% | 1.68% |
| Volatility     | 61.98%  | 17.70% | 5.22% |
| Sharpe Ratio   | 0.49    | 0.73   | 0.32  |
| Max Drawdown   | -138.5% | -38.6% | -21.0% |

---

### 2. LSTM Model Training
- Built and trained LSTM model for TSLA price prediction
- Used sliding-window sequences and `MinMaxScaler`
- Saved model weights and scalers for reproducibility

---

### 3. 12-Month Price Forecast
- Generated 252 trading-day forecast for TSLA
- Computed 95% confidence intervals from residuals
- Visualized historical vs. forecast prices

---

### 4. Portfolio Optimization (Modern Portfolio Theory)
- TSLA expected return: LSTM forecast
- SPY & BND: historical annualized returns
- Covariance matrix from daily returns
- Efficient Frontier plotted; Max Sharpe and Min Volatility portfolios identified
- TSLA allocation capped at 10% for risk management

**Recommended Portfolio (Max Sharpe, TSLA ≤ 10%)**

| Asset | Allocation |
|-------|------------|
| TSLA  | 10%        |
| SPY   | 60%        |
| BND   | 30%        |

- **Expected Annual Return:** 10.36%
- **Annual Volatility:** 15.06%
- **Sharpe Ratio:** 0.69

---

### 5. Strategy Backtesting
- Backtested Aug 2024 – Jul 2025
- Compared:
  - **Hold Strategy:** Fixed weights
  - **Monthly Rebalance:** Monthly portfolio adjustment
  - **Benchmark:** 60% SPY / 40% BND

| Strategy              | Return   | Volatility | Sharpe |
|-----------------------|----------|------------|--------|
| Hold                  | 18.25%   | 18.35%     | 0.99   |
| Monthly Rebalance     | 17.72%   | 18.35%     | 0.97   |
| Benchmark             | 12.49%   | 13.11%     | 0.95   |

---

## Installation & Usage

```bash
git clone <repo_url>
cd market-trend-forecast
pip install -r requirements.txt
```

**Run Data Pipeline:**
```bash
python src/data_fetching.py
python src/data_cleaning.py
```

**Modeling & Analysis:**
- Open and run notebooks in `notebooks/` for modeling, forecasting, optimization, and backtesting.
- Results and charts are saved in `outputs/`.

---

## Key Learnings

- Integrating machine learning (LSTM) with finance theory (MPT) enables robust, data-driven portfolio strategies.
- Limiting high-volatility assets (TSLA) improves risk-adjusted returns.
- Regular rebalancing can reduce risk with minimal impact on returns.
- Backtesting validates forecast-driven strategies and highlights uncertainty.

---

## Outputs & Visualizations

*(See `outputs/` for charts and CSV results)*

---

**For questions or contributions, please open an issue or submit a pull request.**