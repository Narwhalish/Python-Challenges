#!/usr/bin/python3
# -*- encoding: utf-8 -*-

'''
Marked as 'old' because the string *un* cannot be encoded into a bytes-like object without the addition of escape characters.
*un* is set to equal the return value of the re.search
When printed, *un* shows as 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084' and is type <class 'str'>.
However, un.encode('raw_unicode_escape') results in addition of escape characters for each backslashself.
On the other hand, *un2* is directly set with the value 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'.
When printed, *un2* shows as 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084' and is also type <class 'str'>.
However, un2.encode('raw_unicode_escape') results in a bytes version of the same string:
b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
'''

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

un = u'%s' % re.search(pattern, comment[0]).group(1)
# un2 = u'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'

print(un.encode('raw_unicode_escape'))
# print(bz2.decompress(un.encode('raw_unicode_escape')))
