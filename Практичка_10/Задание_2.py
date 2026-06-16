while True:
    first_num = int(input("Введите первое число"))
    second_num = int(input("Введите второе число"))
    if first_num >= second_num:
        print("Ошибка. Пожалуйста, введите второе число заново")
        second_num = int(input("Введите второе число"))
    third_num = int(input("Введите третье число"))
    if second_num >= third_num:
        print("Ошибка. Пожалуйста, введите третье число заново")
        third_num = int(input("Введите третье число"))
    break
