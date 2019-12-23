def cube(n):
    return n ** 3

def toKey(n):
    return ''.join(sorted(str(n)))

def problem62():
    cubes = {}
    i = 1
    test = []
    while True:
        key = toKey(cube(i))
        perms = cubes.get(key)
        if perms == None:
            cubes[key] = [i]
        else:
            cubes[key].append(i)
            if len(cubes[key]) == 5:
                print(min(map(cube, cubes[key])))
                break
        i += 1

# 127035954683
# 0:00:00.033002 ELAPSED

"""
First attempt, Time unkown:

from itertools import permutations

def cube(n):
    total = 1
    for i in range(0, 3):
        total = total * n
    return total

def problem62():
    cubes = []
    for i in range(0, int(1000)):
        cubes.append(str(cube(i)))

    for i in range(125, 1000):
        print(i)
        n = cube(i)
        perms = permutations(str(n))
        numCubes = 0
        for p in perms:
            s = ''.join(p)
            if s in cubes:
                numCubes += 1
        if numCubes == 5:
            break
    print(i)
"""

"""
Second attempt: 2208 iterations,
!!! CANCELLED EXECUTION AFTER 1:42:40.601367

from itertools import permutations
import math

def cube(n):
    return int(math.pow(n, 3))

def isCube(n):
    if n <= 1:
        return False
    return n == cube(round(n ** (1 / 3)))

def problem62():
    
    i = 2
    while True:
        print(i)
        n = cube(i)

        perms = list(filter(isCube, set(map(lambda x: int(''.join(x)), permutations(str(n))))))

        if len(perms) >= 5:
            lens = list(filter(lambda x: len(str(x)) == len(str(n)), perms))
            if len(lens) == 5:
                print(i, lens)
                break

        # next cube
        i += 1

# 2208 so far
"""