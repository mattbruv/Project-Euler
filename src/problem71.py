from fractions import Fraction
from math import ceil, gcd

def problem71():
    closestFraction = Fraction(numerator=1, denominator=10000)
    target = Fraction(numerator=3, denominator=7)

    # for d in range(1, 9):
    for d in range(1, int(1e6) + 1):
        upperBound = ceil((3 / 7) * d)
        # print(d, upperBound)
        n = upperBound
        while True:
            frac = Fraction(numerator=n, denominator=d)
            if frac >= target:
                n -= 1
                continue
            if frac < closestFraction:
                break
            if gcd(n, d) == 1:
                closestFraction = frac
            n -= 1
    print(closestFraction.numerator)
    #print(closestFraction)
    #print(closestFraction.numerator / closestFraction.denominator, 3 / 7)

# 428570
# 0:00:16.386938 ELAPSED