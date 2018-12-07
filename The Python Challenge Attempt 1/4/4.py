#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re

# number = 12345
number = 16044/2
pattern = re.compile('the next nothing is (\d+)')

while True:
    r = requests.get(f'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={number}')
    soup = BeautifulSoup(r.content, 'html.parser')

    text = soup.get_text()
    print(text)

    match = pattern.search(text)
    if match == None:
        print(f'Found something at here:\n"{text}"')
        break

    number = match.group(1)
