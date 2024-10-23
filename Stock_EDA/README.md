# Stock Analysis Tool README

## Overview
This script is a basic stock analysis tool that leverages the `yfinance` library to download historical stock data and uses `pandas`, `matplotlib`, and `seaborn` to analyze and visualize the data. The script is structured to provide basic summary statistics, calculate daily returns, and plot visualizations like line plots of closing prices, histograms of daily returns, and moving averages.

## Requirements
To run the script, you need to have the following Python libraries installed:
- `yfinance`
- `pandas`
- `matplotlib`
- `seaborn`

You can install these libraries using pip:
```bash
pip install yfinance pandas matplotlib seaborn
```

## Usage
1. **Set the Stock Ticker Symbol**:
   - Modify the variable `stock_ticker` to the stock ticker you want to analyze. By default, it is set to `'TSLA'`.

2. **Run the Script**:
   - The script will download historical stock data for the specified ticker from January 1, 2020, to January 1, 2023.

## Features

### 1. Data Download
The script uses `yfinance` to download historical data for the stock ticker specified:
```python
stock_data = yf.download(stock_ticker, start='2020-01-01', end='2023-01-01')
```

### 2. Data Preview
Displays the first few rows of the dataset:
```python
print(stock_data.head())
```

### 3. Summary Statistics
Generates basic summary statistics for the closing prices of the stock:
```python
print(stock_data['Close'].describe())
```

### 4. Daily Return Calculation
Calculates and displays daily percentage returns:
```python
stock_data['Daily Return'] = stock_data['Close'].pct_change()
print(stock_data['Daily Return'].head())
```

### 5. Visualization
The script provides several visualizations:
- **Line Plot of Closing Prices**:
  - Plots the closing prices over time.
- **Histogram of Daily Returns**:
  - Displays the distribution of daily returns using a histogram with a KDE plot.
- **30-Day Moving Average**:
  - Calculates and plots the 30-day moving average alongside the closing prices.

## Example Outputs

### Line Plot of Closing Prices
This plot shows the stock's closing prices over the specified time period.

### Histogram of Daily Returns
A histogram displaying the distribution of daily percentage returns for the stock, with a KDE plot to visualize the density.

### 30-Day Moving Average
A plot showing the closing prices and the 30-day moving average, helping to visualize the trend over time.

## Customization
- **Changing the Stock Ticker**: Modify the `stock_ticker` variable to analyze a different stock.
- **Date Range**: Adjust the `start` and `end` parameters in the `yf.download()` function to analyze different time periods.

## Notes
- Ensure you have internet access when running the script as it downloads data from Yahoo Finance.
- Make sure the libraries are up-to-date to avoid compatibility issues.

## License
This project is open-source and free to use. Feel free to modify and expand the script as needed for your analysis.

Enjoy analyzing stocks! 📈