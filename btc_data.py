import ccxt
import pandas as pd
import mplfinance as mpf
from datetime import datetime, timedelta

# Initialize the exchange
exchange = ccxt.binance()

# Symbol for Bitcoin
symbol = 'BTC/USDT'

# Set the start and end times for January 1, 2023
start_time = datetime(2023, 1, 1, 0, 0, 0)
end_time = datetime(2023, 8, 25, 23, 59, 59)

# Define the timeframe and chunk size
timeframe = '4h'
chunk_size = 1000  # Number of data points per request

# Fetch historical data in chunks
all_ohlcv = []
current_time = start_time
while current_time < end_time:
    since = int(current_time.timestamp() * 1000)
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe, since=since, limit=chunk_size)
    all_ohlcv.extend(ohlcv)
    current_time = datetime.fromtimestamp(ohlcv[-1][0] / 1000) + timedelta(hours=4)  # change hour for timeframe

# Filter data within the desired time range
filtered_ohlcv = [data for data in all_ohlcv if start_time.timestamp() * 1000 <= data[0] < end_time.timestamp() * 1000]

# Convert to DataFrame
df = pd.DataFrame(filtered_ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')  # Convert timestamp to datetime
df.set_index('timestamp', inplace=True)  # Set timestamp as the index

# Save to CSV
csv_filename = 'btc_4h_data_jan_to_aug.csv'
df.to_csv(csv_filename)
print(f"Data saved to {csv_filename}")

# Plot using mplfinance
mpf.plot(df, type='candle', style='yahoo', title='Bitcoin 4-hour OHLCV Data', ylabel='Price')

# Show the plot
mpf.show()
