"""
Let d(n) be defined as the sum of proper divisors of n
(numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b
are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are
1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
therefore d(220) = 284. The proper divisors of 284 are
1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

def sumOfDivisors(n):
    tot = 0
    for i in range(1, n):
        if n % i == 0:
            tot += i
    return tot

def getAmicables(min, max):
    l = []
    for i in range(min, max):
        a = sumOfDivisors(i)
        b = sumOfDivisors(a)
        if a != b and b == i:
            l.append(a)
    return l

a = getAmicables(2, int(1e4))
print(sum(a))

# 31626