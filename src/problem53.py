from itertools import combinations
from math import factorial

def nChooseR(n, r):
    num = factorial(n)
    dom = factorial(r) * factorial(n - r)
    return num // dom

def problem53():
    total = 0
    for n in range(1, 101):
        for r in range(0, n + 1):
            res = nChooseR(n, r)
            if res > int(1e6):
                total += 1
    print(total)

# 4075
# 0:00:00.035002 ELAPSED