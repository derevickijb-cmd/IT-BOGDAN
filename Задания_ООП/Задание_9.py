class Vampire:
    def __init__(self, name, bloodlust):
        self.__name = name
        self.__bloodlust = bloodlust

    def get_bloodlust(self):
        return self.__bloodlust
    
    def set_bloodlust(self, value):
        if value < 0 or value > 100:
            print("Не может так быть, я сказал")
        else: 
            print(f"Жажда крови теперь: {self.__bloodlust}")

vampire = Vampire("Дракула", 50)
print(vampire.get_bloodlust())
vampire.set_bloodlust(1000)


