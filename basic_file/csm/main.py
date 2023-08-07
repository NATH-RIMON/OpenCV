from coffee_types import BlackCoffee, Mocha

# Function to get valid user input for coffee size
def get_coffee_size():
    while True:
        coffee_size = input("Enter coffee size (small/medium/large): ").lower()
        if coffee_size in ["small", "medium", "large"]:
            return coffee_size
        print("Invalid coffee size. Please choose from small, medium, or large.")

# Create instances and call methods based on user input
if __name__ == "__main__":
    coffee_size = get_coffee_size()

    coffee_classes = {
        "black": BlackCoffee,
        "mocha": Mocha
    }

    coffee_type = input("Enter coffee type (black/mocha): ").lower()
    if coffee_type not in coffee_classes:
        print("Invalid coffee type selected.")
    else:
        milk_preference = input("Do you want milk in your coffee? (yes/no): ").lower() == "yes"
        coffee_class = coffee_classes[coffee_type]
        coffee = coffee_class(coffee_size, milk_preference)
        print(coffee)
