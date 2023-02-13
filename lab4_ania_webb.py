#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import statistics as stats

def analysis_data(filename):

    csv_df = pd.read_csv(filename, sep= ",", names=['Min_Temp_C', 'Max_Temp_C', 'Percent_Humidity', 'Inches_Rain'])
    number_days = len(csv_df)
    number_rain_days = len(csv_df[(csv_df['Inches_Rain']>0)])
    min_temp = min(csv_df['Min_Temp_C'])
    max_temp = max(csv_df['Max_Temp_C'])
    average_humidity = stats.mean(csv_df['Percent_Humidity'])
    average_rain = stats.mean(csv_df['Inches_Rain'])
    
    return number_days, number_rain_days, min_temp, max_temp, average_humidity, average_rain


# In[26]:


def estimate_weather(filename):
    csv_df = pd.read_csv(filename, sep= ",", names=['Min_Temp_C', 'Max_Temp_C', 'Percent_Humidity', 'Inches_Rain'])
    csv_df["Max_minus_min"] = (csv_df['Max_Temp_C'] - csv_df['Min_Temp_C'])
 
    EstimatedRainy_df = csv_df[(csv_df['Max_minus_min'] > 10) & (csv_df['Percent_Humidity'] > 50)]
    EstimatedRainyCorrect_df= EstimatedRainy_df.loc[~(EstimatedRainy_df['Inches_Rain']==0)] #drop rows where rain is 0 
    
    EstimatedSunny_df = csv_df[~((csv_df['Max_minus_min'] > 10) & (csv_df['Percent_Humidity'] > 50))]
    EstimatedSunnyCorrect_df = EstimatedSunny_df.loc[(EstimatedSunny_df['Inches_Rain']==0)]
    

    estimated_rain = len(EstimatedRainy_df)
    estimated_rain_correct = len(EstimatedRainyCorrect_df)
    
    estimated_sunny = len(EstimatedSunny_df)
    estimated_sunny_correct = len(EstimatedSunnyCorrect_df)
    
    estimations_correct = estimated_rain_correct + estimated_sunny_correct

    return estimated_rain, estimations_correct


# In[36]:


import csv

def wrtie_estimation(filename_in, filename_out):
    csv_df = pd.read_csv(filename_in, sep= ",", names=['Min_Temp_C', 'Max_Temp_C', 'Percent_Humidity', 'Inches_Rain'])
    csv_df["Max_minus_min"] = (csv_df['Max_Temp_C'] - csv_df['Min_Temp_C'])

    mask = (csv_df['Max_minus_min'] > 10) & (csv_df['Percent_Humidity'] > 50)
    csv_df.loc[mask, 'Estimation_Result'] = "rainy"
    csv_df[['Estimation_Result']] = csv_df[['Estimation_Result']].fillna("sunny")
    csv_df = csv_df.drop(columns=['Max_minus_min'])
    
    csv_df.to_csv(filename_out, header= None, index= False) 


# In[ ]:




