yes=["y","yes","yeah","sure","ok","lets go","let's go","start"]
no=["n","no","na","nah","nope","stop","quit","exit"]
cond = yes+no
condERR="Sorry, I can't understand what you are saying. Just type yes or no."

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

"""ins_n_imp('playsound')
print("Done!")
"""

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

"""ins_frm_imp('gtts','gTTS')
myobj = gTTS(text='mytext is too long', lang='en', slow=False)

myobj.save("welcome_beta.mp3")

# Playing the converted file
from playsound import playsound

playsound('welcome_beta.mp3')
try:
    return getattr(__import__(modulename, globals(), locals(), [classname], -1), classname)
except AttributeError:
    print 'Error in importing class. "%s" has no class "%s"' % (modulename, classname)
except ImportError as e:
    print 'Error in importing class: %s' % (e)"""
