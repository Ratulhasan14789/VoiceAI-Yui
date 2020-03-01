#pylint:disable=C0103
#pylint:disable=W0312
#	#tab
Vcode = ""
func_ver='37'
#*************************************************
#						This code was created by Ratul Hasan
#						  So comlpete credit goes to him(me)
#*************************************************
#		 Sharing this code without my permission is not allowed
#*************************************************
# This code was created based on IDLE, Pydroid(Android), qPython(Android) etc. So most online/web site based idle(i.e: Sololearn) can't run this code properly.
#*************************************************
# If there is any error or you want to help please let me know.
#e-mail: wwwqweasd147@gmail.com
#*************************************************
try:	#to check if the file is reloaded or not
	if reloader==True:
		reloaded=True
except NameError:
	reloaded=False
	reloader=False
ai_import=True


#exec(reader('func_file'+func_ver+'.py'))

############################
##--------##func-file##start------------####
############################
#all functions
"UNCOMMENT THE FOLLoWING WHEN CODE DONE!!!"
#if __name__!='__main__:

if None==None:
	import datetime
	from os import system, makedirs, getcwd
	from os.path import exists, isdir, isfile, basename, splitext
	from time import sleep,time as time_on
	from threading import Thread
	from conversation21 import *
	import sys
	import re
	from web_link import *
	from hashlib import md5
	from urllib.request import urlopen
	import urllib.request #used to make requests
	import urllib.parse #used to parse values into the url
	from platform import system as os_name

	audionum='0'
	
def loc(x):
	'''to fix dir problem'''
	if os_name().lower()=='windows':
		return x.replace('/','\\')
	else:
		return x.replace('\\','/')

def reader(x):
	with open(loc(x)) as f:
		return f.read()

def backup(ui):
	uitimes=str(datetime.datetime.now())
	"""Will backup every command by user"""
	with open(loc("Yui_data/RAM/uidb.txt"), "a") as uinputdb:
		uinput= uitimes,ui
		uinput=str(uinput)+"\n"
		uinputdb.write(uinput)


