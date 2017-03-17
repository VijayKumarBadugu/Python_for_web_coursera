# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
count = raw_input('Enter - ')
pos = raw_input('Enter - ')
def crawler(url,pos):
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	tag = soup('a')
	print tag[int(pos)-1].contents[0]
	return tag[int(pos)-1].get('href', None)
for i in range(int(count)):
    	url = crawler(url,pos)

