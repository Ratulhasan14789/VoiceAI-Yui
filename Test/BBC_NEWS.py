'''
Read the lates News from BBC RSS Feed.

Inspired by Kubas Google API:
https://www.sololearn.com/learn/1099/?ref=app
'''
import urllib.request as RE
import xml.etree.ElementTree as ET

bbc_bit=0
Asia_url='http://feeds.bbci.co.uk/news/world/asia/rss.xml'
UK_url = 'http://feeds.bbci.co.uk/news/rss.xml?edition=uk#'
Afri_url='http://feeds.bbci.co.uk/news/world/africa/rss.xml'
EU_url='http://feeds.bbci.co.uk/news/world/europe/rss.xml'
LatA_url='http://feeds.bbci.co.uk/news/world/latin_america/rss.xml'
MidE_url='http://feeds.bbci.co.uk/news/world/middle_east/rss.xml'
US_Ca_url='http://feeds.bbci.co.uk/news/world/us_and_canada/rss.xml'
Eng_url='http://feeds.bbci.co.uk/news/england/rss.xml'
NIre_url='http://feeds.bbci.co.uk/news/northern_ireland/rss.xml'
Scot_url='http://feeds.bbci.co.uk/news/scotland/rss.xml'
Wales_url='http://feeds.bbci.co.uk/news/wales/rss.xml'
top_url='http://feeds.bbci.co.uk/news/video_and_audio/news_front_page/rss.xml?edition=uk'
world_url='http://feeds.bbci.co.uk/news/video_and_audio/world/rss.xml'
busi_url='http://feeds.bbci.co.uk/news/video_and_audio/business/rss.xml'
tech_url='http://feeds.bbci.co.uk/news/video_and_audio/technology/rss.xml'
science_url='http://feeds.bbci.co.uk/news/video_and_audio/science_and_environment/rss.xml'
polit_url='http://feeds.bbci.co.uk/news/video_and_audio/politics/rss.xml'
entertain_url='http://feeds.bbci.co.uk/news/video_and_audio/entertainment_and_arts/rss.xml'
health_url='http://feeds.bbci.co.uk/news/video_and_audio/health/rss.xml'

data = RE.urlopen (tech_url).read()
#print(data)
tree = ET.fromstring(data)
x=data.find(b'lastBuildDate')+14
lastupdate=data[x:x+29].decode('utf-8')

print ('\nThis are the latest News at the BBC:\n(updated on:%s)'%lastupdate)

for i in tree.iter('item'):
	#print(i)
	news= '\033[1;37;40m\033[4;37;40m{}:\n\033[0;37;40m{}\n'.format(i.find('title').text, i.find('description').text)
	#if bbc_bit<5:
	"""	global typer,speakers
	slowtyper(news,y,ends)
	speakup(news)
	typer.join()"""
	print(news)#remove when implanted to YUI
	#else:
		#global typer
		#slowtyper(news)
		#typer.join()
		###uncomment prev lines
	bbc_bit+=1