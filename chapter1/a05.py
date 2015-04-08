# -*- coding: utf-8 -*-

ss = "I am an NLPer"

def ngram(s,n=1):
    ls = []
    p = 0
    s = s.replace(' ','')
    while p < len(s):
        ls.append(s[p:p+n])
        p = p + n

    return ls

print ngram(ss,2)
print ngram(ss,3)
