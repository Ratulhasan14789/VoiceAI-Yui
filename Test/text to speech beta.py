yes=["y","yes","yeah","sure","ok","lets go","let's go","start"]
no=["n","no","na","nah","nope","stop","quit","exit"]
cond = yes+no
condERR="Sorry, I can't understand what you are saying. Just type yes or no."

# Import the required module for text
# to speech conversion
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


ins_frm_imp('gtts','gTTS')

# This module is imported so that we can
# play the converted audio

# The text that you want to convert to audio
mytext = 'Yes! I did it!'

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("welcome_beta.mp3")

# Playing the converted file
from playsound import playsound

playsound('welcome_beta.mp3')
