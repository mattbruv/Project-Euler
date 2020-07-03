from src.helpers.prime import primeFactors

def prod(ns):
    total = 1
    for n in ns:
        total *= n
    return total

def rad(n):
    return prod(set(primeFactors(n)))

def e(l, n):
    return l[n-1][0]

def problem124():

    ls = []
    for i in range(1, 100001):
        ls.append([i, rad(i)])
    
    a = sorted(ls, key=lambda sl: (sl[1], sl[0]))
    print(e(a, 10000))