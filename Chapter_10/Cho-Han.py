"""Cho-Han, by Al Sweigart al@inventwithpython.com
The traditional Japanese dice game of even-odd.
View this code athttps://nostarch.com/big-book-small-python-projects
Tags: short, beginner, game"""

import random, sys
JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

print('''Cho-Han, by Al Sweigart al@inventwithpython.com

В этой традиционной японской игре в кости два кубика бросают в бамбук.
чашка у дилера, сидящего на полу. Игрок должен угадать,
сумма кубиков до четного (cho) или нечетного (han) числа.
''')

money = 5000
while True:
    print('У вас есть', money, 'mon. Сколько вы ставите? (или ВЫЙТИ)')
    while True:
        pot = input('> ')
        if pot.upper() == 'ВЫЙТИ':
            print('Спасибо за игру!')
            sys.exit()
        elif not pot.isdecimal():
            print('Пожалуйста, введите сумму.')
        elif int(pot) > money:
            print('У вас недостаточно денег, чтобы сделать эту ставку.')
        else:
            pot = int(pot)
            break

    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)

    print('Дилер крутит чашку, и вы слышите стук костей.')
    print('Крупье швыряет чашку на пол, по-прежнему закрывая')
    print('кости и просит вашу ставку.')
    print()
    print('    Cho (четное) or Han (нечетное)?')

    while True:
        bet = input('> ').upper()
        if bet != 'CHO' and bet != 'HAN':
            print('Пожалуйста, введите либо "Cho" или "Han".')
            continue
        else:
            break

    print('Дилер поднимает чашку, чтобы показать:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

    rollIsEven = (dice1 + dice2) % 2 == 0
    if rollIsEven:
        correctBet = 'Cho'
    else:
        correctBet = 'Han'


    playerWon = bet ==correctBet

    if playerWon:
        print('Ты выиграл! твоя сумма', pot, 'mon.')
        money = money + pot
        print('игорный стол собирает', pot // 13, 'mon плата.')
        money = money - (pot // 13)
    else:
        money = money - pot
        print('Ты проиграл!')

    if money == 0:
        print('У вас закончились деньги!')
        print('Спасибо за игру!')
        sys.exit()