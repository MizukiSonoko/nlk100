

c1 = open("col1.txt")
c2 = open("col2.txt")

for line in c1:
    print(line.replace('\n','') + "," + c2.readline(), end='')    




