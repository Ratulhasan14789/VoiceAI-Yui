from tokens import *
import ipinfo
handler = ipinfo.getHandler(ipinfo_token)
details = handler.getDetails()
print(details.city)
#Emeryville
print(details.loc)
#37.8342,-122.2900