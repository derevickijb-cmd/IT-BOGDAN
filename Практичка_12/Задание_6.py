word = input("Введите слово: ")
chars = list(word)

# Создаем перевернутую копию списка с помощью среза [::-1]
reversed_chars = chars[::-1]

if chars == reversed_chars:
    print("Это палиндром")
else:
    print("Не палиндром")