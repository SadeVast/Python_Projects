import math, sys
print('''Множители заданного числа — другие
два числа, произведение которых дает это заданное число. Например,
2 × 13 = 26, так что 2 и 13 — множители 26. Кроме того,
1 × 26 = 26, так что 1 и 26 — также множители 26. Следовательно, у 26 четыре множителя: 1, 2, 13 и 26.
Число, у которого только два множителя: 1 и оно само, называется простым.
В противном случае оно называется составным. Найдите
новые простые числа с помощью нашей программы разложения на множители''')

while True:
    print('Enter a positive whole number to factor (or QUIT):')
    response = input('> ')
    if response.upper() == 'QUIT':
        sys.exit()
    if not (response.isdecimal()and int(response) > 0):
        continue
    number = int(response)

    factors = []
    for i in range (1, int(math.sqrt(number))+1):
        if number % i == 0:
            factors.append(i)
            factors.append(number // i)

    factors = list(set(factors))
    factors.sort()
    for i, factor in enumerate(factors):
        factors[i] = str(factor)
    print(','.join(factors))