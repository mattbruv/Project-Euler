from src.helpers.prime import sieve, isPrime
from math import gcd

""""
    
    generate cubes forever = C
        - for each cube
        generate cube N while N < C
        deduce P from the equation if possible


"""

limit = int(1e6)
primes = set(sieve(limit))

def problem131():
    b = 1 ** 3
    a = 2 ** 3
    diff = a - b
    i = 3
    count = 0
    while diff < int(1e6):
        if isPrime(diff):
            count += 1
        b = a
        a = i ** 3
        i += 1
        diff = a - b
    print(count)


    return

    i = 2
    count = 0
    ratio = 0
    while True:
        cube = i * i * i
        i += 1
        #print(i)
        if ratio != 0:
            lowerBound = int(ratio * i)
        else:
            lowerBound = 1

        for n in range(lowerBound, i - 1):
            n3 = n * n * n
            n2 = n * n
            p = (cube - n3) // n2
            eq = n3 + n2 * p
            if eq == cube:
                if p in primes:
                    count += 1
                    ratio = n / i
                    print("i =", i, "n =", n, "p =", p, eq, "=", cube, count, "below", i)
                    #print(cube - n3 == p * n2)
                    print("p + n", p + n, (p + n ** (1.0 / 3.0)), "\n")
            #print(p, eq, eq == cube)
        if i >= limit:
            break
    print(count, "below", limit)

"""
ratio = 0.3333333333333333 i = 3 n = 1 p = 7 8 = 8
ratio = 0.6153846153846154 i = 13 n = 8 p = 19 1728 = 1728
ratio = 0.7297297297297297 i = 37 n = 27 p = 37 46656 = 46656
ratio = 0.7901234567901234 i = 81 n = 64 p = 61 512000 = 512000
ratio = 0.8537549407114624 i = 253 n = 216 p = 127 16003008 = 16003008
ratio = 0.8988902589395807 i = 811 n = 729 p = 271 531441000 = 531441000
ratio = 0.9082652134423251 i = 1101 n = 1000 p = 331 1331000000 = 1331000000
ratio = 0.9160357880247764 i = 1453 n = 1331 p = 397 3061257408 = 3061257408
ratio = 0.9281791297000422 i = 2367 n = 2197 p = 547 13244763896 = 13244763896
ratio = 0.9330159809588575 i = 2941 n = 2744 p = 631 25412184000 = 25412184000
ratio = 0.9442629252354411 i = 5203 n = 4913 p = 919 140770302408 = 140770302408
ratio = 0.9582578561865007 i = 12697 n = 12167 p = 1657 2046448129536 = 2046448129536
ratio = 0.9599333379626415 i = 14401 n = 13824 p = 1801 2985984000000 = 2985984000000
ratio = 0.9614792935819334 i = 16251 n = 15625 p = 1951 4291015625000 = 4291015625000
14 below 20000
0:02:36.025925 ELAPSED
"""