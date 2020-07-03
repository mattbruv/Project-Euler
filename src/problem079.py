def problem079(args):
    data = open(args[0]).readlines()
    data = list(map(lambda x: int(x.strip()), data))
    data.sort()
    a = list(set(data))
    a.sort()
    a = list(map(lambda x: str(x) + "\n", a))
    f = open("sorted.txt", "w")
    f.writelines(a)
    f.close()
    # calculated answer by hand using this list