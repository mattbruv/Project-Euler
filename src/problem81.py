import math


example = [[131, 673, 234, 103,  18],
           [201,  96, 342, 965, 150],
           [630, 803, 746, 422, 111],
           [537, 699, 497, 121, 956],
           [805, 732, 524,  37, 331]]
        
# what happens if two paths are equal? Try both?

def numberAt(grid, index):
    bound = len(grid[0]) - 1
    x = index[0]
    y = index[1]
    number = math.inf
    if x >= 0 and x <= bound:
        if y >= 0 and y <= bound:
            number = grid[y][x]
    return number

def getMoves(grid, index):
    x = index[0]
    y = index[1]

    right = (x + 1, y)
    down = (x, y + 1)

    moves = [(right, numberAt(grid, right)), (down, numberAt(grid, down))]
    return moves

def path(grid, index, total):
    bound = len(grid) - 1

    print(numberAt(grid, index))

    if index == (bound, bound):
        return total + numberAt(grid, index)

    moves = getMoves(grid, index)
    nextIndex = index
    lowest = math.inf
    for move in moves:
        score = move[1]
        if score < lowest:
            lowest = score
            nextIndex = move[0]
    return path(grid, nextIndex, total + lowest)


def problem81():
    start = (0, 0)
    ans = path(example, start, 0)
    print(ans)