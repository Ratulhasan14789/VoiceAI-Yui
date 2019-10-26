import time

# Import the required module for text
# to speech conversion
t=time.time()
from gtts import gTTS
from playsound import playsound
# This module is imported so that we can
# play the converted audio

# The text that you want to convert to audio
outtxt = 'Welcome to ai.com!'
outvoice='voice'
# Language in which you want to convert
language = 'en'


def speakup(a,x):
#    try:
        # Passing the text and language to the engine,
        # here we have marked slow=False. Which tells
        # the module that the converted audio should
        # have a high speed
    a = gTTS(text=x, lang=language, slow=False)
        # Saving the converted audio in a mp3 file named
    name='outvoice.mp3'
    a.save(name)
    print(x)
        # Playing the converted file
        #playsound("audiofile.mp3")
    playsound(name)
#    except:
#        print('Sorry there was a problem while converting the text.\nPossible Cause Internet connection problem')
speakup(outvoice,outtxt)





print('done in ',time.time()-t)
