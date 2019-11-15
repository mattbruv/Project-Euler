def rev(number):
    return int(str(number)[::-1])

def canPalindrome(number):
    iterations = 1
    test = number
    while True:
        nrev = rev(test)
        ans = test + nrev
        if ans == rev(ans):
            return iterations
        if iterations >= 50:
            return False
        test = ans
        iterations += 1

def problem55():
    total = 0
    for i in range(0, 10000):
        ans = canPalindrome(i)
        if ans == False:
            total += 1
    print(total)

# 249
# 0:00:00.119007 ELAPSED