"""
The sequence of triangle numbers is generated by adding the natural numbers.
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
Let us list the factors of the first seven triangle numbers:
 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.
What is the value of the first triangle number to have over five hundred divisors?
"""

import math

def triangleNumber(term):
    num = 0
    while term != 0:
        num += term
        term -= 1
    return num

def numFactors(num):
    factors = 0
    for n in range(1, int(math.sqrt(num)) + 1):
        if num % n == 0:
            factors += 1
            if num // n != n:
                factors += 1
    return factors

def problem12():
    n = 1
    while True:
        tri = triangleNumber(n)
        facs = numFactors(tri)
        if facs > 500:
            print(n)
            print(tri)
            break
        n += 1

# 76576500