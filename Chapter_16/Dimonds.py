def main():
    print('Diamonds, by Al Sweigart al@inventwithpython.com')

    for dimondsSize in range (0, 6):
        displayOutlineDimond(dimondsSize)
        print()
        displayOutFilledDimond(dimondsSize)
        print()

def displayOutlineDimond (size):
    for i in range(size):
        print(' '* (size - i -1 ), end='')
        print('/', end='')
        print(' '* (i * 2), end='')
        print('\\')

    for i in range(size):
        print(' '* i, end='')
        print('\\', end='')
        print(' '* ((size - i -1)*2), end='')
        print('/')

def displayOutFilledDimond(size):
    for i in range(size):
        print(' ' * (size - i - 1), end='')
        print('/' * (i + 1), end='')
        print('\\' * (i + 1))

    for i in range(size):
        print(' ' * i, end='')
        print('\\' * (size - i), end='')
        print('/' * (size - i))

if __name__ == '__main__':
    main()