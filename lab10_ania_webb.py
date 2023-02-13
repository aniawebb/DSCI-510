#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import json
from bs4 import BeautifulSoup
from opencage.geocoder import OpenCageGeocode


# In[2]:


class SpaceLaunch:
    def __init__(self, payload = "", operator = "", orbit = "", function = "", decay = "", outcome = "") -> None:
        self.payload = payload
        self.operator = operator
        self.orbit = orbit 
        self.function = function
        self.decay = decay 
        self.outcome = outcome    


# In[3]:


class Coordinate:
    def __init__(self, city = "", latitude = 0, longitude = 0) -> None:
        self.city = city
        self.latitude = latitude
        self.longitude = longitude


# In[19]:


def get_contents_from_web(url):
    url_contents = requests.get(url).content #get contents from url using requests.get
    soup = BeautifulSoup(url_contents, 'html.parser') #create BeautifulSoup(content,'html.parser') , choose html parser
    listofinstances = []
    
    for table in soup.find_all('table', {'class': 'wikitable'}):
        tr_tags = table.find_all('tr') #find all the <tr> tags
        
        for tr_tag in tr_tags:
            td_tag = tr_tag.find_all('td') #for each <tr>, find all the <td> tags
            
            if td_tag == "":
                continue
            elif td_tag == 0:
                continue
            elif len(td_tag) < 6:
                continue   
                
            elif len(td_tag) == 6: #within all <td> tags, check if the number of <td> tags we get are 6 
                instance = SpaceLaunch(payload = td_tag[-6].text, 
                                       operator = td_tag[-5].text, 
                                       orbit = td_tag[-4].text, 
                                       function = td_tag[-3].text, 
                                       decay= td_tag[-2].text, 
                                       outcome = td_tag[-1].text) #create an instance of SpaceLaunch class with respective values
                listofinstances += [instance]
                
    return listofinstances


# In[5]:


def obj_dict(obj):
    return obj.__dict__


# In[16]:


def export_json(space_launches):  
    obj_dict_list = []
    i = 0 
    for obj in space_launches:
        obj_dict_list += [obj_dict(space_launches[i])] #use the obj_dict fucnction to convert objects into dict format
        i += 1
    
    json_obj = json.dumps(obj_dict_list, sort_keys = True, indent = 4) #use json_dumps to create a json object as shown in pdf of the objects with indentation 4 and sorted keys. 
    
    with open("launches_ania_webb.json", "w") as filename:
        filename.write(json_obj) #write the json object to file
    
    return filename.name #return filename


# In[9]:


CITIES_URL = "https://dsci.isi.edu/api/cities"

def get_city_coordinates(url):
    csv_contents = requests.get(url) #get the csv file from url using requests.get
    csv_contents = csv_contents.text.split(',')

    key = 'ad0930858c9744db80fb97decabc3caa'
    geocoder = OpenCageGeocode(key)

    city_list = []
    for city in csv_contents:
        city = city.strip()
        geocoder_calc = geocoder.geocode(city, no_annotations='1') #for each city in csv file get the latitude and longitude through opencagedata API
        lat = geocoder_calc[0]['geometry']['lat']
        lng = geocoder_calc[0]['geometry']['lng']

        instance = Coordinate(city = city, 
                              latitude = lat,
                              longitude = lng) #create an instance of Coordinate with respective values
        
        city_list += [instance]

    obj_dict_list = [] 
    i = 0 
    for obj in city_list: #Create a dictionary as shown in pdf using dict.  
        obj_dict_list += [obj_dict(city_list[i])] #use the obj_dict fucnction to convert objects into dict format
        i += 1
        
    obj_dict_list = json.dumps(obj_dict_list)

    return obj_dict_list #Return the dictionary 

