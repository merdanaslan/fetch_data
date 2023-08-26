import yfinance as yf
# import pandas as pd
from datetime import datetime

symbol = "^GSPC"  # S&P 500 symbol
start_date = datetime(2023, 8, 23, 0, 0, 0)  # Start of August 23, 2023
end_date = datetime(2023, 8, 24, 0, 0, 0)    # Start of August 24, 2023 (end of the day)
interval = "15m"

# Fetch historical data
data = yf.download(tickers=symbol, start=start_date, end=end_date, interval=interval)

# Save to CSV
data.to_csv('sp500_15m_data_aug23.csv')
