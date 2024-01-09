import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = urllib.request.urlopen(input('Enter URL: '), context=ctx).read()
pos = int(input('Enter position: '))
soup = BeautifulSoup(html, 'html.parser')

for i in range(int(input('Enter count: '))):
	tags = soup('a')
	html = urllib.request.urlopen(tags[pos-1].get('href', None), context=ctx).read()
	soup = BeautifulSoup(html, 'html.parser')
	print(tags[pos-1].get('href', None))