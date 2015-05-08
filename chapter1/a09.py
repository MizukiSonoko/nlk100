
import random

def rand(w):
    ls = []
    res = w[0]
    while len(ls) != len(w) - 2:
        while True:
            p = random.randint(1,len(w) - 2)
            if p not in ls:
                break
        res += w[p]
        ls.append(p)

    res += w[len(w) - 1]
    return res

ss = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
wls = ss.split(' ')
for w in wls:
    if len(w) < 4:
        print(w, end="")
    else:
        print(rand(w), end="")

