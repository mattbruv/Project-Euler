from src.helpers.prime import sieve

def r(pn, n):
    a = ((pn - 1) ** n) + ((pn + 1) ** n)
    b = pn * pn
    return a % b

def problem123():
    primes = sieve(int(1e8))
    print("done generating primes")

    i = 0
    for p in primes:
        a = r(p, i + 1)
        if a > int(1e10):
            print(p, i + 1)
            break
        i += 1

# 237733 21034
# 0:00:02.537812 ELAPSED