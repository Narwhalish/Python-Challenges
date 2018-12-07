#!/usr/bin/python3
# -*- coding: utf-8 -*-

# encoded = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

encoded = "http://www.pythonchallenge.com/pc/def/map.html"

def decode(encoded):
    conversion_key = str.maketrans('abcdefghijklmnopqrstuvwxyz', 'cdefghijklmnopqrstuvwxyzab')
    decoded = encoded.translate(conversion_key)

    return decoded

print(decode(encoded))
