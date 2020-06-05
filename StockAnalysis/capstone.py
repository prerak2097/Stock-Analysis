import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web
import datetime
import yahoo_finance as yf
from pandas.plotting import scatter_matrix



#asks users to input the tickers of the three stocks they would like to analyze using the program
stock1 = input("what is the ticker of the first stock you would like to analyze: ")
stock2 = input("what is the ticker of the second stock you would like to analyze: ")
stock3 = input("what is the ticker of the third stock you would like to analyze: ")
print("first: {}, second: {}, third: {}" .format(stock1,stock2,stock3))
print("Now you will be asked to enter the date range of this analysis, please enter reasonable ranges with out commas or special characters in between other than spaces")
date1year, date1month, date1day = input("Enter the year, month, and day of the starting date of the analysis(ex. 2018 5 25): ").split() 
daye2year, date2month, date2day = input("Enter the year, month, and day of the ending date of the analysis(ex. 2019 12 25): ").split()
starts = datetime.datetime(int(date1year),int(date1month),int(date1day))
ends = datetime.datetime(int(daye2year),int(date2month),int(date2day))
first = web.DataReader(stock1, 'yahoo',starts,ends)
second = web.DataReader(stock2, 'yahoo',starts,ends)
third = web.DataReader(stock3, 'yahoo',starts,ends)

# up till now our code operates as it should be
fig = plt.figure(figsize=(16,8))
first['Open'].plot(label= stock1, title='Opening Prices')
second['Open'].plot(label= stock2)
third['Open'].plot(label= stock3)
plt.legend()

#fig10 = plt.figure()
first['MA50'] = first['Open'].rolling(50).mean()
first['MA175'] = first['Open'].rolling(175).mean()
first[['Open','MA50','MA175']].plot(label=stock1,figsize=(16,8), title='Moving Avg of ' + stock1)
plt.legend()

#fig11 = plt.figure()
second['MA50'] = second['Open'].rolling(50).mean()
second['MA175'] = second['Open'].rolling(175).mean()
second[['Open','MA50','MA175']].plot(label=stock2,figsize=(16,8),title='Moving Avg of ' + stock2)
plt.legend()

#fig12 = plt.figure()
third['MA50'] = third['Open'].rolling(50).mean()
third['MA175'] = third['Open'].rolling(175).mean()
third[['Open','MA50','MA175']].plot(label=stock3,figsize=(16,8),title='Moving Avg of ' + stock3)
plt.legend()

fig2= plt.figure(figsize=(16,8))
first['Volume'].plot(label= stock1, title='Volume Traded')
second['Volume'].plot(label= stock2)
third['Volume'].plot(label= stock3)
plt.legend()

fig3= plt.figure(figsize=(16,8))
first['Total Traded'] = first['Open']*first['Volume']
second['Total Traded'] = second['Open']*second['Volume']
third['Total Traded'] = third['Open']*third['Volume']
first['Total Traded'].plot(label= stock1, title='Total Traded')
second['Total Traded'].plot(label= stock2)
third['Total Traded'].plot(label= stock3)
plt.legend()

cardf= pd.concat([first['Open'],second['Open'],third['Open']], axis=1)
cardf.columns= [stock1+' Open', stock2+' Open', stock3+ ' Open'] 
scatter_matrix(cardf,figsize=(8,8))
plt.suptitle('Analyze Correlation b/w Stocks')

first['Returns']= first['Close'].pct_change(1)
second['Returns']= second['Close'].pct_change(1)
third['Returns']= third['Close'].pct_change(1)

first['Returns'].hist(bins=100, label=stock1,figsize=(10,8))
second['Returns'].hist(bins=100, label=stock2,figsize=(10,8))
third['Returns'].hist(bins=100, label=stock3,figsize=(10,8))
plt.suptitle("View of Volatility")

fig5=plt.figure()
first['Cumulative Return'] = (1 + first['Returns']).cumprod()
second['Cumulative Return'] = (1 + second['Returns']).cumprod()
third['Cumulative Return'] = (1 + third['Returns']).cumprod()
first['Cumulative Return'].plot(label=stock1 ,figsize=(16,8),title='Cumulative Return')
second['Cumulative Return'].plot(label=stock2)
third['Cumulative Return'].plot(label=stock3)

plt.legend()
plt.show()
#try to finish capstone by tomorrow and clean up my resume and talk to Sunil







