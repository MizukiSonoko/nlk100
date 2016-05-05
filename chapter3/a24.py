
import json

f = open("jawiki-country.json")
data = {}
for line in f.readlines():
	tmp = json.loads(line)
	data[tmp['title']] = tmp['text']

uk = data['イギリス']
for line in uk.split('\n'):
	if '.jpg' in line:
		print(line.split('|')[0].split(':')[1])

f.close()

