import hashlib
with open("Yui_data/RAM/pdatas.txt","r") as udatafile:
    uName=udatafile.readline()
    aiName=udatafile.readline()
    upwmd5=udatafile.readline()

uName=uName[2:len(uName)-1]
upwmd5=upwmd5[2:len(upwmd5)-1]

uiName=""
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
print("done")
