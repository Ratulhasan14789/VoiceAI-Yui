#all functions
if 0==0:
    import datetime
    from os import system, name as os_name
    from time import sleep
    from threading import Thread
    from conversation2 import *
    import sys
def ins_frm_imp(frm,imp):
    global importbit
    importbit=''
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

            else:
                print("\033[1;31;40m*Some error may occur & the program will break!*\033[0;37;40m")

                importbit=frm
    finally :
        if importbit!=frm:
            globals()[imp] = getattr(__import__(frm, globals(), locals(), [imp], 0), imp)

def ins_n_imp(package):
    "Install and import package"
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        print(package,"is missing. Do you want to download it from here?\n*Data charge may apply*")
        permit=input("Yes or no?? *If no some error will occur*\n")
        while permit not in cond:
            permit=input(condERR)
            permit=Ques2.lower()
        if permit in cond:
            if permit in yes:
                import subprocess
                import sys
                subprocess.call([sys.executable, "-m", "pip", "install", package])
            else: print("\033[1;31;40m*Some error will occur & the program will break!*\033[0;37;40m")

    finally:
        globals()[package] = importlib.import_module(package)

def install(package):
    "Just install package"
    import subprocess
    import sys
    subprocess.call([sys.executable, "-m", "pip", "install", package])
def ins_n_imp_voice():
    if os_name == 'nt':
        install("pypiwin32")
        ins_n_imp("pyttsx3")
    else:
        ins_frm_imp('gtts','gTTS')
        ins_frm_imp('playsound','playsound')
        language = 'en'
        n='0'



def speakup(x):
    global n
    try:
        a = gTTS(text=x, lang=language, slow=False)
        name='Yui_data/RAM/outvoice'+n+'.mp3'
        a.save(name)
        playsound(name)
        n=str(int(n)+1)
    except:
        print('',end='')
def slowtype(x, y=0.02):
    for i in x:
        print(i, end="", flush="True")
        sleep(y)
def slowtyper(x,y=0.02):
    global slowtype,typer
    typer=Thread(target=slowtype, args=(x,y,))
    typer.start()
def tnt(x,y=0.02):
    global typer
    slowtyper(x,y)
    speakup(x)
    typer.join()
def tnt_ff(x,z,y):
    slowtyper(x,y=0.02)
    try:
        playsound( 'Yui_data/ROM/offvoice/outvoice'+ z +'.mp3')
    except:
        print('',end='')
def i_slim(ui):
    ui=ui.lower()
    ui=ui.replace("'","")
    ui=ui.replace("?","")
    ui=ui.replace("!","")
    ui=ui.replace(".","")
    ui=ui.replace(",","")
    return ui

def clear():
    # for windows
    if os_name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def backup(ui):
    uitimes=str(datetime.datetime.now())
    """Will backup every command by user"""
    with open("Yui_data/RAM/uidb.txt", "a") as uinputdb:
        uinput= uitimes,"    "+ui
        uinput=str(uinput)+"\n"
        uinputdb.write(uinput)

def delprevline():
    "Use this function to delete the last line in the STDOUT"

    #cursor up one line
    sys.stdout.write('\x1b[1A')

    #delete last line
    sys.stdout.write('\x1b[2K')


def delthisline():
	#Use this to delete current line
	sys.stdout.write('\x1b[2K')
print(1)
