
import json

f = open("jawiki-country.json")
data = {}
for line in f.readlines():
	tmp = json.loads(line)
	data[tmp['title']] = tmp['text']

uk = data['イギリス']
for line in uk.split('\n'):
	if '==' in line:
		print(line.replace('=',''), int(line.count('=')/2-1))

f.close()

