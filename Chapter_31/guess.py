import random

def askForGuess():
    while True:
        guess = input('> ')

        if guess.isdecimal():
            return int(guess)
        print('Введите число от 1 до 100.')

print('Guess the Number, by Al Sweigart al@inventwithpython.com')
print()

secretNumber = random.randint(1, 100)
print('Я думаю о числе от 1 до 100.')

for i in range(10):
    print('У тебя {} попыток. Пробуй!'.format(10 - i))

    guess = askForGuess()
    if guess == secretNumber:
        break
    if guess < secretNumber:
        print('Холоднее')
    if guess > secretNumber:
        print('Теплее!')

if guess == secretNumber:
    print('Ура! Вы угадали мою цифру!')
else:
    print('Игра окончена. Число, о котором я думал, было',secretNumber)