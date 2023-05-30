"""Calendar Maker, by Al Sweigart al@inventwithpython.com
Create monthly calendars, saved to a text file and fit for printing.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: short"""

import datetime

DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday')

MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December')


print('Calendar Maker, by Al Sweigart al@inventwithpython.com')

while True:
        print('Введите год для календаря:')
        response = input('> ')

        if response.isdecimal() and int(response) > 0:
                year = int(response)
                break

        print('Пожалуйста, введите числовое значение года, например 2023.')
        continue
while True:
        print('Введите месяц для календаря, 1-12:')
        response = input('> ')

        if not response.isdecimal():
                print('Пожалуйста, введите числовой месяц, например, 2 для февраля')
                continue

        month = int(response)
        if 1 <= month <= 12:
                break
        print('Введите число от 1 до 12.')


def getCalendarFor (year,month):
        calText = ''
        calText += ('' * 34) +  MONTHS[month - 1] + ' ' + str(year) + '\n'
        calText += '....Sun.....Mon........Tue........Wed........Thu........Fri.......Sat......\n'
        weekSeparator = ('+----------' * 7) + '+\n'
        blankRow = ('|          ' * 7) + '|\n'
        currentDate = datetime.date(year, month, 1)

        while currentDate.weekday() != 6:
                currentDate -= datetime.timedelta(days=1)

        while True:
                calText += weekSeparator

                dayNumberRow = ''
                for i in range(7):
                        dayNumberLabel = str(currentDate.day).rjust(2)
                        dayNumberRow += '|' + dayNumberLabel + (' '* 8)
                        currentDate += datetime.timedelta(days=1)

                dayNumberRow += '|\n'
                calText += dayNumberRow

                for i in range(3):
                        calText += blankRow

                if currentDate.month != month:
                        break

        calText += weekSeparator
        return calText

calText = getCalendarFor(year, month)
print(calText)

calendarFilename = 'calendar_{}_{}.txt'.format(year, month)
with open(calendarFilename, 'w') as fileObj:
        fileObj.write(calText)
print('Сохранено в ' + calendarFilename)
