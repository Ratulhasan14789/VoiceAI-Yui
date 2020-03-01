mypath='books/'
t=26.5
from os import listdir
import re
from threading import Thread
from os.path import isfile, join
import collections
from time import sleep
rem=[]

'''Dracula

The merry adventures of Robin Hood

Frankenstein 

A take of two cities

The picture of Dorian Gray

Oliver Twist

King Solomon's mines

The prince and the pauper 

The invisible man

Ivanhoe

The mutiny on board H.M.S Bounty

The hunchback of Notre Dame

The Oregon Trail

The hound of Baskervilles

Mobidick

Great Expectations

The War of the Worlds

The Wizard of Oz

The Adventures of Tom Sawyer

20000 Leagues under the sea

The Call of the Wild

Around the world in Eighty Days

Galiver's adventures

The Jungle Book

The adventures of Don Quixote

The adventures of Huckleberry Finn

Tales of Mystery and Terror

The man in the Iron Mask

Black beauty

The Last of The Mohicans

David Copperfield

Captain Courageous

White Fang

Peter Pan

The Three Musketeers

The Legend of Sleepy Hollow and other Stories

The Count Of Monte Cristo (my favourite)'''

def distribute(data,min_len):
	global rem,val
	#print(data)
	
	for i in data:
		if len(i)>=min_len:
			rem+=[[val[i],i]]
			print(i+'\t\t'+str(val[i]))

def trend(loc, min_len=0):

	global rem, val
	on = [loc+f for f in listdir(loc) if isfile(join(loc, f)) if f.endswith('.txt')]

	data=''


	for i in on:
		with open(i) as f:
			data+=f.read()+' '
	print('Stage-1 book import done')
	sleep(.5)
	dat=data.lower()
	print('Stage-2 changes done')
	#sleep(.5)
	'''dat= re.sub('[^a-z\'\-]',' ',dat)
	print('Stage-3 change 2 done')
	#dat= re.sub(' [a]* ',' ',dat)
	dat= re.sub('\s+',' ',dat)
	print('Stage-4 change 3 done')
	sleep(.5)
	#print(dat)
	
	dat=dat.replace(' d ','\'d ')
	dat=dat.replace(' t ','\'t ')
	dat=dat.replace(' m ','\'m ')
	dat=dat.replace(' re ','\'re ')
	dat=dat.replace(' d ','\'d ')
	dat=dat.replace(' ll ','\'ll ')'''
	dat=re.findall('[a-z]+[\'\-]?[a-z]*',dat)
	print('Stage-3 full list creation done')
	sleep(.5)
	#print(len(dat))
	dat1 = list(dict.fromkeys(dat))
	dat1.sort()
	print('Stage-4 unique list creation done')
	#sleep(.5)
	val = collections.Counter(dat)
	print('Stage-5 counting done')
	#sleep(.5)
	#del data
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
	
	t1= Thread(target=distribute, args=(dat1[::10],min_len))
	t2= Thread(target=distribute, args=(dat1[1::10],min_len))
	t3= Thread(target=distribute, args=(dat1[2::10],min_len))
	t4= Thread(target=distribute, args=(dat1[3::10],min_len))
	t5= Thread(target=distribute, args=(dat1[4::10],min_len))
	t6= Thread(target=distribute, args=(dat1[5::10],min_len))
	t7= Thread(target=distribute, args=(dat1[6::10],min_len))
	t8= Thread(target=distribute, args=(dat1[7::10],min_len))
	t9= Thread(target=distribute, args=(dat1[8::10],min_len))
	t10= Thread(target=distribute, args=(dat1[9::10],min_len))
	
	print('Stage-6 multi-task creation done')
	
	sleep(.5)
	
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
	
	rem.sort(reverse=True)
	print(rem)
	print('Total words-',len(dat))
	print('Total unique words-',len(dat1))
	with open('output for method.txt','w') as f:
		f.write('References:\nTotal words-'+str(len(dat))+'\nTotal unique words-'+str(len(dat1))+'\nTotal books-'+str(len(on))+'\n')
		for a in on:
			f.write(a+'\n')
		f.write('\n\n=================\n\n')
		for i, j in rem:
			f.write(str(i)+'=\t\t'+str(j)+'\n')
trend(mypath)
		
		