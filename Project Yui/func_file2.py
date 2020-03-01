#all functions
if 0==0:
	import datetime
	from os import system
	from platform import system as os_name
	from time import sleep
	from threading import Thread
	from conversation2 import *
	import sys
	from web_link import *

def delprevline():
	"Use this function to delete the last line in the STDOUT"

	#cursor up one line
	sys.stdout.write('\x1b[1A')

	#delete last line
	sys.stdout.write('\x1b[2K')


def delthisline():
	#Use this to delete current line
	sys.stdout.write('\x1b[2K')

def clear():
	# for windows
	if os_name == 'nt':
		_ = system('cls')
	# for mac and linux(here, os.name is 'posix')
	else:
		_ = system('clear')

def ins_frm_imp(frm,imp,aas = ''):
	if aas=='':
		aas=imp
	global importbit
	importbit=''
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
				import subprocess
				import sys
				subprocess.call([sys.executable, "-m", "pip", "install", frm])

			else:
				print("\033[1;31;40m*Some error may occur & the program will break!*\033[0;37;40m")

				importbit=frm
	finally :
		if importbit!=frm:
			globals()[aas] = getattr(__import__(frm, globals(), locals(), [imp], 0), imp)

def ins_n_imp(pack, aas=''):
	"Install and import package"
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
				import subprocess
				import sys
				subprocess.call([sys.executable, "-m", "pip", "install", pack])
			else: print("\033[1;31;40m*Some error will occur & the program will break!*\033[0;37;40m")

	finally:
		globals()[aas] = importlib.import_module(pack)

def install(package,aas):
	"Just install package"
	import subprocess
	import sys
	subprocess.call([sys.executable, "-m", "pip", "install", package])
def ins_n_imp_voice():
	global voice_up
	voice_up=0
	try:
		if os_name() == 'Windows':
			try:
				import pypiwin32
			except:
				install(pypiwin32)
			delthisline()
			ins_n_imp("pyttsx3")
			# One time initialization
		elif os_name()=='Darwin':
			install('nsss')
			ins_n_imp('pyttsx3')
		elif os_name()=='Linux':
			install('espeak')
			ins_n_imp('pyttsx')
		global engine
		engine = pyttsx3.init()
		# Set properties _before_ you add things to say
		engine.setProperty('rate', 150)	# Speed percent (can go over 100)
		engine.setProperty('volume', 0.9)  # Volume 0-1
	except:
		global n
		ins_frm_imp('gtts','gTTS')
		ins_frm_imp('playsound','playsound')
		language = 'en'
		n='0'
		voice_up=1
def speakx(x):
	if voice_up==5:
		engine.say(x)
		# Flush the say() queue and play the audio
		engine.runAndWait()
		if x.endswith("   "):
			sleep(3)
		elif x.endswith('  '):
			sleep(2)
		elif x.endswith(' '):
			sleep(1)
		else:
			sleep(1.5)
	else:
		 try:
			 a = gTTS(text=x, lang=language, slow=False)
			 name = 'Yui_data/RAM/outvoice' + n +'.mp3'
			 a.save(name)
			 playsound(name)
			 n=str(int(n)+1)
		 except:
			  pass


def speakup(x):
	global n, engine, voice_up
	if '\n' in x:
		x1=x
		x2=x1.split('\n')
		for i in x2:
			speakers=Thread(target=speakx, args=(i))
	else:
		speakers=Thread(target=speakx, args=(x))
	speakers.start()
def slowtype(x, y=0.02):
	for i in x:
		print(i, end="", flush="True")
		sleep(y)
def slowtyper(x,y=0.02):
	global slowtype,typer
	typer=Thread(target=slowtype, args=(x,y,))
	typer.start()
def tnt(x,y=0.01,ends="\n"):
	global typer
	slowtyper(x,y,end)
	speakup(x)
	#typer.join()
	print(ends,end="")

def tnt_ff(x,z,y):
	slowtyper(x,y=0.02)
	try:
		playsound( 'Yui_data/ROM/offvoice/outvoice'+ z +'.mp3')
	except:
		print('',end='')
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
