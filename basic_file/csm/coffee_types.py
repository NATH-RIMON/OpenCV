from coffee import Coffee

class BlackCoffee(Coffee):
    def __init__(self, size):
        super().__init__("black", size, milk=False)  # Set milk=False for black coffee

    def __str__(self):
        milk_status = "With Milk" if self.milk else "Without Milk"
        return "Black Coffee - Type: {}, Size: {}, Milk: {}, Price: ${}".format(
            self.coffee_type, self.size, milk_status, self.calculate_price())

class Mocha(Coffee):
    def __init__(self, size, milk=True):
        super().__init__("mocha", size, milk)

    def __str__(self):
        return "Mocha - Type: {}, Size: {}, Price: ${}".format(self.coffee_type, self.size, self.calculate_price())
