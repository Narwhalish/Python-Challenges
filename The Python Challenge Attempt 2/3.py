#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import os.path
import pyperclip
import webbrowser
import requests
from bs4 import BeautifulSoup as bs
from bs4 import Comment
import re

URL_BASE = 'http://www.pythonchallenge.com/pc/def/'

r = requests.get('http://www.pythonchallenge.com/pc/def/equality.html')
soup = bs(r.content, 'html.parser')

comment = 'a' + soup.find_all(text=lambda text: isinstance(text, Comment))[0] + 'a'

pattern = re.compile(r'[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]')
matches = re.findall(pattern, comment)

url_tail = ''.join(matches)
url = os.path.join(URL_BASE, f'{url_tail}.php')

pyperclip.copy(url)
webbrowser.open(url)
