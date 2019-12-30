from src.helpers.prime import isPrime, primeFactors
from itertools import permutations

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