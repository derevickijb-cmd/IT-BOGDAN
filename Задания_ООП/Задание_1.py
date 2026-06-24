class Monster:
    def __init__ (self, name = "Неизвестная тварь", hp = 100, damage = 10):
        self.name = name
        self.hp = hp 
        self.damage = damage
        print(f"монстр: \n Имя: {self.name}\n Здоровье: {self.hp} \n Дамаг: {self.damage}")
        print()
        

m1 = (f"Первый монстр: \n {Monster("Дракула", 120, 35)}")
m2 = Monster("Люкан", 100, 40)