
def area(a, b, c):
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5

def problem094():
    limit = int(1e9 / 3) + 2
    print(limit)
    #limit = 10
    total = 0
    for i in range(2, limit):
        for offset in [-1, 1]:
            a = area(i, i, i + offset)
            if a.is_integer():
                # it is equilateral
                perimeter = i + i + (i + offset)
                if perimeter < int(1e9):
                    print(i, a, offset)
                    total += perimeter
    print(total)