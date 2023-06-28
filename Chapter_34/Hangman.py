import random, sys

HANGMAN_PICS = [r"""
 +--+
 |  |
    |
    |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
    |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
 |  |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|  |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|\ |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|\ |
/   |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|\ |
/ \ |
    |
====="""]

CATEGORY = 'Country'
WORDS = 'SCOTLAND WALES DENMARK FINLAND NORWAY SWEDEN SWITZERLAND ESTONIA LATVIA AUSTRIA BELGIUM FRANCE GERMANY ITALY NETHERLANDS MEXICO CANADA UKRAINE RUSSIA GREECE SPAIN ROMANIA BULGARIA'.split()

def main():
    print('Hangman, by Al Sweigart al@inventwithpython.com')

    missedLetters = []
    correctLetters = []
    secretWord = random.choice(WORDS)

    while True:
        drawHangman(missedLetters, correctLetters, secretWord)
        guess = getPlayerGuess(missedLetters + correctLetters)

        if guess in secretWord:
            correctLetters.append(guess)
            foundAllLetters = True
            for secretWordLetter in secretWord:
                if secretWordLetter not in correctLetters:
                    foundAllLetters = False
                    break
            if foundAllLetters:
                print('Yes! The secret word is:', secretWord)
                print('You have won!')
                break
        else:
            missedLetters.append(guess)
            if len(missedLetters) == len(HANGMAN_PICS) - 1:
                drawHangman(missedLetters, correctLetters, secretWord)
                print('You have run out of guesses!')
                print('The word was "{}"'.format(secretWord))
                break

def drawHangman(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print('The category is:', CATEGORY)
    print()

    print('Пропущенные буквы: ', end='')
    for letter in missedLetters:
        print(letter, end=' ')
    if len(missedLetters) == 0:
        print('Пропущенных букв пока нет.')
    print()

    blanks = ['_'] * len(secretWord)
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks[i] = secretWord[i]

    print(' '.join(blanks))

def getPlayerGuess(alreadyGuessed):
    while True:
        print('Guess a letter.')
        guess = input('> ').upper()
        if len(guess) != 1:
            print('Пожалуйста, введите одну букву.')
        elif guess in alreadyGuessed:
            print('Вы уже угадали эту букву. Выберите снова.')
        elif not guess.isalpha():
            print('Пожалуйста, введите БУКВУ.')
        else:
            return guess

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
