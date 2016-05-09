import MeCab
import numpy

class Morpheme:
	def __init__(self, surface, base, pos, pos1):
		self.surface = surface
		self.base = base
		self.pos  = pos
		self.pos1 = pos1

def Dot(P,t1,t2):
	res = 0
	if not t1 in P or not t2 in P:
		print("Key invalied")
		return 0
	for k in P[t1].keys():
		if k in P[t2]:
			res += P[t1][k]*P[t2][k]
	return res

R = 10
def exec(tokens):
	M = len(tokens)
	P = {}
	for i in range(len(tokens)):
		token = tokens[i]
		for j in range(-R,R):
			if j == 0:
				continue
			if not token in P:
				P[token] = {}
			if i+j < 0 or i+j >= len(tokens):
				continue 
			if tokens[i+j] in P[token]:
				P[token][tokens[i+j]] += 1
			else:
				P[token][tokens[i+j]] = 1
	
	print(Dot(P,'チノ','リゼ'))	
	print(Dot(P,'チノ','おっとり'))	
	print(Dot(P,'おっとり','クール'))	
	print(Dot(P,'シャロ','喫茶店'))	

if __name__ == "__main__":	
	f = open('test.txt')
	text = f.read()

	m = MeCab.Tagger ("-Ochasen -ucustom.dic")
	m.parse('')
	node =  m.parseToNode( text )

	tokens = []
	while node:
		d = node.feature.split(',')
		tokens.append(node.surface)
		node = node.next

	exec(tokens)
