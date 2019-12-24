import math

def div(number, divisor):
    i = 0
    temp = number
    divs = []

    # a list of visited temp numbers.
    # when we hit a temp number twice, we know we will end back up there
    # again eventually.
    visited = {}

    # counts the times since the last seen thing
    beenHereBefore = False
    cycleCounter = 0

    while True:
        # shift over the tens place while we can't divide it.
        while temp < divisor:
            temp *= 10
        
        # we have a new temp. add it to the dictionary
        seen = visited.get(temp)
        if seen is None:
            #print('never seen this before!', temp)
            visited[temp] = 1
        else:
            visited[temp] += 1
            seen = visited.get(temp)
            if seen == 2:
                cycleCounter += 1
            if seen == 3:
                print(number, '/', divisor, 'recurrs', cycleCounter, 'times.')
                return cycleCounter
        # times divisor can go into temp number
        times = temp // divisor
        #print(temp)
        divs.append(times)
        #print(divisor, "goes into", temp, times, "times.")
        remainder = temp - (divisor * times)
        temp = remainder
        #print("remainder", remainder)
        if remainder == 0:
            return cycleCounter

def problem26():
    longest = 0
    index = 0
    for i in range(1, 1000):
        test = div(1, i)
        if test > longest:
            longest = test
            index = i
    print(index)