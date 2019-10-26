'''import tkinter # note that module name has changed from Tkinter in Python 2 to tkinter in Python 3
top = tkinter.Tk()
# Code to add widgets will go here...
top.mainloop()'''


'''# !/usr/bin/python3
from tkinter import *

from tkinter import messagebox

top = Tk()
top.geometry("100x100")
def helloCallBack():
   msg = messagebox.showinfo( "Warning!", "Hello World")

B = Button(top, text = "Hello", command = helloCallBack)
B.place(x = 50,y = 50)
top.mainloop()'''

'''# !/usr/bin/python3
from tkinter import *

from tkinter import messagebox

top = Tk()

C = Canvas(top, bg = "blue", height = 720, width = 480)

coord = 100, 50, 40, 210
arc = C.create_arc(coord, start = 0, extent = 150, fill = "red")
line = C.create_line(10,10,200,200,fill = 'white')
C.pack()
top.mainloop()'''

'''#!/usr/bin/python3

from PyQt5.QtCore import QDate, QTime, QDateTime, Qt

now = QDate.currentDate()

print(now.toString(Qt.ISODate))
print(now.toString(Qt.DefaultLocaleLongDate))

datetime = QDateTime.currentDateTime()

print(datetime.toString())

time = QTime.currentTime()

print(time.toString(Qt.DefaultLocaleLongDate))'''

'''import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 image - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create widget
        label = QLabel(self)
        pixmap = QPixmap('image.jpg')
        label.setPixmap(pixmap)
        self.resize(pixmap.width(),pixmap.height())

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())'''

from threading import Thread
import datetime
from os import system
from platform import system as os_name
from time import sleep
import sys


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

def install(package):
	"Just install package"
	import subprocess
	import sys
	subprocess.call([sys.executable, "-m", "pip", "install", package])



import pyttsx3
def ins_n_imp_voice():
	global voice_up
	voice_up=0
	print(os_name())
	if os_name() == 'Windows':
		install('pypiwin32')
		delprevline()
		delprevline()
		delprevline()
		ins_n_imp("pyttsx3")
	# One time initialization
	elif os_name()=='Darwin':
		install('nsss')
		delthisline()
		ins_n_imp('pyttsx3')
	elif os_name()=='Linux':
		install('espeak')
		delthisline()
		ins_n_imp('pyttsx3')
	global engine
	engine = pyttsx3.init()
	# Set properties _before_ you add things to say
	engine.setProperty('rate', 150)	# Speed percent (can go over 100)
	engine.setProperty('volume', 0.9)  # Volume 0-1
ins_n_imp_voice()

def speakx(x):
	global voice_up
	global n
	if voice_up==0:
		engine.say(x)
		# Flush the say() queue and play the audio
		engine.runAndWait()

	else:
		 a = gTTS(text=x, lang=language, slow=False)
		 name = 'Yui_data/RAM/outvoice' + n +'.mp3'
		 a.save(name)
		 playsound(name)
		 n=str(int(n)+1)


def speakup(x):
	global n, engine, voice_up
	speakers=Thread(target=speakx, args=(x,))
	speakers.start()
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
	global typer
	slowtyper(x,y,ends)
	speakup(x)
	typer.join()


def tnt_ff(x,z,y):
	slowtyper(x,y=0.02)
	try:
		playsound( 'Yui_data/ROM/offvoice/outvoice'+ z +'.mp3')
	except:
		pass

tnt('HI')
