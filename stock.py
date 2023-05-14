from pandas_datareader import data as pdr
from datetime import date
import matplotlib.pyplot as plt
import yfinance as yf

yf.pdr_override()
import pandas as pd

# Tickers list
# We can add and delete any ticker from the list to get desired ticker live data
ticker_list = ["TSLA", "AAPL", "GOOG", "META", "NVDA"]
today = date.today()
# We can get data by our choice by giving days bracket
start_date = "2022-01-01"
# end_date="2023-05-12"
files = []


def getData(ticker):
    print(ticker)
    data = pdr.get_data_yahoo(ticker, start=start_date, end=today)
    dataname = ticker + "_" + str(today)
    files.append(dataname)
    SaveData(data, dataname)


# Create a data folder in your current dir.
def SaveData(df, filename):
    df.to_csv("./data/" + filename + ".csv")


# This loop will iterate over ticker list, will pass one ticker to get data, and save that data as file.
for tik in ticker_list:
    getData(tik)
for i in range(0, 4):
    df1 = pd.read_csv("./data/" + str(files[i]) + ".csv")
    print(df1.head())

# Plot graph to show the close price of a stock
ccb_data = pdr.get_data_yahoo("AAPL", start=start_date, end=today)
ccb_data.to_pickle("AAPL.pkl")
stock_cls = pd.read_pickle("AAPL.pkl")
stock_cls["Adj Close"]
stock_cls["Adj Close"].plot(grid=True)
plt.show()

# Plot graph to show daily price percentage changes as normal distribution
# calculate the daily percentage change
daily_pct_change = stock_cls.pct_change()

# Plot the distributions
daily_pct_change.hist(bins=50, figsize=(12, 8))

# Show the resulting plot
plt.show()
