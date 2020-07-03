import math
import itertools

def toInt(tup):
    s = ""
    for x in tup:
        s += str(x)
    return int(s)

def isPrime(n):
    if n == 1:
        return False
    sqrt = int(math.sqrt(n))
    for i in range(2, sqrt + 1):
        if n % i == 0:
            return False
    return True

def problem41():
    biggest = 0
    for bound in range(1, 10):
        l = list(range(1, bound + 1))
        ns = list(itertools.permutations(l))
        for n in ns:
            num = toInt(n)
            if isPrime(num):
                if num > biggest:
                    biggest = num

    print(biggest)
    # 7652413
    # 2.78016 SECONDS ELAPSED