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
exec(alpha)
def wikiupt(x):
	for itt in x:
		bits=1
		itt1 =wikipedia.search(itt[0])[0].lower()
		if itt[0] in [i.lower() for i in wikipedia.search(itt[0])]:
			dat=wikipedia.page(itt[0])
			data= '"""/_/+'+dat.title+'=/\n'+wikipedia.summary(itt[0], sentences=5)+'"""'
			out='data= '+data+'\nlink= """'+dat.url+'"""'
		elif wikipedia.search(itt[0])!=[]:
			if itt1 in itt:
				dat=wikipedia.page(itt[0])
				data= '"""/_/+'+dat.title+'=/\n'+wikipedia.summary(itt[0], sentences=5)+'"""'
				out='data= '+data+'\nlink= """'+dat.url+'"""'
			else:
				print('Did you mean '+ wikipedia.search(itt[0])[0]+'?')
				q=asker()
				if q==True:
					with open("Yui_data/ROM/wikiupdate.py", 'w') as beta:
						beta1 =alpha.replace(itt[0],itt1+"', '"+itt[0])
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
	num=0
	bits=0
	for item in wiki_dbs:
		exec( "t%d= Thread(target=wikiupt,args=(%s,))"%(num,item))
		exec('t%d.start()'%num)
		num+=1
	while bits<num:
		exec('t%d.join()'%bits)
		bits+=1
if check_internet():
	wikiup()
