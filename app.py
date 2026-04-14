import random
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
        self.__happiness = happiness
        test =int(input(f"How much do you like your pet {name}, from a scale of 1 to 100?"))
        if test > 100:
            print("lies")
            happiness == -100000000000
        elif test < 100:
            test % 2 
            if test % 2 == float:
                test += 0.5
            happiness += test
            test += happiness
         
    def play(self):
        playtime=0
        random_int = random.randint(1, 10)
        playing=int
        while playing != random_int:
            playing=int(input("Guess the Number to increase happiness!"))
            if playing != random_int:
                playtime -= 10
                print("try again")
                if playing >= random_int:
                    print("Too High")
                elif playing <= random_int:
                    print("Too Low")
            elif playing == random_int:
                playtime += 100
                print("Good Job")
        
        retry = input("Do you want to try again?")
        if retry == "Yes":
                print("Run it Back!")
                randomint = random.randint(1,100)
                playingpt2=int
                while playingpt2 != randomint:
                    playingpt2=int(input("Guess the Number to increase happiness! 1 to 100!"))
                    if playingpt2 == randomint:
                        playtime += 5000
                        print("Good Job")
                    else :
                        playtime -= 250
                        print("try again")
                        if playingpt2 >= randomint:
                            print("Too High")
                        elif playingpt2 <= randomint:
                            print("Too Low")
        elif retry == "No":
                self.__happiness += playtime
        self.__happiness += playtime
    def showmentality(self):
        if self.__happiness > 0:
            print(f"{self.name} has {self.__happiness} happiness, and is happy. Good Job!")
        elif self.__happiness > 100:
            print(f"{self.name} has {self.__happiness} happiness, and is very happy. Good Job!")
        elif self.__happiness > 1000:
            print(f"Wow!{self.name} has {self.__happiness}happiness, and is extremely happy. Excellent work")
        elif self.__happiness < 0:
            print(f"{self.name} has {self.__happiness} happiness, and is not very happy. Do Something you chud")
        


pet=Pet("fatty",0)
pet.play()
pet.showmentality()



