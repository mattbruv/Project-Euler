from itertools import permutations

primes = [2, 3, 5, 7, 11, 13, 17]

def hasProperty(nStr):
    for i in range(1, 8):
        s = nStr[i] + nStr[i + 1] + nStr[i + 2]
        n = int(s)
        p = primes[i - 1]
        if n % p != 0:
            return False
    return True

def stringify(tup):
    s = ""
    for i in tup:
        s += str(i)
    return s

def problem43():
    total = 0
    ps = list(permutations(range(0, 10)))
    for tup in ps:
        s = stringify(tup)
        if hasProperty(s):
            total += int(s)
    print(total)

# 16695334890
# 0:00:25.243444 SECONDS ELAPSED