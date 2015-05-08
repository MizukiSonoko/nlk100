# -*- coding: utf-8 -*-

x = input("x ->")

def cipher(x):
    res = ""
    for i in x:
        if i.islower():
            res += chr(219 - ord(i))
        else:
            res += i
    print(res)

cipher(x)

