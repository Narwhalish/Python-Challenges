#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import os.path
import pyperclip
import webbrowser
import requests
from bs4 import BeautifulSoup as bs
import re

URL_BASE = 'http://www.pythonchallenge.com/pc/def/'

nothing_val = '12345'
message = ''
while True:
    r = requests.get(f'{URL_BASE}linkedlist.php', params={'nothing': nothing_val})
    soup = bs(r.content, 'html.parser')

    pattern = re.compile(r'and the next nothing is (\d+)')
    matches = re.findall(pattern, soup.text)

    try:
        nothing_val = matches[0]
    except IndexError:
        message = soup.text
        break

print(message)


