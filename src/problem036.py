def rev(str):
    return str[::-1]

def problem36():
    total = 0
    for i in range(1, int(1e6)):
        s = str(i)
        if s == rev(s):
            b = bin(i)[2:]
            if b == rev(b):
                total += i
    print(total)
