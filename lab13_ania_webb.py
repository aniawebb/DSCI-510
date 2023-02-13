#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr


# In[2]:


def pearson_correlation(a: list, b: list) -> float:
    pearson_corr, _ = pearsonr(a, b)
    return pearson_corr


# In[3]:


def num_orders(gender: str) -> float:
    customers = pd.read_csv("data/customers.csv")
    orders = pd.read_csv("data/orders.csv")
    customers_orders = pd.merge(customers, orders, on='customer_id')
    if gender == 'Female':
        num_female = len(customers_orders[customers_orders.gender == 'Female'])
        return num_female
    if gender == 'Male':
        num_male = len(customers_orders[customers_orders.gender == 'Male'])
        return num_male


# In[4]:


def histogram_customer_age(savename: str) -> None:
    customers = pd.read_csv("data/customers.csv")
    age = customers['age']
    plt.hist(age, bins=60, color= 'purple')
    plt.xlabel('Age')
    plt.ylabel('Count')
    plt.title('Histogram of Customer Age', fontweight ="bold")
    plt.savefig(savename)


# In[5]:


# if __name__ == '__main__':
#     # Test Q1
#     print(pearson_correlation([1, 2, 3, 4], [5, 6, 7, 8]))
#     print(pearson_correlation([1, 2, 3, 4], [4, 3, 2, 1]))
#     print(pearson_correlation([1, 2, 1, 2], [3, 4, 2, 1]))
#     print(pearson_correlation([1, 2, 3, 4], [1, 2, 1, 2]))

#     # Test Q2
#     print(num_orders("Male"))
#     print(num_orders("Female"))

#     # Test Q3
#     savename = os.path.basename(__file__).replace('.py', '_q3.pdf')
#     histogram_customer_age(savename)

