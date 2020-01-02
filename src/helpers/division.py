import math 

def divisors(n):
    fs = []
    sroot = int(math.sqrt(n))
    for i in range(1, sroot + 1):
        if n % i == 0:
            a = n // i
            if i not in fs:
                fs.append(i)
            if a not in fs:
                fs.append(a)
    return fs

def trial_division(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n /= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n /= f
        else:
            f += 2
    if n != 1: a.append(n)
    # Only odd number is possible
    return a