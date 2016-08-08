# prompts for the url then calculates the sum of the values in the returned JSON obj

import json, urllib

url = raw_input("Enter URL: ")

totalSum = 0

uh = urllib.urlopen(url)
data = uh.read()

JsonObj = json.loads(data)

for comment in JsonObj['comments']:
    totalSum += int(comment['count'])

print totalSum
