from pyowm import OWM
from tokens import *
def check_weather(loc='',co=''):
	owm=OWM()
 	if loc=='':
 		