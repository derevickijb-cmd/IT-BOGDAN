class Monster:
    def __init__ (self, name = "Неизвестная тварь", hp = 100, damage = 10):
        self.name = name
        self.hp = hp 
        self.damage = damage
        print(f"монстр: \n Имя: {self.name}\n Здоровье: {self.hp} \n Дамаг: {self.damage}")
        
name1, hp1, damage1 = input("Введите пожалуйста характеристики первого монстра").split( )
name2, hp2, damage2 = input("Введите пожалуйста характеристики второго монстра").split( )

m1 = Monster(name1, hp1, damage1)
m2 = Monster(name2, hp2, damage2)