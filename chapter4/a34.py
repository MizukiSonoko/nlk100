import MeCab

f = open('neko.txt')
text = f.read()

m = MeCab.Tagger ("-Ochasen -ucustom.dic")
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
	tokens.append(Morpheme(d[-3],d[-1],d[0],d[1]))
	node = node.next

for i in range(1,len(tokens)-1):
	token = tokens[i]
	if token.surface == "の" and token.pos == "助詞":
		prev = tokens[i-1]
		next = tokens[i+1]
		print(prev.surface, " の ", next.surface)
