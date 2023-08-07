from coffee import Coffee

class BlackCoffee(Coffee):
    def __init__(self, size):
        super().__init__("hot", size)
        self.milk = False
        self.cold=False

    def __str__(self):
        return "Black Coffee - Type: {}, Size: {}, Price: taka{}".format(self.coffee_type, self.size, self.calculate_price())

class Mocha(Coffee):
    def __init__(self, size,mocha_type):
        super().__init__("hot", size)
        self.mocha_type = mocha_type

    def __str__(self):
        if self.mocha_type=="Ex":
            price_with_addition = self.calculate_price() + 100
            return "Mocha - Type: {},mocha_type :{}, Size: {}, Price: taka {}".format(self.coffee_type,self.mocha_type ,self.size,price_with_addition)

class Espresso(Coffee):
    def __init__(self, size):
        super().__init__("hot", size)
        self.milk = False
        self.cold=False

    def __str__(self):
        return "Black Coffee - Type: {}, Size: {}, Price: taka{}".format(self.coffee_type, self.size, self.calculate_price())


class Irish(Coffee):
    def __init__(self, size,irish_type):
        super().__init__("hot", size)
        self.irish_type =irish_type

    def __str__(self):
        if self.irish_type=="Ex":
            price_with_addition = self.calculate_price() + 100
            return "Irish - Type: {},irish_type :{}, Size: {}, Price: taka {}".format(self.coffee_type,self.irish_type ,self.size,price_with_addition)


class Cold(Coffee):
    def __init__(self, size):
        super().__init__("cold", size)
        self.milk = True
        self.cold=True

    def __str__(self):
        return "Cold Coffee - Type: {}, Size: {}, Price: taka {}".format(self.coffee_type, self.size, self.calculate_price())
