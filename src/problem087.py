from src.helpers.prime import isPrime
from itertools import combinations, combinations_with_replacement, product
from math import sqrt

def psum(a, b, c):
    return a * a + b * b * b + c * c * c * c

def primeSumsBelow(limit):
    maxPrime = int(sqrt(limit)) + 1
    print("max prime:", maxPrime)
    primes = filter(isPrime, range(1, maxPrime))
    count = 0
    found = set()
    for combo in product(primes, repeat=3):
        n = psum(combo[0], combo[1], combo[2])
        if (n < limit):
            if n not in found:
                print(combo)
                count += 1
                found.add(n)
    return count

def problem087():
    total = 0
    a = 1
    b = 1
    #primes = list(filter(isPrime, range(1, 7072))) # >sqrt of 50mil
    print(primeSumsBelow(50_000_000))