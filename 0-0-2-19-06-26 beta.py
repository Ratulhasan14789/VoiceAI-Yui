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

import datetime
import hashlib

uitimes=str(datetime.datetime.now())
uinput="==========Code start on (",uitimes,") Version:",Vcode,"=========="
uinput=str(uinput)+"\n"
with open("Yui_data/RAM/uidb.txt", "a") as uinputdb:
    uinputdb.write(uinput)

with open("Yui_data/RAM/pdatas.txt","r") as udatafile:
    uName=udatafile.readline()
    aiName=udatafile.readline()
    upwmd5=udatafile.readline()
aiName=aiName[2:len(aiName)-1]
uName=uName[2:len(uName)-1]
upwmd5=upwmd5[2:len(upwmd5)-1]

uiName=input("Please enter your User name: ")

while uiName=="" or uiName!=uName:
    uiName=input("Invalid username!\nPlease RETYPE YOUR USER NAME: ")

uipw=input("Please enter the Password: ")
while uipw=="":
    uipw=input("Don't leave this empty. Enter the Password. Otherwise you can't run this.\nEnter the Password: ")
uipwmd5=hashlib.md5(uipw.encode('utf-8')).hexdigest()


while uipwmd5!=upwmd5:
    uipw=input("*WARNING!*\nYou have entered incorrect Password.\nPlease enter the correct one: ")
    uipwmd5=hashlib.md5(uipw.encode('utf-8')).hexdigest()


timex= datetime.datetime.now()
timex=timex.strftime("%H")
timex=int(timex)
if timex>=6 and timex<16:
    print("Good Morning,",uName)
elif timex>=16 and timex<18:
    print("Good after-noon,",uName)
elif timex>=18 or timex<6:
    print("Good evening,",uName)

print("Welcome back!")

ui=""
uibit1=0

print("Hello, my name is "+aiName+".\nMy current version is:",Vcode+"\nCurently I can do some simple talk & things.\nAnd one more thing, please type 'exit' before exiting or closing for good.;) \n")

def backup():
    with open("Yui_data/RAM/uidb.txt", "a") as uinputdb:
        uinput= uitimes,"    "+ui
        uinput=str(uinput)+"\n"
        uinputdb.write(uinput)

with open("Yui_data/ROM/conversation_1.txt","r") as conv1file:
    conv1list=conv1file.readlines()

import conversation2

escape=["exit","close","shut down","quit","bye","stop","esc"]
hello=conv1list[0]
hellobit=1
hi=conv1list[1]
hibit=1
WyuiNamebit=1
TyuiName="0"
canyou=conv1list[2]
works=["talk","calculate"]
yes=["y","yes","yeah","sure","ok","lets go","let's go","start"]
no=["n","no","na","nah","nope","stop","quit","exit"]
cond = yes+no
condERR="Sorry, I can't understand what you are saying. Just type yes or no."
nameGlad="Ok. Glad to hear that you like my name."

db=conv1list+conv2list
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
    ui=ui.lower()
    uibit1=0
    if ui in hello:
        if hellobit==1:
            print("Hi !")
            hellobit=2
        else:
            print("Yes? Need something?")
    elif ui in hi:
        if hibit==1:
            print("Hello!")
        else:
            print("Hello.")
            if hibit%10==0:
                print("\nHey! You have said Hi",hibit,"times\n")
        hibit=hibit+1
    elif ui in WyuiName:
        print("My name is "+aiName)
        if WyuiNamebit==1:
            print("If you want, you can change my name.")
            FCyuiName()
        WyuiNamebit+=1
    elif ui in QyuiName:
        print("Yes, you can.")
        FCyuiName()
    elif ui in escape:
        break
    elif canyou in ui:
        if ui in works:
            print("Call 911")
    elif ui not in db:
        print("I can't understand that, yet. I'm still learning.\n")
        ui=str(input("Please type something that I understand. "))
        ui=ui.lower()
        if ui not in db:
            uibit1=1
    uitimes=str(datetime.datetime.now())
    backup()
uitimes=str(datetime.datetime.now())
backup()


timex= datetime.datetime.now()
timex=timex.strftime("%H")
timex=int(timex)
if timex>=18 or timex<6:
    print("Good night")

print("Bye! See ya.")
