mypath='books/'
def trend(loc, min_len=0):
	from os import listdir
	import re
	#from multiprocessing import Processn
	from os.path import isfile, join
	on = [loc+f for f in listdir(loc) if isfile(join(loc, f))]

	data=''


	for i in on:
		with open(i) as f:
			data+=f.read()+' '

	dat= re.sub('[^\w]',' ',data)
	dat= re.sub(' [a]* ',' ',dat)
	dat= re.sub('\s+',' ',dat)
	#print(dat)
	dat=dat.lower()
	dat=dat.replace(' d ','\'d ')
	dat=dat.replace(' t ','\'t ')
	dat=dat.replace(' m ','\'m ')
	dat=dat.replace(' re ','\'re ')
	dat=dat.replace(' d ','\'d ')
	dat=dat.replace(' ll ','\'ll ')
	dat0=dat.split()
	#print(len(dat))
	dat1 = list(dict.fromkeys(dat0))
	#del data
	data=[ ]
	for i in dat1:
		try:
			int(i)
		except:
			if re.search('^a+h*$', i):
				pass
			else:
				if len(i)>=min_len:
					data+=[i]
	data.sort()
	#print(len(data))
	#print(len(dat))
	#print(data)

	rem=[]
	'''for i in dat0:
		for m in data:
			x=0
			if m==i: x+=1
		rem+=[(m,x)]
		print()
	print(rem)'''
	for i in data:
		x=len(re.findall(' '+i+' ',dat))
		rem+=[[i,x]]
		print(i+'\t\t'+str(x))
	print(rem)

trend(mypath)
		
		