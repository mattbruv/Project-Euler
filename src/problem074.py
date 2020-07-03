from math import factorial

def factSum(n):
    ns = [int(x) for x in str(n)]
    return sum(list(map(factorial, ns)))

def factChain(n):
    current = n
    chain = { current }
    isRepeating = False
    while True:
        current = factSum(current)
        if current not in chain:
            chain.add(current)
        else:
            if current == n and len(chain) > 1:
                isRepeating = True
            break
    return (isRepeating, len(chain))

def problem74():
    total = 0
    for i in range(1, int(1e6)):
        repeats, length = factChain(i)
        if not repeats and length == 60:
            total += 1
    print(total)

# 402
# 0:02:00.883914 ELAPSED