from func_file37 import install
install('wikipedia')
import wikipedia
exec(open("Yui_data/ROM/wikiupdate.py").read())
def wikiupt(x):
	for i in x:
		dat=wikipedia.page(i[0])
		data='/_/+'+dat.title+'=/\n'+wikipedia.summary(i[0], sentences=5)
		out='data= "'+data+'\nlink= "'+dat.url+'"'
		with open('Yui_data/ROM/WikiOFF/'+i[0]+'.wiki','w') as f:
			f.write(out)
def wikiup():
	from threading import Thread
	
	t1=Thread(target=wikiupt,args=(wiki_person,))
	t2=Thread(target=wikiupt,args=(wiki_object,))
	t3=Thread(target=wikiupt,args=(wiki_topic,))
	t4=Thread(target=wikiupt,args=(wiki_place,))
	t5=Thread(target=wikiupt,args=(wiki_relig,))
	t1.start()
	t2.start()
	t3.start()
	t4.start()
	t5.start()
	t1.join()
	t2.join()
	t3.join()
	t4.join()
	t5.join()

wikiup()
print(wiki_person)