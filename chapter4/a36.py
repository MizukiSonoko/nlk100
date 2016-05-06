import MeCab

f = open('neko.txt')
text = f.read()

m = MeCab.Tagger ("-Ochasen -ucustom.dic")
m.parse('')
node =  m.parseToNode( text )

class Morpheme:
	def __init__(self, surface, base, pos, pos1):
		self.surface = surface
		self.base = base
		self.pos  = pos
		self.pos1 = pos1
	
tokens = []
while node:
	d = node.feature.split(',')
	tokens.append(Morpheme(node.surface.encode('utf-8').decode('utf-8'),d[-3],d[0],d[1]))
	node = node.next

res = ""
data = {}
for token in tokens:
	if token.surface in data:
		data[token.surface] += 1
	else:
		data[token.surface] = 1

cnt = 0
for k, v in sorted(data.items(), key=lambda x:x[1], reverse=True):
	cnt += 1
	if cnt > 10:
		quit(1)
	print(k, v)

