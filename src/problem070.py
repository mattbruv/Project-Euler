from src.helpers.prime import totients, sieve, primeFactors


def isPerm(a, b):
    return sorted(str(a)) == sorted(str(b))

def problem070():
    tots = totients(int(1e7))

    minRatio = 9999999999999999
    n = 420

    for i in range(2, int(1e7)):
        if isPerm(i, tots[i]):
            ratio = i / tots[i]
            if ratio < minRatio:
                minRatio = ratio
                n = i
    print(minRatio, n, tots[n])

# 1.0007090511248113 8319823 8313928
# 0:00:40.677327 ELAPSED