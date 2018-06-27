#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import lxml.html

html = requests.get('http://www.pythonchallenge.com/pc/def/ocr.html')
doc = lxml.html.fromstring(html.content)

mess = doc.xpath('//comment()')[-1]
encoded = str(mess)[5:-4]

unique = []

for sample in encoded:
    count = 0
    for n, compare in enumerate(encoded):
            if sample == compare:
                count += 1
            if count == 2:
                break
    if count != 1:
        encoded = [ltr for ltr in encoded if ltr != sample]
    else:
        unique.append(sample)

decoded = ''.join(unique)

print(decoded)
