#!/usr/bin/env python
# coding: utf-8

# In[8]:


import string 

def is_acceptable(password):
    
    check_upper = False
    check_lower = False
    check_acceptable = False
    check_punctuation = 0 
    check_digits = 0 
    
    for character in password: 
        if character in string.ascii_lowercase: #at least one lowercase letter (Hint: string.ascii_lowercase)
            check_upper = True 
        elif character in string.ascii_uppercase: #at least one uppercase letter (Hint: string.ascii_uppercase)
            check_lower = True
        elif character in string.punctuation: #at least two special characters from this list (Hint: string.punctuation)
            check_punctuation += 1 
        elif character in string.digits: #at least two digits (Hint: string.digits)
            check_digits += 1
        elif character == (' '):
            check_acceptable = True
        else:
            check_acceptable = False
            
    if check_upper == True and check_lower == True and 10 <= len(password) <= 20 and check_punctuation >= 2 and check_digits >= 2:
        check_acceptable = True
    else:
        check_acceptable = False
    
    if check_acceptable == True: 
        return True
    else:
        return False


# In[ ]:


def caesar_cipher(message, n):
    
    new_message = "" #create an empty string to hold the final message later
    
    while len(new_message) < len(message): #run until len the new message is the same as message
        for letter in message: 
            if letter in string.ascii_lowercase: 
                new_message += chr((ord(letter) + n - 97) % 26 + 97) 

            elif letter in string.ascii_uppercase:
                new_message += chr((ord(letter) + n - 65) % 26 + 65)
            
    return new_message


# In[ ]:


def parse_swap(word, c):
    
    letter = 0
    
    while letter < len(word): #run until len of letters is the same as word
        if word[letter] == c: #if the letter is equal to character
            word = word[letter+1:] + c + word[:letter]
            letter = letter + 1
            continue
        else: #if not just increase letter by 1 and begin again 
            letter = letter + 1
            continue
                
    return word

