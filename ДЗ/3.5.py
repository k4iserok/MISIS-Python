# Нужно проверить, все ли числа в последовательности уникальны.
numbers = [1, 4, 5,]
N = len(numbers)
for i in range(N-1):
    for j in range(i+1, N):
        if numbers[i] == numbers[j]:
            print(f'Есть одинаковые: {numbers[i]}')
        elif numbers[i] != numbers[j]:
            print("Все элементы уникальны") #надо перенести

