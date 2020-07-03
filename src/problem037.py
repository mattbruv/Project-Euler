import math

def isPrime(n):
    if n == 1:
        return False
    sqrt = int(math.sqrt(n))
    for i in range(2, sqrt + 1):
        if n % i == 0:
            return False
    return True

primes = list(filter(isPrime, range(1, 1000000)))

def truncLeft(number):
    ns = []
    s = str(number)
    while s != "":
        ns.append(int(s))
        s = s[1:]
    return ns

def truncRight(number):
    ls = [int(x) for x in str(number)]
    nums = []
    for i in range(0, len(ls)):
        n = int(''.join(map(str, ls)))
        nums.append(n)
        ls.pop()
    return nums

def isLRPrime(number):
    if len(str(number)) == 1:
        return False
    right = truncRight(number)
    left = truncLeft(number)
    for r in right:
        if not isPrime(r):
            return False
    for l in left:
        if not isPrime(l):
            return False
    return True

def problem37():
    ans = isLRPrime(3797)
    test = list(filter(isLRPrime, primes))
    print(sum(test))

# 748317
# 0:00:20.507173 ELAPSED