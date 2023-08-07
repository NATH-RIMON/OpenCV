class coffee:
    def __init__(self,coffeeType,coffeeSize):

        self.coffeeType=coffeeType
        self.coffeeSize=coffeeSize

    def get_calculate(self):
        if self.coffeeSize=="small" and self.coffeeType=="hot":
            price=80
            return price
        elif self.coffeeSize=="small" and self.coffeeType=="cold":
            price=70
            return price
        
        elif self.coffeeSize=="medium" and self.coffeeType=="hot":
            price=100
            return price
        
        elif self.coffeeSize=="medium" and self.coffeeType=="cold":
            price=110
            return price
        
        elif self.coffeeSize=="large" and self.coffeeType=="hot":
            price=150
            return price
        
        elif self.coffeeSize=="large" and self.coffeeType=="cold":
            price=180
            return price
        
        else:
            return "Have a good Day"
        
class BlackCoffee(coffee):
    def __init__(self, coffeeType, coffeeSize):
        super().__init__(coffeeType, coffeeSize)

class Latte(coffee):
    def __init__(self, coffeeType, coffeeSize):
        super().__init__(coffeeType, coffeeSize)

    @staticmethod
    def add_steam_milk():
        print("steam Milk added")

    

        
order=coffee("","")
print(order.get_calculate())
        


        
    