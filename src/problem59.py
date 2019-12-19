import itertools
import math
from collections import Counter

def decrypt(bytelist, key):
    keyrepeat = key * math.ceil((len(bytelist) / 3))

    for i in range(0, len(bytelist)):

        bytelist[i] = bytelist[i] ^ ord(keyrepeat[i])

    return bytelist

def toString(bytelist):
    return ''.join(list(map(chr, bytelist)))

alpha = "abcdefghijklmnopqrstuvwxyz"

def lettersInFreqs(letters, freqs):
    for l in letters:
        if l not in freqs:
            return False
    return True

def problem59(args):
    path = args[0]
    bytelist = list(map(int, open(path).read().split(',')))
    ans = decrypt(bytelist, "exp")
    print(sum(ans))

"""
    keys = []
    # generate keys
    for c1 in range(0, len(alpha)):
        for c2 in range(0, len(alpha)):
            for c3 in range(0, len(alpha)):
                s = alpha[c1] + alpha[c2] + alpha[c3]
                keys.append(s)
    
    for key in keys:
        s = toString(decrypt(bytelist, key)).lower()
        counts = Counter(s.lower()).most_common(1)
        freqs = list(map(lambda x: x[0], counts))
    """