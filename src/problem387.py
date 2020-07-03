from src.helpers.prime import isPrime, primeFactors

def isHarshad(n):
    return n % sum(map(int, str(n))) == 0

def isStrong(n):
    return isPrime(n / sum(map(int, str(n))))

def isTrunc(n):
    while len(str(n)) != 1:
        if not isHarshad(n):
            return False
        n = chop(n)
    return isHarshad(n)

def chop(n):
    s = str(n)
    if len(s) <= 1:
        return n
    return int(str(n)[:-1])

def strongTrunc(n):
    return isTrunc(n) and isStrong(n)

def problem387():
    primes = filter(isPrime, range(1, int(1e5)))
    bases = set()
    total = 0
    for p in primes:
        n = chop(p)
        if strongTrunc(n):
            print(p, str(p)[:2])
            bases.add(str(p)[:2])
            total += p
    #print(total)
    s = list(bases)
    s.sort()
    print(s, len(s))
    print(sum(filter(lambda x: strongTrunc(chop(x)) and isPrime(x), range(1, int(1e4)))))