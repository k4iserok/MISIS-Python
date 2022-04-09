year = int(input('Введите год: '))
if (year % 400 == 0) or (year % 4 == 0):
    print(year, 'Високосный год')
else:
    print(year, 'Невисокосный год')
