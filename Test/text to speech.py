import time, pyttsx3

# Import the required module for text
# to speech conversion
t=time.time()
#from gtts import gTTS
#from playsound import playsound
from threading import Thread

# This module is imported so that we can
# play the converted audio

# The text that you want to convert to audio
outtxt = 'Welcome to ai.com!'
outvoice='voice'
outtxt +=outvoice
# Language in which you want to convert
language = 'en'

outno=0
'''def speakup2(x):
    try:
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
    except:
        print('Sorry there was a problem while converting the text.\nPossible Cause Internet connection problem')
        engine = pyttsx3.init()
        engine.say(x)
            # Flush the say() queue and play the audio
        engine.runAndWait()
speakup2(outtxt)

outtxt='next word'''



print('done in ',time.time()-t)

import pyttsx3

#from func_file2 import *

#ins_n_imp_voice()
def speakup(x):
    global n
    global engine
    voice_up=0
    if voice_up==0:
        global engine
        engine = pyttsx3.init()
        engine.say(x)
        # Flush the say() queue and play the audio
        engine.runAndWait()
    else:
        try:
            a = gTTS(text=x, lang=language, slow=False)
            name='Yui_data/RAM/outvoice'+n+'.mp3'
            a.save(name)
            playsound(name)
            n=str(int(n)+1)
        except:
            print('',end='')
        print('gtts')
def slowtype(x, y=0.02):
    for i in x:
        print(i, end="", flush="True")
        time.sleep(y)
def slowtyper(x,y):
    global slowtype
    global typer
    typer=Thread(target=slowtype, args=(x,y,))
    typer.start()

def tnt(x,y=0.02):
    global typer
    slowtyper(x,y)
    speakup(x)
    typer.join()
x='Hello Bangladesh\n Ok'
x+=outtxt
tnt(x)


from gtts import gTTS
import speech_recognition as sr
import os
import re
import webbrowser
import smtplib
import requests
from weather import Weather

def talkToMe(audio):
    "speaks audio passed as argument"

    print(audio)
    for line in audio.splitlines():
        os.system("say " + audio)

    #  use the system's inbuilt say command instead of mpg123
    #  text_to_speech = gTTS(text=audio, lang='en')
    #  text_to_speech.save('audio.mp3')
    #  os.system('mpg123 audio.mp3')


def myCommand():
    "listens for commands"

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Ready...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = myCommand();

    return command


def assistant(command):
    "if statements for executing commands"

    if 'open reddit' in command:
        reg_ex = re.search('open reddit (.*)', command)
        url = 'https://www.reddit.com/'
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        webbrowser.open(url)
        print('Done!')

    elif 'open website' in command:
        reg_ex = re.search('open website (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.' + domain
            webbrowser.open(url)
            print('Done!')
        else:
            pass

    elif 'what\'s up' in command:
        talkToMe('Just doing my thing')
    elif 'joke' in command:
        res = requests.get(
                'https://icanhazdadjoke.com/',
                headers={"Accept":"application/json"}
                )
        if res.status_code == requests.codes.ok:
            talkToMe(str(res.json()['joke']))
        else:
            talkToMe('oops!I ran out of jokes')

    elif 'current weather in' in command:
        reg_ex = re.search('current weather in (.*)', command)
        if reg_ex:
            city = reg_ex.group(1)
            weather = Weather()
            location = weather.lookup_by_location(city)
            condition = location.condition()
            talkToMe('The Current weather in %s is %s The tempeture is %.1f degree' % (city, condition.text(), (int(condition.temp())-32)/1.8))

    elif 'weather forecast in' in command:
        reg_ex = re.search('weather forecast in (.*)', command)
        if reg_ex:
            city = reg_ex.group(1)
            weather = Weather()
            location = weather.lookup_by_location(city)
            forecasts = location.forecast()
            for i in range(0,3):
                talkToMe('On %s will it %s. The maximum temperture will be %.1f degree.'
                         'The lowest temperature will be %.1f degrees.' % (forecasts[i].date(), forecasts[i].text(), (int(forecasts[i].high())-32)/1.8, (int(forecasts[i].low())-32)/1.8))


    elif 'email' in command:
        talkToMe('Who is the recipient?')
        recipient = myCommand()

        if 'John' in recipient:
            talkToMe('What should I say?')
            content = myCommand()

            #init gmail SMTP
            mail = smtplib.SMTP('smtp.gmail.com', 587)

            #identify to server
            mail.ehlo()

            #encrypt session
            mail.starttls()

            #login
            mail.login('username', 'password')

            #send message
            mail.sendmail('John Fisher', 'JARVIS2.0@protonmail.com', content)

            #end mail connection
            mail.close()

            talkToMe('Email sent.')

        else:
            talkToMe('I don\'t know what you mean!')


talkToMe('I am ready for your command')

#loop to continue executing multiple commands
while True:
    assistant(myCommand())
