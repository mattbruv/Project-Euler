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