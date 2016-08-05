import urllib
import re
from BeautifulSoup import *

url = 'http://python-data.dr-chuck.net/comments_307161.html'
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
tags = soup('span')

sumNums = 0

for tag in tags:
    propNum = re.findall('>([0-9]+)<', str(tag))
    if len(propNum):
        for num in propNum:
            sumNums += int(num)

print sumNums
