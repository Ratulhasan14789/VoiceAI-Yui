mypath='books/'

from os import listdir
import re
from threading import Thread
from os.path import isfile, join

rem=[]

def distribute(data):
	global rem,dat
	for i in data:
		x=len(re.findall(' '+i+' ',dat))+1
		rem+=[[i,x]]
		print(i+'\t\t'+str(x))

def trend(loc, min_len=0):

	global rem,dat
	on = [loc+f for f in listdir(loc) if isfile(join(loc, f)) if f.endswith('.txt')]

	data=''


	for i in on:
		with open(i) as f:
			data+=f.read()+' '
	dat=data.lower()
	dat= re.sub('[^a-z\'\-]',' ',dat)
	#dat= re.sub(' [a]* ',' ',dat)
	dat= re.sub('\s+',' ',dat)
	#print(dat)
	
	'''dat=dat.replace(' d ','\'d ')
	dat=dat.replace(' t ','\'t ')
	dat=dat.replace(' m ','\'m ')
	dat=dat.replace(' re ','\'re ')
	dat=dat.replace(' d ','\'d ')
	dat=dat.replace(' ll ','\'ll ')'''
	dat0=re.findall('[a-z]+[\'\-]*[a-z]*',dat)
	#print(len(dat))
	dat1 = list(dict.fromkeys(dat0))
	#del data
	data=[ ]
	for i in dat1:
		try:
			int(i)
		except:
			#if re.search('^a+h*$', i):
				#pass
			#else:
			if len(i)>=min_len:
				data+=[i]
	data.sort()
	#print(len(data))
	#print(len(dat))
	#print(data)
	
	#rem=[]
	'''for i in dat0:
		for m in data:
			x=0
			if m==i: x+=1
		rem+=[(m,x)]
		print()
	print(rem)'''
	t1= Thread(target=distribute, args=(data[::10],))
	t2= Thread(target=distribute, args=(data[1::10],))
	t3= Thread(target=distribute, args=(data[2::10],))
	t4= Thread(target=distribute, args=(data[3::10],))
	t5= Thread(target=distribute, args=(data[4::10],))
	t6= Thread(target=distribute, args=(data[5::10],))
	t7= Thread(target=distribute, args=(data[6::10],))
	t8= Thread(target=distribute, args=(data[7::10],))
	t9= Thread(target=distribute, args=(data[8::10],))
	t10= Thread(target=distribute, args=(data[9::10],))
	t1.start()
	t2.start()
	t3.start()
	t4.start()
	t5.start()
	t6.start()
	t7.start()
	t8.start()
	t9.start()
	t10.start()
	
	t1.join()
	t2.join()
	t3.join()
	t4.join()
	t5.join()
	t6.join()
	t7.join()
	t8.join()
	t9.join()
	t10.join()
	
	rem.sort()
	print(rem)
	
	with open('output.txt','w') as f:
		for i, j in rem:
			f.write(i+'=\t\t'+str(j)+'\n')
trend(mypath)
		
		