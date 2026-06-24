class Inventory:
    def __init__(self, gold):
        self.__gold = gold

    def get_gold(self):
        print(f"В кошеле: {self.__gold} проклятых монет")
        return self.__gold
    
    def change_gold(self, amount):
        if amount > 0:
            self.__gold += amount
            print(f"Сумма монет составляет {self.__gold}")
        else:
            if self.__gold + amount >= 0:  
                self.__gold += amount  
                print(f"Сумма монет составляет {self.__gold}")
            if self.__gold + amount < 0:
                print(f"Операция отменена, текущее кол-во средств: {self.__gold}")
bag = Inventory(300)
print (bag.get_gold())
bag.change_gold(90)
bag.change_gold(-390)
bag.change_gold(-390)