N = int(input())
items = list(map(int, input().split()))

#Сортируем по убыванию
items.sort(reverse=True)

#Суммируем N самых ценных предметов
max_sum = 0
for i in range(min(N, len(items))):
    max_sum += items[i]

print(max_sum)