def cmdrun(x,y=None):
	import subprocess
	a=x.split()
	if y!=None: print(y)
	p= subprocess.run(a, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	return p.stdout.decode('utf-8')
	

#exec( reader('Yui_data/brain/brain.py'))
############################
####------##brain##start##--------#####
############################

def tnt(x=None,y=None,z=None):
	#defined later, only to remove red lines
	pass
def check_installed(pkz):
	import importlib.util
	spam_loader = importlib.util.find_spec(pkz)
	found = spam_loader is not None
	return found

def get_version(package):
	from pip._vendor import pkg_resources
	package = package.lower()
	return next((p.version for p in pkg_resources.working_set if p.project_name.lower() == package), "No match")

def check_internet():
	try:
		response = urlopen('https://www.google.com/', timeout=10)
		return True
	except:
		return False

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

def tnt_helper(text,bit=0):
	#pattern [[xx//yy]]
	if '//' in text:
		while re.search('\[\[([^(//)]*)//([^(\]\])]*)\]\]',text):
			a=re.search('\[\[([^(//)]*)//([^(\]\])]*)\]\]',text)
			if bit=='talk':
				text=text.replace(a.group(0),a.group(2))
			elif bit=='type':
				text=text.replace(a.group(0),a.group(1))
	while re.search('==(.*)==',text):
			a=re.search('===([^(==)]*)===',text)
			if a:
				text =text.replace(a.group(0),'/hu/'+a.group(1)+'/=/')
			a=re.search('==([^(==)]*)==',text)
			if a:
				text =text.replace(a.group(0),'/u/'+a.group(1)+'/=/')
	text=text.replace('/u/','/h/\033[4;37;40m')	#UNDERLINE
	text=text.replace('/a/','\033[4;34;40m')	#LINK
	text=text.replace('/y/','\033[0;33;40m')	#DID YOU MEAN...?
	text=text.replace('/g/','\033[0;32;40m')	#YES SURE
	text=text.replace('/k/','\033[0;30;40m')	#HIDDEN
	text=text.replace('/b/','\033[1;37;40m')	#BRIGHT
	text=text.replace('/r/','\033[1;31;40m')	#WARNING
	text=text.replace('/h/','\033[1;30;43m') #HIGHLIGHT
	text=text.replace('/hu/','\033[0;37;40m\033[4;30;43m')  #Highlight+Underline
	text=text.replace('/=/','\033[0;37;40m\033[1;37;40m')
	return text

def slowtype(txt, y=0.02,ends=''):
	x1=tnt_helper(txt,'type')
	for i in x1:
		print(i, end="", flush="True")
		sleep(y)
		print(ends,end='')

def slowtyper(txt,y,ends):
	global typer
	typer=Thread(target=slowtype, args=(txt,y,ends,))
	typer.start()

not_installed=[]

def install(pack):
	#Just install package
	global not_installed
	import subprocess
	if check_installed(pack)==True:
		slowtype('Already installed')
	elif check_internet()==True:
		subprocess.call([sys.executable, "-m", "pip", "install", pack])
		if check_installed(pack)==False:
			subprocess.call([sys.executable, "-m", "pip", "install",'--user', pack])
	else:
		slowtype('/r/Failed! \nPossible cause: No internet connection./=/\n')
		not_installed.append(pack)

#install('"pip/wikipedia-140.tar.gz"')
def upgrade(pack):
	"Upgrades a package"
	import subprocess
	if check_internet()==False:
		try:
			subprocess.call([sys.executable, "-m", "pip", "install","--upgrade", pack])
		except:
			subprocess.call([sys.executable, "-m", "pip", "install","--upgrade",'--user', pack])
	else:
		slowtype('/r/Failed! \nPossible cause: No internet connection./=/\n')

def ins_frm_imp(frm,imp,aas = ''):
	if aas=='':
		aas=imp
	importbit=0
	"Install and import package"
	import importlib
	try:
		globals()[aas] = getattr(__import__(frm, globals(), locals(), [imp], 0), imp)
	except ImportError:
		slowtype(frm,"is missing. Do you want to download it from here?\n*Data charge may apply*")
		permit=input("/r/Yes or no?? *If no some error will occur*/=/\n")
		while permit not in cond:
			permit=input(condERR)
			permit=permit.lower()
		if permit in cond:
			if permit in yes:
				install(frm)
			else:
				slowtype("\033[1;31;40m*Some error may occur & the program will break!*\033[0;37;40m")

				importbit=1
	finally :
		if importbit==0:
			globals()[aas] = getattr(__import__(frm, globals(), locals(), [imp], 0), imp)
	del importlib

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
		slowtype('\n',pack,"is missing. Do you want to download it from here?\n*Data charge may apply*")
		permit=input("Yes or no?? *If no some error will occur*\n")
		while permit not in cond:
			permit=input(condERR)
			permit=permit.lower()
		if permit in cond:
			if permit in yes:
				install(pack)
			else:
				slowtype("/r/*Some error will occur & the program will break!*/=/")
				importbit=1
				if pack=='pyttsx3':
					importbit=2
				elif pack=='gtts':
					importbit=3
	finally:
		if importbit==0:
			globals()[aas] = importlib.import_module(pack)
	del importlib

def compress(file_names):
	import zlib
	import zipfile
	#print("File Paths:")
	#print(file_names)

	path = getcwd()+'/'

	# Select the compression mode ZIP_DEFLATED for compression
	# or zipfile.ZIP_STORED to just store the file
	compression = zipfile.ZIP_DEFLATED

	# create the zip file first parameter path/name, second mode
	zf = zipfile.ZipFile("RAWs.zip", mode="w")
	try:
		for file_name in file_names:
			# Add file to the zip file
			# first parameter file to zip, second filename in zip
			zf.write(path + file_name, file_name, compress_type=compression)

	except FileNotFoundError:
		print("/r/An error occurred/=/")
	finally:
		# Don't forget to close the file!
		zf.close()
	#file_names= ["brain.py", "voice.py"]
	#compress(file_names)
	del zipfile, zlib

#############################
####---------##brain##end##--------#####
#############################
exec( reader('Yui_data/brain/voice.py'))
exec( reader("Yui_data/RAM/pdatas2.py"))

Vcode=splitext(basename(__file__))[0]

def curr_dir():
	#current directory
	return getcwd().replace('\\','/')

def i_slim(ui):
	ui=ui.lower()
	ui=ui.replace("'","")
	ui=ui.replace("?","")
	ui=ui.replace("!","")
	ui=ui.replace(".","")
	ui=ui.replace(",","")
	return ui

def inputer(x=''):
	tnt(x)
	a=True
	while a==True:
		try:
			y=input()
			a=False
		except UnicodeDecodeError:
			tnt('/r/*invalid input!/=/\nPlease re-type correctly:  ')
	del a,x
	backup(y)
	return y
def locker():
	ins_n_imp('wikipedia')
	#ins_n_imp('ipinfo')
	slowtype("\033[1;37;40mPlease enter your User name: ")
	uName=inputer()

	while uName=="" or uName!=uiName:
		slowtype("/r/Invalid username!/=/\nPlease RETYPE YOUR USER NAME: ")
		uName=inputer()

	'''uipw=inputer("Please enter the Password: ")
	while uipw=="":
		uipw=inputer("\033[1;31;40mDon't leave this empty. Enter the correct Password. Otherwise you can't run this.\033[1;37;40m N\nEnter the Password: ")
	uipwmd5 = md5(uipw.encode('utf-8')).hexdigest()
	while uipwmd5!=upwmd5:
		uipw = inputer("\033[1;31;40m*WARNING!*\nYou have entered incorrect Password.\033[1;37;40m\nPlease enter the correct one: ")
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
	#######To be continued #########
def edit_pdata(old,new):
	with open(loc("Yui_data/RAM/pdatas2.py")) as udatafile:
		udataread=udatafile.read()
		filedata = udataread.replace(str(old),str(new))
	with open(loc("Yui_data/RAM/pdatas2.py"), "w") as udatanewfile:
		udatanewfile.write(filedata)

def asker(out=''):
	tnt(out)
	Ques2=inputer()
	Ques2=Ques2.lower()
	while Ques2 not in cond:
		tnt(condERR)
		Ques2=inputer()
		Ques2=Ques2.lower()
	if Ques2 in cond:
		if Ques2 in yes:
			return True
		else:
			return False

def wikisearch(uix):
	if check_internet()==True and check_installed('wikipedia')==True:
		import wikipedia
		if uix in [i.lower() for i in wikipedia.search(uix)]:
			tnt('\n'+wikipedia.summary(uix, sentences=4))
			tnt('\nDo you want to know some more? ')
			q=asker()
			if q==True:
				ny = wikipedia.page(uix)
				web_go(ny.url)
		elif wikipedia.search(uix)!=[]:
			tnt('Did you mean '+ wikipedia.search(uix)[0]+'? ')
			q=asker()
			if q==True:
				tnt('\n'+wikipedia.summary(wikipedia.search(uix)[0], sentences=4))
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
	elif check_internet()==False:
		tnt('No internet connection!')
	elif check_installed('wikipedia')==False:
		if check_internet()==True:
			tnt('You need to install Wikipidia for that type of commands.')
			ins_n_imp('wikipedia')
			if check_installed('wikipedia')==True:
				wikisearch(uix)
			else:
				tnt("Sorry I can't show you the results without wikipedia.\n")

def find_person(txt):
	wikisearch(txt)
	#tnt("Can't find him")

def tell_time():
	nowits=datetime.datetime.now()
	tnt(random.choice(li_tell_time2)+nowits.strftime("%I:%M %p."))

def go_youtube(ui):
	domain = ui.split("youtube",1)[1]
	query_string = urllib.parse.urlencode({"search_query" : domain})
	html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
	search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode()) # finds all links in search result
	webbrowser.open("http://www.youtube.com/watch?v={}".format(search_results[0]))
	pass

#############################
####-------##func-file##end---------#####
#############################

if reloaded==False:
	uName = locker()

	#install_req()
	uitimes=str(datetime.datetime.now())
	uinput="==========Code start on ("+uitimes+") Version:"+Vcode+"=========="
	uinput=str(uinput)+"\n"
	with open(loc("Yui_data/RAM/uidb.txt"), "a") as uinputdb:
		uinputdb.write(uinput)

	sleep(1)
	wb="\nWelcome back! "
	timex= datetime.datetime.now()
	timex=timex.strftime("%H")
	timex=int(timex)
	if timex>=6 and timex<11:
		outtxt="Good Morning, "+uName+wb
	elif timex>=16 and timex<18:
		outtxt="Good after-noon, "+uName+wb
	elif timex>=18 or timex<6:
		outtxt="Good evening, "+uName+wb
	else: outtxt= wb+uName
	tnt(outtxt)
	sleep(1)
	clean()

	ui=""
	uibit1=0

	outtxt="Hello, my name is "+aiName+".\n"
	outtxt+="My current version is: "+Vcode+"\n"
	outtxt+="Currently I can do some simple talk & things.\nAnd one more thing, please type 'exit' before exiting or closing for good.;) \n"
	#******uncomment following line******#
	#tnt(outtxt)

escape=["exit","close","shut down","quit","bye","stop","esc"]
hellobit=1
hibit=1
WyuiNamebit=1
TyuiName="0"

def FCyuiName():
	a="\nWant to change my name?   "
	tnt(a)
	q=asker()
	if q==True:
		a="I'm sorry for my name )-;\nJust type my new name: "
		tnt(a)
		TyuiName=inputer()
		a="Are you sure? It will change my name. However you can change it later by asking the same question ;-) "
		tnt(a)
		q=asker()
		if q==True:
			edit_pdata(aiName,TyuiName)
			a="Ok, my new name is "+TyuiName+".\nPLease Type exit to make it work well."
			tnt(a)
		else:
			tnt(nameGlad)
	else:
		tnt(nameGlad)

while ui not in escape:
	if uibit1==0:
		a="\nWrite something that I know: "
		tnt(a)
		ui=str(inputer())
	while ui=="":
		a="Try to type something: "
		tnt(a)
		ui=str(inputer())
	ui=i_slim(ui)

	uibit1=0
	if ui in li_redo:
		try:
			if ui1 in li_redo:
				ui=ui2
			else:
				ui=ui1
		except NameError:
			tnt('There is no previous command to redo')
	if ui in li_hello:
		if hellobit==1:
			outtxt="Hi!"
			hellobit=2
		else:
			outtxt="Yes? Need something?"
		tnt(outtxt)
	elif ui in ['i love u','i love you']:
		tnt('I love you too!')
	elif ui in ['i hate u','i hate you']:
		tnt("I'm sorry.'")
	elif ui in li_hi:
		if hibit==1:
			outtxt="Hello!"
		else:
			outtxt="Hello."
			if hibit%10==0:
				outtxt += "\nHey! You have said Hi",hibit,"times\n"
		hibit=hibit+1
		tnt(outtxt)
	elif ui in li_WyuiName:
		outtxt="My name is "+aiName
		if WyuiNamebit==1:
			outtxt+="\nIf you want, you can change my name."
			tnt(outtxt)
			FCyuiName()
		else:
			tnt(outtxt)
		WyuiNamebit+=1
	elif ui in li_QyuiName:
		outtxt="Yes, you can."
		tnt(outtxt)
		FCyuiName()
	elif ui.startswith('install '):
		reg_ex = re.search('install (.+)', ui)
		uiopen = reg_ex.group(1)
		
		tnt('Installing '+uiopen+'\n')
		install(uiopen)
		if check_installed(uiopen)==False:
				tnt('/r/Could not install!/=/')
	elif ui.startswith('upgrade '):
		reg_ex = re.search('upgrade (.+)', ui)
		uiopen = reg_ex.group(1)
		if check_installed(uiopen)==False:
			install(uiopen)
		else:
			old= get_version(uiopen)
			tnt('Upgradeing '+uiopen+'\n')
			upgrade(uiopen)
			if old!=get_version(uiopen):
				tnt('/g/Upgrade complete./=/')
			else:
				tnt('/r/Could not upgrade!/=/')
	elif ui.startswith(li_can_do):
		if ui.startswith(li_goto):
			what=[i for i in li_goto if ui.startswith(i)==True]
			reg_ex = re.search(what[0]+' (.+)', ui)
			if reg_ex:
				uiopen = reg_ex.group(1)
				if uiopen in links:
					linker(uiopen)
				elif uiopen.startswith(url_google[1:]):
					uiopen=[i for i in url_google[1:] if uiopen.startswith(i)][0]
					reg_ex2=re.search(what[0]+' '+uiopen+' (.*)', ui)
					if reg_ex2:
						uiopen = reg_ex2.group(1)
						if uiopen in googles:
							googler(uiopen)
				else:
					searcher(uiopen)

	elif ui in li_AmyName:
		tnt(random.choice(li_AmyName)+uName+'.')
	elif ui=='whats up':
		tnt('Just doing my things.')
	elif ui in li_tell_time1:
		tell_time()

	elif ui.startswith(li_whats):
		what=[i for i in li_whats if ui.startswith(i)==True]
		reg_ex = re.search(what[0]+' (.+)', ui)
		if len(ui)!=what[0] and reg_ex:
			uiopen = reg_ex.group(1)
			if uiopen in li_WmyName:
				tnt(random.choice(yeses)+random.choice(li_AmyName)+uName+'.')
			elif uiopen in li_tell_time:
				tell_time()

			else:
				wikisearch(uiopen)
	elif ui.startswith(li_who):

		who=[i for i in li_who if ui.startswith(i)==True]
		reg_ex = re.search(who[0]+' (.+)', ui)
		if len(ui)!=len(who[0]) and reg_ex:
			uiopen = reg_ex.group(1)
			if uiopen in li_WamI:

				tnt(random.choice(li_AamI)%aiName)
			elif uiopen in li_Qcreator:
				tnt(random.choice(li_Acreator)%random.choice(li_syn_created))
			else:
				find_person(uiopen)
	elif ui in li_reload:
		exec(open(Vcode+'.py').read())
		reloader=True
		break
	elif ui in escape:
		reloaded=False
		reloader=False
		break

	else:
		outtxt="I can't understand that yet. I'm still learning.\nPlease type something that I understand:  "
		tnt(outtxt)
		ui=str(inputer())
		ui=i_slim(ui)
		uibit1=1
	ui1=ui
	if ui not in li_redo:
		ui2=ui


if reloaded==False and reloader==False:
	timex= datetime.datetime.now()
	timex=timex.strftime("%H")
	timex=int(timex)
	if timex>=18 or timex<6:
		outtxt="Good night."
	else:outtxt=''
	outtxt+="\nBye! "
	if timex>=6 and timex<17:
		outtxt+='\nHave a nice day!'
	tnt(outtxt)
