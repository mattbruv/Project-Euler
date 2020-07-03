from itertools import permutations
from src.helpers.prime import isPrime

def rotate(l, n):
    return l[-n:] + l[:-n]

def isCircular(n):
    s = str(n)
    ns = map(lambda x: int(rotate(s, x)), range(1, len(s) + 1))
    for n in ns:
        if not isPrime(n):
            return False
    return True

def problem35():
    print(len(list(filter(isCircular, range(0, int(1e6))))))

# 55
# 0:00:15.748901 ELAPSED