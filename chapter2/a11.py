
f = open("hightemp.txt")

res  = ""
for c in f.read():
    if c == '\t':
        res += ' '
    else:
        res += c

print(res)    

