input_list = [[1, -2, 3, 0], [-5, 10, -1, 7], [0, 0, -3, 4], [8, -9, 2, -4]]

# Вывод меню
print("=== ФИЛЬТРАЦИЯ ВЛОЖЕННОГО СПИСКА ===")
print("Исходный список:")
print(input_list)

# фильтрация 
filtered_list = []
for sublist in input_list:
    temp = []
    for element in sublist:
        if element > 0:
            temp.append(element)
    filtered_list.append(temp)

# Подсчёт статистики
original_count = 0
filtered_count = 0

for sublist in input_list:
    original_count += len(sublist)

for sublist in filtered_list:
    filtered_count += len(sublist)

deleted_count = original_count - filtered_count

# Вывод результатов
print("\n" + "="*50)
print("ОТФИЛЬТРОВАННЫЙ СПИСОК:")
print(filtered_list)
print("="*50)
print("\nСТАТИСТИКА:")
print(f"Всего элементов в исходном списке: {original_count}")
print(f"Положительных элементов (>0): {filtered_count}")
print(f"Удалено элементов: {deleted_count}")

# Детальный вывод по подспискам
print("\n" + "="*50)
print("ДЕТАЛЬНО ПО ПОДСПИСКАМ:")
for i in range(len(input_list)):
    original = input_list[i]
    filtered = filtered_list[i]
    print(f"Подсписок {i+1}:")
    print(f"  Было: {original}")
    print(f"  Стало: {filtered}")
    print(f"  Положительных: {len(filtered)} из {len(original)}")
    print()  # Это пустая строка для разделения подсписков
# Код заканчивается здесь - больше ничего нет