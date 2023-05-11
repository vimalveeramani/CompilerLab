gram = {
	"E":["E+T","T"],
	"T":["T*F","F"],
	"F":["(E)","i"]
}
result = {'E': [['T', "E'"]], 
          'T': [['F', "T'"]], 
          'F': [['(', 'E', ')'], ['i']],
          "E'": [['+', 'T', "E'"], ['e']],
          "T'": [['*', 'F', "T'"], ['e']]}

def first(gram, term):
	a = []
	if term not in gram:
		return [term]
	for i in gram[term]:
		if i[0] not in gram:
			a.append(i[0])
		elif i[0] in gram:
			a += first(gram, i[0])
	return a

firsts = {}
for i in result:
	firsts[i] = first(result,i)
	print(f'First({i}):',firsts[i])


def follow(gram, term):
	a = []
	for rule in gram:
		for i in gram[rule]:
			if term in i:
				temp = i
				indx = i.index(term)
				if indx+1!=len(i):
					if i[-1] in firsts:
						a+=firsts[i[-1]]
					else:
						a+=[i[-1]]
				else:
					a+=["e"]
				if rule != term and "e" in a:
					a+= follow(gram,rule)
	return a

follows = {}
for i in result:
	follows[i] = list(set(follow(result,i)))
	if "e" in follows[i]:
		follows[i].pop(follows[i].index("e"))
	follows[i]+=["$"]
	print(f'Follow({i}):',follows[i])
