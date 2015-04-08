# -*- coding: utf-8 -*-
import codecs
import sys
sys.stdout = codecs.getwriter('utf_8')(sys.stdout)

x = raw_input("x ->")

def cipher(x):
    res = ""
    for i in x:
        if i.islower():
            res += chr(219 - ord(i))
        else:
            res += i
    print res

cipher(x)

