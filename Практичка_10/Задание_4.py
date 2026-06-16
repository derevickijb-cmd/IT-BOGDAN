sum = 0
while True:
    product = int(input("Введите цену товара"))
    if product < 0:
        print("Ошибка цены")
    if product > 0:
        sum += product
    if product == 0:
        break
if sum > 1000:
    discount = sum * 0.1
    price = sum - discount
    print(price, "Это итоговая сумма")
else:
    print(sum, "Это итоговая сумма")
