class Monster:
    def __init__ (self, name = "Неизвестная тварь", hp = 100, dg = 10):
        self.name = name
        self.hp = hp 
        self.dg = dg
        

    def show_info(self):
        print ("-------------Статус монстра-------------")
        print(f"Имя монстра: <{self.name}>")
        print(f"Здоровье: <{self.hp}>")
        print(f"Дамаг:<{self.dg}>")
        print ("----------------------------------------")  


m1 = Monster("Горгулья", 120, 18)
m1.show_info()
