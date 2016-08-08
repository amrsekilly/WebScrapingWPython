import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter a URL: ')
sumNums = 0

while True:

    uh = urllib.urlopen(url)
    data = uh.read()
    tree = ET.fromstring(data)
    counts = tree.findall('.//count')

    for count in counts:
        sumNums += int(count.text)

    print sumNums
    break
