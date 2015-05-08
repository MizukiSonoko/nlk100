
n = int(input())

f = open("hightemp.txt")

for line in f: 
    print(line[:n:])

