
def problem32():
    pans = []
    ans = 0
    test = "123456789"

    a = 2
    b = 1
    while True:
        prod = a * b
        ss = str(a) + str(b) + str(prod)
        s = ''.join(sorted(ss))

        if len(s) > 9:
            a += 1
            b = 1
            continue

        if s == test: # we found a pandigital
            if prod not in pans:
                pans.append(prod)
                ans += prod
        b += 1
        # found that it hangs on this number
        if a == 9999: 
            break

    print(ans)

# 45228
# 0:00:00.198141 ELAPSED