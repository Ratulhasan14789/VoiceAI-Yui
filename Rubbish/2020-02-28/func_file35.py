#all functions
"UNCOMMENT THE FOLLoWING WHEN CODE DONE!!!"
#if __name__!='__main__:
if None==None:
	import datetime
	from os import system
	from platform import system as os_name
	from time import sleep,time as time_on
	from threading import Thread
	from conversation2 import *
	import sys
	import re
	from web_link import *
	from hashlib import md5
	from urllib.request import urlopen
	import urllib.request #used to make requests
	import urllib.parse #used to parse values into the url
	audionum='0'

def check_installed(x):
	import importlib.util
	spam_loader = importlib.util.find_spec(x)
	found = spam_loader is not None
	return found

def check_internet():
	try:
		response = urlopen('https://www.google.com/', timeout=10)
		return True
	except:
		return False


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

not_installed=[]

def install(pack):
	global not_installed
	"Just install package"
	import subprocess
	import sys
	if check_internet()==True:
		try:
			subprocess.call([sys.executable, "-m", "pip", "install", pack])
		except:
			subprocess.call([sys.executable, "-m", "pip", "install",'--user', pack])
	else:
		print('Failed!')
		not_installed.append(pack)

def upgrade(pack):
	"Upgrades a package"
	import subprocess
	import sys
	if check_internet()==True:
		try:
			subprocess.call([sys.executable, "-m", "pip", "install","--upgrade", pack])
		except:
			subprocess.call([sys.executable, "-m", "pip", "install","--upgrade",'--user', pack])
	else:
		print('Failed!')

def ins_frm_imp(frm,imp,aas = ''):
	if aas=='':
		aas=imp
	importbit=0
	"Install and import package"
	import importlib
	try:
		globals()[aas] = getattr(__import__(frm, globals(), locals(), [imp], 0), imp)
	except ImportError:
		print(frm,"is missing. Do you want to download it from here?\n*Data charge may apply*")
		permit=input("Yes or no?? *If no some error will occur*\n")
		while permit not in cond:
			permit=input(condERR)
			permit=permit.lower()
		if permit in cond:
			if permit in yes:
				install(frm)
			else:
				print("\033[1;31;40m*Some error may occur & the program will break!*\033[0;37;40m")

				importbit=1
	finally :
		if importbit==0:
			globals()[aas] = getattr(__import__(frm, globals(), locals(), [imp], 0), imp)

def ins_n_imp(pack, aas=''):
	global importbit
	"Install and import package"
	importbit=0
	if aas=='':
		aas=pack
	import importlib
	try:
		globals()[aas] = importlib.import_module(pack)
	except ImportError:
		print('\n',pack,"is missing. Do you want to download it from here?\n*Data charge may apply*")
		permit=input("Yes or no?? *If no some error will occur*\n")
		while permit not in cond:
			permit=input(condERR)
			permit=permit.lower()
		if permit in cond:
			if permit in yes:
				install(pack)
			else:
				print("\033[1;31;40m*Some error will occur & the program will break!*\033[0;37;40m")
				importbit=1
				if pack=='pyttsx3':
					importbit=2
				elif pack=='gtts':
					importbit=3
	finally:
		if importbit==0:
			globals()[aas] = importlib.import_module(pack)

def tnt_helper(text,bit):
	if re.search('\|\$.*\|\|.*\$\|',text):
		a=re.findall('\|\$.*\|\|.*\$\|',text)
		a1=a[0]
		a2=a1[2:len(a1)-2]
		a3=a2.split('||')
		print(a3)
		if bit=='type':
			text=text.replace(a1,a3[0])
		elif bit=='talk':
			text=text.replace(a1,a3[1])
	text=text.replace('|<','\033[4;34;40m')	#LINK
	text=text.replace('>|','\033[0;37;40m')
	text=text.replace('|?','\033[0;33;40m')	#DID YOU MEAN...?
	text=text.replace('?|','\033[0;37;40m')
	text=text.replace('|!','\033[0;32;40m')	#YES SURE
	text=text.replace('!|','\033[0;37;40m')
	text=text.replace('|-','\033[0;30;40m')	#HIDDEN
	text=text.replace('-|','\033[0;37;40m')
	text=text.replace('|+','\033[0;37;40m')	#BRIGHT
	text=text.replace('+|','\033[0;37;40m')
	text=text.replace('|*','\033[1;37;40m')	#WARNING
	text=text.replace('*|','\033[0;31;40m')
	text=text.replace('|+','\033[1;37;43m')
	text=text.replace('+|','\033[0;37;40m')
	return text


def ins_n_imp_voice():
	global not_installed, vmodule,importbit
	NoVoiceError="\n \n\033[1;31;40mWarning! Voice won't work\n\033[1;37;40m"
	if os_name()=='Windows':
		try:
			ins_n_imp('pyttsx3')
			vmodule='pyttsx3'
			global engine
			if importbit!=2:
				engine = pyttsx3.init()
				# Set properties _before_ you add things to say
				engine.setProperty('rate', 190)
				# Speed percent (can go over 100)
				engine.setProperty('volume', 1)  # Volume 0-1
				en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"

				# Use female English voice
				engine.setProperty('voice', en_voice_id)
			else: raise ValueError
		except ValueError:
			ins_frm_imp('gtts','gTTS')
			if check_installed('gtts')==True:
				vmodule='gtts'
			else:
				print(NoVoiceError)
				vmodule='unav'
	else:
		vmodule='unav'
	return vmodule


