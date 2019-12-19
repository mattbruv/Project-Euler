def charCode(char):
    return ord(char) - 64

def wordToNum(word):
    ns = list(map(charCode, word))
    return sum(ns)

def tri(n):
    return int(0.5 * n * (n + 1))

def problem42(args):

    triNs = list(map(tri, range(1, 1000)))
    path = args[0]

    f = open(path).read().replace("\"", "").split(",")
    a = wordToNum("SKY")
    i = 0

    for word in f:
        triword = wordToNum(word)
        if triword in triNs:
            i += 1

    print(i)