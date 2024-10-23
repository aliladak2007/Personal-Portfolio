import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Define the stock ticker symbol as a variable
stock_ticker = 'TSLA'  # Change this to the stock ticker you want to analyze

# Step 2: Download historical stock data
stock_data = yf.download(stock_ticker, start='2020-01-01', end='2023-01-01')

# Display the first few rows of the data
print(f"First few rows of the data for {stock_ticker}:")
print(stock_data.head())

# Step 3: Basic analysis - Summary statistics
print(f"\nSummary statistics for the closing price of {stock_ticker}:")
print(stock_data['Close'].describe())

# Step 4: Calculate daily returns
stock_data['Daily Return'] = stock_data['Close'].pct_change()

# Display the first few daily returns
print(f"\nFirst few daily returns for {stock_ticker}:")
print(stock_data['Daily Return'].head())

# Step 5: Visualization - Line plot of closing prices
plt.figure(figsize=(14, 7))
plt.plot(stock_data['Close'], label=f'{stock_ticker} Closing Price')
plt.title(f'{stock_ticker} Closing Prices Over Time')
plt.xlabel('Date')
plt.ylabel('Closing Price (USD)')
plt.legend()
plt.show()

# Step 6: Visualization - Histogram of daily returns
plt.figure(figsize=(10, 6))
sns.histplot(stock_data['Daily Return'].dropna(), bins=100, kde=True)
plt.title(f'Distribution of Daily Returns for {stock_ticker}')
plt.xlabel('Daily Return')
plt.ylabel('Frequency')
plt.show()

# Step 7: Calculate and plot the 30-day moving average
stock_data['30 Day MA'] = stock_data['Close'].rolling(window=30).mean()

plt.figure(figsize=(14, 7))
plt.plot(stock_data['Close'], label=f'{stock_ticker} Closing Price')
plt.plot(stock_data['30 Day MA'], label='30 Day Moving Average', color='orange')
plt.title(f'{stock_ticker} Closing Prices with 30 Day Moving Average')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.show()
