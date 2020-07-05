def digitSum(n):
    return sum(map(int, str(n)))

def problem119():
    ns = []
    i1 = 1
    for p in range(2, 40):
        for i in range(2, 100):
            a = i ** p
            if digitSum(a) == i:
                ns.append(a)
                print(str(i) + "^" + str(p), a, i1)
                i1 += 1
    print(sorted(ns)[29])

# 248155780267521
# 0:00:00.048588 ELAPSED