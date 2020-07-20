from src.helpers.prime import primeFactors, sieve
from itertools import combinations

def problem347():
    limit = int(1e7)

    tot = 0
    found = {}
    for i in range(1, limit + 1):
        s = frozenset(primeFactors(i))
        if len(s) == 2:
            if s not in found:
                found[s] = i
            else:
                if i > found[s]:
                    found[s] = i
        #print(i, s)
    total = 0
    for f in found:
        # print(f, found[f])
        total += found[f]
    print(total)

# 11109800204052
# 0:25:43.880305 ELAPSED