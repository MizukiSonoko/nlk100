# -*- coding: utf-8 -*-

s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
ones = [1,5,6,7,8,9,15,16,19]

count = 0
for w in s.split(' '):
    count = count + 1 
    if count in ones:
        print w[0:1]
    else:
	print w[0:2]
