#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import lxml.html

html = requests.get('http://www.pythonchallenge.com/pc/def/equality.html')
doc = lxml.html.fromstring(html.content)

comment = doc.xpath('//comment()')[-1]
stringy_mess = str(comment)[5:-4]

""" A(34) -> Z(90), a(97) -> z(122) """

mess = bytes(stringy_mess, encoding='utf-8')

case = []
for c in mess:
    if 34 <= c <= 90:
        case.append('u')
    elif 97 <= c <= 122:
        case.append('d')
    else:
        case.append('n')
case = ''.join(case)

n = 0
index_i = []
while True:
    match = case.find('duuuduuud', n)
    n = match
    n += 9
    index_i.append(match)
    if match == -1:
        break

# decoded = ''
decoded = []
for i in index_i:
    # decoded += chr(mess[i + 3])
    decoded.append(chr(mess[i + 4]))

print(decoded)
