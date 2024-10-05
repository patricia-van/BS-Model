import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

from BSModel import BSModel

# Get adjusted close price for tickers of interest
tickers = ['JPM', 'GS','MS','BLK', 'C']
data = yf.download(tickers, start='2023-01-01', end='2023-12-31')
adj_close_prices = data['Adj Close']

# Plot adjusted close price
# adj_close_prices.plot()
# plt.title('Adjusted Closing Prices of Selected Assets')
# plt.xlabel('Date')
# plt.ylabel('Price (USD)')
# plt.legend(tickers)
# plt.grid(True)
# plt.show()

def calculate_historical_volatility(prices, window=252):
    log_returns = np.log(prices / prices.shift(1))
    return np.std(log_returns) * np.sqrt(window)

historical_volatility = adj_close_prices.apply(calculate_historical_volatility)
# print(historical_volatility)

rf_rate = 0.02
option_price = {'call':{}, 'put':{}}

for ticker in tickers:
    current_price = adj_close_prices[ticker].iloc[-1]
    strike_price = current_price # assume at the money strike price
    volatility = historical_volatility[ticker]
    bsm = BSModel(current_price, strike_price, 1, rf_rate, volatility)
    option_price['call'][ticker] = bsm.get_call_price()
    option_price['put'][ticker] = bsm.get_put_price()

plt.figure()
plt.bar(option_price['call'].keys(), option_price['call'].values())
plt.title('Calculated Option Prices for Selected Assets')
plt.xlabel('Asset')
plt.ylabel('Price (USD)')
plt.show()