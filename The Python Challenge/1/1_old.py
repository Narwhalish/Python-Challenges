#!/usr/bin/python3
# -*- coding: utf-8 -*-

encoded = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

def decode(ltr):
    #condition 1: if ltr is bigger than or equal to ord('a') and smaller than ord('y')
    if 96 < ord(ltr) < 121:
        ltr = chr(ord(ltr) + 2)
    #condition 2: if ltr is bigger than ord('y')
    elif 121 <= ord(ltr) < 123:
        ltr = chr(96 + ord(ltr) + 2 - 122)

    return ltr

decoded = ''.join([decode(ltr) for ltr in encoded])

print(decoded)
