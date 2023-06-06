"""Conway's Game of Life, by Al Sweigart al@inventwithpython.com
The classic cellular automata simulation. Press Ctrl-C to stop.
More info at: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: short, artistic, simulation"""

import copy, random, sys, time

WIDTH = 69
HEIGHT = 18

Alive = '#'
Dead = '.'
nextCells = {}
for x in range(WIDTH):
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            nextCells[(x, y)] = Alive
        else:
            nextCells[(x, y)] = Dead

while True:
    print('\n' *50)
    cells = copy.deepcopy(nextCells)

    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(cells[(x,y)], end='')
        print()
    print('Press Ctrl-c to quit.')

    for x in range(WIDTH):
        for y in range(HEIGHT):
            left = (x - 1)% WIDTH
            right = (x+ 1) % WIDTH
            above = (y - 1) % HEIGHT
            below = (y + 1) % HEIGHT

            numNeighbors = 0
            if cells[(left, above)] == Alive:
                numNeighbors += 1
            if cells[(x, above)] ==Alive:
                numNeighbors += 1
            if cells [(right, above)] == Alive:
                numNeighbors += 1
            if cells[(left,y)] == Alive:
                numNeighbors += 1
            if cells[(right,y)] == Alive:
                numNeighbors += 1
            if cells[(left, below)] == Alive:
                numNeighbors += 1
            if cells[(right,below)] == Alive:
                numNeighbors += 1
            if cells [(x, below)] == Alive:
                numNeighbors += 1
            if cells [(x, y)] == Alive and  (numNeighbors == 2or numNeighbors == 3):
                nextCells [(x, y)] = Alive
            elif cells [(x,y)] == Dead and numNeighbors == 3:
                nextCells [(x,y)] = Alive
            else:
                nextCells [(x, y)] = Dead

    try:
        time.sleep(1.3)
    except KeyboardInterrupt:
        print("Conway's Game of Life")
        print('By Al Sweigart al@inventwithpython.com')
        sys.exit()