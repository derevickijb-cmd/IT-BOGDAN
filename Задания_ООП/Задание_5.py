class Monster:
    def __init__(self, name):
        self.name = name

    def introduce(self): #name это всего лишь атрибут, а self это ссылка на объект. Если мы 
        #не вставим в introduce 'self',  объект не будет передаваться в метод introduce.
        print(f"Я {self.name}, и я хочу кушать!")

m = Monster("Упырь")
m.introduce()

