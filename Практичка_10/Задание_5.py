count = 1000
while True:
    print("1. Узнать баланс")
    print("2. Снять 100 руб")
    print("3. Положить 100 руб")
    print("4. Выход")
    menu = int(input())
    if menu == 1:
        print(count)
    elif menu == 2:
        if count >= 100:
            count = count - 100
            print("На вашем счету", count, "снято 100")
        else:
            print("Недостаточно средств")
    elif menu == 3:
        count = count + 100
        print(count)
    elif menu == 4:
        print("До свидания!")
        break
