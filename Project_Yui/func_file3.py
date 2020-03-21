#all functions
if 0==0:
	import datetime
	from os import system
	from platform import system as os_name
	from time import sleep,time as time_on
	from threading import Thread
	from conversation2 import *
	import sys
	from web_link import *
	from hashlib import md5
	from urllib.request import urlopen

def check_installed(x):
	import importlib
	spam_loader = importlib.find_loader(x)
	found = spam_loader is not None

def internet_on():
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

def install(pack):
	"Just install package"
	import subprocess
	import sys
	if internet_on()==True:
		subprocess.call([sys.executable, "-m", "pip", "install","--user", pack])
	else:
		print('Failed!')

def upgrade(pack):
	"Upgrades a package"
	import subprocess
	import sys
	if internet_on()==True:
		subprocess.call([sys.executable, "-m", "pip", "install","--upgrade","--user", pack])
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
		print(pack,"is missing. Do you want to download it from here?\n*Data charge may apply*")
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





def ins_n_imp_voice():
	global voice_up
	voice_up=1
	ins_n_imp('pyttsx3')
	if importbit==0:
		voice_up=0
		global engine
		engine = pyttsx3.init()
	# Set properties _before_ you add things to say
		engine.setProperty('rate', 190)	# Speed percent (can go over 100)
		engine.setProperty('volume', 0.9)  # Volume 0-1
		en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"

		# Use female English voice
		engine.setProperty('voice', en_voice_id)
	else:
		ins_frm_imp('gtts','gTTS')
		if importbit==0:
			ins_frm_imp('playsound','playsound')
			if importbit!=0: tnt("Warning! Voice won't work")
		else:
			tnt("Warning! Voice won't work")



def speakup(x):
	global n, engine, voice_up,speakers
	global voice_up,n
	if voice_up==0:
		engine.say(x)
		# Flush the say() queue and play the audio
		engine.runAndWait()

	else:
		if importbit==0:
			a = gTTS(text=x, lang=language, slow=False)
			name = 'Yui_data/RAM/outvoice' + n +'.mp3'
			a.save(name)
			playsound(name)
			n=str(int(n)+1)
def slowtype(x, y,ends):
	for i in x:
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
		uinput= uitimes,"	"+ui
		uinput=str(uinput)+"\n"
		uinputdb.write(uinput)

def locker():

	with open("Yui_data/RAM/pdatas.txt","r") as udatafile:
		uiName=udatafile.readline()
		aiName=udatafile.readline()
		upwmd5=udatafile.readline()
	aiName=aiName[2:len(aiName)-1]
	uiName=uiName[2:len(uiName)-1]
	upwmd5=upwmd5[2:len(upwmd5)-1]
	uName=input("\033[1;37;40mPlease enter your User name: ")

	while uName=="" or uName!=uiName:
		uName=input("\033[1;31;40mInvalid username!\033[1;37;40m\nPlease RETYPE YOUR USER NAME: ")

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
	DAT=[aiName, uName]
	return DAT

def check_performance():
	start_time=time_on()
	#########To be continued #############

