#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests


# In[2]:


def find_weather(location: str) -> float:
    url = "https://weatherapi-com.p.rapidapi.com/current.json"

    city_to_query = {"q": location}

    key_and_host = {
        "X-RapidAPI-Key": "bfcc4eca1amsh8641a0a32e874fcp180d9ejsn9239b08669b0",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=key_and_host, params=city_to_query)
    data = response.json()

    return data["current"]["temp_f"]

# # Test Q1
# print(find_weather("Los Angeles"))
# print(find_weather("San Francisco"))
# print(find_weather("New York"))
# print(find_weather("Seattle"))


# In[3]:


def find_food(location: str) -> list[str, str, str]:
    api_key = "kepPgXtjyOsfupUPk1DXsc-bgc9COOH5feseYu7nopwieBrUWMv4KQJzpRA-lfjL335IEIWJ0ccgGkrVuboTOju6bw89C-YPQhdWdXur61hwbYOkUVmdn5CYkfFqY3Yx" 
    headers = {'Authorization': 'Bearer {}'.format(api_key)}

    url = 'https://api.yelp.com/v3/businesses/search'
    url_params = {
        'categories': 'food',
        'location': location, 
        'limit': 3
        }

    response = requests.request('GET', url, headers=headers, params=url_params)
    data = response.json()

    top_three_restaraunts = [data["businesses"][0]["name"], data["businesses"][1]["name"], data["businesses"][2]["name"]]

    return top_three_restaraunts

# # Test Q2
# print(find_food("USC"))
# print(find_food("UCLA"))
# print(find_food("Caltech"))
# print(find_food("UCI"))


# In[4]:


def find_tweet(username: str) -> list[str, str, str]:
    api_key = 'AAAAAAAAAAAAAAAAAAAAANxjjAEAAAAAIl4LZVObpv3pKfWjcu9G3XfPBb0%3DZztLzbGOanXJjzuQeUpDO5gy1HlZ53aOxMtZQ8i60jMM1QWSPX'
    headers = {'Authorization': 'Bearer {}'.format(api_key)}

    url = "https://api.twitter.com/2/tweets/search/recent"
    url_params = {
            'query': "from:" + username
            }

    response = requests.request('GET', url, headers=headers, params=url_params)
    data = response.json()

    three_recent_tweets = [data["data"][0]["text"], data["data"][1]["text"], data["data"][2]["text"]]
    
    return three_recent_tweets

# # Test Q3
# print(find_tweet("USCmoves"))
# print(find_tweet("elonmusk"))
# print(find_tweet("YellowstoneNPS"))

