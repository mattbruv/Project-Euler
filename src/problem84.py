from random import randrange

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

diceSides = 6

GO = 0
JAIL = 10
C1 = 11
E3 = 24
H2 = 39
R1 = 5

def processSquare(nextSquare):
    result = nextSquare
    if nextSquare == 30:
        result = 10
    return result

def communityChest(squareAt):
    squares = [0, 10] 
    return 0

def chance(squareAt):
    BACK = (squareAt - 3) % 40
    squares = [GO, JAIL, C1, E3, H2, R1, BACK]
    return 0

def roll():
    return (randrange(1, diceSides + 1), randrange(1, diceSides + 1))

def problem84():
    turns = int(1e5)
    visits = {}

    for i in range(0, 40):
        visits[i] = 0

    currentSquare = 0 # start on GO
    consecutiveDoubles = 0

    for i in range(0, turns):
        d1, d2 = roll()
        if d1 == d2: # we rolled doubles
            consecutiveDoubles += 1
            if consecutiveDoubles == 3:
                consecutiveDoubles = 0
                currentSquare = 10
        else:
            nextSquare = ((d1 + d2 + currentSquare) % 40)
            currentSquare = processSquare(nextSquare)
        visits[currentSquare] += 1

    print('monopoly odds')
    print(visits)