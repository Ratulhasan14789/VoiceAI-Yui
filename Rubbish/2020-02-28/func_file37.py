#all functions
"UNCOMMENT THE FOLLoWING WHEN CODE DONE!!!"
#if __name__!='__main__:

if None==None:
	import datetime
	from os import system, makedirs, getcwd
	from os.path import exists, isdir, isfile, basename, splitext
	from time import sleep,time as time_on
	from threading import Thread
	exec(open('conversation21.py').read())
	import sys
	import re
	exec(open('web_link.py').read())
	from hashlib import md5
	from urllib.request import urlopen
	import urllib.request #used to make requests
	from platform import system as os_name
	import urllib.parse #used to parse values into the url
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

exec( reader('Yui_data/brain/brain 2.py'))
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

def locker():
	ins_n_imp('wikipedia')
	#ins_n_imp('ipinfo')
	slowtype("\033[1;37;40mPlease enter your User name: ")
	uName=input()

	while uName=="" or uName!=uiName:
		slowtype("/*Invalid username!=/\nPlease RETYPE YOUR USER NAME: ")
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
	with open(loc("Yui_data/RAM/pdatas2.py","r")) as udatafile:
		udataread=udatafile.read()
		filedata = udataread.replace(str(old),str(new))
	with open(loc("Yui_data/RAM/pdatas2.py", "w")) as udatanewfile:
		udatanewfile.write(filedata)

def asker(out=''):
	tnt(out)
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
	tnt("Can't find him")

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
