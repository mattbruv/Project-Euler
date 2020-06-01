from src.helpers.prime import *

def primeSum(primes, bound):
    maxList = len(primes) - 1
    i = 0
    cons = []
    while True:
        j = i
        test = []
        maxSoFar = []
        while True:
            if j > maxList:
                break

            p = primes[j]
            maxSoFar.append(p)
            ans = sum(maxSoFar)
            if ans > bound:
                break
            if ans in primes and len(maxSoFar) > len(test):
                test = maxSoFar.copy()
            j += 1
        
        if len(test) > len(cons):
            cons = test

        i += 1
        if i > maxList:
            break
    return cons

def problem50():
    primes = list(filter(isPrime, range(1, 1000000)))
    print('done generating primes...')
    ans = primeSum(primes, 1000000)
    print(ans)
    print(len(ans))
    print(sum(ans))
