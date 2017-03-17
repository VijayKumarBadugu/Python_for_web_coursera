# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
#print html
soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('span')
count = 0
total_sum =0
for tag in tags:
    	
    	total_sum = total_sum + int(tag.contents[0])
    	count = count+1
print "Count ",count
print "Sum ",total_sum

