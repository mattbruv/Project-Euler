from src.helpers.palindrome import isPalindrome
from math import sqrt

def square(ns):
    return map(lambda x: x * x, ns)

def problem125():
    print(isPalindrome(595))
    maxN = int(1e8)
    maxN = int(1e8)
    nset = set()

    for i in range(1, int(sqrt(maxN))):
        ns = [i, i + 1]
        f = i + 1
        while True:
            result = sum(square(ns))
            #print(ns)
            if result < maxN and isPalindrome(result):
                nset.add(result)
                print(i, ns, sum(square(ns)))
            if result >= maxN:
                break
            f += 1
            ns.append(f)
        #print(i, ns, sum(square(ns)))
    print(sum(nset))

# incorrect first try: 2916867073 without discarding non-unique numbers
# 2906969179
# 0:00:09.599131 ELAPSED