vmodule=ins_n_imp_voice()

def speakup(x):
	global vmodule, speakers
	if vmodule=='pyttsx3':
		global engine
		x1=tnt_helper(x,'talk')
		engine.say(x1)
		# Flush the say() queue and play the audio
		engine.runAndWait()

	elif vmodule=='gtts':
		global audionum
		a = gTTS(text=x, lang='en', slow=False)
		name = 'Yui_data/RAM/outvoice' + audionum +'.mp3'
		a.save(name)
		audionum=str(int(audionum) +1)
	else: print(vmodule)
def slowtype(x, y=0.02,ends=''):
	x1=tnt_helper(x,'type')
	for i in x1:
		print(i, end="", flush="True")
		sleep(y)
		print(ends,end='')
def slowtyper(x,y,ends):
	global slowtype,typer
	typer=Thread(target=slowtype, args=(x,y,ends,))
	typer.start()
def tnt(x,y=0.02,ends=''):
	global typer,speakers
	slowtyper(x,y,ends)
	speakup(x)
	typer.join()


def tnt_ff(x,z,y):
	slowtyper(x,y=0.02)
	try:
		playsound( 'Yui_data/ROM/offvoice/outvoice'+ z +'.mp3')
	except:
		pass
def i_slim(ui):
	ui=ui.lower()
	ui=ui.replace("'","")
	ui=ui.replace("?","")
	ui=ui.replace("!","")
	ui=ui.replace(".","")
	ui=ui.replace(",","")
	return ui


def backup(ui):
	uitimes=str(datetime.datetime.now())
	"""Will backup every command by user"""
	with open("Yui_data/RAM/uidb.txt", "a") as uinputdb:
		uinput= uitimes,ui
		uinput=str(uinput)+"\n"
		uinputdb.write(uinput)

exec(open("Yui_data/RAM/pdatas2.py").read())


def locker():
	slowtype("\033[1;37;40mPlease enter your User name: ")
	uName=input()

	while uName=="" or uName!=uiName:
		slowtype("\033[1;31;40mInvalid username!\033[1;37;40m\nPlease RETYPE YOUR USER NAME: ")
		uName=input()

	'''uipw=input("Please enter the Password: ")
	while uipw=="":
		uipw=input("\033[1;31;40mDon't leave this empty. Enter the correct Password. Otherwise you can't run this.\033[1;37;40m N\nEnter the Password: ")
	uipwmd5 = md5(uipw.encode('utf-8')).hexdigest()
	while uipwmd5!=upwmd5:
		uipw = input("\033[1;31;40m*WARNING!*\nYou have entered incorrect Password.\033[1;37;40m\nPlease enter the correct one: ")
		uipwmd5 = md5(uipw.encode('utf-8')).hexdigest()

	for i in range(10):
		sleep(.08)
		if i%3==0:
			x=":=="*12
		elif i%3==1:
			x="=:="*12
		elif i%3==2:
			x="==:"*12
		print("\rLogging in",x, end='',flush=True)
	delthisline()
	print("\n\nLogged in")'''
	return uName

def check_performance():
	start_time=time_on()
	#########To be continued ###########
def edit_pdata(old,new):
	with open("Yui_data/RAM/pdatas2.py","r") as udatafile:
		udataread=udatafile.read()
		filedata = udataread.replace(str(old),str(new))
	with open("Yui_data/RAM/pdatas2.py", "w") as udatanewfile:
		udatanewfile.write(filedata)

def asker():
	from conversation2 import yes, no, condERR, cond
	Ques2=input()
	Ques2=Ques2.lower()
	while Ques2 not in cond:
		tnt(condERR)
		Ques2=input()
		Ques2=Ques2.lower()
	if Ques2 in cond:
		if Ques2 in yes:
			return True
		else:
			return False

if 0==0:
	ins_n_imp('wikipedia')
	#ins_n_imp('ipinfo')



def wikisearch(uix):
	import wikipedia
	if check_internet()==True:
		if uix in [i.lower() for i in wikipedia.search(uix)]:
			tnt('\n'+wikipedia.summary(uix, sentences=5))
			tnt('\nDo you want to know some more?')
			q=asker()
			if q==True:
				ny = wikipedia.page(uix)
				web_go(ny.url)
		elif wikipedia.search(uix)!=[]:
			tnt('Did you mean '+ wikipedia.search(uix)[0]+'?')
			q=asker()
			if q==True:
				tnt('\n'+wikipedia.summary(wikipedia.search(uix)[0], sentences=5))
				tnt('\nDo you want to know some more?  ')
				q=asker()
				if q==True:
					ny = wikipedia.page(uix)
					web_go(ny.url)
		else:
			tnt("\nCouldn't find "+uix+"!\nWould you like to search instead?  ")
			q=asker()
			if q==True:
				searcher(uix)
			else:
				tnt('\nOk then.')
	else: tnt('No internet connection!')

def go_youtube(ui):
	domain = command.split("youtube",1)[1]
	query_string = urllib.parse.urlencode({"search_query" : domain})
	html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
	search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode()) # finds all links in search result
	webbrowser.open("http://www.youtube.com/watch?v={}".format(search_results[0]))
	pass
