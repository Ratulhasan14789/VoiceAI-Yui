import pafy, sys

import urllib.request

from urllib.parse import *

from bs4 import BeautifulSoup

from os.path import exists

from playsound import playsound

import requests

import urllib.parse

import re




#print("hi")
start='title%22%3A%22'

end='%22%2C%22lengthSeconds'





def delprevline():

	"Use this function to delete the last line in the STDOUT"



	#cursor up one line

	sys.stdout.write('\x1b[1A')



	#delete last line

	sys.stdout.write('\x1b[2K')



def delthisline():

	sys.stdout.write('\x1b[2K')





def url_search(search_string):



	query_string = urllib.parse.urlencode({"search_query" : search_string})

	html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)

	search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())

	if search_results:

		return search_results[0]

	else: url_search(search_string)





class Youtube_mp3():

	def __init__(self):

		self.lst = []

		self.dict = 0

		self.dict_names = 0

		self.playlist = []

		self.code = 0

	def url_search(self, search_string):

		self.code = url_search(search_string)

		self.dict= "http://www.youtube.com/watch?v="+ self.code



	def get_search_items(self):

		start='title%22%3A%22'
		end='%22%2C%22lengthSeconds'
		a=requests.get('http://youtube.com/get_video_info?video_id='+self.code)

		self.dict_names = urllib.parse.unquote(re.findall(start+'(.*)'+end, a.content.decode())[0].replace("+",''))



	def download_media(self):

		from os import getcwd

		global song_name

		url = self.dict

		info = pafy.new(url)

		audio = info.getbestaudio(preftype="m4a")

		song_name = self.dict
		song_name=re.findall(r'\?v=(.{11})',song_name)[0]

		song_name=getcwd()+"\\songs\\"+song_name+'.m4a'

		print("Buffering: {0}.".format(self.dict_names.replace('+',' ')))

		if not exists(song_name):

			audio.download(filepath = song_name, remux_audio=False)

			delprevline()
		delprevline()
		print("Playing: {0}.".format(self.dict_names.replace('+',' ')))




	def add_playlist(self, search_query):

		url = self.url_search(search_query)

		self.playlist.append(url)



retry=0



def play_youtube(search):

	global song_name, retry

	x = Youtube_mp3()

	x.url_search(search)

	x.get_search_items()



	if len(x.dict)==0:

		retry+=1

		print('retry(',retry,')',end='\r')

		play_youtube(search)

	else:

		if retry>0:

			delthisline()

		x.download_media()

		retry=0

	#delprevline()
	found=False
	with open('songs/data.db','r') as file:
		#file.write(x.dict_names.encode('utf-8'))
		if file.read()=='':
			found=False
		else:
			for i in file.readlines():
				if i.startswith(x.dict+"="):
					found=file.index(i)
					exec(file[found])
					exec('count='+x.dict+'[0]')
					data1=data[0]+1
					break
				else: found=False
	if found==False:
		with open('songs/data.db','ab+') as file:
			file.write(x.code.encode('utf-8'))
			file.write(b'= [1, "')
			file.write(x.dict_names.encode('utf-8'))
			file.write(b'"["')
			file.write(search.encode('utf-8'))
			file.write(b'"]]\n')
	#else:
	playsound(song_name, "m4a")
while __name__=='__main__':
	play_youtube(input('Enter the title: '))
