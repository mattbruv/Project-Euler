from src.helpers.prime import isPrime, primeFactors
from itertools import permutations

nHash = {}

def getHash(pattern, number):
    s = str(number)
    h = ""
    i = -1
    for p in pattern:
        i += 1
        if p == 'n':
            h += s[i]
        else:
            h += '*'
    return h

def unique(pattern, number):
    s = str(number)
    l = []
    i = -1
    for p in pattern:
        i += 1
        if p == '*':
            l.append(s[i])
    return len(set(l))


def test(n):
    string = str(n)
    size = len(string)
    for i in range(1, size):
        #print(i)
        sub = ("n" * i) + (size - i) * '*'
        #print(sub)
        perms = set(list(permutations(sub)))
        for pattern in perms:
            if unique(pattern, n) == 1:
                hStr = getHash(pattern, n)
                #print(hStr)
                if hStr not in nHash:
                    nHash[hStr] = [n]
                else:
                    nHash[hStr].append(n)
                if len(nHash[hStr]) == 8:
                    print(hStr)
                    return nHash[hStr]
    return False


def problem51():
    i = 0
    while True:
        i += 1
        if i % int(1e5) == 0:
            print(i)
        if not isPrime(i):
            continue
        ans = test(i)
        if ans != False:
            print(ans)
            break

# *2*3*3
# [121313, 222323, 323333, 424343, 525353, 626363, 828383, 929393]
# 0:00:58.948372 ELAPSED

"""

print('calculating primes...')
primes = filter(isPrime, range(1, int(1e4)))
print('done finding primes')

def replace(numString, pattern):
    s = ""
    i = 0
    for char in pattern:
        if char == "n":
            s += numString[i]
        i += 1
    return str(int(s))


def problem51():
    primeStrs = map(str, primes)

    digits = 2
    testPrimes = list(filter(lambda x: len(x) == digits, primeStrs))

    print(list(testPrimes))
    for i in range(1, digits):
        testStr = ("n" * i) + ('-' * (digits - i))
        perms = list(permutations(testStr))
        for perm in perms:
            pattern = "".join(perm)
            print(pattern)
            res = map(lambda x: replace(x, pattern), testPrimes)
            print(list(res))
"""

"""
spent a while calculating this algorithm...
was able to find both examples.
2nd example was very slow.

answer is not < 100,000
this algo barely crawls going >100K.
Took 30 mintues to search 56K -> 100k

from src.helpers.prime import isPrime
import itertools

def replaceNumber(number, replace, digit):
    s = str(number)
    i = 0
    newstring = ""
    for i in range(0, len(replace)):
        test = replace[i]
        if test == "n":
            newstring += str(digit)
        else:
            newstring += s[i]
    return int(newstring)

def problem51():
    wantedFamilyCount = 8

    current = 56000 #start here test

    while True:

        string = str(current)
        size = len(string)
        if current % 1000 == 0:
            print(current)

        for i in range(1, size):
            # print(i)
            sub = ("n" * i) + (size - i) * '-'
            # print(sub)
            perms = list(itertools.permutations(sub))
            for p in perms:
                replace = "".join(p)
                primes = []
                for j in range(0, 10):
                    test = replaceNumber(current, replace, j)
                    # print(i, replace, current, test)
                    if isPrime(test) and len(str(test)) == size:
                        primes.append(test)
                if len(primes) >= wantedFamilyCount:
                    print(current, replace, primes)
                    return

        current += 1
"""