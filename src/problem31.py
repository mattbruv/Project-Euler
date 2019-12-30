
coins = [1, 2, 5, 10, 20, 50, 100, 200]
ways = [0] * 201

def problem31():
    ways[0] = 1
    for coin in coins:
        for i in range(coin, 201):
            ways[i] += ways[i - coin]
    print(ways[200])