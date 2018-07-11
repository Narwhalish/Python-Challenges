#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import re
import zipfile

z = zipfile.ZipFile('channel.zip')
print(z.read('readme.txt').decode(encoding='utf-8'))

number = '90052'
pattern = re.compile('Next nothing is (\d+)')

comments = ''

while True:
    comments += z.getinfo(f'{number}.txt').comment.decode(encoding='utf-8')
    match = re.search(pattern, z.read(f'{number}.txt').decode(encoding='utf-8'))
    if match == None:
        break
    number = match.group(1)

print(comments)
