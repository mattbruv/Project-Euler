from src.helpers.prime import *
from itertools import takewhile

def to_infinity():
    index = 0
    while 1:
        yield index
        index += 1

def primesFor(a, b):
    return len(list(takewhile(lambda x: isPrime(ans(a, b, x)), to_infinity())))

def ans(a, b, n):
    return (n * n) + (a * n) + b

def problem27():
    maxprimes = 0
    prod = 0
    for a in range(-1000, 1001):
        for b in range(-999, 1000):
            test = primesFor(a, b)
            if test > maxprimes:
                maxprimes = test
                prod = a * b
    print(prod)

# -59231
# 0:00:14.342820 ELAPSED