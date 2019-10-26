import sys
from time import sleep
from hashlib import md5

def delprevline():
    "Use this function to delete the last line in the STDOUT"

    #cursor up one line
    sys.stdout.write('\x1b[1A')

    #delete last line
    sys.stdout.write('\x1b[2K')

def delthisline():
    "Use this function to delete the this line in the STDOUT"


    #delete last line
    sys.stdout.write('\x1b[2K')

with open("Yui_data/RAM/pdatas.txt","r") as udatafile:
    uName=udatafile.readline()
    aiName=udatafile.readline()
    upwmd5=udatafile.readline()
aiName=aiName[2:len(aiName)-1]
uName=uName[2:len(uName)-1]
upwmd5=upwmd5[2:len(upwmd5)-1]

uiName=input("\033[1;37;40mPlease enter your User name: ")

while uiName=="" or uiName!=uName:
    uiName=input("\033[1;31;40mInvalid username!\033[1;37;40m\nPlease RETYPE YOUR USER NAME: ")

uipw=input("Please enter the Password: ")
while uipw=="":
    uipw=input("\033[1;31;40mDon't leave this empty. Enter the correct Password. Otherwise you can't run this.\033[1;37;40m N\nEnter the Password: ")
uipwmd5=md5(uipw.encode('utf-8')).hexdigest()


while uipwmd5!=upwmd5:
    uipw=input("\033[1;31;40m*WARNING!*\nYou have entered incorrect Password.\033[1;37;40m\nPlease enter the correct one: ")
    uipwmd5=md5(uipw.encode('utf-8')).hexdigest()

for i in range(20):
	sleep(.3)
	if i%3==0:
		x=":=="*12
	elif i%3==1:
		x="=:="*12
	elif i%3==2:
		x="==:"*12
	print("\rLogging in",x, end="")
	sys.stdout.flush()


delthisline()
print("\n\nLogged in")
