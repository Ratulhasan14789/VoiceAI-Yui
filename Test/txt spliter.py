x=0
n='0'
with open('sao/sao.txt','r') as s:
	w=s.read()
	for c in w:
		a=x//999
		n=str(a)
		with open('sao/sao'+n+'.txt','a') as y:
			y.write(c)
			x+=1
		