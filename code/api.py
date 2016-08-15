# Using Google's geo API. Prints place_id and coordinates of the requested place

import json
import urllib

#service_url = 'http://python-data.dr-chuck.net/geojson?'
service_url = "https://maps.googleapis.com/maps/api/geocode/json?"
#address = 'University of Washington - Bothell'
print "To quit press 'Enter'"
while True:
	address = raw_input('Enter your request:')
	if len(address) <= 0: break

	# url = service_url + urllib.urlencode({'sensor':'false','address': address})
	url = service_url + urllib.urlencode({'address': address})
	print url

	data = urllib.urlopen(url).read()
	dic = json.loads(data)
	# print dic

	place_id = dic["results"][0]["place_id"]
	location = dic["results"][0]["geometry"]["location"]
	print "place_id: ", place_id
	print "latiude: ", location["lat"], "longitude: ", location["lng"]


