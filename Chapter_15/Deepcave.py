"""Deep Cave, by Al Sweigart al@inventwithpython.com
An animation of a deep cave that goes forever into the earth.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: tiny, beginner, scrolling, artistic"""
import random, sys, time

WIDTH = 70
PAUSE_AMOUNT = 0.05

print('Deep Cave, by Al Sweigart ')
print('Press Ctrl-C to stop.')
time.sleep(2)
leftWidth = 20
gapWidth = 10
while True:
    rightWidth = WIDTH - gapWidth - leftWidth
    print(('#' * leftWidth)+(' ' * gapWidth)+('#' * rightWidth))
    try:
        time.sleep(PAUSE_AMOUNT)
    except KeyboardInterrupt:
        sys.exit()

    diceRoll = random.randint(1, 6)
    if diceRoll == 1 and leftWidth > 1:
        leftWidth = leftWidth - 1
    elif diceRoll == 2 and leftWidth + gapWidth < WIDTH - 1:
        leftWidth = leftWidth + 1
    else:
        pass

    # diceRoll = random.randint(1, 6)
    # if diceRoll == 1 and gapWidth > 1:
    #      gapWidth = gapWidth - 1
    # elif diceRoll == 2 and leftWidth + gapWidth < WIDTH - 1:
    #      gapWidth = gapWidth + 1
    # else:
    #      pass
