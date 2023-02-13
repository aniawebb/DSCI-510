#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
#!pip3 install yfinance
import yfinance as yf
from bs4 import BeautifulSoup
import pandas as pd
import statistics as stats
from datetime import datetime


# In[2]:


def stock_range_stat(tickers: str, period: str) -> tuple[float, float, float]:
    stock = yf.download(tickers= tickers, period= period)
    stock_df = pd.DataFrame(stock[['High','Low']])
    stock_df['Range']= stock_df['High'] - stock_df['Low']
    min_stock = min(stock_df['Range'])
    max_stock = max(stock_df['Range'])
    mean_stock = stats.mean(stock_df['Range'])
    stat = (min_stock, max_stock, mean_stock)
    
    return stat


# In[3]:


def stock_days_below_today(tickers: str, period: str) -> int:
    stock = yf.download(tickers= tickers, period= period)
    stock_df = pd.DataFrame(stock[['Adj Close']])
    stock_today = stock_df['Adj Close'].iloc[-1]

    num_days = 0
    for row in stock_df['Adj Close']:
        if row < stock_today:
            num_days += 1
        else: 
            continue

    return num_days


# In[4]:


def usc_news_title(url: str) -> list[str]:
    soup = BeautifulSoup(requests.get(url).content, 'html.parser')
    title_list = soup.select('div.preview-content h1')
    title_list

    titles = []
    i = 0
    for title in title_list: 
        titles.append(title_list[i].get_text())
        i += 1

    return titles


# In[5]:


# if __name__ == '__main__':
#     # Test Q1
#     print(stock_range_stat('AAPL', '100d'))
#     print(stock_range_stat('CVX', '100d'))
#     print(stock_range_stat('HON', '100d'))
#     print(stock_range_stat('WMT', '100d'))

#     # Test Q2
#     print(stock_days_below_today('AAPL', '10d'))
#     print(stock_days_below_today('CVX', '20d'))
#     print(stock_days_below_today('HON', '30d'))
#     print(stock_days_below_today('WMT', '40d'))

#     # Test Q3
#     print(usc_news_title("https://news.usc.edu/category/arts/"))
#     print(usc_news_title("https://news.usc.edu/category/athletics/"))
#     print(usc_news_title("https://news.usc.edu/category/business/"))
#     print(usc_news_title("https://news.usc.edu/category/health/"))

