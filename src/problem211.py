from src.helpers.division import divisors
import math

def f(n):
    return sum(map(lambda x: x * x, divisors(n)))

def isSquare(n):
    return math.sqrt(n).is_integer()

def problem211():
    total = 0
    for i in range(1, 64_000_000):
        if i % 100_000 == 0:
            print(i, i / int(64e6) * 100)
        if isSquare(f(i)):
            total += i
    print(total)

# 1922364685
# 14:28:24.920231 ELAPSED - lol