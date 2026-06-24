class Monster:
    def __init__ (self, name = "Неизвестная тварь", hp = 90, power = 15):
        self.name = name
        self.hp = hp 
        self.power = power
    def mutate(self):
        print(f"{self.name} мутирует! Сила увеличина!")
        print(f"Сила: {self.power+5} ")
    def rest(self):
        print(f"{self.name} отдыхает в склепе! Здоровье восстановлено!")
        print(f"Здоровье: {self.hp+10} ")
lucan = Monster("Люкан", 90, 15)
lucan.mutate()
lucan.rest()