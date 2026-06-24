class Monster:
    def __init__ (self, name = "Неизвестная тварь", hp = 90, dg = 20):
        self.name = "Зомби"
        self.hp = hp 
        self.dg = dg

    def bite(self):
        self.bite = int(input("Введите силу укуса: "))
        self.hp -= self.bite
        print(self.hp)
        return(self.hp)
        
m = Monster("Мясник", 90, 20)
m.bite()
