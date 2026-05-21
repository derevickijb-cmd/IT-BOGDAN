
success = False
for n in range(1, 13):
    for k in range(1, 13):
        for m in range(1, 13):
            if 28*n + 30*k + 31*m == 365:
                print(f"Решение: n = {n}, k = {k}, m = {m}")
                print(f"вот решение нашего уравнения: 28*{n} + 30*{k} + 31*{m} = {28*n} + {30*k} + {31*m} = {(28*n) + (30*k) + (31*m)}\n")
                success = True
                if n == 1:  # первое решение с n=1
                    print(">>> Это решение с наименьшим значением n = 1\n")
                    
if not success:
    print("Натуральных решений не найдено!")