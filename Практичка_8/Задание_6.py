import random
secret_num = random.randint(1, 10)

for i in range(1, 4):
    number = int(input("У вас есть три попытки угадать число от 1 до 10 "))
    if i >= 3:
        print("Вы исчерпали все попытки")
        break
    if number != secret_num:
        if number > secret_num:
           print("Неверно, загаданное число меньше") 
        elif number < secret_num:
           print("Неверно, загаданное число больше")
    elif number == secret_num:
        print("Верно! Ты победил!")
        break
    if i >= 3:
        print("Вы исчерпали все попытки")