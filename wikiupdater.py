from func_file37 import install, check_internet,asker
install('wikipedia')
def t_rev(x):
	y=[i for i in x]
	y=y[::-1]
	x=()
	for i in y:
		x+=(i,)
	return x
def t2s(x):
	s="('"
	for i in x:
		s+=i+"', '"
	s+='\b)'
	return s

import wikipedia
with open("Yui_data/ROM/wikiupdate.py") as adata:
	alpha= adata.read()
print(alpha)
exec(alpha)
def wikiupt(x):
	for itt in x:
		bits=1
		if itt[0] in [i.lower() for i in wikipedia.search(itt[0])]:
			dat=wikipedia.page(itt[0])
			data= '"""/_/+'+dat.title+'=/\n'+wikipedia.summary(itt[0], sentences=5)+'"""'
			out='data= '+data+'\nlink= """'+dat.url+'"""'
		elif wikipedia.search(itt[0])!=[]:
			print('Did you mean '+ wikipedia.search(itt[0])[0]+'?')
			q=asker()
			if q==True:
				itt1 =wikipedia.search(itt[0])[0].lower()
				print(itt1)
				with open("Yui_data/ROM/wikiupdate.py", 'w') as beta:
					beta1 =alpha.replace(itt[0],itt1+"', '"+itt[0])
					print(beta1)
					beta.write(beta1)

				dat=wikipedia.page(wikipedia.search(itt[0])[0])
				data= '"""/_/+'+dat.title+'=/\n'+wikipedia.summary(wikipedia.search(itt[0])[0], sentences=5)+'"""'
			out='data= '+data+'\nlink= "'+dat.url+'"'
		else:
			bits=0

		with open('Yui_data/ROM/WikiOFF/'+itt[0]+'.wiki','w') as f:
			if bits==1:
				f.write(out)
				print(itt,'done')
			else: print(itt,'not found')
def wikiup():
	from threading import Thread
	
	#t1=Thread(target=wikiupt,args=(wiki_person,))
	#t2=Thread(target=wikiupt,args=(wiki_object,))
	#t3=Thread(target=wikiupt,args=(wiki_topic,))
	#t4=Thread(target=wikiupt,args=(wiki_place,))
	t5=Thread(target=wikiupt,args=(wiki_relig,))
#	t1.start()
#	t2.start()
#	t3.start()
#	t4.start()
	t5.start()
#	t1.join()
#	t2.join()
#	t3.join()
#	t4.join()
	t5.join()

if check_internet():
	wikiup()
print(wiki_person)