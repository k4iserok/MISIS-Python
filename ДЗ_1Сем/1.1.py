s = int(input('Введите число секунд:'))
sutki = s // 86400
if sutki == 1:
    print(sutki, 'сутки')
if sutki >= 2:
    print(sutki, 'суток')
chas = (s - (sutki * 86400)) // 3600
if chas == 1:
    print(chas, 'час')
if chas >= 5:
    print(chas, 'часов')
if (chas > 1) and (chas < 5):
    print(chas, 'часа')
minut = (s - (sutki * 86400) - (chas * 3600)) // 60
if minut == 1:
    print(minut, 'минута')
if (minut > 1) and (minut < 5):
    print(minut, 'минуты')
if minut >= 5:
    print(minut, 'минут')
sec = (s - (sutki * 86400) - (chas * 3600) - (minut * 60))
if sec == 1:
    print(sec, 'секунда')
if (sec > 1) and (sec < 5):
    print(sec, 'секунды')
if sec >= 5:
    print(sec, 'секунд')
print('Проверка GIT')
