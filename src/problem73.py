from fractions import Fraction
# from src.helpers.division import GCD
from math import gcd

def problem73():
    total = 0
    lowerBound = Fraction(numerator=1, denominator=3)
    upperBound = Fraction(numerator=1, denominator=2)
    for d in range(1, 12001):
    #for d in range(1, 9):
        if d % 100 == 0:
            print(d)
        half = d // 2
        if half <= 1:
            continue
        # print(f > lowerBound) possibly >=
        # print(f < upperBound)
        n = half
        while True:
            f = Fraction(numerator=n, denominator=d)
            if f == upperBound: #skip if half
                #print(f, 'equals', upperBound)
                n -= 1
                continue
            if f <= lowerBound:
                #print(f, 'lower than', lowerBound)
                break
            if gcd(n, d) == 1:
                #print(f)
                total += 1
            n -= 1
    print(total)

# 7295372
# 0:06:42.664031 ELAPSED (with custom GCD code)
# 0:01:33.749362 ELAPSED (with python GCD code)