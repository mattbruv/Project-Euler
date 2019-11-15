def ghettoPower(num, power):
    total = num
    for i in range(1, power):
        total = total * num
    return total

def foo(power):
    n = 1
    digits = []
    while True:
        ans = ghettoPower(n, power)
        length = len(str(ans))
        # print(n, length)
        if length == power:
            digits.append([n, power])
        if length > power:
            break
        n += 1
    return digits

def problem63():
    total = 0
    for i in range(1, 101):
        ans = foo(i)
        n = len(ans)
        total += n
    print(total)

# 49
# 0:00:00.014001 ELAPSED