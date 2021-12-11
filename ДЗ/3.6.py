# Создать функцию, которая просто печатает все элементы заданного ей списка:
# НОМЕР J --> ЗНАЧЕНИЕ
# НОМЕР K --> ЗНАЧЕНИЕ
# J, K — порядковые номера в списке

def print_list(my_list):
    i = 0
    while i < len(my_list):
        print(f'Номер {i} --> значение: {my_list[i]}')
        i += 1


print_list(["я", "не", "в", "отпуск", ''])

print('\n')


# Создать функцию, которая печатает каждый элемент словарика
# КЛЮЧ <<J>> --> ЗНАЧЕНИЕ
# КЛЮЧ <<K>> --> ЗНАЧЕНИЕ
# J, K — ключи словарика

def print_dict(my_dict):
    for i in dict.items(my_dict):
        print(i)


print_dict({"key1": 2, "key3": False, "Приветствие": "Hello"})


# Сделать функцию, которая использует две уже написанные функции следующим образом:
# если ЗНАЧЕНИЕ это LIST --> вызывается print_list
# если ЗНАЧЕНИЕ это DICT --> вызывается print_dict
# во всех других случаях просто выводится ЗНАЧЕНИЕ
print ('<-->')
def print_overlord(mydict):
    for i in mydict.values():
        if isinstance(i, list):
            print_list(i)
        elif isinstance(i, dict):
            print_dict(i)
        else:
            print(i)


print_overlord(dict(key1=1,
                    key2=[1, 2, 3, 4],
                    key3='Hello',
                    key4={"ciao": "Mondo", "Привет": "О дивный мир"}))
