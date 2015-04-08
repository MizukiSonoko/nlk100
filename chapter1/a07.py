# -*- coding: utf-8 -*-
import codecs
import sys
sys.stdout = codecs.getwriter('utf_8')(sys.stdout)

x = raw_input("x ->")
y = raw_input("y ->")
z = raw_input("z ->")

def func(x,y,z):
    return u"{0}時の{1}は{2}".format( unicode(x, 'utf_8'), unicode(y, 'utf_8'), unicode(z,'utf_8'))

print func(x,y,z)

