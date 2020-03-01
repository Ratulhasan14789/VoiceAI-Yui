x=0
n='0'
with open('sao1/sao.txt','r') as s:
	w=s.read()
	print(len(w))
	w=w.replace('\n\n\n','\n')
	w=w.replace('\n\n','\n')
	w=w.replace('.'*5,'..')
	w=w.replace('.'*4,'..')
	w=w.replace('.'*3,'..')
	w=w.replace('Page','P')
	print(len(w))
	input=w
	output = []
	length = 500
	for i in range(len(input))[::length]:
		output.append(input[i:i+length])
	
	for i in range(len(output)):
		if i<10:
			m='00'+str(i)
		elif i<100:
			m='0'+str(i)
		else:
			m=str(i)
		with open('sao1/MEMO_20191204_111111111111'+m+'.txt','w') as y:
			y.write('s1-'+str(i)+output[i])
with open('sao1/sao-1-1.txt','r') as y:
	print(len(y.read()))
#print(x)
		