from time import sleep
wikiOffVersion=0.1
wiki_person=[('Muhammad', 'islam prophet'), ('Bill Gates', 'Big bill')]
wiki_place=[('Saudi Arab', 'Arab'), ('New york', 'nyc', 'new york city')]
wiki_object=[('al quran', 'holy quran'), ('noble prize', 'nobel prize')]
wiki_topic=[('binary'), ('computer'), ('python')]
wiki_relig=[('islam', 'peace'), ('allah'), ('hindu')]

def slowtype(x, y=0.02,ends=''):
	for i in x:
		print(i, end="", flush="True")
		sleep(y)
		print(ends,end='')
def inputer(x):
	slowtype(x)
	return input()
def add_dat(x):
	print(x)
while True:
	try:
		if reload==True: break
	except:
		pass
	if inputer('Enter your username: ')=='rf':
		run=True
		uname='Rafi'
		break
while run==True:
	typex=inputer('What type of data you wish to enter(person<p>, place<pl>, topic<t>, object<ob>, religious topic<rel>): ')
	if typex in ['p','pl','t','ob','rel']:
		add_dat(typex)
	else:
		slowtype("I can't understand what you said? Please retry.\n")

