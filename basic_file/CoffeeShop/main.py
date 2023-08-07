from coffee import Coffee

def get_coffee_type():
    while True:
        coffee_type = input("Enter coffee type (black/espresso/mocha/irish/redeye/cold): ").lower()
        if coffee_type in ["black", "espresso", "mocha", "irish","redeye","cold"]:
            return coffee_type

        print("Invalid coffee type. Please choose from black, espresso, mocha,irish,redeye,cold")

def get_coffee_size():
    while True:
        coffee_size = input("Enter coffee size (small/medium/large): ").lower()
        if coffee_size in ["small", "medium", "large"]:
            return coffee_size
        print("Invalid coffee size. Please choose from small, medium, or large.")

if __name__ == "__main__":
    coffee_type = get_coffee_type()
    coffee_size = get_coffee_size()

    if coffee_type in ["mocha","espresso","irish","redeye","cold"]:
        
        price = Coffee.calculate_coffee_price(coffee_type, coffee_size)
        print(f"Price: {price} taka")

    elif coffee_type in ["black"]:
        
        price = Coffee.calculate_price(coffee_type, coffee_size)
        print(f"Price: {price} taka")
    else:
        print("Invalid coffee type selected.")
