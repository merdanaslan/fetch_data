import ccxt
import pandas as pd
import mplfinance as mpf
from datetime import datetime

# Initialize the exchange
exchange = ccxt.binance()

# Symbol for Bitcoin
symbol = 'BTC/USDT'

# Set the start and end times for August 20, 2023
start_time = datetime(2023, 8, 20, 0, 0, 0)
end_time = datetime(2023, 8, 20, 23, 59, 59)  # Set the end of the day

# Fetch historical data
timeframe = '15m'
ohlcv = exchange.fetch_ohlcv(symbol, timeframe, since=int(start_time.timestamp() * 1000))

# Filter data within the desired time range
filtered_ohlcv = [data for data in ohlcv if data[0] <= int(end_time.timestamp() * 1000)]

# Convert to DataFrame
df = pd.DataFrame(filtered_ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')  # Convert timestamp to datetime
df.set_index('timestamp', inplace=True)  # Set timestamp as the index

# Save to CSV
csv_filename = 'btc_15min_data_aug20.csv'
df.to_csv(csv_filename, index=False)
print(f"Data saved to {csv_filename}")

# Plot using mplfinance
mpf.plot(df, type='candle', style='yahoo', title='Bitcoin 15-minute OHLCV Data', ylabel='Price')

# Show the plot
mpf.show()
