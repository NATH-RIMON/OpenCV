class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer=0

    def get_description_name(self):
        long_time=f"{self.year} {self.model} {self.year}"
        return long_time
    
    def run_car(self):
        print("This Car is Running")
        self.odometer+=10

    def read_odometer(self):
        print(f"The car has {self.odometer} miles on it")


my_new_car=Car("Lexus","570x",2020)

my_new_car.read_odometer()
my_new_car.run_car()
my_new_car.read_odometer()
