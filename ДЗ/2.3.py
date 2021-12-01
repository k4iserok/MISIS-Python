file = 'Моя диссертац.gif'
extensions = ['png', 'jpg', 'jpeg', 'gif', 'svg']
e = (file[:-4:-1])[::-1]
if e in extensions:
    print('Расширение файла: ' + e)
else:
    print('Вашего расширения нет в списке')
