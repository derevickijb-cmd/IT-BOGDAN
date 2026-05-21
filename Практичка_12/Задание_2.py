success = False

for num in range(1, 151):
    for num1 in range(1, 151):
        for num2 in range(1, 151):
            for num3 in range(1, 151):
                for num4 in range(1, 151):
                    sum_abcd = num**5 + num1**5 + num2**5 + num3**5
                    if num4**5 == sum_abcd:
                        success = True
                        print(f"По итогу получилось такое уравнение: {num}**5 + {num1}**5 + {num2}**5 + {num3}**5 == {num4}**5")

                   