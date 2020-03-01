import requests
a= requests.get('http://manga.watchsao.tv/chapter/sword-art-online-progressive-chapter-22/').content
import re
a=str(a)
x = re.findall('https://images[^\s]+png', a)
print(x)
x
#print(a)

'https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http://2.bp.blogspot.com/-Ui9H-z4cuB4/WRPP6cfb-dI/AAAAAAAAb8A/5KcVg0aZhlYC9NZvc_RGq-Nii0xUy_OfQCHM/s16000/0022-002.png'
