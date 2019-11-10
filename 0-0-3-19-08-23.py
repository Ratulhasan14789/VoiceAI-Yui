#pylint:disable=C0103
#pylint:disable=W0312
#	#tab
Vcode = "0.0.1.19.06.12"
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

func_ver=37
from func_file37 import *

uName = locker()

#install_req()
uitimes=str(datetime.datetime.now())
uinput="==========Code start on ("+uitimes+") Version:"+Vcode+"=========="
uinput=str(uinput)+"\n"
with open("Yui_data/RAM/uidb.txt", "a") as uinputdb:
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
	xxx="\nWant to change my name?   "
	tnt(xxx)
	q=asker()
	if q==True:
		xxx="I'm sorry for my name )-;\nJust type my new name: "
		tnt(xxx)
		TyuiName=input()
		xxx="Are you sure? It will change my name. However you can change it later by asking the same question ;-) "
		tnt(xxx)
		q=asker()
		if q==True:
			edit_pdata(aiName,TyuiName)
			xxx="Ok, my new name is "+TyuiName+".\nPLease Type exit to make it work well."
			tnt(xxx)
		else:
			tnt(nameGlad)
	else:
		tnt(nameGlad)

while ui not in escape:
	if uibit1==0:
		xxx="\nWrite something that I know: "
		tnt(xxx)
		ui=str(input())
	while ui=="":
		xxx="Try to type something: "
		tnt(xxx)
		ui=str(input())
	backup(ui)
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
		try:
			tnt('Installing '+uiopen+'\n')
			install(uiopen)
		except:
			tnt('Could not install')
		else:
			if check_installed(uiopen)==False:
				tnt('Could not install')
	elif ui.startswith('upgrade '):
		reg_ex = re.search('upgrade (.+)', ui)
		uiopen = reg_ex.group(1)
		try:
			tnt('Upgradeing '+uiopen+'\n')
			upgrade(uiopen)
			tnt('Upgrade complete.')
		except:
			tnt('Could not upgrade')
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
		exec(open('func_file'+str(func_ver)+'.py').read())
		print('done')
	elif ui in escape:
		break
	else:
		outtxt="I can't understand that yet. I'm still learning.\nPlease type something that I understand:  "
		tnt(outtxt)
		ui=str(input())
		ui=i_slim(ui)
		uibit1=1
	ui1=ui
	if ui not in li_redo:
		ui2=ui
backup(ui)


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
