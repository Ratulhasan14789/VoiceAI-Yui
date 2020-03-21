
Vcode = "0.0.1.19.06.12"
#*************************************************
#            This code was created by Ratul Hasan
#              So comlpete credit goes to him(me)
#*************************************************
#     Sharing this code without my permission is not allowed
#*************************************************
# This code was created based on IDLE, Pydroid(Android), qPython(Android) etc. So most online/web site based idle(i.e: Sololearn) can't run this code properly.
#*************************************************
# If there is any error or you want to help please let me know.
#e-mail: wwwqweasd147@gmail.com
#*************************************************


def ins_frm_imp(frm,imp):
    "Install and import package"
    import importlib
    try:
        getattr(__import__(frm, globals(), locals(), [imp], 0), imp)
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
            else: print("\033[1;31;40m*Some error will occur & the program will break!*\033[0;37;40m")

    finally:
        globals()[imp] = getattr(__import__(frm, globals(), locals(), [imp], 0), imp)


import datetime
from os import system, name
from time import sleep
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

uitimes=str(datetime.datetime.now())
uinput="==========Code start on (",uitimes,") Version:",Vcode,"=========="
uinput=str(uinput)+"\n"
with open("Yui_data/RAM/uidb.txt", "a") as uinputdb:
    uinputdb.write(uinput)

from lock_nd_color import *	# To lock the AI

sleep(1)
wb="\nWelcome back!"
timex= datetime.datetime.now()
timex=timex.strftime("%H")
timex=int(timex)
if timex>=6 and timex<16:
    outttxt="Good Morning, "+uName+wb
elif timex>=16 and timex<18:
    outttxt="Good after-noon, "+uName+wb
elif timex>=18 or timex<6:
    outttxt="Good evening, "+uName+wb

print(outttxt)

sleep(1)
clear()

ui=""
uibit1=0

print("Hello, my name is "+aiName+".\n")
sleep(.23)
print("My current version is:",Vcode+"\n")
sleep(.23)
print("Curently I can do some simple talk & things.\nAnd one more thing, please type 'exit' before exiting or closing for good.;) \n")
sleep(.23)

def backup():
    """Will backup every command by user"""
    with open("Yui_data/RAM/uidb.txt", "a") as uinputdb:
        uinput= uitimes,"    "+ui
        uinput=str(uinput)+"\n"
        uinputdb.write(uinput)

from conversation2 import *

escape=["exit","close","shut down","quit","bye","stop","esc"]
hellobit=1

hibit=1
WyuiNamebit=1
TyuiName="0"
works=["talk","calculate"]
yes=["y","yes","yeah","sure","ok","lets go","let's go","start"]
no=["n","no","na","nah","nope","stop","quit","exit"]
cond = yes+no
condERR="Sorry, I can't understand what you are saying. Just type yes or no."
nameGlad="Ok. Glad to hear that you like my name."
def FCyuiName():
    Ques1=str(input("Want to change my name? "))
    Ques1=Ques1.lower()
    while Ques1 not in cond:
        Ques1=str(input(condERR))
        Ques1=Ques1.lower()
    if Ques1 in cond:
        if Ques1 in yes:
            TyuiName=input("I'm sorry for my name )-;\nJust type my new name: ")
            Ques2=input("Are you sure? It will change my name. However you can change it later by asking the same question ;-) ")
            Ques2=Ques2.lower()
            while Ques2 not in cond:
                Ques2=input(condERR)
                Ques2=Ques2.lower()
            if Ques2 in cond:
                if Ques2 in yes:
                    with open("Yui_data/RAM/pdatas.txt","r") as udatafile:
                        udataread=udatafile.read()
                    filedata = udataread.replace(str(aiName),str(TyuiName))
                    with open("Yui_data/RAM/pdatas.txt","w") as udatanewfile:
                        udatanewfile.write(filedata)
                    print("Ok, my new name is "+TyuiName+".\nPLease Type exit to make it work well.")
                    Ques1=0
                    Ques2=0
                else:
                    print(nameGlad)
                    Ques1=0
                    Ques2=0
        else:
            print(nameGlad)
            Ques1=0
            Ques2=0
while ui not in escape:
    if uibit1==0:
        ui=str(input("Write something that I know: "))
    while ui=="":
        ui=str(input("Try to type something. "))
    uitimes=str(datetime.datetime.now())
    backup()
    ui=ui.lower()
    ui=ui.replace("'","")
    ui=ui.replace("?","")
    ui=ui.replace("!","")
    ui=ui.replace(".","")
    ui=ui.replace(",","")

    uibit1=0
    if ui in li_hello:
        if hellobit==1:
        	outttxt="Hi!"
        	hellobit=2
        else:
            outttxt="Yes? Need something?"
        print(outttxt)
    elif ui in li_hi:
        if hibit==1:
            outttxt="Hello!"
        else:
            outttxt="Hello."
            if hibit%10==0:
                outttxt += "\nHey! You have said Hi",hibit,"times\n"
        hibit=hibit+1
        print(outttxt)
    elif ui in li_WyuiName:
        outttxt="My name is "+aiName
        if WyuiNamebit==1:
            outttxt+="\nIf you want, you can change my name."
            print(outttxt)
            FCyuiName()
        print(outttxt)
        WyuiNamebit+=1
    elif ui in li_QyuiName:
        outttxt="Yes, you can."
        print(outttxt)
        FCyuiName()
    elif ui in escape:
        break
    elif ui not in db:
        outttxt="I can't understand that, yet. I'm still learning.\nPlease type something that I understand. "
        print(outttxt,end=" ")
        ui=str(input())
        ui=ui.lower()
        if ui not in db:
            uibit1=1

uitimes=str(datetime.datetime.now())
backup()


timex= datetime.datetime.now()
timex=timex.strftime("%H")
timex=int(timex)
if timex>=18 or timex<6:
	outttxt="Good night."
else:outttxt=''
outttxt+="\nBye! See ya."
print(outttxt)
