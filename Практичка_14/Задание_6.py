prices = list(map(int, input("Список, будьте любезны: ").split()))

#Сортировка по возрастанию
ascending = sorted(prices)

#Сортировка по убыванию
descending = sorted(prices, reverse=True)

#Оригинальный порядок
original = prices.copy()

#Обратный порядок
reversed_order = prices[::-1]

print(f"Сортировка по возрастанию: {ascending}")
print(f"Сортировка по убыванию: {descending}")
print(f"Оригинальный порядок (от старых к новым): {original}")
print(f"Обратный порядок (от новых к старым): {reversed_order}")
