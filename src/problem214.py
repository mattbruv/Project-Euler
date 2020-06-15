from math import gcd
import functools
import operator
from src.helpers.prime import isPrime, sieve, primeFactors

def totient(n):
    factors = primeFactors(n)
    phi = n * functools.reduce(operator.mul, [1 - 1 / p for p in set(factors)])
    return int(phi)

def chain(n):
    i = n
    count = 0
    while True:
        count += 1
        if i == 1:
            break
        i = totient(i) 
    return count

def problem214():
    total = 0
    primes = sieve(int(40e6))
    for p in primes:
        print(p)
        if chain(p) == 25:
            print(p)
            total += p
    print(total)
