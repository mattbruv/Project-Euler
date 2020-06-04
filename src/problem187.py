from src.helpers.prime import primeFactors

def problem187():
    tot = 0
    for i in range(1, int(1e8)):
        if i % 100_000 == 0:
            print(i, tot)
        if len(primeFactors(i)) == 2:
            tot += 1
    print(tot)

# 11 hours 32 minutes to find the correct answer