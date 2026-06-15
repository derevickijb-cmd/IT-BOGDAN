n_3 = int(input("Введите количество строк: "))

#Создаем пустой список для всех символов
all_chars = []

# Вводим n строк и добавляем их символы в список
for i in range(n_3):
    line = input(f"Введите строку {i+1}: ")
    all_chars.extend(list(line))

print(all_chars)