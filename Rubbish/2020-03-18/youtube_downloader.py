import pafy, sys
import urllib.request
from urllib.parse import *
from bs4 import BeautifulSoup
from os.path import exists
from playsound import playsound


import urllib.request
import urllib.parse
import re


def delprevline():
	"Use this function to delete the last line in the STDOUT"

	#cursor up one line
	sys.stdout.write('\x1b[1A')

	#delete last line
	sys.stdout.write('\x1b[2K')

def delthisline():
	sys.stdout.write('\x1b[2K')


def url_search(search_string):

	query_string = urllib.parse.urlencode({"search_query" : 'Euphoria bts'})
	html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
	search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
	if search_results:
		return "http://www.youtube.com/watch?v=" + search_results[0]
	else: url_search(search_string)


class Youtube_mp3():
	def __init__(self):
		self.lst = []
		self.dict = {}
		self.dict_names = {}
		self.playlist = []

	def url_search(self, search_string):
		self.dict[0]= url_search(search_string)
	def get_search_items(self, max_search):

		if self.dict != {}:
			i = 1
			for url in self.dict.values():
				try:
					info = pafy.new(url)
					self.dict_names[i] = info.title
					#print("{0}. {1}".format(i, info.title))
					i += 1

				except ValueError:
					pass


	def download_media(self, num):
		from os import getcwd
		global song_name
		url = self.dict[0]
		info = pafy.new(url)
		audio = info.getbestaudio(preftype="m4a")
		song_name = self.dict[0]
		song_name=re.findall(r'\?v=(.{11})',song_name)[0]
		song_name=getcwd()+"\\songs\\"+song_name+'.m4a'
		print("Buffering: {0}.".format(self.dict_names[1]))
		if not exists(song_name):
			audio.download(filepath = song_name, remux_audio=False)
			delprevline()


	def add_playlist(self, search_query):
		url = self.url_search(search_query, max_search=1)
		self.playlist.append(url)

retry=0

def play_youtube(search):
	global song_name, retry
	x = Youtube_mp3()
	x.dict = {}
	x.dict_names = {}
	x.url_search(search)
	x.get_search_items(1)

	if len(x.dict)==0:
		retry+=1
		print('retry(',retry,')',end='\r')
		play_youtube(search)
	else:
		if retry>0:
			delthisline()
		x.download_media()
		retry=0
	delprevline()
	playsound(song_name, "m4a")

play_youtube('Euphoria bts')
