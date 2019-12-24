def toInt(line):
    l = line.split(',')
    return list(map(int, l))

def pow(x, n):
    print(n)
    if n < 0:
        return pow(1 / x, -n)
    elif n == 0:
        return 1
    elif n == 1:
        return x
    elif n % 2 == 0:
        return pow(x * x, n / 2)
    else:
        return x * pow(x * x, (n - 1) / 2)

def problem99(args):
    f = open(args[0])
    nums = list(map(toInt, f.readlines()))

    biggest = -1 
    biggestNum = 0

    for i in range(0, len(nums)):
        print("\nCALCULATE", i)
        a = nums[i][0]
        b = nums[i][1]
        n = pow(a, b)
        if n > biggestNum:
            biggestNum = n
            biggest = i
            print("NEW BIGGEST ROW:", biggest)
        print("{}% Done..".format(i / len(nums) * 100))
    
    print("ALL DONE, BIGGEST: ", biggest + 1)

# ALL DONE, BIGGEST:  709
# 5:02:21.550340 ELAPSED
# I am not a smart man