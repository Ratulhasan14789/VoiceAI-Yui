#pylint:disable=W0312
#https://pastebin.com/kHwxfQxm

import datetime
from os import system, makedirs, getcwd
from os.path import exists, isdir, isfile, basename, splitext
from time import sleep,time as time_on
import sys
import re
from hashlib import md5
from platform import system as os_name

admin='9dd4e461268c8034f5c8564e155c67a6'

wikiOffVersion=0.1
wiki_person=[('Muhammad', 'islam prophet'), ('Bill Gates', 'Big bill')]
wiki_place=[('Saudi Arab', 'Arab'), ('New york', 'nyc', 'new york city')]
wiki_object=[('al quran', 'holy quran'), ('noble prize', 'nobel prize')]
wiki_topic=[('binary'), ('computer'), ('python'),('islam', 'peace'), ('allah'), ('hindu')]

def loc(x):
	'''to fix dir problem'''
	if os_name().lower()=='windows':
		return x.replace('/','\\')
	else:
		return x.replace('\\','/')

def writer(locs,fname,mode,data,bit=0):
	if dir==0:
		with open(fname,mode) as file:
			file.write(data)
	else:
		if isdir(locs):
			if locs.endswith('/'):
				with open(loc(locs+fname),mode) as f:
					f.write(data)
			else:
				with open(loc(locs+'/'+fname),mode) as f:
					f.write(data)
		else:
			makedirs(loc(locs))
			writer(locs,fname,mode,data,bit)
#asdf='aaddffghhjjkl'
#writer('temp_yui_data/crack/c','aa.txt','w',asdf)
def delprevline():
	"Use this function to delete the last line in the STDOUT"

	#cursor up one line
	sys.stdout.write('\x1b[1A')

	#delete last line
	sys.stdout.write('\x1b[2K')


def delthisline():
	#Use this to delete current line
	sys.stdout.write('\x1b[2K')

def clean():
	# for windows
	if os_name() == 'Windows':
		_ = system('cls')
	# for mac and linux(here, os.name is 'posix')
	else:
		_ = system('clear')

def tnt_helper(text):
	#pattern [[xx//yy]]
	if '//' in text:
		while re.search('\[\[([^(//)]*)//([^(\]\])]*)\]\]',text):
			a= re.search('\[\[([^(//)]*)//([^(\]\])]*)\]\]',text)
			text= text.replace(a.group(0),a.group(1))
	while re.search('==(.*)==',text):
			a=re.search('===([^(==)]*)===',text)
			if a:
				text =text.replace(a.group(0),'/hu/'+a.group(1)+'/=/')
			a=re.search('==([^(==)]*)==',text)
			if a:
				text =text.replace(a.group(0),'/u/'+a.group(1)+'/=/')
	text=text.replace('/u/','/h/\033[4;37;40m') #UNDERLINE
	text=text.replace('/a/','\033[4;34;40m')	#LINK
	text=text.replace('/y/','\033[0;33;40m')	#DID YOU MEAN...?
	text=text.replace('/g/','\033[1;32;40m')	#YES SURE
	text=text.replace('/k/','\033[0;30;40m')	#HIDDEN
	text=text.replace('/b/','\033[1;37;40m')	#BRIGHT
	text=text.replace('/r/','\033[1;31;40m')	#WARNING
	text=text.replace('/h/','\033[1;30;43m') #HIGHLIGHT
	text=text.replace('/hu/','\033[0;37;40m\033[4;30;43m')  #Highlight+Underline
	text=text.replace('/=/','\033[0;37;40m\033[1;37;40m')
	return text

def slowtype(txt, y=0.02,ends=''):
	x1=tnt_helper(txt)
	for i in x1:
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
	user=inputer('Enter your username: ')
	if user=='rf':
		run=True
		uname='Rafi'
		slowtype('Welcome!\n')
		break
	elif  md5(user.encode('utf-8')).hexdigest()==admin:
		run=True
		uname='Ratul'
		break
while run==True:
	typex=inputer('/=/What type of data you wish to enter\n(person</g/p/=/>, \t\tonly type\n place</g/pl/=/>, \t\tthe /g/green/=/\n topic</g/t/=/>, \t\ttext\n object</g/ob/=/>): ')
	if typex in ['p','pl','t','ob','s']:
		add_dat(typex)
	else:
		slowtype("/y/I can't understand what you said?/=/\nPlease retry.\n")

