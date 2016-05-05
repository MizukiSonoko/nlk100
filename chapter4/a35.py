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
mx = {"text":"","len":0}
l = 0
for token in tokens:
	if "名詞" == token.pos:
		l += 1
		res += token.surface
	else:
		if mx["len"] <= l:
			mx["text"] = res
			mx["len"] = l
		l = 0
		res = ""

print(mx["text"])
