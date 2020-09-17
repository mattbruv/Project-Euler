from decimal import *
from math import sqrt

def area(a, b, c):
    s = Decimal((a + b + c)) / Decimal(2)
    return Decimal(s * (s - a) * (s - b) * (s - c)).sqrt()

def problem094():
    limit = int(1e9 / 3) + 2
    print(limit)
    total = 0
    for i in range(2, limit):
        for offset in [-1, 1]:
            a = area(i, i, i + offset)
            if a == int(a):
                print(a, i)
                perimeter = i + i + (i + offset)
                if perimeter < int(1e9):
                    total += perimeter
    print(total)

# 518408346
# 2:05:54.694104 ELAPSED