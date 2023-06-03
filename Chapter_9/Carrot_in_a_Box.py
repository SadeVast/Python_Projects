"""Carrot in a Box, by Al Sweigart al@inventwithpython.com
A silly bluffing game between two human players. Based on the game
from the show, 8 Out of 10 Cats.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: large, beginner, game, two-player"""

import random

print('''Carrot in a Box, by Al Sweigart al@inventwithpython.com

Это блефовая игра для двух игроков. У каждого игрока есть коробка.
В одной коробке есть морковка. Чтобы выиграть, у вас должна быть коробка с морковью.

Это очень простая и глупая игра.

Первый игрок смотрит в свою коробку (второй игрок должен закрыть
глаза во время этого.) Затем первый игрок говорит: «Есть морковка
в моей коробке» или «В моей коробке нет морковки». Затем второй игрок
решает, хотят ли они поменять коробки местами или нет.
''')

input('Нажмите Enter что бы начать...')

p1Name = input('Игрок 1, введите свое имя: ')
p2Name = input('Игрок 2, введите свое имя: ')
playerNames = p1Name[:11].center(11) + '    ' + p2Name[:11].center(11)

print('''ВОТ ДВЕ КОРОБКИ:
  __________     __________
 /         /|   /         /|
+---------+ |  +---------+ |
|   RED   | |  |   GOLD  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/''')

print()
print(playerNames)
print()
print(p1Name + ', перед вами RED коробка.')
print(p2Name + ', у вас есть GOLD коробка перед вами.')
print()
print(p1Name + ', ты заглянешь в свою коробку.')
print(p2Name.upper() + ', закрой глаза и не смотри!!!')
input('Когда ' + p2Name + ' закрыли глаза, нажмите Enter...')
print()

print(p1Name + ' вот внутренняя часть вашей коробки:')

if random.randint(1,2) == 1:
    carrotInFirstBox = True
else:carrotInFirstBox = False

if carrotInFirstBox:
    print('''
   ___VV____
  |   VV    |
  |   VV    |
  |___||____|    __________
 /    ||   /|   /         /|
+---------+ |  +---------+ |
|   RED   | |  |   GOLD  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/
 (морковь!)''')
    print(playerNames)
else:
    print('''
   _________
  |         |
  |         |
  |_________|    __________
 /         /|   /         /|
+---------+ |  +---------+ |
|   RED   | |  |   GOLD  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/
(нет моркови!)''')
    print(playerNames)

input('Нажмите Enter что бы продолжить...')

print('\n' * 100)
print(p1Name + ', скажите одно из следующих предложений, чтобы ' + p2Name + '.')
print('  1) В моей коробке есть морковь.')
print('  2) В моей коробке нет морковки.')
print()
input('Затем нажмите Enter, чтобы продолжить...')

print()
print(p2Name + ', ты хочешь поменяться коробками с ' + p1Name + '? YES/NO')

while True:
    response = input('> ').upper()
    if not (response.startswith('Y') or response.startswith('N')):
        print(p2Name + ', Пожалуйста, введите "Yes" или "NO".')
    else:
        break

firstBox = 'RED '
secondBox = 'COLD'
if response.startswith('Y'):
    carrotInFirstBox = not carrotInFirstBox
    firstBox, secondBox = secondBox, firstBox

print('''ВОТ ДВЕ КОРОБКИ:
  __________     __________
 /         /|   /         /|
+---------+ |  +---------+ |
|   {}    | |  |   {}    | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/'''.format(firstBox, secondBox))
print(playerNames)

input('Нажмите Enter, чтобы выявить победителя...')
print()

if carrotInFirstBox:
    print('''
   ___VV____      _________
  |   VV    |    |         |
  |   VV    |    |         |
  |___||____|    |_________|
 /    ||   /|   /         /|
+---------+ |  +---------+ |
|   {}    | |  |   {}    | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/'''.format(firstBox, secondBox))

else:
    print('''
   _________      ___VV____
  |         |    |   VV    |
  |         |    |   VV    |
  |_________|    |___||____|
 /         /|   /    ||   /|
+---------+ |  +---------+ |
|   {}    | |  |   {}    | |

|   BOX   | /  |   BOX   | /
+---------+/   +---------+/'''.format(firstBox, secondBox))

print(playerNames)

if carrotInFirstBox:
    print(p1Name + ' победитель!')
else:
    print(p2Name + ' победитель!')

print('Спасибо за игру!')