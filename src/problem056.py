def ghettoPower(num, power):
    total = num
    for i in range(1, power):
        total = total * num
    return total

def sumDigits(number):
    s = [int(c) for c in str(number)]
    return sum(s)

def problem56():
    biggest = 0
    for a in range(0, 100):
        for b in range(0, 100):
            ans = ghettoPower(a, b)
            digitSum = sumDigits(ans)
            if digitSum > biggest:
                biggest = digitSum
    print(biggest)

# 972
# 0:00:00.347020 ELAPSED