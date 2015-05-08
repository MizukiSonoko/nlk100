
f = open("hightemp.txt")

cnt = 0
for s  in f.read():
    if s == '\n':
        cnt += 1

print(cnt)

