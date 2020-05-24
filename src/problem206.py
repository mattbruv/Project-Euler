from math import sqrt

def comp(n):
    s = str(n * n)
    cp = ""
    for i in range(0, len(s)):
        if i % 2 == 0:
            cp += s[i]
        else:
            cp += "_"
    return cp == "1_2_3_4_5_6_7_8_9_0"
            

def problem206():
    lower = int(sqrt(1e18))
    upper = int(sqrt(2e18)) + 1
    # print(comp(3259))

    for i in range(lower, upper):
        if i % int(1e6) == 0:
            print(i)
        if comp(i):
            print(i)
            break

# 1389019170
# 0:21:50.173454 ELAPSED