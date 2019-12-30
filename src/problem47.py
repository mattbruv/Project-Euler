from src.helpers.prime import primeFactors

def flatten(factors):
    flat = []
    done = []
    for f in factors:
        if f in done:
            continue
        done.append(f)
        count = factors.count(f)
        flat.append(f ** count)
    return flat

def problem47():

    distinctSearch = 4
    factsSoFar = []
    i = 2
    while True:
        factors = flatten(primeFactors(i))

        if len(factors) == distinctSearch:
            factsSoFar.append((i, factors))
            if len(factsSoFar) == distinctSearch:
                break
        else:
            factsSoFar = []

        # next number
        i += 1

    print(factsSoFar)
    print(factsSoFar[0][0])

# [(134043, [3, 7, 13, 491]),
#  (134044, [4, 23, 31, 47]),
#  (134045, [5, 17, 19, 83]),
#  (134046, [2, 9, 11, 677])]

# 134043
# 0:00:02.258279 ELAPSED