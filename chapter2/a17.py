
f = open("hightemp.txt")
sss = ""
pos = 0
res = []

for line in f:
    pos = 0
    sss = ""
    for c in line:
        if pos == 0:
            if c == '\t':
                pos = 1
                res.append(sss)
                sss = ""
            else:
                sss += c

print(res)
print(len(res))

