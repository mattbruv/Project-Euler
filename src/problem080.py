from decimal import *
import math

# A few gotchas in this problem:
# 1. You need decimals up to 100, but you have
# to make sure the 100th decimal place isn't rounded...
# 2. They failed to say that the digits before the decimal
# need to be included in the answer..

getcontext().prec = 150

def getDigits(n):
    sqrt = Decimal(n).sqrt()
    split = str(sqrt).split('.')
    first = split[0]
    last = split[1][:100 - len(first)]
    combined = first + last
    return sum([int(x) for x in combined])

def isIrrational(n):
    sqrt = int(math.sqrt(n))
    return sqrt * sqrt != n

def problem80():
    ins = filter(isIrrational, range(1, 100))
    print(sum(map(getDigits, ins)))

# 40886
# 0:00:00.015418 ELAPSED
