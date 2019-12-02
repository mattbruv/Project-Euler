
def tri(n):
    return n * (n + 1) // 2

def pent(n):
    return n * (3 * n - 1) // 2

def hexo(n):
    return n * (2 * n - 1)

def problem45():
    mn = 285
    bound = 500000
    ts = list(map(tri, range(mn, bound)))
    ps = list(map(pent, range(mn, bound)))
    hs = list(map(hexo, range(mn, bound)))
    
    i = 1
    tes = 1
    while True:
        t = ts[i]
        if t in ps and t in hs:
            tes += 1
            if tes == 2:
                print(t)
                break
        i += 1
        
