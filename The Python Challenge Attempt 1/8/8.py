#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import requests
import re
import bz2
from lxml import html

r = requests.get('http://www.pythonchallenge.com/pc/def/integrity.html')
doc = html.fromstring(r.content)

comments = doc.xpath('//comment()')[0].text.split('\n')[1: 3]

pattern = re.compile(".+'(.+)'")
# un, pw = map(lambda x: re.search(pattern, x).group(1), comments)

un = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

message = ' '.join([bz2.decompress(un).decode('utf-8'), bz2.decompress(pw).decode('utf-8')])

print(message) #prints 'huge file'
