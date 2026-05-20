first_num = int(input("Введите число больше или равное 2: "))
next_nums = int(input("напишите число натуральных чисел: "))

for i in range(first_num, next_nums+1, 2):
        second_num = next_nums - 2 
        print (i)
print(next_nums, second_num)
