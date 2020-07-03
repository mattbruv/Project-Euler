# My forum post after solving:
"""
Solved it with Python in 0:01:40.45. I'm not going to post my code because it was almost 100 lines long and got quite hacky towards the end. There were a few "gotchas" that I had to overcome to get the right answer.

Firstly, there was an instance where the anagrams were > 2. eg: ['POST', 'SPOT', 'STOP'].
Secondly, there are cases where letters in a string are repeated multiple times, such as ['CENTRE', 'RECENT'] (both words have two E's).

Lastly, after coding everything, I kept getting 80514729 as my answer, but it was wrong. This was happening on ['CREATION', 'REACTION']. I figured out the problem. When 80514729 is mapped from CREATION to REACTION, the resulting integer is 05184729, and the leading zero is dropped when parsed as an int. The altered number is a perfect square, which screwed up my algorithm.
Even though I thought I had a check for when zero was at the front, that was only checked during the first permutation, not the resulting ones. Once I fixed this bug, I got the right answer.

I solved it with this process:
1. Parse file to get a list of words.
2. Parse list of words to collect and group unique anagrams.
3. For each anagram group, generate permutations in the range from 0-9, limited by the length of the words.
4. For each number permutation, assign that number to a respective character. If the first number is zero, skip this permutation.
5. For each word in the anagram group, get the numerical value using the character map mentioned above.
6. If all words are perfect squares, and the number > anything so far, that is the biggest number so far.
7. Repeat until at the end.
"""

import math
import itertools

def getAnagrams(words):
    done = []
    anagrams = []
    for word in words:
        gram = [word]
        chars = [x for x in word]
        chars.sort()
        thisGram = "".join(chars)
        if thisGram not in done:
            for test in words:
                testCs = [x for x in test]
                testCs.sort()
                if testCs == chars and word != test:
                    gram.append(test)
            if len(gram) > 1:
                anagrams.append(gram)
            done.append(thisGram)
    return anagrams

def is_square(num):
    return num == math.floor(math.sqrt(num)) ** 2

def getUniqueLetters(string):
    letters = []
    for char in string:
        if char not in letters:
            letters.append(char)
    return letters

def combine(chars, nums):
    d = {}
    for i in range(0, len(chars)):
        d[chars[i]] = nums[i]
    return d

def wordToNumber(word, charMap):
    numStr = ""
    for c in word:
        numStr += str(charMap[c])
    return numStr

def getHighestSquare(words):
    chars = getUniqueLetters(words[0])
    numPerms = list(itertools.permutations(range(0, 10), len(chars)))
    maxSquare = 0
    # don't allow zero in front
    for perm in numPerms:
        if perm[0] == 0:
            continue
        test = perm
        charMap = combine(chars, test)
        isPair = True
        maxN = 0
        # loop through each word and get biggest
        for word in words:
            numStr = wordToNumber(word, charMap)
            if int(numStr[0]) == 0:
                isPair = False
                continue
            else:
                num = int(numStr)
                if not is_square(num):
                    isPair = False
                else:
                    if num > maxN:
                        maxN = num
        if isPair:
            if maxN > maxSquare:
                maxSquare = maxN
    print(words, maxSquare)
    return maxSquare

def problem98(args):
    filename = args[0]
    f = open(filename, 'r')
    wordList = f.readlines()[0].replace('"', '')
    words = wordList.split(",")
    print('getting anagrams..')
    ans = getAnagrams(words)
    print('got anagrams..')
    """
    test = ['CREATION', 'REACTION'] 
    print(getHighestSquare(test))
    test = ['CARE', 'RACE'] 
    print(getHighestSquare(test))
    """
    maxA = 0
    for ana in ans:
        res = getHighestSquare(ana)
        if res > maxA:
            maxA = res
    print(maxA)

# 18769
# 0:01:40.453745 ELAPSED