def increasing(n):
    ns = list(map(int, str(n)))
    last = ns[0]
    for x in ns:
        if x < last:
            return False
        last = x
    return True

def decreasing(n):
    ns = list(map(int, str(n)))
    last = ns[0]
    for x in ns:
        if x > last:
            return False
        last = x
    return True

def bouncy(n):
    return not increasing(n) and not decreasing(n)

def problem112():
    isBouncy = 0
    notBouncy = 0
    i = 0
    while True:
        i += 1
        if bouncy(i):
            isBouncy += 1
        else:
            notBouncy += 1
        prop = isBouncy / i
        if prop == 0.99:
            print(i)
            break

# 1587000
# 0:00:10.506601 ELAPSED