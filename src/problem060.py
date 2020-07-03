from src.helpers.prime import isPrime, primeFactors
from itertools import combinations, permutations

primes = list(filter(isPrime, range(2, 10000)))

def p(n):
    print(primeFactors(n))
    print(isPrime(n))

def canConcat(ps):
    for a, b in permutations(ps, 2):
        if not isPrime(int(str(a) + str(b))):
            return False
        #else:
        #    print(a, b, str(a) + str(b))
    return True

def problem060():
    #concats = list(filter(canConcat, combinations(primes, 2)))
    #print(concats)
    #print(canConcat((3, 7, 109, 673)))
    #print(len(list(combinations(primes, 2))))
    #print(len(concats))
    combos = {}
    for a, b in filter(canConcat, combinations(primes, 2)):
        if a not in combos:
            combos[a] = set()
        if b not in combos:
            combos[b] = set()
        combos[a].add(b)
        combos[b].add(a)

    answers = []
    
    for c in sorted(map(int, combos.keys())):
        print("testing", c, combos[c])
        #setTest = combos[c]
        #setTest.add(c)
        a = set(combos[c])
        for n in combos[c]:
            b = set(combos[n])
            #print(comp)
            comp = a.intersection(b)
            comp.add(c)
            comp.add(n)
            if len(comp) >= 5:
                #print(c, n, a.intersection(b))
                if canConcat(comp):
                    print(comp, "\n")
                    if comp not in answers:
                        answers.append(comp)
        #break
        """
        n = combinations(setTest, 4)
        for x in n:
            if c not in x:
                continue
            #print(x)
            if canConcat(x):
                if set(x) not in answers:
                    answers.append(set(x))
                print("\n", x, "\n")
        """
    
    for a in answers:
        print(a, sum(a))

# {8389, 5701, 6733, 5197, 13} 26033
# 0:01:52.054409 ELAPSED