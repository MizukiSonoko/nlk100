# -*- coding: utf-8 -*-

s1 = "paraparaparadise"
s2 = "paragraph"

def ngram(s,n=1):
    ls = []
    p = 0
    s = s.replace(' ','')
    while p < len(s):
        ls.append(s[p:p+n])
        p = p + n

    return ls

X = set( ngram(s1,2))
Y = set( ngram(s2,2))

print(X | Y)
print(X & Y)
print(X - Y)

print("se" in X)
print("se" in Y)


