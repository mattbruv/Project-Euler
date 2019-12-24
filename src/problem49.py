
from src.helpers.prime import isPrime

def isPerm(n, x):
    a = sorted(str(n))
    b = sorted(str(x))
    return a == b

def problem49():
    
    for n in range(1000, 10000):
        if not isPrime(n):
            continue
        for a in range(1000, 10000):
            ns = [n]
            total = n
            while len(ns) != 3:
                total = total + a
                if total > 9999:
                    break
                nextN = total
                if isPrime(nextN) and isPerm(n, nextN):
                    ns.append(nextN)
                else:
                    break
            if len(ns) == 3:
                print(ns)

# [1487, 4817, 8147]
# [2969, 6299, 9629]
# 0:00:16.765959 ELAPSED