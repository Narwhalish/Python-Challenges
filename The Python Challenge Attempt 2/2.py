#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import os.path
import pyperclip
import webbrowser
import requests
from bs4 import BeautifulSoup as bs
from bs4 import Comment

URL_BASE = 'http://www.pythonchallenge.com/pc/def/'

r = requests.get('http://www.pythonchallenge.com/pc/def/ocr.html')
soup = bs(r.content, 'html.parser')

comment = soup.find_all(text=lambda text: isinstance(text, Comment))[1]

comment_fractured = list(comment)
comment_set = set(comment)

unique = []
for c in comment_set:
    if comment_fractured.count(c) == 1:
        unique.append((c, comment_fractured.index(c)))

unique.sort(key=lambda val: val[1])

url_tail = ''.join(c[0] for c in unique)
url = os.path.join(URL_BASE, f'{url_tail}.html')

pyperclip.copy(url)
webbrowser.open(url)
