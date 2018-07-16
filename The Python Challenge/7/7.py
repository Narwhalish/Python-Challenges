#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import requests
import re
from PIL import Image
from io import BytesIO

r = requests.get('http://www.pythonchallenge.com/pc/def/oxygen.png')
i = Image.open(BytesIO(r.content))

bbox = i.getbbox()

values = []
colors = [chr(i.getpixel((m, bbox[3] / 2))[0]) for m in range(0, 629, 7)]

for c in colors:
    values.append(c)

message = ''.join(values)

pattern = re.compile('\[((?:\d+,? ?)+)+\]')
match = re.search(pattern, message)

answer = ''.join([chr(int(c)) for c in match.group(1).split(', ')])

print(answer)
