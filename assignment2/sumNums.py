
import re

text = open('./regex_sum_307156.txt').readlines()

totalCount = 0

for line in text:
    allNumbersInLine = re.findall('([0-9]+)', line)
    if len(allNumbersInLine):
        for number in allNumbersInLine:
            totalCount += int(number)

print  totalCount
