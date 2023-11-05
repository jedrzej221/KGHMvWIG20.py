import yfinance as yf
import matplotlib.pyplot as plt

# Download historical data for KGHM
kghm_data = yf.download('KGH', start='2013-11-05', end='2023-11-05')

# Download historical data for the WIG-20 index (Warsaw Stock Exchange)
wig20_data = yf.download('^WIG20', start='2013-11-05', end='2023-11-05')

# Calculate daily returns for KGHM
kghm_data['KGHM Daily Return'] = kghm_data['Adj Close'].pct_change()

# Calculate daily returns for the WIG-20 index
wig20_data['WIG20 Daily Return'] = wig20_data['Adj Close'].pct_change()

# Calculate the correlation between KGHM and the WIG-20 index daily returns
correlation = kghm_data['KGHM Daily Return'].corr(wig20_data['WIG20 Daily Return'])

# Plot KGHM and WIG-20 price data with improved appearance and display the correlation
plt.figure(figsize=(12, 6))

# Plot KGHM data
plt.plot(kghm_data.index, kghm_data['Adj Close'], label='KGHM', color='blue')

# Plot WIG-20 index data
plt.plot(wig20_data.index, wig20_data['Adj Close'], label='WIG-20', color='green')

plt.xlabel('Date')
plt.ylabel('Price')
plt.title(f'KGHM vs. WIG-20 Index\nCorrelation: {correlation:.2f}')
plt.legend()
plt.grid(True)  # Add a grid for better readability
plt.show()
