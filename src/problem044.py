import math


def pent(n):
    return n * (3 * n - 1) // 2

def isPent(x):
    n = (math.sqrt(24 * x + 1) + 1) / 6
    return n == float(round(n))

def problem44():
    pents = list(map(pent, range(1, int(1e4))))

    for j in pents:
        for k in pents:
            add = k + j
            dif = abs(k - j)
            if isPent(add) and isPent(dif):
                print(dif)
                return dif
    
# 5482660
# 0:00:16.834963 ELAPSED