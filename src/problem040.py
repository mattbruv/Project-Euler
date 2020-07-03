def problem40():
    s = "."
    for i in range(1, int(1e6)):
        s += str(i)
    ps = list(map(lambda x: int(s[int(x)]), [1e0, 1e2, 1e3, 1e4, 1e5, 1e6]))
    prod = 1
    for n in ps:
        prod *= n
    print(prod)