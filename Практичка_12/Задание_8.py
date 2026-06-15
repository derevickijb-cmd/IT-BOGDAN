import random

# Создаем список из 5 случайных чисел
numbers = [random.randint(1, 100) for _ in range(5)]

print("Исходный список:", numbers)

# Находим индекс минимального элемента
min_index = 0
for i in range(1, len(numbers)):
    if numbers[i] < numbers[min_index]:
        min_index = i

print(f"Минимальный элемент: {numbers[min_index]} на позиции {min_index}")

numbers[0], numbers[min_index] = numbers[min_index], numbers[0]

print("Список после обмена:", numbers)