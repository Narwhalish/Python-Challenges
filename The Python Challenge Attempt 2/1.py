#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import os.path
import webbrowser
import pyperclip
import requests
from bs4 import BeautifulSoup as bs

URL_BASE = 'http://www.pythonchallenge.com/pc/def/'

r = requests.get('http://www.pythonchallenge.com/pc/def/map.html')
soup = bs(r.content, 'html.parser')

font_elements = soup.find_all('font')
s = font_elements[1].text.strip()

def caesar_shift(c):
    c_ord = ord(c)
    if 97 <= c_ord <= 122:
        if (c_ord + 2) <= 122:
            return chr(c_ord + + 2)
        elif (c_ord + 2) > 122:
            return chr(c_ord - 24)
    else:
        return c

s_list = s.split()
s_shifted_list = [''.join([caesar_shift(c) for c in w]) for w in s_list]

output = ' '.join(s_shifted_list)

print(output)

url_encrypted = 'map'
url_decrypted = ''.join(caesar_shift(c) for c in url_encrypted)

url = os.path.join(URL_BASE, f'{url_decrypted}.html')

pyperclip.copy(url)
webbrowser.open(url) 
