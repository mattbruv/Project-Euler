from src.helpers.prime import sieve

def getBase(n):
    return int("1" + ("0" * len(str(n))))

def problem135():
    gen = sieve(int(1e7))
    primes = []

    # this includes one prime over 1,000,000 for final test
    # may need to remove it if answer is incorrect.
    for p in gen:
        primes.append(p)
        if p > int(1e6):
            break
    primes.pop(0) # get rid of 2
    primes.pop(0) # get rid of 3

    total = 0

    for i1 in range(0, len(primes) - 1):
        p1 = primes[i1]
        p2 = primes[i1 + 1]
        base = getBase(p1)
        div = 0
        n = p1 + base
        while True:
            if n % p2 == 0:
                div = n
                total += div
                break
            n += base

        print(p1, p2, base, n, div)

    print(total)

# 18613426663617118
# 0:47:20.135441 ELAPSED