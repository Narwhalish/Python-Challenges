#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import os
import re
import zipfile

channel = os.getcwd() + '/channel'
num_files = os.listdir(channel)

pattern = re.compile('(?:n|N)ext nothing is (\d+)')

number = 90052
order = []

while True:
    i = open(channel + '/' + str(number) + '.txt', 'r')

    text = i.read()
    match = pattern.search(text)
    if match == None:
        break
    number = match.group(1)
    order.append(str(number) + '.txt')

i.close()

z = zipfile.ZipFile('channel.zip')
message = ''

for f in order:
    message += z.getinfo(f).comment.decode(encoding='utf-8')

print(message)

# for m in z.infolist():
#     message += m.comment.decode(encoding='utf-8')
