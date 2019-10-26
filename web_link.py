#pylint:disable=W0312
import webbrowser
import re
def generate_list(x):
    l = [globals()[name] for name in globals().keys() if name.startswith(x)]
    return [item for sublist in l for item in sublist]

def gen_list(x):
    l = [globals()[name] for name in globals().keys() if name.startswith(x)]
    return [sublist for sublist in l]


url_google=['https://www.google.com','google','gogle','gooogle']
url_fb=['https://www.facebook.com','facebook','facebok','fb']
url_yahoo=['https://www.yahoo.com','yahoo','yaho']
url_youtube=['https://www.youtube.com','youtube','tubemate','utube']
url_wiki=['https://www.wikipedia.com','wikipedia','wikipidia','wikipidea','wikipedea']
url_reddit=['https://www.reddit.com','reddit','redit']
url_bing=['https://www.bing.com','bing','microsoft search']
url_insta=['https://www.instagram.com','instagram','insta']
'''url_
url_
url_
url_
url_
url_
url_
url_'''

links=generate_list('url_')
links_li=gen_list('url_')
def linker(x):
	global links_li
	for i in links_li:
		if x in i:
			webbrowser.open_new_tab(i[0])
			
def searcher(x):
	loc= x.replace(' ','+')
	webbrowser.open_new_tab( 'https://www.google.com/search?q='+loc)

def web_go(link):
	webbrowser.open_new_tab(link)
	
#https://www.google.com/search?q=how+to+open+a+software+using+python&oq=how+to+open+a+software+u&aqs=chrome.2.69i57j0l3.22155j0j4&sourceid=chrome-mobile&ie=UTF-8

#https://st1x.cdnfile.info/user1342/570c17984dde6298db863245ac92d295/EP.1.mp4?token=Pu0jdnmjn7EBOgCV6QlNlQ&expires=1565879848&id=41503&title=(orginalP%20-%20mp4)%20Sword+Art+Online%3A+Extra+Edition+Episode+1