def check_installed(x):
	import importlib.util
	spam_loader = importlib.util.find_spec(x)
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

def writer(dir,fname,mode,data,bit=0):
	if dir==0:
		with open(fname,mode) as file:
			file.write(data)
	else:
		if isdir(dir):
			if dir.endswith('/'):
				with open(loc(dir+fname),mode) as f:
					f.write(data)
			else:
				with open(loc(dir+'/'+fname),mode) as f:
					f.write(data)
		else:
			makedirs(loc(dir))
			writer(dir,fname,mode,data,bit)
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

def tnt_helper(text,bit):
	if bit=='type':
		if '//' in text:
			t1=text.split('//')
			for s in t1:
				a=re.search('\[\[',s)
				if a:
					t1[t1.index(s)]=s.replace('[[','')
			for s in t1:
				b=re.search('\]\]',s)
				if b:
					b=b.span()
					t1[t1.index(s)]=t1[t1.index(s)][b[1]:len(s)]
			text=''
			for s in t1: text+=s
	elif bit=='talk':
		if '//' in text:
			t1=text.split('//')
			for s in t1:
				a=re.search('\[\[',s)
				if a:
					a=a.span()
					t1[t1.index(s)]=t1[t1.index(s)][0:a[0]]
			for s in t1:
				b=re.search('\]\]',s)
				if b:
					t1[t1.index(s)]=s.replace(']]','')
			text=''
			for s in t1: text+=s
	text=text.replace('/_','\033[4;37;40m')	#UNDERLINE
	text=text.replace('/<','\033[4;34;40m')	#LINK
	text=text.replace('/?','\033[0;33;40m')	#DID YOU MEAN...?
	text=text.replace('/!','\033[0;32;40m')	#YES SURE
	text=text.replace('/-','\033[0;30;40m')	#HIDDEN
	text=text.replace('/+','\033[1;37;40m')	#BRIGHT
	text=text.replace('/*','\033[1;31;40m')	#WARNING
	text=text.replace('/+','\033[1;37;43m')
	text=text.replace('=/','\033[1;37;40m')
	return text

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

not_installed=[]

def install(pack):
	global not_installed
	"Just install package"
	import subprocess
	import sys
	if check_installed(pack)==True:
		slowtype('Already installed')
	elif check_internet()==True:
		subprocess.call([sys.executable, "-m", "pip", "install", pack])
		if check_installed(pack)==False:
			subprocess.call([sys.executable, "-m", "pip", "install",'--user', pack])
	else:
		slowtype('/*Failed! \nPossible cause: No internet connection.=/\n')
		not_installed.append(pack)

#install('"pip/wikipedia-140.tar.gz"')
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
		slowtype('/*Failed! \nPossible cause: No internet connection.=/\n')

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
		permit=input("/*Yes or no?? *If no some error will occur*=/\n")
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
				slowtype("/**Some error will occur & the program will break!*=/")
				importbit=1
				if pack=='pyttsx3':
					importbit=2
				elif pack=='gtts':
					importbit=3
	finally:
		if importbit==0:
			globals()[aas] = importlib.import_module(pack)
	del importlib

def backup(ui):
	uitimes=str(datetime.datetime.now())
	"""Will backup every command by user"""
	with open(loc("Yui_data/RAM/uidb.txt"), "a") as uinputdb:
		uinput= uitimes,ui
		uinput=str(uinput)+"\n"
		uinputdb.write(uinput)

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
		print("An error occurred")
	finally:
		# Don't forget to close the file!
		zf.close()
	#file_names= ["brain.py", "voice.py"]
	#compress(file_names)
	del zipfile, zlib