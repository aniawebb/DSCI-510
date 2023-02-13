#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import necessary libraries
from bs4 import BeautifulSoup
import requests
from urllib import request
import nltk
nltk.download('punkt')
import string
import pandas as pd


# In[2]:


def get_frequency(url, word_to_search):
    file_content = request.urlopen(str(url)).read()
    beautiful_soup = BeautifulSoup(file_content, features="lxml").get_text()
    words = nltk.word_tokenize(beautiful_soup)
    
    word_dict = dict()
    
    for word in words:
        word = word.translate(str.maketrans('', '', string.punctuation))
        word = word.lower()
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    word_to_search = word_to_search.translate(str.maketrans('', '', string.punctuation))

    for key, value in word_dict.items():
        if str(word_to_search.lower()) == key:
            return value 


# In[3]:


def get_contents_from_web(url, outcome):
    website_url = requests.get(url)
    html_string = website_url.text
    soup = BeautifulSoup(html_string, 'html.parser')

    table = soup.find_all('table',{'class':"wikitable"})
    df1 = pd.read_html(str(table[0]))
    df2 = pd.read_html(str(table[1]))
    df1 = pd.DataFrame(df1[0])
    df2 = pd.DataFrame(df2[0])
    
    success_dict = dict()
    
    ####
    
    df1 = df1.droplevel(0, axis=1).droplevel(1, axis=1) #removing multi-index
    df1 = df1.drop(['Date and time (UTC)', 'Unnamed: 1_level_1', 'Payload(⚀ = CubeSat)', 'Orbit', 'Function', 'Decay (UTC)'], axis=1)

    not_successful1 = df1[~(df1['Outcome'] == outcome)].index #get index where where dataframe outcome is not successful

    df1.drop(not_successful1, inplace=True)

    for index, row in df1.iterrows():
        if row['Operator'] in success_dict:
                success_dict[row['Operator']] += 1
        else:
            success_dict[row['Operator']] = 1
            
    ####
    
    df2 = df2.droplevel(0, axis=1).droplevel(1, axis=1) #removing multi-index
    df2 = df2.drop(['Date and time (UTC)', 'Unnamed: 1_level_1', 'Payload(⚀ = CubeSat)', 'Orbit', 'Function', 'Decay (UTC)'], axis=1)
    
    not_successful2 = df2[~(df2['Outcome'] == outcome)].index #get index where where dataframe outcome is not successful

    df2.drop(not_successful2, inplace=True)

    for index, row in df2.iterrows():
        if row['Operator'] in success_dict:
                success_dict[row['Operator']] += 1
        else:
            success_dict[row['Operator']] = 1
    
    ####              
            
    return success_dict                      

