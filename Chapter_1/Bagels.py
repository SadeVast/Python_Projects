"""Бейглз, (c) Эл Свейгарт al@inventwithpython.com
 Дедуктивная логическая игра на угадывание числа по подсказкам.
 Код размещен на https://nostarch.com/big-book-small-python-projects
 Один из вариантов этой игры приведен в книге Invent Your Own
 Computer Games with Python на https://nostarch.com/inventwithpython
 Теги: короткая, игра, головоломка"""

import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def main():
    print('''Bagels,a detective logic game. By Al sweigart
By Al Sweigart al@inventwithpython.com

I am thinking of a {}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say:    That means:
  Pico         One digit is correct but in the wrong position.
  Fermi        One digit is correct and in the right position.
  Bagels       No digit is correct.

For example, if the secret number was 248 and your guess was 843, the
clues would be Fermi Pico.'''.format(NUM_DIGITS))
    while True:
        secretNum = getSecretNum()
        print('I have thought up a number')
        print('You have {} guesses to get it.'. format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess)!= NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}:'.format(numGuesses))
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1
            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print('The answer was {}.'. format(secretNum))
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
        print('Thanks for playing!')



def getSecretNum():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    numbers = list('0123456789')  # Создает список цифр от 0 до 9.
    random.shuffle(numbers)  # Перетасовываем их случайным образом.

    # Берем первые NUM_DIGITS цифр списка для нашего секретного числа:
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    """Возвращает строку с подсказками pico, fermi и bagels
    для полученной на входе пары из догадки и секретного числа."""
    if guess == secretNum:
        return 'You got it!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # Правильная цифра на правильном месте.
            clues.append('Fermi Правильная цифра на правильном месте.')
        elif guess[i] in secretNum:
            # Правильная цифра на неправильном месте.
            clues.append('Pico Правильная цифра на неправильном месте.')
    if len(clues) == 0:
        return 'Bagels Правильных цифр нет вообще.'  # Правильных цифр нет вообще.
    else:
        # Sort the clues into alphabetical order so their original order
        # doesn't give information away.
        clues.sort()
        # Make a single string from the list of string clues.
        return ' '.join(clues)

if __name__ == '__main__':
    main()