from coffee_types import BlackCoffee, Espresso, Mocha, IcedCoffee


def get_coffee_type():
    while True:
        coffee_type = input("Enter coffee type (black/espresso/mocha/iced): ").lower()
        if coffee_type in ["black", "espresso", "mocha", "iced"]:
            return coffee_type
        print("Invalid coffee type. Please choose from black, espresso, mocha, or iced.")

# Function to get valid user input for coffee size
def get_coffee_size():
    while True:
        coffee_size = input("Enter coffee size (small/medium/large): ").lower()
        if coffee_size in ["small", "medium", "large"]:
            return coffee_size
        print("Invalid coffee size. Please choose from small, medium, or large.")

# Create instances and call methods based on user input
if __name__ == "__main__":
    coffee_type = get_coffee_type()
    coffee_size = get_coffee_size()

    if coffee_type == "black":
        coffee = BlackCoffee(coffee_size)
    elif coffee_type == "espresso":
        coffee = Espresso(coffee_size)
    elif coffee_type == "mocha":
        coffee = Mocha(coffee_size)
    elif coffee_type == "iced":
        coffee = IcedCoffee(coffee_size)

    print(coffee)
from coffee_types import BlackCoffee, Espresso, Mocha, IcedCoffee


def get_coffee_type():
    while True:
        coffee_type = input("Enter coffee type (black/espresso/mocha/iced): ").lower()
        if coffee_type in ["black", "espresso", "mocha", "iced"]:
            return coffee_type
        print("Invalid coffee type. Please choose from black, espresso, mocha, or iced.")

# Function to get valid user input for coffee size
def get_coffee_size():
    while True:
        coffee_size = input("Enter coffee size (small/medium/large): ").lower()
        if coffee_size in ["small", "medium", "large"]:
            return coffee_size
        print("Invalid coffee size. Please choose from small, medium, or large.")

# Create instances and call methods based on user input
if __name__ == "__main__":
    coffee_type = get_coffee_type()
    coffee_size = get_coffee_size()

    if coffee_type == "black":
        coffee = BlackCoffee(coffee_size)
    elif coffee_type == "espresso":
        coffee = Espresso(coffee_size)
    elif coffee_type == "mocha":
        coffee = Mocha(coffee_size)
    elif coffee_type == "iced":
        coffee = IcedCoffee(coffee_size)

    print(coffee)
