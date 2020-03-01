def ins_n_imp_voice():
	global not_installed, vmodule,importbit
	NoVoiceError="\n \n|*Warning! Voice won't work\n\033*|"
	if os_name()=='Windows':
		try:
			ins_n_imp('pyttsx3')
			vmodule='pyttsx3'
			global engine
			if importbit!=2:
				engine = pyttsx3.init()
				# Set properties _before_ you add things to say
				engine.setProperty('rate', 190)
				# Speed percent (can go over 100)
				engine.setProperty('volume', 0.1)  # Volume 0-1
				en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"

				# Use female English voice
				engine.setProperty('voice', en_voice_id)
			else: raise ValueError
		except ValueError:
			ins_frm_imp('gtts','gTTS')
			if check_installed('gtts')==True:
				vmodule='gtts'
			else:
				print(NoVoiceError)
				vmodule='unav'
	else:
		vmodule='unav'
	return vmodule


vmodule=ins_n_imp_voice()

def speakup(x):
	global vmodule, speakers
	if vmodule=='pyttsx3':
		global engine
		x=tnt_helper(x,'talk')
		engine.say(x)
		# Flush the say() queue and play the audio
		engine.runAndWait()

	elif vmodule=='gtts':
		global audionum
		a = gTTS(text=x, lang='en', slow=False)
		name = 'Yui_data/RAM/outvoice' + audionum +'.mp3'
		a.save(name)
		audionum=str(int(audionum) +1)
	else: pass

def tnt(x,y=0.02,ends=''):
	global typer,speakers
	slowtyper(x,y,ends)
	speakup(x)
	typer.join()

def tnt_ff(x,z,y):
	slowtyper(x,y=0.02)
	try:
		playsound( 'Yui_data/ROM/offvoice/outvoice'+ z +'.mp3')
	except:
		pass