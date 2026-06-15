ip_string = input()
parts = ip_string.split('.')

if len(parts) != 4:
    print("НЕТ")
else:
    valid = True
    for part in parts:
        # Проверяем, что каждый символ - цифра
        for character in part:
            if character < '0' or character > '9':
                valid = False
                break
        if not valid:
            break
        num = int(part)
        if num < 0 or num > 255:
            valid = False
            break
    
    print("ДА" if valid else "НЕТ")