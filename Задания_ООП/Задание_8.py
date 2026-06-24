class DarkEntinity:
    def __init__(self, name, species, danger_level):
        self.__name = name
        self.__species = species 
        self.__danger_level = danger_level
    def get_hp(self):
        return self.__name
    
    def get_species(self):
        return self.__species
    
    def get_danger_level(self):
        return self.__danger_level
    

boss = DarkEntinity("Балор", "Высший Демон", 99)
print(f"Данные из Гримуара: {boss.get_hp()}, {boss.get_species()}, {boss.get_danger_level()}")
