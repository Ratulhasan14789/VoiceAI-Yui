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


from func_file36 import *

uName = locker()

#install_req()
uitimes=str(datetime.datetime.now())
uinput="==========Code start on ("+uitimes+") Version:"+Vcode+"=========="
uinput=str(uinput)+"\n"
with open("Yui_data/RAM/uidb.txt", "a") as uinputdb:
	uinputdb.write(uinput)

sleep(1)
wb="\nWelcome back!"
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
tnt(outtxt)

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
		print(22)
		reg_ex = re.search('install (.+)', ui)
		uiopen = reg_ex.group(1)
		try:
			tnt('Installing '+uiopen)
			install(uiopen)
		except:
			tnt('Could not install')
		else:
			if check_installed(uiopen)==False:
				tnt('Could not install')
	elif ui.startswith(li_goto):
		what=[i for i in li_whats if ui.startswith(i)==True]
		reg_ex = re.search(what[0]+' (.+)', ui)
		uiopen = reg_ex.group(1)
		if uiopen in links:
			linker(uiopen)
		else:
			searcher(uiopen)

	elif ui in li_myName:
		tnt(random.choice(li_AmyName)+uName+'.')
	elif ui.startswith(li_whats):

		what=[i for i in li_whats if ui.startswith(i)==True]
		reg_ex = re.search(what[0]+' (.+)', ui)
		if len(ui)!=what[0]:
			uiopen = reg_ex.group(1)
			if uiopen in li_WmyName:
				tnt(random.choice(yeses)+random.choice(li_AmyName)+uName+'.')
			elif uiopen in li_tell_time:
				nowits=datetime.datetime.now()
				tnt(random.choice(li_tell_time2)+nowits.strftime("%I:%M %p"))

			else:
				wikisearch(uiopen)
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
