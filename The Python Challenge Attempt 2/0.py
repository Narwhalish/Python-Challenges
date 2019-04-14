#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import os.path
import webbrowser
import pyperclip

URL_BASE = 'http://www.pythonchallenge.com/pc/def/'

val = pow(2, 38)
url = os.path.join(URL_BASE, f'{val}.html')

pyperclip.copy(url)
webbrowser.open(url)
