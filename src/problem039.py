def mostFrequent(inList):
    return max(set(inList), key = inList.count)

def isRight(a, b, c):
    return (a * a) + (b * b) == (c * c)

def problem39():
    rights = []
    for a in range(1, 1000):
        for b in range(1, 1000):
            if a + b > 1000:
                break
            for c in range(1, 1000):
                p = a + b + c
                if p > 1000:
                    break
                if isRight(a, b, c):
                    rights.append(p)
    print(mostFrequent(rights))

# 840
# 63.57622 SECONDS ELAPSED