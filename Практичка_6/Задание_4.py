cell1, column1 = map(int, input("Введите номер клетки и столбца(от 1 до 8): ").split())
cell2, column2 = map(int, input("Введите ёше номер клетки и столбца(от 1 до 8): ").split())
if ((cell1 - column1) - (cell2 - column2)) % 2 == 0:
    print ("YES")

elif column1 == column2:
    print ("NO")
elif cell1 == cell2:
    print("NO")
else:
    print("NO")
