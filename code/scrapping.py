# Simple example of web-scrapping.
# Program counts sum of the numbers in all <span> tags


import urllib
from BeautifulSoup import *

url = "http://python-data.dr-chuck.net/comments_42.html"
html = urllib.urlopen(url).read()
tag_list = BeautifulSoup(html)

list_of_spans = tag_list('span')

counter = 0
for tag in list_of_spans:
    # Look at the parts of a tag
    counter += int(tag.contents[0])
 

print counter