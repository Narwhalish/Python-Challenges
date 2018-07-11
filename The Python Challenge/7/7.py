#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import requests
from Pillow import PIL
from io import BytesIO

r = requests.get('http://www.pythonchallenge.com/pc/def/oxygen.png')
i = Image.open(BytesIO(r.content))
