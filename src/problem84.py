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

def turn(currentSquare):
    nextSquare = randrange(40)
    return nextSquare

def communityChest(squareAt):
    return 0

def chance(squareAt):
    return 0

def problem84():
    turns = int(1e5)
    visits = {}

    for i in range(0, 40):
        visits[i] = 0

    currentSquare = 0 # start on GO
    for i in range(0, turns):
        currentSquare = turn(currentSquare)
        visits[currentSquare] += 1
    print('monopoly odds')
    print(visits)
