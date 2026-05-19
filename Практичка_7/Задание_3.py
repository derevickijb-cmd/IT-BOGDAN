print("Здравствуйте! Пожалуйста, все напитки из нашего меню: 1.Лимонад, 2.Кофе, 3.Чай, 4.Вода, 5.Сок")
menu = int(input("Что бы вы хотели?(напишите цифру от одного до трёх)"))
quality = int(input("Сколько порций? К сожалению можно выбрать до 10 порций каждого напитка"))
sale = input("Напишите код скидки: ")
TEA = 100
COFFEE = 150
LIMONADE = 200
WATER = 50
JUICE = 150

print("_"*36)
match menu:
    case 1:
        print("|", " "*5, "🍹 Квитанция Кафе 🍹", " "*5, "|")
        print("_"*36)
        print()
        print("Товар: Лимонад 🍹")
        print(f"Цена за порцию: {LIMONADE}")
        match quality:
            case 1:
                print(f"Количество: {quality} порция")
            case 2|3|4:
                print(f"Количество: {quality} порции")
            case 5|6|7|8|9:
                print(f"Количество: {quality} порций")
        print(f"Сумма: {(LIMONADE*quality)} рублей")
        print()
        match sale:
            case 'STUDENT':
                print()
                print(f"Скидка 'STUDENT' (20%): -{(20 * 200)//100} рублей")
        print("_"*36)
        print(f"💰 К оплате: {(LIMONADE*quality)-((20 * 200)//100)}")
        print("_"*36)

    case 2:
        print("|", " "*5, "☕ Квитанция Кафе ☕", " "*5, "|")
        print("_"*36)
        print()
        print("Товар: Кофе ☕")
        print(f"Цена за порцию: {COFFEE}")
        match quality:
            case 1:
                print(f"Количество: {quality} порция")
            case 2|3|4:
                print(f"Количество: {quality} порции")
            case 5|6|7|8|9:
                print(f"Количество: {quality} порций")
        print(f"Сумма: {(COFFEE*quality)} рублей")
        print()
        match sale:
            case 'STUDENT':
                print()
                print(f"Скидка 'STUDENT' (20%): -{(20 * 150)//100} рублей")
        print("_"*36)
        print(f"💰 К оплате: {(COFFEE*quality)-((20 * 150)//100)}")
        print("_"*36)

    case 3:
        print("|", " "*5, "💦 Квитанция Кафе 💦", " "*5, "|")
        print("_"*36)
        print()
        print("Товар: Вода 💦")
        print(f"Цена за порцию: {WATER}")
        match quality:
            case 1:
                print(f"Количество: {quality} порция")
            case 2|3|4:
                print(f"Количество: {quality} порции")
            case 5|6|7|8|9:
                print(f"Количество: {quality} порций")
        print(f"Сумма: {(WATER*quality)} рублей")
        print()
        match sale:
            case 'STUDENT':
                print()
                print(f"Скидка 'STUDENT' (20%): -{(20 * 50)//100} рублей")
        print("_"*36)
        print(f"💰 К оплате: {(WATER*quality)-((20 * 50)//100)}")
        print("_"*36)    
    
    case 4:
        print("|", " "*5, "🍵 Квитанция Кафе 🍵", " "*5, "|")
        print("_"*36)
        print()
        print("Товар: Чай 🍵")
        print(f"Цена за порцию: {TEA}")
        match quality:
            case 1:
                print(f"Количество: {quality} порция")
            case 2|3|4:
                print(f"Количество: {quality} порции")
            case 5|6|7|8|9:
                print(f"Количество: {quality} порций")
        print(f"Сумма: {(TEA*quality)} рублей")
        print()
        match sale:
            case 'STUDENT':
                print()
                print(f"Скидка 'STUDENT' (20%): -{(20 * 100)//100} рублей")
        print("_"*36)
        print(f"💰 К оплате: {(TEA*quality)-((20 * 100)//100)}")
        print("_"*36)    
    
    case 5:
        print("|", " "*5, "🥤 Квитанция Кафе 🥤", " "*5, "|")
        print("_"*36)
        print()
        print("Товар: Сок 🥤")
        print(f"Цена за порцию: {JUICE}")
        match quality:
            case 1:
                print(f"Количество: {quality} порция")
            case 2|3|4:
                print(f"Количество: {quality} порции")
            case 5|6|7|8|9:
                print(f"Количество: {quality} порций")
        print(f"Сумма: {(JUICE*quality)} рублей")
        print()
        match sale:
            case 'STUDENT':
                print()
                print(f"Скидка 'STUDENT' (20%): -{(20 * 200)//100} рублей")
        print("_"*36)
        print(f"💰 К оплате: {(JUICE*quality)-((20 * 200)//100)}")
        print("_"*36)    
    
    