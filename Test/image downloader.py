import requests

for x in range(1, 10):
    str1 = '[Warashibe] Nikuyoku Analyze [English] [Yoroshii + Afro]_%2.2d.png' % (x)
    str2 = 'https://i.nhentai.net/galleries/471851/%2.2d.png' % (x)

    f = open(str1, 'wb')
    f.write(requests.get(str2).content)
    f.close()