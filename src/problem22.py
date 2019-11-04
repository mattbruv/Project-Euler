"""
Using names.txt (right click and 'Save Link/Target As...'),
a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order.
Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, 
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

import sys

def nameScore(index, name):
    tot = 0
    for c in name.strip().upper():
        tot += ord(c) - 64
    return tot * index

filePath = sys.argv[1]

contents = open(filePath, 'r').read()
names = contents.replace('"', '').split(',')
names.sort()

total = 0
index = 1

for name in names:
    total += nameScore(index, name)
    index += 1

print(total)

# 871198282
