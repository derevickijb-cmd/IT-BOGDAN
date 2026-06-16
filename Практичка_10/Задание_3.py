max_number = 0

while True:
    num = int(input("введите число"))

    if num == 0:
        break

    number = int(num)

    if number > max_number:
        max_number = number

print("Самое большое число это", max_number)
