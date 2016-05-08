import MeCab
import numpy

class Morpheme:
	def __init__(self, surface, base, pos, pos1):
		self.surface = surface
		self.base = base
		self.pos  = pos
		self.pos1 = pos1

R = 10
def exec(tokens):
	M = len(tokens)
	P = {}
	for i in range(len(tokens)):
		token = tokens[i]
		for j in range(-R,R):
			if j == 0:
				continue
			if not token.surface in P:
				P[token.surface] = {}
			if token[i+j].surface in P[token.surface]:
				P[token.surface][token[i+j].surface] += 1
			else:
				P[token.surface][token[i+j].surface] = 1

	print(P)

if __name__ == "__main__":	
	f = open('test.txt')
	text = f.read()

	m = MeCab.Tagger ("-Ochasen -ucustom.dic")
	m.parse('')
	node =  m.parseToNode( text )

	tokens = []
	while node:
		d = node.feature.split(',')
		tokens.append(Morpheme(node.surface,d[-3],d[0],d[1]))
		node = node.next

	exec(tokens)
