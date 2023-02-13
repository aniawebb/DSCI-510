#!/usr/bin/env python
# coding: utf-8

# In[5]:


def celsius_to_fahrenheit(celcius_input):
    fahrenheit_temp = float(celcius_input) * (9/5)
    fahrenheit_output = fahrenheit_temp + 32
    return fahrenheit_output

celsius_to_fahrenheit(33.6)


# In[7]:


import math

def circle_area(radius_input):
    area_output = float(math.pi * ((radius_input)**2))
    return area_output

circle_area(42.9)


# In[8]:


import math

def cylinder_volume_surface(radius_input, height_input):
    volume_output = float(math.pi * ((radius_input)**2) * height_input)
    surface_output = float((2 * math.pi * radius_input * height_input) + (2 * math.pi * (radius_input)**2))
    return volume_output, surface_output

cylinder_volume_surface(2.8, 6.5)

