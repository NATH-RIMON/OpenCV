from coffee import Coffee

class BlackCoffee(Coffee):
    def __init__(self, size):
        super().__init__("hot", size)
        self.milk = False

    def __str__(self):
        return "Black Coffee - Type: {}, Size: {}, Price: ${}".format(self.coffee_type, self.size, self.calculate_price())


class Espresso(Coffee):
    def __init__(self, size):
        super().__init__("hot", size)
        self.shot_count = 1

    def __str__(self):
        return "Espresso - Type: {}, Size: {}, Price: ${}".format(self.coffee_type, self.size, self.calculate_price())


class Mocha(Coffee):
    def __init__(self, size):
        super().__init__("hot", size)
        self.chocolate_syrup = True

    def __str__(self):
        return "Mocha - Type: {}, Size: {}, Price: ${}".format(self.coffee_type, self.size, self.calculate_price())


class IcedCoffee(Coffee):
    def __init__(self, size):
        super().__init__("cold", size)
        self.ice_cubes = True

    def __str__(self):
        return "Iced Coffee - Type: {}, Size: {}, Price: ${}".format(self.coffee_type, self.size, self.calculate_price())
