
import json

f = open("jawiki-country.json")
data = {}
for line in f.readlines():
	tmp = json.loads(line)
	data[tmp['title']] = tmp['text']

uk = data['イギリス']
for line in uk.split('\n'):
	if 'Category' in line:
		print(line.split(':')[1].split(']]')[0].split('|')[0])

f.close()

