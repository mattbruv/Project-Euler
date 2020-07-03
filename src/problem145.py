
def reversible(n):
    a = str(n)
    b = str(int(a[::-1]))
    if len(a) != len(b):
        return False
    y = n + int(b)
    ns = list(map(int, str(y)))
    for x in ns:
        if x % 2 == 0:
            return False
    return True

def problem145():

    total = 0
    for i in range(int(1e9)):
        if i % 1000000 == 0:
            print(i)
        if reversible(i):
            total += 1
    print(total)

# 608720
# 1:34:16.454530 ELAPSED - not proud of this