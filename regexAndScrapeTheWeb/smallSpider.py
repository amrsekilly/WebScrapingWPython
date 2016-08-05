import urllib, re
from BeautifulSoup import *

url = 'http://python-data.dr-chuck.net/known_by_Caelen.html'
pos = 18
repeatTimes = 7
name = None

while repeatTimes:
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    tag = tags[pos-1]
    newUrl = tag.get('href', None)
    url = newUrl
    repeatTimes -= 1
    name = re.findall('>(.+)<', str(tag))

print name[0]
