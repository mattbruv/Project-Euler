from fractions import Fraction

def cycle(n):
    acc = Fraction(numerator=1, denominator=2)
    while n > 1:
        acc = Fraction(numerator=1, denominator=(Fraction(2) + acc))
        n -= 1
    return Fraction(1) + acc

def problem57():
    i = 0
    for n in range(1, 1001):
        f = cycle(n)
        if len(str(f.numerator)) > len(str(f.denominator)):
            i += 1
    print(i)

# 153
# 0:00:14.386823 ELAPSED