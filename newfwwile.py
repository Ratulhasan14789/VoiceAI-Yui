from multiprocessing import Process
from time import sleep

from conversation2 import *

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
        print('Done')
        playsound(name)
        n=str(int(n)+1)
    except:
        print('')
def slowtype(x, y=0.02):
    for i in x:
        print(i, end="", flush="True")
        sleep(y)
def tnt(x,y=0.02):
    slowtype(x,y)
    speakup(x)
def tnt_ff(x,y,z):
    slowtype(x,y=0.02)
    
tnt("Allah is almighty.")