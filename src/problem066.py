import math

def is_square(n):
    sqrt = math.sqrt(n)
    return (sqrt - int(sqrt)) == 0

def solve(d, x, y):
    return (x * x) - (d * (y * y))

def findSolution(d):
    found = False
    x = 1
    while not found:
        y = round(math.sqrt((x * x) / d)) or 1
        if solve(d, x, y) == 1:
            found = True
            break
        x += 1

    return [x, d, y]

"""
def findSolution(d):
    found = False
    x = 2
    y = 1
    while not found:
        bound = x * x
        # print(d, bound, x, y)
        y = 1
        while True:
            bTest = (y * y) #originally with d
            if bTest > (bound / d):
                break
            if solve(d, x, y) == 1:
                found = True
                break
            y += 1
        if not found:
            x += 1

    return [x, d, y]
"""

D = list(filter(lambda x: not is_square(x), range(2, 100)))

def problem66():
    ans = []
    print(findSolution(202))
    """
    for dn in D:
        print(dn)
        print(findSolution(dn))
    print(ans)
    """