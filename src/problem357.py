from src.helpers.prime import isPrime, primeFactors
from src.helpers.division import divisors
from math import gcd

print(primeFactors(30))
print(divisors(30))

def problem357(n):
    divs = divisors(n)
    for d in divs:
        a = d + n // d
        if not isPrime(a):
            return False
    return True

tot = 0
for i in range(1, 100_000_000):
    if i % 100_000 == 0:
        print(i)
    if test(i):
        tot += i
print(tot)

# took 2 days to solve ¯\_(ツ)_/¯
# 1739023853137