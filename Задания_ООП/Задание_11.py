class Werewolf:
    def __init__(self, name = "Гриша", form = "Человек", power = 15):
        self.__name = name
        self.__form = form
        self.__power = power
    
    def get_status(self):
        print(f"{self.__name} сейчас является: {self.__form}")
        return self.__form
    
    def transform(self):
        if self.__form == "Человек":
            self.__form = "Оборотень"
            self.__power == 45
            print(f"{self.__name} обрастает шерстью!")
        if self.__form ==  "Оборотень":
            self.__form = "Человек"
            self.__power == 15
            print(f"{self.__name} перевоплатился в человека!")

wolf = Werewolf()
print("=== ТЕСТИРОВАНИЕ ===")
wolf.get_status()      # Гриша сейчас является: Человек
wolf.transform()       # Гриша обрастает шерстью!
wolf.get_status()      # Гриша сейчас является: Оборотень
wolf.transform()       # Гриша перевоплотился в человека!
wolf.get_status()      # Гриша сейчас является: Человек