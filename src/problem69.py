# from src.helpers.division import divisors

def phiGCD(n):
    phi = int(n > 1 and n)
    for p in range(2, int(n ** 0.5) + 1):
        if not n % p:
            phi -= phi // p
            while not n % p:
                n //= p
    #if n is > 1 it means it is prime
    if n > 1:
        phi -= phi // n 
    return phi

"""
cache = {}

def relativePrimes(n):
    ns = cache[n]
    coprimes = []
    for i in range(1, n):
        combined = ns & cache[i]
        if len(combined) == 1:
            coprimes.append(i)
    return coprimes

30030 5.213541666666667
^C!!! CANCELLED EXECUTION AFTER 0:31:19.360074
0:31:19.363531 ELAPSED
"""

def problem69():

    bound = int(1e6)

    maxN = 1
    maxTest = 0
    
    for i in range(1, bound + 1):
        if i % 1000 == 0:
            print(i)
        phi = phiGCD(i)
        if phi != 0:
            test = i / phi
            if test > maxTest:
                maxTest = test
                maxN = i
    print(maxN, maxTest)
    