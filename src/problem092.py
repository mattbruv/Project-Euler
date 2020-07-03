def nextChain(num):
    return sum([int(n) * int(n) for n in str(num)])

def chain(n):
    l = [n]
    while True:
        n = nextChain(n)
        l.append(n)
        if n == 89 or n == 1:
            val = n
            break
    return val

def problem92():
    total = 0
    for i in range(1, 10000000):
        if chain(i) == 89:
            total += 1
    print(total)

# 8581146
# 235 seconds to calculate XD
# programmer time > cpu time amirite XD