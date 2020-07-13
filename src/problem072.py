from src.helpers.prime import phi, totients

def problem072():
    total = 0
    for i in range(2, int(1e6) + 1):
        total += phi(i)
    print(total)

# 303963552391
# 0:00:57.646297 ELAPSED