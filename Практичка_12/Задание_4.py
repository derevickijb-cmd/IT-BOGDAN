marks = [5, 4, 3, 5, 2, 5, 4, 3, 5, 5,]
marks_5 = 0
marks_2 = 0

for i in (marks):
    if i == 5:
        marks_5 += 1
    if i == 2:
        marks_2 += 1

print(f"Количество пятерок: {marks_5}\nКоличество двоек: {marks_2}")
    