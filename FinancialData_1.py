import pandas as pd
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt 
import yfinance as yf

nvda = yf.Ticker("nvda")
stockinfo = nvda.info
hist = nvda.history(period="max")
hist.plot(kind="line", figsize=(12,12), subplots=True)
major_indices = pd.read_html("https://finance.yahoo.com/world-indices")[0]
ticker_list = major_indices [ 'Symbol'].str.replace("^","").str.lower().to_list()
df = yf.download (ticker_list, period="ld", start="2020-01-13", end="2021-03-10")
adj_close = df.dropna (thresh=10, axis=1)['Adj Close']
adj_close.plot(figsize=(12,12));

for key,value in stockinfo.items():
    
    print(key,":", value)

print("sharesOutstanding"+ ": " +  str(nvda.info["sharesOutstanding"]))

print(nvda.splits)
print(nvda.dividends)
print(nvda.major_holders)
print(nvda.institutional_holders)

# df = data frames of all years 

df = nvda.dividends
print(df)

df = nvda.dividends
data = df.resample("YE").sum() 
data = data. reset_index() 
data['Year'] = data['Date'].dt.year 
plt.figure() 
plt.bar(data['Year'], data['Dividends'])
plt.ylabel( 'Dividend Yield ($)')
plt.xlabel( "Year") 
plt.title( "Nvdia Dividend History") 
plt.xlim(2000,2024)
plt.show()
