numbers = [10, 20, 30, 40, 50]
user_number = int(input("Введите число: "))

# Флаг для отслеживания, найдено ли число
found = False

for i in range(len(numbers)):
    if numbers[i] == user_number:
        print(i)
        found = True
        break

if not found:
    print("Нет такого числа")