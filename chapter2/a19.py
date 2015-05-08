
f  = open("hightemp.txt")
d = {}

for line in f:
    first = line.split('\t')[0]
    for c in first:
        if c in d.keys():
            d[c] = d[c] + 1
        else:
            d[c] = 1

for k, v in sorted(d.items(), key =lambda x:x[1], reverse= True):
    print( k, v)

