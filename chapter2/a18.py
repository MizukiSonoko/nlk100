
from operator import itemgetter

f = open("hightemp.txt")

dat = []
for line in f:
    dat.append(line.split('\t'))

for l in sorted(dat, key=itemgetter(-1)):
    print(l)


