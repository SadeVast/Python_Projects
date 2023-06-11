"""Digital Stream, by Al Sweigart al@inventwithpython.com
A screensaver in the style of The Matrix movie's visuals.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: tiny, artistic, beginner, scrolling"""

import random, shutil, sys, time
MIN_STREAM_LENGTH = 6
MAX_STREAM_LENGTH = 14
PAUSE = 0.1
STREAM_CHARS = ['0', '1']
DENSITY = 0.02
WIDTH = shutil.get_terminal_size()[0]
WIDTH -= 1

print('Digital Stream, by Al Sweigart al@inventwithpython.com')
print('Press Ctrl-C to quit.')
time.sleep(2)
try:
    columns = [0] * WIDTH
    while True:
        for i in  range(WIDTH):
            if columns[i] == 0:
                if random.random() <= DENSITY:
                    columns[i] = random.randint(MIN_STREAM_LENGTH,
                                                MAX_STREAM_LENGTH)

            if columns[i] > 0:
                print(random.choice(STREAM_CHARS), end='')
                columns[i] -= 1
            else:
                print(' ', end='')
        print()
        sys.stdout.flush()
        time.sleep(PAUSE)
except KeyboardInterrupt:
    sys.exit()
