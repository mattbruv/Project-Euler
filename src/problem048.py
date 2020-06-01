def ghettoPower(num, pow):
    total = num
    for i in range(1, pow):
        total = total * num
    return total

def seriesSum(power):
    total = 0
    for i in range(0, power):
        total += ghettoPower(i + 1, i + 1)
    return total

def problem48():
    ans = str(seriesSum(1000))
    print(ans[-10:])

# 9110846700
# 0:00:00.259014 ELAPSED