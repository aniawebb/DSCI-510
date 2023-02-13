#!/usr/bin/env python
# coding: utf-8

# In[6]:


def day_of_week(day, offset):
    if 0 <= day <= 6:
        finaldate = (int(day) + offset) % 7
        return finaldate
    else:
        print("Please enter a number between 0 and 6 for the day of the week!")


# In[2]:


def is_leap_year(year):
    if int(year) % 4 == 0 and year % 100 != 0: #1) The year is a multiple of 4 and not a multiple of 100. 
        return True
    elif int(year) % 400 == 0: #2) The year is a multiple of 400.
        return True
    else: 
        return False


# In[3]:


def type_triangle(s1, s2, s3):
    triangle= float(s1), float(s2), float(s3) #convert to float
    triangle_list= list(triangle) #put values into list
    triangle_list.sort() #sort list from smallest to greatest to assign values
    
    min_length= triangle_list[0] #smallest value
    middle_length= triangle_list[1] #middle value
    max_length= triangle_list[2] #greatest value
    
    acute= 1 
    right= 2
    obtuse= 3
    invalid= 0
    
    if (max_length) < (min_length + middle_length): #the longest side must shorter than the sum of the smaller sides.
        if (max_length**2) < ((min_length**2) + (middle_length**2)): #acute
            return acute
        elif (max_length**2) == ((min_length**2) + (middle_length**2)): #right
            return right
        elif (max_length**2) > ((min_length**2) + (middle_length**2)): #obtuse
            return obtuse
    else: 
        return invalid 


# In[4]:


if __name__ == '__main__':
    # If you want to use input, use it here, inside the if statement
    # day = float(input("Enter day:"))
    # offset = float(input("Enter offset:"))
    day = 1
    offset = 2


# In[5]:


# Testing Q1
#print(day_of_week(day, offset))

# Testing Q2
#print(is_leap_year(2022))

# Testing Q3
#print(type_triangle(3, 5, 4))

