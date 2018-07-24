#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import requests
import re
import bz2
from lxml import html

# r = requests.get('http://www.pythonchallenge.com/pc/def/integrity.html')
# doc = html.fromstring(r.content)
#
# pattern = re.compile(".*'(.*)'")
# comments = doc.xpath('//comment()')[0].text.split('\n')[1:3]
#
# un, pw = map(lambda x: re.search(pattern, x).group(1).encode('raw_unicode_escape'), comments)
#
#
#
# print(un)
# print(pw)

r = requests.get('http://www.pythonchallenge.com/pc/def/integrity.html')

doc = html.fromstring(r.content)
comment = doc.xpath('//comment()')[0].text.split('\n')[1:3]

pattern = re.compile("[a-z]{2}: '(.+)'")

un = re.search(pattern, comment[0]).group(1)
un2 = u'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
exec('a=' + un)
print(a)
# print(un2)
# print(bz2.decompress(un.encode('raw_unicode_escape')))
