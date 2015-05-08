
def split(s, n):
    return [s[i:i+n] for i in range(0, len(s), n)]

n = int(input())
f = open("hightemp.txt")

for line in f:
    print(split(line, n))

