#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import pickle

# url = 'http://www.pythonchallenge.com/pc/def/peak.html'
#
# r = requests.get(url)
# soup = BeautifulSoup(r.text, 'html.parser')
#
# peakhell = soup.find_all('peakhell')[0]
#
# url = 'http://www.pythonchallenge.com/pc/def/banner.p'
#
# r = requests.get(url)

f = open('banner.p', 'rb')
unpicked = pickle.load(f)

message = ''

for word in unpicked:
    for letter in word:
        message += letter[0] * letter[1]
    message += '\n'

print(message)
