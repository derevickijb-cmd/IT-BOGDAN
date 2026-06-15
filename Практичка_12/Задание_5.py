data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

#Первая тройка чисел [10, 20, 30]
first_three = data[0:3]  # или data[:3]
print("Первая тройка:", first_three)

#Последняя тройка чисел [80, 90, 100]
last_three = data[-3:]  # или data[7:10]
print("Последняя тройка:", last_three)

reversed_list = data[::-1]
print("В обратном порядке:", reversed_list)

odd_indexes = data[1::2]  
print("Элементы с нечетными индексами:", odd_indexes)