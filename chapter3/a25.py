
import json

f = open("jawiki-country.json")
data = {}
for line in f.readlines():
	tmp = json.loads(line)
	data[tmp['title']] = tmp['text']

uk = data['イギリス']
section = False

raw = ""
for line in uk.split('\n'):	
	if section:
		if "}}" == line:
			section = False
			break
		raw += line
	elif '基礎情報' in line:
		section = True

prev = ""
info = {}
for i in raw.split('|'):
	if '' == i:
		continue

	tmp = i.split('=')
	if len(tmp) >= 2:
		info[tmp[0]] = tmp[1].split('<')[0]
		prev = tmp[0]
	else:
		info[prev] = info[prev] + tmp[0]

for k, v in info.items():
	print(k,v)

f.close()

