file_path = input("Введите полное имя файла: ")

# Разбиваем строку по символу \
parts = file_path.split('\\')

# Выводим каждую часть в отдельной строке
for part in parts:
    print(part)