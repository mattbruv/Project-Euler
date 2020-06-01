import math

def isPrime(n):
    if n == 1:
        return False
    sqrt = int(math.sqrt(n))
    for i in range(2, sqrt + 1):
        if n % i == 0:
            return False
    return True

primes = list(filter(isPrime, range(1, 100000)))

def conject(number):
    for p in primes:
        if p > number:
            return False
        square = 1
        while True:
            test = p + 2 * (square * square)
            if (square * square) > number:
                break
            if test == number:
                return (number, p, square)
            square += 1
    return False

def nextComposite(n):
    test = n + 1
    while True:
        if not isPrime(test):
            if test % 2 != 0:
                return test
        test += 1

def problem46():
    n = nextComposite(2)
    while True:
        if conject(n) == False:
            print(n)
            break
        else:
            n = nextComposite(n)

# 5777
# 0:00:03.862221 ELAPSED