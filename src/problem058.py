from src.helpers.prime import isPrime

def calc():
    corner = 1
    size = 2

    nonPrime = [1]
    prime = []
    i = 3

    while True:
        # loop through this layer
        for _ in range(4):
            corner += size
            if isPrime(corner):
                prime.append(corner)
            else:
                nonPrime.append(corner)
        # calculate new ratio
        corners = len(nonPrime) + len(prime)
        primes = len(prime)
        ratio = primes / corners
        print("i=", i, corners, primes, ratio)
        if ratio < 0.10:
            break
        size += 2
        i += 2
    return i


def problem58():
    ans = calc()
    print(ans)

# 26241
# 0:00:19.060090 ELAPSED