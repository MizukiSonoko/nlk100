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
	tokens.append(Morpheme(node.surface,d[-3],d[0],d[1]))
	node = node.next

for token in tokens:
	if "動詞" == token.pos:
		print(token.base)
