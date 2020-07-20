from math import gcd
from src.helpers.prime import totients, sieve, phi

lookup = {}

def chain(n):
    start = n
    count = 1
    if n == 1:
        return 1
    while n != 1:
        count += 1
        n = phi(n)
        if n in lookup:
            return count + lookup[n]
    lookup[start] = count - 1
    return count

def problem214():
    #primes = sieve(40_000_000)
    #print('done generating primes')
    limit = 40_000_000
    chainLength = 25
    #print(len(primes))
    primes = sieve(limit)
    total = 0
    for p in primes:
        print(p, p / int(40e6) * 100)
        if chain(p) == chainLength:
            print(p, total)
            total += p
    print(total)