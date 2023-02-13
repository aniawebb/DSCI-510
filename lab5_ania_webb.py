#!/usr/bin/env python
# coding: utf-8

# In[223]:


import pandas as pd
import statistics as stats

def analysis_ecommerce(filename):
    csv_df = pd.read_csv(filename, sep= ",", header= 0)
    csv_df['Description'] = csv_df['Description'].replace(['SMALL POPCORN HOLDER'],'POPCORN HOLDER')
    #1
    unique_stock = csv_df.StockCode.nunique(dropna=False) #Number of unique items according to column StockCode
    #2
    unique_customers = csv_df.CustomerID.nunique(dropna=False) #Number of unique customers according to column CustomerID
    #3
    unique_countries = csv_df.Country.nunique(dropna=False) #Number of unique countries according to column Country
    #4
    invoice_stock_dictionary = csv_df.groupby('InvoiceNo')['StockCode'].agg(set).to_dict()
    
    count_dict_stock = dict()
    for invoice_code, stock_code in invoice_stock_dictionary.items():
        count_dict_stock[invoice_code]= len([item for item in stock_code if item])
    
    stock_total_count = 0 
    for stock_count in count_dict_stock.values():
        stock_total_count += stock_count
        stock_per_invoice_mean = stock_total_count/len(count_dict_stock) #Average number of unique items per invoice. 
    #5    
    total_quantity = csv_df.Quantity.sum()
    quantity_per_invoice_mean = total_quantity/csv_df.InvoiceNo.nunique(dropna=False) #Average number of items per invoice
    #6
    csv_df["Trascation"] = (csv_df['UnitPrice'] * csv_df['Quantity'])
    total_transcations = csv_df.Trascation.sum()
    transaction_per_invoice_mean = total_transcations/csv_df.InvoiceNo.nunique(dropna=False) #Average transaction amount per invoice
    #7
    item_quantity_dictionary = csv_df.groupby('StockCode')['Quantity'].sum().to_dict() #Calculate the total number of purchases for each item
    
    sorted_quantities = sorted(item_quantity_dictionary.values(), reverse= True)
    sorted_item_quantity_dictionary = dict()

    for item in sorted_quantities: 
        for description in item_quantity_dictionary.keys():
            if item_quantity_dictionary[description] == item:
                sorted_item_quantity_dictionary[description] = item_quantity_dictionary[description]

    sorted_item_quantity_list = list(sorted_item_quantity_dictionary.items())           
    top_three_purchased = sorted_item_quantity_list[0:3] #top 3 purchased items

    item1= csv_df.loc[csv_df['StockCode'] == top_three_purchased[0][0]]
    description1 = (pd.unique(item1['Description']))
    description1 = ' '.join(description1)

    item2= csv_df.loc[csv_df['StockCode'] == top_three_purchased[1][0]]
    description2 = (pd.unique(item2['Description']))
    description2 = ''.join(description2)

    item3= csv_df.loc[csv_df['StockCode'] == top_three_purchased[2][0]]
    description3 = (pd.unique(item3['Description']))
    description3 = ''.join(description3)
    
    tuple1 = (top_three_purchased[0][1], top_three_purchased[0][0], description1)
    tuple2 = (top_three_purchased[1][1], top_three_purchased[1][0], description2)
    tuple3 = (top_three_purchased[2][1], top_three_purchased[2][0], description3)
    
    top_three_list = [tuple1, tuple2, tuple3]
    
    return unique_stock, unique_customers, unique_countries, stock_per_invoice_mean, quantity_per_invoice_mean, transaction_per_invoice_mean, top_three_list
    


# In[ ]:




