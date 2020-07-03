def numToList(n):
    ns = [int(x) for x in str(n)]
    ns.sort()
    return ns

def sameDigits(x, curX, maxX, compareList):
    testList = numToList(x * curX)
    if testList == compareList:
        if curX == maxX:
            return True
        return sameDigits(x, curX + 1, maxX, compareList)
    else:
        return False

def problem52():
    result = 0
    i = int(1e5)
    while True:
        iList = numToList(i)
        if sameDigits(i, 2, 6, iList):
            result = i
            break
        else:
            i += 1
    print(result)
