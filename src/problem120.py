

def r(a, n):
    x = (a - 1) ** n + (a + 1) ** n
    y = a * a
    return x % y

def problem120():
    total = 0
    for a in range(3, 1001):
        rMax = 0
        print(a)
        for n in range(1, 5000):
            rem = r(a, n)
            if rem > rMax:
                rMax = rem
        total += rMax
    print(total)

# 333082500
# 0:21:14.064341 ELAPSED