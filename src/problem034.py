import math

def factSum(n):
    return sum([math.factorial(int(n)) for n in str(n)])


def problem34():
    total = 0
    for i in range(3, int(1e6)):
        if factSum(i) == i:
            total += i
    print(total)

# 40730