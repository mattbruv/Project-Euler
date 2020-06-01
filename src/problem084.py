from random import randrange, shuffle

# board has squares from 00 -> 39
# wraps around at 39

# can land on a community chest or chance squares

"""
card selection says to be done in a FILO stack order.
This may or may not affect squares.
perhaps if I don't get the right answer,
this needs to be cycled as if it were played ingame.
"""

# the three most popular squares, in order,
# are JAIL (6.24%) = Square 10,
# E3 (3.18%) = Square 24,
# and GO (3.09%) = Square 00.
# So these three most popular are the six-digit modal string: 102400.

squareNames = [
    "GO", "A1", "CC1", "A2", "T1", "R1", "B1", "CH1", "B2", "B3",
    "JAIL", "C1", "U1", "C2", "C3", "R2", "D1", "CC2", "D2", "D3",
    "FP", "E1", "CH2", "E2", "E3", "R3", "F1", "F2", "U2", "F3",
    "G2J", "G1", "G2", "CC3", "G3", "R4", "CH3", "H1", "T2", "H2"
]

board = list(zip(squareNames, range(40))) 

ADVANCE_TO_GO = -1
GO_TO_JAIL = -2
GO_TO_NEXT_R = -3
GO_TO_NEXT_U = -4
GO_BACK_3_SQUARES = -5
DO_NOTHING = -6

def index(name):
    for sq, idx in board:
        if name.upper() == sq:
            return idx

def name(index):
    for sq, idx in board:
        if index == idx:
            return sq

# Initialize community chest cards
communityChestCards = [DO_NOTHING] * 16
communityChestCards[0] = ADVANCE_TO_GO
communityChestCards[1] = GO_TO_JAIL
shuffle(communityChestCards)

# Initialize chance cards
chanceCards = [DO_NOTHING] * 16
chanceCards[0] = ADVANCE_TO_GO
chanceCards[1] = GO_TO_JAIL
chanceCards[2] = index("C1")
chanceCards[3] = index("E3")
chanceCards[4] = index("H2")
chanceCards[5] = index("R1")
chanceCards[6] = GO_TO_NEXT_R
chanceCards[7] = GO_TO_NEXT_R
chanceCards[8] = GO_TO_NEXT_U
chanceCards[9] = GO_BACK_3_SQUARES
shuffle(chanceCards)

def nextSquare(current, roll):
    nextSq = (current + roll) % 40

    # if we land on Go To Jail
    if nextSq == index('G2J'):
        nextSq = index('JAIL')

    currentName = name(nextSq)

    # if our next square is a community chest, draw a card
    if 'CC' in currentName:
        nextSq = communityChest(nextSq)
    # if next square is chance, draw card
    if 'CH' in currentName:
        nextSq = chance(nextSq)

    return nextSq

def squareDict():
    s = {}
    for sq, _ in board:
        s[sq] = 0
    return s

def rollDice(sides):
    return (randrange(1, sides + 1), randrange(1, sides + 1))

def communityChest(currentSquare):
    nextSquare = currentSquare
    nextCard = communityChestCards.pop(0)
    if nextCard == ADVANCE_TO_GO:
        nextSquare = index("GO")
    if nextCard == GO_TO_JAIL:
        nextSquare = index("JAIL")
    communityChestCards.append(nextCard)
    return nextSquare

def nextOfType(squareType, current):
    ss = list(filter(lambda x: squareType in x[0], board))
    lowest = min(list(map(lambda x: x[1], ss)))
    nexts = list(filter(lambda x: x[1] > current, ss))
    nextSquare = current
    if len(nexts) == 0:
        nextSquare = lowest
    else:
        nextSquare = nexts[0][1]
    return nextSquare

def chance(currentSquare):
    nextSquare = currentSquare
    nextCard = chanceCards.pop(0)
    if nextCard == ADVANCE_TO_GO:
        nextSquare = index("GO")
    if nextCard == GO_TO_JAIL:
        nextSquare = index("JAIL")
    if nextCard == GO_BACK_3_SQUARES:
        nextSquare = (nextSquare - 3) % 40
        title = name(nextSquare)
        if 'CC' in title:
            nextSquare = communityChest(nextSquare)
        if 'CH' in title:
            nextSquare = chance(nextSquare)
    if nextCard >= 0: # if we drew a normal GOTO
        nextSquare = nextCard
    if nextCard == GO_TO_NEXT_R:
        nextSquare = nextOfType("R", nextSquare)
    if nextCard == GO_TO_NEXT_U:
        nextSquare = nextOfType("U", nextSquare)
    chanceCards.append(nextCard)
    return nextSquare

def simulateGame(diceSides, steps):
    counts = squareDict()
    current = index("GO")
    doubles = 0

    for i in range(steps):
        rollA, rollB = rollDice(diceSides)
        if rollA == rollB:
            doubles += 1
        if doubles >= 3:
            current = index('JAIL')
            doubles = 0
        else:
            current = nextSquare(current, rollA + rollB)
        counts[name(current)] += 1

    return counts

def topSquares(counts):
    names = sorted(counts, key=counts.get, reverse=True)
    amounts = list(map(lambda x: counts[x], names))
    return list(zip(names, amounts))

def problem84():
    ans = simulateGame(4, 100000)
    ts = topSquares(ans)
    foo = ts
    a = list(map(lambda x: index(x[0]), foo))
    print(ts)
    print(a)