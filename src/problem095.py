from src.helpers.division import divisors

def divSum(n):
    if n <= 1:
        return 1
    ds = divisors(n)
    return sum(ds) - n

def chain(n):
    chainset = { n }
    nextChain = n
    isChain = False
    while True:
        nextChain = divSum(nextChain)
        if nextChain == 1:
            break
        if nextChain > int(1e6):
            break
        if nextChain not in chainset:
            chainset.add(nextChain)
        else:
            if nextChain == n:
                isChain = True
            break
    return (isChain, chainset)

def problem95():
    longestChain = 0
    smallestN = int(1e6)
    chainI = 0
    for i in range(int(1e6)):
        if i % 10000 == 0:
            print(i)
        ans = chain(i)
        if ans[0] == True: # if a chain
            theChain = ans[1]
            length = len(theChain)
            if length > longestChain:
                #print(i, theChain)
                longestChain = length
                chainI = i
                smallestN = min(theChain)
    print(chainI, longestChain, smallestN)

# 14316 28 14316
# 0:05:45.447602 ELAPSED