import pandas as pd
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt 
import yfinance as yf


nvda = yf.Ticker("nvda")
hist = nvda.history(period="max")
## not working nvda.recommendations
## not working nvda.recommendations["To Grade"].value_counts() # How many recommendations
nvda.actions
nvda.calendar
nvda.options
hist.plot(kind="line", figsize=(12,12), subplots=True)
major_indices = pd.read_html("https://finance.yahoo.com/world-indices")[0]
major_indices.head()
ticker_list = major_indices [ 'Symbol'].str.replace("^","").str.lower().to_list()
df = yf.download (ticker_list, period="ld", start="2020-01-13", end="2021-03-10")
adj_close = df.dropna (thresh=10, axis=1)['Adj Close']
adj_close.plot(figsize=(12,12));

