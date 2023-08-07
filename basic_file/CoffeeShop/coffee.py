class Coffee:
    def __init__(self, coffee_type, size):
        self.coffee_type = coffee_type.lower()
        self.size = size.lower()
        

    def calculate_price(coffee_type, size, milk=False):
        base_prices = {
            "black": {
                "small": 100.0,
                "medium": 120.0,
                "large": 150.0
            }

        }

        base_price = base_prices.get(coffee_type, {}).get(size, None)

        if base_price is None:
            print("Invalid coffee size or type.")
            return 0.0

        

        return base_price


    def calculate_coffee_price(coffee_type, size, milk=True):
        base_prices = {
          
            "mocha": {
                "small": 120.0,
                "medium": 130.0,
                "large": 140.0
            },
            "espresso": {
                "small": 140.0,
                "medium": 150.0,
                "large": 180.0
            },
            "irish": {
                "small": 100.0,
                "medium": 110.0,
                "large": 120.0
            },
        
            "redeye": {
                "small": 140.0,
                "medium": 150.0,
                "large": 160.0
            },

            "cold": {
                "small": 100.0,
                "medium": 120.0,
                "large": 130.0
            },
        }

        mocha_types = {
            "espresso": 20,
            "chocolate": 30.0,
            "steamed milk": 25.0
        }

        irish_types = {
            "coffee": 15,
            "wishkey": 20.0,
            "sugar": 10.0,
            "cream":30,
        }

        redeye_types={
             "coffee": 30,
            "espresso": 20.0,
        }


        base_price = base_prices.get(coffee_type, {}).get(size, None)

        if base_price is None:
            print("Invalid coffee size or type.")
            return 0.0

        if coffee_type == "mocha" and milk:
            mocha_type_price = mocha_types.get(input("Enter mocha type (espresso/chocolate/steamed milk): ").lower(), None)
            if mocha_type_price is None:
                print("Invalid mocha type.")
                return 0.0
            base_price += mocha_type_price
        
        elif coffee_type =="espresso" and milk:
                return base_price
        
        elif coffee_type == "irish" and milk:
                irish_type_price = irish_types.get(input("Enter irish type (coffee/wishkey/sugar/cream): ").lower(), None)
                if irish_type_price is None:
                    print("Invalid espresso type.")
                    return 0.0
                base_price += irish_type_price

        elif coffee_type == "redeye" and milk:
                redeye_type_price = redeye_types.get(input("Enter irish type (coffee/espresso): ").lower(), None)
                if redeye_type_price is None:
                    print("Invalid redeye type.")
                    return 0.0
                base_price += redeye_type_price

        elif coffee_type =="cold" and milk:
                return base_price

        

        return base_price
