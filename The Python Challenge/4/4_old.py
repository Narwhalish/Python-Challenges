#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re

data = []


def store_numbers(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    text = soup.get_text()
    number = re.findall('^.*the next nothing is (\d+)', text)[0]
    print(number)
    url = f'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={number}'
    data.append(number)

    return url


if __name__ == '__main__':
    # url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345'
    # url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=8022'
    url ='http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=63579'
    for _ in range(400):
        try:
            url = store_numbers(url)
        except IndexError:
            print(f'Found something! Go to {data[-1]}')
            break
