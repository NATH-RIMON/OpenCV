class Coffee:
    def __init__(self, coffee_type, size, milk=True):
        self.coffee_type = coffee_type.lower()
        self.size = size.lower()
        self.milk = milk

    def calculate_price(self):
        base_prices = {
            "black": {
                "small": 2.0,
                "medium": 3.0,
                "large": 4.0
            },
            "mocha": {
                "small": 3.0,
                "medium": 4.0,
                "large": 5.0
            }
        }

        mocha_types = {
            "espresso": 1.5,
            "chocolate": 2.0,
            "steamed milk": 1.0
        }

        base_price = base_prices.get(self.coffee_type, {}).get(self.size, 0)

        if base_price == 0:
            print("Invalid coffee size or type.")
            return None

        if self.coffee_type == "mocha" and self.milk:
            mocha_type_price = mocha_types.get(input("Enter mocha type (espresso/chocolate/steamed milk): ").lower(), 0)
            if mocha_type_price == 0:
                print("Invalid mocha type.")
                return None
            base_price += mocha_type_price

        return base_price
