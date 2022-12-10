from string import ascii_lowercase
from string import ascii_uppercase
import re

def generate_char_rv_dict()->dict:
    rv_dict = {}

    for i in range(10):
        rv_dict[str(i)] = i 
    
    x = 10
    for i in range(len(ascii_lowercase)):
        rv_dict[ascii_lowercase[i]] = x
        rv_dict[ascii_uppercase[i]] = x+1
        x = x+2

    return rv_dict

def generate_rv_char_dict()->dict:
    rv_dict = {}

    for i in range(10):
        rv_dict[i] = str(i)
    
    x = 10
    for i in range(len(ascii_lowercase)):
        rv_dict[x] = ascii_lowercase[i]
        rv_dict[x+1] = ascii_uppercase[i]
        x = x+2

    return rv_dict

def filter_text(text:str)->str:
    my_text = re.sub("[^A-Za-z0-9]","",text)
    return my_text