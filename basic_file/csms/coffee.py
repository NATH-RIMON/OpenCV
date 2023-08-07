class Coffee:
    def __init__(self, coffee_type, size):
        self.coffee_type = coffee_type
        self.size = size
        self.base_prices = {
            "hot": {
                "small": 2.0,
                "medium": 2.5,
                "large": 3.0,
            },
            "cold": {
                "small": 2.5,
                "medium": 3.0,
                "large": 3.5,
            }
        }

    def calculate_price(self):
        if self.coffee_type in self.base_prices and self.size in self.base_prices[self.coffee_type]:
            return self.base_prices[self.coffee_type][self.size]
        else:
            raise ValueError("Invalid coffee type or size")
