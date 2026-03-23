""" class hero:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory

    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)

Louis= hero("Louis",100,["Doordash Gift Card"])
Louis.buy({"title": "Fried Chicken", "hunger": 50})
print(Louis.__dict__) """


class Pet:
    def __init__(self,name,happiness):
        self.name = name
        self.__happiness = int(happiness)
    def play(self, playtime):
        playtime = int(input("How Much do you play?"))
        self.__happiness += playtime
    def showmentality(self):
        if self.__happiness > 0:
            print(f"{self.name} has {self.__happiness}, and is very happy. Good Job!")
        elif self.__happiness < 0:
            print(f"{self.name}has {self.__happiness} and is not very happy. Do Something you chud")

BarffaceMcChuckleLampport = Pet

