
JACK = 11
QUEEN = 12
KING = 13
ACE = 14
CARD_DICT = {'T': 10, 'J': JACK, 'Q': QUEEN, 'K': KING, 'A': ACE }

def parseCardNumber(number):
    try:
        return int(number)
    except:
        return CARD_DICT[number.upper()]

def parseCard(card):
    return (parseCardNumber(card[0]), card[1].upper())

def parseHand(hand):
    return list(map(parseCard, hand.split(' ')))

def royalFlush(hand):
    return sorted([x[0] for x in hand]) == [10, JACK, QUEEN, KING, ACE] and flush(hand)

def straightFlush(hand):
    return straight(hand) and flush(hand)

def fourOfAKind(hand):
    return nOfAKind(hand, 4)

def fullHouse(hand):
    return threeOfAKind(hand) and onePair(hand)

def twoPairs(hand):
    return numPairs(hand) == 2

def onePair(hand):
    return numPairs(hand) == 1

def threeOfAKind(hand):
    return nOfAKind(hand, 3)

def highCard(hand):
    return True

def compareHandValue(player1, player2):
    p1 = list(reversed(sorted([x[0] for x in player1])))
    p2 = list(reversed(sorted([x[0] for x in player2])))

    for i in range(0, len(p1)):
        a = p1[i]
        b = p2[i]
        if a == b:
            continue
        if a > b:
            return 1
        else:
            return 2
    return 0

def numPairs(hand):
    nums = [x[0] for x in hand]
    table = {}
    for n in nums:
        table[n] = nums.count(n)
    pairs = []
    for key in table:
        num = table[key]
        if num == 2:
            pairs.append(key)
    return len(pairs)

def nOfAKind(hand, n):
    nums = [x[0] for x in hand]
    count = max([nums.count(x) for x in nums])
    return count >= n

def straight(hand):
    nums = sorted([x[0] for x in hand])
    for i in range(0, len(nums) - 1):
        if nums[i] + 1 != nums[i + 1]:
            return False
    return True

def flush(hand):
    return len(set([x[1] for x in hand])) == 1

def getHandValue(hand):
    fs = [
        royalFlush,
        straightFlush,
        fourOfAKind,
        fullHouse,
        flush,
        straight,
        threeOfAKind,
        twoPairs,
        onePair,
        highCard
    ]
    val = 99
    for i in range(0, len(fs)):
        if fs[i](hand) == True:
            return val
        else:
            val -= 1
    return val

def problem54(args):
    path = args[0]
    f = open(path).readlines()
    score = 0
    enemy = 0
    for line in f:
        cards = line.replace("\n", '').split(' ')
        player1 = parseHand(' '.join(cards[:5]))
        player2 = parseHand(' '.join(cards[5:]))
        val1 = getHandValue(player1)
        val2 = getHandValue(player2)

        if (val1 > val2):
            score += 1
        if (val2 > val1):
            enemy += 1
        if (val1 == val2):
            result = compareHandValue(player1, player2)
            if result == 1:
                score += 1
            else:
                enemy += 1
    print(score, enemy, score + enemy)

# Problem: Pair of 8s needs to beat a pair of 5s. doesn't do that now.