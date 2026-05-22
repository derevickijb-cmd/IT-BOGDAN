number = int(input("Напшите любое натуральное число: "))
#переменная original нужна для 
num_3 = 0
last_digit = number % 10 
last_num = 0
more_5 = 0
more_7 = 1
even_num = 0
num_05 = 0
while number > 0:
    digit = number % 10

    i = 0    
    while i < 1:
        if digit == 3:
            num_3 += 1
       
        if digit == last_digit:
            last_num += 1 

        if digit % 2 == 0:
            even_num += 1
        
        if digit > 5:
            more_5 += digit

        if digit > 7:
            more_7 *= digit
            if digit < 7:
                more_7 += 0

        if digit == 0 or digit == 5:
            num_05 += 1
        i += 1
    number //= 10
print (f"\nКоличество троек: {num_3}  \nКоличество цифр как последняя: {last_num} \nКоличество четных цифр: {even_num}")
print (f"Сумма цифр, больших пяти: {more_5} \nПроизведение цифр, больших семи: {more_7} \nКоличество цифр пяти и ноль: {num_05} ")