import glob
import re
import os

files = glob.glob("src/*.*")
pad = 3

print(list(files))

for f in files:
    print(f)
    x = re.search("([\d]+)", f)
    a = x.group()
    n = int(a)
    sn = str(n)
    name = ("0" * (pad - len(sn))) + sn
    fname = f.replace(a, name)
    os.rename(f, fname)
