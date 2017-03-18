import urllib
import xml.etree.ElementTree as ET
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'

while True:
    address = raw_input('Enter address: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(address)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    #print data
    info = json.loads(data)
    print info["comments"]
    total = 0
    for i in info["comments"]:
	total = total + i["count"]
    print total
    break

