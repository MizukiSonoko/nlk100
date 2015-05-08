
f = open("hightemp.txt")
c1 = open("col1.txt", 'w')
c2 = open("col2.txt", 'w')
res = ""

pos = 0
for line in f:
    pos = 0
    res = ""
    for c in line:
        if pos == 0:
            if c == '\t':
                pos = 1
                #print(res +' ',end="")
                c1.write(res+'\n')
                res = ""
            else:
                res += c
        elif pos == 1:
            if c == '\t':
                pos = 2
                #print(res)
                c2.write(res+'\n')
                res = ""
            else:
                res += c

c1.close()
c2.close()

