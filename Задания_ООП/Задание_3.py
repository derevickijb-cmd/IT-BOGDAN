class Monster:
    def __init__ (self, name, hp , dg):
        self.name = name
        self.hp = hp 
        self.dg = dg
        print(f"монстр: \n Имя: {self.name}\n Здоровье: {self.hp} \n Дамаг: {self.dg}")
        
name1, hp1, dg1 = input("Введите пожалуйста характеристики первого монстра").split( )
name2, hp2, dg2 = input("Введите пожалуйста характеристики второго монстра").split( )

m1 = Monster(name1, int(hp1), int(dg1))
m2 = Monster(name2, int(hp2), int(dg2))

while True:
    print (f"Монстр {m1.name} наносит удар!")
    m2.hp -= m1.dg
    if m2.hp > 0:
        print(f"Монстр {m2.name} отняли {m1.dg}, осталось {m2.hp}")
    if m2.hp < 0:
        print(f"Монстр {m2.name} проиграл!")
        break 

    print (f"Монстр {m2.name} наносит удар!")
    m1.hp -= m2.dg
    if m1.hp > 0:
        print(f"Монстру {m1.name} отняли {m2.dg}, осталось {m1.hp}")
    if m2.hp <= 0:
        print(f"Монстр {m1.name} проиграл!")
        break 