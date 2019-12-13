import math

def isPrime(n):
    if n <= 1:
        return False
    sqrt = int(math.sqrt(n))
    for i in range(2, sqrt + 1):
        if n % i == 0:
            return False
    return True