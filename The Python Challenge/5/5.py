#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import pickle

f = open('banner.p', 'rb')
unpicked = pickle.load(f)

for line in unpicked:
    print(''.join([k * v for k, v in line]))
