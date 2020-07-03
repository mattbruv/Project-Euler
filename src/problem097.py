def power(x, n):
    p = x
    for i in range(1, n):
        x *= p
    return x

# My original chimpanzee-brain solution.
# it brute forced the answre in an hour
def originalSolution():
    a = 28433
    b = power(2, 7830457)
    c = a * b + 1
    return str(c)[-10:]
# 8739992577
# 3899.28403 SECONDS ELAPSED

def optimizedSolution():
    a = 28433
    for i in range(0, 7830457):
        a *= 2
        a = a % int(1e10)
    return a + 1
# 8739992577
# 4.97828 SECONDS ELAPSED

def problem97():
    print(optimizedSolution())