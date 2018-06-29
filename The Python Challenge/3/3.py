#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import requests
import lxml.html
import re

html = requests.get('http://www.pythonchallenge.com/pc/def/equality.html')
doc = lxml.html.fromstring(html.content)

comment = doc.xpath('//comment()')[-1]
mess = str(comment)[5: -4]

print(''.join(re.findall('(?:^|[^A-Z])[A-Z]{3}([a-z])[A-Z]{3}(?:$|[^A-Z])', mess)))
