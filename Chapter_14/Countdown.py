"""Countdown, by Al Sweigart al@inventwithpython.com
Show a countdown timer animation using a seven-segment display.
Press Ctrl-C to stop.
More info at https://en.wikipedia.org/wiki/Seven-segment_display
Requires sevseg.py to be in the same folder.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: tiny, artistic"""

import sys, time
import sevseg
secondsLeft = 30
try:
    while True:
        print('\n' * 60)
        hours = str(secondsLeft // 3600)
        minutes = str((secondsLeft % 3600) // 60)
        seconds = str(secondsLeft % 60)

        hDigits = sevseg.getSevSegStr(hours, 2)
        hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()

        mDigits = sevseg.getSevSegStr(minutes,2)
        mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()

        sDigits = sevseg.getSevSegStr(seconds,2)
        sTopRow, sMiddleRow, sBottomRow, = sDigits.splitlines()

        print(hTopRow + '     ' + mTopRow + '     ' + sTopRow)
        print(hMiddleRow + '  *  ' + mMiddleRow + '  *  ' + sMiddleRow)
        print(hBottomRow + '  *  ' + mBottomRow + '  *  ' + sBottomRow)

        if secondsLeft == 0:
            print()
            print('   * * * * BOOM * * * *')
            break
        print()
        print('Press Ctrl-C to quit.')
        time.sleep(1)
        secondsLeft -= 1
except KeyboardInterrupt:
    print('Countdown, by Al Sweigart al@inventwithpython.com')
    sys.exit()