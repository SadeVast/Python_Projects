"""Моделирование парадокса дня рождения, Эл Свейгарт al@inventwithpython.com
Исследуйте удивительные вероятности «парадокса дня рождения».
Больше информации на https://en.wikipedia.org/wiki/Birthday_problem.
Этот код доступен по адресу https://nostarch.com/big-book-small-python-programming.
Теги: короткая, математика, симуляция"""
import datetime, random

def getBirthday(numberOfBirthdays):
    birthdays = []
    for i in range(numberOfBirthdays):
        starOfYear = datetime.date(2023,1,1)
        randomNumberOfDays = datetime.timedelta(random.randint(0,364))
        birthday = starOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays

def getMatch(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None

    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1 :]):
            if birthdayA  == birthdayB:
                return birthdayA


print('''Birthday Paradox, by Al Sweigart al@inventwithpython.com

The birthday paradox shows us that in a group of N people, the odds
that two of them have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation (that is, repeated random
simulations) to explore this concept.

(It's not actually a paradox, it's just a surprising result.)
''')

MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True:
    print('How many birthdays shall I generate? (Max 100)')
    response = input('> ')
    if response.isdecimal() and (0< int(response)<=100):
        numBdays = int(response)
        break
print()

print(f'Here are {numBdays} birthdays:')
birthdays = getBirthday(numBdays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(', ', end='')
    monthName = MONTHS[birthday.month - 1]
    dateText = '{} {}'.format(monthName,birthday.day)
    print(dateText, end='')
print()
print()

match = getMatch(birthdays)

print('In this simulation, ', end='')
if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = '{} {}'.format(monthName,match.day)
    print(f'multiple people have a birthday on {dateText}')
else:
    print('there are no matching dirthdays.')
print()

print(f'Generating {numBdays} random birthdays 100,000 times...')
input('Press Enter to begin...')

print('Let\'s run another 100,000 simulations.')
simMatch = 0
for i in range (100_000):
    if i % 10_000 == 0:
        print(i, 'simulations run...')
    birthdays = getBirthday(numBdays)
    if getMatch(birthdays) != None:
        simMatch = simMatch + 1
print('100,000 simulations run.')

probability = round(simMatch / 100000 * 100, 2)
print(f"""Out of 100,000 simulations of {numBdays} people, there was a matching birthday in that group {simMatch} times. 
    This means that {numBdays} people have a {probability}% chance of having a matching birthday in their group.
    That\'s probably more than you would think!""")
