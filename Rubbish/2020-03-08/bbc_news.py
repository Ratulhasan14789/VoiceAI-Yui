'''
Read the lates News from BBC RSS Feed.

Inspired by Kubas Google API:
https://www.sololearn.com/learn/1099/?ref=app
'''
import urllib.request as RE
import xml.etree.ElementTree as ET

bbc_bit=0
bbc_topics={
"Asia_url":'http://feeds.bbci.co.uk/news/world/asia/rss.xml',
"UK_url":'http://feeds.bbci.co.uk/news/rss.xml?edition=uk#',
"Afri_url":'http://feeds.bbci.co.uk/news/world/africa/rss.xml',
"EU_url":'http://feeds.bbci.co.uk/news/world/europe/rss.xml',
"LatA_url":'http://feeds.bbci.co.uk/news/world/latin_america/rss.xml',
"MidE_url":'http://feeds.bbci.co.uk/news/world/middle_east/rss.xml',
"US_Ca_url":'http://feeds.bbci.co.uk/news/world/us_and_canada/rss.xml',
"Eng_url":'http://feeds.bbci.co.uk/news/england/rss.xml',
"NIre_url":'http://feeds.bbci.co.uk/news/northern_ireland/rss.xml',
"Scot_url":'http://feeds.bbci.co.uk/news/scotland/rss.xml',
"Wales_url":'http://feeds.bbci.co.uk/news/wales/rss.xml',
"top_url":'http://feeds.bbci.co.uk/news/video_and_audio/news_front_page/rss.xml?edition=uk',
"world_url":'http://feeds.bbci.co.uk/news/video_and_audio/world/rss.xml',
"busi_url":'http://feeds.bbci.co.uk/news/video_and_audio/business/rss.xml',
"tech_url":'http://feeds.bbci.co.uk/news/video_and_audio/technology/rss.xml',
"science_url":'http://feeds.bbci.co.uk/news/video_and_audio/science_and_environment/rss.xml',
"polit_url":'http://feeds.bbci.co.uk/news/video_and_audio/politics/rss.xml',
"entertain_url":'http://feeds.bbci.co.uk/news/video_and_audio/entertainment_and_arts/rss.xml',
"health_url":'http://feeds.bbci.co.uk/news/video_and_audio/health/rss.xml'
}

def tnt_helper(text):
	text= text.replace('/u/','/h/\033[4;37;40m')	#UNDERLINE
	text=text.replace('/a/','\033[4;34;40m')	#LINK
	text=text.replace('/y/','\033[0;33;40m')	#DID YOU MEAN...?
	text=text.replace('/g/','\033[0;32;40m')	#YES SURE
	text=text.replace('/k/','\033[0;30;40m')	#HIDDEN
	text=text.replace('/b/','\033[1;37;40m')	#BRIGHT
	text=text.replace('/r/','\033[1;31;40m')	#WARNING
	text=text.replace('/h/','\033[1;30;43m') #HIGHLIGHT
	text=text.replace('/bu/','\033[1;37;40m\033[4;37;40m')  #Brightlight+Underline
	text=text.replace('/hu/','\033[0;37;40m\033[4;30;43m')  #Highlight+Underline
	text=text.replace('/=/','\033[0;37;40m')

	return text

def news_report(x):
	link=bbc_topics[x]
	data = RE.urlopen (link).read()
	#print(data)
	tree = ET.fromstring(data)
	x=data.find(b'lastBuildDate')+14
	lastupdate=data[x:x+29].decode('utf-8')
	report=''

	report+='\nThis are the latest News at the BBC:\n(updated on:%s)\n'%lastupdate
	for i in tree.iter('item'):
		#print(i)
		news= '/bu/{}:/=/\n{}\n'.format(i.find('title').text, i.find('description').text)

		report+=news+"/s/"
		report+='\n'
	return report
#print(__name__)
def task(Topic):
	if __name__=='__main__':
		print(tnt_helper(news_report(Topic)))
	else:
		return news_report(Topic)
if __name__=='__main__':
	task('Asia_url')
