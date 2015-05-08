
n = int(input())
f = open("hightemp.txt")

for line in f:
    print(line[::-1][1:n+1:][::-1])

