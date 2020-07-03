from fractions import Fraction

# here be dragons

def doTest(numer, denom):
    n = str(numer)
    d = str(denom)
    if n == d:
        return False
    
    if sorted(n) == sorted(d):
        return False
    
    if n[1] == '0' or d[1] == '0':
        return False

    if n[0] + n[0] != n and n[0] in d and n[0] + n[0] != d:
        return True
    
    if n[1] + n[1] != n and n[1] in d and n[1] + n[1] != d:
        return True
    return False

def cancel(numer, denom):
    n = str(numer)
    d = str(denom)
    test = n[0]
    if test in n and test in d:
        test = n[0]
    else:
        test = n[1]
    a = n.replace(test, '')
    b = d.replace(test, '')
    return (int(a), int(b))

def problem33():
    prod = 1
    for numer in range (10, 100):
        # start at 50 to ensure ans < 1
        for denom in range(50, 100):
            if doTest(numer, denom):
                a, b = cancel(numer, denom)
                test1 = numer / denom
                test2 = a / b
                if test1 == test2:
                    ans = numer / denom
                    #print(numer, '/', denom, ans)
                    prod *= ans
    foo = Fraction(prod).limit_denominator()
    print(foo.denominator)