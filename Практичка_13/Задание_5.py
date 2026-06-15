numbers_string = input()

#Преобразуем строку в список целых чисел
numbers = list(map(int, numbers_string.split()))

#Подсчитываем количество пар
count = 0
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j]:
            count += 1

print(count)