from geopy.geocoders import GoogleV3
import json
geolocator = GoogleV3(api_key='AIzaSyDbc7MpEGMGa81KjeXoGcVSFyapPHB_K8o')
location = geolocator.geocode("Washington", language='en')
if location != None:
    print(json.dumps(location.raw, indent=4))
    print(location.address)
else:
    print("No location!" , location)