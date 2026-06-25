class Monster:
    def __init__ (self, name, hp, dmg):
        self.__name = name
        self.__hp = hp
        self.__dmg = dmg
    
    def take_damage(self, damage):
        self.__hp -= damage
        if self.__hp < 0:
            self.__hp = 0
        print(f"{self.__name} получил {damage} урона. Осталось HP: {self.__hp}")
        return self.__hp

    def attack_hunter(self, hunter):
        print(f"{self.__name} атакует {hunter.get_name()}!")
        hunter.take_damage(self.__dmg)

    def get_name(self):
        return self.__name
    
    def get_hp(self):
        return self.__hp
    
    def get_dmg(self):
        return self.__dmg
    
    def set_hp(self, value):
        if value < 0:
            self.__hp = 0
            
    def is_alive(self):
        if self.__hp > 0:
            return True
        else:
            return False
        
    def show_status(self):
        print("-------Статус-------")
        print(f"Имя: {self.__name}")
        print(f"Здоровье: {self.__hp}")
        print("--------------------")

    #Второй этап игры:
"""class Zombie(Monster):
    def __init__(self):
        super().__init__(name="Zombie", hp=120, dmg=10)"""

class Vampire(Monster):
    def __init__(self):
        super().__init__(name="Vampire", hp=80, dmg=10)

    def take_damage(self, damage):
        super().take_damage = damage
        damage -= 5
        print(f"Вампир поглотил 5 урона! а получает он всего {damage} урона")
        return damage

m1 = Vampire()
m1.take_damage(45)

"""class Ghost(Monster):
    def __init__(self):
        super().__init__(name="Ghost", hp=60 dmg=10)

    def take_damage(self, damage):

class Werewolf(Monster):
    def __init__(self):
        super().__init__(name="Werewolf", hp=100, dmg=10)
    
    def take_damage(self, damage):"""
