from src.helpers.division import divisors


def problem179():
    total = 0
    for i in range(2, int(1e7)):
        n1 = len(divisors(i))
        n2 = len(divisors(i + 1))
        if n1 == n2:
            total += 1
    print(total)