def generate_list(x):
    l = [globals()[name] for name in globals().keys() if name.startswith(x)]
    return [item for sublist in l for item in sublist]
import random
yeses=['Yeah! ', 'Yeah. ', 'Yes! ', 'Yes. ', 'Sure! ', 'Sure. ', 'Yeah of course. ']

li_WyuiName=["whats your name", "may i know your name?", "whats your name", 'your name']
li_QyuiName=["can i change your name", 'i want to change your name']
li_QyuiNamePre=["can i call you "]
li_hello=['hello']
li_hi=['hi']
li_redo=['redo my last command', 'retry my last command', 'redo last command', 'redo last command', 'redo']
li_QmyName=['my name']
li_syn_created=['created','programmed','invented','designed','made']
li_Qcreator=[i+" you" for i in li_syn_created]
li_Acreator=['I was %s by Ratul Hasan.', 'A boy named Ratul Hasan %s me.','Ratul Hasan %s me.']

li_WamI=['are you', 'you']
li_AamI=['I am an AI. My name is %s & I am your voice assistant.','My name is %s. I am an AI voice assistant.']
li_WmyName=['my name']
li_AmyName=['Your name is ']
li_do_u_know=['do you know ', 'you know ', 'did you know ','']
li_do_u_know2=['s', ' is', ' was',' are','']
li_whats=()
li_who=()
li_where=()
for x in li_do_u_know2:
	for s in li_do_u_know:
		li_whats+=(s+'what'+x,)
		li_who+=(s+'who'+x,)
		li_where+=(s+'where'+x,)
li_tell_time=['time','the time','current time']
li_tell_time1=li_tell_time+['tell time','tell the time']
li_tell_time2=['The time is ', "It's "]
li_goto=('open','go to','goto')
li_play=('play',)
li_can_do=li_goto+li_play
works=["talk", "calculate"]
yes=["y", "yes", "yeah", "sure", "ok", "lets go", "let's go", "start","yep","yeap"]
yes2=yes1=yes
yes2.extend(['well '+j for j in yes])
yes2.extend(['actually '+i for i in yes1])
no=["n", "no", "na", "nah", "nope", "stop", "quit", "exit",'not really','no','not at all','never']
no2=no1=no
no2.extend(['well '+j for j in no])
no2.extend(['actually '+i for i in no1])
cond = yes+no
condERR="Sorry,  I can't understand what you are saying. Just type yes or no.   "
nameGlad="Ok. Glad to hear that you like my name."

db=generate_list('li_')
