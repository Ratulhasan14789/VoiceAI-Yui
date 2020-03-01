a=['an','rb','cc','dx']
b=['ad','bc']
for i in b:
	id=[]
	for w0 in i:
		for s in a:
			w1=s[i.index(w0)]
			if w0==w1:
				id += [a.index(s)]
	id = list(dict.fromkeys(id))
	print('b[%i] ~ a'%b.index(i) ,id)
