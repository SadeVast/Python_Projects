print('Gullible, by Al Sweigart al@inventwithpython.com')

while True:
    print('Хотите знать, как занять доверчивого человека на несколько часов? Да/Нет')
    response = input('> ')
    if response.lower() == 'нет' or response.lower() == 'н':
        break
    if response.lower() == 'да' or response.lower() == 'д':
        continue
    print('"{}" is not a valid да/нет response.'.format(response))

print('Спасибо! Хорошего дня!)')