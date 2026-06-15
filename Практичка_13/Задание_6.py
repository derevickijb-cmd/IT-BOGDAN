numbers = [8, 9, 10, 11]

#Заменил второй элемент списка на 17
numbers[1] = 17
print("После замены 2-го элемента:", numbers)


numbers.extend([4, 5, 6]) 
print("После добавления 4,5,6:", numbers)

#Удалил первый элемент списка
del numbers[0] 
print("После удаления первого элемента:", numbers)


numbers.extend(numbers) 
print("После удвоения списка:", numbers)

#Вставил число 25 по индексу 3
numbers.insert(3, 25)

print("После вставки 25 по индексу 3:", numbers)
print("\nИтоговый список:", numbers)