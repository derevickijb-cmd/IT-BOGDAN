import random

#Генерация вложенного списка
nested_list = [[random.randint(1, 10) for _ in range(5)] for _ in range(5)]

#Вывод списка
print("Сгенерированный вложенный список:")
for row in nested_list:
    print(row)

#Ввод значения для поиска
target = int(input("\nВведите значение для поиска: "))

#Поиск позиций
positions = []
for i, row in enumerate(nested_list):
    for j, value in enumerate(row):
        if value == target:
            positions.append((i, j))

if positions:
    print(f"\nЭлемент {target} найден на позициях:")
    for i, j in positions:
        print(f"  Строка {i}, столбец {j} (значение: {nested_list[i][j]})")
    print(f"\nВсего найдено: {len(positions)}")
else:
    print(f"\nЭлемент {target} не найден")
